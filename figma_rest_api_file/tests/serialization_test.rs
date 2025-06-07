use figma_api::models::InlineObject;
use figma_api::models::Node;
use serde_json;
use std::fs;
use std::path::Path;

fn read_json_file<P: AsRef<Path>>(path: P) -> String {
    fs::read_to_string(path).expect("Failed to read JSON file")
}

// #[test]
// fn test_deserialize_file_response() {
//     // Read JSON from file
//     let json = read_json_file("../examples/__primitive__.json");

//     // Try to deserialize the JSON into our model
//     let result = serde_json::from_str::<InlineObject>(&json);
//     assert!(
//         result.is_ok(),
//         "Failed to deserialize JSON: {:?}",
//         result.err()
//     );

//     let file = result.unwrap();
//     assert_eq!(file.document.name, "Document");
//     assert_eq!(
//         file.document.r#type,
//         figma_api::models::document_node::Type::Document
//     );
//     assert_eq!(file.role, figma_api::models::inline_object::Role::Owner);
//     assert_eq!(
//         file.editor_type,
//         figma_api::models::inline_object::EditorType::Figma
//     );
// }

#[test]
fn test_deserialize_node() {
    // Read JSON from file
    let json = read_json_file("../examples/__rectangle__.json");

    // Try to deserialize the JSON into a Node
    let result = serde_json::from_str::<Node>(&json);
    println!("Deserialization result: {:?}", result);
    assert!(
        result.is_ok(),
        "Failed to deserialize Node: {:?}",
        result.err()
    );
}
