# CANVAS

    IE9+画布,DOM对象，通过获取其上下文，设置笔触设置路径绘制、填充图形，imageData对图片进行逐像素编辑。模糊、重复、  inline-block

> canvas是位图

## 基础使用

    ```js
        var c = document.querySelector('#myCanvas');
        var ctx = c.getContext('2d');
        ctx.beginPath();
        ctx.lineWidth = 10;
        ctx.moveTo(0,0);
        ctx.lineJoin = 'round';
        ctx.lineTo(100.,100)
        ctx.lineTo(50,100);
        ctx.lineTo(100,150);
        ctx.stroke()
    ```


## API

### 笔触  （需要stroke）

方法 | 描述 | 传参
-|-|-
beginPath() | 开始/重置一条路径 | 坐标
moveTo() | 将笔移到指定位置 | 坐标
lineTo() | 添加新点，创建连线 | 坐标
closePath() | 直线连接头尾位置 | 坐标
rect | 绘制矩形 | 左上 宽高
fill() | 填充路径(未闭合 自动闭合首位) | ——
stroke() | 描边路径 | ——
quadraticCurveTo() | 创建二次贝塞尔曲线 | 控制点，终点
bezierCurTo() | 创建三次贝塞尔曲线 | 控制点，控制点，终点
arc() | 创建弧/曲线 | 圆点坐标，半径,弧度(0~2*Math.PI) 顺时针
arcTo() | 创建两点间的圆弧 | 起点坐标，终点坐标，半径

属性 | 描述 | 取值
-|-|-
fillStyle | 填充颜色 仅对下一次绘制生效
globalAlpha | 透明度仅影响 后面的透明度
strokeStyle | 笔的颜色
lineCap | 线头样式 | round，square
lineJoin | 线条相交点 | round，bevel
lineWidth | 线条宽度 无需单位 | number
miterLimit | 斜接长度 宽线条内外交汇点间距离(控制接头的大小) | number

### 色卡

创建色卡对象，设置颜色，在对应的位置进行着色

方法 | 描述 | 传参
-|-|-
createLinearGradient() | 创建线性渐变色卡 | 矩形的左上右下坐标
createRadialGradient() | 创建环形渐变色卡 | 两个圆 的圆心坐标半径
addColorStop | 色卡 设置渐变停止位置(0~1)以及颜色 | 0.6，'red'

### 阴影

属性 | 描述
-|-
shadowColor | 阴影颜色
shadowBlur | 模糊级别 越小越清晰
shadowOffsetX | 水平阴影距离 像素无需单位
shadowOffsetY | 垂直阴影距离

### 矩形 （无需stroke）

方法 | 描述 | 传参
-|-|-
fillRect | 矩形填充 | 左上 **长宽**
strockRect  | 矩形描边 4参 坐标，长高
clearRect | 擦去矩形

### 文本

属性 | 描述 | 取值
-|-|-
font | 同css font
textAlign | 文本的左右对齐方式
textBaseLine | 文本水平基线位置
fillText() | 填充文字 | 文本，坐标，[最大宽度(缩放)]
strokeText() | 描边文本
measureText() | 获取文本的宽度

### imageData对象

- Img对象 像素级操作

方法 | 描述 | 传参
-|-|-
createImageData() | 创建空白ImageData对象(data.length 对图片逐像素编辑rgba)
getImageData() | 获取 ImageData对象 | x,y,w,h
putImageData() | 把图像数据 放到画布上  对象,坐标

属性 | 描述
-|-
width | 返回 ImageData对象的宽度
height | 返回ImageData对象高度
data | 返回ImageData对象数据

#### imageData像素处理

> 一个像素 有4位  分别是 rgba

- 滤镜

    ```js
        //滤镜处理
        let c = document.querySelector('canvas')
        let ctx = c.getContext('2d')
        let oImg = new Image();
        oImg.src = './6.jpg';
        oImg.onload = function(){
            ctx.drawImage(oImg,0,0,c.width,c.height)

            let imageData = ctx.getImageData(0,0,oImg.width,oImg.height)
            //获取 imageData对象
            let data = imageData.data;
            for(let i = 0; i < imageData.height; i ++){
                for(let j = 0; j < imageData.width; j++){
                    // data[(i * imageData.width + j) * 4 + 0]  r
                    // data[(i * imageData.width + j) * 4 + 1]  g
                    // data[(i * imageData.width + j) * 4 + 2]  b
                    // data[(i * imageData.width + j) * 4 + 3]  a

                    //黄色滤镜
                    data[(i * imageData.width + j) * 4 + 2] = 200;


                    //灰色滤镜
                    data[(i * imageData.width + j) * 4 + 0] = data[(i * imageData.width + j) * 4 + 1] = data[(i * imageData.width + j) * 4 + 2] = (data[(i * imageData.width + j) * 4 + 0] + data[(i * imageData.width + j) * 4 + 1] + data[(i * imageData.width + j) * 4 + 2])/3
                    

                }
            }  
            
            ctx.putImageData(imageData,0,0)          
            //将修改过imageData对象  绘制到canvas 上
        }
    ```

#### video操作

- drawImage 逐帧绘制 video

    ```js
        //滤镜处理
        let c = document.querySelector('canvas')
        let ctx = c.getContext('2d')
        let v = document.querySelector('video')
        
        requestAnimationFrame(next)
        function next(){
            ctx.drawImage(v,0,0,320,176)    //绘制video一次

            let imageData = ctx.getImageData(0,0,320,176)   
            let data = imageData.data;
            let W = imageData.width;
            let H = imageData.height;
            for(let r = 0; r < H; r++){
                for(let l = 0; l < W; l++){ //黑白处理
                    data[(r * W + l)*4 + 0] = data[(r * W + l)*4 + 1] = data[(r * W + l)*4 + 2] = (data[(r * W + l)*4 + 0] + data[(r * W + l)*4 + 0] + data[(r * W + l)*4 + 0]) / 3
                }
            }

            ctx.putImageData(imageData,0,0) //绘图
            requestAnimationFrame(next)
        }
    ```
#### 上传服务器  

- let str = ctx.toDataURL()  上传base64

    ```js
        $('#uplo').click(function(){    //上传
            let str = c.toDataURL()
            $.ajax('./upload',{
                method:'POST',
                data:{
                    str
                },
                success(data){
                    console.log(data)
                },
                error(err){
                    console.log(err)
                }
            })
        })
    ```

    ```js
    if(pathname == '/upload'){      //接受上传
        let arr = []
        req.on('data',(chunk)=>{
            arr.push(chunk)
        })
        req.on('end',()=>{
            let data = querystring.parse(Buffer.concat(arr).toString())
            let img = data.str;
            fs.writeFile('./upload/abcd.png',img.replace(/^data:[^,]+base64,/,''),'base64',(err)=>{
                if(err){
                    console.log('上传错误')
                } else {
                    res.end('ok 上传成功')
                }
            })
        })
    ```

- 设置http头 下载文件

    ```html
    <form action="./download" method="POST">
        <button id="downlo">download</button>
    </form>
    ```

    ```js
    if(pathname == '/download'){ //下载
        let rs = fs.createReadStream('./upload/abcd.png')
        rs.on('error',()=>{
            console.log('读取失败')
            res.end('下载失败')
        })
        res.setHeader('Content-Disposition', 'attachment; filename=download.png')
                        //返回下载图
        rs.pipe(res)
    } 
    ```

### 对图像操作

属性 | 作用
-|-
createPattern() | 设置图形重复
clip()  | 裁剪去掉超出范围的部分
isPointInPath() | 判断点是否在路径上(包含闭合内部分) 返回 boolean
scale() | 缩放 可叠加，对后面绘制的图形影响 rect 的四个参数都倍增
rotate() | 旋转 对后面的绘图进行影响
translate() | 更新画布的0,0点  影响后面的绘制
transform() | 3d 综合变换
setTransform() |
drawImage() | 向画布绘制图像、视频、画布(dom) 通过传参裁剪来绘制一部分
globalCompositeOperation | 重叠部分Z-index  source-over/destination-over
save() 保存当前环境的状态
restore() | 返回 之前保存过得路径状态和属性

 > save 保存  后resotre 恢复  尽量多用

### 画弧

- arc

    ```js
        let c = document.querySelector('canvas')
        let ctx = c.getContext('2d')
        ctx.moveTo(400,300)
        ctx.lineTo(550,300)
        ctx.arc(400,300,150,0, d2a(90),false)
        /*
            圆点
            半径
            起始弧度
            是否逆时针

            -- 0度在右
        */
        ctx.closePath()
        ctx.stroke()

        function d2a(d){
            return d/180 * Math.PI
        }
    ```

## canvas transform

- canvas 支持3中transform

    ```js
    //ctx.rotate()  旋转        先旋转在画图 
    /*
        旋转以  canvas 左上角为圆点进行旋转
    */


    //ctx.translate 平移
    //ctx.scale()   缩放

    let cs = document.querySelector('canvas')
    let ctx = cs.getContext('2d')
    let r = 0;
    let r2 = 0;
    requestAnimationFrame(next)
    function next(){
        ctx.clearRect(0,0,cs.width,cs.height); //清屏

        ctx.save()  // translate 属性会叠加  save 没有translate的环境
        ctx.beginPath()
        ctx.translate(200,150)   //图形  100,100  
        ctx.rotate(r)              //旋转
        ctx.strokeRect(-100,-50,200,100)    //先操作 最后绘图
        /*
            因为 canvas 以canvas左上角 为原点进行旋转  
            要使图形   以自身中心旋转    则将图形中心移至  canvas左上角
        */
        ctx.restore()   //将环境恢复为 没有translate的

        ctx.beginPath()
        ctx.save()
        ctx.translate(50 + 300, 100 + 50)
        ctx.rotate(r2)
        ctx.fillRect(-50,-50,100,100)
        ctx.restore()

        
        r += Math.PI / 180;
        r2 -= Math.PI /180;
        requestAnimationFrame(next)
    }
    ```

### save resolve

- save保存状态 resolve 恢复保存的状态


## canvas动画

- canvas动画 requestAnimationFrame()


    ```js
        let canvas = document.querySelector('canvas')
        let ctx = canvas.getContext('2d')
        let x = 0,
            y = 0;
        ctx.beginPath();
        ctx.strokeStyle='green'
        ctx.strokeRect(x,y,20,20);
        requestAnimationFrame(next);    //获取合适动画帧
        function next(){
            ctx.clearRect(0,0,320,500)  //清空画板
            if(x < 300 && y < 480 && y !=480){
                x += 0.5
            } else if(x == 300 && y < 480){
                y += 0.5
            } 
            ctx.strokeRect(x,y,20,20)   //重新画
            requestAnimationFrame(next)
        }

    ```

## 图片操作

- drawImage

    ```js
     let c = document.querySelector('canvas')
        let ctx = c.getContext('2d')
        let oImg = new Image()
        oImg.src = './6.jpg'
        oImg.onload = ()=>{
            ctx.drawImage(oImg,
                223, 0, 130, 130,
                100,100,300,300
            )
        }
        /*
            ctx.drasImage(  截取图片资源绘制到canvas
                oImg,               base64、 video 、 Img对象
                sx, sy, sw, sh,     原图x,y,w,h
                dx, dy, dw, dh      绘制到canvas上时的 x,y,w,h
            )
        */
    ```


## canvas事件

- 通过e.clientX 判断点击到canvas的那个区域 执行不同的回调

    ```js
        let canvas = document.querySelector('canvas')
        let ctx = canvas.getContext('2d')
        ctx.fillStyle = 'blue'
        ctx.fillRect(50,50,100,100)

        canvas.onmousemove = function(e){
            // console.log(e)
            let mouseX = e.clientX,
                mouseY = e.clientY;
                if(mouseX > 50  && mouseY > 50 && mouseX < 150 && mouseY <150){
                    console.log('in')
                    ctx.beginPath()
                    ctx.clearRect(0,0,320,500)
                    ctx.fillStyle = 'red'
                    ctx.fillRect(50,50,100,100)
                } else {
                    ctx.beginPath()
                    ctx.clearRect(0,0,320,500)
                    ctx.fillStyle = 'blue'
                    ctx.fillRect(50,50,100,100)
                }
        }
    ```