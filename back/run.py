#!/usr/local/bin/python

import bottle, socket, os, functools

print = functools.partial(print, flush=True)
app = bottle.Bottle()

@app.route("/")
def root():
    base = f"Hello! This is the backend image. My name is <b>{socket.gethostname()}</b><br/><br/>"
    if os.path.exists('/data/'):
        return base + "I found something mounted as /data!"
    else:
        return base + "Nothing is mounted as /data :-("

app.run(host="0.0.0.0", port=80, server="paste")
