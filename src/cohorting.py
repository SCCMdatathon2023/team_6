# -*- coding: utf-8 -*-
"""cohorting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DtzI29UQsBC0RgM1Bja9svpx2gHSds3L
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import pandas as pd
from google.colab import files
from google.colab import auth
auth.authenticate_user()
print('Authenticated')

# %load_ext google.colab.data_table
# %env GOOGLE_CLOUD_PROJECT = sccm-datathon-2023-participant

# Commented out IPython magic to ensure Python compatibility.
# %%bigquery VIRUS_demographics --project sccm-datathon-2023-participant
# SELECT * FROM `sccm-discovery.VIRUS.coredata1_2`

VIRUS_demographics = pd.DataFrame(VIRUS_demographics)
VIRUS_demographics['sex'] = VIRUS_demographics['sex'].replace(1.0, 'Male')
VIRUS_demographics['sex'] = VIRUS_demographics['sex'].replace(2.0, 'Female')
VIRUS_demographics['sex'] = VIRUS_demographics['sex'].replace(3.0, 'Intersex')
VIRUS_demographics['sex'] = VIRUS_demographics['sex'].replace(4.0, 'Transgender')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(1.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(2.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(3.0, 'Black')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(4.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(5.0, 'White')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(6.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(7.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(8.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(9.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(10.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(11.0, 'Other')
VIRUS_demographics['race'] = VIRUS_demographics['race'].replace(12.0, 'Other')

VIRUS_demographics['ethnic_group'] = VIRUS_demographics['ethnic_group'].replace(1.0, 'Hispanic')
VIRUS_demographics['ethnic_group'] = VIRUS_demographics['ethnic_group'].replace(0.0, 'Non-Hispanic')
VIRUS_demographics['ethnic_group'] = VIRUS_demographics['ethnic_group'].replace(2.0, 'Non-Hispanic')
VIRUS_demographics['ethnic_group'] = VIRUS_demographics['ethnic_group'].replace(3.0, 'Non-Hispanic')

cols=['sex','bmi_value','WHO_Region','race','age','ethnic_group','day_prior_covid19_symptoms','days_prior_covid_testing']
oxygenation_other	STRING	NULLABLE
oxygenation_methods_2___0

newDF=VIRUS_demographics[cols]

def pychart(dayPrior):
  if 0 < dayPrior < 14:
    return "goodRange"
  elif pd.isna(dayPrior):
    return 'badNull'
  else:
    return "badRange"


newDF['priorSymptomPi']=newDF['day_prior_covid19_symptoms'].apply(pychart)
newDF['priorTestPi']=newDF['days_prior_covid_testing'].apply(pychart)

newDF['priorSymptomPi'].unique()