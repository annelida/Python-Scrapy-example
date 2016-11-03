import requests

resp = requests.get('http://www.apercite.fr/api/apercite/120x90/yes/www.iacono.fr')
img = resp.raw
# save raw img on hard disc
