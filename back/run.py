#!/usr/local/bin/python

import bottle, socket, functools

print = functools.partial(print, flush=True)
app = bottle.Bottle()

@app.route("/")
def root():
    return f"Hello! This is the backend image, I'm <b>{socket.gethostname()}</b>"

app.run(host="0.0.0.0", port=80, server="paste")
