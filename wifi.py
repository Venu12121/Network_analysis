from scapy.all import ARP, Ether, srp, conf

def get_devices(ip_range):
    # Disable verbose output
    conf.verb = 0
    
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    print("Sending ARP requests...")
    
    # Send the packet and receive responses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse the responses to get IP and MAC addresses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Example usage
if __name__ == "__main__":
    ip_range = "172.20.10.0/24"
  # Adjust this range based on your wifis IP range
    devices = get_devices(ip_range)
    
    if devices:
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("No devices found. Ensure the devices are connected to the same network and the script is running with proper permissions.")
