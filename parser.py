import json
import sys
import urllib.request

url_name = input("Enter the domain/subdomain (For best results, include wildcard '%'): ")

filename = input("File Name to Write: ")
sys.stdout = open(filename, 'w')

with urllib.request.urlopen('https://crt.sh/?q='+url_name+'&output=json') as url:
	data = json.loads(url.read().decode())
	i = 0
	while i == i:
		try:
			print(data[i]['name_value'],)
			i=i+1
		except (IndexError) as err:
			pass
			break
sys.stdout.close()
