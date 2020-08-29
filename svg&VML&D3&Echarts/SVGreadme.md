# SVG

- 源自XML、 矢量图、 有事件和属性、 性能一般

> svg 不是html标签

## 基础绘图

- svg标签内 line

    ```html
        <svg width='800' height="600">  
            <!-- width height 在行间设置  且因为是  矢量图 不使用单位 -->
            <line x1='100' y1='100' x2='200' y2 = '300' stroke-width='20' stroke="black"></line>
            <line x1='200' y1='100' x2='300' y2 = '300' style="stroke-width: 20; stroke:blue"></line>  与写在style标签内相同
            <!--样式  可以写在style 中  决定图形位置、形状的  不能 -->
        </svg>
    ```

### 优先级

-  行间 stroke-width=20 < * < css style=""行间

### 图形

- 不同标签对应图形

    图形 | 标签 | 参数 | 例子 | 样式 | 注释
    -|-|-|-|-|-
    线 | line | x1,y1,x2,y2 | \<line x1='100' y1='100' x2='200' y2 = '300' ></line> | stroke | x1,y1是起点 x2,y2是终点
    矩形 | rect | x,y,width,height,rx,ry | \<rect id="rect" x="100" y="100" width="100" height="100"></rect> | stroke fill | rx,ry是圆角
    圆形 | circle | cx,cy,r |\<circle cx="100" cy="100" r="50" fill="pink"></circle> | stroke fill | 圆点 半径
    椭圆 | ellipse | cx,cy,rx,ry | \<ellipse cx="100" cy="100" rx="100" ry="50"></ellipse> | | rx、ry 是椭圆的宽 高
    路径 | path | d="M 100,100 L 100,100" | | | M moveto、 L lineto

## 事件

- 与html事件绑定相同

    ```html
        <svg width='800' height="600">
            <line x1='100' y1='100' x2='200' y2 = '200' id="l1"></line>
        </svg>

        <script>
            let oL1 = document.querySelector('#l1');
            oL1.addEventListener('click',function(){
                console.log(this)
                this.setAttribute('x1','50')    //setAttribute 设置属性
                this.style.stroke = 'red'
            })
        </script>
    ```

## path 

- path  d 设置路径 通过空格分隔

    参数 | 功能 | demo
    -|-|-
    M | moveto | M 0 100
    L | lineto | L 100 100
    A | arc | A rx ry 旋转角度 largeFlag大弧 镜像 终点X 终点Y
    S | 二次贝塞尔曲线 | S 控制点X 控制点Y 终点X 终点Y
    Q | 四次贝塞尔曲线 | Q 控制点X 控制点Y 终点X 终点Y
    Z | 闭合路径 | Z

    ```html
      <svg width="800" height="600">
        <!-- A rx ry x旋转 大弧 镜像 终点X 终点Y  -->
        <path d="M 0 100 L 100 100 A 1 1 0 1 1 200 100 L 300 100" fill="none" stroke="black"></path>

        <path id="bing" stroke="blue" fill="none"></path>

        <path id="large1" stroke="red" fill="none"></path>
        <path id="large2" stroke="blue" fill="none"></path>
        <path id="large3" stroke="green" fill="none"></path>
        <path id="large4" stroke="pink" fill="none"></path>
    </svg>
    
    <script>
        //画饼图  ang1 ~ ang2
        let bing = document.querySelector('#bing');

        //#1
        let ang1 = 0,
            ang2 = 300,
            r = 100,
            x = 100,
            y = 300
        function d2a(d) {   //角度转弧度
            console.log(d / 180 * Math.PI)
            return d /180 * Math.PI
        }

        let arr = [],
            x1 = x + Math.sin(d2a(ang1)) * r,
            y1 = y - Math.cos(d2a(ang1)) * r;
        
        arr.push(`M ${x} ${y} L ${x1} ${y1} `)

        //#2
        x2 = x + Math.sin(d2a(ang2)) * r,
        y2 = y - Math.cos(d2a(ang2)) * r;

        arr.push(`A ${r} ${r} 0 ${Math.abs(ang2 - ang1) < 180 ? 0 : 1} 1 ${x2} ${y2}`)
            //largeflag 大于180度 1 小于180度 0

        //#3
        arr.push('Z')       //闭合

        bing.setAttribute('d',arr.join(' '))

        // 大弧  镜像  0 1  

        /*
            通过相同两点  相同半径  有两个椭圆   相交出4条线

            largeFlag 画圆
            > π         1
            < π         0

            镜像 笔的  
                左侧 0
                右侧 1 
        */


        let large1 = document.querySelector('#large1');
        let large2 = document.querySelector('#large2');
        let large3 = document.querySelector('#large3');
        let large4 = document.querySelector('#large4');

        
        large1.setAttribute('d',`M 400 400 A 150 100 0 0 0 500 400`)
        large2.setAttribute('d',`M 400 400 A 150 100 0 0 1 500 400`)
        large3.setAttribute('d',`M 400 400 A 150 100 0 1 0 500 400`)
        large4.setAttribute('d',`M 400 400 A 150 100 0 1 1 500 400`)


        //贝塞尔
        let bessel4 = document.querySelector('#bessel4');   //四次贝塞尔
        bessel4.setAttribute('d',`M 100 500 Q 300 400 300 500 `)
        
        // Q 控制点x 控制点y  终点X 终点y
        let bessel2 = document.querySelector('#bessel2');   //二次贝塞尔
        bessel2.setAttribute('d',`M 100 550 S 300 450 300 550 `)
        // S 控制点x 控制点y  终点X 终点y
    </script>
    ```

## js创建svg

- document.createElement 只是 createElementNS 的简写  

    ```js
        let svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
        document.body.appendChild(svg)
    ```
## svg动画

- svg 不支持transition transform 只能用js做动画

    ```js
        let oL = document.querySelector('#l1');
        oL.onclick=function(){
            requestAnimationFrame(next)
            let frameCount = 0,
                that = this;
            function next(){
                let x1 = that.getAttribute('x1')
                if(frameCount % 4 == 0){
                    that.setAttribute('x1', parseInt(x1) + 1)
                }                                        
                if(x1 >= 200) {
                    return
                }                
                frameCount ++;
                requestAnimationFrame(next)
            }
        }
    ```

