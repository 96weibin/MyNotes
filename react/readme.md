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


### 组件传值

- 父组件

```tsx
function App() {
  let [dolor, setDolor] = useState(0);
  let [rmb, setRmb] = useState(0);

  const morneyTransformHandel = (type: string, value: number) => {
    switch (type) {
      case 'dolor':
        setDolor(value);
        setRmb(Number((value / 7).toFixed(2)))
        break;
      case 'rmb':
        setDolor(value * 7);
        setRmb(value)
        break;
      default:
        break;
    }
  }
  return(<>
  <h1>人民币《-》 美元</h1>
  <Morney title='人民币' value={rmb} morneyTransform={(value: number)=>morneyTransformHandel('rmb', value)}></Morney>
  <Morney title='美元' value={dolor} morneyTransform={(value: number)=>morneyTransformHandel('dolor', value)}></Morney>
  </>)
```

- 子组件

```tsx
export default function Morney({title, value, morneyTransform}: IMorneyProps){

    const onChangeHandel = (e: ChangeEvent<HTMLInputElement>)=>{

        //受控组建 对输入进行 filter
        let numVal = Number(e.target.value.split('').filter(x => !isNaN(Number(x))).join(''));
        morneyTransform(numVal)
    }

    return(<>
    <h2>{title}</h2>
    <input type="text" value={value} onChange={(e)=>onChangeHandel(e)}/>
    </>)
}

interface IMorneyProps {
    title: string,
    value: number,
    morneyTransform: Function
}
```

## 生命周期

- 生命周期。主要是对 类组件的钩子

钩子函数 | hoks | 作用
-|-|-
constructor | 1| 组件创建时执行一次
render | 3 | **必须** 
componentDidMount | | mounted 挂载 执行一次
componentWillUnmount | | 组件销毁时调用
componentDidUpdate | | 更新后调用

## Hoks