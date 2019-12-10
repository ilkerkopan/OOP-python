from property import Property

class Apartment(Property):
    def __init__(self, balcony='', elevator='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.elevator = elevator
        
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("has elevator: %s" % self.elevator)
        print("has balcony: %s" % self.balcony)
        
    def prompt_init():
        parent_init = Property.prompt_init()
        balcony = input("Does the property have a balcony? [yes] [no]")
        elevator = input("Does the property has an elevator? [yes] [no]")
        parent_init.update({"elevator": elevator,"balcony": balcony})
        return parent_init
    
    prompt_init = staticmethod(prompt_init)
