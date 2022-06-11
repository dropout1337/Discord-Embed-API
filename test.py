import requests

json = {
    "redirect": "https://discord.gg/glass",
    
    "title": "embedss",
    "description": "Wow soo cool!!",
    "color": "#2F3136",
    
    "image": "https://c.tenor.com/KlrPPgR3ADMAAAAC/hitam-atau.gif",
    "thumbnail": True,
}

response = requests.post("http://localhost/api/create", json=json)
print(response.text)