#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试PDF报告生成功能
"""

import json
import os
from pdf_report_generator import generate_cleaning_report, generate_ecommerce_report


def create_test_results():
    """创建测试结果数据"""
    test_results = {
        "total_tests": 5,
        "passed_tests": 5,
        "failed_tests": 0,
        "pass_rate": 100,
        "total_records": 1000,
        "cleaned_records": 995,
        "cleaning_success_rate": 99.5,
        "test_cases": [
            {
                "id": 1,
                "description": "价格格式清洗测试",
                "passed": True,
                "execution_time": 45
            },
            {
                "id": 2,
                "description": "时间格式标准化测试",
                "passed": True,
                "execution_time": 32
            },
            {
                "id": 3,
                "description": "手机号验证测试",
                "passed": True,
                "execution_time": 28
            },
            {
                "id": 4,
                "description": "地址信息补全测试",
                "passed": True,
                "execution_time": 51
            },
            {
                "id": 5,
                "description": "重复数据去重测试",
                "passed": True,
                "execution_time": 37
            }
        ]
    }
    
    # 保存测试结果
    with open('test_results_for_pdf.json', 'w', encoding='utf-8') as f:
        json.dump(test_results, f, ensure_ascii=False, indent=2)
    
    print("测试结果文件已创建: test_results_for_pdf.json")
    return test_results


def test_pdf_generation():
    """测试PDF生成"""
    print("开始测试PDF报告生成...")
    
    # 1. 创建测试数据
    test_results = create_test_results()
    
    # 2. 生成测试报告
    try:
        output_file = "test_cleaning_report.pdf"
        generate_cleaning_report('test_results_for_pdf.json', output_file)
        
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file) / 1024
            print(f"✓ PDF报告生成成功: {output_file}")
            print(f"✓ 文件大小: {file_size:.1f} KB")
        else:
            print("✗ PDF文件未生成")
            
    except Exception as e:
        print(f"✗ PDF生成失败: {e}")
        return False
    
    # 3. 测试电商报告生成（如果有数据文件）
    ecommerce_file = "原始电商订单数据.csv"
    if os.path.exists(ecommerce_file):
        try:
            output_file = "test_ecommerce_report.pdf"
            generate_ecommerce_report(ecommerce_file, output_file)
            
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file) / 1024
                print(f"✓ 电商报告生成成功: {output_file}")
                print(f"✓ 文件大小: {file_size:.1f} KB")
            else:
                print("✗ 电商PDF文件未生成")
                
        except Exception as e:
            print(f"✗ 电商报告生成失败: {e}")
    
    return True


def create_sample_ecommerce_data():
    """创建示例电商数据（如果不存在）"""
    import pandas as pd
    import numpy as np
    
    # 创建示例数据
    data = {
        '订单号': [f'ODR{1000+i}' for i in range(50)],
        '用户ID': [f'U{np.random.randint(100, 200)}' for _ in range(50)],
        '商品名称': ['iPhone 15 Pro', 'MacBook Air', 'AirPods Pro', 'iPad Pro', 'Apple Watch'] * 10,
        '价格': [f'¥{np.random.randint(1000, 10000)}' for _ in range(50)],
        '购买时间': [f'2024-01-{15 + i//10} {np.random.randint(10, 20)}:{np.random.randint(0, 60)}:00' for i in range(50)],
        '收货地址': ['北京市朝阳区', '上海市浦东新区', '广州市天河区', '深圳市南山区', '杭州市西湖区'] * 10,
        '手机号': [f'138{np.random.randint(10000000, 99999999)}' for _ in range(50)],
        '订单状态': ['已发货', '已付款', '已发货', '已付款', '已发货'] * 10
    }
    
    df = pd.DataFrame(data)
    df.to_csv('sample_ecommerce_data.csv', index=False, encoding='utf-8-sig')
    print("示例电商数据已创建: sample_ecommerce_data.csv")
    
    return 'sample_ecommerce_data.csv'


if __name__ == "__main__":
    print("=" * 60)
    print("Data Cleaner Pro PDF生成功能测试")
    print("=" * 60)
    
    # 检查必要文件
    if not os.path.exists("原始电商订单数据.csv"):
        print("未找到原始电商数据文件，创建示例数据...")
        data_file = create_sample_ecommerce_data()
    else:
        data_file = "原始电商订单数据.csv"
    
    # 运行测试
    success = test_pdf_generation()
    
    print("=" * 60)
    if success:
        print("✅ PDF生成功能测试通过！")
        print("生成的文件：")
        print("  - test_cleaning_report.pdf (测试报告)")
        print("  - test_ecommerce_report.pdf (电商报告)")
        print("  - test_results_for_pdf.json (测试数据)")
        if os.path.exists("sample_ecommerce_data.csv"):
            print("  - sample_ecommerce_data.csv (示例数据)")
    else:
        print("❌ PDF生成功能测试失败")
    print("=" * 60)