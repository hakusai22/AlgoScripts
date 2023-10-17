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

## 项目目录
- [Algorithm](#Algorithm)
  - [Python3/Go算法模版总结](#算法模版总结)
- [Goland_Grammar](#Goland_Grammar)
  - [Go语法](#Go语法)
- [Middleware](#Middleware)
  - [Go中间件](#Go中间件)
- [Python3_Grammar](#Python3_Grammar)
  - [Python3语法](#Python3语法)

## 目录

- [上手指南](#上手指南)
    - [开发前的配置要求](#开发前的配置要求)
    - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [项目特点](#项目特点)
- [功能介绍](#功能介绍)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
    - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)
- [成果演示](#成果演示)

### 上手指南

###### 开发前的配置要求

###### **安装步骤**

### 项目特点

(1) go mod命令
命令 作用

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

- [链表](https://github.com/hakusai22/Go_Python_Study#链表)
- [哈希表](https://github.com/hakusai22/Go_Python_Study#哈希表)
- [字符串](https://github.com/hakusai22/Go_Python_Study#字符串)
- [双指针算法](https://github.com/hakusai22/Go_Python_Study#双指针算法)
- [栈与队列](https://github.com/hakusai22/Go_Python_Study#栈与队列)
- [二叉树](https://github.com/hakusai22/Go_Python_Study#二叉树)
- [回溯](https://github.com/hakusai22/Go_Python_Study#回溯)
- [贪心算法](https://github.com/hakusai22/Go_Python_Study#贪心算法)
- [动态规划](https://github.com/hakusai22/Go_Python_Study#动态规划)
- [二分搜索](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Binary_Search/二分查找.md)
- [前缀和&&差分数组](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Prefix_Sum/前缀和.md)
- [大根堆&&小根堆]()
- [位运算]()

## 链表
- [203. 移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements/) 
- [707. 设计链表](https://leetcode-cn.com/problems/design-linked-list/) 
- [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) 
- [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) 
- [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) 
- [面试题 02.07. 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/) 
- [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) 
- [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/) 

## 哈希表

- [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/) 
- [383. 赎金信](https://leetcode-cn.com/problems/ransom-note/) 
- [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)
- [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/) 
- [349. 两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays/) 
- [350. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/) 
- [202. 快乐数](https://leetcode-cn.com/problems/happy-number/) 
- [1. 两数之和](https://leetcode-cn.com/problems/two-sum/) 
- [454. 四数相加 II](https://leetcode-cn.com/problems/4sum-ii/) 
- [15. 三数之和](https://leetcode-cn.com/problems/3sum/) 
- [18. 四数之和](https://leetcode-cn.com/problems/4sum/) 

## 双指针算法

- [27. 移除元素](https://leetcode-cn.com/problems/remove-element/) 
- [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) 
- [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/) 
- [844. 比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/) 
- [977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/) 
- [344. 反转字符串](https://leetcode-cn.com/problems/reverse-string/) 
- [剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/) 
- [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/) 
- [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/) 
- [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) 
- [面试题 02.07. 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/) 
- [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) 
- [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
- [15. 三数之和](https://leetcode-cn.com/problems/3sum/) 
- [18. 四数之和](https://leetcode-cn.com/problems/4sum/) 

## 栈与队列

- [232. 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/) 
- [225. 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/) 
- [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/) 
- [1047. 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/) 
- [150. 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/) 
- [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) 
- [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) 

## 二叉树

### 遍历二叉树

- [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
- [589. N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)
- [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
- [590. N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
- [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
- [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
- [107. 二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)
- [429. N 叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)
- [199. 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/)
- [637. 二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/)
- [515. 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)
- [116. 填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)
- [117. 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

### 求二叉树的属性

- [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
- [559. N 叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/)
- [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
- [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
- [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/)
- [100. 相同的树](https://leetcode-cn.com/problems/same-tree/)
- [572. 另一棵树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree/)
- [222. 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/)
- [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)
- [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)
- [404. 左叶子之和](https://leetcode-cn.com/problems/sum-of-left-leaves/)
- [513. 找树左下角的值](https://leetcode-cn.com/problems/find-bottom-left-tree-value/)
- [112. 路径总和](https://leetcode-cn.com/problems/path-sum/)

### 二叉树的修改与构造

- [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. 从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
- [654. 最大二叉树](https://leetcode-cn.com/problems/maximum-binary-tree/)
- [617. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)
### 求二叉搜索树的属性

- [700. 二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/)
- [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
- [530. 二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)
- [501. 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)
- [538. 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)

### 二叉树公共祖先问题

- [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [235. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

### 二叉搜索树的修改与构造

- [701. 二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)
- [450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/)
- [669. 修剪二叉搜索树](https://leetcode-cn.com/problems/trim-a-binary-search-tree/)
- [108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

## 回溯

### 组合问题

- [77. 组合](https://leetcode-cn.com/problems/combinations/)
- [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)
- [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
- [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/)
- [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)

### 分割问题

- [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/)
- [93. 复原 IP 地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

### 子集问题

- [78. 子集](https://leetcode-cn.com/problems/subsets/)
- [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)
- [491. 递增子序列](https://leetcode-cn.com/problems/increasing-subsequences/)

### 排列问题

- [46. 全排列](https://leetcode-cn.com/problems/permutations/)
- [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

### 棋盘问题

- [51. N 皇后](https://leetcode-cn.com/problems/n-queens/)
- [52. N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/)
- [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/)

### 其他

- [332. 重新安排行程](https://leetcode-cn.com/problems/reconstruct-itinerary/)
## 贪心算法

### 简单贪心

- [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/)
- [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
- [1005. K 次取反后最大化的数组和](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/)
- [860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)

### 中等贪心

- [376. 摆动序列](https://leetcode-cn.com/problems/wiggle-subsequence/)
- [738. 单调递增的数字](https://leetcode-cn.com/problems/monotone-increasing-digits/)

### 股票问题

- [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

### 两个维护度权衡问题

- [135. 分发糖果](https://leetcode-cn.com/problems/candy/)
- [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)

### 区间问题

- [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)
- [45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)
- [452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)
- [435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)
- [763. 划分字母区间](https://leetcode-cn.com/problems/partition-labels/)
- [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)


## 动态规划

### 动态规划基础

- [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/) 
- [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/) 
- [746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/) 
- [62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)
- [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)
- [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)
- [96. 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/)

### 背包问题

- [416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
- [1049. 最后一块石头的重量 II](https://leetcode-cn.com/problems/last-stone-weight-ii/)
- [494. 目标和](https://leetcode-cn.com/problems/target-sum/)
- [474. 一和零](https://leetcode-cn.com/problems/ones-and-zeroes/)
- [518. 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)
- [377. 组合总和 Ⅳ](https://leetcode-cn.com/problems/combination-sum-iv/)
- [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)
- [279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/)
- [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)
### 打家劫舍系列问题

- [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)
- [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)
- [337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)

### 股票系列问题

- [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
- [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
- [188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)
- [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

### 子序列系列问题

- [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
- [674. 最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/)
- [718. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)
- [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
- [1035. 不相交的线](https://leetcode-cn.com/problems/uncrossed-lines/)
- [53. 最大子数组和](https://leetcode-cn.com/problems/maximum-subarray/)
- [392. 判断子序列](https://leetcode-cn.com/problems/is-subsequence/)
- [115. 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)
- [583. 两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)
- [72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)
- [647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)
- [516. 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)
- [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

## 单调栈

- [739. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/)
- [496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/)
- [503. 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/)
- [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)
- [84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

## 滑动窗口问题

- [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
- [918. 环形子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-circular-subarray/)
- [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
- [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)
- [209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)
- [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)
- [904. 水果成篮](https://leetcode-cn.com/problems/fruit-into-baskets/)
