class Automobile():
    #Define a constructor
    #The constructor defines what happens when we create a automobile
    def __init__(self, make, model, vin, engine_size, owner):
        #Assign parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
