# Kuma-MCP-server

Kuma-MCP-server is a lightweight, extensible server built with Python, designed to provide a modular control plane (MCP) for managing and monitoring distributed systems. The server exposes RESTful APIs for service registration, health checks, and status monitoring, making it suitable for microservices architectures and cloud-native environments.

## Features

- **Service Registration:** Register and deregister services dynamically.
- **Health Checks:** Monitor the health of registered services.
- **Status Endpoints:** Query the status and metadata of services.
- **Extensible Architecture:** Easily add new endpoints and integrations.
- **Lightweight:** Minimal dependencies and easy to deploy.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` for dependency management
- Run kuma locallly / whereever you want
- Download Claud or any local LLM which supports MCP server

### Installation

```bash
git clone https://github.com/yourusername/Kuma-MCP-server.git
cd Kuma-MCP-server
pip install -r requirements.txt
```

### Running the Server

```bash
python main.py
```

The server will start on `http://localhost:8000` by default.

## API Endpoints


| Method | Endpoint                | Description                              |
|--------|------------------------|------------------------------------------|
| GET    | `/services`            | List all registered services             |
| POST   | `/register`            | Register a new service                   |
| POST   | `/deregister`          | Deregister a service                     |
| GET    | `/health`              | Health check for the server              |
| GET    | `/status/<name>`       | Get status of a specific service         |
| GET    | `/metrics`             | Get server metrics (if implemented)      |
| GET    | `/`                    | Root endpoint, usually returns welcome   |

*Note: Endpoints may vary based on your `main.py` implementation. Please refer to the code for any custom or additional endpoints.*

## Example Usage

Register a service:

```bash
curl -X POST http://localhost:8000/register -H "Content-Type: application/json" -d '{"name": "service1", "address": "127.0.0.1", "port": 5000}'
```


## Screenshots

<img width="1702" height="693" alt="dashboard" src="https://github.com/user-attachments/assets/cd5c3ea9-d351-4191-846e-ae72a90897ec" />
<img width="400" height="500" alt="policyCreation" src="https://github.com/user-attachments/assets/1cc27b1f-8e4b-444b-8230-95fd6dba6109" />
<img width="450" height="500" alt="insights" src="https://github.com/user-attachments/assets/d522d44f-4a66-425c-8f0b-bb69d40d30fb" />


## Sample Video



## Directory Structure

```
Kuma-MCP-server/
├── assets/
│   ├── dashboard.png
│   ├── ss1.png
│   ├── ss2.png
│   └── demo.mp4
├── main.py
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License.
