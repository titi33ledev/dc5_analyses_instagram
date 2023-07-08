#%%
import pandas as pd
import dtale

df_sneakersaddict = pd.read_json("/Users/feedastic/Desktop/Digital Campus/analyse_instagram/sneakersaddict.json")
df_sneakers = pd.read_json("/Users/feedastic/Desktop/Digital Campus/analyse_instagram/sneakers.json")
df_clean_sneakers = pd.read_json("/Users/feedastic/Desktop/Digital Campus/analyse_instagram/cleansneakers.json")


# %%
merge_df = df_sneakers.merge(df_sneakersaddict,how='outer')
df_clean = merge_df[["username","commentCount","likeCount","description","location","query"]]
df_fr = df_clean[df_clean['location'].str.contains("France")]
dtale.show(df_fr)

# %%
pattern = r"(#\w+)"
hashtags = df_fr["description"].str.extractall(pattern).groupby(level=0).agg(lambda x: ','.join(x))
hashtags.columns = ["Hashtags"]
# %%
hashtags["Hashtags"] = hashtags['Hashtags'].astype(str).str.split(',')
hashtags_analysis = hashtags.explode('Hashtags').reset_index(drop=True)