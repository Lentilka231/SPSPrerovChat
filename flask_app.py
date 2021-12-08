from flask import Flask, request,render_template
from flask_socketio import SocketIO, send,emit
app = Flask(__name__)
app.config["SECRET_KEY"]="randomSECRETkey"
socketio = SocketIO(app)
client={}

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handleMessage(msg):
    if msg["address"] in client:
        emit("pmsg",msg,room=client[msg["address"]])
        emit("pmsg",msg,room=client[msg["name"]])
    else:
        send(msg, broadcast=True)
    print("Message: ", msg)
@socketio.on("privatemsg")
def pmsg(borec):
    client[borec]=request.sid
if __name__ =="__main__":
    socketio.run(app, host='0.0.0.0',debug=True)