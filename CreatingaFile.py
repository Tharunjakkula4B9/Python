'''
open()
read()
readline()
write()
writeline()
close()
fseek()
ftell()
'''
fp=open("csa1.txt","w")
if fp:
    print("file is created successsfully")
fp.writelines("all students are welcomed to cmr engineering college\n today's python class \n today's ongoing class ")

fp.close()
