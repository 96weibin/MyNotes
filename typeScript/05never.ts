function fn():never{
    // return void
    throw new Error('err')
}

fn()