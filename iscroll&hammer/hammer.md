# hammerjs 

- 手势操作库[https://github.com/hammerjs/hammer.js](https://github.com/hammerjs/hammer.js)

## 使用

```js
    window.onload = ()=>{
        let box = document.querySelector('.box')
        let hammer = new Hammer(box);
        hammer.on('tap',()=>{
            console.log('tap')
        })
    }
```

## 事件

事件 | 功能
-|-
tap | 更灵敏的点击 1~250ms
press | 点击 250ms ~
swipe | 滑动 快速 300px/s>
swipeleft | 向左滑动
swiperight | 向右滑动
swipeup | 向上滑动
swipedown | 向下滑动
pan | 滑动 慢速
panleft | 向左滑动
panright | 向右滑动
panstart | 滑动开始
panmove | 滑动中
panend | 滑动结束
pancancel | 取消 滑动

- pan和swipe的区别

    >pan 类似拖拽实时反馈   swipe使用结果判断左右滑动 

## 手势

- 旋转手势

    ```js
        let box = document.querySelector('.box')
        let hammer = new Hammer(box);
        let config = hammer.get('rotate')
        config.set({enable:true})
        hammer.on('rotatemove',e=>{
            // alert(e.rotation)  旋转角度
            box.style.transform = `rotate(${e.rotation}deg)`
        })
    ```
18797897999
    事件 | 功能
    -|-
    rotatestart | 开始旋转
    rotatemove | 旋转中
    rotateend | 旋转结束

- 缩放手势

    ```js
        let box = document.querySelector('.box')
        let hammer = new Hammer(box);
        let config = hammer.get('pinch')
        config.set({enable:true})
        hammer.on('pinchmove',e=>{
            // alert(e.scale)
            box.style.transform = `scale(${e.scale})`
        })
    ```

    事件 | 功能
    -|-
    pinchstart | 开始缩放
    pinchmove | 缩放中
    pinchend | 缩放结束

## 细致的应用

- 更细致的应用  使用swipe单纯判断方向效果就没有那么好所以使用panstart panmove panend  e.center.x、e.center.y

- 类似原生touch写 拖拽 根据move时值与 start时的值 自行判断