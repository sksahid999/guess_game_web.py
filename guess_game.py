import streamlit as st
import random

# --- Page setup ---
st.set_page_config(page_title="Guess the Number Game", page_icon="🎯", layout="centered")

# --- Title & Instructions ---
st.title("🎮 Guess the Number Game")
st.markdown("Try to guess the **secret number** between 1 and 10. Good luck! 🍀")
st.markdown("---")

# --- Game State Initialization ---
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0

# --- User Input ---
guess = st.number_input("🔢 Enter your guess (1-10):", min_value=1, max_value=10, step=1)

# --- Guess Button ---
if st.button("Guess", key="main_guess_button"):
    st.session_state.attempts += 1
    if guess == st.session_state.secret_number:
        st.success(f"🎉 Correct! The number was {st.session_state.secret_number}.")
        st.balloons()
        st.markdown(f"💡 Total attempts: **{st.session_state.attempts}**")
        # Reset game
        st.session_state.secret_number = random.randint(1, 10)
        st.session_state.attempts = 0
    elif guess < st.session_state.secret_number:
        st.warning("🔼 Too low! Try a higher number.")
    else:
        st.warning("🔽 Too high! Try a lower number.")

# --- Footer ---
st.markdown("---")
st.markdown("👨‍💻 Developed by [SK SAHID] · Powered by Streamlit")
