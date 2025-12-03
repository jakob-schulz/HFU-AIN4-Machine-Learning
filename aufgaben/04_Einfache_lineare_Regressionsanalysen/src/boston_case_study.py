from ISLP import load_data
from ISLP.models import (ModelSpec as MS, summarize, poly)
import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
import statsmodels.api as sm

Boston = load_data("Boston")
Boston.columns()
#Modellmatrix erzeugen und mit len für Intercept füllen
X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]), 'lastat': Boston['lstat']})
X[:4]
#Respnsevariable definieren
y = Boston['medv']
#Model spezifizieren
model = sm.OLS(y,X)
#Model fitten
results = model.fit()
#Regressionstabelle auswerten
results.summary()