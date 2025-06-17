import streamlit as st
import random

st.title("🎮 Guess the Number Game")

# Initialize game state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.tries = 0

# User input
guess = st.number_input("Enter a number (1-10):", min_value=1, max_value=10, step=1)

# Fixed: added unique key to button
if st.button("Guess", key="main_guess_button"):
    st.session_state.tries += 1

    if guess == st.session_state.secret:
        st.success(f"🎉 Correct! It was {st.session_state.secret}. Attempts: {st.session_state.tries}")
        # Reset game
        st.session_state.secret = random.randint(1, 10)
        st.session_state.tries = 0
    elif guess < st.session_state.secret:
        st.warning("🔼 Too low!")
    else:
        st.warning("🔽 Too high!")
