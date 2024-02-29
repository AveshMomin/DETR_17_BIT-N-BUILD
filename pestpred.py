import pickle

def pestpred(input_data):
    # Load the pickled model
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Make predictions
    prediction = model.predict([input_data])[0]  # Assuming only one prediction

    # Define your class labels and respective pesticides
    class_labels = ['Brownplanthopper', 'Gallmidge', 'Greenleafhopper', 'LeafFolder',
                    'Yellowstemborer', 'Caseworm', 'Miridbug', 'Whitebackedplanthopper',
                    'ZigZagleafhopper', 'LeafBlast', 'NeckBlast']

    pesticides = [
        ['Neonicotinoids', 'Pyrethroids', 'Carbamates'],
        ['Neonicotinoids', 'Organophosphates'],
        ['Neonicotinoids', 'Pyrethroids', 'Carbamates'],
        ['Bacillus thuringiensis (Bt)', 'Neonicotinoids'],
        ['Neonicotinoids', 'Pyrethroids'],
        ['Bacillus thuringiensis (Bt)', 'Spinosad'],
        ['Neonicotinoids', 'Pyrethroids'],
        ['Neonicotinoids', 'Pyrethroids'],
        ['Neonicotinoids', 'Pyrethroids'],
        ['Triazoles', 'Strobilurins'],
        ['Triazoles', 'Strobilurins']
    ]

    # Print the prediction
    print("Predicted Class:", class_labels[prediction - 1])

    # Return the corresponding class label and pesticides
    if 1 <= prediction <= len(class_labels):
        predicted_class = class_labels[prediction - 1]
        predicted_pesticides = pesticides[prediction - 1]
        print("Most Commonly Used Pesticides:", predicted_pesticides)
    else:
        print("Invalid prediction index.")
        predicted_class = None
        predicted_pesticides = None

    return predicted_class, predicted_pesticides

