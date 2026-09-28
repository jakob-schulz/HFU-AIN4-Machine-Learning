
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Airline Passengers dataset
from statsmodels.datasets import get_rdataset
data = get_rdataset("AirPassengers", "datasets").data

# Tme series dataframe 
data["time"] = pd.date_range(start="1949-01", periods=len(data), freq=???)
data.set_index("time", inplace=True)
data.rename(columns={"value": "Passengers"}, inplace=True)

#  Moving Average der alten Daten
window_size = 
data["Moving_Avg"] = data["Passengers"].rolling(...)

# Im DataFrame 12 Monate in Zukunft vorbereiten
future_dates = pd.date_range(start=data.index[-1] + pd.DateOffset(months=1), periods=12, freq="M")
future_data = pd.DataFrame(index=future_dates, columns=data.columns)

# Letzte 12 Monate als Durchschnitt
forecast_value = ...iloc
future_data["Moving_Avg"] = 

# Daten kombinieren
forecasted_data = 

# Fehlermetrik
mse = mean_squared_error(,)

# Plotten 
plt.figure(figsize=(12, 6))
plt.plot(,)
plt.title("Vorhersager mit Moving Average")
plt.xlabel("Datum")
plt.ylabel("Anzahl Passagiere")