from random import choice

# Player and Enemy Health:

p1_health = 100
p2_health = 100

# Introduction and How to Play:

print('''
                \        / !**** !     !**** !****! !\  /! !****   **!** !****! o
                 \  /\  /  !---- !     !     !    ! ! \/ ! !----     !   !    !
                  \/  \/   !____ !____ !____ !____! !    ! !____     !   !____! o   

!    / !\    ! **!** !*****  !     ! ***!*** !\    /!     /\    !******  ***!*** !****** !******! !*!
!   /  ! \   !   !   !       !     !    !    ! \  / !    /  \   !           !    !       !      ! ! !
!--<   !  \  !   !   !       !-----!    !    !  \/  !   /----\  !******!    !    !------ !______! ! !
!   \  !   \ !   !   !  ***! !     !    !    !      !  /      \        !    !    !       !    \   !_!
!    \ !    \! __!__ !_____! !     !    !    !      ! /        \ ______!    !    !______ !     \  [_]

              !\  /! !    ! !     **!** **!** !****! !       /\   \   / !**** !****! !
              ! \/ ! !    ! !       !     !   !____! !      /--\   \_/  !---- !____! !
              !    ! !____! !____   !   __!__ !      !____ /    \   !   !____ !   \  o
''')

print('''
How to play:
Welcome to Knight Master Multiplayer! In this game, you will fight your friend (the opposing knight) until one of you is the victor. To play, you must each choose between "attack up", "attack down", "attack forward", "block", or "heal". "attack up" beats "attack down", "attack down" beats "attack forward", "attack forward" beats "attack up", and "block" blocks all attacks. Healing will regain 20 health points if executed correctly. Have fun and good luck!
''')

# Actual Game:

while p1_health > 0 and p2_health > 0:
    
    inp = input('Player 1, what is your choice? ')
    inp2 = input('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Player 2, what is your choice? ')

    if inp == 'attack up' and inp2 == 'attack up':
        print('\nYour swords clash and no one rises the victor.\n ')
    elif inp == 'attack up' and inp2 == 'attack down':
        print('\nAttack Up beats Attack Down. Player 2 lost 20 health.\n ')
        p2_health -= 20
    elif inp == 'attack up' and inp2 == 'attack forward':
        print('\nAttack Forward beats Attack Up. Player 1 lost 20 health\n ')
        p1_health -= 20
    elif inp == 'attack up' and inp2 == 'block':
        print('\nPlayer 2 blocked. No damage dealt.\n ')
    elif inp == 'attack up' and inp2 == 'heal':
        print('\nPlayer 2 healed, but was attacked. Player 2 lost 10 health.\n ')
        p2_health -= 10
    elif inp == 'attack down' and inp2 == 'attack up':
        print('\nAttack Up beats Attack Down. Player 1 lost 20 health.\n ')
        p1_health -= 20
    elif inp == 'attack down' and inp2 == 'attack down':
        print('\nYour swords clash and no one rises the victor.\n ')
    elif inp == 'attack down' and inp2 == 'attack forward':
        print('\nAttack Down beats Attack Forward. Player 2 lost 20 health.\n ')
        p2_health -= 20
    elif inp == 'attack down' and inp2 == 'block':
        print('\nPlayer 2 blocked. No damage dealt.\n ')
    elif inp == 'attack down' and inp2 == 'heal':
        print('\nPlayer 2 healed, but was attacked. Player 2 lost 10 health.\n ')
        p2_health -= 10
    elif inp == 'attack forward' and inp2 == 'attack up':
        print('\nAttack Forward beats Attack Up. Player 2 lost 20 health.\n ')
        p2_health -= 20
    elif inp == 'attack forward' and inp2 == 'attack down':
        print('\nAttack Down beats Attack Forward. Player 1 lost 20 health.\n ')
        p1_health -= 20
    elif inp == 'attack forward' and inp2 == 'attack forward':
        print('\nYour swords clash and no one rises the victor.\n ')
    elif inp == 'attack forward' and inp2 == 'block':
        print('\nPlayer 2 blocked. No damage dealt.')
    elif inp == 'attack forward' and inp2 == 'heal':
        print('\nPlayer 2 healed, but was attacked. Player 2 lost 10 health.\n ')
        p2_health -= 10
    elif inp == 'block' and inp2 == 'attack up':
        print('\nPlayer 1 blocked. No damage dealt.\n ')
    elif inp == 'block' and inp2 == 'attack down':
        print('\nPlayer 1 blocked. No damage dealt.\n ')
    elif inp == 'block' and inp2 == 'attack forward':
        print('\nPlayer 1 blocked. No damage dealt.\n ')
    elif inp == 'block' and inp2 == 'block':
        print('\nYour shields raise and no one attacks.\n ')
    elif inp == 'block' and inp2 == 'heal':
        print('\nPlayer 1 blocked, accomplishing nothing, and Player 2 healed. Player 2 gained 20 health.\n ')
        p2_health += 20
    elif inp == 'heal' and inp2 == 'attack up':
        print('\nPlayer 1 healed, but was attacked. Player 1 lost 10 health.\n ')
        p1_health -= 10
    elif inp == 'heal' and inp2 == 'attack down':
        print('\nPlayer 1 healed, but was attacked. Player 1 lost 10 health.\n ')
        p1_health -= 10
    elif inp == 'heal' and inp2 == 'attack forward':
        print('\nPlayer 1 healed, but was attacked. Player 1 lost 10 health.\n ')
        p1_health -= 10
    elif inp == 'heal' and inp2 == 'block':
        print('\nPlayer 1 healed and Player 2 blocked, accomplishing nothing. Player 1 gained 20 health.\n ')
        p1_health += 20
    elif inp == 'heal' and inp2 == 'heal':
        print('\nBoth Players healed. Player 1 and Player 2 gained 20 health.\n ')
        p1_health += 20
        p2_health += 20
    else:
        print('That is not an option. Try again.\n ')
    
    print('''Player 1's health is: ''' + str(p1_health))
    print('''Player 2's health is: ''' + str(p2_health))
    print(' ')

    if p1_health <= 0:
        break
    if p2_health <= 0:
        break

# Output at Game Ending:

if p2_health <= 0:
    print('''

!****! !       /\   \   / !**** !****!    /!     \        / **!** !\  ! !****  !!
!____! !      /--\   \_/  !---- !____!     !      \  /\  /    !   ! \ ! !____  !!
!      !____ /    \   !   !____ !   \    __!__     \/  \/   __!__ !  \!  ____! []

''')

if p1_health <= 0:
    print('''

!****! !       /\   \   / !**** !****!   ****!   \        / **!** !\  ! !****  !!
!____! !      /--\   \_/  !---- !____!   ____!    \  /\  /    !   ! \ ! !____  !!
!      !____ /    \   !   !____ !   \   !____      \/  \/   __!__ !  \!  ____! []

''')