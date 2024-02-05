# create a function to convrt emo. into emoji
def convert(face):
    face1=face.replace(':)', '🙂')
    face2=face1.replace(':(','🙁')
    return face2


#input to the user
msg=input("inter chat ")
#call the funtion
result=convert(msg)
#output
print(result)
