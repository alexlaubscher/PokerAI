import random
import deck
import card
import hand

def equity():
  runs = 0
  hero = 0
  enemy = 0
  nothing = 0
  pair = 0
  twopair = 0
  trips = 0
  straight = 0
  flush = 0
  fullhouse = 0
  quads = 0
  straightflush = 0

  for i in range(25000):
    winner = simulation()
    runs += 1
    if winner == 1:
      hero += 1
    elif winner == -1:
      enemy += 1

  print("hero won " + str(float(hero)/float(runs) * 100) + "%")
  print("enemy won " + str(float(enemy)/float(runs) * 100) + "%")
  print("chop pot " + str(float(runs-hero-enemy)/float(runs) * 100) + "%")

def simulation():
  
  card_list = []
  hero_card_list = []
  enemy_card_list = []
  board_list = []

  deck = Deck.Deck()

  hero_card_list.append(Card.Card(14,"C"))
  deck.setDict("14C")
  hero_card_list.append(Card.Card(14,"S"))
  deck.setDict("14S")
  enemy_card_list.append(Card.Card(13, "H"))
  deck.setDict("13H")
  enemy_card_list.append(Card.Card(13, "S"))
  deck.setDict("13S")

  while len(board_list) != 5:
    board_list.append(deck.genCard())

  hero_card_list += board_list
  enemy_card_list += board_list

  hero_strength, hero_five = getHandStrength(hero_card_list)
  enemy_strength, enemy_five = getHandStrength(enemy_card_list)

  hero_hand = Hand(hero_five, hero_strength)
  enemy_hand = Hand(enemy_five, enemy_strength)
  result = compareHands(hero_hand,enemy_hand)

  return result


def getHandStrength(card_list):
  strength = 0
  hand = []
  strength, hand = check_straight_flush(card_list)
  if strength == 0:
    strength, hand = check_quads(card_list)
  if strength == 0:
    strength, hand = check_full_house(card_list)
  if strength == 0:
    strength, hand = check_pairs(card_list)
  return strength, hand
  
    
def check_pairs(card_list):
  values_list = []
  hand_list = []
  pairs = 0
  if (type(card_list[0]) == int):
    values_list = card_list
  else:
    for card in card_list:
      values_list.append(card.getValue())
    values_list.sort(reverse=True)
  for i in range(len(values_list) - 1):
    if values_list[i] == values_list[i+1] and values_list[i] != -1:
      if len(hand_list) < 4:  
        pairs += 1
        hand_list.append(values_list[i])
        hand_list.append(values_list[i+1])
        values_list[i] = -1
        values_list[i+1] = -1

  values_list.sort(reverse=True)
  index = 0
  while(len(hand_list) != 5):
    hand_list.append(values_list[index])
    index += 1
  return pairs, hand_list

def check_full_house(card_list):
  values_list = []
  hand_list = []
  strength = 0

  for card in card_list:
    values_list.append(card.getValue())
  values_list.sort(reverse=True)

  for i in range(len(values_list) - 2):
    if values_list[i] == values_list[i+1] and values_list[i] == values_list[i+2]:
      strength = 3
      hand_list.append(values_list[i])
      hand_list.append(values_list[i+1])
      hand_list.append(values_list[i+2])
      values_list[i] = -1
      values_list[i+1] = -1
      values_list[i+2] = -1
      break

  if strength == 3:
    pair, pair_list = check_pairs(values_list)
    if pair != 0:
      strength = 6
      hand_list.append(pair_list[0])
      hand_list.append(pair_list[1])
    else:
      index = 0
      while(len(hand_list) != 5):
        hand_list.append(pair_list[index])
        index += 1
  return strength, hand_list

  
def check_quads(card_list):
  values_list = []
  hand_list = []
  strength = 0
  
  for card in card_list:
    values_list.append(card.getValue())
  values_list.sort(reverse=True)
  for i in range(len(values_list) - 3):
    if values_list[i] == values_list[i+1] and values_list[i] == values_list[i+2] and values_list [i] == values_list[i+3]:
      hand_list.append(values_list.pop(i))
      hand_list.append(values_list.pop(i))
      hand_list.append(values_list.pop(i))
      hand_list.append(values_list.pop(i))
      strength = 7
      break

  index = 0
  while len(hand_list) != 5:
    hand_list.append(values_list[index])
    index += 1

  return strength, hand_list
    
def check_straight_flush(card_list):
    flush = False
    straight = False
    strength = 0
    hand_list = []

    flush, flush_list = check_flush(card_list)
    straight, straight_list = check_straight(card_list)
   
    if flush == True and straight == True:
      if flush_list == straight_list:
        strength = 8
        hand_list += straight_list[:5]
      else:
        strength = 5
        hand_list += flush_list
    elif flush == True and straight == False:
      strength = 5
      hand_list += flush_list
    elif flush == False and straight == True:
      strength = 4
      hand_list += straight_list

    return strength, hand_list

def check_straight(card_list):
    straight = False
    hand_list = []
    values_list = []
    high_index = -1

    for card in card_list:
      values_list.append(card.getValue())
    
    values_list.sort(reverse=True)
    counter = 0
    if values_list[0] == 14:
      values_list.append(1)
    for i in range(len(values_list) - 1):
      if values_list[i] == (values_list[i+1] + 1):
        hand_list.append(values_list[i])
        if counter == 3:
          hand_list.append(values_list[i+1])
          straight = True
          break
        counter += 1
      elif values_list[i] == values_list[i+1]:
        pass
      else:
        if counter == 4:
          stright = True
          break
        else:
          counter = 0

    return straight, hand_list
    
def check_flush(card_list):
    flush = 0
    hand_list = []
    high_value = -1
    flush_count = 0
    
    for card in card_list:
      flush_count = 0
      suit_store = card.getSuit()
      for check in card_list:
        if suit_store == check.getSuit():
          hand_list.append(check.getValue())
          flush_count += 1
      if flush_count >= 5:
        break
      else:
        hand_list = []

    if flush_count >= 5:
      flush = True
      hand_list.sort(reverse=True)
      if len(hand_list) > 5:
        hand_list = hand_list[0:5]
    
    return flush, hand_list
      

def compareHands(hero_hand, enemy_hand):
  hero_strength = hero_hand.getStrength()
  enemy_strength = enemy_hand.getStrength()
  hero_list = hero_hand.getHand()
  enemy_list = enemy_hand.getHand()
  if hero_strength > enemy_strength:
    return 1
  elif hero_strength < enemy_strength:
    return -1
  else:
    for i in range(5):
      if hero_list[i] > enemy_list[i]:
        return 1
      elif enemy_list[i] > hero_list[i]:
        return -1
    return 0   

    
equity()

