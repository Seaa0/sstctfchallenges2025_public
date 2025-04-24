Open the file with a decompiler such as binary ninja  
Look for main function and see that only function inside is rqiuheaog  
Look at rqiuheaog and see that the xor function is used in conjunction with a for loop to loop through all characters of both var_10 and var_28  
Since var_10 is shorter, it is likely the key while var_28 is likely an encrypted flag  
Create a python script with the 2 values which does the same thing and then find the flag starting with sstctf{}  