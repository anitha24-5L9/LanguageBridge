from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import os

app = Flask(
    __name__,
    template_folder='views',
    static_folder='assets'
)

translator = Translator()

@app.route('/')
def home():
    return render_template('translator.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    text = data.get('text', '')
    source = data.get('source', 'en')
    target = data.get('target', 'en')

    if not text:
        return jsonify({'error': 'Text is empty'}), 400

    try:
        translated = translator.translate(
            text,
            src=source,
            dest=target
        )

        return jsonify({
            'translated_text': translated.text
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)