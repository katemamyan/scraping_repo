#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
# %%
profiles_df = pd.read_csv("links_of_pages.csv")
dict_new = dict(zip(profiles_df.id.values.tolist(), profiles_df.profile_link.values.tolist()))
# %%
dict_new
# %%
info_dict = {}
for key, value in dict_new.items():
    itnernal_dict = {}
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    itnernal_dict['name'] = soup.find("div", class_="pers-title").find("span").text.strip()
    itnernal_dict['position'] = soup.find("div", class_="pers-title").find("strong").text.strip()
    itnernal_dict['date'] = soup.find("div", class_="pers-title").contents[-1].strip()
    itnernal_dict['link'] = value
    info_dict[key] = itnernal_dict
info_dict

df = pd.DataFrame(info_dict)
df = df.transpose()

df.to_csv("general_info.csv") #general info
# %%
#
#  %%
#
# %%

# %%
positions_dict = {}
for key, value in dict_new.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    li_list = soup.find("div", class_="static-box__content").find("ul").find_all("li")
    internal_list = []
    for li in li_list:
        itnernal_dict ={}
        itnernal_dict['link'] = value
        itnernal_dict['position'] = li.contents[-1].strip()
        itnernal_dict['decl_title'] = li.find("a").text.strip()
        itnernal_dict['decl_link'] = f'http://cpcarmenia.am{li.find("a").get("href")}'
        internal_list.append(itnernal_dict)
    positions_dict[key] = internal_list
positions_dict
# %%

df_list = [pd.DataFrame(positions_dict[key]) for key in positions_dict]
df = pd.concat(df_list, keys=positions_dict.keys())
print(df)
# %%
df.to_csv("positions_info.csv") #positions_info
# %%
# %%
#
#  %%
#
# %%

trial_url = "http://cpcarmenia.am//hy/declarations-registry/user_id=6692/"
r = requests.get(trial_url)
r.status_code
# %%
soup = bs(r.content, "html.parser")
# %%
soup.find("table", {'id':"relations-decl"}).find_all("tr")[1:][0].find_all("li")[0].find("a").text

soup.find("table", {'id':"relations-decl"}).find_all("tr")[1:][0].find_all("li")[0].text

soup.find("table", {'id':"relations-decl"}).find_all("tr")[1:][0].find_all("td")[0]
soup.find("table", {'id':"relations-decl"}).find_all("tr")[1:][0].find_all("td")[1]

# %%
relatives_dict = {}
for key, value in dict_new.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    try:
        all_tr = soup.find("table", {'id':"relations-decl"}).find_all("tr")
    except:
        print(key, value)
    list_rel = []
    for i, tr in enumerate(all_tr[1:]):
        dict_rel = {}
        dict_rel['id'] = f'{key}_{str(i+1).rjust(2,"0")}'
        dict_rel['name'] = tr.find_all("td")[0].text.strip()
        dict_rel['connection_type'] = tr.find_all("td")[1].text.strip()
        li_list = []
        for li in tr.find_all("li"):
            li_dict = {}
            li_dict['decl_name'] = li.find("a").text
            li_dict['decl_link'] = f'http://cpcarmenia.am{li.find("a").get("href")}'
            li_list.append(li_dict)
        dict_rel['decls'] = li_list
        list_rel.append(dict_rel)
    relatives_dict[key] = list_rel
relatives_dict
# %%
# 
relatives_dict

# %%
print(positions_dict)


# %%
