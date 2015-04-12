import time, logging
from timing import log_timing
from multiprocessing import Pool


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def f(x):
    time.sleep(x)
    return x*x

if __name__ == '__main__':
    p = Pool(3)
    with log_timing('test multiprocessing', logger):
        print(p.map(f, [1, 2, 3]))