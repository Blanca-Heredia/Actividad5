import re
from typing import Optional

def normalize_isbn(s: Optional[str]) -> str:
    """Elimina guiones y espacios, convierte a mayúsculas."""
    if s is None:
        return ""
    s = re.sub(r"[\s-]+", "", s)
    return s.upper()

def is_valid_isbn10(s: str) -> bool:
    """Valida un ISBN-10 con o sin 'X' al final."""
    s = normalize_isbn(s)
    if len(s) != 10 or not re.match(r"^\d{9}[\dX]$", s):
        return False
    total = 0
    for i, ch in enumerate(s):
        value = 10 if ch == "X" else int(ch)
        total += value * (10 - i)
    return total % 11 == 0

def is_valid_isbn13(s: str) -> bool:
    """Valida un ISBN-13."""
    s = normalize_isbn(s)
    if len(s) != 13 or not s.isdigit():
        return False
    total = 0
    for i, ch in enumerate(s):
        factor = 1 if i % 2 == 0 else 3
        total += int(ch) * factor
    return total % 10 == 0

def detect_isbn(s: Optional[str]) -> str:
    """Detecta si el código es ISBN-10, ISBN-13 o inválido."""
    s = normalize_isbn(s)
    if is_valid_isbn10(s):
        return "ISBN-10"
    elif is_valid_isbn13(s):
        return "ISBN-13"
    return "INVALID"
