//给一组数据 赋予更好的名字
var Collor;
(function (Collor) {
    Collor[Collor["red"] = 0] = "red";
    Collor[Collor["green"] = 1] = "green";
    Collor[Collor["blue"] = 2] = "blue";
})(Collor || (Collor = {}));
console.log(Collor);
var c = Collor.green;
console.log(c);
var collorName = Collor[2];
console.log(collorName);
