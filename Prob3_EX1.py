
def f(x, y, z):
    """
    This function represents the system of first order differential equations derived from the given second order
    differential equation y'' - y = x. It takes as input the current values of x, y, and z (where z is y'), and returns
    the derivatives of y and z.
    :x: The current value of the independent variable.
    :y: The current value of y(x).
    :z: The current value of y'(x).
    Returns:
        tuple: A tuple containing the derivatives of y and z.
    Chatgpt assisted with the development of this function
    """
    return z, x + y

def improved_euler(h, x, y, z):
    """
    This function implements the Improved Euler (Heun's) method for solving second order differential equations.

    Parameters:
    h (float): The step size for the numerical solution.
    x (float): The current value of the independent variable.
    y (float): The current value of the dependent variable y(x).
    z (float): The current value of the derivative y'(x).

    Returns:
    y (float): The updated value of y after one step of the Improved Euler method.
    z (float): The updated value of y' after one step of the Improved Euler method.

    The function calculates two estimates (k1 and k2) of the change in y and y' over the interval [x, x+h] using the
    function f(x, y, z) which represents the second order differential equation. The final values of y and y' are then
    updated using the average of these estimates.
    Chatgpt assisted with the development of this function
    """
    k1_y = h * z
    k1_z = h * f(x, y, z)[1]
    k2_y = h * (z + k1_z)
    k2_z = h * f(x + h, y + k1_y, z + k1_z)[1]
    y += (k1_y + k2_y) / 2
    z += (k1_z + k2_z) / 2
    return y, z

def runge_kutta(h, x, y, z):
    """
    This function is modeled after the Runge-Kutta Method in
    Kreyszig's "Advanced Engineering Mathematics" 10th ed. section 21.3 formula (6b).  This function
    calculates 4 auxiliary quantities used to approximate the next iterative value of the solution.
    The function uses the parameters h,x,y,z to calculate the next values of y and z (i.e., y(x+h) and z(x+h)).
    :param h: is the step size of the iteration
    :param x: the current value of the independent variable.
    :param y: the current value of the y(x) function that is being approximated
    :param z: the equivalent to y'(x).
    :return: the updated values of y and z after one step.
                the updated value of y represents the approximate value of the function y(x) at the point x + h.
                the updated value of z represents the approximate value of the derivative y'(x) at the point x + h.
    Chatgpt assisted with the development of this function.
    """
    k1_y = h * z
    k1_z = h * f(x, y, z)[1]
    k2_y = h * (z + 0.5 * k1_z)
    k2_z = h * f(x + 0.5 * h, y + 0.5 * k1_y, z + 0.5 * k1_z)[1]
    k3_y = h * (z + 0.5 * k2_z)
    k3_z = h * f(x + 0.5 * h, y + 0.5 * k2_y, z + 0.5 * k2_z)[1]
    k4_y = h * (z + k3_z)
    k4_z = h * f(x + h, y + k3_y, z + k3_z)[1]
    y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
    z += (k1_z + 2 * k2_z + 2 * k3_z + k4_z) / 6
    return y, z

def solve_ode(method, h, x_end):
    """
    This function solves the given second order differential equation using the specified numerical method (either
    'improved_euler' or 'runge_kutta'), step size h, and ending value of x (x_end). It initializes y and z to the given
    initial conditions, then iteratively updates y and z until x reaches x_end.
    :method: The numerical method to use ('improved_euler' or 'runge_kutta').
    :h: The step size for the numerical solution.
    :x_end: The ending value of x.
    :returns:
        tuple: A tuple containing the final values of y and z.
    Chatgpt assisted with developing this function.
    """
    x, y, z = 0, 1, -2
    while x < x_end:
        if method == 'improved_euler':
            if x + h > x_end:
               h = x_end - x
            y, z = improved_euler(h, x, y, z)
        elif method == 'runge_kutta':
            if x + h > x_end:
                h = x_end - x
            y, z = runge_kutta(h, x, y, z)
        x = round(x, 5)
        x +=  h
    return y, z

def main():
    """
    This function prompts the user for the ending value of x and the step size, then calls the solve_ode function
    to solve the differential equation using both the Improved Euler and Runge-Kutta methods. The results
    are then printed to the CLI.
    The user is asked to continue or end the function after each execution.
    Chatgpt assisted with developing this function.
    """
    quit = False
    while (quit == False):
        print("For the initial value problem y’’- y = x")
        x_end = float(input("At what value of x do you want to know y and y’? "))
        h = float(input("Enter the step size for the numerical solution: "))
        y_ie, z_ie = solve_ode('improved_euler', h, x_end)
        print(f"At x={x_end}")
        print(f"For the improved Euler method: y={y_ie:.4f}, and y’={z_ie:.4f}")
        y_rk, z_rk = solve_ode('runge_kutta', h, x_end)
        print(f"For the improved Euler method: y={y_rk:.4f}, and y’={z_rk:.4f}")
        quit = input("Do you want to continue with another x? (y/n)") == "n"
    pass

if __name__ == "__main__":
    main()