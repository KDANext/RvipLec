Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@KDANext 
nickiteks
/
lectionRwip
Public
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
lectionRwip/main.py /
@nickiteks
nickiteks ltction2
Latest commit d95a3e0 yesterday
 History
 1 contributor
50 lines (37 sloc)  1.16 KB
   
import threading
import time

def thread_a():
    print('Thread A is starting...')

    print('Thread A waiting to acquire lock A.')
    lock_a.acquire()
    print('Thread A has acquired lock A, performing some calculation...')
    time.sleep(2)

    print('Thread A waiting to acquire lock B.')
    lock_b.acquire()
    print('Thread A has acquired lock B, performing some calculation...')
    time.sleep(2)

    print('Thread A releasing both locks.')
    lock_a.release()
    lock_b.release()

def thread_b():
    print('Thread B is starting...')

    print('Thread B waiting to acquire lock B.')
    lock_b.acquire()
    print('Thread B has acquired lock B, performing some calculation...')
    time.sleep(5)

    print('Thread B waiting to acquire lock A.')
    lock_a.acquire()
    print('Thread B has acquired lock A, performing some calculation...')
    time.sleep(5)

    print('Thread B releasing both locks.')
    lock_b.release()
    lock_a.release()

lock_a = threading.Lock()
lock_b = threading.Lock()

thread1 = threading.Thread(target=thread_a)
thread2 = threading.Thread(target=thread_b)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Finished.')
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete