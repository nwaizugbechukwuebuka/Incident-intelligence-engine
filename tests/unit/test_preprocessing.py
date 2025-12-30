from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.language_detection import detect_language
from src.preprocessing.normalization import normalize_text

def test_clean_text():
    assert clean_text("  test\nincident  ") == "test incident"

def test_detect_language():
    assert detect_language("This is English.") == "en"

def test_normalize_text():
    assert normalize_text("test", "en") == "test"
