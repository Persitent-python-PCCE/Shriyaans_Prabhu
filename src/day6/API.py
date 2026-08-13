import urllib.request as U
import urllib.parse as P
url="https://serpapi.com/dashboard"
url2="https://jsonplaceholder.typicode.com/comments?postId=1"
response=U.urlopen(url2)
# print(response.read())
# print(response.headers)
print(response.status)
print(response.headers.get("Content-Type"))

d=response.read().decode('utf-8')
print(d)