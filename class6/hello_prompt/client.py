import requests

URL = "http://localhost:8001/mcp"
# PAYLOAD = {
#     "jsonrpc":"2.0",
#     "method":"prompts/list",
#     "params":{},
#     "id":1
# }

PAYLOAD = {
    "jsonrpc":"2.0",
    "method":"prompts/get",
    "params":{
        "name":"greet",
        "arguments":{
            "name":"Habiba"
        }
    },
    "id":1
}


HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream"
}

response = requests.post(URL, json=PAYLOAD, headers=HEADERS,stream=True)
for line in response.iter_lines():
    if line:
        print(line)