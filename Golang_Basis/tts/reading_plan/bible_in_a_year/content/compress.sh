#!/bin/bash

# 定义输入目录和输出目录
input_dir="./"    # 当前目录
output_dir="./compressed"

# 如果输出目录不存在，创建它
mkdir -p "$output_dir"

# 遍历目录中的每一个 MP3 文件
for file in "$input_dir"*.mp3; do
    # 获取文件名，不包括路径和扩展名
    filename=$(basename "$file")

    # 压缩并输出到新的文件夹
    ffmpeg -i "$file" -b:a 64k "$output_dir/$filename"

    echo "Compressed: $filename"
done

echo "All MP3 files have been compressed."
