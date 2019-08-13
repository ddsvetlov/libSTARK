import subprocess
import create_asm_file
#add testing security params
t=3
s=3
#add testing transaction data
asm_cash1=10
asm_cash2=10
asm_value=50
flag=False

f=open("condoub.txt", 'w') #create .txt with console duplication for parcing
value1='-t'+str(t)  
value2='-s'+str(s)
#create  asm file
create_asm_file.create_asm_file(asm_cash1, asm_cash2, asm_value)
#show asm file
tes=open("test.asm")
for line in tes:
	print(line)

#run tinyram
subprocess.call(["./../stark-tinyram", "test.asm", value1, value2], stdout=f)
#all info after finish tinyRAM with params t,s now in condoub.txt, find here ACCEPT
f.close()
f=open("condoub.txt", 'r')
for line in f:
	if "can make this transaction" in line:
		flag =True

if flag==True:
	#print("old status",asm_cash1,asm_cash2)
	asm_cash1-=asm_value
	asm_cash2+=asm_value
	#print("new status",asm_cash1,asm_cash2)
	print("can make transaction")
else:
	print("ERROR: Can't make transaction")
