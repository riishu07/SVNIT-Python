class PasswordManager:
    def __init__(self):
        self.passwords = []

    def getPassword(self):
        if self.passwords:
            return self.passwords[-1]
        return None

    def setPassword(self, newPassword):
        if newPassword not in self.passwords:
            self.passwords.append(newPassword)

    def isCorrect(self, password):
        return password == self.getPassword()


pwdMng = PasswordManager()
pwdMng.setPassword("pass2")
print(pwdMng.getPassword())  
print(pwdMng.isCorrect("pass1")) 
pwdMng.setPassword("pass2")