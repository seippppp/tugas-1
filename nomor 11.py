M = int(input("enter first side: "))
N = int(input("enter second side: "))

side1 =  M ** 2 - N ** 2
side2 = 2 * M * N
hyp = M ** 2 + N ** 2

print(f"the triple pythagorean is {side1} {side2} {hyp}")