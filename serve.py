import argparse
import uvicorn
import streamsync.serve

parser = argparse.ArgumentParser(description='serve.py')

parser.add_argument('--loglevel', type=str, default='info',
                    help='Log level for the server script')

args = parser.parse_args()

app_path = "." # . for current working directory
mode = "run" # run or edit

asgi_app = streamsync.serve.get_asgi_app(app_path, mode)

uvicorn.run(asgi_app,
    host="0.0.0.0",
    port=3333,
    log_level=args.loglevel,
    ws_max_size=streamsync.serve.MAX_WEBSOCKET_MESSAGE_SIZE)
