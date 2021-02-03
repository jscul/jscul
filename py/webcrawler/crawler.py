import requests
from bs4 import BeautifulSoup


def get_links_func(link=None, data=None):

    if link is not None:
        page = requests.get(link)
        if page.status_code == 200:
            data = page.text

    soup = BeautifulSoup(page.text, "html.parser")

    artist_name_list = soup.find(class_="content-area")
    if artist_name_list is None:
        return []

    artist_name_list_items = artist_name_list.find_all(class_="entry-content")

    result = []
    for item in artist_name_list_items:
        artist_name_list_items2 = item.find_all("a")
        result.extend(
            [
                {"name": m.get_text(), "link": m.get("href")}
                for m in artist_name_list_items2
            ]
        )

    print(f"Retrieved {len(result)} results")
    return result


data = """
<ul>
    <li class="item">item1</li>
    <li class="item">item2</li>
    <li class="item">item3</li>
</ul>
"""

soup = BeautifulSoup(data, "html.parser")

for item in soup.select("li.item"):
    print(item.get_text())
