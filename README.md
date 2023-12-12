# Go_Python_Study

Go_Python_Study 学习记录

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
![GitHub top language](https://img.shields.io/github/languages/top/hakusai22/Go_Python_Study?style=for-the-badge)

<!-- PROJECT LOGO -->
<br />



<p align="center">
    <a href="https://github.com/hakusai22/Go_Python_Study/">
    </a>
    <h3 align="center">Go_Python 算法学习笔记 🔞</h3>
  <p align="center">
    ·
    <a href="https://github.com/hakusai22/Go_Python_Study/issues">报告Bug</a>
    ·
    <a href="https://github.com/hakusai22/Go_Python_Study/issues">提出新特性</a>
  </p>


<img src="https://fastly.jsdelivr.net/gh/hakusai22/Go_Python_Study/al.png"/>
<img src="https://fastly.jsdelivr.net/gh/hakusai22/Go_Python_Study/code_language.png"/>

<!-- links -->

[your-project-path]:hakusai22/Go_Python_Study

[contributors-shield]: https://img.shields.io/github/contributors/hakusai22/Go_Python_Study.svg?style=for-the-badge

[contributors-url]: https://github.com/hakusai22/Go_Python_Study/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/hakusai22/Go_Python_Study.svg?style=for-the-badge

[forks-url]: https://github.com/hakusai22/Go_Python_Study/network/members

[stars-shield]: https://img.shields.io/github/stars/hakusai22/Go_Python_Study.svg?style=for-the-badge

[stars-url]: https://github.com/hakusai22/Go_Python_Study/stargazers

[issues-shield]: https://img.shields.io/github/issues/hakusai22/Go_Python_Study.svg?style=for-the-badge

[issues-url]: https://img.shields.io/github/issues/hakusai22/Go_Python_Study.svg

[license-shield]: https://img.shields.io/github/license/hakusai22/Go_Python_Study.svg?style=for-the-badge

[license-url]: https://github.com/hakusai22/Go_Python_Study/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/xxxx


## [Python3 刷题总结](./Python3_README.md)
## [GO 刷题总结](./Go_README.md)

## 分类型刷题

### 算法复杂度讲解 
![img_1.png](img_1.png)
![img_2.png](img_2.png)
- https://zhuanlan.zhihu.com/p/248284657
- https://pegasuswang.github.io/python_data_structures_and_algorithms/06_%E7%AE%97%E6%B3%95%E5%88%86%E6%9E%90/big_o/
- logN 计算
```python
import math
print(math.log2(10 ** 5)) # 16.609640474436812
```

## 高级数据结构总结
https://www.yuque.com/hakusai/gyb5dn/ntylqxpxvl7hxvgx

## Go 项目编译运行命令
```bash
go mod init	生成 go.mod 文件
go mod download	下载 go.mod 文件中指明的所有依赖
go mod tidy	整理现有的依赖
go mod graph	查看现有的依赖结构
go mod edit	编辑 go.mod 文件
go mod vendor	导出项目所有的依赖到vendor目录
go mod verify	校验一个模块是否被篡改过
go mod why	查看为什么需要依赖某模块
```

## Python3 项目编译运行命令
```bash
pip3 freeze > requirements.txt   

pip3  install -r requirements.txt
```