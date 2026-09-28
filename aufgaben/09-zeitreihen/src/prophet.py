# Prophet model

# Importieren der notwendigen Bibliotheken
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import seaborn as sns

# Laden des "flights"-Datensatzes aus Seaborn
data = sns.load_dataset("flights")
data.rename(columns={"year": "Year", "month": "Month", "passengers": "Sales"}, inplace=True)

# Erstellen einer Datetime-Spalte für Prophet
data["Month"] =   # Umwandeln von 'Month' in Strings
data["Date"] = pd.to_datetime(data["Year"].astype(str) + "-" + data["Month"])

# Behalten nur der relevanten Spalten
data = data[["Date", "Sales"]]


# Vorbereitung der Daten für Prophet
data_prophet = data.rename(columns={"Date": "ds", "Sales": "y"})

# Prophet-Modell erstellen
model = ???(yearly_seasonality=???)
model.fit...

# Vorhersage für die nächsten ... Monate
future = model.make_future_dataframe(periods=???, freq="???
forecast = model.predict...

# Visualisierung der Vorhersagen
fig = model.plot()
plt.title("Prognose der monatlichen Flüge mit Prophet")
plt.xlabel("Datum")
plt.ylabel("Anzahl der Passagiere (Sales)")
plt.show()

# Komponenten der Vorhersage anzeigen
fig2 = model.plot_components(forecast)
plt.show()

# Teilen der Daten in Trainings- und Testdaten
train = data_prophet.iloc[:-12]
test = data_prophet.iloc[-12:]

# Modell auf Trainingsdaten anpassen
model_train = ???(yearly_seasonality=??)
model_train.fit...

# Vorhersage auf Testdaten
future_test = model_train.make_future_dataframe(periods=???, freq=???)
forecast_test = 

# Berechnung des Mean Squared Error (MSE)
