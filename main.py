import numpy as np
import matplotlib.pyplot as plt


def main():

    #parameters
    x_max = 0.005
    v_max = 0.2 #aT/c needs to be between 0 and 1 so v_max <= c/2, not sure why the factor of 1/2
    a0 = (v_max**2)/x_max
    T = 2*x_max/v_max
    t = np.linspace(0, 2 * T, 10000)
    c = 1


    tao = proper_time(a0, t, T, c)
    x_t = trajectory_t(a0, t, T)
    v_t = velocity_t(a0, t, T)
    a_t = acceleration_t(a0, t, T)

    x_tao = trajectory_tao(a0, tao, T)

    plt.plot(t, tao)
    plt.title("Tao")
    plt.show()
    plt.plot(t, x_t)
    plt.title("X")
    plt.show()
    plt.plot(t, v_t)
    plt.title("V")
    plt.show()
    plt.plot(t, a_t)
    plt.title("A")
    plt.show()

    plt.plot(tao, x_tao)
    plt.title("X in accelerated coordinates")
    plt.show()
    plt.plot(tao, v_tao)
    plt.title("V in accelerated coordinates")
    plt.show()
    plt.plot(tao, a_tao)
    plt.title("A in accelerated coordinates")
    plt.show()



def coord_acceleration(a0, t, T):
    low_t = a0 * (t <= T / 2).astype(int)
    medium_t = -a0 * ((t > T / 2) & (t <= 3 * T / 2)).astype(int)
    high_t = a0 * (t > 3 * T / 2).astype(int)
    return low_t + medium_t + high_t


def coord_velocity(a0, t, T):
    low_t = a0 * t * (t <= T / 2).astype(int)
    medium_t = a0 * (T - t) * ((t > T / 2) & (t <= 3 * T / 2)).astype(int)
    high_t = a0 * (t - 2*T) * (t > 3 * T / 2).astype(int)
    return low_t + medium_t + high_t

def coord_trajectory(a0, t, T):
    low_t = (0.5)*a0 *(t**2) * (t <= T / 2).astype(int)
    medium_t = (a0*T*t - 0.5*a0*(t**2) - (0.25)*a0*(T**2)) * ((t > T / 2) & (t <= 3 * T / 2)).astype(int)
    high_t = (0.5*a0*((t-2*T)**2)) * (t > 3 * T / 2).astype(int)
    return low_t + medium_t + high_t

def acc_trajectory(a, tao, T, c):
    #solve for coordinate time t at proper time tao
    # t =
    #calculate the accelration at coordinate time t
    a = coord_acceleration(a, t, T)
    #find the four vector due to this acceleration
    x = (1/a) * np.cosh(a*tao)
    t = (1/a) * np.sinh(a*tao)
    return [c*t, x]


def antiderivative(k, u):
    root = (1 - k * u) ** (-1/2)
    return (u / 2) * root + (1 / (2 * k)) * np.arcsin(k * u)


def g_function(a0, c, t):
    return antiderivative(a0 / c, t)


def proper_time(a0, t, T, c):
    low_t = (t <= T / 2).astype(int)
    medium_t = ((t > T / 2) & (t <= 3 * T / 2)).astype(int)
    high_t = (t > 3 * T / 2).astype(int)
    return low_t*(g_function(a0, c, t)) + medium_t*(2 * g_function(a0, c, T / 2) + g_function(a0, c, t - T)) + (4 * g_function(a0, c, T / 2) + g_function(a0, c, t - 2 * T))*high_t

if __name__ == "__main__":
    main()
