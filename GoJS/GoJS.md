# GoJS

- JS 交互图标库

## Ease demol

- 直接html引入

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

## GraphObject

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





