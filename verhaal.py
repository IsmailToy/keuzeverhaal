rungame = 0
Verhaallijn2 = 0
Verhaallijn3 = 0
Verhaallijn4 = 0
Verhaallijn5 = 0
Verhaallijn6 = 0
Verhaallijn7 = 0
Verhaallijn8 = 0
Verhaallijn9 = 0
Verhaallijn10 = 0
Verhaallijn11 = 0
Verhaallijn12 = 0
Verhaallijn13 = 0
Verhaallijn14 = 0
Verhaallijn15 = 0
Verhaallijn16 = 0
Verhaallijn17 = 0
Verhaallijn18 = 0
Verhaallijn19 = 0
Verhaallijn20 = 0
Verhaallijn21 = 0
Verhaallijn22 = 0
Verhaallijn23 = 0
Verhaallijn24 = 0
Verhaallijn25 = 0
Verhaallijn26 = 0

print("Your name is Johanalipo Vevu Lupe. You live in Uganda but because of the ecenomic downfall Amerika sought out to take over Uganda because of the minerals. You're debating whether you want to run away from Uganda and try or find somewhere else to live. But the choice is up to you..." )
print("What do you decide to do? FLEE or STAY" )
choice = input()
if choice == 'FLEE':
    Verhaallijn2 += 1
elif choice == 'STAY':
    Verhaallijn3 += 1
else:
    print(choice, " wasn't a valid choice")

if Verhaallijn2 == 1:
    print("You fleed from Uganda. You want to go to a safer country called The Netherlands. Do you take a PLANE, BOAT or TRAIN?" )
    choice = input()
    if choice == 'PLANE':
        Verhaallijn4 += 1
    elif choice == 'BOAT':
        Verhaallijn5 += 1
    elif choice == 'TRAIN':
        Verhaallijn6 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn3 == 1:
    print("You decided to stay in Uganda, do you HIDE or FIGHT?" )
    choice = input()
    if choice == 'HIDE':
        Verhaallijn7 += 1
    elif choice == 'FIGHT':
        Verhaallijn8 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn4 == 1:
    print("You decide to take a plane to The Netherlands. The take off went smoothly but as soon as you were in the air the plane got shot down. The plane crashed on a island. Do you Survive or GIVE UP?" )
    choice = input()
    if choice == 'SURVIVE':
        Verhaallijn9 += 1
    elif choice == 'GIVE UP':
        Verhaallijn10 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn5 == 1:
    print("You decide to take the boat to The Netherlands. You almost made it out of Uganda but a missile hit your boat and you died...")
    print("(BAD ENDING) You and the boat are have both sunken to the bottom of the ocean...")

if Verhaallijn6 == 1:
    print("You decide to take the train to The Netherlands. You boared a refugee train. The train was filled with many people that are also fleeing from Uganda. You made it half-way to The Netherlands but the train was forcibly stopped by the Americans. What do you decide to do? HIDE or RUN AWAY")
    choice = input()
    if choice == 'HIDE':
        Verhaallijn11 += 1
    elif choice == 'RUN AWAY':
        Verhaallijn12 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn7 == 1:
    print("You decide to hide from the Americans. You get found and you get filled with lead..." )
    print("(BAD ENDING) You got shot and died...")

if Verhaallijn8 == 1:
    print("You choose to fight against the Americans. You meet a person called Jonas Savimbi. He helps you fight against the Americans. You see a tank, do you throw a GRENADE or shoot with a ROCKET LAUNCHER" )
    choice = input()
    if choice == 'GRENADE':
        Verhaallijn13 += 1
    elif choice == 'ROCKET LAUNCHER':
        Verhaallijn14 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn9 == 1:
    print("You want to survive, you explore the island. You find civilization but... they are cannibals. Do you RUN or FIGHT them off?" )
    choice = input()
    if choice == 'RUN':
        Verhaallijn15 += 1
    elif choice == 'FIGHT':
        Verhaallijn16 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn10 == 1:
    print("You gave up... You sit in silence and starve to death..." )
    print("(BAD ENDING) You died because of starvation...")


if Verhaallijn11 == 1:
    print("You hide from the cannibals. It starts raining, so you decide to find shelter. You see a cave, do you go IN or try and FIND somewhere else" )
    choice = input()
    if choice == 'IN':
        Verhaallijn17 += 1
    elif choice == 'FIND':
        Verhaallijn18 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn12 == 1:
    print("You hide from the Americans. Where do you hide? In a empty CONTAINER or under some HAYBALES?" )
    choice = input()
    if choice == 'CONTAINER':
        Verhaallijn19 += 1
    elif choice == 'HAYBALES':
        Verhaallijn20 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn13 == 1:
    print("You use a grenade it did nothing, you got shot by the tank and blew up in to pieces..." )
    print("(BAD ENDING) Your body is scattered everywhere...")


if Verhaallijn14 == 1:
    print("You use a rocket launcher to blow up the tank. The Americans retreat. Do you STAY or PURSUE?" )
    choice = input()
    if choice == 'STAY':
        Verhaallijn21 += 1
    elif choice == 'PURSUE':
        Verhaallijn22 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn15 == 1:
    print("You ran away from the cannibals. They follow you but you lost them in the woods but... You starved and froze to death..." )
    print("(BAD ENDING) You froze to death...")


if Verhaallijn16 == 1:
    print("You fight the the cannibals but there were too many... You got eaten by them..." )
    print("(BAD ENDING) You got eaten...")

if Verhaallijn17 == 1:
    print("You go in the cave, make a fire and stay there fir the night. Morning comes and you go outside you try to look around again. Do you want the go BACK to the plane or do you try and go FURTHER into the forest?" )
    choice = input()
    if choice == 'BACK':
        Verhaallijn23 += 1
    elif choice == 'FURTHER':
        Verhaallijn24 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn18 == 1:
    print("You decide to find somewhere else to stay. It becomes night and it starts the rain. You froze to death because of the cold rain..." )
    print("(BAD ENDING) You died because of the cold...")


if Verhaallijn19 == 1:
    print("You hide in a container, they didn't find you. Do you WAIT longer or GET OUT?" )
    choice = input()
    if choice == 'WAIT':
        Verhaallijn25 += 1
    elif choice == 'GET OUT':
        Verhaallijn26 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn20 == 1:
    print("You hide in the haybales but they lit it on fire, you burned to death...")
    print("(BAD ENDING) You got burnt to a crisp...")

if Verhaallijn21 == 1:
    print("You stay and don't pursue the Americans, you've fended the Americans away and they leave Uganda" )
    print("(UGANDA ENDING) You survived...")

if Verhaallijn22 == 1:
    print("You decide to pursue the Americans, they got back up and you died..." )

if Verhaallijn23 == 1:
    print("You go back to the plane and find a radio, you call for help and get a answer. You get picked up by the Dutch Army and you safely make it to The Netherlands")
    print("(GOOD ENDING) You survived and life the rest of your life in The Netherlands...")

if Verhaallijn24 == 1:
    print("You decide to go further into the forest and get lost, you spend the rest of your days in the forest. Do you SURVIVE or GIVE UP" )
    choice = input()
    if choice == 'SURVIVE':
        Verhaallijn21 += 1
    elif choice == 'GIVE UP':
        Verhaallijn22 += 1
    else:
        print(choice, " wasn't a valid choice")

if Verhaallijn25 == 1:
    print("You wait in the container for a few minutes and go out. The Americans left and the train starts to move again. You make it to The Netherlands." )
    print("(GOOD ENDING) You made it to The Netherlands and live the rest of your life there...")

if Verhaallijn26 == 1:
    print("You got out too early and the Americans find you. You get captured, tortured and killed..." )
    print("(BAD ENDING) You died...")

restart = input ()
print ("Do you wish to restart..? ")
if restart == 'RESTART':
          rungame = 0

else: 
    if restart == 'RESTART': 
        print()
    exit ()   