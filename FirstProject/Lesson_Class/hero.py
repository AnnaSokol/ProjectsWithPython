class Hero():
    """Class to create Hero for game"""
    def __init__(self, name, level, race):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of this Hero"""
        discription = (self.name + " Level is: " + str(self.level) + ", Race is: " + self.race + ", Health is " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level += 1

    def move(self):
        """start moving hero"""
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health