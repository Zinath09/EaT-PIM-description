from eatpim.rank_subs_in_recipe import execute_recipe_processing
from pathlib import Path
import pandas as pd
from tabulate import tabulate
import csv
file_name = 'substitution_50.csv'
with open(file_name, 'w') as file:
    for i in range(50):
        recipe, ing,  a = execute_recipe_processing(target_ingredient='', target_recipe='')

        print(f"\n___________{ing}___________")
        df = pd.DataFrame()
        for key in a.keys():
            # df[key] = list(zip(*a[key]))[0]
            row = [recipe, ing, list(zip(*a[key]))[0]]
            row_data = ','.join(str(item) for item in row)
            file.write(row_data + '\n')

print(tabulate(df, headers=df.columns ))


data = []
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

for row in data:
    print(row)



# recipe, ing,  a = execute_recipe_processing(target_ingredient='', target_recipe='')

# print(f"\n___________{ing}___________")
# df = pd.DataFrame()
# for key in a.keys():
#     df[key] = list(zip(*a[key]))[0]
# print(tabulate(df, headers=df.columns ))
