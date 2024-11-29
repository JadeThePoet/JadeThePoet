# src/ai/inference.py
import random

def generate_poem(style="free", lines=4):
    styles = {
        "haiku": lambda _: generate_haiku(),
        "limerick": lambda _: generate_limerick(),
        "free": lambda l: generate_free_verse(l)
    }
    poem_generator = styles.get(style, lambda l: generate_free_verse(l))
    poem = poem_generator(lines)
    cleaned_poem = "\n".join(line.strip() for line in poem.split("\n") if line.strip())
    return cleaned_poem.strip()





def generate_haiku():
    haiku_templates = [
        "An old silent pond...\nA frog jumps into the pond,\nsplash! Silence again.",
        "Autumn moonlight—\na worm digs silently\ninto the chestnut.",
        "In the twilight rain\nthese brilliant-hued hibiscus -\nA lovely sunset."
    ]
    return random.choice(haiku_templates)

def generate_limerick():
    limericks = [
        "There was an Old Man with a beard,\nWho said, 'It is just as I feared!\nTwo Owls and a Hen,\nFour Larks and a Wren,\nHave all built their nests in my beard!'",
        "There was a young lady of Niger,\nWho smiled as she rode on a tiger;\nThey returned from the ride\nWith the lady inside,\nAnd the smile on the face of the tiger.",
        "There once was a man from Nantucket\nWho kept all his cash in a bucket.\nBut his daughter, named Nan,\nRan away with a man\nAnd as for the bucket, Nantucket."
    ]
    return random.choice(limericks)

def generate_free_verse(lines):
    words = ["love", "heart", "soul", "mind", "life", "time", "world", "day", "night", "sun", "moon", "star", "flower", "tree", "river", "mountain", "ocean", "wind", "rain", "dream"]
    poem = []
    for _ in range(lines):
        line_length = random.randint(3, 7)
        line = " ".join(random.choice(words) for _ in range(line_length))
        poem.append(line.capitalize())
    return "\n".join(poem)
