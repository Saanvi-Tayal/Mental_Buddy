# AI Chatbot for Mental Health Support

This project is  web-based chatbot designed to provide empathetic responses and emotional support, tailored to teens' mental health. Built with Flask and powered by the BlenderBot model, it includes a custom dataset, sentiment analysis, input filtering, and session logging.

## Project Overview

- **Objective**: Create a safe, supportive chatbot with sentiment analysis to help teens express their feelings and receive tailored responses.
- **Features**:
  - Conversational AI using BlenderBot (Hugging Face Transformers).
  - Sentiment analysis to adjust responses based on user emotions.
  - Session logging for tracking interactions.
  - Web interface built with Flask, HTML, and CSS.
  - Custom dataset created specifically for teens' mental health.

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Hugging Face Transformers
- TextBlob (for NLP filtering)
- Requests (for API calls)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Saanvi-Tayal/Mental_Buddy.git
   cd Mental_Buddy      
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app locally:
   ```
   python app.py
   ```
   Open your browser and go to ` http://localhost:5001/`.

## Usage
- Enter a message in the chat interface.
- The chatbot uses BlenderBot via the Hugging Face API to respond empathetically, tailored to teens' mental health.
- Sentiment analysis adjusts the tone based on your input.
- Session logs are saved in a `logs/` directory.


## API Integration
- The BlenderBot model is uploaded to Hugging Face and accessed via their API.
- The Flask app sends user inputs to the API and processes the responses with sentiment analysis.

## Deployment
This project was deployed on Render, but a memory limit issue (exceeding 512MB) caused a failure. 


## Contributing
Feel free to fork this repo and submit pull requests! Ideas to improve the custom dataset, sentiment analysis, UI, or deployment are welcome.

## License
This project is open-source under the MIT License.

## Acknowledgments
- Hugging Face for the Transformers library, BlenderBot model, and API.
- Render for hosting the app.
- TextBlob for NLP filtering.

## Disclaimer
This chatbot is a personal project and not intended for medical use. For professional mental health support, please consult a licensed healthcare provider or counselor.