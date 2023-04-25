#%%
import requests
from bs4 import BeautifulSoup as bs
import tqdm
import pandas as pd
# %%
def profiles(section_url, department_name, pages_number): #function, that collects profiles and IDs from given section in cpcarmenia
    profiles_links = []
    for page in range(pages_number):
        r = requests.get(f'{section_url};page={page+1}/')
        soup = bs (r.content, "html.parser")
        profiles_link = [f'http://cpcarmenia.am/{soup.get("href")}' for soup in soup.find_all("a", class_="pers-fullname")]
        profiles_links.extend(profiles_link)
    
    profiles_link_dict = {}
    for i, link in enumerate(profiles_links):
        profiles_link_dict[f'{department_name}_{str(i+1).rjust(2,"0")}'] = link # rjust function add 0 before 1-character number to make it 2-character number
    return profiles_link_dict
# %% #all dicts together
profiles_dict = {}
profiles_dict.update(profiles("http://cpcarmenia.am/hy/declarations-registry/group_id=5740", "ԿԿՀ", 1))
profiles_dict.update(profiles("http://cpcarmenia.am/hy/declarations-registry/group_id=9716", "ՀԿ", 5))
profiles_dict.update(profiles("http://cpcarmenia.am/hy/declarations-registry/firstname=;lastname=;position=%D5%B0%D5%A1%D5%AF%D5%A1%D5%AF%D5%B8%D5%BC%D5%B8%D6%82%D5%BA%D6%81%D5%AB%D5%B8%D5%B6%20%D5%A4%D5%A1%D5%BF%D5%A1%D6%80%D5%A1%D5%B6%D5%AB;year=;", "ՀԴԴ", 2))
profiles_dict.update(profiles("http://cpcarmenia.am/hy/declarations-registry/firstname=;lastname=;position=%D5%A1%D5%BA%D6%85%D6%80%D5%AB%D5%B6%D5%AB%20%D5%AE%D5%A1%D5%A3%D5%B8%D6%82%D5%B4%20%D5%B8%D6%82%D5%B6%D5%A5%D6%81%D5%B8%D5%B2;year=", "ԱԾՈՒԳ", 1))
# %%
profiles_dict #final dict with all profiles' links from givem sections
# %%
df = pd.DataFrame.from_dict(profiles_dict.items())
# %%
df.columns = ['id', 'profile_link']
df
# %%
df.to_csv("links_of_pages.csv")
# %%
