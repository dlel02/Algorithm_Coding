while True:
    counter = 0
    check = []
    N = int(input())
    if N == -1:
        break
    
    for _ in range(1, N):
        if N % _ == 0:
            check.append(_)
            counter += _
            
            
    if counter == N:
        print("{} = ".format(N), end = "")
        for i in range(len(check)):
            if i == len(check) -1:
                print("{}".format(check[i]), end = "")
            else:
                print("{} + ".format(check[i]), end = "")
        print()
    else:
        print("{} is NOT perfect.".format(N))