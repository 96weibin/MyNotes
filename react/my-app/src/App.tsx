import React, { useEffect, useState } from 'react';

function App() {
  let [count, setCount] = useState(0);
  let [gridData, setGridData] = useState([]);

  useEffect(()=>{
    console.log('useEffect no DependencyList')
  })  //没有 dependency list 每次渲染后会执行一次， 


  useEffect(()=> {
    console.log("get data...")
  },[]) // 只会在组件挂载后执行

  useEffect(() => {
    document.title = `点击了${count} 次`;
    const sayHi = setInterval(()=>{
      console.log("hello")
    }, 1000)
    return () => {
      clearInterval(sayHi);  //返回清理函数
    }
  }, [count]) // 渲染结束 且 count值 不一样时调用
  

  return(<>
    <div>
      count: {count}
      <button onClick={()=>{setCount(++count)}}>click</button>
      <button onClick={()=>console.log("normal click")}>click2</button>
    </div>
  </>)
}

export default App;
