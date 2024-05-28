# NLP App

This project is an NLP (Natural Language Processing) application built with Python and Tkinter. The application provides various NLP functionalities such as sentiment analysis, named entity recognition (NER), and emotion analysis. It also includes a user authentication system where users can register and log in.

## Features

- User Registration and Login
- Sentiment Analysis
- Named Entity Recognition (NER)
- Emotion Analysis

## Project Structure

The project consists of the following files:

- `nlp_app.py`: Contains the main application logic and GUI implementation using Tkinter.
- `mydb.py`: Contains the database class for handling user registration and login.
- `myapi.py`: Contains the API class for making requests to the NLP services.

## Classes

### NlpApp

This class initializes the main GUI of the application and includes methods for various functionalities such as login, registration, sentiment analysis, NER, and emotion analysis.

### API

This class handles the interaction with external NLP APIs. It includes methods for querying sentiment analysis, NER, and emotion analysis.

### database

This class handles the user registration and login functionalities using a JSON file (`db.json`) as a simple database.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (should be included with Python standard library)
- `requests` library for making HTTP requests

### Installing

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/your-username/nlp-app.git
    ```

2. Navigate to the project directory:

    ```sh
    cd nlp-app
    ```

3. Install the required packages:

    ```sh
    pip install requests
    ```

### Running the Application

1. Ensure you have a `db.json` file in the project directory. If it doesn't exist, create one with the following content:

    ```json
    {}
    ```

2. Run the `nlp_app.py` script to start the application:

    ```sh
    python nlp_app.py
    ```

### API Configuration

The application uses external APIs for NLP functionalities. Make sure to replace the placeholder API key in the `API` class with your actual API key.

## Usage

1. **Login/Register**: Users can register with their name, email, and password. Once registered, users can log in with their credentials.
2. **Sentiment Analysis**: Analyze the sentiment of a given text.
3. **Named Entity Recognition (NER)**: Identify named entities in a given text.
4. **Emotion Analysis**: Analyze the emotions present in a given text.
