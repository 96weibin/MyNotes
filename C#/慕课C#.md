# C# Node


- console 程序执行 生成exe, dll, pdb 等  在bin/debug/net5.0下
- using 命名空间 获取变量  system

## Console

- system上的类 方法如下 

    方法 | 作用
    -|-
    Write | 行内写
    writeLine | 新行写
    Read | 读一个字符
    ReadLine | 读直至Enter
    ReadKay | 读一个按键 返回对象
    Clear | 清屏

## 变量与数据类型

1. 基本类型

    变量 | 声明
    -|-
    整数 | int < lang
    小数 | float < dbuble < decimal
    char | 'a'
    bool | true false



### 字符串

- string 和 String 一样没有区别只是别名

- 声明字符串

    ```c#
        string name = "weibin";
        int age = 18;
        string msg = $"my name is {name}, I'm {age} years old";  //内嵌字符串
        string msg2 = "my name is " + name + ", I'm " + age + " years old"; //js 写法 也可以
        string msg3 = @"ss
        fs
        sfsfsf";  //保留格式  原意字符串
        Console.WriteLine(msg);         
        Console.WriteLine(msg2);
        Console.WriteLine(msg3);
    ```


## 方法

- 方法签名 与ts类似， 支持箭头

    ```C# 
    // 访问修饰符 声明修饰符 返回类型 名称 (参数) {函数体}
    public static void main(string[] args){ }
    ```

- 传参 ref out 

    ```c#
    public static void Main(String[] args)
    {

        int a = 0;
        addOne(ref a);      //参数传递  实参需要赋值
        Console.WriteLine(a);   //1


        int b;  
        ToFive(out b);      //输出传参 的实参  可以不赋值
        Console.WriteLine(b);   //5

    }

    private static void ToFive(out int num) //输出传参
    {
        num = 5;    //
    }

    private static void addOne(ref int a)   //引用地址传递 
    {
        a += 1;     //这里不是声明的 而是  同一个a
    }
    ```

## 面向对象

### 对象与内存管理

1. 内存生命周期

    1. 分配内存
    2. 读写内存
    3. 释放内存

2. 内存分区

    1. 栈区： 由编译器自动分配， 存放 值类型，对象索引等，
    2. 堆区： 动态存储区， 存放 对象本身，由垃圾回收机制（GC）管理
    3. 静态区，常量区： static 和 const 的变量， 程序运行结束才释放 ∴限制使用 降低负荷
    4. 代码区： 存放函数体 二进制代码

3. 堆栈
    1. 栈： 内存大小确定，编译时分配内存空间， 不受GC管理，用完即释放
    2. 堆： 内存大小不确定， 运行时动态分配空间， 受GC管理
    - 对象的索引 存储在栈， 实体存储在堆

### class

- 高内聚 低耦合, 尽量对象会用的方法  放到对象内,  

    ```c#
    public static void Main(string[] args)
    {
        var a = new Point(1, 2);
        a.drawPoint();
        var b = new Point(10,20);
        a.dragLine(b);
    }

    public class Point
    {
        private int x;   //成员变量
        private int y;
        public Point() //构造函数
        {
            x = 0;
            y = 0;
        }
        public Point(int x, int y)  //构造函数 带形参
        {
            this.x = x;     //this 调用成员变量
            this.y = y;
        }
        public void drawPoint() //成员方法
        {
            Console.WriteLine($"x is {x} and y is {y}"); //成员变量可以直接使用不用this
        }
        public void dragLine(Point d)
        {
            Console.WriteLine($"from {x}, {y} to {d.x}, {d.y}");
        }
    }
    ```

1. 访问修饰符

    修饰符 | 功能
    -|-
    public | 类外可以访问
    private | 只能类内访问
    protected | 类内和子集可以访问
    internal | 仅类库项目内可访问
    protected internal | 

    - 创建class Library: add > new project > class library
    - 创建关联 ： add > project reference
    - using : using 类库之后 public可访问，internal 只有类库内可访问

2. get set 封装

    - get set 成员变量, 可以做过滤等操作
    - 只get即 readonly, 只set即 write only

    ```c#
    public class Point
    {
        
        //手动 get set, 修改私有变量
        private int _x;   //字段

        public int GetX()   
        {
            return _x;
        }
        public void SetX(int x)
        {
            if(x < 0) { throw new Exception("errorrrrrrrrrrrrrrrr"); } //filter
            this._x = x;
        }

        //property 属性  实质Y 是方法，只是调用方式与变量相同
        private int _y;   //字段 y 小写
        public int Y { get { return this._y; } set { this._y = value; } }   //property Y 大写


        //终极懒 get set  自动实现属性
        public int Z { get; set; }  // 会自动生成一个 private z 且 通过Z属性访问

        public Point(int x, int y)
        {
            this._y = y;
            this._x = x;

        }
    }

    public static void Main(string[] args)
    {
        var a = new Point(1, 2);
        a.GetX();
        a.SetX(4);
        
        Console.WriteLine(a.Y);
        a.Y = 3;

        Console.WriteLine(a.Z);
        a.Z = 10;
    }
    ```

### 索引index，范围range

- 111
    ```C#
    string[] arr = new string[] {
        "aaa",
        "bbb",
        "CCC",
        "DDD"
    };

    Index i = ^1;
    Console.WriteLine(arr[i]);  //倒数第一位  DDD

    Range r = 0..2; //0 , 1
    foreach(string s in arr[r])
    {
        Console.WriteLine(s);
        //"aaa",
        //"bbb",
    }

    //还可以通过this 给类添加索引
    ```

### partial 类

- 使用局部类，可以拆分文件

### 耦合

- 指 类之间相互依赖关系 如继承等， 基类修改操作，从而所有派生类都修改，过度消耗性能----避免高耦合

1. 封装 ： 对业务逻辑实现细节隐藏
2. 类关系
3. **使用接口**

### 类关系

TODO

### 继承 :

- 方法属性继承
    ```C#
    internal class Program
    {
        public static void Main(string[] args)
        {

            Triangle t = new Triangle();
            t.GetArea();//继承方法
            t.SayHi();  
            t.Width = 10; //继承属性
            t.Height = 10;
        }
        
    }
    class Sharp     //基类
    {
        public int Width { get; set; }
        public int Height { get; set; }
        public void GetArea()
        {
            Console.WriteLine("Sharp Area");
        }
    }
    class Triangle: Sharp   //继承
    {
        public void SayHi()
        {
            Console.WriteLine("Triangle");
        }
    }
    ```

- 构造函数继承

    ```c#
    public static void Main(string[] args)
    {
        new Manager(123);           //继承会先执行父级的构造函数再执行子级 的构造函数
        //Staff 一个参数初始化
        //Manager NO:123 初始化
    }
    public class Staff
    {
        public string StaffNumber { get; set; }
        public Staff()
        {
            Console.WriteLine("Staff 无参初始化");
        }

        public Staff(int Number)
        {
            Console.WriteLine("Staff 一个参数初始化");
            StaffNumber = $"NO:{Number}" ; 
        }
    }

    public class Manager: Staff
    {
        public Manager()
        {
            Console.WriteLine("Manager 无参初始化");
        }

        public Manager(int number) :base(number)    //使用传number的构造函数 根据base传参选择
        {
            Console.WriteLine($"Manager {StaffNumber} 初始化");     //StaffNumber 继承来的变量
        }
    }
    ```

- 修饰符
    
    - 

    ```C#
    ```


### 复合

- 将实例传入构造函数，的依赖

    ```c#
    internal class Program
    {
        public static void Main(string[] args)
        {
            Logger logger = new Logger();
            Installer i = new Installer(logger);    //传入实例
            i.Install();
        }
    }

    class Installer
    {
        private readonly Logger _logger;
        public Installer(Logger logger) //logger实例
        {
            _logger = logger;
        }
        public void Install()
        {
            _logger.Log("install log"); //使用logger的方法
            Console.WriteLine("logging"); 
            //install logic
        }
    }
   
    class Logger
    {
        public void Log(string logMsg)
        {
            Console.WriteLine(logMsg);
        }
    }
    ```

### 类型转换 拆箱 装箱

- 对象转化

    ```C#
    public static void Main(string[] args)
    {
        //向上
        Sharp sharp = new Cricl();  //new 子类，转化成基类
        //sharp.R 不能得到
        
        //向下
        Cricl cricl1 = (Cricl)new Sharp(); //可以通过 (type) 的方式转换 如果失败报错
        Cricl cricl = new Sharp() as Cricl; //基类 转化成子类 可以使用 as 如果失败则为 null

        //避免失败的问题
        Sharp sharp1 = new Sharp();
        if (sharp1 is Cricl)    //判断类型之后再去转换
        {
            Cricl cricl2 = (Cricl)sharp1;
        }
    }

    class Cricl: Sharp
    {
        public int r;
    }

    class Sharp
    {
        public int Width;
        public int Height;
        public int X;
        public int Y;
    }
    ```

- 装箱拆箱： 指的是 值类型 <-> 引用类型， 会是存储 栈<->堆， 消耗性能
- ∴ 使用泛型 避免拆装

## correlation

集合 | 特点
-|-
string[] | 限定类型 长度不能修改
ArrayList | 任意类型， 缺少类型判断
List<type> | 泛型 

```C#
string[] cars = { "BMW", "DZ", "AD" };
ArrayList array = new ArrayList();
array.Add('1');     //
array.Add(sharp);   //可以add 任何类型

List<String> lArr = new List<string>();
lArr.Add("777");    //泛型规定只能 add  字符串

```


### 虚方法 多态

- overide virtual , 虚方法可以重写

```c#
internal class Program
{
    public static void Main(string[] args)
    {
        List<Sharp> sharps = new List<Sharp>() { new Ciclr(2), new Triangle(2, 4) };
        foreach(Sharp sh in sharps)
        {
            Console.WriteLine(sh.getArea());    //调用的是基类的虚方法，实际执行的是子类的 override 方法
            //12.566370614359172
            //4
        }
    }

}
class Triangle: Sharp
{
    
    public Triangle(int width, int height):base(width, height) { }
    public override double getArea()        //重写方法
    {
        return 0.5 * Width * Height;
    }
}

class Ciclr : Sharp
{
    public int R { get; set; }
    public Ciclr(int R){
        this.R = R;
    }
    public override double getArea()    //重写方法
    {
        return 2 * Math.PI * R;
    }
}

class Sharp
{
    public int Width { get; set; }
    public int Height { get; set; }
    public Sharp() { }
    public Sharp(int width, int height)
    {
        Width = width;
        Height = height;

    }
    virtual public double getArea() //虚方法
    {
        return Width * Height;
    }
}
```

### 抽象 abstract

- 抽象类，抽象成员，派生类必须实现全部抽象成员
- 抽象类不能实例化

```c# 
class Manager : Staff
{
    public override void SayHi()
    {
        Console.WriteLine("Hello"); // 继承抽象类必须实现抽象方法
    }
}
abstract class Staff
{
    public abstract void SayHi();   //抽象方法
}
```

### 密封 sealed 与 抽象相对 没啥用的

- 密封类： 不能被继承
- 密封方法: 不能被重写

### 接口 interfice

- 面向对象解耦 很重要的一环

```C# 
public static void Main(string[] args)
        {
            ICalculator calculator;
            
            if (DateTime.Now.Date.Equals("11/11"))
            {
                calculator = new Double11Calculator();
            } else
            {
                calculator = new NormalCalculator();
            }
            
            Alibaba alibaba = new Alibaba(calculator);
            alibaba.buy();

        }

        // 接口很重要 
        // 如果类A 是淘宝，需要在不同的时间段采用不同的运费计算，有多个运费计算相关类
        // 通过复合，得到B  的方法
        // 如果直接复合 日常运费计算类B，这时在 A 中的代码，就是写死的 调用B 和 B 的方法(多个)，
        // 这样 A 和 B 就是耦合的，联系太多了，
        // 如果到1111计算运费， A 中的 B 需要修改的地方很多，复合C 换成调用C 的方法(很多)
        // 就很烦了
        // 这时  BC 同为运费计算，只是逻辑略微不同，提取公共方法，就可以得到一个接口类 IB，
        // BC 都 继承 IB， 且实现各自不同的 计算逻辑
        // 这时 A 中的代码可以 改写成 引入 IB,调用IB 的方法，
        // 这样 切换不同的复合， 不需要修改 A里的代码， 只需要在复合的地方传入实现接口的不同类即可

        public class Alibaba
        {
            private ICalculator _calculator1;
            public Alibaba(ICalculator calculator)
            {
                _calculator1 = calculator;
            }

            public void buy()
            {
                Console.WriteLine("Buy Some thing");
                Console.WriteLine($"运费：{_calculator1.Calculatoe()}");
            }
        }

        public interface ICalculator //接口类需要 I加类名
        {
            int Calculatoe();   //接口方法 默认public
        }

        public class NormalCalculator : ICalculator
        {
            public int Calculatoe()
            {
                return 10;
            }
        }

        public class Double11Calculator : ICalculator
        {
            public int Calculatoe()
            {
                return 0;
            }
        }
```



## Array Collection

类 | 创建 | 特点
-|-|-
Array 数组 | string[] | 固定长度 固定类型
ArrayList 列表 | | 可变长度 任意类型
List<T> 泛型列表| | 可变长度 固定类型
Dictionary<T> 字典| | K-V
Queue<T> 队列| | 先进先出
Stack<T> 栈 | | 后进先出
IEnumerable<T> | | 可迭代集合


- 数组

    ```c#
    string[] daysOfWeek = { "1", "2", "3", "4", "5", "6", "7" }; //字面量
    string[] arr2 = new string[5];  //new 构造
    arr2[0] = "1";
    arr2[5] = "22222222";   //error index outside
    foreach(string day in daysOfWeek)
    {
        Console.WriteLine(day); //通过forEach遍历
    }
    ```

- ArrayList List<>

    ```C#
    List<string> list = new List<string>(); //空构造
    list.Add("1");
    list.Add("2");
    list.Add("3");
    list.Add("4");
    list.Add("5");
    var list2 = new List<string>(list);     //构造传入 可迭代的对象
    Console.WriteLine(list2[1]);//2
    List<string> list3 = new List<string>(5);  //创建初始化有长度的数组
    Console.WriteLine($"length: {list3.Count}, capacity: {list3.Capacity}");
    List<string> list4 = new List<string>   //初始化 直接赋值
    {
        "1",
        "2",
        "3",
        "4",
    };
    Console.WriteLine(list4[3]);    //4

    //插入 insert insertRange
    //删除 removeAt RemoveRange
    //Remove 遍历 删除第一个找到的 RemoveAll 
    //迭代器 Enumerator moveNext
    //foreach() 通过迭代器实现的， 不能遍历时修改长度 且只读
    //Eenumerable TODO 对象继承迭代器，实现后实例可以遍历
    //yield 类似懒加载 TODO

    //IList<string> list4 = new List<string>();   // IList 接口类型
    ArrayList arr = new ArrayList();    //类型问题 一般不用
    arr.Add(list);
    arr.Capacity = 5;
    ```
- Dictionary

    ```C#
    public class Customer   //某个类
    {
        public string Name { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public Customer(string firstName, string lastName) {
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Name = $"{firstName} - {lastName}";
            Console.WriteLine($"Welcome Customer {Name}");
        }
    }

    //字典的使用  
    public static void ddd()
    {
        //字典支持泛型
        Dictionary<string, Customer> cd = new Dictionary<string, Customer>();
        cd.Add("001", new Customer("Z", "Wb"));
        cd.Add("002", new Customer("Z", "YS"));
        foreach(Customer c in cd.Values)
        {
            Console.WriteLine(c.Name);
        }
        Console.WriteLine(cd["001"].Name);  //[]访问
    }

    //HashSet用法相同只是缺少泛型约定
    ```

## [LinQ](https://www.entityframeworktutorial.net/querying-entity-graph-in-entity-framework.aspx)

- 与SQL 关键字类似

方法 | 功能 
-|-
Where | 返回复合条件
OrderBy | 排序
OrderByDescending | 降序
ThenBy | 二级排序
ThenByDescending | 二级降序
Count | 返回长度
Skip | 跳过行
Take | 取前几行
First | 空会报错 
FirstOrDefault | 不匹配返回空 
Any | 返回 bool， 可用于判断集合为空
Contains | 返回 bool， 包含
All | 返回bool
Select | 最后返回内容拼接
Join | 链接表 tab1.Join(tab2, t1=>xxx, t2=>xxx, new(tab1,tab2))
Group | 类似SQL


### 深层原理 TODO  

### 
