import requests

url = "https://url-shortener-service.p.rapidapi.com/shorten"

payload = "url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fjayanth-kumar-91947b220%2F"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "90d09469fdmsh603a8182f61dd63p1ffd67jsn5d89089d43d7",
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)