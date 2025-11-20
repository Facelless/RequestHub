# Simple Python API Server

This is a lightweight Python script that uses `http.server` for routing and `urllib` to handle requests. It enables basic API creation and is perfect for local testing and learning about web servers.

## Features

-  **Simple Routing** – Easily handle multiple endpoints.  
-  **Lightweight** – No external dependencies required.  
- **Easy to Extend** – Quickly modify and expand functionality.  
-  **Local Testing** – Ideal for rapid API prototyping.

##  Installation & Usage

###  Requirements

-  **Python 3.6+**

###  Running the Server

Clone the repository and run the script:

```bash
git clone https://github.com/Facelless/RequestHub.git
cd SimplePythonAPIServer
python server.py
```

###  Example Request

```bash
curl http://localhost:8000/api/example
```

## 📖 How It Works

- The script uses `http.server` to listen for incoming requests.  
- Endpoints are defined directly in the script to handle different requests.  
- `urllib` processes request parameters and generates responses.

Enjoy building your simple API! 
