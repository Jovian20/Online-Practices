if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    
    first = max(arr)
    while first in arr:
        arr.remove(first)
    second = max(arr)
    print(second)
