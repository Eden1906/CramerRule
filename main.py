
def cramer():

    print("Enter the variables in the following format")
    print("a1x+b1y=c1")
    print("a2x+b2y=c2")

    a1 = float(input("enter a1:"))
    b1 = float(input("enter b1:"))
    c1 = float(input("enter c1:"))
    a2 = float(input("enter a2:"))
    b2 = float(input("enter b2:"))
    c2 = float(input("enter c2:"))

    print("The equations entered are")
    print(a1, "x +", b1, "y=", c1)
    print(a2, "x +", b2, "y =", c2)
    print("Now let's look at the equations as determinate")
    print("##########")
    print(a1, b2, "|", c1)
    print(a2, b2, "|", c2)
    print("##########")

    if a1*b2 - a2*b1 == 0:
        print("The determinant of the variables matrix is zero,cant apply cramer rule")
    else:
        x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
        print("x=",c1*b2 - c2*b1,"/",a1*b2 - a2*b1,"=>Dx")
        y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
        print("y=",a1*c2 - a2*c1, "/", a1*b2 - a2*b1,"=>Dy")

        print("Solutions by using cramer rule are")
        print("x=", x, "y=", y)


cramer()
