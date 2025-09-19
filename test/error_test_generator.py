import random
import json
import time
import os
import sys

# 设置随机种子确保可重现性
random.seed(42)

# O(n²)时间复杂度的排序算法 - 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 基础模板
template = {
    "max_cpu_time": 4000,  # 5秒超时限制
    "max_memory": 2684354560,  # 足够大的内存限制
    "test_display": 1,
    "language": "python",
    "src": """
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
    
    # 排序 - 使用选择排序算法 O(n²)
    # 您可以更改为bubble_sort或insertion_sort来使用其他排序算法
    sorted_arr = selection_sort(arr)
    
    # 输出结果
    print(" ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()
""",
    "test": []
}

# 生成测试用例
def generate_test_cases():
    test_cases = []
    
    # 生成10个测试点，数据量从10递增到1000000
    sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000]
    
    for size in sizes:
        # 生成随机数组
        arr = [random.randint(-10000, 10000) for _ in range(size)]
        
        # 转换为输入格式
        input_str = " ".join(map(str, arr))
        
        # 生成正确的输出（这里使用排序作为示例）
        output_str = " ".join(map(str, sorted(arr)))
        
        # 添加测试用例
        test_cases.append({
            "input": input_str,
            "output": output_str
        })
    
    return test_cases

# 生成测试文件
def save_test_cases(filename="test_cases.json"):
    test_cases = generate_test_cases()
    
    # 构建测试数据结构
    test_data = {
        "max_cpu_time": 10000,  # 10秒超时限制
        "max_memory": 536870912,  # 内存限制（512MB）
        "test_display": 1,
        "language": "python",
        "src": """
def main():
    # 读取输入
    arr = list(map(int, input().split()))
    
    # 进行处理（这里以排序为例）
    sorted_arr = sorted(arr)
    
    # 输出结果
    print(" ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()
""",
        "test": test_cases
    }
    
    # 写入文件
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(test_data, f, indent=4, ensure_ascii=False)
    
    print(f"测试用例已保存到: {filename}")
    print(f"生成了10个测试点，数据量从10个到1000000个")

# 执行生成
save_test_cases()

if __name__ == "__main__":
    # 支持命令行参数指定输出文件名
    output_file = "size_test_cases.json"
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    if save_test_cases(output_file):
        print("测试用例生成成功!")
    else:
        print("测试用例生成失败!")
        sys.exit(1)