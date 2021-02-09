# tools
web develop tools
webpack : 组合插件使用实现打包、编译、测试、调试等功能

## webpack

- 自身只能对json、js进行打包，通过loader、plugin的使用实现对各中资源的打包
- loader  只能处理   js   webpack本身能处理的东西
- 其他资源  通过plugin 进行处理


1. 安装

    ```shell
    $ npm i -g webpack # webpack、webpack-cli全局安装，开发安装，
    ```

2. 配置文件(默认webpack.config.js)

    ```js
        const pathLib = require('path')
        module.exports = {
            mode : 'development',   //模式  dev 打包不压缩、pro打包会压缩

            //entry : pathLib.resolve('./libs/1.js'),     //单入口  
            entry : {                                     //多入口
                test1 : pathLib.resolve('./libs/1.js'),
                test2 : pathLib.resolve('./libs/2.js'),
            }, 
            output : {  //输出配置
                path:pathLib.resolve('./dest/'),        //结果目录
                // filename:'bundle.js'                    //单入口结果文件名    
                filename : '[name].bundle.js'       //多入口输出 test1.bundle.js、test2.bundle.js
            }, 
            module:{
                rules:[]//loader(翻译)配置 
            },
            plugins:[]  //插件配置
        }
    ```
3. 启动
    ```shell
    $ webpack --config ***.webpack.js     #启动非默认配置文件
    $ webpack  #启动默认配置文件
    ```

4. 命令行运行处理

    ```shell
    $ webpack ./index.js -o ./build/bundle.js --mode=development # 将index.js编译到bundle.js
    ```

### 打包各种文件

#### 打包样式资源

1. 将css打包到js中通过style插入*css-loader style-loader*

    ```js
    module : {
        rules : [
            {
                test : /\.css$/,
                use : [ //loader自下至上一次使用,顺序很重要
                    'style-loader',
                    //创建style标签，将js中的样式资源插入到html head
                    'css-loader'
                    //将css文件变成模块加载进js中
                    ]
            },
            {
                test:/\.less$/,
                use:[
                    'style-loader',
                    //在html header内添加style标签引入
                    'css-loader',
                    //2将css以字符串以便引入到js,
                    'less-loader'
                    //1 将less转换成css
                ]
            }
        ]
    },
    ```

2. 将css文件打包后生成css文件以link标签引入*css-loader min-css-extract-plugin*

    ```js
    //提取css为单独文件的插件
    const MiniCssExtractPlugin = require('mini-css-extract-plugin')
    module.exports = {
        entry : "./src/index.js",
        output : {
            filename : "js/bundle.js",
            path : resolve("./build")
        },
        module : {
            rules : [
                {
                    test : /\.css$/,
                    use : [
                        MiniCssExtractPlugin.loader,
                        //插件自带的loader
                        'css-loader'
                    ]
                }
            ]
        },
        plugins:[
            new HtmlWebpackPlugin({
                template:'./src/index.html'
            }),
            new MiniCssExtractPlugin({
                filename:'css/build.css'
                //将输处理后的css放到css目录下
            })
        ],
        mode:"development"
    }
    ```

3. css文件兼容行处理*postcss-loader postcss-preset-env*
vue-cli就用的这种方法  **plugins 返回数组**

    - webpack.config.js

        ```js
        process.env.NODE_ENV = 'development'
        //设置node环境为开发模式，默认为生产模式

        module.exports ={
            module : {
                rules : [
                    {
                        test : /\.css$/,
                        use : [
                            MiniCssExtractPlugin.loader,
                            'css-loader',
                            {
                                loader:'postcss-loader',
                                options :{
                                    ident :'postcss',//固定写法
                                    plugins:()=>[   //plugins返回数组
                                        require('postcss-preset-env')()
                                        //postcss-preset-env插件会去package.json中
                                        //找browserslist获取兼容行配置
                                    ]
                                }
                            }
                        ]
                    }
                ]
            },
        }
        ```

    - package.json

        ```js
        {

        "browserslist": {       //postcss-preset-env会找到他
            "development": [    //node环境为开发时的配置
            "last 1 chrome version",
            "last 1 firefox version",
            "last 1 safari version"
            ],
            "production": [     //默认的配置
            ">0.2%",          //80%的浏览器都支持
            "not dead",       //已经死的不兼容
            "not op_mini all" //不兼容欧朋mini
            ]
        }
        }
        ```

4. 压缩css *optimize-css-assets-webpack-plugin*

    - webpack.config.js

        ```js
        const MiniCssExtractPlugin = require('mini-css-extract-plugin')
        module.exports = {
            plugins:[
                new HtmlWebpackPlugin({
                    template:'./src/index.html'
                }),
                new MiniCssExtractPlugin({
                    filename:'css/build.css'
                }),
                //new调用，默认配置将css文件进行压缩
                new OptimizeCssAssetsWebpackPlugin()
            ],
        }

        ```


#### 打包脚本文件

1. eslint检查

    - webpack.config.js

        ```js
        module.exports={
            //****
            module:{
                rules:[
                    {   
                        //eslint 
                        //eslint-loader
                        //eslint-plugin-import 
                        //eslint-config-airbnb-base 
                        //使用airbnb风格指南需要以上插件

                        //在package.json中eslintConfig写入规则配置
                        test:/\.js$/,
                        exclude:/node_modules/, //不检查第三方库
                        use:[
                            {
                                loader:'eslint-loader',
                                options:{
                                    fix:true
                                    //自动修复src内文件,不符合规则的
                                }
                            }
                        ]
                    }

                ]
            }
        }
        ```

    - package.json

        ```js

        "eslintConfig":{
            "extends":"airbnb-base" //使用airbnb-base风格规范
        }
        ```
2. 兼容性处理 babel

    处理方法 | 缺点 | 插件 | 方式
    -|-|-|-
    预设处理 | 预设编译ie不能识别promise等 | babel-loader, @babel/preset-env | 配置loader
    全部处理 | 全部处理js文件过大 | babel-loader, @babel/preset-env, @babel/polyfill | 配置loader + 页面引入
    按需加载 | | babel, core-js | babel-loader，@babel/preset-env, core-js | 配置loader

    - 预设处理

        webpack.config.js

        ```js
        rules:[
            {   
                //1. babel-loader @babel/preset-env 预设处理
                test:/\.js$/,
                exclude:/node_modules/, //不检查第三方库
                use:[
                    {
                        loader:'babel-loader',
                        options:{
                            //使用预设环境进行基础兼容处理,不支持promise等es6
                            presets:["@babel/preset-env"],
                            //presets 要是一个数组
                        }
                    }
                ]
            },
        }
        ```

    - 全部处理

        index.js
        
        ```js
            import "@babel/ployfill"
            //****
        ```
        webpack.config.js 同上

    - 按需加载 core-js
        
        webpack.config.js

        ```js
        module.exports={
            module:{
                rules:[
                    {
                        //使用core-js按需加载

                        test:/\.js$/,
                        exclude:/node_modules/,
                        use:[
                            {
                                loader:'babel-loader',
                                options:{
                                    presets:[
                                        [
                                            '@babel/preset-env',
                                            {
                                                useBuiltIns:'usage',//按需加载
                                                corejs:{
                                                    version:3   //core-js的版本
                                                },
                                                targets:{         //详细兼容到的浏览器版本
                                                    ie:'8',
                                                    chrome:'60',
                                                    // firefox:'60'
                                                    // safair:"69"
                                                    // edage:'50'
                                                }
                                            }
                                        ]
                                    ]

                                }
                            }
                        ]
                    }
                ]
            }
        }
        ```
    3. js压缩

        将mode改成"production"时会自动进行压缩

#### 打包html文件 html-webpack-plugin

1. html

    ```js
    const hwp = require('html-webpack-plugin')  //plugin 需要引入页面使用
    const pathLib = require('path')
    module.exports={
        entry:'./src/index.js',
        output:{
            path: pathLib.resolve("./build"),
            filename:"build.js"
        },
        plugins:[
            new hwp({
                template:'./src/index.html',
                minify:{    //压缩
                    collapseWhitespace:true,//移除空行
                    removeComents:true //移除注释
                }
            })
            //复制index.html 并 引入所有构建后的所有文件
        ],
        mode:"development"
    }
    ```


2. 图片资源

    url-loader 依赖于file-loader  还需要-D 安装file-loader

    ```js

    const {resolve} = require('path')
    const HtmlWebpackPlugin = require('html-webpack-plugin')
    module.exports={
        entry:"./src/index.js",
        output:{
            path:resolve('./build'),
            filename:'build.js'
        },
        mode:"development",
        module:{
            rules:[
                {
                    test:/\.less$/,
                    use:[   //多个loader使用use
                        'style-loader',
                        'css-loader',
                        'less-loader'
                    ]
                },
                {
                    test:/\.(jpg|png|gif)$/,
                    loader:'url-loader',    //只是用一个loader
                    //url-loader 处理图片, 依赖file-loader
                    options:{
                        limit:10*1024,   //小于8k的图转为base64
                        esModule:false,  //不使用es6的模块化使用commenjs
                        name:'[hash:10].[ext]', //处理后图片命名取hash前10位.拓展名
                        outputPath:'img'    //图片输出到build/img
                    }
                },
                {
                    test:/\.html$/,
                    loader:'html-loader'    //处理img标签文件
                }
            ]
        },
        plugins:[
            new HtmlWebpackPlugin({
                template:"./src/index.html"
            })
        ]
    }
    ```

3. 打包其他资源 file-loader

    ```js
    module:{
        rules:[
            {
                exclude:/\.(html|css|js)$/,//排除
                loader:'file-loader'  //其他资源直接使用fileloader处理
            }
        ]
    },
    ```


### dev-server

    自动编译、自动刷新、自动打开浏览器
    只在内存中进行运行,build不会输出文件

1. 安装

    ```
    $ cnpm i -D webpack webpack-cli webpack-dev-server
    ```

2. 配置 webpack.config.js

    ```js
        plugins:[
            new Weboack.HotModuleReplacementPlugin() //依赖webpack的插件
        ],
        devServer : {   
            contentBase : pathLib.resolve('./static'),  //静态目录
            port : 8090,        
            compress:true,              //启用gzip压缩
            
            hot:true,                   //hmr 热模块替换 优化编译速度
            historyApiFallback : true,   //404转到 index.html
            open:true                   //自动在默认浏览器
        },
    ```

    启动指令

    ```shell
    $ webpack-dev-server --watch --inline --config xxxx.js
    $ #            watch静态文件  在线刷新 或者 --ifream
    ```

### webpack 的优化


#### 开发环境优化
    - 优化打包速度

##### HMR hot module replacement

    一个模块发生变化，未配置hmr时，会将全部模块都进行重新打包，
    启动hmr后则值重新打包某个模块

文件资源 | 是否支持hmr | 解决方法
-|-|-
样式资源 | style-lader支持可以使用 | 
js文件   | 默认不支持 | 修改js添加支持hmr的代码
html文件 | 不支持<br>且开启hmr会导致文件不能热更新 | 修改entry为数组添加html路径

- js模块热替换

    ```js
    if(module.hot){ //开启了hmr
        module.hot.accept('./print.js',function(){  //入口模块不适用
            //xxx  print重新打包时执行xxx
            //当开启hmr后，修改print.js 其他模块不会一起打包
        })
    }
    ```

- 开启hmr后修改配置使html热响应
    ```js
        entry:['./src/index.js','./src/index.html'],
    ```

##### oneOf:[]

```js
module:{
    
    rules[
        {},     //不被oneOf的loader
        {
            oneOf:[
                {
                    //oneOf数组包裹的多loader
                    //只有一个与文件匹配,即匹配到就不继续向下匹配
                    //不能有两项配置处理同一类型的文件
                },
                {

                }
            ]
        }
    ]
}

```

##### 缓存

1. babel缓存
    修改一个js文件,只重新编译一个js文件，其他js文件从缓存中读取
    ```js
    module:{
            rules:[
                {
                    //使用core-js按需加载
                    test:/\.js$/,
                    exclude:/node_modules/,
                    use:[
                        {
                            loader:'babel-loader',
                            options:{
                                presets:[
                                    [
                                        '@babel/preset-env',
                                        {
                                            useBuiltIns:'usage',//按需加载
                                            corejs:{
                                                version:3   //core-js的版本
                                            },
                                            targets:{         //详细兼容到的浏览器版本
                                                ie:'8',
                                                chrome:'60',
                                                // firefox:'60'
                                                // safair:"69"
                                                // edage:'50'
                                            }
                                        }
                                    ]
                                ],
                                cacheDirectory:true
                                //开启babel缓存，
                                //只改变一个模块的时候,其他模块从缓存中调用
                            }
                        }
                    ]
                }
                
            ]
        },
    ```
2. 文件缓存

    http设置返回使用缓存的时候，文件在缓存时间内不会被改变，<br>
    解： 文件名设置hash进行区别版本<br>
    hash 每一次编译一个相同的hash <br>
    chunkhash   根据chunk生成hash<br>
    ***contenthash*** 根据文件内容生成hash值,文件内容不变hash不变

    ```js
        output:{
            filename:'bundle.[contenthash:10].js', //文件名添加10位hash值
            path: resolve('./build')
        },
    ```
3. tree shaking 去除无用代码，在应用中未使用到的方法等代码进行删减

    条件： 使用es6模块化  import 、 production环境

    由于版本问题可能过滤掉js中引入的css文件，可以在package.json中设置"sideEffects"：[*.css]不摇css文件 
    
4. code split 将文件分割，使之并行下载、按需加载等

    


#### 生产环境优化
    - 代码运行速度优化

