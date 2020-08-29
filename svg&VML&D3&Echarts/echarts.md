# echarts

- [官网](https://echarts.apache.org/zh/index.html)
- 页面引入 js
- echarts.init(dom)
- option ={....}        
- chart.setOption(option)

- [更多实例](https://echarts.apache.org/examples/zh/index.html)

## 柱状图 

- xAxis yAxis 

    ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style>
                #main{
                    width: 800px;
                    height: 600px;
                    border: solid;
                    margin: 10px auto;
                }
            </style>
        </head>
        <body>
            <div id="main"></div>
            <script src="../js/echarts.min.js"></script>
            <script>
                let $ = document.querySelectorAll.bind(document);
                


                let myChart = echarts.init($('#main')[0]);  //初始化
                let option = {        //设置参数
                    title: {
                        text: '北京人口调查',    //主标题
                        subtext:'2020年度 单位：万人',        //副标题
                        x :'center'
                    },
                    tooltip: {},                //提示信息
                    legend: {                   //图例
                        data:['男','女'],
                        right:0,
                        top:'50%',
                        orient:'vertical'
                    },
                    xAxis: [                    //X轴
                        {
                            type:'category',  //分类轴
                            data : ["1月","2月","3月","4月","5月","6月"]

                        }
                    ],
                    yAxis: [                    //Y轴 
                        {
                            type:'value'        //数值轴
                        }
                        
                    ],
                    series: [               //与图例对应的 值
                        {
                        name: '男',
                        type: 'bar',
                        data: [5, 20, 36, 10, 10, 20]
                        },
                        {
                        name: '女',
                        type: 'bar',
                        data: [6, 18, 3, 20, 17, 25]
                        },

                    ]

                }
                myChart.setOption(option)     //设置参数
            </script>
        </body>
        </html>
    ```

## 饼图

- pie

    ```js
        let $ = document.querySelector.bind(document);
        let chart = echarts.init($('.box'));
        let option = {
            title:{
                text:'美国大选投票',
                subtext:'2020年度'
            },
            series:[
                {
                    name:'选票比例',
                    type:'pie',             //饼图
                    radius:'40%',           //半径
                    // radius:['40%','60%']  环形  可以实现套在一起的饼图   
                    center:['30%','50%'],   //圆心
                    data:[
                        {
                            name:'特朗普',
                            value : 500
                        },
                        {
                            name:'拜登',
                            value : 6000
                        },
                        {
                            name:'希拉里',
                            value: 4000
                        }
                    ]
                },
                {
                    name:'年龄比例',
                    type:'pie',               
                    radius:'40%',
                    center:['70%','50%'],
                    data:[
                        {
                            name:'特朗普',
                            value : 500
                        },
                        {
                            name:'拜登',
                            value : 6000
                        },
                        {
                            name:'希拉里',
                            value: 4000
                        }
                    ]
                }
            ]
        }
        chart.setOption(option)
    ```

## 雷达图

- radar

    ```js
        let $ = document.querySelector.bind(document)
        let chart = echarts.init($('.container'));
        let option = {
            title:{
                text:'角色能力图',
                subtext:'鬼剑士'
            },
            legend:{
                data:[
                    '狂战士',
                    '鬼泣',
                    '阿修罗',
                    '剑魂'
                ]
            },
            radar:{
                name:{
                    textStyle:{
                        color: '#fff',
                        backgroundColor: '#999',
                        borderRadius: 3,
                        padding: [3, 5]
                    }
                },
                indicator:[
                    { name:'攻击', max:100 },
                    { name:'防御', max:100 },
                    { name:'速度', max:100 },
                    { name:'控制', max:100 },
                    { name:'辅助', max:100 },

                ]

            },
            series:[
                {
                    name:'鬼剑士职业比较',
                    type:'radar',
                    data:[

                        {
                            name: '狂战士',
                            value:[100,60,80,10,20]
                        },
                        {
                            name:'剑魂',
                            value:[80, 50, 90, 40, 40]
                        },
                        {
                            name:'鬼泣',
                            value:[70, 40, 69, 60, 50]
                        },
                        {
                            name:'阿修罗',
                            value:[70, 90, 60, 80, 50]
                        }

                    ]
                }
            ]
        }
        
        chart.setOption(option)
    ```
## js操作

- 