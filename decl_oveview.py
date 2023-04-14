
#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
#%%
df = pd.read_csv("positions_info.csv")
df
# %%
mask = df['decl_title'].str.contains('2021', case=False, na=False)

# %%
yearly_2021_df = df[mask]
# %%
# %%

# %%
pattern = 'ստանձնելու.*2022'
mask = df['decl_title'].str.contains(pattern, case=False, na=False)

# %%
new_2022_df = df[mask]
# %%
df
# %%
filtered_df = pd.concat([yearly_2021_df, new_2022_df])
filtered_df
# %%
filtered_df.to_csv("filtered_data.csv")
# %%

# %%

# %%

# %%

# %%

# %%
df = pd.read_csv("mk_v2 - Sheet1.csv")
df
# %%
id_link_dict = zip(df.id.values.tolist(), df.decl_link.values.tolist())

# %%
# %%
len_list = []
for key, url in id_link_dict:
    len_dict ={}
    r = requests.get(url)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all(class_="tbl mcol")
    len_dict['id'] = key
    len_dict["len"] = len(tables)
    len_list.append(len_dict)

# %%
len_list
# %%
len_df = pd.DataFrame(len_list)
# %%
len_df
# %%
len_df.to_csv("len.csv")



# %%

merged_df = pd.merge(df, len_df, on='id')
merged_df
# %%
