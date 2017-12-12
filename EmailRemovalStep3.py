#!/usr/bin/python3
import io

with io.open("users3.txt", 'r',encoding='utf16') as fin:
	ll2 = fin.readlines()
new_file = open("users3.txt",'w')
	
for line in ll2:
	ll3 = line.replace("SamAccountName","").replace("--------------","").lstrip().replace(" ","")
	new_file.write(ll3)
	print(ll3)