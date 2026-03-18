from Character import Character

class Novice(Character):
    def basicAttack(self, Character):
        Character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
        
username = input("Enter Your Username:")
user_Character = Character(username)
print(user_Character.getUsername())
print(user_Character.getHp())