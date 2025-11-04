from src.isbn import is_valid_isbn10

def test_valid_isbn10_digits():
    assert is_valid_isbn10("0306406152")

def test_valid_isbn10_with_X():
    assert is_valid_isbn10("0-8044-2957-X")

def test_invalid_isbn10_length():
    assert not is_valid_isbn10("123456789")
    assert not is_valid_isbn10("12345678901")

def test_invalid_isbn10_characters():
    assert not is_valid_isbn10("ABCDEFGHIJ")