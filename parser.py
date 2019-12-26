import json
import urllib.request

url_name = input("Enter the crt.sh url (don't forget to append '&output=json'):")

with urllib.request.urlopen(url_name) as url:
	data = json.loads(url.read().decode())
	i = 0
while i == i:
	try:
		print(data[i]['name_value'])
		i=i+1
	except (IndexError) as err:
		pass
		break
