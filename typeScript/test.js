var Circle = /** @class */ (function () {
    function Circle(r) {
        this.r = r;
    }
    Circle.prototype.draw = function () {
        console.log('画圆');
    };
    Circle.prototype.area = function () {
        return Math.PI * Math.pow(this.r, 2);
    };
    return Circle;
}());
var Rect = /** @class */ (function () {
    function Rect(width, height) {
        this.width = width;
        this.height = height;
    }
    Rect.prototype.draw = function () {
        console.log('画方块');
    };
    Rect.prototype.area = function () {
        return this.width * this.height;
    };
    return Rect;
}());
var c1 = new Circle(10);
console.log(c1.area());
var r1 = new Rect(10, 20);
console.log(r1.area());
