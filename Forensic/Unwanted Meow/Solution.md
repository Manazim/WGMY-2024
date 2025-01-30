# Question
Uh.. Oh.. Help me, I just browsing funny cats memes, when I click download cute cat picture, the file that been download seems little bit wierd. I accidently run the file making my files shredded. Ughh now I hate cat meowing at me.

# Tools
-Cyberchef
-Python script

# Description
This challenge is related with file image manipulation. Givne a file name flag.shreded, but we cant see the image. Need to investiagte further what cause this issue

# Solution
1.Upload the file into cyberchef. It wil interpret the hexadecimal of the image into human-readable
2. And will see this:
   
![image](https://github.com/user-attachments/assets/c35de567-1ad0-4d8d-844a-e2f44af2ba8c)

There are a lot of "meow" words between data. The value in hexadecimal of meow is "6d 65 6f 77".

4. Use python script to remove the unwanted "meow" word insisde teh data:

with open(r"D:\Users\Asus Zephyrus G15\Documents\updated_file.jpeg", 'rb') as f:
    data = f.read()

# Remove the sequence `6d 65 6f 77`
updated_data = data.replace(b'\x6d\x65\x6f\x77', b'')

with open(r"finally_yes.jpeg", 'wb') as f:
    f.write(updated_data)



6. Finally we can see the image, and the flag is inside the image:

![image](https://github.com/user-attachments/assets/8a12cfdd-2cfc-4c47-970d-dcac65ebfe41)

WGMY{4a4be40c96ac6314e91d93f38043a634}



