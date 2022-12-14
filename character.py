class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    #subclass of character class
class Enemy(Character):
    def __init__(self,char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        
    def set_weakness(self, weak):
        self.weakness = weak
        
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("you fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you")
            return False
