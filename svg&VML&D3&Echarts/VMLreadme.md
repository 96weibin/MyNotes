# VML

- 比svg 更早 兼容<iE7 的矢量图
- 与SVG搭配实现 全兼容  !ie8
- vml是 html 可以 document.createElement 支持事件 

## 简单使用 

- demo

    ```html

        <!DOCTYPE html>
        <html xmlns:v="urn:schemas-microsoft-com:vml">
            <!-- xml name space -->
        <head>
            <meta charset="UTF-8">
            <title>Document</title>
            <style>
                v\:*{      
                    behavior: url(#default#VML);
                }   
                /* vml  <v:xxx  /> 的标签  */
                v\:rect{
                    position: absolute;
                    display: block;
                }
                v\:oval{
                    position: absolute;
                }
                v\:shape{
                    position: absolute;
                }
            </style>
        </head>
        <body>

            <!-- 
                vml用于低版本IE  
                1. 配置html xmlns 和style v\:*{behavior:url(#default#vml)}
                2. v:line v:rect
                3. 标签一定要闭合
            -->
            <v:line from="20,0" to="100,100" strokecolor="blue" strokeweight="20" />

            <!-- 矩形 -->
            <v:rect style="width: 100px; height: 100px; top: 150px; left: 20px;"/>

            <!-- 圆形 -->
            <v:oval style="width: 200px; height: 100px; left: 20px; top: 300px;" />

            <!-- 路径 -->
            <v:shape path="M 0 0 L 500 200 200 200 X" style=" top: 500px; width: 1000px; height: 1000px;"/>
            <!-- width height 是画布大小  影响路径比例 -->

        </body>
        </html>


    ```