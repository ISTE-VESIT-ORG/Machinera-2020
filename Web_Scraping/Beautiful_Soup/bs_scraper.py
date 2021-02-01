''' Importing Libraries '''
import requests
import bs4

''' Make Request '''
res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')  
# print(res.text)

''' Beautiful Soup '''
soup = bs4.BeautifulSoup(res.text, 'html.parser') # Array of elements 
content = soup.select('.mw-headline')
# print(content)
for i in content:
    print(i.text)