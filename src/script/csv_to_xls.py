import pandas as pd

read_file = pd.read_csv (r'../original_data/background_data_variable_description.csv', sep=';')
read_file.to_excel (r'../../bld/background_data_variable_description.xlsx', index = None, header=True)

read_file = pd.read_csv (r'../original_data/background_data_long_variable_description.csv', sep=';')
read_file.to_excel (r'../../bld/background_data_long_variable_description.xlsx', index = None, header=True)

read_file = pd.read_csv (r'../original_data/covid_variable_description.csv', sep=';')
read_file.to_excel (r'../../bld/covid_variable_description.xlsx', index = None, header=True)
