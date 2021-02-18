# [layui](https://www.layui.com/doc/)

- 

## 引入

将layui文件夹放入项目中，引入js、css

```html
    <link rel="stylesheet" href="./layui/css/layui.css">
    <script src="./layui/layui.js"></script>
```

## 基础样式

1. 容器 **layui-container**

  容器 | 长度
  -|-
  layui-container | 两边留余地
  layui-container-fluid | 父级宽度100%

2. 栅格 layui-row 、 layui-col-md3
    > 与bootstrap相同12 超过12 换行

    ```html
    <div class="layui-container">
        <!-- 容器 -->
        <div class="layui-row layui-col-space4">
        <!-- 行   列边距4  列边距需要设置在行上-->
        <!-- 列边距通过 col 添加 span 挤压实现 1~30px-->
        <div class="layui-col-xs4" style="background: blueviolet;">4</div>
            <!-- 占4/12的列 -->
        <div class="layui-col-xs4 layui-col-offset4" style="background: salmon;">4</div>
            <!-- 占4/12,偏移4的列 -->
        </div>
    </div>
    ```

3. 按钮

    - 不同颜色、大小按钮

    ```html
        <button type="button" class="layui-btn">一个标准的按钮</button>
        <a href="http://www.layui.com" class="layui-btn">一个可跳转的按钮</a>
    ```
    - 带图标的按钮

    ```html
    <button type="button" class="layui-btn">
        <i class="layui-icon">&#xe608;</i> 添加
        <!-- 官网字符实体选择图标 -->
    </button>
    ```

4. 导航

    - 导航需要依赖 element 模块

    ```html
    <header>
        <ul class="layui-nav" lay-filter="">
            <li class="layui-nav-item"><a href="">最新活动</a></li>
            <li class="layui-nav-item layui-this"><a href="">产品</a></li>
            <!-- layui-this 默认选中 -->
            <li class="layui-nav-item"><a href="">大数据</a></li>
            <li class="layui-nav-item">
              <a href="javascript:;">解决方案</a>
              <dl class="layui-nav-child"> 
                  <!-- 二级菜单 -->
                <dd><a href="">移动模块</a></dd>
                <dd><a href="">后台模版</a></dd>
                <dd><a href="">电商平台</a></dd>
              </dl>
            </li>
            <li class="layui-nav-item"><a href="">社区</a></li>
          </ul> 
    </header>
    
    <script>
        //注意：导航 依赖 element 模块，否则无法进行功能性操作
        layui.use('element', function(){
          var element = layui.element;
          
          //…
        });
    </script>
    ```

5. 选项卡

    - 需要依赖element模块 

    ```html
    <div class="layui-tab layui-tab-brief" lay-filter="docDemoTabBrief">
        <ul class="layui-tab-title">
            <li class="layui-this">网站设置</li>
            <li>用户管理</li>
            <li>权限分配</li>
            <li>商品管理</li>
            <li>订单管理</li>
        </ul>
        <div class="layui-tab-content">
        </div>
    </div>   

    <script>
        //注意：导航 依赖 element 模块，否则无法进行功能性操作
        layui.use('element', function(){
          var element = layui.element;
          
          //…
        });
    </script>
    ```

6. 表格

    - table上添加参数  进行样式设置

    ```html
    <table class="layui-table" lay-even lay-skin="line" lay-size="lg">
                            <!-- 隔行换色 行分割线  -->
        <colgroup>
            <col width="150">
            <col width="200">
            <col>
        </colgroup>
        <thead>
            <tr>
            <th>昵称</th>
            <th>加入时间</th>
            <th>签名</th>
            </tr> 
        </thead>
        <tbody>
            <tr>
            <td>贤心</td>
            <td>2016-11-29</td>
            <td>人生就像是一场修行</td>
            </tr>
            <tr>
            <td>许闲心</td>
            <td>2016-11-28</td>
            <td>于千万人之中遇见你所遇见的人，于千万年之中，时间的无涯的荒野里…</td>
            </tr>
        </tbody>
    </table>
    ```

7. 表单

    1. 输入框

        - 依赖form模块  layui.use('form')
        - layui-input-block  占满宽度
        - layui-input-inline  占默认宽度

        lay-verify | 验证
        -|-
        required | 必填
        phone | 手机号
        email | 邮箱
        url | 网址
        number| 数字
        date | 日期
        indentity | 身份证

        ```html
        <form class="layui-form" >
        <!-- form  -->
        <div class="layui-form-item">
        <label class="layui-form-label">email</label>
        <div class="layui-input-block">
            <!-- <input type="text" name="title" required lay-verify="email" placeholder="请输入标题" autocomplete="off" class="layui-input">     -->
        </div>
        </div>
        </form>  
        ```
    2. 下拉框

        - lay-search 可以搜索
        - selected  默认选中
        - disabled  禁止选中
        - optgroup  选项分组
        ```html
        <select name="city" lay-search>
            <option value="">请选择</option>
            <optgroup label="所在城市">
                <option value="010" selected>北京</option>
                <option value="021">上海</option>
                <option value="0571" disabled>杭州</option>
            </optgroup>
            <optgroup label="学生时代">
                <option value="学号">学号</option>
                <option value="最喜欢的老师">最喜欢的老师</option>
            </optgroup>
        </select>  
        ```
    3. 复选框

      - title 属性设置 对应文本
      - checked 默认选中
      - disable 禁用
      - lay-skin   设置复选框的样式
      - lay-text 开关的文本

      lay-skin | 样式
      -|-
      switch | 开关效果
      primary | 默认效果


      ```html
      <div class="layui-form-item">
        <label class="layui-form-label">email</label>
        <div class="layui-input-block">
          <input type="checkbox" checked name="" title="写作" checked>
          <input type="checkbox" name="" title="发呆">
          <input type="checkbox" name="" title="禁用" disabled>
        </div>
      </div>
      <div class="layui-form-item">
        <label class="layui-form-label">开关</label>
        <div class="layui-input-block">
          <input type="checkbox" name="switch" lay-skin="switch" lay-text="1|2">
        </div>
      </div>
      ```
## 组件

- 模块化使用

  - 引入 layui css 和 js

  ```js
  layui.use('layer',()=>{
    let layer = layui.layer
    layer.msg('hello')
  })
  ```

1. 弹出层 layer

  type | 类型 | 属性 | 示例
  -|-|-|-
  0 | 默认 信息框 | title、content | 
  1 | 元素 | | $('#id')
  2 | iframe
  3 | 加载层
  4 | tips层

2. 分页 laypage

  ```html
  <script>
  layui.use('laypage', function(){
    var laypage = layui.laypage;
    
    //执行一个laypage实例
    laypage.render({
      elem: 'test1' //注意，这里的 test1 是 ID，不用加 # 号
      ,count: 50 //数据总数，从服务端得到
    });
  });
</script>
  ```

3. 数据表格 table

  - 三种转换方式，  独爱方法渲染 

  参数 | 值 | 功能
  -|-|-
  elem | 选择器 | 渲染的ele
  cols | 列配置 [[]]  | 设置表头
  url | 异步接口 | 
  method | 默认get |
  type | number, checkbox | 添加序号、复选列等
  toolbar | | 设置工具栏

  cols | 功能 
  -|-
  field | 领域 字段  唯一标示
  title | 标题
  width | 
  minWidth | 
  fixed | 固定列
  sort | 排序 默认false 
  edit | 拖拽  默认true




  ```html
  <table id="demo"></table>
  <script>
  layui.use('table', function(){
    var table = layui.table;
    table.render({
      elem: '#demo',  //table的id
      height: 400,
      url: '/demo/table/user/', //数据接口
      page: true, //开启分页
      cols: [[ //表头
        {field: 'id', title: 'ID', width:80, sort: true, fixed: 'left'},
        {field: 'username', title: '用户名', width:80},
        {field: 'sex', title: '性别', width:80, sort: true},
        {field: 'city', title: '城市', width:80} ,
        {field: 'sign', title: '签名', width: 177},
        {field: 'experience', title: '积分', width: 80, sort: true},
        {field: 'score', title: '评分', width: 80, sort: true},
        {field: 'classify', title: '职业', width: 80},
        {field: 'wealth', title: '财富', width: 135, sort: true}
      ]]
    });
    
  });
  </script>
  ```
