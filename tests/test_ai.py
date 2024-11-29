# tests/test_ai.py
from src.ai.model import PoemGenerator

def test_poem_generation():
    generator = PoemGenerator()
    poem = generator.generate_poem()
    assert isinstance(poem, str)
    assert len(poem) > 0

# tests/test_data.py
from src.data.data_loader import load_poetry_data
from src.data.preprocessor import preprocess_text

def test_data_loading():
    data = load_poetry_data()
    assert isinstance(data, list)
    assert len(data) > 0

def test_preprocessing():
    text = "Hello, World!"
    processed = preprocess_text(text)
    assert processed == "hello, world!"

# tests/test_utils.py
from src.utils.text_processing import tokenize, remove_punctuation
from src.utils.metrics import evaluate_poem

def test_tokenize():
    text = "Hello world"
    tokens = tokenize(text)
    assert tokens == ["Hello", "world"]

def test_remove_punctuation():
    text = "Hello, world!"
    clean_text = remove_punctuation(text)
    assert clean_text == "Hello world"

def test_evaluate_poem():
    poem = "A simple test poem"
    metrics = evaluate_poem(poem)
    assert "word_count" in metrics
    assert "estimated_syllables" in metrics

# tests/test_x_automation.py
from src.x_automation.api_client import XAPIClient
from src.x_automation.scheduler import PoemScheduler
from src.ai.model import PoemGenerator

def test_api_client():
    client = XAPIClient()
    client.authenticate()
    assert client.authenticated

def test_scheduler():
    generator = PoemGenerator()
    scheduler = PoemScheduler(generator)
    assert scheduler.posting_interval == 3600
