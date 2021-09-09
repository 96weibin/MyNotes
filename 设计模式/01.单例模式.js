class Single {
    constructor(name){
        this.name = name;
        this.instance = null;
    }
    static getInstance(name){
        if(!this.instance){
            this.instance = new Single(name)
        } 
        return this.instance;
    }
}

console.log(Single.getInstance('zme'));     //Single { name: 'zme', instance: null }
let d = Single.getInstance('BL');           //Single { name: 'zme', instance: null }
console.log(d)