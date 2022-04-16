T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    benefit = 0
    maxi = 0
    for i in range(N-1, -1, -1):
        if stocks[i] >= maxi:
            maxi = stocks[i]
            continue

        benefit += maxi - stocks[i]

    print(benefit)
