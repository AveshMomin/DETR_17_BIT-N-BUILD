import pandas as pd
import joblib

def predict_week(week):
    # Load the model from the .joblib file
    loaded_model = joblib.load('./decision_tree_model.pkl')

    # Make predictions on new data
    X_new = pd.DataFrame({'Standard\nWeek': [week]})
    predictions = loaded_model.predict(X_new)
    print("Predictions:", predictions)

    # Decode the predictions back to original text values
    pest_mapping = {
        0: 'AmericanBollworm',
        1: 'AmericanBollworm-Larva',
        2: 'Aphid',
        3: 'Jassid',
        4: 'Mealybug',
        5: 'PinkBollworm-Larva',
        6: 'Spodoptera',
        7: 'SpottedBollworm-Larva',
        8: 'Thrips',
        9: 'Whitefly'
    }

    # Map numeric predictions to pest names using the mapping dictionary
    pest_names = [pest_mapping[pred] for pred in predictions]

    print("Decoded Predictions (Pest Names):", pest_names)

    # Map pest names to pesticides
    pesticides_mapping = {
        'AmericanBollworm': ['Pyrethroids', 'Organophosphates', 'Neonicotinoids'],
        'AmericanBollworm-Larva': ['Bacillus thuringiensis (Bt)', 'Insect growth regulators (e.g., methoxyfenozide)'],
        'Aphid': ['Neonicotinoids', 'Pyrethroids', 'Insecticidal soaps'],
        'Jassid': ['Neonicotinoids', 'Pyrethroids', 'Carbamates'],
        'Mealybug': ['Neonicotinoids', 'Insecticidal soaps', 'Systemic insecticides'],
        'PinkBollworm-Larva': ['Bacillus thuringiensis (Bt)', 'Insect growth regulators (e.g., diflubenzuron)'],
        'Spodoptera': ['Bacillus thuringiensis (Bt)', 'Pyrethroids', 'Organophosphates'],
        'SpottedBollworm-Larva': ['Bacillus thuringiensis (Bt)', 'Insect growth regulators (e.g., methoxyfenozide)'],
        'Thrips': ['Neonicotinoids', 'Spinosad', 'Pyrethroids'],
        'Whitefly': ['Neonicotinoids', 'Insect growth regulators (e.g., pyriproxyfen)', 'Pyrethroids']
    }

    # Get respective pesticides based on pest names
    pesticides = [pesticides_mapping[pest] for pest in pest_names]

    print("Respective Pesticides:", pesticides)

    return pest_names, pesticides

