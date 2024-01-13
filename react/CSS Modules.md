# [CSS Models](http://www.ruanyifeng.com/blog/2016/06/css_modules.html)

- CSS MOdels 模块化 CSS 把css 写在js中， 并且能生成变量

## Demo

- app.js

```js
import React from 'react';
import style from './app.css';

export default ()=>{
    return (        //页面引入也是 哈希字符串
      <div>
        <h1 className = {style.title}>局部变量</h1>
        <h1 className='title'>全局变量</h1>
        <h1 className={style.combineLocal}>混合局部</h1>
        {/* composes 不能够 用在global上 */}

        <h1 className={style.combineModel}>combineModel</h1>
        <h1 className={style.customValue}>customValue</h1>
      </div>
        
    )
}
```

- app.css

```css
/* 自定义变量 */
@value oBlue: #0c77f8;


.title {
  color: red;
}

/* 全局变量 */
:global(.title){
  color: rgb(120, 226, 110);
}
/* 混合变量 */
.combineLocal{
  composes: title;
  background: #eee;
}
/* 引入其他文件 */
.combineModel{
  composes: oTitle from './another.css';
  background:rgb(120, 226, 110);
}
/* 使用自定义value */
.customValue{
  color: oBlue;
}
```

- another.css

```css
.oTitle{
    color: blueviolet;
}

```