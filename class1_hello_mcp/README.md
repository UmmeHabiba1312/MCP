# MCP (Model Context Protocol)
It's a way to send your context (like data, instructions, API details, or tool access) to a Large Language Model (LLM) through a standardized protocol.

### In simple words:

* You prepare your message + relevant data in a specific structured format

* Send it to the LLM

* The LLM uses that context to generate a more accurate and relevant response

This ensures the model only gets controlled, relevant, and secure information, improving accuracy and reducing unnecessary processing.

### Covered Topics :

#### HTTP: Theory, Evolution, and AI Communication

[01 - HTTP THEORY](https://notebooklm.google.com/notebook/710a382b-b260-4792-9b8c-5630b7f195b1)

#### REST: Principles and API Design

[02 - REST](https://notebooklm.google.com/notebook/c55d05e8-f146-47ad-858c-49bc8180166d)

#### JSON-RPC 2.0: Protocol for Agent Orchestration


[03 - JSON-RPC 2.0](https://notebooklm.google.com/notebook/8b39ea6f-17ec-45ca-854c-065c5b152f50)


### TCP (Transmission Control Protocol): 
A reliable protocol that ensures data arrives complete, in order, and without errors but it's slower because of extra checks.

### UDP (User Datagram Protocol): 
A fast, lightweight protocol that sends data without guarantees of delivery or order less reliable but much quicker.

### QUIC (Quick UDP Internet Connections):
A modern protocol built on UDP that adds reliability, security, and speed combining the best of TCP and UDP.

### Persistence  
keeping the same connection open for many requests instead of closing and reopening it every time.
In HTTP:

- HTTP/1.0 (old) → Non-persistent by default (new connection for every file).
- HTTP/1.1 → Persistent by default (one connection can handle many files).
- HTTP/2 & HTTP/3 → Always persistent, plus they can even send multiple requests at the same time (multiplexing).

# 🔄 Connection Management (Does it stay open?)
When you visit a website, your browser (the client) talks to the web server using HTTP (HyperText Transfer Protocol).
But HTTP doesn’t actually send the data itself it relies on transport protocols (like TCP or UDP) to move the data across the network.

### 🔹 HTTP/1.1

- Uses TCP connections.
- With persistent connections (via keep-alive), the browser can reuse the same connection to request multiple files (HTML, CSS, JS, images).
- Problem: It processes one request at a time per connection.
- If your page has 50 files, it either opens multiple connections (costly) or handles them sequentially → slow.
- Issue: Head-of-line blocking → If one request is slow, the others behind it get stuck.

### 🔹 HTTP/2

- Still uses TCP, but introduces multiplexing:
- Multiple requests and responses can be sent simultaneously over the same connection.
- Example: Instead of waiting for file A before requesting file B, it can request both at the same time.
- Uses binary framing, which structures data more efficiently.
- Faster than HTTP/1.1, but still has TCP’s limitation:
-If a single packet is lost in TCP, everything waits (head-of-line blocking at the transport level).


### 🔹 HTTP/3 (based on QUIC)
- Built on UDP instead of TCP.
- QUIC (Quick UDP Internet Connections) is a protocol developed by Google that adds reliability, security, and multiplexing on top of UDP.
- Benefits:

    - Avoids TCP’s head-of-line blocking → if one packet is lost, others can still flow.

    - Faster setup: QUIC integrates TLS (encryption), so secure connections are established in fewer steps.

    - More resilient on unstable networks (like mobile data) because it handles connection migration (e.g., if your Wi-Fi switches to 4G, the connection doesn’t break).

Best for streaming, video calls, gaming, and modern web apps.


## Summary
Communication between two computers happens using HTTP, but HTTP doesn’t actually move the data it relies on transport protocols like TCP and UDP.

- TCP: Reliable but slower. Data goes in packets, and if one packet is delayed or corrupted, the others wait (head-of-line blocking). TCP will re-send lost packets, so data isn’t lost, but the user experiences delays. This is what HTTP/1.1 uses.

- HTTP/2: Still uses TCP, but allows multiplexing, meaning multiple requests/responses can happen at once over the same connection — faster than HTTP/1.1.

- UDP: Much faster, but not safe. If one packet is lost or corrupted, it’s gone no waiting, no re-sending.

- QUIC (used in HTTP/3): Built on UDP but adds TCP-like reliability and TLS security. It’s both fast and safe, making it the modern standard.

## Common HTTP Status Codes

| Code | Meaning                               |
|------|---------------------------------------|
| 200  | OK – Success                          |
| 201  | Created – New resource made           |
| 400  | Bad Request – You sent something wrong|
| 401  | Unauthorized – You need to log in     |
| 403  | Forbidden – You can’t access this     |
| 404  | Not Found – Page doesn’t exist        |
| 500  | Server Error – Something broke on the server |


## 🔨 List of Common HTTP Methods (with Examples)

| Method  | What It Does                          | Simple Example                                |
|---------|---------------------------------------|-----------------------------------------------|
| **GET/read**     | Get data or a page                  | `GET /home` → Fetch home page                 |
| **POST/create**    | Send data to server (like a form)   | `POST /signup` → Create new account           |
| **PUT/replace**     | Update (replace) a resource         | `PUT /user/1` → Replace user info             |
| **DELETE/remove**  | Remove a resource                   | `DELETE /user/1` → Delete user 1              |
| **HEAD/only metadata**    | Just get headers, no body           | Check if a file exists                        |
| **OPTIONS/Ask capabilities** | Ask server what methods it allows   | Used for **CORS** (cross-origin requests)     |
| **PATCH/update**   | Partially update a resource         | `PATCH /user/1` → Update user’s email only    |


## 🧃 Analogy: Ordering at a Café

| Action                                | HTTP Method        |
|---------------------------------------|--------------------|
| Looking at the menu                   | `GET /menu`        |
| Placing an order                      | `POST /order`      |
| Changing your whole order             | `PUT /order/5`     |
| Cancelling your order                 | `DELETE /order/5`  |
| Asking what payment types they accept | `OPTIONS /payment` |
| Asking for receipt only (no food)     | `HEAD /receipt`    |
| Changing only 1 item in your order    | `PATCH /order/5`   |
