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
        
        # 4. Check win condition
        if blacks == 4:
            st.session_state.game_over = True
            st.balloons()
            st.success(f"🎉 Congratulations! You guessed the secret code in {len(st.session_state.attempts)} attempt(s)!")
            
        # 5. Check loss condition (max 10 attempts)
        elif len(st.session_state.attempts) >= 10:
            st.session_state.game_over = True
            secret_str = "".join(st.session_state.secret_code)
            st.error(f"💥 Game Over! You reached the limit of 10 attempts. The secret code was: {secret_str}")
        else:
            st.success(f"Guess submitted: {formatted_guess}")
        
    except ValueError as e:
        st.error(e)

# -----------------------------------------------------------------------------
# RESET GAME OPTION
# -----------------------------------------------------------------------------
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.clear()
        st.rerun()

# -----------------------------------------------------------------------------
# TEMPORARY DEBUG PANEL (For testing win/loss flow)
# -----------------------------------------------------------------------------
st.divider()
st.write("🕵️ **Debug Panel (Testing session state):**")
st.write(f"**Secret Code:** `{st.session_state.secret_code}`")
st.write(f"**Attempts Count:** `{len(st.session_state.attempts)} / 10`")
st.write(f"**Game Over:** `{st.session_state.game_over}`")