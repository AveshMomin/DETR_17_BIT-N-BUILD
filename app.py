from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
import os
from PestWatch import pestwatch  # Import your pestwatch function
from PestWatch2 import predict_and_return_output_path
from pestpred import pestpred
from week import predict_week

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
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
            # Call pestwatch function and pass the result to the template
            pest_class, suggestion = pestwatch('static/uploads/' + filename)
            print(f"pest_class: {pest_class}, suggestion: {suggestion}")
            return render_template('pestwatch.html', pest_class=pest_class, suggestion=suggestion)
    
    # Handle the case where no file is uploaded
    return redirect(url_for('pest_watch'))

# New route for handling image uploads
@app.route('/pestwatch2-image', methods=['POST','GET'])
def image_uploadv2():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
            
            # Use YOLO model for prediction
            saved_image_path = predict_and_return_output_path('static/uploads/' + filename)
            print(saved_image_path)
            
            return render_template('weather-result.html')
    
    # Handle the case where no file is uploaded
    saved_image_path = None  # Provide an empty or None value for no image uploaded
    return render_template('weather-result.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = [float(request.form['feature1']),
                      float(request.form['feature2']),
                      float(request.form['feature3']),
                      float(request.form['feature4']),
                      float(request.form['feature5'])]

        result = pestpred(input_data)
        return render_template('pestpred.html', result=result)

@app.route('/pestpred')
def PestPred():
    return render_template('pestpred.html')

@app.route('/pestwatch2')
def weather():
    return render_template('weather.html')

@app.route('/week', methods=['GET', 'POST'])
def week():
    result = None

    if request.method == 'POST':
        current_week = request.form['current_week']
        result = predict_week(int(current_week))

    return render_template('week.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
