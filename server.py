from flask import Flask

app = Flask(__name__)

@app.route("/")
async def route():
    return "<h1>Check <a href='https://github.com/ROO73D'>me</a></h1>"

if __name__ == "__main__":     
   app.run()
