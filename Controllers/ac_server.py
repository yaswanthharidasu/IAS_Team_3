import sys
from flask import Flask, request

app = Flask(__name__)

@app.route("/acAction", methods=["POST", "GET"])
def performAction():
    data = request.json
    print(data)
    if data['data'] == 0:
        print("Turn Off AC")
    else:
        print("Turn On AC")
    return "AC"

if __name__ == "__main__":
    port = sys.argv[1]
    app.run(port=port, debug=True)