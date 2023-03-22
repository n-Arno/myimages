#!/usr/local/bin/python

import bottle, socket, requests, functools

print = functools.partial(print, flush=True)
app = bottle.Bottle()

@app.route("/")
def root():
    base = f"Hello! This is the frontend image. I'm <b>{socket.gethostname()}</b><br/><br/>"
    try:
        r = requests.get("http://back")
        if r.status_code == requests.codes.ok:
            return base + f'I got news from <u>http://back</u>: <br/><br/><table style="border:1px solid black"><tr><td>{r.text}</td></tr></table>'
        else:
            raise Exception("Got an error from http://back")
    except:
        return base + "I didn't heard from <u>http://back</u> (yet)"

app.run(host="0.0.0.0", port=80, server="paste")
