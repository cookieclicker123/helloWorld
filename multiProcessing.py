from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count <=num:
        count+=1


def main():
    print("Number of CPU cores: ", cpu_count())
    
    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))
    
    start_time = time.time()  # Get the current time

    a.start()
    b.start()
    c.start()   
    d.start() 
    e.start()
    f.start()
    g.start()
    h.start()

    
    a.join()
    b.join()
    c.join()    
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    end_time = time.time()

    print("Time taken: ", end_time - start_time, "seconds")



if __name__ == "__main__":
    main()