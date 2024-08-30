use crate::vector;

pub fn assert_true(b: bool, description: &str) {
    if b {
        println!("PASSED: {}", description);
    } else {
        println!("FAILED: {}", description);
    }
}

pub fn run_all_tests() {
    test_one();
    test_two();
    test_three();
    test_four();
}

fn test_one() {
    let v = vector::vector::new();
    assert_true(v.size() == 0, "empty vector");
}

fn test_two() {
    let mut v = vector::vector::new();
    v.push_back(3);
    v.push_back(2);
    v.push_back(1);
    assert_true(
        v.size() == 3 &&
        *v.at(0) == 3 &&
        *v.at(1) == 2 &&
        *v.at(2) == 1,
        "vector {3, 2, 1}"
    );
}

fn test_three() {
    let mut v = vector::vector::new();
    v.push_back(3);
    v.push_back(2);
    v.push_back(1);
    v.sort();
    assert_true(
        v.size() == 3 &&
        *v.at(0) == 1 &&
        *v.at(1) == 2 &&
        *v.at(2) == 3,
        "sorting vector {3, 2, 1}"
    );
}

fn test_four() {
    let mut v = vector::vector::new();

    // insert 32 to 0 inclusive
    for i in (0..=32).rev() {
        v.push_back(i);
    }

    v.sort();

    let mut is_correct: bool = true;

    if v.size() != 33 {
        is_correct = false;
    }

    for i in 0..=32 {
        if *v.at(i) != i.try_into().unwrap() {
            is_correct = false;
        }
    }

    // check modifiability using .at()
    *v.at(2) += 1;
    if *v.at(2) != 3 {
        is_correct = false;
    }

    assert_true(is_correct, "comprehensive large vector test");
}
