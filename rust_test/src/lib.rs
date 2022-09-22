use wasm_bindgen::prelude::*;

// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

// #[wasm_bindgen]
// extern {
//     fn alert(s: &str);
// }

// #[wasm_bindgen]
// pub fn greet(input: String) -> String {
//     return input.to_owned() + "!";
//     // alert("Hello, {{project-name}}!");
// }


#[wasm_bindgen]
pub fn greet() -> String {
    "hehu".to_owned()
    // return "hehu".to_owned();
    // alert("Hello, {{project-name}}!");
}
