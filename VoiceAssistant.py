import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import random
import pyjokes
import time
import pyaudio
import sys
import python_weather
import asyncio
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

## Variables
voice_name = "Not Alexa"
engine.setProperty('voice', voices[1].id)
city_name = "Your City" # Set locality, for weather forecasting

# Defaults to values set in .env, if found.
voice_name = os.getenv('voice_name')
city_name = os.getenv('city_name')

## Functions
def check_voice_list():
    index = 0
    for voice in voices:
        print(f'index -> {index} -- {voice.name}')
        index +=1
#check_voice_list()

def talk(text):
    engine.say(text)

def talk_and_print(text):
    engine.say(text)
    print(text)

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout = 5)
            command = listener.recognize_google(voice, language='en-US')
            command = command.lower()
    except Exception as ex:
        print(ex)
        command = ''
        pass
    return command

def get_pa():
    rannum = random.randint(1, 3)
    greetings_list = [ 'I am here', 'Hello', 'I am listening' ]
    talk(random.choice(greetings_list))
    talk('How can I help?')

def it_crowd():
    talk('Have you tried turning it off and on again?')

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good morning!')
    elif hour >= 12 and hour < 17:
        talk('Good afternoon!')
    else:
        talk('Good evening.')

    engine.say('How can I help?')

async def getweather():
    # Declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # Fetch a weather forecast from a city
    weather = await client.find(city_name)

    talk_and_print('Weather forecast for: ' + str(city_name))

    # Returns the current day's forecast temperature (int)
    temp_now = str(weather.current.temperature)
    sky_now = str(weather.current.sky_text) # sunny, cloudy, etc.
    humid_now = str(weather.current.humidity)
    wind_now = str(weather.current.wind_speed)

    talk_and_print('The current temperature is ' + temp_now + ' degrees.')
    talk_and_print('It is ' + sky_now + ', ' + humid_now + ' percent humidity,' + 
        ' wind speed ' + wind_now + ' miles per hour')
    
    # Get the weather forecast for a few days
    for forecast in weather.forecasts:
        todays_date = datetime.today().strftime('%Y-%m-%d')
        if (str(forecast.date).find(todays_date) != -1):
            sky_forecast = str(forecast.sky_text)
            temp_high = str(forecast.high)
            precip_forecast = str(forecast.precip)
            talk_and_print('Today will be ' + sky_forecast + ' with a high of ' + temp_high + ' degrees, ' + 
                'and a ' + precip_forecast + ' percent chance of precipitation.')

    # Close the wrapper once done
    await client.close()

def run_pa(command):
    if command in ('today\'s date', 'what day is it'):
        todays_date = datetime.today().strftime('%B %d, %Y')
        day = datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 
                    5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        day_of_the_week = Day_dict[day]
        talk('Today is ' + day_of_the_week + ", " + todays_date)
    elif 'time' in command:
        time = datetime.now().strftime('%H:%M %p')
        talk('Current time is ' + time)
    elif 'tell' in command and 'joke' in command:
        talk('Ok, Here is a joke:')
        talk(pyjokes.get_joke())
    elif command in ('computer', 'is broken', 'problem with'):
        it_crowd()
    elif 'weather' in command:
        if 'forecast' in command:
            try:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweather())
            except Exception as ex:
                print('An error occurred fetching weather forecast data.')
                print(ex)
                traceback.print_exc()
                pass
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Searching for ' + song + ' on YouTube.')
        talk('Now playing first result for ' + song)
        pywhatkit.playonyt(song)
    elif command in ('who', 'what', 'where', 'when', 'why', 'how'):
        talk('I am searching Wikipedia for ' + command)
        question = command
        info = wikipedia.summary(question, 3)
        talk(info)
    elif command in ('thank you', 'thanks'):
        talk('You\'re welcome.')
    else:
        talk('Sorry I did not understand')

def main():
    wishMe()
    while True:
        engine.runAndWait()
        command = take_command()
        # command = input("Enter command: ")

        try:
            if command == 'exit' or command == 'quit':
                sys.exit()
            elif command == None or command == '':
                continue
            elif voice_name in command:
                get_pa()
            else:
                run_pa(command)
        except Exception as ex:
            traceback.print_exc()


if __name__ == "__main__":
    main()
