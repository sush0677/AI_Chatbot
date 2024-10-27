AI Chatbot

An AI-powered chatbot built using PyTorch that understands and responds to user queries based on predefined intents. This chatbot classifies input text into specific categories and generates relevant responses, making it adaptable for a variety of applications, from customer service to personal assistance.

Features

Intent Classification: Uses a feedforward neural network to categorize user messages based on intent.

Customizable Responses: Each intent is paired with multiple potential responses, allowing for varied interactions.

Confidence-Based Replying: Only responds if the confidence level of the intent classification is high; otherwise, it displays a fallback message.


How It Works

1. Data Preprocessing: Loads intents and patterns from intents.json, tokenizes and processes text into a bag-of-words format.


2. Model Training: A neural network model is trained to recognize patterns and predict intents. The training data is saved to data.pth.


3. Real-Time Inference: When deployed, the model processes new user input, identifies the most likely intent, and responds accordingly.



Project Structure

intents.json: Defines intents, patterns, and responses.

model.py: Contains the neural network model (a simple feedforward network).

nltk_utilities.py: Provides helper functions for tokenizing text, stemming words, and creating bag-of-words vectors.

data.pth: Stores trained model parameters and data for quick deployment.

chatbot.py: Main script for interacting with the chatbot.


Getting Started

Prerequisites

Python 3.6+

PyTorch

NLTK


Installation

1. Clone this repository:

git clone https://github.com/sush0677 /AI-Chatbot.git
cd AI-Chatbot


2. Install the required libraries:

pip install torch nltk


3. Download NLTK resources:

import nltk
nltk.download('punkt')



Training the Model

To train the model, run the train.py script, which will generate data.pth to save the trained model’s parameters:

python train.py

Running the Chatbot

To start chatting with the bot, run:

python chatbot.py

Type your message, and the bot will respond based on the highest-confidence intent. Type quit to exit.

Example Interaction

You: Hello
Bot: Hi there! How can I assist you today?

Customization

To add new intents, update the intents.json file with new patterns and responses. You can retrain the model after making these changes.

Future Enhancements

Integrate with a web or mobile app for a more interactive experience.

Add support for more complex NLP techniques like word embeddings.

Improve the model by experimenting with different neural network architectures.
