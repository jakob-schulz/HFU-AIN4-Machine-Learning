import pandas as pd

column_names=['age', 'workclass', 'final_weight', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
adult_income = pd.read_csv(filepath_or_buffer='./src/adult.csv',names=column_names, na_values=' ?') # na_values -> verschiedene darstellungsarten von NaN Values vereinheitlichen

#print first five lines
print(adult_income.head(5))

# search vor missing entries
#column_names.isnull().sum()

# calculations for age
print("Mean age ", adult_income['age'].mean())