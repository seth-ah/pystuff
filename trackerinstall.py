import os, time
clear = open('clear.py', 'w+')
clear.write("f = open('mem.txt', 'w+')\nf.truncate()\nf.close()")
clear.close()
os.system("python clear.py")
time.sleep(0.1)
os.system("del clear.py -y")