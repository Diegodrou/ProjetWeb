from flask import*
from user import User
import json

jsonPsw = open("pswords.json")
jsonData = open("comptes.json")
 
pswToUser:list[dict[str,str]] = json.load(jsonPsw)
comptes:list = json.load(jsonData)
jsonData.close()
jsonPsw.close()

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
 
    return render_template("accueil.html",prenom="")

@app.route('/sign-up',methods=["GET"])
def login():
    return render_template("sign-up.html")

@app.route('/form-sign-up',methods=["POST"])
def signUpForm():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        psw = request.form.get("password")
        pswToUser.append({psw:prenom})
        nouveauUser = User(prenom).serialize() 
        comptes.append(nouveauUser)
        with open("comptes.json","w") as output:
            json.dump(comptes,output)
        with open("pswords.json","w") as output:
            json.dump(pswToUser,output)
        

        

        return render_template("accueil.html",prenom=prenom)    


if __name__ == '__main__':
    app.run(debug=True)