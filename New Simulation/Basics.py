
class Service():
    def __init__(self):
        self.id = id
        self.name = name

class DeviceType():
    type_name = ""
    # Smartphone = 1
    # car = 2
    # Tablet = 3
    # Smart fitness = 4
    # Smart watch = 5
    # PC = 6
    # Printer = 7
    # Home Sensor = 8
    # Point of Interest = 9
    # Environment and Weather = 10
    # Transportation = 11
    # Indicator = 12
    # Garbage Truck = 13
    # Street Light = 14
    # Parking = 15
    # Alarms = 16


class User():
    def __init__(self):
        self.id = id
        self.name = name
    User_device_list=[]


    def __str__(self):
        return str(self.pk)


class Device(id,value,energy,type,model,user, edge_node,x_co, y_co):
    def __init__(self):
        self.value = value
        self.energy = energy
        self.type = type
        self.model = model
        self.user = user
        self.id = id
        self.edge_node = edge_node
        self.x_co = x_co
        self.y_co = y_co

    def price_calculator(self):
        #calculating device price
        return price

    def value_update(self):
        #update device value in time
        return value

    def energy_update(self):
        #update device energy
        return energy

    def price_calculator(self):
        #calculating device prive
        return price

    device_in_range=[]

    def add_device(id):
        #check distance and relations
        return True






    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING, related_name='devices')
    brand = models.CharField(max_length=1000)
    model = models.CharField(max_length=1000)
    services = models.ManyToManyField(Service)
    lat = models.CharField(max_length=1000)
    long = models.CharField(max_length=1000)
    weight = models.IntegerField(default=random.randint(1, 99))
    trust = models.IntegerField(default=random.randint(1, 99))
    security = models.IntegerField(default=random.randint(1, 99))
    accuracy = models.IntegerField(default=random.randint(1, 99))
    charge = models.IntegerField(default=random.randint(1, 99))

    def evaluator(self):
        return int((self.trust + self.security + self.accuracy + self.charge)/4)

    def __str__(self):
        return str(self.pk)


class Edge_node(id, x_co, y_co):
    def __init__(self):
        self.id = id
        self.edge_node = edge_node
        self.x_co = x_co
        self.y_co = y_co

    Device_list=[]
    def add_device(id):
        #check distance and relations
        return True

    def check_resources(Device_list):
        #check available resources
        return x
