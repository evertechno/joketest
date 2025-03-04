import streamlit as st
import random
import requests
from PIL import Image
import pyttsx3
from io import BytesIO
import webbrowser
import json

# --- Functions to fetch data for different features ---
# Joke API
def get_random_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?type=single'
    response = requests.get(url)
    joke_data = response.json()
    if joke_data['type'] == 'single':
        return joke_data['joke']
    else:
        return "Oops, couldn't fetch a joke right now."

# Quote API
def get_random_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    quote_data = response.json()
    return f"\"{quote_data['content']}\"\n\n- {quote_data['author']}"

# Fun fact API
def get_random_fact():
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    response = requests.get(url)
    fact_data = response.json()
    return fact_data['text']

# Random animal picture
def get_random_animal_image():
    url = 'https://place.dog/500/500'
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Random cat image
def get_random_cat_image():
    url = 'https://cataas.com/cat'
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Random meme
def get_random_meme():
    url = 'https://meme-api.herokuapp.com/gimme'
    response = requests.get(url)
    meme_data = response.json()
    return meme_data['url']

# Random trivia question
def get_random_trivia():
    url = 'https://opentdb.com/api.php?amount=1&type=multiple'
    response = requests.get(url)
    trivia_data = response.json()['results'][0]
    question = trivia_data['question']
    correct_answer = trivia_data['correct_answer']
    options = trivia_data['incorrect_answers'] + [correct_answer]
    random.shuffle(options)
    return question, options, correct_answer

# Knock-knock joke
def get_knock_knock_joke():
    return "Knock knock! Who’s there? Lettuce. Lettuce who? Lettuce in, it’s cold out here!"

# Random number generator
def random_number():
    return random.randint(1, 100)

# Random fortune
def get_random_fortune():
    fortunes = [
        "You will find great luck today!",
        "A pleasant surprise awaits you.",
        "Good things are coming your way!",
        "Beware of unexpected opportunities.",
        "Trust in yourself and success will follow."
    ]
    return random.choice(fortunes)

# Random Spotify playlist
def get_random_spotify_playlist():
    playlists = [
        "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M",  # Today's Top Hits
        "https://open.spotify.com/playlist/37i9dQZF1DX1X7bsl3PDQw",  # Pop Remix
        "https://open.spotify.com/playlist/37i9dQZF1DWXhZkJ5yGxNS"   # Chill Hits
    ]
    return random.choice(playlists)

# Random dance GIF
def get_random_dance_gif():
    url = 'https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY&tag=dance'
    response = requests.get(url)
    gif_data = response.json()['data']
    return gif_data[0]['images']['original']['url']

# Random weather
def get_random_weather():
    cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
    city = random.choice(cities)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    return f"Weather in {city}: {weather_data['weather'][0]['description']}, Temp: {weather_data['main']['temp']}°C"

# Random YouTube channel
def get_random_youtube_channel():
    channels = [
        "https://www.youtube.com/c/Veritasium",
        "https://www.youtube.com/c/TEDxTalks",
        "https://www.youtube.com/c/Kurzgesagt"
    ]
    return random.choice(channels)

# Random movie recommendation
def get_random_movie():
    movies = [
        "Inception (2010)",
        "The Matrix (1999)",
        "The Dark Knight (2008)",
        "Interstellar (2014)",
        "Parasite (2019)"
    ]
    return random.choice(movies)

# Random TV show recommendation
def get_random_tv_show():
    shows = [
        "Breaking Bad",
        "Stranger Things",
        "The Office",
        "Game of Thrones",
        "Black Mirror"
    ]
    return random.choice(shows)

# Random riddle
def get_random_riddle():
    riddles = [
        {"question": "What has keys but can't open locks?", "answer": "A piano"},
        {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter 'M'"},
        {"question": "What is full of holes but still holds a lot of weight?", "answer": "A net"}
    ]
    riddle = random.choice(riddles)
    return riddle['question'], riddle['answer']

# Random quote of the day
def get_random_quote_of_the_day():
    url = 'https://quotes.rest/qod'
    response = requests.get(url)
    quote_data = response.json()
    return quote_data['contents']['quotes'][0]['quote']

# --- Streamlit layout ---
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

# --- Animal Image ---
st.subheader("🐶 Random Animal Picture")
if st.button('Generate a Random Animal Image'):
    img = get_random_animal_image()
    st.image(img, caption="Cute Animal!")

# --- Cat Image ---
st.subheader("🐱 Random Cat Picture")
if st.button('Generate a Random Cat Image'):
    img = get_random_cat_image()
    st.image(img, caption="Cute Cat!")

# --- Random Meme ---
st.subheader("😆 Random Meme")
if st.button('Generate Random Meme'):
    meme_url = get_random_meme()
    st.image(meme_url, caption="Random Meme")

# --- Random Trivia ---
st.subheader("🧠 Random Trivia Question")
if st.button('Generate Random Trivia'):
    question, options, correct_answer = get_random_trivia()
    st.write(question)
    st.write("Options: ", options)
    st.write(f"Correct Answer: {correct_answer}")

# --- Knock Knock Joke ---
st.subheader("🔔 Knock-Knock Joke")
if st.button('Generate Knock Knock Joke'):
    knock_joke = get_knock_knock_joke()
    st.write(knock_joke)

# --- Random Movie ---
st.subheader("🎬 Random Movie Recommendation")
if st.button('Generate Movie'):
    movie = get_random_movie()
    st.write(f"How about watching: {movie}")

# --- Random TV Show ---
st.subheader("📺 Random TV Show Recommendation")
if st.button('Generate TV Show'):
    show = get_random_tv_show()
    st.write(f"How about watching: {show}")

# --- Random Riddle ---
st.subheader("🧩 Random Riddle")
if st.button('Generate Riddle'):
    riddle_question, riddle_answer = get_random_riddle()
    st.write(f"Riddle: {riddle_question}")
    st.write(f"Answer: {riddle_answer}")

# --- Quote of the Day ---
st.subheader("🌟 Quote of the Day")
if st.button('Generate Quote of the Day'):
    quote_of_the_day = get_random_quote_of_the_day()
    st.write(quote_of_the_day)

# --- Footer ---
st.markdown("Made with 💙 by ChatGPT. Enjoy the randomness!")

