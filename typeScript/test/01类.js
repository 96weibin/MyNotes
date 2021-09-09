var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Foo = /** @class */ (function () {
    function Foo(type) {
        this.type = type;
    }
    return Foo;
}());
var Son = /** @class */ (function (_super) {
    __extends(Son, _super);
    function Son(type) {
        var _this = _super.call(this, type) || this;
        _this.type = type;
        return _this;
    }
    Son.prototype.test = function () {
        console.log(this.type);
    };
    return Son;
}(Foo));
var s = new Son('son');
console.log(s);
