import matplotlib.pyplot as plt
import re
import csv
import pandas as pd
from numpy import sort


path_source = 'csv/autores.csv'
path_data = 'results'

df = pd.read_csv(path_source, usecols=['Year',	'Author 1',	'Country 1',	'City 1',	'University 1',	'Department 1',	'Gender',	'Type']) #, encoding="ISO-8859-1"

#genero
autores = {}
for i in range(0, len(df.index)):
    aux_uni = sort([df['Author 1']])
    # print aux_uni
    autores[]

