with open('test.txt','w') as file:
    file.write("hello")
with open('test.txt','a') as file:
    file.write(" bro")
with open('test.txt','r') as file:
    text = file.read()
    print(text)