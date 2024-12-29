# Question
Partial traffic packet captured from hacked machine, can you analyze the provided pcap file to extract the message from the packet perhaps by reading the packet data?

# Tools
- Wireshark
- any pcap reader

# Description
This challenge has a lot of icmp packet

# Strategy
1. Read the pcap
2. Analyze the data on the icmp prtocol, the data is not same. This is suspicious since the data should same for all icmp packet.
3. Craft the tshark query to extract only icmp 

# Solution
1. Use Tshark to extract the icmp.
2. The query:
   
   tshark -nr traffic.pcap -Y icmp -T fields -e data.text -o data.show_as_text:True
   
4. Then will directly get the flag:
   ![image](https://github.com/user-attachments/assets/4dd08e8e-319c-49be-9968-10211e00b05e)

