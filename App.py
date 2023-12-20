from flask import*
from user import User

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
 
    return render_template("accueil.html")

@app.route('/sign-up',methods=["GET"])
def login():
    return render_template("sign-up.html")

@app.route('/form-sign-up',methods=["POST"])
def loginForm():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        psw = request.form.get("password")
        nouveauUser = User(prenom,psw)
        return redirect("/")        


if __name__ == '__main__':
    app.run(debug=True)