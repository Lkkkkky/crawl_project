'''
=========================================================    
       @File     : 类目映射.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/17 14:40
       @Desc     : 
=========================================================   
'''
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# 读取 TikTok 类目和自己平台的类目数据
tiktok_file = 'tiktok类目.xlsx'  # TikTok 类目表文件路径
platform_file = '西之月类目.xlsx'  # 自己平台类目表文件路径

# 读取 Excel 文件
tiktok_df = pd.read_excel(tiktok_file)
platform_df = pd.read_excel(platform_file)

# 假设 TikTok 类目表中有 '类目名称', '类目ID' 和 '类目节点' 列
# 假设自己平台类目表中有 '类目名称' 列，我们将根据此列进行模糊匹配

# 为平台类目表添加两列 'TikTok 类目ID' 和 'TikTok 类目节点'，用于保存匹配结果
platform_df['TikTok 类目ID'] = None
platform_df['TikTok 类目节点'] = None

# 遍历平台类目表中的每一行，进行模糊匹配
for idx, row in platform_df.iterrows():
    platform_category = row['分类CN']
    platform_category_node = row['分类节点-cn']

    # 使用 fuzzywuzzy 进行模糊匹配，找到 TikTok 类目表中最接近的类目名称和分类节点
    best_match_category = process.extractOne(platform_category, tiktok_df['分类cn'], scorer=fuzz.partial_ratio)
    best_match_node = process.extractOne(platform_category_node, tiktok_df['分类节点cn'], scorer=fuzz.partial_ratio)

    # 如果匹配度较高，则填充 TikTok 类目ID 和 类目节点
    if best_match_category and best_match_category[1] >= 80:  # 80 是匹配度阈值，可以调整
        matched_category = best_match_category[0]
        matched_row = tiktok_df[tiktok_df['分类cn'] == matched_category].iloc[0]
        platform_df.at[idx, 'TikTok 类目ID'] = matched_row['分类ID']
        platform_df.at[idx, 'TikTok 类目节点'] = matched_row['分类节点cn']

    # 如果分类节点也匹配得较好，则更新分类节点信息
    if best_match_node and best_match_node[1] >= 80:  # 同样的阈值调整
        matched_node = best_match_node[0]
        platform_df.at[idx, 'TikTok 类目节点'] = matched_node
# 保存更新后的平台类目表
output_file_path = 'mapped_platform_categories.xlsx'
platform_df.to_excel(output_file_path, index=False)

# 返回文件路径
output_file_path
