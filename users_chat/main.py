from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
# socketio = SocketIO(app)


active_users = set()


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect", {"data": f"id: {request.sid} is connected"})


@socketio.on("data")
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ", str(data))
    emit("data", {"data": data, "id": request.sid}, broadcast=True)


@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect", f"user {request.sid} disconnected", broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
