class Enemy:
    def __init__(self, health, distance, size):
        self.health = health
        self.distance = distance
        self.size = size

    def takeDamage(self, damage):
        self.health -= damage