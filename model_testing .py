# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# from peft import PeftModel
# # bnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4")
# base_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot_small-90M")
# model = PeftModel.from_pretrained(base_model, "./model")
# tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot_small-90M")

# while True :
#     input_text =str(input("user: " ))
#     if input_text== "end":
#         break        
#     else:
#         inputs = tokenizer(input_text, return_tensors="pt")
#         outputs = model.generate(**inputs, max_length=100)
#         print("model:",  tokenizer.decode(outputs[0], skip_special_tokens=True))

from chatbot import get_chatbot_response
print(get_chatbot_response("I want to kill myself"))
print(get_chatbot_response("You’re stupid"))