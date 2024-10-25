import requests

PROMPTLY_TOKEN = '7983cf570352388c0d84d5bac4e8c8437c2acc73'    
url = 'https://trypromptly.com/api/apps/d353d815-2767-4709-b64f-ba919ada371a/run'

payload = {
  "input": {
    "task": "<task_value>"
  },
  "stream": False,
}
headers = {
  "Content-Type": "application/json",
  "Authorization": "Token " + PROMPTLY_TOKEN,
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text.encode('utf8'))