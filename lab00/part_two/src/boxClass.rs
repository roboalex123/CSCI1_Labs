// Turn Warnings off
#[allow(dead_code)]
#[allow(unused_variables)]
#[allow(non_snake_case)]

// Includes
use std::fmt;
use std::ops::{AddAssign, SubAssign};

pub struct Box {
    width: u32,
    character: char,
}

impl Box {
    pub fn newEmpty() -> Self {
        Self { width: 0, character: '*' }
    }

    pub fn new(inputWidth: u32, inputCharacter: char) -> Self {
        Self { width: inputWidth, character: inputCharacter }
    }

    // Getters
    pub fn getWidth(&self) -> u32 {
        self.width
    }

    pub fn getCharacter(&self) -> char {
        self.character
    }

    // Setters
    pub fn setWidth(&mut self, width: u32) {
        self.width = width;
    }

    pub fn setCharacter(&mut self, character: char) {
        self.character = character;
    }

}

// OPERATORS
// Add
impl AddAssign for Box { // box += box
    fn add_assign(&mut self, rhs: Box) {
        self.width += rhs.width;
    }
}

impl AddAssign<u32> for Box { // box += u32
    fn add_assign(&mut self, rhs: u32) {
        self.width += rhs;
    }
}

impl AddAssign<i32> for Box { // box += i32
    fn add_assign(&mut self, rhs: i32) {
        if rhs < 0 {
            self.width -= rhs.abs() as u32;
        } else {
            self.width += rhs as u32;
        }
    }
}

// Sub
impl SubAssign for Box { // box -= box
    fn sub_assign(&mut self, rhs: Box) {
        if rhs.width > self.width {
            self.width = 0;
        } else {
            self.width -= rhs.width;
        }
    }
}

impl SubAssign<u32> for Box { // box -= u32
    fn sub_assign(&mut self, rhs: u32) {
        if rhs > self.width {
            self.width = 0;
        } else {
            self.width -= rhs;
        }
    }
}

impl SubAssign<i32> for Box { // box -= i32
    fn sub_assign(&mut self, rhs: i32) {
        if rhs.abs() > self.width as i32 {
            self.width = 0;
        } else if rhs < 0 {
            self.width += rhs.abs() as u32;
        } else {
            self.width -= rhs as u32;
        }
    }
}

// Display
impl fmt::Display for Box {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", (self.character.to_string().repeat(self.width as usize) + "\n").repeat(self.width as usize))
    }
}
