# VS Code Code

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2

def pestwatch(fn):

    # Load the model
    best_model = load_model('my_model.h5')

    # Load and resize the image
    img=cv2.imread(fn)
    img = cv2.resize(img, (150, 150))
    pest_class = ['aphids', 'armyworm', 'beetle', 'bollworm','grasshopper', 'mites', 'mosquito', 'sawfly', 'stem_borer']
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    y_prob = best_model.predict(x)
    y_class = y_prob.argmax(axis=-1)
    y_class = y_class[0]
    suggest = ['Imidacloprid, Acetamiprid, Thiamethoxam', 'Chlorpyrifos, Lambda-cyhalothrin, Bifenthrin', 'Imidacloprid, Carbaryl, Malathion, Cypermethrin', 'Chlorantraniliprole, Emamectin benzoate, Spinosad, Indoxacarb', 'Carbaryl, Malathion, Pyrethroids', 'Abamectin, Bifenazate, Chlorfenapyr', 'Adulticides, Larvicides', 'Malathion, Carbaryl, Cypermethrin', 'Neonicotinoids, Pyrethroids, Chlorantraniliprole']
    print(f"Given Image has been affected by {pest_class[y_class]}")
    print()
    print("Suggesstion")    
    print("*"*20)
    print("Please use the below pesticide")
    print(suggest[y_class])
    print("*"*28)
    result = f"Given Image has been affected by {pest_class[y_class]}."
    suggestion = f"Please use the below pesticide: {suggest[y_class]}"
    return result, suggestion

