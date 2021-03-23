if __name__ == '__main__':
    n, m = map(int,input().split())

    min_max = 0;
    for i in range(n):
        data = list(map(int,input().split()))
        if(min_max<min(data)):
            min_max = min(data)
        #max(min_max,min(data)) 가 더 깔끔하긴함
    print(min_max)