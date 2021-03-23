if __name__ == '__main__':
    n, m, k = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()

    first = data[n-1]
    second = data[n-2]

    if first==second:
        print(m*first)
    else:
        val,res = divmod(m,k+1)
        print(val*(first*k+second)+res*first)