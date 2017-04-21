# -*-coding:utf-8 -*-
import websocket
import unittest

try:
    import thread
except ImportError:  # TODO use Threading instead of _thread in python3
    import _thread as thread
import time
import sys


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_close(ws):
    ws.close()
    print("Thread terminating...")


def on_open(ws):
    def run(*args):
        count = 0
        run_error = []

        ws.send("connect Eric Zepler")
        time.sleep(1)

        ws.send("@path UG Lab")
        time.sleep(1)
        
        print count
        print run_error

        ws.close()

    thread.start_new_thread(run, ())


def check_run_result(s_str, d_str, func_name, ret_list):
    if s_str not in d_str:
        ret_list.append(func_name)


if __name__ == "__main__":
    websocket.enableTrace(True)
    if len(sys.argv) < 2:
        host = "ws://127.0.0.1:5000/ws"
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()
