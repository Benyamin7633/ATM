class Car (object):
    def __init__(self,model,color,company): 
        self.model = model
        self.color = color
        self.company = company
    def start(self):
        print("car starting...")
    def accelerate(self):
        print("car accelerating...")
    def right_turn(self):
        print("car turning right...")


Mercedes = Car("W12","grey","Mercedes")
Mercedes.start()
print(Mercedes.company)
Red_Bull = Car("RB18","black","Red_Bull")
Red_Bull.start()
print(Red_Bull.company)
McLaren = Car("MCL36","orange","McLaren")
McLaren.start()
print(McLaren.company)
Mercedes.accelerate()
print(Mercedes.company)
Red_Bull.accelerate()
print(Red_Bull.company)
McLaren.accelerate()
print(McLaren.company)
Mercedes.right_turn()
print(Mercedes.company)
Red_Bull.right_turn()
print(Red_Bull.company)
McLaren.right_turn()
print(McLaren.company)