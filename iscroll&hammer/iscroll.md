# iScroll

## 基础用法

- 页面引入

    ```js
    //1. 页面引入 scroll.js
    //2. new IScroll  
    /*
        参数1 可以是 CSS选择器  或者  dom对象
        参数2 为{}   即设置 IScroll.option的值
    */
    // 3. wrapprer 的第一个子元素  实现拖拽功能


        let scroll = new IScroll('.wrapper',{
        //   bounce:true,
          bounceTime: 200,
          scrollY: true,
          scrollX: true,
          freeScroll:true,
          /*...*/
        })
        console.log(scroll.options)
    ```

## 常用参数

- 常用参数

    参数 | 取值 | 功能
    -|-|-
    bounce | boolean | 拖拽过界 true允许拖过界
    bounceTime | number | 过界回弹时间
    scrollX | boolean | 是否允许横向拖拽 默认false
    scrollY | boolean | 是否允许纵向拖拽 默认true
    startX | number | 起始X
    startY | number | 起始Y
    freeScroll | boolean | 是否允许自由拖拽 scrollX为true 才生效
    directionLockThreshold | number | 方向锁定判定阈值
    disableMouse | boolen | 禁用鼠标 pc
    disableTouch | boolean | 禁用鼠标 移动
    disablePointer | boolean | 禁用鼠标 兼容
    invertWheelDirection | | 反转鼠标滚轮
    momentum | boolean | 是否开启物理引擎<br>true 提高效果 降低性能，<br> false 降低效果 提升性能
    probeType | 1,2,3 | 返回数据等级 <br> 1 : 定时轮询 <br> 2 ：实时监测拖拽 <br> 3 : 实时检测拖拽 + 实时监测运动本身 && 抛弃了transition

## 方法

- 配合probeType 监听 scroll对象属性变化

    事件 | 功能
    -|-
    beforeScrollStart | 
    scrollStart | 
    scroll | 
    scrollEnd | 
    scrollCancel | 
    zoomStart | 
    zoomEnd |

    ```js

    ```


- 定格scroll scroll.disable()
   
