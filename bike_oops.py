class bike:
    def __init__(self,vin,brand,model,engine,brake,cost):
        self.a=vin
        self.b=brand
        self.c=model
        self.d=engine
        self.e=brake
        self.f=cost
    def display(self):
        print("VIN:{}".format(self.a))
        print("Brand:{}".format(self.b))
        print("Model:{}".format(self.c))
        print("Engine Displacement:{}".format(self.d))
        print("Brake System:{}".format(self.e))
        print("Cost:{}".format(self.f))
        print("")
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, bike):
            return self.a==other.a and self.b==other.b and self.c==other.c and self.d==other.d and self.e==other.e and self.f==other.f
        return False
print("Bike1 details")
a=bike('MD2GJ3214JR258416','KTM','RC','390cc','Disk',225000.0)
print("Bike2 details")
b=bike('MD2GJ3214JR258416','BMW','RC','390cc','Disk',225000.0)
print("Bike1")
a.display()
print("Bike2")
b.display()
print(a==b)
