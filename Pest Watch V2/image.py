import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

class YOLOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLO Image Prediction App")

        # Set window size
        self.root.geometry("1200x600")  # Set the window size to 1200x600

        # Create GUI elements
        self.create_widgets()

        # YOLO model initialization
        self.model = YOLO("best.pt")

    def create_widgets(self):
        # Browse button to select an image
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_image, width=20, height=2, font=("Helvetica", 14))
        self.browse_button.pack(pady=10)

        # Frame to hold input and output image labels
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        # Display input image on the left
        self.input_image_label = tk.Label(self.image_frame, text="Input Image")
        self.input_image_label.pack(side="left")

        # Display output image on the right
        self.output_image_label = tk.Label(self.image_frame, text="Output Image")
        self.output_image_label.pack(side="right")

    def browse_image(self):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            # Process image using YOLO model
            output_image_path = self.predict_and_return_output_path(file_path)

            # Display input image on the left
            self.display_image(file_path, self.input_image_label)

            # Display output image on the right
            self.display_image(output_image_path, self.output_image_label)

    def predict_and_return_output_path(self, image_path):
        # Predict using the YOLO model
        output = self.model.predict(image_path, save=True, save_txt=True)
        output_directory = "runs/detect/predict/"
        image_name = os.path.basename(image_path)
        saved_image_path = os.path.join(output_directory, image_name)

        return saved_image_path

    def display_image(self, image_path, label):
        # Open and display the image using PIL and Tkinter
        image = Image.open(image_path)
        image = image.resize((300, 300))  # Resize for display
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)
        label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOApp(root)
    root.mainloop()
