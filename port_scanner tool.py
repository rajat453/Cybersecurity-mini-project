import socket
import datetime

target = input("Enter IP address or domain: ")
print(f"\n🔍 Scanning {target}...")

start_time = datetime.datetime.now()

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    sock.close()

end_time = datetime.datetime.now()
print(f"\n✅ Scan completed in: {end_time - start_time}")
