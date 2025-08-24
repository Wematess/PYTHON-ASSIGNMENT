open("Coding.pdf","w")
file=open("Coding.pdf","w")
file.write("I am learning to code with python")

file=open("Coding.pdf","r")
content=file.read()
print(content)

try:
    file=open("Learn.pdf","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("file not found please check the file path")
              