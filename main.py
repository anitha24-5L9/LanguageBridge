from flask import Flask, render_template, request, jsonify
from googletrans import Translator

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
    text = data.get('text')
    source = data.get('source')
    target = data.get('target')

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
    app.run(debug=True)