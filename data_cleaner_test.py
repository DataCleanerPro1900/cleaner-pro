#!/usr/bin/env python3
"""
Data Cleaner Pro 测试脚本
模拟数据清理功能测试
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json

def test_data_cleaning():
    """测试数据清理功能"""
    print("=== Data Cleaner Pro 测试开始 ===")
    print(f"测试时间: {datetime.now()}")
    
    # 创建测试数据
    data = {
        '姓名': ['张三', '李四', '王五', None, '赵六'],
        '年龄': [25, 30, None, 35, 40],
        '邮箱': ['zhangsan@example.com', 'lisi@example.com', 'wangwu@example.com', 'zhaoliu@example.com', None],
        '分数': [85.5, 92.0, 78.5, 88.0, 95.5]
    }
    
    df = pd.DataFrame(data)
    print(f"\n原始数据:\n{df}")
    
    # 数据清理操作
    print("\n=== 执行数据清理 ===")
    
    # 1. 处理缺失值
    df_cleaned = df.copy()
    df_cleaned['姓名'] = df_cleaned['姓名'].fillna('未知')
    df_cleaned['年龄'] = df_cleaned['年龄'].fillna(df_cleaned['年龄'].mean())
    df_cleaned['邮箱'] = df_cleaned['邮箱'].fillna('无邮箱')
    
    print(f"清理后数据:\n{df_cleaned}")
    
    # 2. 数据统计
    stats = {
        '总记录数': len(df_cleaned),
        '平均年龄': df_cleaned['年龄'].mean(),
        '平均分数': df_cleaned['分数'].mean(),
        '最高分数': df_cleaned['分数'].max(),
        '最低分数': df_cleaned['分数'].min()
    }
    
    print(f"\n=== 数据统计 ===")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # 3. 保存测试结果
    result = {
        '测试时间': str(datetime.now()),
        '测试状态': '成功',
        '清理记录数': len(df_cleaned),
        '统计数据': stats
    }
    
    with open('test_results.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n测试结果已保存到: test_results.json")
    print("=== Data Cleaner Pro 测试完成 ===")
    
    return True

def test_performance():
    """测试性能"""
    print("\n=== 性能测试 ===")
    
    # 创建大数据集
    n = 10000
    big_data = {
        f'列{i}': np.random.randn(n) for i in range(5)
    }
    
    df_big = pd.DataFrame(big_data)
    start_time = datetime.now()
    
    # 执行一些操作
    df_big_cleaned = df_big.fillna(0)
    mean_values = df_big_cleaned.mean()
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print(f"处理 {n} 行数据耗时: {duration:.3f} 秒")
    print(f"平均每列均值: {mean_values.mean():.4f}")
    
    return duration

if __name__ == "__main__":
    try:
        test_data_cleaning()
        test_performance()
        print("\n✅ 所有测试通过!")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        raise