/**
 * @Time 2024/09/08 13:47
 * @Author  : https://github.com/hakusai22
 */

/*
    TypeScript是由微软开发维护的JavaScript的超集，它在JavaScript的基础之上添加了静态类型的支持。
    这意味着TypeScript可以在编译时发现并报告类型错误，而不是在运行时才发现。

    typeScript 的优点
        1.类型安全：TS的类型系统可以帮助开发者在编码阶段就发现并修复潜在的错误,提高代码的可靠性和稳定性。
        2.更好的tooling支持：TS提供了更好的IDE支持，如代码补全、重构、跳转定义等功能，提高了开发效率。
        3.更好的可维护性：TS的类型声明使得代码的结构和意图更加清晰，增强了可读性和可维护性，特别是在团队协作和大型项目中非常有优势。
 */

// https://juejin.cn/post/7358352353294106664
export {}
// 类型注解
// 一、基本类型
let age: number = 18
let name: string = 'Andy'
let num: undefined = undefined
let isVal: boolean = true

// 二、数组类型
let arr: number[] = [1, 3, 5]
let arr2: Array<string> = ['1', '2']

// 三、联合类型
let str: (number | string | boolean)[] = ['1', 2, false]
let str1: number | string[] = 3

// 四、类型别名    type 用来定义该变量是存放类型的
type ArrType = number | string | boolean | null | undefined
let a: ArrType[] = ['1', 2, false]

// 五、函数类型
// 法1
function add(num1: number, num2: number): string {
    return String(num1 + num2)
}

// 法2
type addFn = (num1: number, num2: number) => string // 该方法只使用于函数表达式
const add2: addFn = (num1, num2) => {
    return String(num1 + num2)
}

// 六、void类型
const sayHello = () => {
}
const sayHi = (): void => {
}
/*
  注意：

在 JS 中，如果没有返回值，默认返回的是 undefined。
在 TS 中，函数不写返回值，返回类型为void。
void 和 undefined 在 TypeScript 中并不是一回事
如果指定返回值类型是 undefined 那返回值必须是 undefined
*/
const s = (): undefined => {
    return undefined
}

// 七、可选参数
// 使用 ? 表示该参数是可选的，可传可不传。可选参数要放到必选的后面
// 因为函数接参的时候是根据传来数据的顺序来的，若第一个参数是可选的，那传一个值过来，这个值，是那个形参来接呢？
const aaa = (a: number, b?: number) => {
    return b && a + b
}

aaa(9)
aaa(1, 3)

// 八、对象类型
// 对象中方法返回值的类型声明 方法名:()=>返回类型 或者 方法名():返回类型
let person: {} = {}

let person1: { name: string; sayHi: () => void } = {
    name: 'Tom',
    sayHi() {
    },
}

let person2: {
    name: string
    sayHi(): void
} = {
    name: 'jack',
    sayHi() {
    },
}

// 九、接口    只能用来声明对象类型
interface People {
    name: string
    age: number
    sayHi: () => void
}

let persons: People = {
    name: 'jack',
    age: 19,
    sayHi() {
    },
}

// 接口继承   extends
interface Point2D {
    x: number
    y: number
}

interface Point3D extends Point2D {
    z: number
}

let point: Point3D = {
    x: 0,
    y: 0,
    z: 0,
}

// 交叉类型    & 也可以实现接口继承
type TPoint2D = {
    x: number
    y: number
}

type TPoint3D = TPoint2D & {
    z: number
}

let tpoint: TPoint3D = {
    x: 0,
    y: 0,
    z: 0,
}

// interface 和 type 的区别
// 相同点：都可以定义对象的类型，都可以继承
// 不同点：重复定义，interface会合并，type会报错

// 十、类型推断

// 1.更加变量定义的初始值来自动加上类型
let ab = 123
// ab = '123'

// 2.根据函数变量计算后的类型来推断
let func = (n1: number, n2: number) => {
    return n1 + n2
}

// 十一、字面量类型
let car: '汽车'
car = '汽车'

let fruit = 'apple' // 类型推断
const tree = '柳树' // const 声明的变量值不能改变，所以类型只能是它的值

// 十二、any类型    TS会忽略类型检查
// 隐式any的情况：声明变量不给类型或初始值，函数参数不给类型或初始值
let obj4: any = {
    age: 18,
}
obj4.bar = '123'
obj4 = '123'
obj4()

// 十三、类型断言 as 指定更具体的类型
const aLink = document.getElementById('link') as HTMLAnchorElement

// 十四、泛型    在变量名称的后面添加  <类型> 类似于参数的作用
// 1.泛型别名
type User = {
    name: string
    age: number
}
type Data<T> = {
    msg: string
    code: number
    data: T
}
type UserData = Data<User>
const data1: UserData = {
    msg: '请求成功',
    code: 200,
    data: {
        name: 'Tom',
        age: 18,
    },
}

// 2.泛型接口
interface Idfn<T> {
    id: () => T
    ids: () => T[]
}

const change: Idfn<string> = {
    id: () => '123',
    ids: () => ['1', '2', '3'],
}

// 3.泛型函数
const fn5 = <T>(a: T): T => {
    return a
}

const num0 = fn5<number>(1)

// 十五、枚举类型
/**
 * 语法：enum 枚举名 { key1, key2 }
 * 作用：给变量当作类型和值使用
 * 场景：解决数字字面量类型可读性差，同时可以存值
 * 注意：枚举类型只能在ts格式中存在，打包后该类型任存在于代码中
 */

// 问题：后台的数字型数据，可读性差
// 0 女 | 1 男
// type Sex = 0 | 1
// const sex: Sex = 1

// 不指定枚举属性的值，默认第一个属性的值为0，往后依次加一
enum Sex {
    '女' = 1,
    '男'
}

const sex: Sex = Sex.男


// 补充

// 1. TS中，当对象中的属性值不确定时
interface myObj {
    // 属性名不确定，类型可以为 number 或 string
    [key: number | string]: number
}

let myTestObj: myObj = {
    1: 1,
    age: 18
}

// https://juejin.cn/post/7379060488351989770?searchId=20240908145340DBDD8B0CAD4F3EB2B797
// 数组
let numbers: number[] = [1, 2, 3, 4, 5, 6]
let strings: Array<string> = ["one", "two", "three"]

// 联合类型
let numbers2: (number | string)[] = ["zero", 1, 2, 3, 4]
let strings2: Array<string | number> = ["one", "two", "three", 4];
let arr222: any = ["one", "two", "three", 4, true,];

//元祖
let person111: [string, number] = ["hakusai", 30]
person = ["John", "thirty"]; // 报错：不能将类型"[string，string]"分配给类型"[string，number]"
person = ["John"]; // 报错：不能将类型"[string]"分配给类型"[string，number]”。源具有1个元素，但目标需要2个

// 枚举
enum Direction {
    Up,
    Down,
    Left,
    Right
}

let move: Direction = Direction.Up;

// 函数
// 必需参数：默认情况下，TypeScript 中的函数参数都是必需的
// 可选参数：在参数名的末尾使用 ? 标记，则可设置为可选参数
// 剩余参数：在最后一个参数的参数名前使用 ... 以定义不定数量的参数
function greet(name: string, greeting?: string): string {
    return greeting ? `${greeting}, ${name}` : `Hello, ${name}`;
}

console.log(greet('John', 'Good morning')); // Good morning, John
console.log(greet('John')); // Hello, John

function sum(...numbers: number[]): number {
    return numbers.reduce((acc, curr) => acc + curr, 0);
}


// 返回值
function sayHello2(): void {
    console.log("Hello!");
}

function multiply(a: number, b: number): number {
    return a * b;
}

//接口
// 接口（Interface） 是一种用于定义对象结构的方式，类似于结构体。它描述了对象的属性和方法，但不包含具体的实现。

interface Person {
    name: string;
    age: number;

    greet(): string;
}

let john: Person = {
    name: "John",
    age: 25,
    greet: () => "Hello!"
};

// 接口还可以使用 extends 关键字 扩展（extend） 其他接口：
interface Employee extends Person {
    employeeId: number;
}

let jane: Employee = {
    name: "Jane",
    age: 30,
    employeeId: 123,
    greet: () => "Hi!"
};


// 类型别名
// 使用 type 关键字定义，可以为任何类型创建一个新名称。类型别名可以用于基础类型、联合类型、元组等
type StringOrNumber = string | number;

let value: StringOrNumber;
value = "Hello"; // 正确
value = 123;     // 也正确

// 类型别名也可以用于对象类型，达成和接口类似的效果
type Point = {
    x: number;
    y: number;
};

let point22: Point = { x: 10, y: 20 };

// 泛型
function identity<T>(arg1: T, arg2: T): T {
    return arg1;
}

let output1 = identity<string>("Hello", "world!");
let output2 = identity<number>(123, 321);

// 不仅在函数中，泛型也可以应用于接口和类：
interface Box<T> {
    contents: T;
}

let stringBox: Box<string> = { contents: "Hello" };
let numberBox: Box<number> = { contents: 123 };

class GenericNumber<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = (x, y) => x + y;



