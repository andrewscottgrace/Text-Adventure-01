import os

#region RESTART FUNCTION
def restart_game():
    while True:
        restart = input("Would you like to restart? (yes/no): ").strip().lower()
        if restart == "yes":
            start_game()
            return  # Ensures the function exits after restarting
        elif restart == "no":
            print("Thank you for playing!")
            exit()  # Exits the game
        else:
            print("Invalid choice. Try again.")
#endregion

def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen

#region INTRO
    lines = [
        "The Lost Wilds: A Text-based Adventure by Andrew Scott Grace",
        "You wake up in the middle of a meadow with no memory of who you are or how you got there.",
        "You stand up and look around.",
        "To the East, you see a village several kilometers away.",
        "To the West, you see a castle atop a steep, snowy mountain."
    ]

    for line in lines:
        print(line)
        input("Press ENTER to Continue...")

    print("Do you want to travel East or West?")

    while True:
        dirChoice = input("> ").strip().lower()
#endregion

#region EAST PATH
        if dirChoice == "east":
            print("You begin your journey towards the village.")
            lines = [
                "You enter a dense forest teeming with wildlife.",
                "The earthy aroma of moss & pine fills your body.",
                "After a few kilometers of hiking through the wilderness, you start to feel tired & hungry.",
                "Do you want to stop to eat & rest? (yes/no)"
            ]
            for line in lines:
                input("Press ENTER to Continue...")
                print(line)

            while True:
                break_choice = input("> ").strip().lower()
                if break_choice == "yes":
                    print("You stop and find a decent spot to make a camp.")
                    lines = [
                        "Using sticks & leaves, you build a small shelter & a fire",
                        "You manage to gather some edible berries & boil water from a nearby stream.",
                        "The sun sets as you lay in your makeshift bed.",
                        "The forest calms and the moonlight scatters through the trees.",
                        "You feel yourself start to doze off...",
                        "...",
                        "...",
                        "Morning comes and you are awakened by the sound of forest birds.",
                        "Do you want to STAY at camp or CONTINUE on?"
                    ]
                    for line in lines:
                        input("Press ENTER to Continue...")
                        print(line)

                    while True:
                        camp_choice = input("> ").strip().lower()
                        if camp_choice == "stay":
                            print("You decide to stay at your camp.")
                            lines = [
                                "After a few days, your camp has improved",
                                "You pick up a lot of skills that make surviving easier.",
                                "You learn to hunt & grow food.",
                                "Over the months, your camp grows into a homestead.",
                                "Years pass and you've grown to enjoy this life.",
                                "While lonely at times, you've thrived in the bush.",
                                "You pass away of natural causes at age 71.",
                                "Never remembering your previous life before waking up in the woods...",
                                "Your adventure ends here."
                            ]
                            for line in lines:
                                input("Press ENTER to Continue")
                                print(line)

                            restart_game()  # gameover

                        elif camp_choice == "continue":
                            print("You push on through the forest towards the village.")
                            lines = [
                                "After a few more kilometers of trekking, the terrain becomes more difficult.",
                                "You approach a wide river.",
                                "It seems to be several meters deep.",
                                "Do you attempt to build a RAFT to cross or try to SWIM across?"
                            ]
                            for line in lines:
                                input("Press ENTER to Continue...")
                                print(line)

                            while True:
                                river_choice = input("> ").strip().lower()
                                if river_choice == "raft":
                                    print("You search the area for materials to build a raft.")
                                    
                                    lines = [
                                        "You gather up some sticks, logs & plant matter from the surrounding area.",
                                        "Securing the lumber with the plant matter, you build a crude raft.",
                                        "You plunge the raft into the water.",
                                        "It seems to float!",
                                        "You board your makeshift vessel and paddle across.",
                                        "The water is cold & your raft barely floats...",
                                        "...but you manage to make it across safely.",
                                        "You keep moving onwards through the wilds.",
                                        "You can hear distant chatter from the nearby village.",
                                        "Must be getting close!",
                                        "Filled with excitement, you pick up the pace and forge ahead towards the village.",
                                        "The village must be less than a kilometer away!",
                                        "In your bout of eagerness, you trip on a tree root and injure your leg.",
                                        "You try to stand but the pain is unbearable.",
                                        "Do you SCREAM for help or try to CRAWL your way to the village?"
                                    ]
                                    for line in lines:
                                        input("Press ENTER to Continue...")
                                        print(line)

                                    while True:
                                        injury_choice = input("> ").strip().lower()
                                        if injury_choice == "scream":
                                            print("You scream out for help...")
                                            lines = [
                                                "After several moments of yelling & screaming, your lungs tire.",
                                                "The loud noises don't seem to alert the villagers of your distress.",
                                                "Suddenly, you hear footsteps approaching!",
                                                "These don't sound like human footsteps...",
                                                "Amongst the crunch of the leaves, you hear panting and soft growling.",
                                                "A piercing howl erupts from the direction of the footsteps.",
                                                "It's a pack of wolves!",
                                                "Your cries for help must have drawn the attention of these ferocious beasts.",
                                                "You grab around looking for a weapon but all you can find is small rocks and sticks.",
                                                "The wolves circle you as you desperately throw rocks & twigs.",
                                                "Unbothered by your small projectiles, one of the wolves lunges towards you.",
                                                "You manage to roll and dodge the attack.",
                                                "Another wolf pounces...",
                                                "Its jaws clench down and the teeth sink into your upper arm.",
                                                "You cry out again but to no avail.",
                                                "Another wolf makes its move...",
                                                "The second wolf goes for your neck.",
                                                "The light slips away...",
                                                "Your adventure ends here."
                                            ]
                                            for line in lines:
                                                input("Press ENTER to Continue")
                                                print(line)
                                            
                                            restart_game()  # gameover

                                        elif injury_choice == "crawl":
                                            print("You try to crawl your way to the village...")
                                            lines = [
                                                "Unable to walk, you dig your hands into the ground and pull yourself along.",
                                                "Seething pain shoots down your leg as you shuffle your way along the forest ground.",
                                                "You see lights peeking through the branches!",
                                                "The village is near.",
                                                "You creep your way closer to the edge of the village.",
                                                "A local villager spots you.",
                                                "You cry out in pain as the villager approaches you.",
                                                "The villager calls to the others requesting aid for your injuries.",
                                                "You fade in and out of consciousness as they tend to your wounds",
                                                "...",
                                                "You wake up in a clean, comfortable cot and notice a split on your leg.",
                                                "An elderly woman is sitting in a chair near the end of your bed.",
                                                "You thank her for the aid.",
                                                "She inquires about your identity and how you ended up in the forest.",
                                                "You reply unsure.",
                                                "The woman is suspicious and becomes somewhat confrontational",
                                                "An outsider with no story?",
                                                "You assure her that you have no recollection.",
                                                "Reluctantly, she offers refuge in the village.",
                                                "...",
                                                "Years pass...",
                                                "You live out your years doing farm work in this small village.",
                                                "You pass away at age 76 of natural causes.",
                                                "Never remembering your past life...",
                                                "Your adventure ends here."
                                            ]
                                            for line in lines:
                                                input("Press ENTER to Continue")
                                                print(line)
                                            
                                            restart_game() #gameover

                                        else:
                                            print("Invalid choice. Try again.")
                                                                       
                                elif river_choice == "swim":
                                    print("You plunge into the river...")

                                    lines = [
                                        "The frigid water bites at your skin.",
                                        "You try to press on and swim to the other side.",
                                        "You make it about halfway across as a numbness starts to spread through your body.",
                                        "You try to stay afloat as you feel yourself become weaker with every stroke.",
                                        "The other side of the river now seems to be lightyears away.",
                                        "Your muscles cramp from the unrelenting chill.",
                                        "Unable to keep afloat, water starts to fill your lungs.",
                                        "The light slowly starts to fade as you drift off into unconsciousness.",
                                        "Your adventure ends here."
                                    ]
                                    for line in lines:
                                        input("Press Enter to Continue...")
                                        print(line)

                                    restart_game()  # gameover

                                else:
                                    print("Invalid choice. Try again.")                           
                        else:
                            print("Invalid choice. Try again.")
                    
                elif break_choice == "no":
                    print("You continue on, starving and sleepless.")

                    lines = [
                        "The sun starts to set and your stomach is howling for food & water.",
                        "Each step you take pushes you further into exhaustion.",
                        "You collapse.",
                        "The light slowly starts to fade as you drift off into unconsciousness.",
                        "Your adventure ends here."
                    ]
                    for line in lines:
                        input("Press Enter to Continue...")
                        print(line)

                    restart_game()  #gameover

                else:
                    print("Invalid choice. Try again.")

            
#endregion

#region WEST PATH
        elif dirChoice == "west":
            print("After a short hike, you find yourself at the base of the mountain.")
            lines = [
                "The climb looks treacherous.",
                "You assess the terrain.",
                "You notice a path to the LEFT enshrouded by dense vegetation.",
                "You also see a path to the RIGHT covered with deep snow.",
                "Which path do you take? (left/right)"
            ]
            for line in lines:
                input("Press ENTER to Continue...")
                print(line)

            while True:
                path_choice = input("> ").strip().lower()
                if path_choice == "left":
                    print("You trek through the thick foliage.")
                    lines = [
                        "The path is narrow and the brush is thick.",
                        "Pushing through the dense undergrowth for nearly a kilometer...",
                        "You find yourself on a rocky cliff.",
                        "Feeling the cool breeze of the mountain air.",
                        "You notice a small cave in the cliffside.",
                        "Do you enter the cave to REST or CONTINUE on?"
                    ]
                    for line in lines:
                        input("Press ENTER to Continue...")
                        print(line)

                    while True:
                        cave_choice = input("> ").strip().lower()
                        if cave_choice == "rest":
                            print("You decide to rest in the cave.")
                            lines = [
                                "You find a comfortable spot in the cave and lay down.",
                                "You drift off into a deep sleep...",
                                "You wake up to a loud growling sound.",
                                "You open your eyes to see a pair of glowing eyes in the darkness.",
                                "A bear!",
                                "The bear lunges at you and you try to fend it off with your hands.",
                                "The bear's claws rip through your flesh.",
                                "You scream in agony as the bear mauls you to death.",
                                "Your adventure ends here."
                            ]
                            for line in lines:
                                input("Press ENTER to Continue...")
                                print(line)
                            restart_game()  #gameover

                        elif cave_choice == "continue":
                            print("You decide to press on.")
                            lines = [
                                "You continue along the cliffside.",
                                "The terrain becomes more difficult as you climb higher.",
                                "You're tired but the view is breathtaking.",
                                "You reach a point where the path narrows to a thin ledge.",
                                "With careful footing, you manage to traverse the ledge.",
                                "The path opens up to a small clearing with light vegetation.",
                                "You see a small cabin just up ahead.",
                                "Do you approach the CABIN or CONTINUE on?"
                            ]
                            for line in lines:
                                input("Press ENTER to Continue...")
                                print(line)
                            
                            while True:
                                cabin_choice = input("> ").strip().lower()
                                if cabin_choice == "cabin":
                                    print("You approach the cabin.")
                                    lines = [
                                        "The cabin is small and deteriorating.",
                                        "You knock on the door.",
                                        "No answer.",
                                        "You try the door and it creaks open.",
                                        "You step inside and see a small bed, a table, and a chair.",
                                        "It's not the nicest place but it's shelter.",
                                        "You head back outside to search for some food.",
                                        "You find some dried meat and water in a small storage box.",
                                        "You eat and decide to rest for a bit.",
                                        "The wind howls outside as you lay down on the bed.",
                                        "You drift off into a deep sleep...",
                                        "...",
                                        "...",
                                        "The sound of the harsh mountain winds jostle you awake.",
                                        "You feel rested and ready to continue your journey.",
                                        "You step outside the cabin and look around.",
                                        "From here, you can see the castle in the distance.",
                                        "About halfway up the mountain!",
                                        "You notice a path behind the cabin that leads up the mountain.",
                                        "The terrain is simple and the path is clear.",
                                        "As you ascend, you find yourself at a fork in the path.",
                                        "To the LEFT, you see an icy path that leads up towards the summit.",
                                        "To the RIGHT, you spot what seems to be stairs carved into the mountain.",
                                        "Which path do you take? (left/right)"
                                    ]
                                    for line in lines:
                                        input("Press ENTER to Continue...")
                                        print(line)
                                    
                                    while True:
                                        summit_choice = input("> ").strip().lower()
                                        if summit_choice == "left":
                                            print("You take the icy path to the LEFT.")
                                            lines = [
                                                "The path is slick and you struggle to keep your footing.",
                                                "You slide and slip your way up the mountain.",
                                                "The cold bites at your skin.",
                                                "You're almost to the summit!",
                                                "You take one last step and slip.",
                                                "You fall off the edge.",
                                                "The wind rushes past you as you plummet.",
                                                "The ground rushes up to meet you.",
                                                "Your adventure ends here."
                                            ]
                                            for line in lines:
                                                input("Press ENTER to Continue...")
                                                print(line)

                                            restart_game()  # gameover

                                        elif summit_choice == "right":
                                            print("You proceed with caution while climbing the stairs.")
                                            lines = [
                                                "The stairs are steep but manageable.",
                                                "You climb higher and higher.",
                                                "The air is thin and you're out of breath.",
                                                "You reach the summit!",
                                                "The view is breathtaking.",
                                                "You see the village to the East.",
                                                "You feel a sense of accomplishment.",
                                                "You sit and take in the view.",
                                                "The castle gates open and a figure emerges.",
                                                "A man dressed in strange clothes and an odd hat approaches you.",
                                                "He introduces himself as Jad, the Charred Wizard.",
                                                "Jad explains that he has been watching you.",
                                                "You inquire about the meaning of his words.",
                                                "Jad describes that you are an eexperiment of his.",
                                                "An experiment to test the limits of the human spirit.",
                                                "You stand before him in disbelief.",
                                                "Jad quickly waves his hand and you feel a surge of energy.",
                                                "The energy quickly fades.",
                                                "...",
                                                "Your vision starts to blur.",
                                                "The inner workings of your mind start to unravel.",
                                                "You start to remember...",
                                                "...",
                                                "...",
                                                "Nothing.",
                                                "You remember nothing.",
                                                "You fall to your knees and look up at Jad.",
                                                "He smiles and says, 'The experiment is complete.'",
                                                "'Now, it's time for phase two...'"
                                            ]
                                            for line in lines:
                                                input("Press ENTER to Continue...")
                                                print(line)

                                            restart_game #gameover

                                        else:
                                            print("Invalid choice. Try again.")

                                elif cabin_choice == "continue":
                                    print("You decide to continue on.")
                                    lines = [
                                        "You leave the cabin behind and continue on the path.",
                                        "The path is steep and the air is thin.",
                                        "Exhaustion starts to set in.",
                                        "You push on.",
                                        "The terrain becomes more difficult as you climb higher.",
                                        "Muscles ache and your lungs burn.",
                                        "You reach a point where the path narrows to a thin ledge.",
                                        "You take a few steps onto the ledge and slip.",
                                        "You fall off the edge.",
                                        "The wind rushes past you as you plummet.",
                                        "The ground rushes up to meet you.",
                                        "Your adventure ends here."
                                    ]
                                    for line in lines:
                                        input("Press ENTER to Continue...")
                                        print(line)

                                    restart_game()  #gameover

                                else:
                                    print("Invalid choice. Try again.")                                                          
                        else:
                            print("Invalid choice. Try again.")
                                        
                elif path_choice == "right":
                    print("You press on through the snow.")
                    lines = [
                        "The snow is deep and the wind is biting.",
                        "You trudge through the snow for nearly a kilometer.",
                        "You find yourself at a frozen stream.",
                        "The ice looks thick enough to cross.",
                        "Do you attempt to CROSS the stream or FOLLOW the stream?"
                    ]
                    for line in lines:
                        input("Press ENTER to Continue...")
                        print(line)

                    while True:
                        stream_choice = input("> ").strip().lower()
                        if stream_choice == "cross":
                            print("You attempt to cross the frozen stream.")
                            lines = [
                                "You step out onto the ice.",
                                "The ice creaks beneath your weight.",
                                "You hear a loud crack.",
                                "The ice beneath you gives way.",
                                "You fall into the freezing water.",
                                "The cold bites at your skin.",
                                "You try to swim to the surface but the ice is too thick.",
                                "You struggle to stay afloat.",
                                "The cold starts to numb your body.",
                                "You take one last breath.",
                                "The light fades as you drift off into unconsciousness.",
                                "Your adventure ends here."
                            ]
                            for line in lines:
                                input("Press ENTER to Continue...")
                                print(line)

                            restart_game()  #gameover

                        elif stream_choice == "follow":
                            print("You decide to follow the stream.")
                            lines = [
                                "You follow the stream for a few kilometers.",
                                "The snow starts to thin out.",
                                "You find yourself at the base of a steep cliff.",
                                "The cliff is too steep to climb.",
                                "You notice a small path that leads around the cliff.",
                                "You take the path and continue on.",
                                "The path winds around the cliffside.",
                                "You see a small cave in the cliff.",
                                "Do you enter the cave to REST or CONTINUE on?"
                            ]
                            for line in lines:
                                input("Press ENTER to Continue...")
                                print(line)

                            while True:
                                cave_choice = input("> ").strip().lower()
                                if cave_choice == "rest":
                                    print("You decide to rest in the cave.")
                                    lines = [
                                        "Entering the cave, you gather some materials to make a fire.",
                                        "With the fire lit, you warm up and cook up some cave insects.",
                                        "You eat and lay down to rest.",
                                        "You drift off into a deep sleep...",
                                        "...",
                                        "...",
                                        "You wake up to the sound of bats swarming over your head as they fly out of the cave.",
                                        "You feel rested and ready to continue your journey.",
                                        "You step outside the cave and look around.",
                                        "You see the castle in the distance.",
                                        "About halfway up the mountain!",
                                        "You notice a path adjacent to the cave that leads up the mountain.",
                                        "The terrain seems easy and the path is clear.",
                                        "As you ascend, you find yourself at a fork in the path.",
                                        "To the LEFT, you see an icy path that leads up towards the summit.",
                                        "To the RIGHT, you spot what seems to be stairs carved into the mountain.",
                                        "Which path do you take? (left/right)"
                                    ]
                                    for line in lines:
                                        input("Press ENTER to Continue...")
                                        print(line)

                                    while True:
                                        summit_choice = input("> ").strip().lower()
                                        if summit_choice == "left":
                                            print("You take the icy path to the LEFT.")
                                            lines = [
                                                "The path is slick and you struggle to keep your footing.",
                                                "You slide and slip your way up the mountain.",
                                                "The cold bites at your skin.",
                                                "You're almost to the summit!",
                                                "You take one last step and slip.",
                                                "You fall off the edge.",
                                                "The wind rushes past you as you plummet.",
                                                "The ground rushes up to meet you.",
                                                "Your adventure ends here."
                                            ]
                                            for line in lines:
                                                input("Press ENTER to Continue...")
                                                print(line)

                                            restart_game()  # gameover

                                        elif summit_choice == "right":
                                            print("You proceed with caution while climbing the stairs.")
                                            lines = [
                                                "The stairs are steep but manageable.",
                                                "You climb higher and higher.",
                                                "The air is thin and you're out of breath.",
                                                "You reach the summit!",
                                                "The view is breathtaking.",
                                                "You see the village to the East.",
                                                "You feel a sense of accomplishment.",
                                                "You sit and take in the view.",
                                                "The castle gates open and a figure emerges.",
                                                "A man dressed in strange clothes and an odd hat approaches you.",
                                                "He introduces himself as Jad, the Charred Wizard.",
                                                "Jad explains that he has been watching you.",
                                                "You inquire about the meaning of his words.",
                                                "Jad describes that you are an eexperiment of his.",
                                                "An experiment to test the limits of the human spirit.",
                                                "You stand before him in disbelief.",
                                                "Jad quickly waves his hand and you feel a surge of energy.",
                                                "The energy quickly fades.",
                                                "...",
                                                "Your vision starts to blur.",
                                                "The inner workings of your mind start to unravel.",
                                                "You start to remember...",
                                                "...",
                                                "...",
                                                "Nothing.",
                                                "You remember nothing.",
                                                "You fall to your knees and look up at Jad.",
                                                "He smiles and says, 'The experiment is complete.'",
                                                "'Now, it's time for phase two...'"
                                            ]
                                            for line in lines:
                                                input("Press ENTER to Continue...")
                                                print(line)

                                            restart_game #gameover

                                        else:
                                            print("Invalid choice. Try again.")

                                elif cave_choice == "continue":
                                    print("You decide to continue on.")
                                    lines = [
                                        "You carry on past the cave and continue on the path.",
                                        "The path is steep and the air is thin.",
                                        "Exhaustion starts to set in.",
                                        "You push on.",
                                        "The terrain becomes more difficult as you climb higher.",
                                        "Muscles ache and your lungs burn.",
                                        "You reach a point where the path narrows to a thin ledge.",
                                        "You take a step onto the ledge and slip.",
                                        "You fall off the edge.",
                                        "The wind rushes past you as you plummet.",
                                        "The ground rushes up to meet you.",
                                        "Your adventure ends here."
                                    ]
                                    for line in lines:
                                        input("Press ENTER to Continue...")
                                        print(line)

                                    restart_game()  #gameover

                                else:
                                    print("Invalid choice. Try again.")
                        else:
                            print("Invalid choice. Try again.")
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Invalid choice. Try again.")

#endregion
start_game()