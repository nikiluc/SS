import urllib.request
import json
import webbrowser

client_access_token = 'MRsQ4rozaguFgqIZ36BuP0d84xulRHVFuxs2b6MLhH3CvbA7jKa8_QfQPgdjlxHR'

search_term = input("Type lyrics here: ")
_URL_API = "https://api.genius.com/"
URL = "https://genius.com"
_URL_SEARCH = "search?q="
querystring = _URL_API + _URL_SEARCH + urllib.request.pathname2url(search_term)
request = urllib.request.Request(querystring)
request.add_header("Authorization", "Bearer " + client_access_token)
request.add_header("User-Agent", "")

response = urllib.request.urlopen(request, timeout=3)

data = response.read()

#print(data)

j_obj = json.loads(data)
#print(json_obj.keys())

num = 0

for x in j_obj['response']['hits']:

	print(j_obj['response']['hits'][num]['result']['full_title'])
	pathname = j_obj['response']['hits'][num]['result']['path']
	full_link = URL + pathname



	ans = input("Do you want to open a link? (Y) or (N) (hit (x) to quit) ")

	if ans == 'Y':

		webbrowser.open(full_link)
		break

	elif ans == 'y':

		webbrowser.open(full_link)
		break

	elif ans == 'x':

		print ("Quitting program...")
		break

	num += 1









