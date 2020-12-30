const {resolve} = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin')    //关联、压缩html
const MiniCssExtractPlugin = require('mini-css-extract-plugin') //输出css文件插件
const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin')    //压缩css插件

const commentCssLoader = [  //css处理复用
    MiniCssExtractPlugin.loader,    //生成css文件
    'css-loader',
    {
        loader:'postcss-loader',
        options:{
            ident:'postcss',
            plugins(){
                return [
                    require('postcss-preset-env')()
                    //在package.json 中写详细配置

                    /**
                     * "browserslist": {
                     *     "development": [
                     *          "last 1 chrome version",
                     *          "last 1 firefox version",
                     *          "last 1 safari version"
                     *      ],
                     *      "production": [
                     *           ">0%",
                     *           "not dead"
                     *       ]
                     *   },
                     */
                ]
            }
        }
    }
]


module.exports={
    entry:'./src/index.js',
    output:{
        filename:'bundle.js',
        path: resolve('./build')
    },
    module:{
        rules:[
            {   //css处理
                test:/\.css$/,
                use:[...commentCssLoader]
            },
            {   //less处理
                test:/\.less$/,
                use:[
                    ...commentCssLoader,
                    'less-loader'
                ]
            },
            {   //babel兼容
                test:/\.js$/,
                exclude:/node_modules/,
                use:[
                    {
                        loader:'babel-loader',
                        options:{
                            presets:[
                                '@babel/preset-env',
                                {
                                    useBuiltIns:'usage',
                                    corejs:{version:3},
                                    targets:{ie:'8'}
                                }
                            ]
                        }
                    }
                ]
            },
            {   //esLint
                test:/\.js$/,
                exclude:/node_modules/,
                enforce:'pre', //多个对同种文件处理的loader要分先后顺序  pre 则限制性eslint
                use:[
                    {
                        loader:'eslint-loader',
                        options:{
                            fix:true
                            //自动修复src内文件,不符合规则的
                        }
                        //在package.json中定义使用什么标准
                        /**
                         * 
                         *  "eslintConfig": {
                         *      "extends": "airbnb-base"
                         *  }
                         */

                    }
                ]
            },
            {   //css中图片
                test:/\.(jpg|img|png)$/,
                loader:'url-loader',
                options:{
                    limit:10*1024,
                    esModule:false,
                    name:'[hash:10].[ext]',
                    outputPath:'imgs'
                }
            },
            {   //html中的img
                test:/\.html$/,
                loader:'html-loader'
            },
            {
                exclude:/\.(js|html|less|css|jpg|png|gif)$/,
                loder:'file-loader',
                options:{
                    outputPath:'media'
                }
            }
        ]
    },
    plugins:[
        new HtmlWebpackPlugin({
            template:'./src/index.html',
            minify:{    
                collapseWhitespace:true,
                removeComents:true
            }
        }),
        new MiniCssExtractPlugin({
            filename:'css/build.css'
            //生成css文件名字
        }),
        new OptimizeCssAssetsWebpackPlugin()
    ],
    mode:"production"
}