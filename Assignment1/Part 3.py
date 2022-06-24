from urllib.request import Request, urlopen
import time
import sys

#a
diskcontent = ""
start = time.time()
while (time.time() - start < 4):
    f = open(r"C:\Users\rober\Desktop\Grad\CSC555\Assignment1\CDM _ DePaul CDM.html", 'r', encoding='utf-8')
    diskcontent = diskcontent + f.read()
    f.close()
end = time.time()
disktime = end - start
disksize = sys.getsizeof(diskcontent) / 1048576 #convert to megabytes (1024^2)
diskspeed = disksize/disktime
print("Reading from disk")
print("{} MBytes/sec".format(diskspeed))



#b
webcontent = ""
start = time.time() #initial time
while (time.time() - start < 4):
    url = 'https://www.cdm.depaul.edu/Pages/default.aspx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    request = Request(url, headers=headers)
    resource = urlopen(request)
    webcontent = webcontent + resource.read().decode()
end = time.time() #exact end time
webtime = end - start
websize = sys.getsizeof(webcontent) / 1048576 #convert to megabytes (1024^2)
webspeed = websize/webtime
print("Reading from the Web")
print("{} MBytes/sec".format(webspeed))

#c
f = open(r"C:\Users\rober\Desktop\Grad\CSC555\Assignment1\CDM _ DePaul CDM.html", 'r', encoding='utf-8')
content = f.read() #get material to write
f.close()
writecontent = ""

start = time.time()
while (time.time() - start < 4):
    f = open(r"C:\Users\rober\Desktop\Grad\CSC555\Assignment1\writetodisk.txt", 'a', encoding='utf-8')
    f.write(content)
    writecontent = writecontent + content
end = time.time()
writetime = end - start
writesize = sys.getsizeof(writecontent) / 1048576 #convert to megabytes (1024^2)
writespeed = writesize/writetime
print("Writing to disk")
print("{} MBytes/sec".format(writespeed))


#d
diskcontent = ""
start = time.time()
while (time.time() - start < 4):
    f = open(r"C:\Users\rober\Desktop\Grad\CSC555\Assignment1\CDM _ DePaul CDM.html", 'r', encoding='utf-8')
    content = f.read()
    print(content)
    diskcontent = diskcontent + content
    f.close()
end = time.time()
disktime = end - start
disksize = sys.getsizeof(diskcontent) / 1048576 #convert to megabytes (1024^2)
diskspeed = disksize/disktime
print("Reading and Printing from disk")
print("{} MBytes/sec".format(diskspeed))


