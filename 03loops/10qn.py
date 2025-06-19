
import time

wait_time = 1
attempts = 0
max_retries = 5

while attempts < max_retries:
    print("Attempt no.:",attempts+1,"Wait Time:",wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

