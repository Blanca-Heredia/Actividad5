from hypothesis import given, strategies as st
from src.isbn import normalize_isbn, detect_isbn

@given(st.text())
def test_normalize_idempotent(s):
    """Probar que normalizar dos veces da el mismo resultado."""
    assert normalize_isbn(normalize_isbn(s)) == normalize_isbn(s)

@given(st.text())
def test_detect_returns_valid_type(s):
    """detect_isbn siempre debe devolver una de las tres etiquetas."""
    assert detect_isbn(s) in ["ISBN-10", "ISBN-13", "INVALID"]