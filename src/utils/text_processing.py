# src/utils/text_processing.py
def tokenize(text):
    return text.split()

def remove_punctuation(text):
    import string
    return text.translate(str.maketrans("", "", string.punctuation))

# src/utils/metrics.py
def calculate_syllables(word):
    # Simplified syllable counting
    return len(word) // 3 + 1

def evaluate_poem(poem):
    words = poem.split()
    return {
        "word_count": len(words),
        "estimated_syllables": sum(calculate_syllables(word) for word in words)
    }
