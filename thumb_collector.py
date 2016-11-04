import requests
import logging

logger = logging.getLogger('thumbnails')
hdlr = logging.FileHandler('thumbnails.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

f = open('test_words.csv')
for url in f:
    url = url.strip()
    logging.debug("This is images url: %s" % (url))
    resp = requests.get(url)
    img = resp.raw
    # save raw img on hard disc
    filename = url.split('//')[-1].replace('/', '_')
    logging.debug("This is images file name: %s" % (filename))
    # with open("images/file01.jpg", "wb") as test:
    #     test.write(resp.content)
    #     test.close()



