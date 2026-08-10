import streamlit as st
import logic

# Page configuration (title and icon displayed on the browser tab)
st.set_page_config(page_title="Mastermind Game", page_icon="🧩")

# Main Title and Subtitle
st.title("🧩 Mastermind Game")
st.caption("Try to guess the secret 4-letter code!")

# Game rules inside a collapsible menu (expander)
with st.expander("📖 How to play"):
    st.write("""
    - The secret code consists of **4 unique letters** from **A** to **F**.
    - You have **10 attempts** to guess the correct code.
    - **Black matches (⬛):** Correct letter in the correct position.
    - **White matches (⬜):** Correct letter in the wrong position.
    """)

# Player input section
st.subheader("Make your guess")

user_input = st.text_input("Enter 4 letters (A-F):", max_chars=4)

if st.button("Submit Guess"):
    try:
        logic.validate_guess(user_input)
        st.success(f"Valid guess: {user_input.upper()}")
    except ValueError as e:
        st.error(e)