import { ChangeEvent } from "react"

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