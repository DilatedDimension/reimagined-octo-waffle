
coeffList = []
coeffNum = 0
print("Enter the coefficients for your function.")
while True:
    coeff = input("Enter the " + str(coeffNum) + " order coefficient ('q' to end):")

    if coeff == -666:
        break
    else:
        coeffList.append(coeff)

print(coeffList)
