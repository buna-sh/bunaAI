import paramiko

def ssh_connect(host, username, password):
    """Connect to a server via SSH."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password)
        print(f"Connected to {host}")
        return client
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
        return None

def execute_command(client, command):
    """Execute a command on the server."""
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        if output:
            print(f"OUTPUT: {output}")
        if error:
            print(f"ERROR: {error}")
    except Exception as e:
        print(f"Failed to execute command: {e}")

def configure_server(host, username, password):
    """Automate server configuration."""
    client = ssh_connect(host, username, password)
    if not client:
        return

    # Example tasks
    commands = [
        "sudo apt update && sudo apt upgrade -y",
        "sudo apt install -y nginx",
        "sudo systemctl enable nginx",
        "sudo systemctl start nginx",
    ]
    
    for command in commands:
        print(f"Executing: {command}")
        execute_command(client, command)

    client.close()

if __name__ == "__main__":
    # Example server details (replace with actual credentials)
    servers = [
        {"host": "192.168.1.10", "username": "root", "password": "yourpassword"},
        {"host": "192.168.1.20", "username": "root", "password": "yourpassword"},
    ]
    
    for server in servers:
        print(f"Configuring server: {server['host']}")
        configure_server(server["host"], server["username"], server["password"])

