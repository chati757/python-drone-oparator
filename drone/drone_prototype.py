class dog:
    #constructor 
    #ex gender = famale < it's class variable
    def __init__(self,name,age):
        #slef name < it's instance variable
        self.name = name
        self.age = age
        self.data = None
 
    def say_hello(self):
        print 'Hello, my name is', self.name
        self.data = 8+3
 
    def say_age(self):
        print 'I am', self.age, 'years old'
        return 5