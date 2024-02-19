import math

def simp_rule(f, a, b, n = 1000):
    """
    This function uses the Simpsons 1/3 rule of numerical integration.
    :param f:  the callback function. The function of x to integrate
    :param a: left limit of integration
    :param b: right limit of integration
    :param n:  number of points in integration
    :return: the value of the integral of f(x) between a, b
    Chatgpt and Dr. Jim Smay's video assisted in the development of this function
    video titled hw3b_SP24   https://youtu.be/mhMG3mFU18M?si=4fF89xy_cyos9pm3
    """
    xL = min(a,b)
    xR = max(a,b)
    if xL == xR:
        return 0
    h = (xR - xL) / n # calculate panel width
    x = [xL + i * h for i in range(n + 1)]
    integral = f(xL) + f(xR)
    for i in range(1, n, 2):
        integral += 4 * f(x[i])
    for i in range(2, n - 1, 2):
        integral += 2 * f(x[i])
    integral *= h / 3
    return integral # return the value for the interval.

def distribution(m, u):
    """
    Calculates the cumulative distribution function (CDF) for a t-distribution.
    The function uses Simpson's rule for numerical integration to compute the CDF.
    The t-distribution is defined by the degrees of freedom `m` and the upper limit of integration `u`.
    Parameters:
    m (int): The degrees of freedom for the t-distribution.
    u (float): The upper limit of integration for the CDF.
    Returns:
    prob (float): The computed probability from the CDF of the t-distribution.
    chatgpt assisted in developing this function
    """
    def Fz(x):
        """
        Calculates the value of the probability density function (PDF) for a t-distribution at a given point.
        The t-distribution is defined by the degrees of freedom `m`. The function computes the PDF value at the point `x`.
        Note: The variable `m` must be defined in the scope where this function is called.
        Parameters:
        x (float): The point at which to compute the PDF of the t-distribution.
        Returns:
        (float): The computed PDF value of the t-distribution at `x`.
        chatgpt assisted in developing this function
        """
        return math.gamma((m + 1) / 2) / (math.sqrt(m * math.pi) * math.gamma(m / 2)) * (1 + (x ** 2)/ m) ** ( - (m + 1) / 2)
    return simp_rule(Fz, 0, u, 1000) + 0.5

def main():
    """
    Interactively calculates the cumulative distribution function (CDF) for a t-distribution.
    The function prompts the user to input the degrees of freedom and the z value.
    It then calculates the CDF using the `distribution` function and prints the result.
    The user is repeatedly prompted to calculate another CDF until they choose to quit.
    chatgpt assisted in developing this function and so did Dr. Jim Smay's video
    https://youtu.be/mhMG3mFU18M?si=MY85waZed1nfcvaH
    """
    quit = False
    while (quit == False):
        m = int(input(f"Enter degrees of freedom:  "))
        u = float(input(f"Enter z value: "))
        prob = distribution(m, u) # Begin calculation
        print(f"F({m})={prob:.3f}")
        quit = input("Calculate another (y/n)?") == "n"
    pass


if __name__=="__main__":
    main()