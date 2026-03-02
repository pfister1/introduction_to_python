#opening a file
f = open("demo")
print(f.read())

#opening a file using with statement
with open("demo") as f:
    print(f.read())

#readline and close
with open("demo") as f:
    print(f.readline())
f.close()

#looping
with open("demo") as f:
    for x in f:
        print(x)

#appending
with open("demo", "a") as f:
    f.write("more content")
with open("demo") as f:
    print(f.read())

#overwritting a text
with open("demo", "w") as f:
    f.write("oops i have overwritten the content")
with open("demo") as f:
    print(f.read())

#creating a new file
f = open("myfile.txt", "x")
x = open("other_file", "x")

#removing a file
import os
os.remove("myfile.txt")

#check if file exists
import os
if os.path.exists("other_file"):
    os.remove("other_file")
else:
    print("file does not exist")

 #delete a folder
import os
os.rmdir("exist")

#creating new folder.
import os
os.mkdir("newfile")