
// Event
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
pub struct Event {
    pub id: String,
    pub title: String,
}

impl Event {
    pub fn new(id: String, title: String) -> Self {
        Event { id, title }
    }
}

// Query arams & PutTitleParams
use serde::{Deserialize, Serialize};

#[derive(Clone, Debug, Serialize, Deserialize, PartialEq, Eq)]
pub struct QueryParams {
    pub title: Option<String>,
}

#[derive(Clone, Debug, Serialize, Deserialize, PartialEq, Eq)]
pub struct PutTitleParams {
    pub title: String,
}


//handler
use anyhow::Result;
use axum::extract::Query;
use axum::http::StatusCode;
use axum::{
    extract::{Path, State},
    response::Json,
};
use serde_json::{json, Value};

pub async fn get_events(
    State(service): State<EventService>,
    Query(params): Query<QueryParams>,
) -> (StatusCode, Json<Value>) {
  (
        StatusCode::OK,
        Json(json!({ "request parameters": params })),
    )
}

pub async fn post_event(
    State(service): State<EventService>,
    Json(event): Json<Event>,
) -> (StatusCode, Json<Value>) {
(
        StatusCode::OK,
        Json(json!({ "request body": event })),
    )
}

pub async fn get_event_single(
    State(service): State<EventService>,
    Path(id): Path<String>,
) -> (StatusCode, Json<Value>) {
    (
        StatusCode::OK,
        Json(json!({ "get request id": id})),
    )
}

pub async fn delete_event_single(
    State(service): State<EventService>,
    Path(id): Path<String>,
) -> (StatusCode, Json<Value>) {
(
        StatusCode::OK,
        Json(json!({ "delete request id": id })),
    )
}

pub async fn put_event_title(
    State(service): State<EventService>,
    Path(id): Path<String>,
    Json(put_title_params): Json<PutTitleParams>,
) -> (StatusCode, Json<Value>) {
    (
        StatusCode::OK,
        Json(json!({ "put new title": put_title_params.title })),
    )
}


// Axum Router

pub mod handler;

use lambda_http::{run, tracing, Error};
use axum::{routing::get, Router};
use std::env::set_var;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing::init_default_subscriber();
    set_var("AWS_LAMBDA_HTTP_IGNORE_STAGE_IN_PATH", "true");

    let app = Router::new()
        .route("/events", get(handler::get_events).post(handler::post_event))
        .route(
            "/events/:id",
            get(handler::get_event_single).delete(handler::delete_event_single),
        )
        .route("/events/:id/title", put(handler::put_event_title));

    run(app).await
}

let event_api = Router::new()
    .route("/", get(handler::get_events).post(handler::post_event))
    .route(
        "/:id",
        get(handler::get_event_single).delete(handler::delete_event_single),
    )
    .route("/:id/title", put(handler::put_event_title));

let app = Router::new()
    .nest("/events", event_api);


    


