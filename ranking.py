from eatpim.rank_subs_in_recipe import execute_recipe_processing
from pathlib import Path
import pandas as pd
from tabulate import tabulate
import json
file_name = 'substitution_50.json'
import json

data = []
with open(file_name, 'w') as file:
    for i in range(50):
        print(i, end = " ")
        recipe, ing, rankings = execute_recipe_processing(target_ingredient='', target_recipe='')
        print(f"\n___________{ing}___________")
        for key in rankings.keys():
            data.append([recipe, ing,  [str(sublist[0]) for sublist in rankings[key]]])

with open(file_name, 'w') as file:
    json.dump(data, file)



# recipe, ing,  a = execute_recipe_processing(target_ingredient='', target_recipe='')

# print(f"\n___________{ing}___________")
# df = pd.DataFrame()
# for key in a.keys():
#     df[key] = list(zip(*a[key]))[0]
# print(tabulate(df, headers=df.columns ))
