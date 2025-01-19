# [Gatsby](https://www.gatsbyjs.com/docs/tutorial/getting-started/part-3/)

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

### [plugins](https://www.gatsbyjs.com/plugins)

- 添加插件
  1. npm install gatsby-plugin-xxx   
  2. 在 gatsby-config.js 中添加配置
  3. 在页面 import

1. gatsby-plugin-image

  ```shell
  npm install gatsby-plugin-image gatsby-plugin-sharp gatsby-source-filesystem gatsby-transformer-sharp
  ```

  2. gatsby-config.js

  ```js
   plugins: [
    `gatsby-plugin-image`,
    `gatsby-plugin-sharp`,
    `gatsby-transformer-sharp`, // Needed for dynamic images
  ],
  ```

  3. 使用插件

  ```js
  import { StaticImage } from "gatsby-plugin-image"

  export const Kitten = ({width, height, ph}) =>{
    var imgStyle = { width, height }
    return <StaticImage imgStyle={imgStyle} src="https://www.gatsbyjs.com/static/5b3d5aedde3f9fe6f43af137058f2031/4ef49/index-page-with-static-image-from-filesystem.png" title={ph} alt="A kitten"/>
  }
  const IndexPage = () => {
    return (
      <>
        <h1>Hi, welcome to my site!</h1>
        <Link to="/about">goto</Link>
        <Kitten width={80} height={80} ph={'哈哈哈哈哈'}></Kitten>
        <StaticImage src="../images/icon.png" />
      </>
    )
  }
  ```

4. 使用graphQL

  - gatsby 有 data layer 
  - 通过 gatsby-source  源插件 链接数据
  - useStaticQuery

```jsx
const data = useStaticQuery(graphql
        `query MyQuery {
            site {
                siteMetadata {
                    title
                }
            }
        }`
    )
```

question :
 怎么是同步的，  怎么异步请求  以及 promise all

5. 转换数据以及 使用 MDX

  - 安装 plugin

  ```shell
  $ npm install gatsby-plugin-mdx gatsby-source-filesystem @mdx-js/react
  ```

  - set config.js

  ```js
  import { dirname } from "path"
  import { fileURLToPath } from "url"

  const __dirname = dirname(fileURLToPath(import.meta.url))

  const config = {
    plugins: [
      `gatsby-plugin-mdx`,      // 读取 mdx 
      {
        resolve: `gatsby-source-filesystem`,
        options: {
          name: `pages`,                    // graphql 名字
          path: `${__dirname}/src/pages`,   //配置路径
        },
      },
    ],
  }

  export default config
  ```

  - mdx: 结合 markdown 和  jsx
    - 可以读取  title date 等自定义变量

  ```mdx
  ---
  title: "Another Post"
  date: "2021-07-24"
  slug: "another-post"
  some: "my spical2"
  ---

  Here's another post! It's even better than the first one!
  ```

## 创建git仓库


## [unsplash](https://unsplash.com/)
- 免费素材库


## gatsby on Netlify 部署

- install 

```
```