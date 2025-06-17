import streamlit as st
import random
import streamlit as st
import random
import time

st.set_page_config(
    page_title="🎯 Guess the Number",
    page_icon="🎮",
    layout="centered"
)

st.image("https://i.imgur.com/Bo4nY9z.png", use_column_width=True)
st.markdown("## 🎉 Welcome to the Guessing Game!")
st.markdown("Try to guess the number between 1 and 10 🎯")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.tries = 0

guess = st.number_input("🔢 Enter a number (1-10):", min_value=1, max_value=10, step=1)

if st.button("Guess"):
    with st.spinner("Thinking..."):
        time.sleep(1)
    st.session_state.tries += 1
    if guess == st.session_state.secret:
        st.success(f"🎉 Correct! It was {st.session_state.secret}. Attempts: {st.session_state.tries}")
        st.balloons()
        st.session_state.secret = random.randint(1, 10)
        st.session_state.tries = 0
    elif guess < st.session_state.secret:
        st.warning("🔼 Too low!")
    else:
        st.warning("🔽 Too high!")

st.write(f"🔁 Attempts so far: {st.session_state.tries}")


st.title("🎮 Guess the Number Game")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.tries = 0

guess = st.number_input("Enter a number (1-10):", min_value=1, max_value=10, step=1)

if st.button("Guess"):
    st.session_state.tries += 1
    if guess == st.session_state.secret:
        st.success(f"🎉 Correct! It was {st.session_state.secret}. Attempts: {st.session_state.tries}")
        st.session_state.secret = random.randint(1, 10)
        st.session_state.tries = 0
    elif guess < st.session_state.secret:
        st.warning("🔼 Too low!")
    else:
        st.warning("🔽 Too high!")
