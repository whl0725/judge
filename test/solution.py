def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    # 读取输入
    arr = list(map(int, input().split()))
    
    # 排序 - O(n²)复杂度
    # 注意：大量数据可能会导致超时
    count = 60000  # 循环次数（注意：这是Python注释格式）
    sorted_arr = selection_sort(arr)
    
    # 输出结果
    print(" ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main() 