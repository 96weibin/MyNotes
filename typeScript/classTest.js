var Student = /** @class */ (function () {
    function Student(firstName, mind, lastName) {
        this.firstName = firstName;
        this.mind = mind;
        this.lastName = lastName;
        this.fullname = this.firstName + this.mind + this.lastName;
    }
    return Student;
}());
function greeter(person) {
    return 'Hello' + person.firstName + person.lastName;
}
var user = new Student('Zhao', 'wei', 'bin');
console.log(user);
document.body.innerHTML = greeter(user);
