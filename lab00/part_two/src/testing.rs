// Includes
use std::fmt::Write;
use crate::Box;

fn assert(expected: bool, description: &str) {
    if expected {
        println!("PASSED: {}", description);
    } else {
        println!("FAILED: {}", description);
    }
}

struct BoxTest {
    inputWidth: u32,
    inputCharacter: char,
    expectedWidth: u32,
    expectedCharacter: char,
    expectedString: String,
    boxObject: Box
}

impl BoxTest {
    fn new(inputWidth: u32, inputCharacter: char, expectedWidth: u32, expectedCharacter: char, expectedString: String) -> Self {
        Self { inputWidth, inputCharacter, expectedWidth, expectedCharacter, expectedString , boxObject: Box::new(inputWidth, inputCharacter) }
    }

    fn newEmpty() -> Self {
        Self { inputWidth: 0, inputCharacter: ' ', expectedWidth: 0, expectedCharacter: '*', expectedString: String::from(""), boxObject: Box::newEmpty() }
    }

    fn runTest(&self) -> () {
        let mut actualString = String::new();
        write!(&mut actualString, "{}", self.boxObject);
        let description = format!("{} {} {} {} \"{}\"", self.inputWidth, self.inputCharacter, self.expectedWidth, self.expectedCharacter, self.expectedString);
        assert(
            self.expectedWidth == self.boxObject.getWidth() &&
            self.expectedCharacter == self.boxObject.getCharacter() && 
            self.expectedString == actualString
            , &description
        );
    }
}

pub fn runAllTests() -> () {
    println!("Running All Tests");
    println!("\nProvided Tests:");
    BoxTest::newEmpty().runTest(); // runBoxTestEmpty
    BoxTest::new(1, '$', 1, '$', String::from("$\n")).runTest(); // runBoxTestSize1
    BoxTest::new(3, '%', 3, '%', String::from("%%%\n%%%\n%%%\n")).runTest(); // runBoxTestSize3

    let mut runBoxTestSetBoxChar = BoxTest::new(1, '$', 1, '%', String::from("$\n")); // runBoxTestSetBoxChar
    runBoxTestSetBoxChar.boxObject.setCharacter('%');
    runBoxTestSetBoxChar.expectedCharacter = '%';
    runBoxTestSetBoxChar.expectedString = String::from("%\n");
    runBoxTestSetBoxChar.runTest();

    // runBoxTestIncDec
    let mut runBoxTestIncDec = BoxTest::new(1, '*', 1, '*', String::from("*\n"));
    let mut isCorrect: bool = true;
    runBoxTestIncDec.boxObject += 2;
    runBoxTestIncDec.expectedWidth = 3; // inc
    isCorrect = runBoxTestIncDec.expectedWidth == runBoxTestIncDec.boxObject.getWidth() && isCorrect;

    runBoxTestIncDec.boxObject -= 2;
    runBoxTestIncDec.expectedWidth = 1; // dec
    isCorrect = runBoxTestIncDec.expectedWidth == runBoxTestIncDec.boxObject.getWidth() && isCorrect;

    runBoxTestIncDec.expectedString = String::from("*\n");
    let mut resultString = String::new();
    write!(&mut resultString, "{}", runBoxTestIncDec.boxObject);
    isCorrect = runBoxTestIncDec.expectedString == resultString && isCorrect;

    assert(isCorrect, "inc/dec");

    println!("My Tests:");
    BoxTest::new(10, '*', 10, '*', String::from("**********\n**********\n**********\n**********\n**********\n**********\n**********\n**********\n**********\n**********\n")).runTest(); // Test 1
    BoxTest::new(2, '@', 2, '@', String::from("@@\n@@\n")).runTest(); // Test 2
    BoxTest::new(7, '&', 7, '&', String::from("&&&&&&&\n&&&&&&&\n&&&&&&&\n&&&&&&&\n&&&&&&&\n&&&&&&&\n&&&&&&&\n")).runTest(); // Test 3
    BoxTest::new(0, ' ', 0, ' ', String::from("")).runTest(); // Test 4
    BoxTest::new(5, ' ', 5, ' ', String::from("     \n     \n     \n     \n     \n")).runTest(); // Test 5

    let mut runBoxTestSubAssign = BoxTest::new(5, ' ', 5, ' ', String::from("     \n     \n     \n     \n     \n"));
    runBoxTestSubAssign.boxObject -= 3;
    runBoxTestSubAssign.expectedWidth = 2;
    runBoxTestSubAssign.expectedString = String::from("  \n  \n");
    runBoxTestSubAssign.runTest(); // Test 6
}
