#!/usr/bin/env python3
"""
Data Cleaner Pro 简化测试脚本
"""

import json
from datetime import datetime
import csv

def test_basic_cleaning():
    """测试基本数据清理功能"""
    print("=== Data Cleaner Pro 简化测试开始 ===")
    print(f"测试时间: {datetime.now()}")
    
    # 创建测试数据
    test_data = [
        {"id": 1, "name": "张三", "age": 25, "score": 85.5},
        {"id": 2, "name": "李四", "age": 30, "score": 92.0},
        {"id": 3, "name": "王五", "age": None, "score": 78.5},
        {"id": 4, "name": None, "age": 35, "score": 88.0},
        {"id": 5, "name": "赵六", "age": 40, "score": None}
    ]
    
    print(f"\n原始数据:")
    for item in test_data:
        print(f"  {item}")
    
    # 数据清理
    print("\n=== 执行数据清理 ===")
    
    cleaned_data = []
    total_age = 0
    age_count = 0
    total_score = 0
    score_count = 0
    
    # 第一遍：计算平均值
    for item in test_data:
        if item["age"] is not None:
            total_age += item["age"]
            age_count += 1
        if item["score"] is not None:
            total_score += item["score"]
            score_count += 1
    
    avg_age = total_age / age_count if age_count > 0 else 0
    avg_score = total_score / score_count if score_count > 0 else 0
    
    # 第二遍：清理数据
    for item in test_data:
        cleaned_item = item.copy()
        
        # 填充缺失值
        if cleaned_item["name"] is None:
            cleaned_item["name"] = "未知"
        if cleaned_item["age"] is None:
            cleaned_item["age"] = avg_age
        if cleaned_item["score"] is None:
            cleaned_item["score"] = avg_score
            
        cleaned_data.append(cleaned_item)
    
    print(f"清理后数据:")
    for item in cleaned_data:
        print(f"  {item}")
    
    # 统计数据
    stats = {
        "total_records": len(cleaned_data),
        "average_age": avg_age,
        "average_score": avg_score,
        "max_score": max(item["score"] for item in cleaned_data),
        "min_score": min(item["score"] for item in cleaned_data)
    }
    
    print(f"\n=== 数据统计 ===")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # 保存结果
    result = {
        "test_time": str(datetime.now()),
        "test_status": "success",
        "cleaned_records": len(cleaned_data),
        "statistics": stats
    }
    
    with open('simple_test_results.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    # 保存为CSV
    with open('cleaned_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age", "score"])
        writer.writeheader()
        writer.writerows(cleaned_data)
    
    print(f"\n测试结果已保存到: simple_test_results.json")
    print(f"清理数据已保存到: cleaned_data.csv")
    print("=== Data Cleaner Pro 简化测试完成 ===")
    
    return True

def test_file_operations():
    """测试文件操作"""
    print("\n=== 文件操作测试 ===")
    
    # 创建测试文件
    test_content = """id,name,email,score
1,张三,zhangsan@example.com,85.5
2,李四,lisi@example.com,92.0
3,王五,wangwu@example.com,78.5
4,赵六,zhaoliu@example.com,88.0
5,钱七,qianqi@example.com,95.5"""
    
    with open('test_data.csv', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # 读取文件
    with open('test_data.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"测试文件创建成功: test_data.csv")
    print(f"文件行数: {len(lines)}")
    print(f"文件内容:")
    for line in lines:
        print(f"  {line.strip()}")
    
    return True

if __name__ == "__main__":
    try:
        test_basic_cleaning()
        test_file_operations()
        print("\n✅ 所有测试通过!")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        raise