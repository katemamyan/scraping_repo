#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
# %%
#%%
new_df = pd.read_csv("mk_v2 - ստանձմաններ_2022.csv")
new_dict = dict(zip(new_df.id.values.tolist(), new_df.decl_link.values.tolist()))
# %%
len(new_dict)
# %%
df = pd.read_csv("mk - հայտարարագրերի կառուցվածք(ստանձման 2022).csv")
# %%
names_dict = dict(zip(df.number.values.tolist(), df.name.values.tolist()))
names_dict
# %%

for number, name in names_dict.items(): 
    df_final = pd.DataFrame()
    for key, value in new_dict.items():
        r = requests.get(value)
        soup = bs(r.content, "html.parser")
        tables = soup.find_all("table")
        try:
            rows = tables[number-1].find_all('tr')
            for row in rows:
                data = []
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)
                df = pd.DataFrame(data)
                df = df.dropna(how='all') # to remove empty rows
                df['id'] = key
                df_final = pd.concat([df_final, df], ignore_index=True)
        except:
            pass
    df_final.to_csv(f'2022 | {names_dict[number][:30]}.csv')
# %%
