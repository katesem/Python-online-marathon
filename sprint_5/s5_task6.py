import cmath

def solve_quadric_equation(a, b, c):
    try:
        d = (float(b)**2) - 4*float(a)*float(c)
        x1 = (-b-cmath.sqrt(d))/(2*a)
        x2 = (-b+cmath.sqrt(d))/(2*a)

    except ZeroDivisionError:
        print("Zero Division Error" )
    except ValueError:
        print("Could not convert string to float")
    else:
        print(f"The solution are x1={x1} and x2={x2}")
