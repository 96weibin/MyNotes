# Recact

- 声明式， 构建用户界面的JS库，
- 虚拟dom
- 单向数据流

## `问题`

- 组件的逻辑 代码如何区分， 是写在里面 还是外边， 怎么嵌套


## `搭建本地开发环境`

```shell
$ px create-react-app my-app --template cra-template-typescript
```

## JSX

```jsx
function App() {
  const msg = 'click me';
  const clickHandel = function(e: React.MouseEvent<HTMLDivElement>){  //handel
    console.log(e)
  }
  const arr = [{name:'weibin', age: 11},{name: 'lulu', age: 18}]; //元数据
  //虚拟dom片段
  const jsxArr = arr.map((x, i)=> (<div key={x.name} id={x.name}>   
    姓名： {x.name} 
    <br />
    年龄：{x.age}
    {i%2=== 0? '偶数': '奇数'}
  </div>))

  const element1 = React.createElement('a', {className: 'myA',href:'#'}, 'clickme');
  const element2 = <a href="#">click me</a>; //等同于。React.createElement();
  console.log(element1, element2)

  return (      
    <div className="App">
      <h2>hello react</h2>
      
      <div style={{color: 'blue', fontSize: '48px'}} onClick={clickHandel}>{msg}</div>
      {/* 注释 */}
      <div className={style.redBlock}></div>
      <div className="redblock">
        {jsxArr}
      </div>
      {element1}
      <MyImg></MyImg>
    </div>
  );
}
```

## Compoment

- 类组件

```js
class HeaderComp extends React.Component{ //需要继承 实现 类组建
  
  render(): React.ReactNode {
    return(<>comp</>)
  }
}
```

- 函数组件