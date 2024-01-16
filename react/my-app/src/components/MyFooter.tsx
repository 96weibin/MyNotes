import React, { ReactElement } from "react";


interface IFooterProps {
    title:  string;
    msg?: string;
    children: ReactElement
}
export class MyFooter extends React.Component<IFooterProps>{
    // private msg: string = "my footer"
    static defaultProps:IFooterProps = {
        title: 'my title',
        msg: 'my msg',
        children: <></>
    };
    
    constructor(props: IFooterProps | Readonly<IFooterProps>){
        super(props)
        console.log(props)
    }
   

    public state: any = {
        count: 1

    }
    render(): React.ReactNode {
        return(<>

        <h1>{this.props.msg}</h1>
        <h2>{this.props.title}</h2>
        <h3>msg: {this.props.msg}</h3>
        <h4>{this.state.count}</h4>
        <button onClick={(e)=>this.handelClick(e)}>click footer</button>

        <div>插槽 children 
            {this.props.children}
        </div>
        </>)
    }

    private handelClick(e: any) {
        console.log(e);
        this.setState({count: ++(this.state.count)},()=>{
            console.log(this.state.count)
        })
    }
}
