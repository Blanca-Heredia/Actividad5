from src.isbn import is_valid_isbn13

def test_valid_isbn13():
    assert is_valid_isbn13("9780306406157")

def test_invalid_isbn13_length():
    assert not is_valid_isbn13("978030640615")
    assert not is_valid_isbn13("97803064061577")

def test_invalid_isbn13_characters():
    assert not is_valid_isbn13("97803O6406157")  # O en lugar de cero