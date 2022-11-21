import numpy as np
#We have to do the computation for 7 values which are 10,100,100, 1k,10k,100k,1000k
subintervals = [10, 100, 100, 1000, 10000, 100000, 1000000]


def integral(fn, samples_number, lower, upper):
    dx = np.divide((upper - lower), samples_number)
    Xs = np.arange(lower, upper, dx)
    integral = np.sum(fn(Xs)*dx)
    return integral


def fn(x): return np.abs(np.sin(x))


if __name__ == '__main__':

    a = 0.0
    b = np.pi
#We loop to obtain results for each value of subintervals
    for i in subintervals:
        print(integral(fn, i, a, b))
