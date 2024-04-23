def ip_address(address):
    split_address = address.split(".")
    defanged_address = "[.]".join(split_address)
    return defanged_address

# Example usage:
input_ip = input("Enter the IP address you want to defang: ")
defanged_ip = ip_address(input_ip)
print("Defanged IP address:", defanged_ip)

# Optionally, prompt the user for another IP address
new_input_ip = input("Enter another IP address: ")
defanged_new_ip = ip_address(new_input_ip)
print("Defanged new IP address:", defanged_new_ip)
