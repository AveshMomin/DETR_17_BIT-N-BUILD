from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration for file uploads
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/uploads"
configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pestwatch')
def pest_watch():
    return render_template('pestwatch.html')

# New route for handling image uploads
@app.route('/image_upload', methods=['POST'])
def image_upload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], 'upload.png'))
            return redirect(url_for('pest_watch', filename='upload.png'))

    # Handle the case where no file is uploaded
    return redirect(url_for('pest_watch'))

@app.route('/weather')
def weather():
    return render_template('weather.html')


if __name__ == '__main__':
    app.run(debug=True)
