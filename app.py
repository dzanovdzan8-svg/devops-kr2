# KR2: Bakiev
import os
import socket

import redis
from flask import Flask, request

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)
STUDENT = os.getenv("STUDENT", "unknown")


@app.route("/")
def index():
    hits = r.incr("hits")
    return f"KR2 | {STUDENT} | container {socket.gethostname()} | hits: {hits}\n"


@app.route("/health")
def health():
    return "ok\n"


@app.route("/whoami")
def whoami():
    h = request.headers
    return (
        f"scheme: {h.get('X-Forwarded-Proto', 'none')}\n"
        f"client: {h.get('X-Real-IP', 'none')}\n"
        f"host: {h.get('Host', 'none')}\n"
    )
