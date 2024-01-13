import React from 'react';
import style from './App.module.css';

export function MyImg () { //创建函数式组件
  return (
    <img src="/test.jpg" alt="" />
  )
}


class HeaderComp extends React.Component{ //需要继承 实现 类组建
  private myCount: number = 0;
  public state: Readonly<{}> = {
    myCount: this.myCount
  };
  constructor(props: {} | Readonly<{}>){
    super(props);
  }
  private clickHandel(e:any) {
    this.myCount ++;
    this.setState({myCount: this.myCount})
    console.log(this.myCount)
  }
  
  render(): React.ReactNode {
    return(<>
      <div>{this.myCount}</div>
      <button onClick={(e) => this.clickHandel(e)}>Add </button>
    </>)
  }
}

function App() {
  const handelClick = function(e: any, msg: string) {
    console.log(e, msg)
  }
  return(<>
    <button onClick={(e)=> handelClick(e, 'abc')}>click me</button>
    <HeaderComp></HeaderComp>
  </>)
}

export default App;
