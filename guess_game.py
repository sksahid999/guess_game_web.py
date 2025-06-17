import streamlit as st
import random

# --- Page setup ---
st.set_page_config(page_title="Guess the Number Game", page_icon="🎯", layout="centered")

# --- Title & Instructions ---
st.title("🎮 Guess the Number Game")
st.markdown("""
Try to guess the **secret number** between 1 and 10.

🎯 **How to Play**:
- Use **numpad** or keyboard to type your number
- Press **Enter** to submit your guess
- After winning, press **Tab + Enter** to play again
- Mouse is optional — fully keyboard-friendly!
""")
st.markdown("---")

# --- Game State Setup ---
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_won = False

# --- Form for Guessing (Enables Enter Key Support) ---
with st.form(key="guess_form"):
    guess = st.number_input("🔢 Your Guess (1–10):", min_value=1, max_value=10, step=1)
    submitted = st.form_submit_button("Guess")

# --- Game Logic ---
if submitted and not st.session_state.game_won:
    st.session_state.attempts += 1
    if guess == st.session_state.secret_number:
        st.success(f"🎉 Correct! The number was {st.session_state.secret_number}")
        st.balloons()
        st.markdown(f"✅ You guessed it in **{st.session_state.attempts}** attempts.")
        st.session_state.game_won = True
    elif guess < st.session_state.secret_number:
        st.warning("🔼 Too low! Try again.")
    else:
        st.warning("🔽 Too high! Try again.")

# --- Reset Game Logic ---
if st.session_state.game_won:
    st.markdown("🎮 Press **Tab + Enter** to restart, or click below:")
    if st.button("🔄 Play Again"):
        st.session_state.clear()  # Clear all session data
        st.experimental_rerun()   # Restart the app cleanly

# --- Footer ---
st.markdown("---")
st.markdown("👨‍💻 Developed by [SK SAHID] · Powered by Streamlit")
