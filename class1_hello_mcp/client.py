import requests

url = "http://localhost:8000/mcp/"

headers = {
    "Accept": "application/json,text/event-stream",
}

# jsonrpc stands for JSON Remote Procedure Call.
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

# tool calling testing with python client.py
# {
#     "jsonrpc": "2.0",
#     "method": "tools/call",
#     "params": {
#         "name":"get_weather",
#         "arguments":{
#             "location":"Karachi"
#         }
#     },
#     "id": 1
# }
