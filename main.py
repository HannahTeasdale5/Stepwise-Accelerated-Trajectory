import numpy as np

def main():
    print("Main")
    a = 0.5 #must be below c
    T = 10
    t = np.linspace(0, 2*T, 1000)
    c = 1
    tao = proper_time(a, t, T, c)
    print(tao)

def acceleration (a, t, T):
    if t < T/2:
        return a
    elif t < 3*T/2:
        return -a
    else:
        return a

def velocity (a, t, T):
    if t < T / 2:
        return a*t
    elif t < 3 * T / 2:
        return a*(T-t)
    else:
        return a*(t-2*T)

def antiderivative(k, u):
    root = (1 - k*u)**(-1/2)
    return (u/2)*root + (1/(2*k))*np.arcsin(k*u)

def g_function(a, c, t):
    return antiderivative(a/c, t)

def proper_time(a, t, T, c):
    if t < T / 2:
        return g_function(a, c, t)
    elif t < 3 * T / 2:
        return 2*g_function(a, c, T/2) + g_function(a, c, t-T)
    else:
        return 4*g_function(a, c, T/2) + g_function(a, c, t-2*T)


if __name__ == "__main__":
    main()
