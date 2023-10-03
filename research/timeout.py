from concurrent.futures import ProcessPoolExecutor
import time

def main():
    with ProcessPoolExecutor(max_workers=1) as pool:
        future = pool.submit(f)
        res = None
        try:
            res = future.result(timeout=3)
        except TimeoutError:
            pass
        print(res)

def f():
    time.sleep(1)
    return "fish"

if __name__ == "__main__":
    main()
