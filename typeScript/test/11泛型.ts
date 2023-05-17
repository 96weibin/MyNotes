interface testI {
    name: string,
    age: number
}

declare const concat: {
    (value: string, age: number): string
}

function identity <concat>(args: concat) {return args};

identity({value: 'hhh', age1: 12})