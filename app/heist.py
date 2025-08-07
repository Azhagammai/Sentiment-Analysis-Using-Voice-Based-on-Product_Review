from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from analyze import analyze_audio
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('online shopping.html')

@app.route('/one')
def one():
    return render_template('one.html')

@app.route('/analyze_audio', methods=['POST'])
def analyze_audio_endpoint():
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['audioFile']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
           
            text, sentiment, probabilities = analyze_audio(filepath)

            
            plt.figure(figsize=(8, 6))
            plt.bar(['Negative', 'Neutral', 'Positive'], probabilities, color=['red', 'gray', 'green'])
            plt.xlabel('Sentiment')
            plt.ylabel('Probability')
            plt.title(f'Sentiment Prediction for Review:')
            plt.ylim(0, 1)

            
            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            plot_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')

            return jsonify({'success': True, 'sentiment': sentiment, 'plot': plot_base64})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
