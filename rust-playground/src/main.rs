fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let a = 1;
    let b = 2;
    let res = add(a, b);
    println!("{} + {} = {}", a, b , res);
}