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
    try:
        data = request.get_json()

        text = data.get('text')
        source = data.get('source')
        target = data.get('target')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        result = translator.translate(
            text,
            src=source,
            dest=target
        )

        return jsonify({
            "translated_text": result.text
        })

    except Exception as e:
        return jsonify({
            "error": "Translation failed",
            "details": str(e)
        }), 500


# ✅ IMPORTANT: Render uses this (NO debug mode)
if __name__ == "__main__":
    app.run()