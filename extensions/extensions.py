# input from the user
ext = input("File name: ")

# create conditions
if ext.lower().strip().endswith(".gif"):
    print("image/gif")

elif ext.lower().strip().endswith((".jpg" ,".jpeg")):
    print("image/jpeg")

elif ext.lower().strip().endswith(".png"):
    print("image/png")

elif ext.lower().strip().endswith(".pdf"):
    print("application/pdf")

elif ext.lower().strip().endswith(".txt"):
    print("text/plain")

elif ext.lower().strip().endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")