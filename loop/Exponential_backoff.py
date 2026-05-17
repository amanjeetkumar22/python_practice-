import time

wait_time=1
attempt=0
max_tries=5

while attempt<max_tries:
    print("attempt:",attempt+1,"wait time:",wait_time,"second")
    time.sleep(wait_time)
    attempt+=1
    wait_time*=2