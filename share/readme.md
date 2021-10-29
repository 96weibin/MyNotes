# tech share

1. 模板字符串在使用组件中的使用
   - 模板字符串格式化代码，易于观察，但是保留的格式也会被传输给组件，组件调用时模板字符串的解析，存在不足

    ```ts
    template:`<select-menu-with-new
                        searchable 
                        options.bind="options" 
                        value.bind="property" 
                        change.delegate="onChange($event)"
                        placeholder.bind="placeHolder" 
                        add-params.bind="addParams"
            ></select-menu-with-new>`,
    //标签闭合  的位置导致 解析异常
    //这么写传输过去就会报错   
    ```