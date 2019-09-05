if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    d=dict(enumerate(arr,0))
    el = max(d.values())
    count = arr.count(el)
    for x in range(count):
        arr.remove(el)
    print(max(arr))

