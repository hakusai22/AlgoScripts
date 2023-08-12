```bash
    switch和if的区别是， if 之后只能是bool类型， 而switch 可以作用其他类型。 
    但是case 后面的数据必须和变量类型一致。 case 是没有先后顺序的，只要符合条件就会进入。
    case后面的数值 必须是唯一的不能重复。default 不是必须的，根据实际情况来写。
```

```go

//switch语法一
switch 变量名{
    case 数值1: 分支1
    case 数值2: 分支2
    case 数值3: 分支3
    ...
    default:
        最后一个分支
}


//语法二 省略变量 相当于作用在了bool 类型上

switch{
    case true: 分支1
    case false: 分支2
}

//语法三 case 后可以跟随多个数值， 满足其中一个就执行
switch num{
    case 1,2,3:
        fmt.Println("num符合其中某一个 执行代码")
    case 4,5,6:
        fmt.Println("执行此代码")
}

//语法四 可以添加初始化变量 作用于switch内部

switch name:="huangrong"; name{
    case "guojing":
        fmt.Println("shideguojing")
    case "huangrong":
        fmt.Println("shidehuangrong")
} 

```