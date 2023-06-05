
import wikipediaapi
from datetime import datetime
import json

now = datetime.now()
date_time = now.strftime("%d-%m-%Y")
wiki_wiki = wikipediaapi.Wikipedia('pt')

file_name = "politica-wikipedia-0.2.json"
f = open("politica-wikipedia-2.json")
data = json.load(f)


page = wiki_wiki.page('Politicos Brasileiros')
all_data = [
    {
        "data_source": "Wikipedia",
        "date":date_time,
        "title":page.title,
        "body":page.text
    }
]
all_data = all_data + data
def get_references(page):
        links = page.links
        for title, body in links.items():
            all_data.append(
                            {
                    "data_source": "Wikipedia",
                    "date":date_time,
                    "title":title,
                    "body":body.text
                }
            )


new_data = ""
count = 0
for item in all_data:
    if count == 950:
        break
    if count > 700:
        new_data = item['body'] + "  " + new_data
    count = 1 + count
    
with open(file_name, 'w', encoding="utf-8") as output_file:
    output_file.write('')
    json.dump(new_data, output_file,ensure_ascii=False)





