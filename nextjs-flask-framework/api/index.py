from flask import Flask

app = Flask(__name__)

@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {
        "status": "success", 
        "message": "Integrate Flask Framework with Next.js", 
        "a second field": "this is a second field"
        }

if __name__ == "__main__":
    app.run()
