class SeeMee:
  def youcanseeme(self):
    self.__youcannotseeme()
    
  def __youcannotseeme(self):
    print('you cannot see me')
    
#Outside class    
Check = SeeMee()
Check.youcanseeme()
# you can see me
#Check.__youcannotseeme()
#AttributeError: 'SeeMee' object has no attribute '__youcannotseeme'

