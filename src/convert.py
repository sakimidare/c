import re
import os
from pathlib import Path

def process_markdown_content(text):
    """
    # --- 1. 微观处理：中英文空格 & 行内代码空格 ---
    # 汉字与英文/数字
    text = re.sub(r'([\u4e00-\u9fa5])([a-zA-Z0-9])', r'\1 \2', text)
    text = re.sub(r'([a-zA-Z0-9])([\u4e00-\u9fa5])', r'\1 \2', text)
    # 反引号与正文
    text = re.sub(r'([^\s`])(`[^`\n]+`)', r'\1 \2', text)
    text = re.sub(r'(`[^`\n]+`)([^\s`])', r'\1 \2', text)
"""
    lines = text.split('\n')
    new_lines = []
    in_code_block = False

    # --- 2. 宏观处理：强制每行上下空行 ---
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # A. 处理代码块 (```) - 内部不换行
        if stripped.startswith('```'):
            if not in_code_block: 
                new_lines.append("") # 代码块前加空行
                new_lines.append(line)
                in_code_block = True
            else: 
                new_lines.append(line)
                new_lines.append("") # 代码块后加空行
                in_code_block = False
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        # B. 处理表格 (|) - 内部不换行
        if stripped.startswith('|'):
            # 如果是表格起始行
            if i > 0 and not lines[i-1].strip().startswith('|'):
                new_lines.append("")
            new_lines.append(line)
            # 如果是表格结束行
            if i < len(lines)-1 and not lines[i+1].strip().startswith('|'):
                new_lines.append("")
            continue

        # C. 处理普通行（包括列表 * 、数字列表、普通正文）
        if stripped == "":
            new_lines.append("")
        else:
            # 在每一行非空行前后都尝试加空行
            new_lines.append("")
            new_lines.append(line)
            new_lines.append("")

    # --- 3. 收尾：统一清理 ---
    # 将多个连续换行符压缩为两个（即一个可见空行）
    result = '\n'.join(new_lines)
    # 移除行尾多余空格
    result = re.sub(r'[ \t]+\n', '\n', result)
    # 核心：将 2 个以上的连续换行替换为 2 个
    result = re.sub(r'\n{2,}', '\n\n', result)
    
    return result.strip() + '\n'

def batch_process(target_dir):
    target_path = Path(target_dir)
    count = 0
    for md_file in target_path.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            formatted = process_markdown_content(content)
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(formatted)
            print(f"成功处理: {md_file}")
            count += 1
        except Exception as e:
            print(f"处理失败 {md_file}: {e}")
    print(f"\n✨ 批量处理完成！共处理 {count} 个文件。")

if __name__ == "__main__":
    # 将 '.' 改为你实际的文件夹路径
    batch_process('.')
