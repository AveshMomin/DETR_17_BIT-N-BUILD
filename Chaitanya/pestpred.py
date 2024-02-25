import pickle

def pestpred(input_data):
    

    # Load the pickled model
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)

    
    # Make predictions
    prediction = model.predict([input_data])[0]  # Assuming only one prediction

    # Define your class labels
    class_labels = ['Brownplanthopper', 'Gallmidge', 'Greenleafhopper', 'LeafFolder',
                    'Yellowstemborer', 'Caseworm', 'Miridbug', 'Whitebackedplanthopper',
                    'ZigZagleafhopper', 'LeafBlast', 'NeckBlast']

    # Print the prediction

    # Print the corresponding class label
    if 1 <= prediction <= len(class_labels):
        predicted_class = class_labels[prediction - 1]
        print("Predicted Class:", predicted_class)
    else:
        print("Invalid prediction index.")

    return predicted_class