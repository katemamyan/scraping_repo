#%%
import requests
from bs4 import BeautifulSoup as bs
import tqdm
import pandas as pd
# %%
url = "http://cpcarmenia.am/hy/declarations-registry/user_id=538/"

r = requests.get(url)
soup = bs(r.content, "html.parser")
soup.selec
# %%
soup.select_one("body > main > div.static-box > div > div.static-box__content > div > ul")
# %%
uls = soup.find_all("ul")
uls[3]
# %%
ul_dict = {}
for ul in uls:
    ul_dict['name'] = 
