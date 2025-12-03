import pandas as pd

#Blatt 1

# 1 Datensatz einlesen
column_names=['age', 'workclass', 'final_weight', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
adult_income = pd.read_csv(filepath_or_buffer='./src/adultcsv_task/adult.csv',names=column_names, na_values=' ?') # na_values -> verschiedene darstellungsarten von NaN Values vereinheitlichen


# 2 Erste Inspektion der Daten
print(adult_income.head(5))
print("Fehlende Werte: ", adult_income.isnull().sum()) #gibt spaltenweise die summe der fehlenden Werte an

# 3 Berechnung statistischer Kennzahlen

# Berechnungen fuer das Alter, fuer education-num und hours-per-week koennen die selben Funktionen verwendet werden
print("Mean alter: ", adult_income['age'].mean())
print("Median alter: ", adult_income['age'].median())
print("Haeufigstes alter: ", adult_income['age'].mode()[0])
print("Varianz alter: ", adult_income['age'].var())
print("Standardabweichung alter: ", adult_income['age'].std())
print("Interquartilsabstand: ", adult_income['age'].quantile(0.75) - adult_income['age'].quantile(0.25))


#Blatt 2
# 1 Einkommen in Altersgruppen aufteilen:

# einfacher über pd.cut?
df_young = adult_income[(adult_income['age'] >= 18) & (adult_income['age'] <= 30)]
df_middle = adult_income[(adult_income['age'] >= 31) & (adult_income['age'] <= 50)]
df_old = adult_income[adult_income['age'] > 50]

print("Median Young: ", df_young['hours-per-week'].median())
print("Varianz Young: ", df_young['hours-per-week'].var())
print("Median Middle: ", df_middle['hours-per-week'].median())
print("Varianz Middle: ", df_middle['hours-per-week'].var())
print("Median Old: ", df_old['hours-per-week'].median())
print("Varianz Old: ", df_old['hours-per-week'].var())

# Die alte Altersgruppe zeigt die größte Variabilität der Arbeitszeit auf. Dies ist erkennbar an der Varianz (diese zeigt an wie sehr es streut) 
# Im Median arbeiten alle Altersgruppen gleich viel. Alle arbeiten 40 Stunden (Bei vielen 40 Stunden erkennt man, dass viele Menschen in der Gesellschaft Vollzet arbeiten)

# 2 Bildungsniveau und Einkommen
df_income_groups_mean = adult_income.groupby('income')['education-num'].mean()
df_income_groups_median = adult_income.groupby('income')['education-num'].median()
print("Mean education: ", df_income_groups_mean)
print("Median education: ", df_income_groups_median)
# education-num anzahl der Jahre die man in Bildung investiert hat
# Menschen, die mehr Jahre in Bildung investiert haben (im median 12), haben ein groesseres Einkommen als 50K

# 3 Arbeitszeitunterschiede zwischen Geschlechtern
df_workhours_sex = adult_income.groupby('sex')['hours-per-week']
print('Mean hours per week:', df_workhours_sex.mean())
print('Standardabweichung: ', df_workhours_sex.std())
# Männer arbeiten im Median etwa sechs Stunden mehr pro Woche als Frauen. Die Streuung der Arbeitszeiten ist bei beiden Geschlechtern aehnlich groß, was bedeutet, dass innerhalb jeder Gruppe sowohl kürzere als auch längere Arbeitszeiten vorkommen. 

# 4 Bildungsabschluss erfolgreicher Personen
print("Haeufigster Bildungsabschluss von Personen mit hohem Einkommen: ", adult_income.groupby('income')['education'].apply(lambda x: x.mode()[0]))
# Moegliche Aussage: Menschen mit hoeherer Bildung haben ein hoeheres Einkommen

# 5 Altersverteilung nach Einkommensklassen
df_income_grouped_q1 = adult_income.groupby('income')['age'].quantile(0.25)
df_income_grouped_q3 = adult_income.groupby('income')['age'].quantile(0.75)

print("25 Prozent Quantil des Alters: ", df_income_grouped_q1)
print("75 Prozent Quantil des Alters: ", df_income_grouped_q3)
# Personen mit hohen Einkommen (>50K) sind im Durschnitt aelter

# Create a sample DataFrame
data = pd.DataFrame({
 'Day': ['Mon', 'Mon', 'Tue', 'Tue', 'Wed', 'Wed', 'Thu', 'Mon'],
 'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A'],
 'Sales': [200, 150, 220, 130, 250, 170, 300, 200],
 'Profit': [50, 40, 60, 35, 70, 50, 90, 1]
 })
# Create a pivot table to summarize sales by Day and Category
pivot_table = pd.pivot_table(data, values='Sales', index='Day', columns='Category', 
aggfunc='sum')

print(pivot_table)
print(pivot_table.index)