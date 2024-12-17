import pandas as pd
import statsmodels.api as sm

def perform_regression(csv_file, target_variable):
    # Load the dataset
    data = pd.read_csv(csv_file)
    
    # Drop the first column from the dataset
    data = data.iloc[:, 1:]
    
    # Separate target variable (Y) and predictors (X)
    Y = data[target_variable]
    X = data.drop(columns=[target_variable, 'Oppo%', 'Edge%', 'Straight%', 'Weak%', 'Topped%', 'Under%', 'Flare/Burner%', 'Solid%', 'Launch-Angle-Sweet-Spot%', 'Barrel%', 'ZoneSwing%', 'Swing%', 'LD%', 'FB%', 'Meatball-Swing%', 'Pull%', '1st-PitchSwing%', 'ZoneContact%', 'Chase%', 'Meatball%', 'BBE', 'ChaseContact%', 'GB%', 'PU%'])
    
    # Add a constant to the predictors
    X = sm.add_constant(X)
    
    # Perform the regression
    model = sm.OLS(Y, X).fit()
    return model
    
def make_prediction_from_csv(model, new_data_csv):
    # Load new data from CSV file
    new_data = pd.read_csv(new_data_csv)

    # Exclude the columns specified in exclude_variables
    actual = new_data['WOBA']
    new_data = new_data.drop(columns=['WOBA'])

    # Add constant for intercept to new data
    new_data = sm.add_constant(new_data)

    # Make predictions using the fitted model
    predictions = model.predict(new_data)

    return [predictions, actual]

# Example usage:
# Fit the model first
model = perform_regression('data.csv', 'WOBP')

# Predict with a new CSV file
total = make_prediction_from_csv(model, '2023.csv')
predictions = total[0]
actual = total[1].tolist()
calculated = predictions.tolist()

#Find MAE
sum = 0
for i in range(len(actual)):
    sum += abs(actual[i] - calculated[i])
error = sum / len(actual)
print(error)
#MAE: 0.0063060574053542895