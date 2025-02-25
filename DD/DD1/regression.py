import pandas as pd
import statsmodels.api as sm

def perform_regression(csv_file, target_variable):
    # Load the dataset
    data = pd.read_csv(csv_file)
    
    # Drop the first column from the dataset
    data = data.iloc[:, 1:]
    
    # Separate target variable (Y) and predictors (X)
    Y = data[target_variable]
    X = data.drop(columns=[target_variable, "G", "H", "SLG", "BB", "SO", "OBA", "1B", "3B", "BA"])
    
    # Add a constant to the predictors
    X = sm.add_constant(X)
    
    # Perform the regression
    model = sm.OLS(Y, X).fit()
    # print(model.summary())
    return model

def make_prediction_from_csv(model, new_data_csv):
    # Load new data from CSV file
    new_data = pd.read_csv(new_data_csv)

    # Exclude the columns specified in exclude_variables
    new_data = new_data.drop(columns=["G", "H", "SLG", "BB", "SO", "OBA", "1B", "3B", "BA"])

    # Add constant for intercept to new data
    new_data = sm.add_constant(new_data)

    # Make predictions using the fitted model
    predictions = model.predict(new_data)

    return predictions

# Fit the model first
model_real = perform_regression('train.csv', 'W')
# print(model.summary())

# intercept = model_real.params[0]  

# coefficients = model_real.params[1:]  

# # Constructing the equation string
# equation_string = "y = " + str(intercept) 
# for i, coeff in enumerate(coefficients):

#     equation_string += " + " + str(coeff) + " * x" + str(i+1)
# print(equation_string) 
#Equation: y = -67.0921049845063 + -0.09350184405582775 * x1 + -0.06596865726982984 * x2 + 0.05868997083642177 * x3 + 241.23257863972964 * x44

prediction = make_prediction_from_csv(model_real, 'test.csv')
for row in prediction:
    print(row)

