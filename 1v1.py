from random import choice

e_health = 100
p_health = 100

dialoges_a_a = ['You both swing your swords and are both injured losing 10 health\n ', 'Your swords clash and both of you are slightly injured, losing 10 health\n ', 'Swords fly and both combatants sustain injuries. You have each lost 10 health\n ']
dialog_a_a = choice(dialoges_a_a)

dialoges_b_a = ['The knight swings his sword at your head, but you raise you shield in time to block it.\n ', 'The knight attacks you and you raise your shield, enduring the onslaught.\n ', 'Out of the corner of your eye you spot a sword flying at your head and you raise your shield just in time to block it.\n ']
dialog_b_a = choice(dialoges_b_a)

dialoges_h_a = ['You duck away and wrap a bandage around your arm, but the knight rushes in and strikes you, dealing 10 damage.\n ', 'You try to escape and heal up, but the knight attacks in your moment of weakness. You have lost 10 health.\n ', 'You wrap a bandage around your leg, but when your sword is down the knight attacks and deals 10 damage.\n ']
dialog_h_a = choice(dialoges_h_a)

dialoges_a_m = ['You attack the knight and he tries to block with his shield, but is not quick enough. You dealt 20 damage.\n ', 'You advance on the knight and he hurries to raise his shield, but your sword strikes home. You dealt 20 damage.\n ', 'Your sword flies at the knight, but his shield is not up in time. You dealt 20 damage.\n ']
dialog_a_m = choice(dialoges_a_m)

dialoges_b_m = ['You both raise your shields to block, but the knight stumbles and falls.\n ', 'Both shields are raised, but the knight clumsily drops his.\n ', 'You each raise your shields in preperation, but the knight trips and falls.\n ']
dialog_b_m = choice(dialoges_b_m)

dialoges_h_m = ['You back away and heal up, but the knight swings his sword at you. Luckily he misses and you have time to prepare for his next move. You regained 10 health.\n ', 'The knight swings his sword at you and misses. You sue the precious seconds to heal up. You have gained 10 health.\n ', 'You take a chance and heal up, but the knight rushes in as attacks. Luckily he trips and has to retreat before you bring up your sword again. You have gained 10 health.\n ']
dialog_h_m = choice(dialoges_h_m)

dialoges_a_b = ['You attack the knight, but he raises his sheild and blocks your swing.\n ', 'You swing your sword at the knights head, but he blocks you with his shield.\n ', 'You rush at the knight and swing you sword, but he blocks you with his shield.\n ']
dialog_a_b = choice(dialoges_a_b)

dialoges_b_b = ['You both raises your shields to block and an awkward silence arises.\n ', 'You both raises your shields in preperation for an attack that will never come.\n ', 'You both cower in fear behind your shields and nothing happens.\n ']
dialog_b_b = choice(dialoges_b_b)

dialoges_h_b = ['You heal yourself and the knight, confused, raises his shield to block. You have gained 10 health.\n ', 'You use a bandage, while the knight hides behind his shield ready for your attack. You have gained 10 health.\n ', 'You heal up, while the knight raises his shield ready for your next attack. You have gained 10 health.\n ']
dialog_h_b = choice(dialoges_h_b)

dialoges_a_h = ['The knight backs away and tries to heal, but you are on him in a second. You have dealt 10 damage.\n ', 'The knight tries to escape and heal up, but you catch him off guard and deal 10 damage.\n ', 'The knight tries to run away and heal, but you catch him and strike, dealing 10 damage.\n ']
dialog_a_h = choice(dialoges_a_h)

dialoges_b_h = ['You raise you shield, ready to block, but the knight backs away and heals, gaining 10 health\n ', 'You prepare to block, but the knight retreats and heals, gaining 10 health.\n ', 'You prepare to defend yourself, but the knight backs away and heals, gaining 10 health.\n ']
dialog_b_h = choice(dialoges_b_h)

dialoges_h_h = ['You both back away and heal. You each gain 10 health.\n ', 'You each use a bandage and gain 10 health.\n ', 'You both retreat and heal, gaining 10 health each.\n ']
dialog_h_h = choice(dialoges_h_h)



while p_health > 0 and e_health > 0:
    
    inp = input('What is your next choice? ')

    fight = ['Attacked', 'Attacked', 'Attacked', 'Attacked', 'Blocked', 'Blocked', 'Blocked', 'Blocked', 'Missed', 'Missed', 'Healed', 'Healed']
    ai = choice(fight)

    if inp == 'attack' and ai == 'Attacked':
        print(dialog_a_a)
        p_health -= 10
        e_health -= 10
    elif inp == 'block' and ai == 'Attacked':
        print(dialog_b_a)
    elif inp == 'heal' and ai == 'Attacked':
        print(dialog_h_a)
        p_health -= 10
    elif inp == 'attack' and ai == 'Missed':
        print(dialog_a_m)
        e_health -= 20
    elif inp == 'block' and ai == 'Missed':
        print(dialog_b_m)
    elif inp == 'heal' and ai == 'Missed':
        print(dialog_h_m)
        p_health += 10
    elif inp == 'attack' and ai == 'Blocked':
        print(dialog_a_b)
    elif inp == 'block' and ai == 'Blocked':
        print(dialog_b_b)
    elif inp == 'heal' and ai == 'Blocked':
        print(dialog_h_b)
        p_health += 10
    elif inp == 'attack' and ai == 'Healed':
        print(dialog_a_h)
        e_health -= 10
    elif inp == 'block' and ai == 'Healed':
        print(dialog_b_h)
        e_health += 10
    elif inp == 'heal' and ai == 'Healed':
        print(dialog_h_h)
        p_health += 10
        e_health += 10
    else:
        print('That is not an option. Try again.')

    print('''Your enemy's health is: ''' + str(e_health))
    print('Your health is: ' + str(p_health))
    print(' ')

    if p_health <= 0:
        break
    if e_health <= 0:
        break

if e_health <= 0:
    print('''
        
        
        
    You have won! Congratulations!
        
        
        
    ''')

if p_health <= 0:
    print('''
        
        
        
    You have lost! Try again.
        
        
        
    ''')