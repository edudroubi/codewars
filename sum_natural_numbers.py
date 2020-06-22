# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Note: If the number is a multiple of both 3 and 5, only count it once.
#
# Courtesy of ProjectEuler.net


def solution(number):
    int_division_3 = (number-1) // 3
    int_division_5 = (number-1) // 5
    base_op_3 = 3
    base_op_5 = 5
    multiples = []
    for i in range(int_division_3):
        multiples.append(base_op_3)
        base_op_3 = base_op_3 + 3
    for i in range(int_division_5):
        multiples.append(base_op_5)
        base_op_5 = base_op_5 + 5
    multiples = sum(set(multiples))
    return(multiples)

print(solution(10))
