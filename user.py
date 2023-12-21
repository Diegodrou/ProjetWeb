class User:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0],str):
            self.prenom = args[0]
        elif len(args) == 1 and isinstance(args[0],dict):
            self.prenom = args[0]["prenom"]

    
    def serialize(self):
        return {"prenom":self.prenom}
