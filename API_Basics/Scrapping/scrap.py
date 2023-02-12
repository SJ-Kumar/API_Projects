import requests

url = "https://scrapingbee.p.rapidapi.com/"

querystring = {"url":"https://www.linkedin.com/in/jayanth-kumar-91947b220/","render_js":"true"}

headers = {
	"X-RapidAPI-Key": "90d09469fdmsh603a8182f61dd63p1ffd67jsn5d89089d43d7",
	"X-RapidAPI-Host": "scrapingbee.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)