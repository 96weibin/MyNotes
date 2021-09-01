interface Person{
    firstName: string;
    lastName: string;
}


class Student{
    protected fullname:string;
    constructor(public firstName:string, public mind:string, public lastName:string){
        this.fullname = this.firstName + this.mind + this.lastName
    }
}

function greeter(person: Person):string{
    return 'Hello' + person.firstName + person.lastName
}

let user = new Student('Zhao','wei','bin');
console.log(user)
document.body.innerHTML = greeter(user)