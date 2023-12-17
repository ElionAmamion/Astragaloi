use std::io;

fn main() {
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("couldn't read line");
    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("couldn't read line");

    let int_input1: f64 =input1.trim().parse().unwrap();
    let int_input2: f64 =input2.trim().parse().unwrap();

    println!("{}", int_input1 + int_input2);
}
