const http = require('http');

let server = http.createServer( async(req,res)=>{

    function delay(s){
        return new Promise(reslove=>{
            setTimeout(() => {
                reslove()
            }, s * 1000);
        },reject=>{

        })
    }
    console.log(req.url)
    await delay(5)
    res.setHeader('Access-Control-Allow-Origin','*')
    res.end('thanks')
})

server.listen(8081)