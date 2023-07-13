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
all_decls
# %%
delcarant_list = []
for decl in all_decls[1:]:
    ppl_dict = {}
    ppl_dict["name"] = decl.find("div", class_="delcarant-info").text.strip()
    ppl_dict["data-id"] =decl.get("data-id")
    ppl_dict["link"] ="https://registry.cpcarmenia.am/declaration/?id=" + decl.get("data-id")
    ppl_dict["declaration-type"] = decl.find("div", class_="declaration-info").find("div", class_="name").text
    ppl_dict["institution"] = decl.find("div", class_="institution").text
    ppl_dict["position"] = decl.find("div", class_="position").text
    delcarant_list.append(ppl_dict)
# %%
delcarant_list
# %%
url 
# %%

#MAIN CODE!!!!

url = "https://registry.cpcarmenia.am/?fn&ln&md&po=%D5%A1%D5%BA%D6%85%D6%80%D5%AB%D5%B6%D5%AB%20%D5%AE%D5%A1%D5%A3%D5%B8%D6%82%D5%B4%20%D5%B8%D6%82%D5%B6%D5%A5%D6%81%D5%B8%D5%B2%20%D5%A3%D5%B8%D6%82%D5%B5%D6%84%D5%AB%20%D5%A2%D5%BC%D5%B6%D5%A1%D5%A3%D5%A1%D5%B6%D5%B1%D5%B4%D5%A1%D5%B6&y=2022&type&instg&inst"


def pages_maker(link, start_number, end_number): #link should be full page link, just without page number
    pages_list = []
    for i in range(start_number, end_number+1):
        pages_list.append(f'{link}&paging={i}')
    return pages_list
    
# %%
pages_maker(url, 1, 4)
# %%
def page_scraper(link): 
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    all_decls = soup.find_all("div", class_='declaration')
    delcarant_list = []
    for decl in all_decls[1:]:
        ppl_dict = {}
        ppl_dict["name"] = decl.find("div", class_="delcarant-info").text.strip()
        ppl_dict["data-id"] =decl.get("data-id")
        ppl_dict["link"] ="https://registry.cpcarmenia.am/declaration/?id=" + decl.get("data-id")
        ppl_dict["declaration-type"] = decl.find("div", class_="declaration-info").find("div", class_="name").text
        ppl_dict["institution"] = decl.find("div", class_="institution").text
        ppl_dict["position"] = decl.find("div", class_="position").text
        delcarant_list.append(ppl_dict)
    return delcarant_list
# %%
full_delcarant_list = []
for page in pages_maker(url, 1, 4):
    full_delcarant_list.extend(page_scraper(page))
# %%
len(full_delcarant_list)

df = pd.DataFrame(full_delcarant_list)
df.to_csv("ԱԾՈՒԳ_ delcarant_list.csv")
# %%
