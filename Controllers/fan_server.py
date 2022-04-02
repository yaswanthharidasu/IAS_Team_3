import sys
from flask import Flask, request

app = Flask(__name__)

@app.route("/fanAction", methods=["POST", "GET"])
def performAction():
    data = request.json
    print(data)
    if data['data'] == 0:
        print("Turn Off Fan")
    else:
        print("Turn On Fan")
    return "FAN"


if __name__ == "__main":
    port = sys.argv[1]
    app.run(port=port, debug=True)