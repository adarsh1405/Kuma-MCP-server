from mcp.server.fastmcp import FastMCP
import requests
import json

mcp = FastMCP(name="Tool Example")


@mcp.tool()
def get_meshes():
    """Get how many meshes there are with name"""
    response = requests.get("http://localhost:25681/meshes")
    data = response.json()
    total = data.get("total", 0)
    mesh_names = [item["name"] for item in data.get("items", [])]

    return f"Total meshes: {total}, Mesh names: {', '.join(mesh_names)}"

@mcp.tool()
def get_meshInsights():
    """List all the mesh insights with total mesh available , total policies and breakdown of policies"""
    response = requests.get("http://localhost:25681/mesh-insights")
    data = response.json()
    total = data.get("total", 0)
    policy_map = {}
    total_policy_count = 0
    for item in data.get("items", []):
        mesh_name = item.get("name", "default")
        # Get policies information
        policies = item.get("policies", {})
        if policies:
            # Calculate total policy count
            total_policy_count = sum(policy_info.get("total", 0) for policy_info in policies.values())        
            for policy_type, policy_info in policies.items():
                count = policy_info.get("total", 0)
                policy_map[policy_type] = count
    return f"Total Mesh Insights: {total}, Total Policies: {total_policy_count}, Policy Breakdown: {policy_map}"

@mcp.tool()
def create_trafficpermission(tp_name: str, source: str , destination: str) -> str:
    # Define the URL
    url = f"http://localhost:25681/meshes/default/traffic-permissions/{tp_name}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "type": "TrafficPermission",
        "name": tp_name,
        "mesh": "default",
        "sources": [
            {"match": {"kuma.io/service": source}}
        ],
        "destinations": [
            {"match": {"kuma.io/service": destination}}
        ]
    }
    try:
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == 200:
            return f"Traffic permission created successfully for {tp_name}"
        else:
            return f"Request failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

@mcp.tool()
def list_trafficpermissions():
    response = requests.get("http://localhost:25681/meshes/default/traffic-permissions")
    data = response.json()
    total = data.get("total", 0)
    tp_names = [item["name"] for item in data.get("items", [])]
    return f"Total Traffic Permissions: {total}, Names: {', '.join(tp_names)}"

@mcp.tool()
def delete_trafficpermission(tp_name: str) -> str:
    url = f"http://localhost:25681/meshes/default/traffic-permissions/{tp_name}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return f"Traffic permission {tp_name} deleted successfully"
        else:
            return f"Request failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')