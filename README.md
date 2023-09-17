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


<img src="https://fastly.jsdelivr.net/gh/hakusai22/Algorithm-study/img.png"/>

![code_language.png](code_language.png)

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

(2) go mod环境变量

```bash
GO111MODULE="on"
GOARCH="arm64"
GOBIN="/usr/local/go/bin"
GOCACHE="/Users/yinpeng/Library/Caches/go-build"
GOENV="/Users/yinpeng/Library/Application Support/go/env"
GOEXE=""
GOEXPERIMENT=""
GOFLAGS=""
GOHOSTARCH="arm64"
GOHOSTOS="darwin"
GOINSECURE=""
GOMODCACHE="/Users/yinpeng/go/pkg/mod"
GONOPROXY=""
GONOSUMDB=""
GOOS="darwin"
GOPATH="/Users/yinpeng/go"
GOPRIVATE=""
GOPROXY="https://goproxy.cn"
GOROOT="/usr/local/go"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/darwin_arm64"
GOVCS=""
GOVERSION="go1.18"
GCCGO="gccgo"
AR="ar"
CC="clang"
CXX="clang++"
CGO_ENABLED="1"
GOMOD="/Users/yinpeng/GoWorkSpace/Go_Python_Study/go.mod"
GOWORK=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -arch arm64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/_z/tcz_9b2s48sf10q0bt80q9r40000gn/T/go-build1770543171=/tmp/go-build -gno-record-gcc-switches -fno-common"
```