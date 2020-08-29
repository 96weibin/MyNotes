# raphael 拉斐尔

- [官网](http://raphaeljs.com/)  兼容至ie6的 类似jq的 支持transform 小巧矢量图绘制库

## 使用

- 页面引入

    ```html
        <div id="container"></div>
        <script src="./js/raphael-min.js"></script>
        <script>
            //画布
            var paper = Raphael('container',800,600);

            //画圆
            var dot = paper.circle(100,100,100).attr({
                fill:'none',
                stroke:'#000',
                "stroke-width":1
            });
            
            //方框
            var rect = paper.rect(100,200,100,100).attr({
                fill:'blue',
                stroke:'none'
            }).click(function(){            //类似jq的 链式
                this.animate({              //jq animate
                    width:'200',
                    fill:'pink'
                },2000, 'ease-in-out')
                //bounce 弹性
                //elastic 弹性
            })
              //path 
            var path = paper.path('M 0 300 L 50 400 100 300 150 400 200 300').attr({
                "stroke-width":10
            })
            path.click(function(){
                this.animate({
                    path:'M 0 400 L 50 300 100 400 150 300 200 400',
                    transform:'r30t100,100s2,1'     //rotate 30 translate 100,100 scale 2,1
                }, 1000, 'bounce')
            })

            // 椭圆    顶点 在 右侧  所以  transform  rx ry
            let cx = 400,
                cy = 300,
                rx = 150,
                ry = 50;
            let elipse2 = paper.path(`M ${cx} ${cy - ry} A ${rx} ${ry} 0 1 1 ${cx} ${cy - ry - 0.001}`).attr({'stroke':"blue", "stroke-width" : 20,"transform":`t${rx},${ry},r-120`})
        </script>
    ```
