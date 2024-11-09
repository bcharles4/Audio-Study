import os
import pyttsx3
from flask import Flask, request, render_template, send_file, jsonify, abort
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


# Function to extract text from files
def extract_text_from_file(file_path, file_type):
    text = ""
    if file_type == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    elif file_type == 'pdf':
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif file_type == 'docx':
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text
    return text


# Function to convert text to speech using pyttsx3 and save it to an audio file
def speak_text_to_file(text, audio_file, voice_id=None):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Set the chosen voice, if it exists
    if voice_id:
        found_voice = next((voice for voice in voices if voice.id == voice_id), None)
        if found_voice:
            engine.setProperty('voice', voice_id)
        else:
            print(f"Voice ID {voice_id} not found. Using default voice.")

    engine.save_to_file(text, audio_file)
    engine.runAndWait()


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for convert  (Text-to-Speech)
@app.route('/convert')
def convert():
    return render_template('convert.html')

@app.route('/lesson')
def lesson():
    return render_template('lesson.html')

# Route for page 1 labor law (Text-to-Speech)
@app.route('/laborlaw1')
def laborlaw1():
    return render_template('laborlaw1.html')

# Route for Lesson 2 (Speech-to-Text)
@app.route('/laborlaw2')
def laborlaw2():
    return render_template('laborlaw2.html')

@app.route('/laborlaw3')
def laborlaw3():
    return render_template('laborlaw3.html')

@app.route('/laborlaw4')
def laborlaw4():
    return render_template('laborlaw4.html')

@app.route('/laborlaw5')
def laborlaw5():
    return render_template('laborlaw5.html')

@app.route('/laborlaw6')
def laborlaw6():
    return render_template('laborlaw6.html')


# Get available voices (for selection on frontend)
@app.route('/get_voices', methods=['GET'])
def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voices_list = [{'id': voice.id, 'name': voice.name} for voice in voices]
    return jsonify(voices_list)


# Route for file upload and TTS conversion
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'voice_id' not in request.form:
        return "File or voice selection not provided", 400

    file = request.files['file']
    voice_id = request.form['voice_id']

    if file.filename == '':
        return "No file selected", 400

    if file:
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        if file_ext not in ['txt', 'pdf', 'docx']:
            return "Unsupported file type", 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Extract text from the uploaded file
        text = extract_text_from_file(file_path, file_ext)

        # Convert text to speech and save as an audio file
        audio_file = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
        speak_text_to_file(text, audio_file, voice_id)

        return send_file(audio_file, as_attachment=True, mimetype='audio/mpeg')


# Route for converting paragraph text to speech and playing it (with voice selection)
@app.route('/read_paragraph', methods=['POST'])
def read_paragraph():
    data = request.json
    text = data.get('text')
    voice_id = data.get('voice_id')

    if not text:
        return "No text provided", 400

    audio_file = os.path.join(app.config['UPLOAD_FOLDER'], 'paragraph_output.mp3')
    speak_text_to_file(text, audio_file, voice_id)

    return send_file(audio_file, as_attachment=True, mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run(debug=True)
