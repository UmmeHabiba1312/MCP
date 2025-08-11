import requests

url = "http://localhost:9000/mcp/"

headers = {
    "Accept": "application/json,text/event-stream",
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1,
    "params": {},
    
}

response = requests.post(url, headers=headers, json=body)
print(response.text)
for lines in response.iter_lines():
    if lines:
        print(lines)