
# https://www.youtube.com/watch?v=GT10PnUFLlE
# multi-threading (single CPU, GIL) vs multi-processing (multiple CPUs - works well with CPU intensive apps)

import multiprocessing as mp
import time
import math

results_a = [float]
results_b = [float]
results_c = [float]

def make_calculation_one(numbers: list[float]) -> None:
    for number in numbers:
        # results_a.append(math.factorial(number))
        results_a.append(math.sqrt(number ** 3))

def make_calculation_two(numbers: list[float]) -> None:
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

def make_calculation_three(numbers: list[float]) -> None:
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))


def main() -> None:

    # mp.cpu_count()
    # mp.active_children()
    # mp.current_process()
    # mp.get_logger()

    # numbers = [5_000_000 + x for x in range(20000000)]
    numbers = list(range(50000000))

     # 1 - Process in sequence
    start = time.time()

    make_calculation_one(numbers=numbers)
    make_calculation_two(numbers=numbers)
    make_calculation_three(numbers=numbers)

    end = time.time()
    print(f"Sequence completed in {(end - start):.4f} seconds")

    # # 2 - Process in parallel
    # mp.set_start_method("fork")
    p1 = mp.Process(target=make_calculation_one, args=(numbers,))
    p2 = mp.Process(target=make_calculation_two, args=(numbers,))
    p3 = mp.Process(target=make_calculation_three, args=(numbers,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()

    # p1.join()
    # p2.join()
    # p3.join()

    end = time.time()
    print(f"Parallel completed in {(end - start):.4f} seconds")

if __name__ == "__main__":
    main()
