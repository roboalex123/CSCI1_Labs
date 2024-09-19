// Prevent console window in addition to Slint window in Windows release builds when, e.g., starting the app via file manager. Ignored on other platforms.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::error::Error;

slint::include_modules!();

fn main() -> Result<(), Box<dyn Error>> {
    let ui = AppWindow::new()?;

    let ui_handle = ui.as_weak();

    let u2 = ui_handle.clone();
    ui.on_say_hello(move |string| {
        if let Some(ui) = u2.upgrade() {
            ui.set_printable_string(format!("Hello, {}! Hope you like the app!", string).into())
        }
    });

    let u3 = ui_handle.clone();
    ui.on_close(move || {
        if let Some(ui) = u3.upgrade() {
            ui_handle.unwrap().window().hide().unwrap()
        }
    });

    ui.run()?;

    Ok(())
}
