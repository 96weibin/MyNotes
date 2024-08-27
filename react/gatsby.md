# Gatsby

- install

```shell
$ yarn global add gatsby-cli
```

- create app

```shell
$ gatsby new
```

## Guid

### Gatsby Head API

- 添加 head 元素
```js
export const Head = () => (<>
  <title>home page</title>
  <link rel="icon" href="/images/icon.png" type="image/ico" />
</>)
```

### Link API

- Link跳转

```js
import { Link } from "gatsby"
const IndexPage = () => {
  return (
    <>
      <h1>Hi, welcome to my site!</h1>
      <Link to="/about">goto</Link>
    </>
  )
}
```

## 创建git仓库


## gatsby on Netlify 部署

- install 

```
```