import streamlit as st
import random
import requests
from PIL import Image
import pyttsx3
from io import BytesIO
import json

# --- Functions to fetch data for different features ---

def get_random_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?type=single'
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification (temporary fix)
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data['type'] == 'single':
                return joke_data['joke']
            else:
                return "Oops, couldn't fetch a joke right now."
        else:
            return f"Failed to fetch joke, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_quote():
    url = 'https://api.quotable.io/random'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            quote_data = response.json()
            return f"\"{quote_data['content']}\"\n\n- {quote_data['author']}"
        else:
            return f"Failed to fetch quote, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except json.JSONDecodeError:
        return "Failed to decode JSON response for quote"

def get_random_fact():
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fact_data = response.json()
            return fact_data['text']
        else:
            return f"Failed to fetch fact, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except json.JSONDecodeError:
        return "Failed to decode JSON response for fact"

def get_random_meme():
    url = 'https://meme-api.herokuapp.com/gimme'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            meme_data = response.json()
            return meme_data.get('url', 'No meme available')
        else:
            return f"Failed to fetch meme, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except json.JSONDecodeError:
        return "Failed to decode JSON response for meme"

def get_random_quote_of_the_day():
    url = 'https://quotes.rest/qod'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            quote_data = response.json()
            return quote_data['contents']['quotes'][0].get('quote', 'No quote available')
        else:
            return f"Failed to fetch quote of the day, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return "Failed to find the expected keys in the response for the quote of the day"
    except json.JSONDecodeError:
        return "Failed to decode JSON response for quote of the day"

def get_random_movie():
    movies = [
        "Inception (2010)",
        "The Matrix (1999)",
        "The Dark Knight (2008)",
        "Interstellar (2014)",
        "Parasite (2019)"
    ]
    return random.choice(movies)

def get_random_tv_show():
    shows = [
        "Breaking Bad",
        "Stranger Things",
        "The Office",
        "Game of Thrones",
        "Black Mirror"
    ]
    return random.choice(shows)

def get_knock_knock_joke():
    return "Knock knock! Who’s there? Lettuce. Lettuce who? Lettuce in, it’s cold out here!"

def get_random_trivia():
    url = 'https://opentdb.com/api.php?amount=1&type=multiple'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            trivia_data = response.json()['results'][0]
            question = trivia_data['question']
            correct_answer = trivia_data['correct_answer']
            options = trivia_data['incorrect_answers'] + [correct_answer]
            random.shuffle(options)
            return question, options, correct_answer
        else:
            return "Failed to fetch trivia, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_weather():
    cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
    city = random.choice(cities)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            return f"Weather in {city}: {weather_data['weather'][0]['description']}, Temp: {weather_data['main']['temp']}°C"
        else:
            return f"Failed to fetch weather, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_animal_image():
    url = 'https://place.dog/500/500'
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_cat_image():
    url = 'https://cataas.com/cat'
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# --- Streamlit Layout ---
st.title("Ultimate Fun Generator")
st.markdown("Welcome to the **Ultimate Fun Generator**! Let's get your dose of randomness.")

# --- Random Joke ---
st.subheader("😂 Random Joke")
if st.button('Generate a Random Joke'):
    joke = get_random_joke()
    st.write(joke)

# --- Random Quote ---
st.subheader("💬 Random Quote")
if st.button('Generate a Random Quote'):
    quote = get_random_quote()
    st.write(quote)

# --- Random Fun Fact ---
st.subheader("🎉 Random Fun Fact")
if st.button('Generate Random Fact'):
    fact = get_random_fact()
    st.write(fact)

# --- Random Meme ---
st.subheader("😆 Random Meme")
if st.button('Generate Random Meme'):
    meme_url = get_random_meme()
    if meme_url.startswith('http'):
        st.image(meme_url, caption="Random Meme")
    else:
        st.error(meme_url)

# --- Random Movie Recommendation ---
st.subheader("🎬 Random Movie Recommendation")
if st.button('Generate Random Movie'):
    movie = get_random_movie()
    st.write(f"How about watching: {movie}")

# --- Random TV Show Recommendation ---
st.subheader("📺 Random TV Show Recommendation")
if st.button('Generate Random TV Show'):
    show = get_random_tv_show()
    st.write(f"How about watching: {show}")

# --- Random Knock Knock Joke ---
st.subheader("🔔 Knock-Knock Joke")
if st.button('Generate Knock Knock Joke'):
    knock_joke = get_knock_knock_joke()
    st.write(knock_joke)

# --- Random Trivia Question ---
st.subheader("🧠 Random Trivia Question")
if st.button('Generate Random Trivia'):
    question, options, correct_answer = get_random_trivia()
    st.write(question)
    st.write("Options: ", options)
    st.write(f"Correct Answer: {correct_answer}")

# --- Random Animal Image ---
st.subheader("🐶 Random Animal Picture")
if st.button('Generate Random Animal Image'):
    img = get_random_animal_image()
    st.image(img, caption="Cute Animal!")

# --- Random Cat Image ---
st.subheader("🐱 Random Cat Picture")
if st.button('Generate Random Cat Image'):
    img = get_random_cat_image()
    st.image(img, caption="Cute Cat!")

# --- Random Weather ---
st.subheader("☀️ Random Weather")
if st.button('Generate Random Weather'):
    weather = get_random_weather()
    st.write(weather)

# --- Quote of the Day ---
st.subheader("🌟 Quote of the Day")
if st.button('Generate Quote of the Day'):
    quote_of_the_day = get_random_quote_of_the_day()
    st.write(quote_of_the_day)

# --- Footer ---
st.markdown("Made with 💙 by ChatGPT. Enjoy the randomness!")
