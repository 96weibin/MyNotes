# ASP .Net Core MVC

- 课程知识点

    ![](./img/knowledge%20point.png)

## .Net 历史

- .net framework 与 .net core 不同的产品
- .net framework 早期 闭塞
- .net core 后来者 开源跨平台
- .net core MVC 开发时框架

    ![](./img/history.png)

## 安装 .net core && sdk

- 通过 visual studio 安装
    ![](./img/setup.png)


## 创建项目

- 创建 .Net core Empty
- .net 5.0

### 项目目录 

- Properties/launchSettings.json
    - IIS 端口 开发模式 等设置
- wwwroot

- program.cs 
    - 入口 main函数 创建HTTP服务
    ```c#
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                });
    }
    ```
- startup.cs 
    - 环境设置， 请求通道
    ```C#
    public class Startup
    {
        // This method gets called by the runtime. Use this method to add services to the container.
        // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
        public void ConfigureServices(IServiceCollection services) //组建依赖
        {
            services.AddMvc();  //注册MVC组件
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)//配置 HTTP请求通道中间件
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();    //当前开发环境
            }

            app.UseRouting(); //传递 app？ 

            app.UseEndpoints(endpoints =>       //路由表
            {
                endpoints.MapGet("/test", async context =>  //在 / 之前
                {
                    await context.Response.WriteAsync("Hello test!");   //短路
                });
                endpoints.MapGet("/", async context =>
                {
                    await context.Response.WriteAsync("Hello World!");
                });
            });
        }
    }
    ``` 

### nuGet

- c# 的包管理工具

## 增量

1. 开发思维
2. 代码过程 规范
3. 设计模式
4. 系统架构 路基，运行，数据，物理

## 路由

- controller/action/
    
中间件 | 功能
-|-
MapDefaultControllerRoute | 传统默认路由
MapControllers | 注释参数路由
MapControllerRoute | 自定义组合路由

### 路由两种模式  

1. 传统路由 Conventional Routing
    通过路由表
    - startup.cs
    ```c#
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();  //引入 MVC 依赖
        }
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapDefaultControllerRoute();  //添加路由中间件
            });
        }
    }
    ```

    - HomeController
    
    ```C#
    public class HomeController : Controller  //以controller结尾 且 继承Controller 基类
    {
        public object Index()
        {
            return "hello Index";
        }
    }
    ```
2. 特性注释路由 Attribute Routing
    - 地址/controller/action/value

    - startup.cs
    ```C#
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();  //引入 MVC 依赖
        }
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();  //注释  参数路由
            });
        }
    }
    ```

    - HomeController
    
    ```C#
    [Route("Home")]
    //[Route("[controller]/[action]")]      //模式匹配路由 [controller] 会匹配所有controller, [action]会根据函数名匹配
    public class HomeController : Controller
    {
        [Route("Index")]
        public object Index()
        {
            return "hello Index";
        }
    }
    ```
3. 自定义路由

    - startup.cs
    ```C#
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();  //引入 MVC 依赖
        }
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                 endpoints.MapControllerRoute(name:"default", pattern:"{controller=home}/{action=index}/{id?}");  //启动自定义路由 并 指定默认路由
            });
        }
    }
    ```

    - HomeController.cs
    
    ```c#
    public class HomeController : Controller
    {
        public ActionResult Index()       //打开网页默认跳转 也是 home 或 home/index
        {   //ActionResult 可以解析 string view等
            return View();  // 右键添加 Razor View 即 .schtml文件
        }

        public string About()       //home/about
        {
            return "hello About";
        }
    }
    ```

    - UserController.cs

    ```C#
    //组合 attribute使用
    [Route("admin/[controller]/[action]")]
    public class UserController : Controller
    {
        public List<string> Index()     // /admin/user/index
        {
            return new List<string>() { "user1", "user2" };
        }
    }
        
    ```

## MVC

- model 不单单是请求访问数据库

## Model

- 模型 包含Entity属性 和 业务逻辑， 不单单是映射数据库的类

### 模型仓库示例

1. 创建 entity 类

```C#
namespace RouterTest.Models
{
    public class Noodle     //entity
    {
        //属性
        public string Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public double Price { get; set; }
        public string ImgUrl { get; set; }
    }
}
```
2. 创建仓库 定义 接口

```C#
using System.Collections.Generic;

namespace RouterTest.Models
{
    public interface INoodleRepository     //仓库方法接口  接口类 以Ixxx格式
    {

        //两个 业务逻辑方法的接口
        IEnumerable<Noodle> GetAllNoodles();    
        //IEnumerable 处理数据库列表
        Noodle GetNoodleById(string id);
    }
}
```

3. 实现 接口

```C#
using System.Collections.Generic;
using System.Linq;

namespace RouterTest.Models
{
    public class MockNoodleRepository : INoodleRepository //实现接口
    {
        // 链接数据库获取数据
        private List<Noodle> _noodles;      //_xxx 下划线 表示私有
        public MockNoodleRepository()
        {
            if(_noodles == null)
            {
                InitNoodle();
            }
        }

        private void InitNoodle()
        {
            _noodles = new List<Noodle>
            {
                new Noodle{ Id = "1", Name ="牛肉"},
                new Noodle{ Id = "2", Name ="猪肉"},
                new Noodle{ Id = "3", Name ="羊肉"}
            };
        }

        //实现方法
        IEnumerable<Noodle> INoodleRepository.GetAllNoodles()
        {
            return _noodles;
        }

        Noodle INoodleRepository.GetNoodleById(string id)
        {
            return _noodles.FirstOrDefault(n => n.Id == id);
        }
    }
}
```

4. 注册仓库 startup

```c# 
public void ConfigureServices(IServiceCollection services)
{
    services.AddMvc();
    //如果这里没有注册  则  constructor 好像读取得不到
    services.AddTransient<INoodleRespository, MockNoodleRespository>();//依赖注入 注册仓库
    //每次初始化新的  结束 销毁

    //services.AddSingleton<INoodleRespository, MockNoodleRespository>(); //每次使用同一个
    //services.AddScoped<INoodleRespository, MockNoodleRespository>();    //
}
```

5. controoller 中调用

```C#
private INoodleRepository _noodleRepository;   //下滑表私有

public HomeController(INoodleRepository noodleRespository)      //Todo 构造函数
{
    _noodleRepository = noodleRespository;
}
public ActionResult Page()
{
    var n = _noodleRepository.GetAllNoodles();
    return View(n);     //右键生成 Razor 页面
}
```

6. 在Razor页面中使用

```cs
@model IEnumerable<RouterTest.Models.Noodle> 
@{
    ViewData["Title"] = "Page";
}

<h1>Page</h1>

@foreach(var n in Model)
{
    <h1>n.name</h1>
    <h2>n.id</h2>
}

```

## Entity Frame Core

LINQ 
ADO.Net

1. 安装 entity framework core 和 Entity Framework sqlserver

    右键 sln > manage nuget packages > browse > Entity Framework Core
