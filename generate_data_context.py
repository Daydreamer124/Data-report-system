#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storyteller.algorithm.utils.DatasetContextGenerator import DatasetContextGenerator
import json
import os

def run_data_context_generation(api_key, base_url, csv_file, output_file, dataset_name="", dataset_description="", n_samples=5):
    """
    运行数据集上下文生成
    
    Args:
        api_key: OpenAI API Key
        base_url: OpenAI API的基础URL
        csv_file: CSV文件路径
        output_file: 输出JSON文件路径
        dataset_name: 数据集名称（默认使用文件名）
        dataset_description: 数据集描述（默认由LLM生成）
        n_samples: 用于分析的样本数量
    
    Returns:
        dict: 生成的数据集上下文信息
    """
    try:
        # 初始化数据集上下文生成器
        generator = DatasetContextGenerator(api_key=api_key, base_url=base_url)
        
        # 生成数据集上下文
        print(f"正在处理文件: {csv_file}")
        dataset_context = generator.generate_context(
            data=csv_file,
            dataset_name=dataset_name,
            dataset_description=dataset_description,
            n_samples=n_samples
        )
        
        # 保存结果到文件
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(dataset_context, f, indent=2, ensure_ascii=False)
            print(f"结果已保存到 {output_file}")

        # 打印部分关键信息
        print("\n数据集信息摘要:")
        print(f"数据集名称: {dataset_context['name']}")
        print(f"总行数: {dataset_context['total_rows']}")
        print(f"总列数: {dataset_context['total_columns']}")
        print(f"\n数据集描述: {dataset_context['dataset_description']}")
        
        return dataset_context
        
    except Exception as e:
        print(f"错误: {str(e)}")
        import traceback
        print(traceback.format_exc())
        raise

if __name__ == "__main__":
    # 直接运行数据上下文生成，无需命令行参数
    print("=" * 60)
    print("🚀 数据集上下文生成程序")
    print("=" * 60)
    
    # 预设的生成参数（您可以根据需要修改这些参数）
    API_KEY = "sk-N3NMJtA44V4Qu5NhB18cE97331734788Bc18A77b8fC1DaD6"  # 请替换为您的实际API密钥
    BASE_URL = "https://svip.yi-zhan.top/v1"
    CSV_FILE = "/Users/zhangzhiyang/mcts/storyteller/dataset/insurance.csv"
    OUTPUT_FILE = "insurance.json"
    DATASET_NAME = ""  # 留空将使用文件名
    DATASET_DESCRIPTION = ""  # 留空将由LLM自动生成
    N_SAMPLES = 5
    
    try:
        # 直接调用run_data_context_generation函数
        results = run_data_context_generation(
            api_key=API_KEY,
            base_url=BASE_URL,
            csv_file=CSV_FILE,
            output_file=OUTPUT_FILE,
            dataset_name=DATASET_NAME,
            dataset_description=DATASET_DESCRIPTION,
            n_samples=N_SAMPLES
        )
        
        print("\n" + "=" * 60)
        print("🎉 数据上下文生成成功完成！")
        print("=" * 60)
        print(f"📊 数据集名称: {results['name']}")
        print(f"📁 结果已保存到: {OUTPUT_FILE}")
        print(f"📄 总行数: {results['total_rows']}")
        print(f"📄 总列数: {results['total_columns']}")
        
    except Exception as e:
        print(f"\n❌ 生成过程中发生错误: {e}")
        print("\n💡 请检查:")
        print("1. API_KEY是否设置正确")
        print("2. CSV文件路径是否正确")
        print("3. 网络连接是否正常")
        print("4. API服务是否可用")
        import sys
        sys.exit(1) 