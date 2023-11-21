import pandas as pd
import matplotlib.pyplot as plt

# Exercise functions
def exercise_0(file):
    df = pd.read_csv(file)
    return df

def exercise_1(df):
    return df.describe()

def exercise_2(df, k):
    payment_df = df[df['type'] == k]
    return payment_df

def exercise_3(df, k):
    result_df = df[df['amount'] > k]
    return result_df

def exercise_4(df):
    isFraud_df = df.sort_values(by='isFraud', ascending=False) 
    return isFraud_df

def exercise_5(df):
    flagFraud_df = df.sort_index()
    return flagFraud_df

def exercise_6(df):
    correlations_df = df[['oldbalanceOrg', 'newbalanceOrig', 'newbalanceDest', 'amount', 'isFraud']].corr()
    return correlations_df

def exercise_7(df):
    total_fraud_loss = df[df['isFraud'] > 0]['amount'].sum()
    return total_fraud_loss

# Visual functions
def visual_1(df):
    transaction_counts = df['type'].value_counts()
    
    plt.figure(figsize=(10, 6))
    transaction_counts.plot(kind='bar', color='skyblue')
    plt.title('Distribution of Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.show()

def visual_2(df):
    fraud_counts = df['isFraud'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(fraud_counts, labels=['Non-Fraud', 'Fraud'], autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'])
    plt.title('Distribution of Fraud Transactions')
    plt.show()

def exercise_custom(df):
    result_custom = df.groupby('type')['amount'].mean()
    return result_custom

def visual_custom(df):
    fraud_data = df[df['isFraud'] == 1]
    plt.figure(figsize=(10, 6))
    plt.scatter(fraud_data['amount'], fraud_data['oldbalanceOrg'], color='red', alpha=0.5)
    plt.title('Scatter Plot of Amount vs Old Balance for Fraud Transactions')
    plt.xlabel('Amount')
    plt.ylabel('Old Balance Origin')
    plt.show()

# File name
file_name = 'transactions.csv'

# Read the CSV file into a DataFrame
df = exercise_0(file_name)

# Calling functions exercise and displaying results
result_1 = exercise_1(df)
print("Exercise 1:")
print(result_1)

result_2 = exercise_2(df, 'TRANSFER')
print("\nExercise 2:")
print(result_2)

result_3 = exercise_3(df, 10000)
print("\nExercise 3:")
print(result_3)

result_4 = exercise_4(df)
print("\nExercise 4:")
print(result_4)

result_5 = exercise_5(df)
print("\nExercise 5:")
print(result_5)

result_6 = exercise_6(df)
print("\nExercise 6:")
print(result_6)

result_7 = exercise_7(df)
print("\nExercise 7:")
print(result_7)

# Calling functions visual and displaying results
visual_1(df)
visual_2(df)

# Calling functions custom exercise and displaying results
resultExc_cust = exercise_custom(df)
print("\nExercise Custom:")
print(resultExc_cust)

# Calling functions custom visual and displaying results
visual_custom(df)
