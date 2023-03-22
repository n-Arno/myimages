#!/usr/local/bin/python

import bottle, socket, os, functools

print = functools.partial(print, flush=True)
app = bottle.Bottle()

@app.route("/")
def root():
    base = f"Hello! This is the backend image. I'm <b>{socket.gethostname()}</b><br/><br/>"
    if os.path.exists('/data/'):
        return base + "I found a something mounted as /data!"
    else:
        return base + "Nothing is mounted as /data :-("

app.run(host="0.0.0.0", port=80, server="paste")
