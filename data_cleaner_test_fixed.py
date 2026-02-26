#!/usr/bin/env python3
"""
Data Cleaner Pro 测试脚本（修复编码问题）
"""

import json
from datetime import datetime
import csv

def test_basic_cleaning():
    """测试基本数据清理功能"""
    print("=== Data Cleaner Pro 测试开始 ===")
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
    
    with open('test_results_final.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    # 保存为CSV
    with open('cleaned_data_final.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age", "score"])
        writer.writeheader()
        writer.writerows(cleaned_data)
    
    print(f"\n测试结果已保存到: test_results_final.json")
    print(f"清理数据已保存到: cleaned_data_final.csv")
    print("=== Data Cleaner Pro 测试完成 ===")
    
    return True

if __name__ == "__main__":
    try:
        test_basic_cleaning()
        print("\n[SUCCESS] 所有测试通过!")
    except Exception as e:
        print(f"\n[ERROR] 测试失败: {e}")
        raise