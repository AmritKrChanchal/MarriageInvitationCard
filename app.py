from flask import Flask, render_template, request, send_file
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    # If user does not select file, browser also submits an empty part without filename
    if file.filename == '':
        return "No selected file"

    # If the file is allowed, save it and process
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Video processing code
        processed_path = process_video(file_path)

        return send_file(processed_path, as_attachment=True)

def process_video(video_path):
    # Video processing code
    cap = cv2.VideoCapture(video_path)

    # Video processing code (use the code from the previous response)
    # ...

    # Save the processed video
    output_path = 'static/output_video.mp4'
    cv2.imwrite(output_path, processed_frame)  # Replace with the actual video processing result

    return output_path

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
