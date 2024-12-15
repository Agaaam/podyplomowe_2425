import requests
import pandas
import matplotlib.pyplot as plt

#1. pobieranie danych z publicznego api
url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"

response_users = requests.get(url_users)
response_posts = requests.get(url_posts)
response_comments = requests.get(url_comments)

print(response_users)
print(response_users.json())