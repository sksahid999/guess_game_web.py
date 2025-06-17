import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Guess the Number", page_icon="🎯", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🎮 Guess the Number Game</h1>", unsafe_allow_html=True)
st.markdown("### Press `Tab + Enter` to guess without using your mouse.")

# Sound function using HTML
def play_sound(url):
    st.markdown(
        f"""
        <audio autoplay>
            <source src="{url}" type="audio/ogg">
        </audio>
        """,
        unsafe_allow_html=True
    )

# Initialize session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.tries = 0
    st.session_state.play_again = False

# Game form
with st.form("guess_form", clear_on_submit=True):
    guess = st.number_input("Enter a number between 1 and 10 👇", min_value=1, max_value=10, step=1)
    submitted = st.form_submit_button("🎯 Guess")

# Game logic
if submitted:
    st.session_state.tries += 1
    if guess == st.session_state.secret:
        st.success(f"✅ Correct! It was {st.session_state.secret}.")
        st.info(f"🎉 You guessed it in {st.session_state.tries} tries.")
        play_sound("https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg")
        st.session_state.play_again = True
    elif guess < st.session_state.secret:
        st.warning("📉 Too low! Try again.")
        play_sound("https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg")
    else:
        st.warning("📈 Too high! Try again.")
        play_sound("https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg")

# Play Again button
if st.session_state.play_again:
    if st.button("🔁 Play Again"):
        st.session_state.secret = random.randint(1, 10)
        st.session_state.tries = 0
        st.session_state.play_again = False
        play_sound("https://actions.google.com/sounds/v1/cartoon/slide_whistle_to_drum_hit.ogg")
        st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>🔧 Created by <b>Sk Sahid</b> using Python + Streamlit</p>",
    unsafe_allow_html=True
)
