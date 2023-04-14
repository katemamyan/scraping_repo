#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
# %%
#%%
yearly_df = pd.read_csv("mk_v2 - տարեկաններ_2021.csv")
yearly_dict = dict(zip(yearly_df.id.values.tolist(), yearly_df.decl_link.values.tolist()))
# %%
import itertools # for getting slice of dictionary
trial_yearly_dict = dict(itertools.islice(yearly_dict.items(), 10))
print(trial_yearly_dict)
# %%
df_final = pd.DataFrame()
for key, value in trial_yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[1].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_final = pd.concat([df_final, df], ignore_index=True)


# %%
print(df_final)
df_final.to_csv("trial.csv")     
# %%
#MAIN CODE FOR SCRAPE ALL TABLES FROM YEARLY 2021 DECLS

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
# %%
yearly_df = pd.read_csv("mk_v2 - տարեկաններ_2021.csv")
yearly_dict = dict(zip(yearly_df.id.values.tolist(), yearly_df.decl_link.values.tolist()))

# %%
# TABLE 2 | Ա.2. Հայտարարատու պաշտոնատար անձի ընտանիքի անդամների մասին տվյալները

df_2_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[1].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_2_final = pd.concat([df_2_final, df], ignore_index=True)

# %%
df_2_final.to_csv("2021 | Ա.2. Հայտարարատու պաշտոնատար անձի ընտանիքի անդամների մասին տվյալները.csv")
# %%
# TABLE 3 | Ա.3. Հայտարարատու պաշտոնատար անձի հետ մերձավոր ազգակցությամբ կամ խնամիությամբ կապված համատեղ չբնակվող անձանց մասին տվյալները

df_3_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[2].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_3_final = pd.concat([df_3_final, df], ignore_index=True)

# %%
df_3_final.to_csv("2021 | Ա.3. Հայտարարատու պաշտոնատար անձի հետ մերձավոր ազգակցությամբ կամ խնամիությամբ կապված համատեղ չբնակվող անձանց մասին տվյալները.csv")
# %%
# TABLE 4 | Բ.1.1. Տվյալ տարվա սկզբում առկա անշարժ գույքը


df_4_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[3].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_4_final = pd.concat([df_4_final, df], ignore_index=True)

# %%
df_4_final.to_csv("2021 | Բ.1.1. Տվյալ տարվա սկզբում առկա անշարժ գույքը.csv")

# %%
# TABLE 5 | Բ.1.2. Տվյալ տարվա ընթացքում ձեռք բերված և օտարված անշարժ գույքը


df_5_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[4].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_5_final = pd.concat([df_5_final, df], ignore_index=True)

# %%
df_5_final.to_csv("2021 | Բ.1.2. Տվյալ տարվա ընթացքում ձեռք բերված և օտարված անշարժ գույքը.csv")
# %%
# TABLE 6 | Բ.1.3. Տվյալ տարվա վերջում առկա անշարժ գույքը

df_6_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[5].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_6_final = pd.concat([df_6_final, df], ignore_index=True)

# %%
df_6_final.to_csv("2021 | Բ.1.3. Տվյալ տարվա վերջում առկա անշարժ գույքը.csv")
# %%
# TABLE 7 | Բ.1.4. Հայտարարատուի կողմից տվյալ տարվա ընթացքում 90 օրից ավելի փաստացի տիրապետվող անշարժ գույք

df_7_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[6].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_7_final = pd.concat([df_7_final, df], ignore_index=True)

# %%
df_7_final.to_csv("2021 | Բ.1.4. Հայտարարատուի կողմից տվյալ տարվա ընթացքում 90 օրից ավելի փաստացի տիրապետվող անշարժ գույք.csv")
# %%
# TABLE 8 | Բ.2.1. Տվյալ տարվա սկզբում առկա տրանսպորտի միջոց

df_8_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[7].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_8_final = pd.concat([df_8_final, df], ignore_index=True)

# %%
df_8_final.to_csv("2021 | Բ.2.1. Տվյալ տարվա սկզբում առկա տրանսպորտի միջոց.csv")
# %%
# TABLE 9 | Բ.2.2. Տվյալ տարվա ընթացքում ձեռք բերված և օտարված տրանսպորտի միջոց


df_9_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[8].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_9_final = pd.concat([df_9_final, df], ignore_index=True)

# %%
df_9_final.to_csv("2021 | Բ.2.2. Տվյալ տարվա ընթացքում ձեռք բերված և օտարված տրանսպորտի միջոց.csv")
# %%
# TABLE 10 | Բ.2.3. Տվյալ տարվա վերջում առկա տրանսպորտի միջոց


df_10_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[9].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_10_final = pd.concat([df_10_final, df], ignore_index=True)

# %%
df_10_final.to_csv("2021 | Բ.2.3. Տվյալ տարվա վերջում առկա տրանսպորտի միջոց.csv")
# %%
# TABLE 11 | Բ.2.4. Հայտարարատուի կողմից տվյալ տարվա ընթացքում 90 օրից ավելի փաստացի տիրապետվող տրանսպորտի միջոց 


df_11_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[10].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_11_final = pd.concat([df_11_final, df], ignore_index=True)

# %%
df_11_final.to_csv("2021 | Բ.2.4. Հայտարարատուի կողմից տվյալ տարվա ընթացքում 90 օրից ավելի փաստացի տիրապետվող տրանսպորտի միջոց.csv")
# %%
# TABLE 12 | Բ.3.1. Բաժնային արժեթղթեր և այլ ներդրումներ 

df_12_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[11].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_12_final = pd.concat([df_12_final, df], ignore_index=True)

# %%
df_12_final.to_csv("2021 | Բ.3.1. Բաժնային արժեթղթեր և այլ ներդրումներ.csv")
# %%
# TABLE 13 | Բ.3.2. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձին սեփականության իրավունքով պատկանող բաժնային արժեթղթեր և այլ ներդրումներ կամ բաժնային արժեթղթեր և այլ ներդրումներ, որից փաստացի օգուտ է ստանում կամ այն տնօրինում է հայտարարատուն

df_13_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[12].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_13_final = pd.concat([df_13_final, df], ignore_index=True)

# %%
df_13_final.to_csv("2021 | Բ.3.2. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")

# %%
# TABLE 14 | Բ.3.3. Պարտքային և այլ արժեթղթեր

df_14_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[13].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_14_final = pd.concat([df_14_final, df], ignore_index=True)

# %%
df_14_final.to_csv("2021 | Բ.3.3. Պարտքային և այլ արժեթղթեր.csv")
# %%
# TABLE 15 | Բ.3.4. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձին սեփականության իրավունքով պատկանող պարտքային և այլ արժեթղթեր, կամ պարտքային և այլ արժեթղթեր, որից փաստացի օգուտ է ստանում կամ տնօրինում է հայտարարատուն

df_15_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[14].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_15_final = pd.concat([df_15_final, df], ignore_index=True)

# %%
df_15_final.to_csv("2021 | Բ.3.4. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")
# %%
# TABLE 16 | Բ.4.1. Հանձնված և վերադարձված փոխառություններ

df_16_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[15].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_16_final = pd.concat([df_16_final, df], ignore_index=True)

# %%
df_16_final.to_csv("2021 | Բ.4.1. Հանձնված և վերադարձված փոխառություններ.csv")
# %%
# TABLE 17 | Բ.4.2. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձի հանձնված և վերադարձված փոխառություններ, որից փաստացի օգուտ է ստանում կամ տնօրինում է հայտարարատուն

df_17_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[16].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_17_final = pd.concat([df_17_final, df], ignore_index=True)

# %%
df_17_final.to_csv("2021 | Բ.4.2. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")
# %%
# TABLE 18 | Բ.4.3. Բանկային ավանդներ

df_18_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[17].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_18_final = pd.concat([df_18_final, df], ignore_index=True)

# %%
df_18_final.to_csv("2021 | Բ.4.3. Բանկային ավանդներ.csv")
# %%
# TABLE 19 | Բ.4.4. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձի բանկային ավանդներ, որից փաստացի օգուտ է ստանում կամ տնօրինում է հայտարարատուն

df_19_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[18].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_19_final = pd.concat([df_19_final, df], ignore_index=True)

# %%
df_19_final.to_csv("2021 | Բ.4.4. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")
# %%
# TABLE 20 | Բ.5.1. Տվյալ տարվա սկզբում առկա՝ չորս միլիոն դրամից կամ դրան համարժեք արտարժույթից ավելի արժեք ունեցող գույք (թանկարժեք գույք)

df_20_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[19].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_20_final = pd.concat([df_20_final, df], ignore_index=True)

# %%
df_20_final.to_csv("2021 | Բ.5.1. Տվյալ տարվա սկզբում առկա՝ չորս միլիոն դրամից կամ դրան համարժեք արտարժույթից ավելի արժեք ունեցող գույք.csv")
# %%
# TABLE 21 | Բ.5.2. Տվյալ տարվա ընթացքում ձեռք բերված և օտարված՝ չորս միլիոն դրամից կամ դրան համարժեք արտարժույթից ավելի արժեք ունեցող գույք (թանկարժեք գույք)

df_21_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[20].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_21_final = pd.concat([df_21_final, df], ignore_index=True)

# %%
df_21_final.to_csv("2021 | Բ.5.2. Տվյալ տարվա ընթացքում ձեռք բերված և օտարված թանկարժեք գույք.csv")
# %%

# TABLE 22 | Բ.5.3. Տվյալ տարվա վերջում առկա՝ չորս միլիոն դրամից կամ դրան համարժեք արտարժույթից ավելի արժեք ունեցող գույք (թանկարժեք գույք) 

df_22_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[21].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_22_final = pd.concat([df_22_final, df], ignore_index=True)

# %%
df_22_final.to_csv("2021 | Բ.5.3. Տվյալ տարվա վերջում առկա՝ չորս միլիոն դրամից կամ դրան համարժեք արտարժույթից ավելի արժեք ունեցող գույք.csv")
# %%
# TABLE 23 | Բ.5.4 Հայտարարատուի կողմից տվյալ տարվա ընթացքում 90 օրից ավելի փաստացի տիրապետվող՝ չորս միլիոն դրամից կամ դրան համարժեք արտարժույթից ավելի արժեք ունեցող գույք (թանկարժեք գույք) կամ հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձին սեփականության իրավունքով պատկանող թանկարժեք գույք, կամ թանկարժեք գույք, որից փաստացի օգուտ է ստանում կամ այդ գույքը տնօրինում է հայտարարատուն

df_23_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[22].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_23_final = pd.concat([df_23_final, df], ignore_index=True)

# %%
df_23_final.to_csv("2021 | Բ.5.4 Հայտարարատուի կողմից տվյալ տարվա ընթացքում 90 օրից ավելի փաստացի տիրապետվող.csv")
# %%
# TABLE 24 | Բ.6.1. Բանկային հաշիվների մնացորդներ (բացառությամբ ավանդների)

df_24_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[23].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_24_final = pd.concat([df_24_final, df], ignore_index=True)

# %%
df_24_final.to_csv("2021 | Բ.6.1. Բանկային հաշիվների մնացորդներ.csv")
# %%
# TABLE 25 | Բ.6.2. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձին սեփականության իրավունքով պատկանող բանկային հաշիվների մնացորդներ (բացառությամբ ավանդների), կամ այն բանկային հաշիվների մնացորդները (բացառությամբ ավանդների), որից փաստացի օգուտ է ստանում կամ այն տնօրինում է հայտարարատուն

df_25_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[24].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_25_final = pd.concat([df_25_final, df], ignore_index=True)

# %%
df_25_final.to_csv("2021 | Բ.6.2. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")
# %%
# TABLE 26 | Բ.6.3. Էլեկտրոնային հաշիվներ և կրիպտոարժույթ

df_26_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[25].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_26_final = pd.concat([df_26_final, df], ignore_index=True)

# %%
df_26_final.to_csv("2021 | Բ.6.3. Էլեկտրոնային հաշիվներ և կրիպտոարժույթ.csv")
# %%
# TABLE 27 | Բ.6.4. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձին սեփականության իրավունքով պատկանող էլեկտրոնային հաշիվներ և կրիպտոարժույթ, կամ էլեկտրոնային հաշիվներ և կրիպտոարժույթ, որից փաստացի օգուտ է ստանում կամ այն տնօրինում է հայտարարատուն

df_27_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[26].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_27_final = pd.concat([df_27_final, df], ignore_index=True)

# %%
df_27_final.to_csv("2021 | Բ.6.4. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")
# %%
# TABLE 28 | Բ.6.5. Կանխիկ դրամ

df_28_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[27].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_28_final = pd.concat([df_28_final, df], ignore_index=True)

# %%
df_28_final.to_csv("2021 | Բ.6.5. Կանխիկ դրամ.csv")
# %%
# TABLE 29 | Բ.6.6. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված, երրորդ անձին պատկանող կանխիկ դրամ, կամ կանխիկ դրամ, որից փաստացի օգուտ է ստանում կամ այն տնօրինում է հայտարարատուն

df_29_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[28].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_29_final = pd.concat([df_29_final, df], ignore_index=True)

# %%
df_29_final.to_csv("2021 | Բ.6.6. Հայտարարատուի անունից, օգտին կամ հաշվին ձեռք բերված.csv")
# %%
# TABLE 30 | Բ.7. ԼՐԱՑՈՒՑԻՉ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ

df_30_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[29].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_30_final = pd.concat([df_30_final, df], ignore_index=True)

# %%
df_30_final.to_csv("2021 | Բ.7. ԼՐԱՑՈՒՑԻՉ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ.csv")
# %%
# TABLE 31 | Գ.1.1. Հաշվետու տարվա եկամուտներ

df_31_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[30].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_31_final = pd.concat([df_31_final, df], ignore_index=True)

# %%
df_31_final.to_csv("2021 | Գ.1.1. Հաշվետու տարվա եկամուտներ.csv")
# %%
# TABLE 32 | Գ.1.2.Ստացված վարկերի և փոխառությունների մայր գումարի մնացորդը հաշվետու տարվա դեկտեմբերի 31-ի դրությամբ

df_32_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[31].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_32_final = pd.concat([df_32_final, df], ignore_index=True)

# %%
df_32_final.to_csv("2021 | Գ.1.2.Ստացված վարկերի և փոխառությունների մայր գումարի մնացորդը հաշվետու տարվա դեկտեմբերի 31-ի դրությամբ.csv")
# %%

# TABLE 33 | Գ.2. ԼՐԱՑՈՒՑԻՉ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ

df_33_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[32].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_33_final = pd.concat([df_33_final, df], ignore_index=True)

# %%
df_33_final.to_csv("2021 | Գ.2. ԼՐԱՑՈՒՑԻՉ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ.csv")

# %%
# TABLE 34 | Գ.3.1. ԾԱԽՍԵՐԻ ՀԱՅՏԱՐԱՐԱԳԻՐ

df_34_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[33].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_34_final = pd.concat([df_34_final, df], ignore_index=True)

# %%
df_34_final.to_csv("2021 | Գ.3.1. ԾԱԽՍԵՐԻ ՀԱՅՏԱՐԱՐԱԳԻՐ.csv")
# %%
# TABLE 35 | Գ.4. ԼՐԱՑՈՒՑԻՉ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ

df_35_final = pd.DataFrame()
for key, value in yearly_dict.items():
    r = requests.get(value)
    soup = bs(r.content, "html.parser")
    tables = soup.find_all("table")
    rows = tables[34].find_all('tr')
    for row in rows:
        data = []
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
        df = pd.DataFrame(data)
        df = df.dropna(how='all') # to remove empty rows
        df['id'] = key
        df_35_final = pd.concat([df_35_final, df], ignore_index=True)
# %%
df_35_final.to_csv("2021 | Գ.4. ԼՐԱՑՈՒՑԻՉ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ.csv")
# %%
