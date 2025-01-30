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

4. Then crack the NTLM Hash, this is the information needed to crack the hash:
   ![image](https://github.com/user-attachments/assets/e7ff28b9-3e7d-49ec-a207-12fcf60c5dc2)

then arrange in this sequence:
user::domain:challenge:HMAC-MD5:NTLMV2_Response

6. Then proceed to crack the hash by issuing this command:

hashcat -a0 -m5600 wgmy.txt /usr/share/wordlists/rockyou.txt

And will get the password :

![image](https://github.com/user-attachments/assets/515c3c83-0392-4b26-b01d-9abcfa2fcdbc)


password<3
   
8. 

