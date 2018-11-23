class Card:
    #constructs card
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        self.valueDict = {14:"A",2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"T",11:"J",12:"Q",13:"K"}

    #returns value
    def getValue(self):
        return self.value

    #returns suit
    def getSuit(self):
        return self.suit

    #returns string w value and suit
    def __str__(self):
        return str(self.valueDict[self.value])+self.suit
    