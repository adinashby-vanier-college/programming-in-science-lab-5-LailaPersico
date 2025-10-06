# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range (n, 0, -1):
        if i == n or i == n - (n - 1):
            result += (n * "*")
            result += "\n"
        else:
            result += ("*" + (n - 2) * " " + "*")
            result += "\n"
    return result.rstrip()

#print(hollow_square(5)) 


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(n):
        for j in range(1, 2 + i):
            result += str(j)
        result += "\n"

    return result.rstrip()
            

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0
    total = 0
    for i in range(1, n + 1):
        total += i

    return total 


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        result += " " * (n - i - 1)
        result += "*" * (2 * i + 1)
        result += "\n"
    return result.rstrip()

    

