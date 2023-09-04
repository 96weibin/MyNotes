import React, { useState } from 'react';
import { Switch, FormControlLabel, FormGroup } from '@material-ui/core';
import InputLabel from '@mui/material/InputLabel';
import './App.css';
import MenuItem from '@mui/material/MenuItem';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import { dark } from '@mui/material/styles/createPalette';

function App() {
  enum themes {
    default,
    dark,
    light,
  }
  // let listItems = options.map((o, i) => <MenuItem value={o.value} key={i}>{o.lable}</MenuItem>)



  const [theme, setTheme] = useState(getTheme());
  const [checked, setChecked] = useState(false);

  function getTheme(): string{
    let localTheme = localStorage.getItem('theme');
    if(localTheme != ''){
      return localTheme == 'dark' ? 'dark': 'light';
    } else {
      let media = window.matchMedia("(prefers-color-scheme: dark)");
      return media.matches ? 'dark' : 'light';
    }
  }

  const handelDarkTheme = ()=>{
    let newtheme = theme == 'dark' ? 'light': 'dark'
    setTheme(newtheme);
    localStorage.setItem('theme', newtheme);
  }

  return (
    <div className={`App ${theme == 'dark'? 'dark-theme': ''}`}>
      darkTheme
       <Switch
        checked={checked}
        name=''
        onChange={handelDarkTheme}
       ></Switch>
       <div className='box1'>哈哈哈哈哈</div>
    </div>
  );
}

export default App;
