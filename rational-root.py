import math

def potential_solutions(a, d):
    factors_d_array = []
    factors_a_array = []
    potential_solutions_array = []
    for x in range(1, abs(d) + 1):
        if (d % x == 0):
            factors_d_array.append(d / x)
    for y in range(1, abs(a) + 1):
        if (a % y == 0):
            factors_a_array.append(a / y)
    for factor_d in factors_d_array:
        for factor_a in factors_a_array:
            potential_solutions_array.append(factor_d / factor_a)
    for factor_d in factors_d_array:
        for factor_a in factors_a_array:
            potential_solutions_array.append(-1 * factor_d / factor_a)
    return potential_solutions_array

def find_solution(a, b, c, d, the_potential_solutions):
    solutions_array = []
    for solution in the_potential_solutions:
        cubic_value = (a * solution ** 3 + b * solution ** 2 +
                       c * solution + d)
        if cubic_value == 0:
            solutions_array.append(solution)
    return solutions_array

a = 2
b = -1
c = -13
d = -6

the_potential_solutions = potential_solutions(a, d)

the_solutions = find_solution(a, b, c, d, the_potential_solutions)

print("The solutions are ")
for solution in the_solutions:
    print("x = " + str(solution) + " \n")
