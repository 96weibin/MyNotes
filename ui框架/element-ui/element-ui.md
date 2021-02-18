# element ui

## 引入

### 布局 和 容器

1. 布局 

    - 一行24 份
    - :span 占的份
    - :gutter 列间隔
    - :offset 偏移
    - :xs :sm :md :lg :lx 响应
    - 居中 可以设置 type="flex" justyfy:center 

    ```html
        <el-row>
            <el-col :span="24"><div></div></el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="10" :offset="7"><div></div></el-col>
        </el-row>
    ```

2. 容器

    - \<el-container>
    - \<el-header>
    - \<elaside>
    - \<el-main>
    - \<el-footer>