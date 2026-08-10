import random
class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.max_health = health
        # remember the starting value
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    def take_damage(self, amount):
        dmg = max(1, amount - self.defense)
        self.health -= dmg
        return dmg

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        pass
        # base attack — subclasses will override this
class Worrior(Character):
    def __init__(self,name):
        super().__init__(name, 130, 22, 12, 6)
        self.rage=0
    def attack(self, target):
        raw_damage=self.attack_power
        if self.health< 0.3*self.max_health:
            raw_damage *= 2
            print(f"💢 {self.name} (Warrior) enters Berserk Mode! Attack power increased.")
            print(f"⚔ Thor (Warrior) strikes with double power! Deals {raw_damage} damage.")
        damage=target.take_damage(raw_damage)
        print(f"⚔ {self.name} (Warrior) swings a sword! Deals {damage} damage.")
class Mage(Character):
    def __init__(self,name):
        super().__init__(name,90,30,5,8)
        self.mana=100
    def attack(self, target):
            raw_damage=self.attack_power
            if self.mana>=50:
                raw_damage=1.5*self.attack_power
                self.health-=5
            damage=target.take_damage(raw_damage)
            print(f"🔥 {self.name} (Mage) casts Fireball! Deals {damage} damage but loses {self.health} health.")
    
class Archer(Character):
    def __init__(self,name):
        super().__init__(name,100,24,7,12)
        self.critical_chance=0.30
    def attack(self, target):
            raw_damage=self.attack_power
            if random.random()<self.critical_chance:
                raw_damage *=2
                print(f"🎯 Alex (Archer) lands a Critical Hit! Deals {raw_damage} damage.")
            damage=target.take_damage(raw_damage)
            print(f"🏹 {self.name} (Archer) shoots an arrow! Deals {damage} damage.")
Thor=Worrior("Thor")
Alex=Archer("Alex")
Gandalf=Mage("Gandalf")
lst=[Thor,Alex,Gandalf]
# print(lst)
lst.sort(key=lambda fighter:fighter.speed,reverse=True)
round_no = 1
while sum(fighter.is_alive() for fighter in lst) > 1:
    # print(f"\n========== ROUND {round_no} ==========")
    for fighter in lst:
        # Skip defeated fighters
        if not fighter.is_alive():
            continue
        # Find alive opponents
        targets = [ opponent for opponent in lst if opponent != fighter and opponent.is_alive()]
        # No opponent left
        if not targets:
            break
        # Attack the first alive opponent
        target = targets[0]
        fighter.attack(target)
        # Check if target was defeated
        if not target.is_alive():
            print(f"💀 {target.name} ({target.__class__.__name__}) is defeated!")
        # Stop immediately if only one fighter remains
        if sum(f.is_alive() for f in lst) == 1:
            break
    round_no += 1
champion=next(fighter for fighter in lst if fighter.is_alive())
print(f"{champion.name} ({champion.__class__.__name__}) wins the battle!")