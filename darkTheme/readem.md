# how to achieve dark theme

- 切换主题， 即 切换 html 的 calss
- 通过 css variable 的覆盖实现 修改整体 theme

```js
// 1. :root --  html选择器
// 2. css variable --xxx  通过 var(--xxx) 调用变量
// 3. 获取 system theme

let media = window.matchMedia("(prefers-color-scheme: dark)");
return media.matches ? 'dark' : 'light';
```

```css
/* variables */
:root{
  --main-background-color: #FFF;
  --main-color: #000;
  --main-border-color: #eee;
}

.dark-theme{
  --main-background-color: #000;
  --main-color: #FFF;
  --main-border-color: #eeeeee1a;
}
```


