import cmath


def sqrt():
    try:
        num = int(input("Enter the number : "))
        if num >= 0:
            main(num)
        else:
            complex_num(num)
    except:
        print("OOPS..!!Something went wrong, try again")
        sqrt()
    return


def main(num):
    square_root = num**(1/2)
    print("The square Root of ", num, " is ", square_root)
    return


def complex_num(num):
    ans = cmath.sqrt(num)
    print("The Square root if ", num, " is ", ans)
    return


sqrt()

# функцию hello_world, которая будет печать приветственную строку "Hello World".
def hello_world():
    m = 'hello, world'
    print(m.replace('h', 'H') and m.replace('w', 'W'))


hello_world()