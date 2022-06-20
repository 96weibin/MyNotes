const Koa = require('koa');
const Router = require('@koa/router')
const cors = require('@koa/cors') 

let app = new Koa();
let router = new Router();
router.get('/', ctx =>{
    ctx.body = 'love you'
})
app.use(cors({
    origin:"*"
})) 
.use(router.routes())
.use(router.allowedMethods())
app.listen(8888);
