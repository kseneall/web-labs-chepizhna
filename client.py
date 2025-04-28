import requests

response = requests.get("https://localhost:8443/api/message", verify=False)
print("Відповідь сервера:", response.text)
