// Turn Warnings off
#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(non_snake_case)]

// Includes
use std::io;
use std::io::Write;

mod boxClass;
use boxClass::Box;

mod testing;
use testing::runAllTests;

fn main() {
    print!("User input or run tests? (u/t): ");
    std::io::stdout().flush();

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");

    println!("");
    if input.trim() == "u" {
        userRun();
    } else if input.trim() == "t" {
        runAllTests();
    } else {
        println!("Invalid input");
    }
}

fn userRun() {
    print!("Enter a width: ");
    std::io::stdout().flush();
    let mut inputWidth = String::new();
    io::stdin().read_line(&mut inputWidth).expect("Failed to read line");
    let inputWidth: u32 = match inputWidth.trim().parse() {
        Ok(num) => num,
        Err(_) => 0
    };
    print!("Enter a character: ");
    std::io::stdout().flush();
    let mut inputCharacter = String::new();
    io::stdin().read_line(&mut inputCharacter).expect("Failed to read line");
    let inputCharacter: char = match inputCharacter.trim().parse() {
        Ok(num) => num,
        Err(_) => ' '
    };
    let mut boxObject = Box::new(inputWidth, inputCharacter);
    print!("{}", boxObject);
    std::io::stdout().flush();
}
