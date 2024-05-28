import requests


class API:
    def __init__(self):
        self.base_url = "https://services.hyphenapi.com/api/"
        self.headers = {
            "Accept": "application/json",
            "x-api-key": "5ior-gnqb-omlk-oas7-d55l-o51f",  # Replace with your actual API key
            "Content-Type": "application/json"
        }

    def query(self, endpoint, payload):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def sentiment_analysis(self, text):
        payload = {"text": text}
        try:
            response = self.query("sentimental_analysis", payload)
            return response
        except Exception as e:
            print(f"Error occurred: {e}")
            return "Sentiment analysis failed due to unexpected error"

    def ner_analysis(self, text):
        payload = {"text": text}
        try:
            response = self.query("ner_analysis", payload)  # Adjust the endpoint as needed
            return response
        except Exception as e:
            print(f"Error occurred: {e}")
            return "NER analysis failed due to unexpected error"

    def emotion_analysis(self, text):
        payload = {"text": text}
        try:
            response = self.query("emotional_analysis", payload)  # Adjust the endpoint as needed
            return response
        except Exception as e:
            print(f"Error occurred: {e}")
            return "Emotion analysis failed due to unexpected error"
