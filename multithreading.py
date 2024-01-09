import threading
import time

def eatBreakfast():
    time.sleep(3)
    print("You ate breakfast")

def drinkTea():
    time.sleep(4)
    print("You drank tea")

def study():
    time.sleep(5)
    print("You studied")

x = threading.Thread(target=eatBreakfast, args=())
x.start()
y = threading.Thread(target=drinkTea, args=())
y.start()
z = threading.Thread(target=study, args=()) 
z.start() 

x.join()
y.join()    
z.join()    


#eatBreakfast()
#drinkTea()
#study()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
