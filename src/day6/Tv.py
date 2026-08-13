from urllib.request import urlopen
from urllib.parse import quote
import json 
class Tv:
    def __init__(self):
        pass

    def show(self):
        return False
    
    def show_details(self,show_id):
        url = f"https://api.tvmaze.com/shows/{show_id}"
        response = urlopen(url)
        data = json.loads(response.read())
        print(f"Name: {data['name']}")
        print(f"Language: {data['language']}")
        print(f"Status: {data['status']}")
        print(f"Genres: {data['genres']}")
        print(f"Rating: {data['rating']['average']}")

    def cast(self,show_id):
        url=f"https://api.tvmaze.com/shows/{show_id}/cast"
        response=urlopen(url)
        data=json.loads(response.read())
        for i in data:
            person = i["person"]
            character = i["character"]

            print(f"Actor: {person['name']}")
            print(f"Character: {character['name']}")
            print()

    def episodes(self,show_id):
        url=f"https://api.tvmaze.com/shows/{show_id}/episodes"
        response=urlopen(url)
        data=json.loads(response.read())
        for i in data:
            print(f"S{i['season']} E{i['number']} - {i['name']}")
                

    def search_show(self):
        name=input("enter the show name:")
        url=f"https://api.tvmaze.com/search/shows?q={quote(name)}"
        response=urlopen(url)
        data=json.loads(response.read())
        # print(data)
        for i in data:
            show=i["show"]
            print(f"name:{show["name"]} ")
            print(f"url:{show["url"]}")
            text=input("want this show or move next:")
            if text.lower()=="yes":
               return show["id"]
            elif text.lower()=="no":
                continue
         

tv=Tv()
# tv.search_show()
# print(tv.search_show())
url=None
show=tv.show()
while True:
    try:
        if  show==False:
            print(f"1.search a show")
            print(f"2.Exit")
            c=int(input("choice:"))
            if c==1:
                url=tv.search_show()
                show=True
            elif c==2:
                break
        else:
            print(f"1.display show details")
            print(f"2. return to menu")
            print(f"3. Display Episodes")
            print(f"4. Display Cast")
            print(f"9.exit")
            ch=int(input("choice:"))
            if ch==1:
                tv.show_details(url)
            if ch==2:
                show=False
                url=None
            if ch==3:
                tv.episodes(url)
            if ch==4:
                tv.cast(url)
            if ch==9:
                break
            else:
                print("No such coice available.")
    except:
        print("an error occured.")
    





