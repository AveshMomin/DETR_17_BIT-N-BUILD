from ultralytics import YOLO
import os

def predict_and_return_output_path(image_path):
    # Initialize YOLO model
    model = YOLO("best.pt")

    # Predict using the model
    output = model.predict(image_path, save=True, save_txt=True)

    output_directory = "../runs/detect/predict/"
    
    # Get the filename from the image path
    image_name = os.path.basename(image_path)

    # Get the path of the saved image
    saved_image_path = os.path.join(output_directory, image_name)
    print(saved_image_path)

    return saved_image_path
