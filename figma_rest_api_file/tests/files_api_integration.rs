#[cfg(feature = "client")]
use figma_api::apis::configuration::Configuration;
#[cfg(feature = "client")]
use figma_api::apis::files_api::get_file;
#[cfg(feature = "client")]
use std::env;

#[cfg(feature = "client")]
#[tokio::test]
#[ignore]
async fn test_get_file() {
    // Read the Figma API token from the environment variable
    let token = env::var("X_FIGMA_TOKEN").expect("X_FIGMA_TOKEN environment variable not set");
    let file_key = "kk5VAC0mXblEzdLug3B7fi";

    // Create a configuration with the token
    let mut config = Configuration::default();
    config.api_key = Some(figma_api::apis::configuration::ApiKey {
        prefix: None,
        key: token,
    });

    // Call the get_file endpoint
    let result = get_file(&config, file_key, None, None, None, None, None, None).await;
    assert!(
        result.is_ok(),
        "get_file request failed: {:?}",
        result.err()
    );
}

#[cfg(feature = "client")]
#[tokio::test]
#[ignore]
async fn test_get_image_fills() {
    // Read the Figma API token from the environment variable

    use figma_api::apis::files_api::get_image_fills;
    let token = env::var("X_FIGMA_TOKEN").expect("X_FIGMA_TOKEN environment variable not set");
    let file_key = "kk5VAC0mXblEzdLug3B7fi";

    // Create a configuration with the token
    let mut config = Configuration::default();
    config.api_key = Some(figma_api::apis::configuration::ApiKey {
        prefix: None,
        key: token,
    });

    // Call the get_file endpoint
    let result = get_image_fills(&config, file_key).await;
    assert!(
        result.is_ok(),
        "get_image_fills request failed: {:?}",
        result.err()
    );
}
