use std::alloc::{alloc, dealloc, Layout};
use std::ptr;
use std::fmt;

pub struct vector {
    arr: *mut i32,
    num_items: usize,
    capacity: usize,
}

impl vector {
    // CSTOR should create a new vector with capacity 1 but no elements inside
    pub fn new() -> Self { 
        let cstorArr: *mut i32 = unsafe {
            alloc(
                Layout::array::<i32>(1).unwrap()
            ) as *mut i32
        };

        Self {
            arr: cstorArr,
            num_items: 0,
            capacity: 1,
        }

    }

    pub fn size(&self) -> usize {
        self.num_items
    }

    pub fn push_back(&mut self, val: i32) {
        if self.num_items == self.capacity {
            self.resize(); // resize if necessary
        }

        unsafe {
            // add(x) adds x to the ptr in order to access the corresponding element
            *self.arr.add(self.num_items) = val;
        }
        self.num_items += 1;
    }

    pub fn at(&mut self, index: usize) -> &mut i32 { // &self = immutable reference
        if index >= self.num_items { // check if index is out of bounds
            panic!("Index out of bounds");
        }

        unsafe {
            &mut *self.arr.add(index) // return the element at index so we can modify it
        }
    }

    pub fn sort(&mut self) {
        // only sort the first num_items elements
        if self.num_items > 0 { // only sort if there are elements
            unsafe {
                std::slice::from_raw_parts_mut(self.arr, self.num_items).sort();
            }
        }
    }

    fn resize(&mut self) {
        let new_capacity = self.capacity * 2;

        // how much memory do we need? (unwrap allows us to panic if allocation fails)
            // panic = throw from c world
        let new_layout = Layout::array::<i32>(new_capacity).unwrap();

        // allocate memory
        let new_ptr = unsafe { alloc(new_layout) as *mut i32 };

        if new_ptr.is_null() { // check if allocation was successful
            panic!("Allocation failed");
        }

        if self.num_items > 0 { // only copy if necessary
            unsafe { // unsafe means we are not checking for rust's normal errors
                // copy the elements from the old array to the new one
                ptr::copy_nonoverlapping(self.arr, new_ptr, self.num_items);
            }
        }

        if !self.arr.is_null() {
            // calculate how much memory to deallocate
            let old_layout = Layout::array::<i32>(self.capacity).unwrap();
            unsafe {
                // deallocate the old array
                    // u8 = unsigned byte because dealloc works with bytes
                dealloc(self.arr as *mut u8, old_layout);
            }
        }

        // update the capacity
        self.capacity = new_capacity;
        self.arr = new_ptr;
    }
}

impl Drop for vector { // destructor
    fn drop(&mut self) {
        if !self.arr.is_null() {
            unsafe {
                let layout = Layout::array::<i32>(self.capacity).unwrap();
                dealloc(self.arr as *mut u8, layout);
            }
        }
    }
}

// Display and Debug for printing vector
impl fmt::Debug for vector {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        unsafe {
            let slice = std::slice::from_raw_parts(self.arr, self.num_items);
            write!(f, "{:?}", slice)
        }
    }
}

impl fmt::Display for vector {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        unsafe {
            let slice = std::slice::from_raw_parts(self.arr, self.num_items);
            write!(f, "Contains: {:?}", slice)
        }
    }
}
