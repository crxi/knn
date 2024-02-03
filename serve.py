import uvicorn
import streamsync.serve

app_path = "." # . for current working directory
mode = "run" # run or edit

asgi_app = streamsync.serve.get_asgi_app(app_path, mode)

uvicorn.run(asgi_app,
    host="0.0.0.0",
    port=3005,
    log_level="info",
    ws_max_size=streamsync.serve.MAX_WEBSOCKET_MESSAGE_SIZE)
