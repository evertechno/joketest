import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO
import pyttsx3
import json

# --- Functions to fetch data for different features ---
def get_random_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?type=single'
    try:
        response = requests.get(url, verify=True)
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
    url = 'https://quotes.rest/qod'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            quote_data = response.json()
            return quote_data['contents']['quotes'][0]['quote']
        else:
            return f"Failed to fetch quote, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

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

def get_random_meme():
    url = 'https://api.imgflip.com/get_memes'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            meme_data = response.json()
            random_meme = random.choice(meme_data['data']['memes'])
            return random_meme['url']
        else:
            return f"Failed to fetch meme, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

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

def play_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_random_song_recommendation():
    songs = [
        "Blinding Lights - The Weeknd",
        "Shape of You - Ed Sheeran",
        "Levitating - Dua Lipa",
        "Save Your Tears - The Weeknd",
        "Uptown Funk - Mark Ronson"
    ]
    return random.choice(songs)

def get_random_book_recommendation():
    books = [
        "To Kill a Mockingbird by Harper Lee",
        "1984 by George Orwell",
        "The Great Gatsby by F. Scott Fitzgerald",
        "Moby Dick by Herman Melville",
        "Pride and Prejudice by Jane Austen"
    ]
    return random.choice(books)

def get_random_food_recommendation():
    foods = [
        "Pizza",
        "Burger",
        "Sushi",
        "Pasta",
        "Salad"
    ]
    return random.choice(foods)

def get_random_riddle():
    riddles = [
        "What has keys but can't open locks? A piano.",
        "What can travel around the world while staying in the corner? A stamp.",
        "What is always in front of you but can't be seen? The future."
    ]
    return random.choice(riddles)

def get_random_dog_image():
    url = 'https://dog.ceo/api/breeds/image/random'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dog_data = response.json()
            return dog_data['message']
        else:
            return f"Failed to fetch dog image, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_joke_of_the_day():
    url = 'https://official-joke-api.appspot.com/jokes/random'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data['setup'] + " - " + joke_data['punchline']
        else:
            return f"Failed to fetch joke of the day, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# --- Unique Features ---
def get_random_poem():
    url = 'https://www.poemist.com/api/v1/randompoems'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            poem_data = response.json()[0]
            title = poem_data['title']
            content = poem_data['content']
            return f"{title}\n\n{content}"
        else:
            return f"Failed to fetch poem, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_advice():
    url = 'https://api.adviceslip.com/advice'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            advice_data = response.json()
            return advice_data['slip']['advice']
        else:
            return f"Failed to fetch advice, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def get_random_yoga_pose():
    poses = [
        "Mountain Pose (Tadasana)",
        "Downward-Facing Dog (Adho Mukha Svanasana)",
        "Warrior I (Virabhadrasana I)",
        "Tree Pose (Vrksasana)",
        "Child's Pose (Balasana)"
    ]
    return random.choice(poses)

# --- Streamlit Layout ---
st.title("Ultimate Fun Generator")
st.markdown("Welcome to the **Ultimate Fun Generator**! Let's get your dose of randomness. Choose something fun below.")

# --- Dark Mode Toggle ---
st.sidebar.title("Settings")
theme = st.sidebar.radio("Choose a theme:", ("Light", "Dark"))
if theme == "Dark":
    st.markdown("""
        <style>
        body {
            background-color: #2e2e2e;
            color: white;
        }
        .stButton>button {
            background-color: #6c757d;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Organizing content with multiple columns ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("😂 Random Joke")
    if st.button('Generate a Random Joke'):
        joke = get_random_joke()
        st.write(joke)
    
    st.subheader("🎬 Random Movie Recommendation")
    if st.button('Generate Random Movie'):
        movie = get_random_movie()
        st.write(f"How about watching: {movie}")
    
    st.subheader("🎶 Random Song Recommendation")
    if st.button('Generate Random Song'):
        song = get_random_song_recommendation()
        st.write(f"How about listening to: {song}")
    
    st.subheader("🍕 Random Food Recommendation")
    if st.button('Generate Random Food'):
        food = get_random_food_recommendation()
        st.write(f"How about eating: {food}")
    
    st.subheader("🐶 Random Dog Image")
    if st.button('Generate Random Dog Image'):
        dog_image = get_random_dog_image()
        st.image(dog_image, caption="Cute Dog!")

with col2:
    st.subheader("💬 Random Quote")
    if st.button('Generate a Random Quote'):
        quote = get_random_quote()
        st.write(quote)
    
    st.subheader("🧠 Random Trivia Question")
    if st.button('Generate Random Trivia'):
        question, options, correct_answer = get_random_trivia()
        st.write(question)
        st.write("Options: ", options)
        st.write(f"Correct Answer: {correct_answer}")
    
    st.subheader("📚 Random Book Recommendation")
    if st.button('Generate Random Book'):
        book = get_random_book_recommendation()
        st.write(f"How about reading: {book}")
    
    st.subheader("🌟 Quote of the Day")
    if st.button('Generate Quote of the Day'):
        quote_of_the_day = get_random_quote_of_the_day()
        st.write(quote_of_the_day)

    st.subheader("🎭 Joke of the Day")
    if st.button('Generate Joke of the Day'):
        joke_of_the_day = get_random_joke_of_the_day()
        st.write(joke_of_the_day)

with col3:
    st.subheader("🐱 Random Cat Image")
    if st.button('Generate Random Cat Image'):
        img = get_random_cat_image()
        st.image(img, caption="Cute Cat!")
    
    st.subheader("⚡ Random Fact")
    if st.button('Generate Random Fact'):
        fact = get_random_fact()
        st.write(fact)
    
    st.subheader("🌍 Random Weather")
    if st.button('Generate Random Weather'):
        weather = get_random_weather()
        st.write(weather)
    
    st.subheader("🔮 Random Riddle")
    if st.button('Generate Random Riddle'):
        riddle = get_random_riddle()
        st.write(riddle)

    st.subheader("🐶 Random Animal Image")
    if st.button('Generate Random Animal Image'):
        img = get_random_animal_image()
        st.image(img, caption="Cute Animal!")

    st.subheader("📜 Random Poem")
    if st.button('Generate Random Poem'):
        poem = get_random_poem()
        st.write(poem)

    st.subheader("💡 Random Advice")
    if st.button('Generate Random Advice'):
        advice = get_random_advice()
        st.write(advice)

    st.subheader("🧘 Random Yoga Pose")
    if st.button('Generate Random Yoga Pose'):
        pose = get_random_yoga_pose()
        st.write(f"Try this yoga pose: {pose}")

# --- Footer ---
st.markdown("Made with 💙 by ChatGPT. Enjoy the randomness!")
