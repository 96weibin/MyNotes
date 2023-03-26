var arr = [1, 2, 3, 5, 6, 7, 8, 11];
function binarySearch(arr, item) {
    var start = 0;
    var end = arr.length;
    var mid = arr.length / 2;
    if (item < arr[mid]) {
        //在 start~mid
        end = mid;
        mid = end / 2;
    }
    else if (item > arr[mid]) {
        //在 mid~end
        start = mid;
    }
    else {
        return mid;
    }
    arr = arr.slice(start, end);
    arguments.callee(arr, item);
}
var res = binarySearch(arr, 3);
console.log(res);
