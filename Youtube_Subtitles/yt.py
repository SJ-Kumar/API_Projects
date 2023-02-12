import requests

url = "https://subtitles-for-youtube.p.rapidapi.com/subtitles/%7BvideoId%7D.srt"

headers = {
	"X-RapidAPI-Key": "90d09469fdmsh603a8182f61dd63p1ffd67jsn5d89089d43d7",
	"X-RapidAPI-Host": "subtitles-for-youtube.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)