import ipaddress

def subnetting_details(ip_with_cidr):
    try:
        # Create an IPv4 network object
        network = ipaddress.ip_network(ip_with_cidr, strict=False)

        print(f"Input IP with CIDR: {ip_with_cidr}")
        print(f"Network Address   : {network.network_address}")
        print(f"Broadcast Address : {network.broadcast_address}")
        print(f"Subnet Mask       : {network.netmask}")
        print(f"Wildcard Mask     : {network.hostmask}")
        print(f"Total Hosts       : {network.num_addresses}")
        print(f"Usable Hosts      : {network.num_addresses - 2 if network.num_addresses > 2 else 0}")
        print(f"Prefix Length (/x): /{network.prefixlen}")

        print("\nAll possible subnets (first few shown):")
        subnets = list(network.subnets())
        for i, subnet in enumerate(subnets[:5]):
            print(f"Subnet {i+1}: {subnet}")

        if len(subnets) > 5:
            print("...")

    except ValueError as e:
        print(f"Invalid input: {e}")

# Example usage
ip_input = input("Enter IP address with CIDR (e.g., 192.168.1.0/24): ")
subnetting_details(ip_input)

