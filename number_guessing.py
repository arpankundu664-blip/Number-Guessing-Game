import random
import streamlit as st

# Page setup
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# Initialize game
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.message = ""
    st.session_state.game_over = False

# Title
st.title("🎯 Number Guessing Game")
st.write("Guess a number between **1 and 100**!")

# Input
guessed = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)

# Guess button
if st.button("🎯 Guess", use_container_width=True):

    if not st.session_state.game_over:

        st.session_state.tries += 1

        if guessed == st.session_state.num:
            st.session_state.message = (
                f"🎉 Congratulations! You got the number "
                f"in **{st.session_state.tries} tries**!"
            )
            st.session_state.game_over = True

        elif guessed > st.session_state.num:
            st.session_state.message = "⬇️ Sorry! Go a little **lower**."

        else:
            st.session_state.message = "⬆️ Sorry! Go a little **higher**."

# Show message
if st.session_state.message:
    st.info(st.session_state.message)

# Show tries
st.write(f"🔢 **Attempts:** {st.session_state.tries}")

# New game button
if st.button("🔄 New Game", use_container_width=True):

    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.message = ""
    st.session_state.game_over = False

    st.rerun()