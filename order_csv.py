import csv
import pandas as pd

# Read the data from the CSV file
input_file = 'Player data map.csv'
output_file = 'sorted_output.csv'


# Read in your .csv files as dataframes
# df is a common standard for naming a dataframe. You can
# name them something more descriptive as well.
# Using a descriptive name is helpful when you are dealing
# with multiple .csv files.
df = pd.read_csv(input_file)

# the .sort_values method returns a new dataframe, so make sure to
# assign this to a new variable.
sorted_df = df.sort_values(by=["Address Dec"], ascending=True)

# Index=False is a flag that tells pandas not to write
# the index of each row to a new column. If you'd like
# your rows to be numbered explicitly, leave this as
# the default, True
sorted_df.to_csv(output_file, index=False)