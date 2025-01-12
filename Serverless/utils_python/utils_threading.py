
import threading
import time

import concurrent.futures
from concurrent.futures import Future

done = False

def worker(arg):
    counter = 0
    while not done and counter < 10:
        time.sleep(1)
        counter += 1
        print("Thread", arg, "-", counter)

# worker()
# t1 = threading.Thread(target=worker, args=(100, "200"), name="thread-1", daemon=False)
# #t1 = threading.Thread(target=worker, args=(100, "200"), daemon=True).start() # daemon threads stop when others finish

# t1.start()
# t1.join(5) # wait 5 secs for t1 to finish

# input("Press any key to exit..")
# done = True

if __name__ == "__main__":

    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     executor.map(worker, (1, ))
    #     executor.map(worker, (2, ))
    #     executor.map(worker, (3, ))
    #     # future:Future = executor.submit(worker, (3, ))
    #     executor.shutdown(wait=True)

    # Use with multiple threads/processes
    workers = 4
    # with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
    #     futures = [
    #         executor.submit(do_sth, job_no, workers)
    #         for job_no in range(workers)
    #     ]
    #     concurrent.futures.wait(futures)
