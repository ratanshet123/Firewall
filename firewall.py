import subprocess

# Define the firewall rules
rules = [
    {"chain": "INPUT", "protocol": "tcp", "dport": 80, "action": "ACCEPT"},
    {"chain": "INPUT", "protocol": "tcp", "dport": 22, "action": "ACCEPT"},
    {"chain": "INPUT", "protocol": "all", "action": "DROP"}
]

# Define the iptables command
iptables_cmd = "iptables -A {} -p {} --dport {} -j {}"

# Apply the firewall rules
for rule in rules:
    cmd = iptables_cmd.format(rule["chain"], rule["protocol"], rule["dport"], rule["action"])
    subprocess.run(cmd, shell=True)

