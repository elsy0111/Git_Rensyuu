for i in range(1, 10):
    for j in range(1, 10):
        if j == 1:
            print(i, "|", end = "")
        if i * j < 10:
            print(" ", end = "")
        print(i * j, end = " ")
        if j == 9:
            print("|")
