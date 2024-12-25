import time

def stopwatch():
    print("Press ENTER to start the stopwatch. Press CTRL+C to stop.")
    input()
    start_time = time.time()
    try:
        while True:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"Elapsed Time: {elapsed_time} seconds", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped!")

stopwatch()

