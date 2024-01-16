export interface IMyHeaderProp{
    title: string;
    callback: Function
}


export default function MyHeader({title, callback}: IMyHeaderProp){
    return (<>
        <div className="my-header">
            <h1>{title}</h1>
            <SearchBox callback={callback}></SearchBox>
            {/* <img src="/test.jpg" alt="" className="icon" /> */}
        </div>
    </>)
}


export interface ISearchBoxProp {
    callback: Function;
}
export function SearchBox({callback}: ISearchBoxProp) {
    let state={
        inpVal :''
    }
    function handelClick(){
        callback && callback();
    }
    return (<>
    <div className="search-box">
        <input type="text" className="search-input" value={state.inpVal}/>
        <button className="search-btn" onClick={()=>{handelClick()}}>search</button>
    </div>
    
    </>)
}