import random, math

#剑客
class Warriors:
    
    def __init__(self, name, kongfu, attackMax, defenceMax):
        self.name = name
        self.energyValue = kongfu
        self.attack_value = attackMax
        self.defence_value = defenceMax
    #攻击力
    def attack(self):
        return self.attack_value * (random.random() + .5)
    #防守力
    def defence(self):
        return self.defence_value * (random.random() + .5)

#比武
class Battles:
    def launchattack(self, Warrior1, Warrior2):
        while True:
            if self.fight(Warrior1, Warrior2) == 'Game Over':
                print('Game Over')
                break
            if self.fight(Warrior2, Warrior1) == 'Game Over':
                print('Game Over')
                break

    @staticmethod
    def fight(warriorA, warriorB):
        attackAmount = warriorA.attack()
        defendAmount = warriorB.defence()
        damageAmount = math.ceil(attackAmount - defendAmount)
        warriorB.energyValue = warriorB.energyValue - damageAmount

        print('{}进攻， {}防守， 此次伤害{}， {}的战斗力下降到{}'.format(warriorA.name, warriorB.name, damageAmount, warriorB.name, warriorB.energyValue))

        if warriorB.energyValue <= 0:
            return 'Game Over'
        else:
            return 'Continue fight'

blowSnow = Warriors('西门吹雪',50,20,10)
longCity = Warriors('叶孤城',50,20,10)

forbidenCity = Battles()
forbidenCity.launchattack(blowSnow, longCity)