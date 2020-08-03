# SQLServer 笔记

## 增删改查

### 插入数据 Insert

  ```sql
  insert into
  <表名>[(<列名1>[，<列名2>....)]]
  values (<数据1>[,<数据2>...])
  ```

  上面伪代码的<br>
  \<\>是 必写的属性,内容为解释<br>
  [] 是 可选项 根据需求

  ```sql
  insert into userList (usrename, userid) values('yaoming', '1')
  -- 要注意   values里的值 要用单一好包裹起来
  ```

### 更新数据 Update

```sql
update <表名> set <列名> = <数据>[,<列明2> = <数据2>]
[where<条件>]
```

**注意是** date 而不是 data  我也不明白更新数据   为啥叫update 更新日期？。。。害我一开始打错了

```sql
update userList set sex = 'maile'  where username = 'weibin'
-- 把 username是 weibin 的 sex 改为了 maile
```

### 删除数据 delete

```sql
delete from <表名>
[where <条件>]

-- 省略 where 则全部删除
```

```sql
delete from getList where userid = 15
-- 删除 userid 为15的数据
```

### 查询数据 Select

```sql
select [all | Distinct]<目标表列达式1>[,<目标列表达式2>]
from <表名1>[,<表名>]
[where<条件表达式>]
[grop by <列名1>[having<条件表达式>]]
[order by <列名>[asc|desc]]
```

1. all | distinct ：默认是all可设置成distinct，意思就是删除返回中重复的数据

2. 目标表达式 ： 字段名，可以 "字段名 as 列名" 设置查询结果的列名。

3. where 条件:特殊的比较运算符， 除了以下几个其他都和js相同

    ```html
    <> 或!=        不等于
    !>           不大于
    !<           不小于
    between...and 和 not between ... and
    and 和 or 连接多个条件
    ```

    * demo

    ```sql
    select age as 年龄,name as 姓名
    from userList
    where age between 15 and 20
    -- 获取uesrList中age 在15 - 20 的 人名对应的年龄
    ```

4. group by 将查询结果以某条件分组

    ```sql
    select
    e.dept_id as 部门,
    count(e.emp_no) as 人数,  -- 可以结合聚合函数
    from employee e
    where e.date_of_resign != null
    group by e.dept_id
    having count(e.dept_id) > 1
    -- 以部门分组，查询 离职 部门人数。
    -- having ： 对group by的内容进行筛选。
    ```

    * 聚合函数

    函数 | 功能
    -|-
    count() | 计数
    sum() | 求和
    avg() | 平均数
    max() | 最大值
    min() | 最小值

5. order by 排序

    默认ASC 是升序     可以设置 desc 为 降序

6. 使用top 限制返回行数

    ```sql
      select top 200 from userList where sex=maile
      -- top n 还可以设置 n 为百分数  显示产寻结果的百分之多少
    ```

7. 分页查询