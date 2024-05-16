import subprocess

def check_host(host):
    # Execute ping command
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check the return code to determine if the host is alive
    if result.returncode == 0:
        return True
    else:
        return False

def main():
    # Read hostnames from hostlist.txt
    with open('hostlist.txt', 'r') as file:
        hosts = file.read().splitlines()
    
    # Check each host
    for host in hosts:
        if check_host(host):
            print(f"{host} is alive")
        else:
            print(f"{host} is not reachable")

if __name__ == "__main__":
    main()
