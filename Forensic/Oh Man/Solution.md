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
   
8. Decrypt the smb packet by using the password that we have cracked.

Wireshark:
Edot -> Preferences -> ntlmssp. Thne enter the password (password<3)

![image](https://github.com/user-attachments/assets/afe79a61-858d-44ed-8450-9782f3a6788d)

Now we can see the content or the smb object:

Go to file -> exports object -> SMB
![image](https://github.com/user-attachments/assets/026e7ec8-8ba0-4e32-9f72-80c71b6b0ad2)

10. Open all the file, and one of the file show this:

    ![image](https://github.com/user-attachments/assets/0d3e9127-ee68-47ec-8774-b9826392a034)

    These were the instructions to restoring the minidump signature and extract the secret. In order to use scripts/restore_signature, you will need to clone the NanoDump repository and install pypykatz.

12. Run the repair script:
python3 -m pypykatz lsa minidump 20241225_1939.log

and we will get the flag:

![image](https://github.com/user-attachments/assets/a58d44c6-5bea-4461-9c5c-56c94f842b46)

