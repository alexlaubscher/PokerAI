class Hand:
  def __init__(self,hand_list,strength=0):
    self.hand_list = hand_list
    self.strength = strength

  def getHand(self):
    return self.hand_list

  def getStrength(self):
    return self.strength
