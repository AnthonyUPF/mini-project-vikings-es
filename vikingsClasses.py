import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health=health
        self.strength=strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health-=damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name=name 
        super().__init__(health,strength)
    
    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        super().receiveDamage(damage)
        if (self.health>0):
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


   # Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        # your code here
        super().receiveDamage(damage)
        if (self.health>0):
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
#yop
class War2:

    def __init__(self):
        # your code here
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        # your code here
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        # your code here
        self.saxonArmy.append(Saxon)
 
    def vikingAttack(self):
        # your code here
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        if (saxon.health-viking.attack()<=0):
            self.saxonArmy.remove(saxon)
        return saxon.receiveDamage(viking.attack())

    def saxonAttack(self):
        # your code here
        saxon=random.choice(self.saxonArmy) 
        viking=random.choice(self.vikingArmy)
        if (viking.health-saxon.attack()<=0):
            self.vikingArmy.remove(viking)
        return viking.receiveDamage(saxon.attack())


    def showStatus(self):
        # your code here
        if(len(self.vikingArmy)>0 and len(self.saxonArmy)>0):
            return "Vikings and Saxons are still in the thick of battle."
        elif(len(self.saxonArmy)<1):
            return "Vikings have won the war of the century!"
        else:
            return "Saxons have fought for their lives and survive another day..."

    pass



# Davicente

class War(War2):
    def __init__(self):
        # your code here
        super().__init__()
"""
    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here

    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass
"""

