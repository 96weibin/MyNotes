const http = require('http');
const urlLib = require('url');
const fs = require('fs');
const querystring = require('querystring')

let server = http.createServer((req,res)=>{
    let {pathname,query} = urlLib.parse(req.url,true)
    if(pathname == '/upload'){      //上传
        let arr = []
        req.on('data',(chunk)=>{
            arr.push(chunk)
        })
        req.on('end',()=>{
            let data = querystring.parse(Buffer.concat(arr).toString())
            let img = data.str;
            fs.writeFile('./upload/abcd.png',img.replace(/^data:[^,]+base64,/,''),'base64',(err)=>{
                if(err){
                    console.log('上传错误')
                } else {
                    res.end('ok 上传成功')
                }
            })
        })

    } else if(pathname == '/download'){ //下载
        let rs = fs.createReadStream('./upload/abcd.png')
        rs.on('error',()=>{
            console.log('读取失败')
            res.end('下载失败')
        })
        res.setHeader('Content-Disposition', 'attachment; filename=download.png')
        rs.pipe(res)
    } else {
        let rs = fs.createReadStream(`./www${pathname}`);
        rs.on('error',(err)=>{
            res.writeHead(404)
            res.end('no such file')
        })
        rs.pipe(res)
    }

}).listen(8080)