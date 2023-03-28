let arr = [1,2,3,5,6,7,8,11];

function binarySearch(arr: number[], item: number){
    let start = 0;
    let end = arr.length;
    let mid = arr.length / 2;

    if(item < arr[mid]){
        //在 start~mid
        end = mid;
        mid = end / 2;
    } else if (item > arr[mid]) {
        //在 mid~end
        start = mid;
    } else {
        return mid;
    }
    arr = arr.slice(start, end)
    arguments.callee(arr, item);
}

let res = binarySearch(arr, 3);
console.log(res);
