
# Online Python - IDE, Editor, Compiler, Interpreter

y=input("Enter any word in  : ")
c=y.lower()
print("The word in Lower case letters : ",c)
#IRISH LANGUAGE
r = input("Enter any word in irish  letters : ")
if (r[0] == 'n' or r[0] == 't') and (r[1] == 'A' or r[1] == 'E' or r[1] == 'I' or r[1] == 'O' or r[1] == 'U' or r[1] == 'Á' or r[1] == 'É' or r[1] =='Í' or r[1] =='Ó' or r[1] == 'Ú'):
    print(r[0].rstrip(),'-',r[1:].lower())
else:
    print(r.lower())
#GREEK language
O=input("Enter any word in greek  letters: ")
c=O.lower()
print("The word in greek lower letters : ",c)
#TURKISH language
def _init_(self,word,language):
    self.w = word
    self.l = language
def setlower(self):
    if self.l == 'tr':
        word = self.w.replace('\u0049','\u0131')
        return self.w.lower()