# C# 高级编程

## 7-2 structs 结构体

- 类似于class 但是是值类型，无默认构造函数，需实例化 全部内部属性赋值才能被调用，

    ```c# 
    struct Game
        {
            public int Id;
            public string Name;
            public string Description;
        }
        static void Main(string[] args)
        {
            Game game = new Game();
            game.Id = 01234;
            game.Name = "pokmon";
            game.Description = "精灵宝可梦";
            Console.WriteLine(game.Name);
            Console.WriteLine("Hello World!");
        }
    ```

## 枚举enum

- 与ts相同

## generic 泛型

