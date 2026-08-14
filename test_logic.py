import pytest
import logic

def test_generate_secret_code():
    code = logic.generate_secret_code()
    assert len(code) == 4
    assert len(set(code)) == 4
    assert all(letter in logic.ALPHABET for letter in code)

def test_validate_guess_valid():
    # Should not raise any exception
    logic.validate_guess("ABCD")

def test_validate_guess_invalid_length():
    with pytest.raises(ValueError):
        logic.validate_guess("ABC")

def test_validate_guess_duplicates():
    with pytest.raises(ValueError):
        logic.validate_guess("AABC")

def test_validate_guess_invalid_chars():
    with pytest.raises(ValueError):
        logic.validate_guess("AB12")

def test_calculate_matches():
    secret = ['A', 'B', 'C', 'D']
    
    # All exact matches
    _, blacks, whites = logic.calculate_matches("ABCD", secret)
    assert blacks == 4
    assert whites == 0
    
    # Partial matches
    _, blacks, whites = logic.calculate_matches("DCBA", secret)
    assert blacks == 0
    assert whites == 4
    
    # Mixed matches
    _, blacks, whites = logic.calculate_matches("ABDC", secret)
    assert blacks == 2
    assert whites == 2