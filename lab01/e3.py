# CANNOT COMPARE STRING TO INT AHAHAHAHHAHAHAHAHAHAHHAHAHAGHAHAHAHHAHA
# iterations = int(input("Enter number of times you want to iterate: "))
# when entering :q it gives error
# while iterations < 0:
#     iterations = int(input("It must be 0 or greater: "))
#
# i = 0
# total = 0
# while i < iterations:
#     total += 1 / (2 ** i)
#     i = i + 1
#
# print("Sum: ", total)

# anti gia ena polu aplo goto prepei na bazw flags????????????????
flag = False
while not flag:
    iterations = input("enter number of times you want to iterate: ")
    if iterations.isdigit():
        iterations = int(iterations)
        flag = True

i = 0
total = 0
while i < iterations:
    total += 1 / (2 ** i)
    i += 1

print("Sum: ", total)
