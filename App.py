from flask import*
from user import User
import json

jsonPsw = open("pswords.json")
jsonData = open("comptes.json")

accueil_file = open("acceuil.txt","r")

accueil_txt = accueil_file.readlines()
accueil_txt_js = json.dumps(accueil_txt)
 
pswToUser:list[dict[str,str]] = json.load(jsonPsw)
comptes:list = json.load(jsonData)
jsonData.close()
jsonPsw.close()

def lookForUser(prenom, password):
    if comptes.__contains__({"prenom":prenom}):
        if pswToUser.__contains__({password:prenom}):
            return (True,None)
        else:
            return (False, "Mot de passe incorrecte")
    else:
        return (False,"Le compte n'existe pas")    

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
 
    return render_template("accueil.html",prenom="",txt = accueil_txt_js,nlines = len(accueil_txt))

@app.route('/sign-up',methods=["GET"])
def signUp():
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
        

        

        return render_template("accueil.html",prenom=prenom,txt = accueil_txt,nlines = len(accueil_txt))    

@app.get('/login')    
def login():
    message = request.args.get('error_message')


    return render_template("login.html", message = message)

@app.post("/form-login")
def loginForm():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        psw = request.form.get("password")
        udata = lookForUser(prenom, psw)
        if udata[0]:
            return render_template("accueil.html",prenom = prenom,txt = accueil_txt,nlines = len(accueil_txt))
        else:
            return redirect(url_for('login',error_message = udata[1]))
            


if __name__ == '__main__':
    app.run(debug=True)