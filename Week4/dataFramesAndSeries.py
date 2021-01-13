#%%
import pandas as pd
#%%
a_List_Of_Cities = ['Austin','New York','Tokyo','Qingdao']
# %%
city_Series = pd.Series(a_List_Of_Cities)
# %%
type(city_Series)
# %%
city_Series.count
# %%
for city in city_Series:
    print(city)
# %%
city_Series[0]
# %%
city_Series.T
# %%
clockWorkOrange = {
    "MovieTitle" : "Clockwork Orange", "Genre" : "Horror"
}
mandalorian = {
    "MovieTitle" : "The Mandalorian", "Genre" : "Sci Fi"
}
pulpFiction = {
    "MovieTitle" : "Pulp Fiction", "Genre" : "Action"
}
#%%
a_list_of_movies = [clockWorkOrange,mandalorian,pulpFiction]
#%%
movies_df = pd.DataFrame(a_list_of_movies)
# %%
type(movies_df)
# %%
movies_df['MovieTitle']
# %%
type(movies_df['MovieTitle'])
# %%
movies_df['MovieTitle'][0]
# %%
movies_df.T
# %%
