def nose(n):
    if n == 0:
        print(0)
    else:
        for a in range(n):
            if a == 0:
                print(1)
            else:
                print(f"1/{a+1}")

nose(5)