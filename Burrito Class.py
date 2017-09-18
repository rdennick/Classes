#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Make your own burrito using classes
class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

            
            
            
class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
            
class Burrito:
    def __init__(self,meat,to_go,rice,beans,extra_meat = False,guacamole= False,cheese = False, pico = False, corn = False):
        self.meat = Meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.extra_meat = self.set_extra_meat(extra_meat)
        self.guacamole = self.set_guacamole(guacamole)
        self.cheese = self.set_cheese(cheese)
        self.pico = self.set_pico(pico)
        self.corn = self.set_corn(corn)
        
    def get_meat(self):
        return self.meat.get_value()
        
    def get_to_go(self):
        return self.to_go
    
    def get_rice(self):
        return self.rice.get_value()
    
    def get_beans(self):
        return self.beans.get_value()
    
    def get_extra_meat(self):
        return self.extra_meat
    
    def get_guacamole(self):
        return self.guacamole
        
    def get_cheese(self):
        return self.cheese
    
    def get_pico(self):
        return self.pico
    
    def get_corn(self):
        return self.corn
        
    def get_cost(self):
        burrito = 5
        if self.meat.get_value() in ["chicken","pork","tofu"]:
            burrito += 1
        if self.meat.get_value() in ["steak"]:
            burrito += 1.5
        if self.extra_meat == True and self.meat.get_value() != False:
            burrito += 1
        if self.guacamole == True:
            burrito += .75
        return burrito
    
    def set_meat(self,meat):
        self.meat = Meat(meat)
                   
    def set_to_go(self,to_go):
        if to_go == True or to_go == False:
            self.to_go = to_go
            return self.to_go
        else:
            return False
        
    def set_rice(self,rice):
        self.rice = Rice(rice)
    
    def set_beans(self,beans):
        self.beans = Beans(beans)
    
    def set_extra_meat(self,extra_meat):
        if extra_meat == True or extra_meat == False:
            self.extra_meat = extra_meat
            return self.extra_meat
        else:
            return False
    
    def set_guacamole(self,guacamole):
        if guacamole == True or guacamole == False:
            self.guacamole = guacamole
            return self.guacamole
        else:
            return False
            
    def set_cheese(self,cheese):
        if cheese == True or cheese == False:
            self.cheese = cheese
            return self.cheese
        else:
            return False
    
    def set_pico(self,pico):
        if pico == True or pico == False:
            self.pico = pico
            return self.pico
        else:
            return False
            
    def set_corn(self,corn):
        if corn == True or corn == False:
            self.corn = corn
            return self.corn
        else:
            return False  
        
myBurrito = Burrito("chicken",True,"brown",False)
myBurrito.set_cheese(True)
myBurrito.set_pico(True)
myBurrito.set_guacamole(True)
myBurrito.set_corn(True)
print(myBurrito.get_cost())
print(myBurrito.get_pico())
print(myBurrito.get_extra_meat())
