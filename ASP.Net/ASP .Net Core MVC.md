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
    public class HomeController : Controller
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
                endpoints.MapControllers();  //添加路由中间件
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



