def main():
    print("Main")


def coord_velocity ( t, v_0):
    integral = scipy.integrate.quad(coord_acceleration, 0, t)
    return v_0 + integral

def gamma(t, v_0):
    return  1/((1-(coord_veloity(t, v_0)/c)**2)**(1/2))

def inverse_gamma(t, v_0):
    return 1/gamma(t, v_0)

def proper_time (t, v_0):
    return scipy.integrate.quad(inverse_gamma, 0, t, args=(v_0))

def proper_wordline():


if __name__ == '__main__':
    main()
