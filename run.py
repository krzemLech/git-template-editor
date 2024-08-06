import uvicorn

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=5003, log_level="info", reload=True, reload_includes=["*.html", "*.css", "*svg"],), 