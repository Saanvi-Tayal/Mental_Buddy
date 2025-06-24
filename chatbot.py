from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.tokenize import word_tokenize
import logging
from peft import PeftModel
import re

logging.basicConfig(filename='logs/chatbot_logs.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot_small-90M")
# model = AutoModelForSeq2SeqLM.from_pretrained("./model")
model = PeftModel.from_pretrained(base_model, "saanvitayal/mental_buddy")

sia = SentimentIntensityAnalyzer()

empathetic_responses = {}
with open("response.txt", "r") as f:
    for line in f:
        if ":" in line:
            key, value = line.strip().split(": ", 1)
            empathetic_responses[key] = value

def detect_crisis(text):
    crisis_keywords = ["suicide", "kill myself", "end my life", "hopeless"]
    return any(keyword in text.lower() for keyword in crisis_keywords)


def get_chatbot_response(user_input):
    # Log user input (anonymized)
    logging.info("User: {}".format(re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[email]', user_input)))
   
    if detect_crisis(user_input):
        response = empathetic_responses.get("crisis", "I’m not a professional, but I care. Please reach out to a helpline.")
        logging.info(f"Bot: {response}")
        return response
    
    sentiment = sia.polarity_scores(user_input)
    if sentiment['compound'] < -0.5:  # Negative sentiment
        for keyword in empathetic_responses:
            if keyword in user_input.lower():
                response = empathetic_responses[keyword]
                logging.info(f"Bot: {response}")
                return 
                

    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    logging.info(f"Bot: {response}")
    return response                

