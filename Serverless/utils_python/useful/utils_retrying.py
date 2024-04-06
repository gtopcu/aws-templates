
# https://pypi.org/project/retrying/
# pip install --upgrade retrying

import random
from retrying import retry

# @retry() # retries forever
@retry(wait_random_min=1000, wait_random_max=2000) # retries if exception
def do_something_unreliable():
    rand = random.randint(0, 10)
    print("Random:", rand)
    if  rand > 5:
        raise IOError("Broken sauce")
    else:
        print("Retry complete")

do_something_unreliable()

@retry(stop_max_attempt_number=7)
def stop_after_7_attempts():
    print("Stopping after 7 attempts")

@retry(stop_max_delay=10000)
def stop_after_10_s():
    print("Stopping after 10 seconds")

@retry(wait_fixed=2000)
def wait_2_s():
    print("Wait 2 second between retries")

@retry(wait_random_min=1000, wait_random_max=2000)
def wait_random_1_to_2_s():
    print("Randomly wait 1 to 2 seconds between retries")

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def wait_exponential_1000():
    print("Wait 2^x * 1000 milliseconds between each retry, up to 10 seconds, then 10 seconds afterwards")

def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)

@retry(retry_on_exception=retry_if_io_error)
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")

@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def only_raise_retry_error_when_not_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError")

def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None

@retry(retry_on_result=retry_if_result_none)
def might_return_none():
    print("Retry forever ignoring Exceptions with no wait if return value is None")