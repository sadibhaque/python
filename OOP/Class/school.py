class student:
    def __init__(self, name, id, claass):
        self.name = name
        self.id = id
        self.claass = claass

    def __repr__(self) -> str:
        return f"Name : {self.name}\nID : {self.id}\nClass : {self.claass}"
    
class teacher:
    def __init__(self, name, id, sub):
        self.name = name
        self.id = id
        self.sub = sub
    def __repr__(self) -> str:
        return f"Name : {self.name}\nID : {self.id}\nSub : {self.sub}"


class school:
    def __init__(self, name):
        self.name = name
        self.teachers = []
    
    def add_teacher(self, name, id, sub):
        id = len(self.teachers) + 101
        t1 = teacher(name, id, sub)
        self.teachers.append(t1)


s1 = teacher("Drifter",32,10)
t1 = teacher("Mendax",221,"Physics")

print(s1)
print(t1)