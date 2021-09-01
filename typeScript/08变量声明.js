var a = 123;
function fn(flag, msg) {
    if (!flag) {
        var msg_1 = "false ya";
        return msg_1;
    }
    return msg;
}
console.log(fn(false, 'true ya'));
