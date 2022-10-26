// 1 基础有序 二分
let arr1 = [1,4,5,6,6,7,,7,34,354,,7,,4534,2,34,6,7,8,353,45];
// let len1 = 100000;
// while(len1 --){
//     arr1.push(10 * Math.random());
// }


// function binaraySelect(arr: number[], item){
//     let l = 0;
//     let r = arr.length;
//     let m = Math.ceil((l + r) / 2);
    
//     while(true){
//         if(item < arr[m]){
//             r = m - 1;
//         } else if(item == arr[m]) {     //找不到会陷入死循环 所以不可行
//             return `find  + ${m}`
//         } else {
//             r = m;
//         }
    
//     }
// }

//重复 找第一个和最后一个， revert 反转一下 就可以
function binaraySelect(arr: number[], item: number){
    let l = 0; 
    let r = arr.length;
    while(l + 1 != r){
        //mid 前
        for(var i = l; i < r; i ++){
            if(item == arr[i]){
                return `find: ${i}`
            }
        }
        l = Math.floor((r + l) / 2);
    }
    return "not find"
}

console.log(binaraySelect(arr1, 34));

var arr = [1,2,3,4,5,6,7,7,8,9,91];

function lessEqual(mid: number): boolean{
    var target = 4;
    return arr[mid] < target ? true: false;
}

function bSearch_1(l: number, r: number): number{
    while(l < r){
        let mid: number;

        if((r - l) % 2 == 0) {
            mid = (r - l) / 2;
        } else {
            mid = (r - l + 1) / 2;
        }

        if(lessEqual(mid)){
            r = mid;
        } else {
            l = mid;
        }

        return 1;
    }
    return l;
}