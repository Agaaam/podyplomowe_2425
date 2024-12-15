import requests
import pandas as pd
import matplotlib.pyplot as plt

# #1. pobieranie danych z publicznego api
# url_users = "https://jsonplaceholder.typicode.com/users"
# url_posts = "https://jsonplaceholder.typicode.com/posts"
# url_comments = "https://jsonplaceholder.typicode.com/comments"
#
# response_users = requests.get(url_users)
# response_posts = requests.get(url_posts)
# response_comments = requests.get(url_comments)
#
# # print(response_users)
# # print(response_users.json())
# # print(response_users.status_code)
#
# if response_users.status_code == 200 and response_posts.status_code == 200 and response_comments.status_code == 200 :
#     data_users = response_users.json()
#     data_posts = response_posts.json()
#     data_comments = response_comments.json()
# else:
#     raise EXCEPTION("nie udało się pobrać danych")
#
#
# # print(data_users)
# # print(data_posts)
# # print(data_comments)
#
# #tworzenie data frames z jsonów
# df_users = pd.DataFrame(data_users)
# df_posts = pd.DataFrame(data_posts)
# df_comments = pd.DataFrame(data_comments)
#
# #print(df_users.to_string())
#
# posts_per_user = df_posts.groupby('userId', as_index = False)['id'].count()
# posts_per_user.rename(columns={'id': 'post_count'}, inplace=True)
# print(posts_per_user)



#---------------------------------------
#cwiczenie z plikiem jason
#wczytanie danych
df = pd.read_json('Pliki_do_cwiczen\\dane.json')

#Wyswietlanie danych
print("Pierwsze 5 wierszy dancyh:")
print(df.head())

#filtracja danych
mlodsi_niz_30 = df[df["wiek"] <30]
print("\nosoby mlodsze niż 30 lat:")
print(mlodsi_niz_30)

#dodanie nowej kolumny
df["wiek_za_5_lat"] = df["wiek"] + 5
print("\nDane z dodaną kolumną 'wiek_za_5_lat':")
print(df)

#Statystyka
sredni_wiek = df['wiek'].mean()
print(f'\nsredni_wiek: {sredni_wiek}')

#sortoowanie
df_sortted = df.sort_values('wiek', ascending=False)
print(df_sortted)

#eksport danych
df.to_json('dane_po_obrobce\\json1.json')
df.to_json('dane_po_obrobce\\json2.json', orient = "split")
df.to_json('dane_po_obrobce\\json3.json', orient = "records", indent=4)
df.to_json('dane_po_obrobce\\json4.json', orient = "index")
df.to_json('dane_po_obrobce\\json5.json', orient = "columns")
df.to_json('dane_po_obrobce\\json6.json', orient = "values")
df.to_json('dane_po_obrobce\\json7.json', orient = "table")





