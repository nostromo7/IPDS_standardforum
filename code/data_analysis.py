import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt

survey_covid_names = pd.read_csv('../data/survey_covid_variables_names_labels.csv', header=0)

survey_covid = pd.read_csv('../data/survey_covid_variables_data.csv',
                           header=0)
print(survey_covid['co05_01'].value_counts())
print(survey_covid.shape)
print(survey_covid.columns.sort_values())

exit(0)
