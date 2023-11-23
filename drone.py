
class Drone():
    def __init__(self,ip,number,model,tipo):
        self.ip = ip
        self.number = number
        self.model = model
        self.tipo = tipo
        self.battery = 0
        self.status = "Idle"
        self.accelaration_x = 0
        self.accelaration_y = 0
    
    def set_battery(self, novabateria):
        self.battery = novabateria

    def set_model(self,modelo):
        self.model = modelo
        





drone1 = Drone("192.168.1.10",1,"tello","Boost")
drone2 = Drone("192.168.1.100",2,"tello","fast")

print(drone1.tipo)
print(drone2.tipo)

print(drone1.battery)

drone1.set_battery(80)

print(drone1.battery)