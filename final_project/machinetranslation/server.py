from machinetranslation import translator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/englishToFrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(textToTranslate)
    return french_text

@app.route('/frenchToEnglish')
def french_to_english():
    textToTranslate = request.form.get('textToTranslate')
    english_text = translator.french_to_english(textToTranslate)
    return english_text
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
