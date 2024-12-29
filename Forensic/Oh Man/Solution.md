# Question
We received a PCAP file from an admin who suspects an attacker exfiltrated sensitive data. Can you analyze the PCAP file and uncover what was stolen?

# Tools
- Wireshark
- Cyberchef
- Python script for allign the file
- hashcat

# Description
This challenge is related with NTLMSSP and SMB.Finf the key of NTLM. Need some knowledge on how to crack NTLM hash

# Solution
1. Read the pcap and filter for NTLMSSP.
2. And will see this:
   
   ![image](https://github.com/user-attachments/assets/0033c437-9d5a-4622-a1c0-bfe9ac84798a)

4. Understand the structure
