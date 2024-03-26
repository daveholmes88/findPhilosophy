import sys
from bs4 import BeautifulSoup
import requests

hops = 0

def find_link(url):
    global hops
    if hops > 100:
        print('hops has reached the max, script is ending')
        exit()

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    div = soup.find('div', {'class': 'mw-content-ltr mw-parser-output'})

    for child in div:
        if child.name == 'p':
            if child.text:
                p_string = str(child)
                index_open = p_string.find('(')
                index_close = p_string.find(')')
                string_without_parenthesis = p_string
                if index_open and index_close:
                    string_without_parenthesis = p_string[:index_open] + p_string[index_close+1:]
                beginning = string_without_parenthesis.find('/wiki')
                if beginning and beginning > 0:
                    ending = string_without_parenthesis.find('"', beginning)
                    new_url = 'https://en.wikipedia.org' + string_without_parenthesis[beginning:ending]
                    print(new_url)
                    if new_url == 'https://en.wikipedia.org/wiki/Philosophy':
                        print(hops, 'hops')
                        exit()
                    else:
                        hops += 1
                        find_link(new_url)

find_link(sys.argv[1])