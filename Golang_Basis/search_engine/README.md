# search-engine-demo

原始搜索数据可以使用悟空数据源 https://wukong-dataset.github.io/wukong-dataset/download.html

实现步骤

1. 数据准备
2. 文档分词构建倒排索引
3. 关键字分词搜索 (基于gse)
4. 排名算法 (基于TF-IDF)
5. 返回最终结果

https://github.com/go-ego/gse 分词使用的库

// todo
- 倒排表压缩算法实现
- 文本相关性排名算法 BM25 实现
- 搜索结果过滤 
- 添加/删除 倒排索引数据修改
- 搜索多条件匹配
- 搜索词纠错 自动填充