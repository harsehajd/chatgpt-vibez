from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# setting up the openai api key
openai.api_key = "[KEY HERE LOL]"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    vibe_description = request.form['vibe_description']
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a music playlist with a {vibe_description} vibe.",
        max_tokens=100,
        n=10,
        temperature=0.7,
        stop=None
    )
    playlist = [choice["text"].strip() for choice in response.choices]
    
    return render_template('result.html', playlist=playlist)

if __name__ == '__main__':
    app.run()
