import requests
import time

f = open('test_words.csv')
for url in f:
    url = url.strip()
    resp = requests.get('http://www.apercite.fr/api/apercite/320x240/yes/url')
    img = resp.raw
    # save raw img on hard disc
    time.sleep(20)
    filename = url.split("//")[-1].replace('/', '_') + '.jpg'
    print filename
    # output = open("images/filename", "wb")
    # output = open("images/file01.jpg", "wb")
    # output.write(resp.content)
    # output.close()
