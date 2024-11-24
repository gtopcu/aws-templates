
# pip install langchain openai requests python-dotenv
# export OPENAI_API_KEY='your-api-key-here'

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import requests
from typing import Dict
import os

class WeatherApp:
    def __init__(self, openai_api_key: str):
        # Initialize the ChatGPT model
        self.chat_model = ChatOpenAI(
            model="gpt-4",
            openai_api_key=openai_api_key,
            temperature=0
        )
        
        # System message for the weather assistant
        self.system_message = SystemMessage(
            content="You are a weather app. Ask the user which city they want to learn about the weather. The temperature should be in celcius"
        )
        
        self.messages = [self.system_message]
    
    def get_city_from_user(self) -> str:
        """
        Use ChatGPT to interact with the user and get the city name
        """
        # Get response from ChatGPT
        response = self.chat_model(self.messages)
        self.messages.append(AIMessage(content=response.content))
        
        # Get user input
        user_input = input(f"ChatGPT: {response.content}\nYou: ")
        self.messages.append(HumanMessage(content=user_input))
        
        return user_input
    
    def get_weather_data(self, city: str) -> Dict:
        """
        Call the weather API to get weather data for the specified city
        """
        try:
            response = requests.get(f"http://localhost?city={city}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

def main():
    # Make sure to set your OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable")
    
    # Initialize the weather app
    weather_app = WeatherApp(openai_api_key)
    
    # Get city from user
    city = weather_app.get_city_from_user()
    
    # Get weather data
    weather_data = weather_app.get_weather_data(city)
    
    # Display results
    if weather_data:
        print(f"\nWeather data for {city}:")
        print(weather_data)
    else:
        print(f"\nUnable to fetch weather data for {city}")

if __name__ == "__main__":
    main()