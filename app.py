import streamlit as st
import logic

# Page configuration (title and icon displayed on the browser tab)
st.set_page_config(page_title="Mastermind Game", page_icon="🧩")

# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if "secret_code" not in st.session_state:
    st.session_state.secret_code = logic.generate_secret_code()

if "attempts" not in st.session_state:
    st.session_state.attempts = []

if "game_over" not in st.session_state:
    st.session_state.game_over = False

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

user_input = st.text_input(
    "Enter 4 letters (A-F):", 
    max_chars=4, 
    disabled=st.session_state.game_over
)

if st.button("Submit Guess", disabled=st.session_state.game_over):
    try:
        # 1. Validate guess syntax
        logic.validate_guess(user_input)
        formatted_guess = user_input.upper().strip()
        
        # 2. Calculate matches using logic.py
        _, blacks, whites = logic.calculate_matches(formatted_guess, st.session_state.secret_code)
        
        # 3. Store the attempt in session state: (guess_string, blacks, whites)
        st.session_state.attempts.append((formatted_guess, blacks, whites))
        
        st.success(f"Guess submitted: {formatted_guess}")
        
    except ValueError as e:
        st.error(e)

# -----------------------------------------------------------------------------
# TEMPORARY DEBUG PANEL (For testing session state persistence)
# -----------------------------------------------------------------------------
st.divider()
st.write("🕵️ **Debug Panel (Testing session state):**")
st.write(f"**Secret Code:** `{st.session_state.secret_code}`")
st.write(f"**Attempts History:** `{st.session_state.attempts}`")