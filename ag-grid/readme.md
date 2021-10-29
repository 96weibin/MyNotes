# ag-grid

# 页面引入使用demo

- 引入js 和 css 直接使用

    ```html
        <script src="http://www.itxst.com/package/ag-grid/ag-grid-community.js"></script>
        <link href="http://www.itxst.com/package/ag-grid/styles/ag-grid.css" rel="stylesheet"/>
    ```

    ```html
    <div id="myGrid" style="width: 100%; height: 500px;" class="ag-theme-balham"></div>
    <button onclick="updateGrid3()">updateGrid3</button>
    <button onclick="deleteRow()">delete</button>
    <button onclick="changeSelect">select</button>
    <script>
            let $ = document.querySelector.bind(document);
            let myGridEl = $('#myGrid');
            var columnDefs = [
                { 
                    headerName: '姓名1',         //列标题名
                    field: 'name',              //data的属性名
                    'pinned': 'left',           
                    width:120,
                    filter:'agTextColumnFilter',
                    headerCheckboxSelection:true,       //表头  checkbox 可选
                    checkboxSelection:true,             //行    chackbox 可选

                 },
                { headerName: '性别', field: 'sex' },
                { headerName: '年龄', field: 'age' },
                { headerName: '籍贯', field: 'jg' },
                { headerName: '省份', field: 'sf' },
                { headerName: '地址', field: 'dz' },
            ];
            var rowData = [
                { name: '张三', sex: '男', age: '100', 'jg': '中国', 'sf': '浙江', 'dz': '杭州市古墩路1号' },
                { name: '李四', sex: '女', age: '5', 'jg': '中国', 'sf': '浙江', 'dz': '杭州市古墩路12号' },
                { name: '王五', sex: '女', age: '20', 'jg': '中国', 'sf': '浙江', 'dz': '杭州市古墩路31号' }
            ];
            var topRows=[
                { name: '顶部合计行', sex: 'X', age: '15', 'jg': '中国', 'sf': '顶部1', 'dz': '杭州市文一西路' } 
            ];
            var botRows=[
                { name: '置底行1', sex: 'X', age: '15', 'jg': '中国', 'sf': '顶部1', 'dz': '杭州市文一西路' },
                { name: '置底行2', sex: 'X', age: '15', 'jg': '中国', 'sf': '顶部2', 'dz': '杭州市文一西路' }
            ];


            let gridOptions = {
                    rowHeight: 30,          //行高
                    columnDefs,             //表头
                    rowData,                //数据

                    //下面为一组
                    rowSelection:'multiple',    //点击 checkbox 多选, 默认single
                    rowMultiSelectWithClick:true, //点击行 多选
                    rowDeselection:true,          //点击行 取消选中

                    onGridReady(){              
                        gridOptions.api.sizeColumnsToFit();
                    },
                    defaultColDef: {
                        editable: true,         //单元表格是否可编辑
                        enableRowGroup: true,   //
                        enablePivot: true,
                        enableValue: true,
                        sortable: true,     //排序
                        resizable: true,    //resize
                        filter: true        //筛选
                    },
                    
                    // 分页  下面连个属性 也是一组
                    pagination: true,  //开启分页（前端分页）
                    paginationAutoPageSize: true, //根据网页高度自动分页（前端分页）
                    
                    pinnedTopRowData:topRows, //顶部合计行
                    pinnedBottomRowData:botRows ,//底部合计行
                    //**************设置置顶行样式**********
                    getRowStyle: function (params) { 
                            if (params.node.rowPinned) {   
                                    return {'font-weight': 'bold','color':'red'};
                    }
                },       
            }
            new agGrid.Grid(myGridEl,gridOptions);

        // 更新数据
        function updateGrid3 () {
            let rowObj = gridOptions.api.getRowNode(2);  //获取第三行 的对象
            let newRow =  { name: '三行', sex: '男', age: '35', 'jg': '中国', 'sf': '浙江', 'dz': '杭州市古墩路12号' };
            rowObj.setData(newRow) 
            //gridOptions.api.updateRowData({add : newRow, addIndex : 1})
            //在第二行新增
        }
        //删除选中行
        function deleteRow(){
            let selectRows = gridOptions.api.getSelectedRows();     //获取选中行
            gridOptions.api.updateRowData({remove: selectRows})  //删除行
        }

        function changeSelect (){
            //集中表格选择情况
            gridOptions.api.selectAll()                 //全选
            gridOptions.api.deselectAll()               //反全选
            gridOptions.api.selectAllFiltered();        //条件全选
            gridOptions.api.deselectAllFiltered();      //条件反全选
        }
    ```

## demo 

- [多表头](http://www.itxst.com/ag-grid/7r7zbbfu.html)


## gridOptions

- 表格 Options
  
    prop | 功能  | 默认 | demo 
    -|-|-|-
    defaultColDef | 默认列设置 | {} | 
    columenDefs | 列设置 |  |
    rowData | 数据 | |
    floatingFilter | 显示筛选器 | false | boolean
    pagination | 开启分页 | false | boolean
    paginationAutoPageSize | 分局高度自动分页 | false | boolean
    editType | 编辑类型 | | fullRow 点击一个单元格，一整行的edit 都触发
    rowSelection | 选中类型 | single | multiple 多选
    rowHeight | 行高 | 25 | px
    suppressDragLeaveHidesColumns | 阻止拖拽离开后隐藏 | false | boolean 拖拽排序时需要禁止
    


- 表格 事件
  
    fun | 功能 | 常用设置
    -|-|-
    onGridReady | ready | gridOptions.api.sizeColumnsToFit() 调整表格合适大小
    onRowEditingStopped | 整行编辑事件完成 | 配合 editType: fullRow 使用
    onCellEditingStopped | 单元格编辑事件完成 | 
    onRowClicked | 行点击事件| 
    onCellClicked | 单元格点击事件 | 
    onCellDoubleClicked | 单元格双击事件 |

    
### API

- xxx

    api | 功能 | note
    -|-|-
    setRowData() | 重渲染表格 | [{}]
    getSelectedRows() | 获取选中行node | 
    getRowNode() | 获取RowNode | id:string
    updateRowData() | 更新表格 | {'action',[{}]}, add, remove,update,, 
    selectAll() | 全选  | 
    deselectAll() | 反全选 | 
    selectAllFiltered() | 条件全选 | 
    deselectAllFiltered() | 条件反全选 | 
    sizeColumnsToFit() | 调整大小 | 
    setColumnDefs() | 设置列 | 
    forEachNode() | 遍历行对象 | node,index
    refreshCells() | 刷新表格 | {force:true}
    getFocusedCell() | 聚焦的单元格 | 
    setFocusedCell() | 聚焦单元格 | index, 'name'
    clearFocusedCell() | 取消聚焦 |
    tabToNextCell() | 聚焦下一个单元格 | 
    tabToPreviousCell() | 聚焦前一个单元格 | 

> note: updateRowData is deprecated, use applyTransaction instead

#### RowNode

- rowNode 上的方法

    方法 | 功能 | note
    -|-|-
    setData | 设置新Data | 


### defaultColDef

设置各列之间相同的属性

- prop 

    prop | 功能 | 默认 | demo 
    -|-|-|-
    resizable | 调整宽度 | false | boolean
    lockPosition | 拖动列 | false | boolean
    filter | 筛选 | false | true  开启所有选择器
    -|-|-| agNumberColumnFilter 开启数字了行选择器
    -|-|-| agTextColumnFilter 开启字符串选择器
    -|-|-| agDatecolumnFilter 开启时间选择器


### colmDefs

设置各列之间不同的属性

- 设置表头
  
    prop | 功能 | 默认 | note
    -|-|-|-
    headerName | 列标题 | | 
    field | 根据field 填充 rowdata.field | |
    valeFormatter | 过滤函数 | | TODO 
    pinned | 固定位置 | | right, left
    filter | 过滤器 | | agNumberColumnFilter, agTextColumnFilter, agDateColumnFilter
    width, minWidth,maxWidth | 列宽 |  |
    sort | asc排序 | asc 顺序, desc倒叙 | 
    sortable | 是否可以排序 | false | boolean
    multiSortKey | 设置多列排序key | | 'ctrl' 
    resizeable | 拖动大小 | boolean |
    cellRender | cell表面的html渲染 | 
    valueFormatter | cell渲染text | 只渲染text 用这个会更好
    cellEditor | 编辑 | | agSelectCellEditor 通过select编辑
    cellEditorParams | 双击后渲染 | | {values:['male','femal']}
    cellEditor|-|-| agLargeTextCellEditor 通过文本框编辑
    headerCheckboxSelection | 表头checkbox | false | boolean
    checkboxSelection | 行checkbox | flase | boolean
    suppressMovable | 阻止移动 | false | boolean
    lockPosition | | 
    lockVisible | 阻止Colum 拖拽 | 
    lockPinned | 阻止pinned  | boolean, 'left', 'right'
    colSpan | 占几个col | | num
    children | 定义分组 | | [{}]
    openByDefault | 默认展开分组 | | boolean
    marryChildren | child拖拽到不同分组 | boolean
    suppressColumnsToolPanel | 不被列显示panel控制 | boolean
    

## 编辑单元格

- select 编辑

    ```js
    { 
        headerName: '性别', 
        field: 'sex',
        cellEditor:"agSelectCellEditor",
        cellEditorParams:{
            values:['男','女']  //内部foreach循环, 需是数组类型
        }
    },
    ```
    
- 文本编辑
  
    ```js
    {
        headerName: '年龄', 
        field: 'age', 
        cellEditor:'agLargeTextCellEditor', cellEditorParams:{
            maxLength:'30', //输入文本length
            cols:'50',      //textarea col row
            rows:'6'
        }
    },
    ```