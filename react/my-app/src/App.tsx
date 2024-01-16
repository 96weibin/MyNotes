import React, { useState } from 'react';
import Morney from './components/Morney';

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
}

export default App;
