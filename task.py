import requests
from bs4 import BeautifulSoup

page = 1
for pg in range(21):
    site_to_parse = 'http://yermilovcentre.org/medias/?page=' + str(page)
    my_answer = requests.get(site_to_parse)

    soup = BeautifulSoup(my_answer.content, 'html.parser')

    for data in soup.select('.mx-0.px-0.container.block-container-small-title.row > a'):
        print(data.text.replace('\n', '').strip(), ' — ', 'http://yermilovcentre.org' + data.get("href").replace('\n', '').strip())
    page += 1