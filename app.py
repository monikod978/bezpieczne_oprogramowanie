# Minimalny skrypt korzystający z urllib3 (wersja w requirements.txt jest podatna)
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://example.com')
print('Status:', r.status)
