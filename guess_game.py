import streamlit as st
import random

# Page config
st.set_page_config(page_title="🎯 Guess the Number", page_icon="🎲", layout="centered")

# Header
st.markdown("<h1 style='text-align:center;'>🎮 Guess the Number Game</h1>", unsafe_allow_html=True)
st.markdown("### ➡️ Use `Tab` + `Enter` to play without mouse. Enter number & press Enter.")

# Function to play sound
def play_sound(url):
    st.markdown(
        f"""
        <audio autoplay>
            <source src="{url}" type="audio/ogg">
        </audio>
        """,
        unsafe_allow_html=True
    )

# Reset the game
def reset_game():
    st.session_state.clear()
    st.experimental_rerun()

# Initialize session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.tries = 0
    st.session_state.play_again = False

# Game logic
if not st.session_state.play_again:
    with st.form("guess_form", clear_on_submit=True):
        guess = st.number_input("🔢 Enter a number between 1 and 10:", min_value=1, max_value=10, step=1)
        submitted = st.form_submit_button("🎯 Guess (Tab + Enter)")

    if submitted:
        st.session_state.tries += 1
        if guess == st.session_state.secret:
            st.success(f"✅ Correct! The number was {st.session_state.secret}")
            st.info(f"🎉 You got it in {st.session_state.tries} tries!")
            play_sound("https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg")
            st.session_state.play_again = True
        elif guess < st.session_state.secret:
            st.warning("📉 Too low! Try again.")
            play_sound("https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg")
        else:
            st.warning("📈 Too high! Try again.")
            play_sound("https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg")

# Play Again section
if st.session_state.play_again:
    with st.form("restart_form"):
        restart = st.form_submit_button("🔁 Play Again (Tab + Enter)")
        if restart:
            play_sound("https://actions.google.com/sounds/v1/cartoon/slide_whistle_to_drum_hit.ogg")
            reset_game()

# Footer credits
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>🔧 Created by <strong>Sk Sahid</strong> using Python + Streamlit</p>",
    unsafe_allow_html=True
)
