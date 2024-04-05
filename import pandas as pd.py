import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the spreadsheet into a DataFrame
file_path = r'C:\Users\VaterRW14\Downloads\baseball.xlsx'
data = pd.read_excel(file_path)

# Display the data to understand its structure
print("Loaded data:")
print(data.head())

# Select relevant columns for modeling
features = ['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']
target = 'Playoffs'

# Prepare the feature matrix X and the target vector y
X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Function to predict playoffs based on user input
def predict_playoffs():
    print("\nEnter the statistics for the team to predict playoffs:")
    runs_scored = float(input("Runs Scored: "))
    runs_allowed = float(input("Runs Allowed: "))
    wins = float(input("Wins: "))
    obp = float(input("OBP: "))
    slg = float(input("SLG: "))
    batting_average = float(input("Team Batting Average: "))

    # Make predictions
    new_data = [[runs_scored, runs_allowed, wins, obp, slg, batting_average]]
    prediction = model.predict(new_data)

    print("\nPrediction:")
    if prediction[0] == 1:
        print("The team is predicted to make the playoffs.")
    else:
        print("The team is predicted not to make the playoffs.")

# Predict playoffs for user-inputted team
predict_playoffs()
