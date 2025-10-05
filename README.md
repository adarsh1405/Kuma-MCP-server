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

| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| GET    | `/services`        | List all registered services  |
| POST   | `/register`        | Register a new service        |
| POST   | `/deregister`      | Deregister a service          |
| GET    | `/health`          | Health check for the server   |
| GET    | `/status/<name>`   | Get status of a service       |

## Example Usage

Register a service:

```bash
curl -X POST http://localhost:8000/register -H "Content-Type: application/json" -d '{"name": "service1", "address": "127.0.0.1", "port": 5000}'
```

Check health:

```bash
curl http://localhost:8000/health
```

## Screenshots

![Dashboard Screenshot](assets/dashboard.png)
![Service Registration Screenshot](assets/service_registration.png)

## Sample Video

[![Watch the demo](assets/video_thumbnail.png)](assets/demo.mp4)

## Directory Structure

```
Kuma-MCP-server/
├── assets/
│   ├── dashboard.png
│   ├── service_registration.png
│   ├── video_thumbnail.png
│   └── demo.mp4
├── main.py
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License.