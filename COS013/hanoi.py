""" Solving the Hanoi Tower Problem """

def print_step(start, end):
    print(str(start) + '->' + str(end))
def hanoi(n, start, end):
    if n == 1:
        print_step(start, end)
    else:
        other = 6 - (start + end)
        hanoi (n-1, start, other)
        print_step(start, end)
        hanoi(n-1, other, end)

hanoi(3,1,3)
