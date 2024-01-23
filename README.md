
# Chatbot App with Clarifai Vision and GPT-4 Integration


https://github.com/SamiaAlshehri/health_down_syndrome_chatbot/assets/52881648/e5b397ca-9454-4d79-9efe-0321cd456657


## Overview
This Flask application serves as a simple chatbot utilizing the Clarifai Vision API and GPT-4 model for generating responses. 

It provides a basic web interface where users can input queries, and the application responds based on both a predefined dataset and GPT-4 model predictions.

## Features
- Utilizes Clarifai Vision API for image-related predictions.
- Fallback mechanism using GPT-4 model for questions not found in the dataset.
- Provides a simple web interface for user interaction.

## Prerequisites
- Python 3.8.10
- Flask3.0.1
- Pandas
- Clarifai Python SDK

## Getting Started
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

    Install dependencies:

    bash

pip install -r requirements.txt

Set up your Clarifai Personal Access Token (PAT) as an environment variable:

bash

export CLARIFAI_PAT='your-clarifai-pat'

Run the application:

bash

    python app.py

    Access the application at http://localhost:5000/.

Configuration

    Dataset: The application loads a CSV dataset from dataset/dataset.csv. Ensure your dataset is appropriately formatted.
    Clarifai PAT: Set your Clarifai PAT as an environment variable before running the application.

Usage

    Visit the web interface at http://localhost:5000/.
    Input your query in the provided field.
    Submit the form, and the application will respond based on the dataset or GPT-4 predictions.

Acknowledgments

    This project is powered by Clarifai Vision API and OpenAI's GPT-4 model.
    Dataset source: [Provide source or describe if applicable]
    Developed by Langchain Tech
