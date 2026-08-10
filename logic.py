import random

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F']

def generate_secret_code() -> list[str]:
    """
    Generates a random secret code of 4 unique letters.

    Returns:
        list[str]: A list containing 4 unique letters chosen from ALPHABET.
    """
    return random.sample(ALPHABET, 4)


def validate_guess(guess: str, alphabet: list[str] = ALPHABET) -> None:
    """
    Validates the user's guess according to the game rules.

    Args:
        guess (str): The guess sequence entered by the player.
        alphabet (list[str], optional): The list of allowed letters. Defaults to ALPHABET.

    Raises:
        ValueError: If the guess contains non-alphabetic characters.
        ValueError: If the guess length is not exactly 4 characters.
        ValueError: If the guess contains duplicate letters.
        ValueError: If the guess contains letters not present in the allowed alphabet.
    """
    guess = guess.upper().strip()

    # Check if input contains only alphabetic characters
    if not guess.isalpha():
        raise ValueError("ERROR: Please enter letters only! Try again.")

    # Check if length is exactly 4 characters
    if len(guess) != 4:
        raise ValueError(
            f"ERROR: You entered {len(guess)} letters. Please enter exactly 4 letters!"
        )

    # Check for duplicate letters
    if len(set(guess)) != 4:
        raise ValueError(
            "ERROR: Letters cannot be repeated! Enter 4 unique letters."
        )

    # Check if all letters belong to the allowed alphabet (A-F)
    invalid_letters = [letter for letter in guess if letter not in alphabet]
    if invalid_letters:
        raise ValueError(
            f"ERROR: Invalid letters: {', '.join(invalid_letters)}. Use only A, B, C, D, E, or F!"
        )


def calculate_matches(
    guess: str, secret_code: list[str]
) -> tuple[str, int, int]:
    """
    Calculates exact (black) and partial (white) matches for a guess against the secret code.

    Args:
        guess (str): The validated user's guess.
        secret_code (list[str]): The target secret code to compare against.

    Returns:
        tuple[str, int, int]: A tuple containing (guess_string, black_matches, white_matches).
    """
    guess = guess.upper().strip()
    guess_list = list(guess)

    blacks = 0  # Correct letter in the correct position
    whites = 0  # Correct letter in the wrong position

    code_copy = secret_code.copy()
    guess_copy = guess_list.copy()

    # Check exact matches (blacks)
    for i in range(4):
        if guess_list[i] == secret_code[i]:
            blacks += 1
            code_copy[i] = None
            guess_copy[i] = None

    # Check partial matches (whites)
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in code_copy:
            whites += 1
            index = code_copy.index(guess_copy[i])
            code_copy[index] = None

    return (guess, blacks, whites)