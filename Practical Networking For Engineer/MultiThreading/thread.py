import threading
import time
import random

class MyThread(threading.Thread):
    
    def __init__(self, numb):
        super(MyThread, self).__init__()
        self.number = numb
        
    def run(self):
        time.sleep(1)
        print("Running" + str(self.number) + "\n")
        

threads_list = []

def startAllThreads_WaitTillDone():

    # Get all threads started and add all to the list of threads
    for i in range(10):
        t = MyThread(i)
        threads_list.append(t)
        t.start()

    # Wait till the threads are done, then carry on
    for one_thread in threads_list:
        one_thread.join()

    # All the above threads are done, then we go on printing 'Done!'
    print("Done!")

def check_status_of_all_threads():
    for one_thread in threads_list:
        # The main thread does not have the 'number' property, so use except to get its name
        try:
            print(one_thread.number, " : " , one_thread.is_alive())
            one_thread.start()
            print(one_thread.number, " : " , one_thread.is_alive())
            time.sleep(3)
        except:
            print(one_thread.getName())



for i in range(10):
    t = MyThread(i)
    threads_list.append(t)
    
    
check_status_of_all_threads()

# Wait till the threads are done, then carry on
for one_thread in threads_list:
    one_thread.join()

print("Done!")

