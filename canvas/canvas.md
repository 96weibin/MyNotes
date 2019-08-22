# CANVAS

    IE9+画布,DOM对象，通过获取其上下文，设置笔触设置路径绘制、填充图形，imageData对图片进行逐像素编辑。模糊、重复、

## API

### 笔触  （需要stroke）

方法 | 描述 | 传参
-|-|-
beginPath() | 开始/重置一条路径 | 坐标
moveTo() | 将笔移到指定位置 | 坐标
lineTo() | 添加新点，创建连线 | 坐标
closePath() | 直线连接头尾位置 | 坐标
rect | 绘制矩形 | 左上右下
fill() | 填充路径(未闭合 自动闭合首位) | ——
stroke() | 描边路径 | ——
quadraticCurveTo() | 创建二次贝塞尔曲线 | 控制点，终点
bezierCurTo() | 创建三次贝塞尔曲线 | 控制点，控制点，终点
arc() | 创建弧/曲线 | 圆点坐标，弧度(0~2*Math.PI) 顺时针
arcTo() | 创建两点间的圆弧 | 起点坐标，终点坐标，半径

属性 | 描述 | 取值
-|-|-
fillStyle | 填充颜色 仅对下一次绘制生效
globalAlpha | 透明度仅影响 后面的透明度
strockeStyle | 笔的颜色
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

方法 | 描述 | 传参
-|-|-
createImageData() | 创建空白ImageData对象(data.length 对图片逐像素编辑rgba)
getImageData() | 获取 ImageData对象
putImageData() | 把图像数据 放到画布上  对象,坐标

属性 | 描述
-|-
width | 返回 ImageData对象的宽度
height | 返回ImageData对象高度
data | 返回ImageData对象数据

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
