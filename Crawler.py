__author__ = 'YUVAL'

import webbrowser, requests, bs4, pprint

url = 'http://www.nexusmods.com/skyrim/mods/top/?'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
File_Names = soup.find_all('a', attrs={"class": "file"})

for file in File_Names:
    s = str(file.text)
    s = s.strip().replace('for', '').replace('Skyrim', '')
    print(s)


# May be useful later
x = soup.select(".file")
