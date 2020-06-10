from flask import Flask

app_name = Flask(__name__)

@app_name.route("/")
def Wishes():
    return "<head><title>Birthday Wishes</title></head>" \
           "<body><h1>Many Happy Returns of the Day</h1>" \
           "<h1 style='color:blue;'>Ravi Teja Reddy Palagiri</h1>" \
           "<Br><p>From" \
           "<Br><big> Koncham Touch Lo Undam Gang" \
           "<Br>Vinay" \
           "<Br>Vijay" \
           "<Br>Jaya" \
           "<Br>Vamsi" \
           "<Br>Charan" \
           "<Br>Saranya" \
           "<Br>Keerthi" \
           "<Br>Himaja" \
           "</big></p>" \
           "</body>"


# To run this program, Go to the existing path and follow
# 1. We need to set an environmental Variable
# export FLASK_APP = app.py
# 2. then
# flask run



