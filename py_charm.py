def num_list(a):
    for i in range(a):
        if i > 0:
            print(i)
            print("wait for new number")
            a -= 1
    print("---END---")

num_list(5)

