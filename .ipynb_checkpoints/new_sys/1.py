#%%
import requests
from bs4 import BeautifulSoup as bs
import tqdm
import pandas as pd
# %%
url = "https://registry.cpcarmenia.am/?fn&ln&md&po=%D5%A1%D5%BA%D6%85%D6%80%D5%AB%D5%B6%D5%AB%20%D5%AE%D5%A1%D5%A3%D5%B8%D6%82%D5%B4%20%D5%B8%D6%82%D5%B6%D5%A5%D6%81%D5%B8%D5%B2%20%D5%A3%D5%B8%D6%82%D5%B5%D6%84%D5%AB%20%D5%A2%D5%BC%D5%B6%D5%A1%D5%A3%D5%A1%D5%B6%D5%B1%D5%B4%D5%A1%D5%B6&y=2022&type&instg&inst"
# %%
r = requests.get(url)
# %%
r.text
# %%
soup = bs(r.text, "html.parser")
# %%
all_decls = soup.find_all("div", class_='declaration')
# %%
soup.find_all("div", class_='declaration')[1].find("div", class_="delcarant-info").text.strip()

# %%
