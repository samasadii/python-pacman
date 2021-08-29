sc=open("highscore.txt","r")
hscore=sc.read()
sc.close()
hscore=int(hscore)
print hscore
print type(hscore)
if score>hscore:
    hscore=score
sc=open("highscore.txt","w")
sc.write(str(hscore))
sc.close
