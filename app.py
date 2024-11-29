from flask import Flask, render_template('index.html'), request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    style = request.form['style']
    lines = int(request.form['lines']) if style == 'free' else None
    
    poem = generate_poem(style, lines)
    
    return jsonify({
        'poem': poem,
        'style': style,
        'lines': lines
    })

def generate_poem(style, lines):
    if style == 'haiku':
        return "Soft whispers of jade\nEchoes in digital realms\nPoetry blooms here"
    elif style == 'limerick':
        return "There once was an AI named Jade\nWhose poems were expertly made\nWith pixels and prose\nGreat verses arose\nA digital poet displayed"
    else:  # free verse
        words = ["dream", "whisper", "eternity", "star", "ocean", "mountain", "silence", "echo", "shadow", "light"]
        import random
        return "\n".join([f"{random.choice(words).capitalize()} {' '.join(random.choices(words, k=random.randint(3,6)))}" for _ in range(lines)])

if __name__ == '__main__':
    app.run(debug=True)
