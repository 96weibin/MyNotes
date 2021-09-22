# GoJS

- JS 交互图标库 ， canvas

## 创建

1. 直接html引入,通过GraphObject 实现

    ```html
        <script src="./go-debug.js"></script>

        <div id="box" style="width:400px; height:150px; background-color: #DAE4E4;"></div>
        <!-- 容器需要通过CSS设值样式 -->
        <script>
            //获取容器
            var $ = go.GraphObject.make;  //go.GraphObject 非dom操作耗费性能少
            var myDiagram = $(go.Diagram, 'box', {
            "undoManager.isEnabled": true //undoManager
            })


            //通过  nodeTemplate 定义表格, model提供数据
            myDiagram.nodeTemplate = $(
                go.Node,
                "Auto",
                $(go.Shape,"RoundedRectangle",new go.Binding('fill',"color")),
                $(go.TextBlock, {margin:3}, new go.Binding('text','key'))
            ),
        
            myDiagram.model = new go.GraphLinksModel(  //$(go.Model).nodeDataArray
            [
                { key: "Alpha", color: "lightblue" },
                { key: "Beta", color: "orange" },
                { key: "Gamma", color: "lightgreen" },
                { key: "Delta", color: "pink" }
            ],
            [
                { from: "Alpha", to: "Beta" },
                { from: "Alpha", to: "Gamma" },
                { from: "Beta", to: "Beta" },
                { from: "Gamma", to: "Delta" },
                { from: "Delta", to: "Alpha" }
            ]
            )
        </script>
    ···

2. import 通过 同步线性代码实现  out
    
    - node add... 

    ```ts
    import * as go from 'gojs'; 

    export class Diagram{
        private diagramEle:HTMLDivElement;      //div 
        constructor(){}
        attached() {
            this.initDiagram();
        
        }
        initDiagram(){

            let $go = go.GraphObject.make;
                let myDiagram = $go(go.Diagram, this.diagramEle,{
                    "undoManager.isEnabled": true
                });
                let node = new go.Node(go.Panel.Auto);      //go.node
                let shape = new go.Shape();                 //go.shap
                shape.figure = 'RoundedRectangle';
                shape.fill = 'pink';
                node.add(shape);
                let textblock = new go.TextBlock()          //go.textblock
                textblock.text = 'Hello';
                node.add(textblock);
                myDiagram.add(node);
        }
    }
    ```
3. import 通过GraphObject add

    ```ts
    import * as go from 'gojs';

    export class Diagram{
        private diagramEle:HTMLDivElement;
        constructor(){}
        attached() {
            this.initDiagram();
        
        }
        initDiagram(){

            let $go = go.GraphObject.make;
            let myDiagram = $go(go.Diagram, this.diagramEle,{
                "undoManager.isEnabled": true
            });
            
            myDiagram.add(
            $go(
                go.Node,
                go.Panel.Auto,
                $go(go.Shape,
                {
                figure:"RoundedRectangle",
                fill:'pink'
                }),
                $go(go.TextBlock, {
                    text:"TextBlock",
                })
            )
        )
    }

    ```

4. 使用模板 及 绑定数据

    ```ts
    //A， B 两个节点
    let nodeDataArray = [
      {key:'A'},
      {key:'B'}
    ]
    //两条线
    let linkDataArray = [
      {from:'A', to:'B'},
      {from:'B', to:'B'}
    ]
    //节点 模板
    myDiagram.nodeTemplate = $go(go.Node,
      'Auto',
      $go(go.Shape,{figure:'RoundedRectangle',fill:'white'}),
      //绑定数据, 字段 ， key , renderHandl
      $go(go.TextBlock,{margin : 5},new go.Binding('text','key',(key)=>{return key + 'hhhhh'}));
      )
    //创建图线实例
    myDiagram.model = new go.GraphLinksModel(nodeDataArray,linkDataArray)
    ```


5. 绑定数据

    ```ts
    ```

## GraphObject

- gojs 最上层的父类，派生出 panel、part等子类
- make 方法，创建并返回实例



## Shape

## TextBlock

## Picture

## Panel

## nodeTemplate

- $(Nodetype, type?, css?, content) 可嵌套

    node type | feature
    -|-
    Shape | 带有颜色预设定或自定义的几何图形
    TextBlock | 各种字体显示及编辑
    Picture | 照片
    Panel | 集合容器


1. TextBlock

    ```ts
        let $ = go.GraphObject.make;
        let myDiagram = $(go.Diagram, 'box')
        myDiagram.nodeTemplate = $(go.Node,'default val',$(go.TextBlock,new go.Binding('text','key'))) 
        //go.Binding text类型绑定数据 key,
        
        myDiagram.model = new go.GraphLinksModel(
            [
            { key: "Alpha"},
            { key: "Beta"},
            { key: "Gamma"},
            { key: "Delta"},
            {}  //空对象也会显示  array 的index会被解析为key 若绑定为其他且未找到会显示'default val '
        ])
    ```
2. mix Node

    ```ts
        let $ = go.GraphObject.make;
        let myDiagram = $(go.Diagram, 'box');
        myDiagram.nodeTemplate =
        $(go.Node, "Horizontal",
            { background: "#44CCFF" },
            $(go.Picture,
                { margin: 10, width: 50, height: 50, background: "red" },
                new go.Binding("source")
            ),
            $(go.TextBlock,
                "Default Text", 
                { margin: 12, stroke: "white", font: "bold 16px sans-serif" },
                new go.Binding("text", "name")
            )
        );
        var model = $(go.Model);
        model.nodeDataArray =
        [ 
        { name: "Don Meow", source: "/images/learn/cat1.png" },
        { name: "Copricat", source: "/images/learn/cat2.png" },
        { name: "Demeter",  source: "/images/learn/cat3.png" },
        { /* Empty node data */  }
        ];
        myDiagram.model = model;
    ```


## GraphlinksModel

- 包含 nodeDataArray 和 linkDataArray 分别是数据和连线的对象

- 连线对象有两种

1. link  和 tree


## 