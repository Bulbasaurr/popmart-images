import json

base = "https://raw.githubusercontent.com/Bulbasaurr/popmart-images/main/Molly"

# Row -> (series_folder, filename) mapping
# Filenames need to match what's on GitHub exactly
mapping = {
    # MSM Series 1
    526: ("Mega_Space_Molly_Series_1", "The_Girl_From_The_Earth.jpg"),
    527: ("Mega_Space_Molly_Series_1", "Candy.jpg"),
    528: ("Mega_Space_Molly_Series_1", "Christmas.jpg"),
    529: ("Mega_Space_Molly_Series_1", "Instinctoy.jpg"),
    530: ("Mega_Space_Molly_Series_1", "Jelly.jpg"),
    531: ("Mega_Space_Molly_Series_1", "Keith_Haring.jpg"),
    532: ("Mega_Space_Molly_Series_1", "Little_Painter.jpg"),
    533: ("Mega_Space_Molly_Series_1", "Spongbob.jpg"),
    534: ("Mega_Space_Molly_Series_1", "Toffee.jpg"),
    535: ("Mega_Space_Molly_Series_1", "Watermelon.jpg"),
    # MSM Series 2
    536: ("Mega_Space_Molly_Series_2", "Birthday_Bear.jpg"),
    537: ("Mega_Space_Molly_Series_2", "Cheer_Bear.jpg"),
    538: ("Mega_Space_Molly_Series_2", "Melting.jpg"),
    539: ("Mega_Space_Molly_Series_2", "Meta.jpg"),
    540: ("Mega_Space_Molly_Series_2", "Wish_Bear.jpg"),
    541: ("Mega_Space_Molly_Series_2", "Banana_2017.jpg"),
    542: ("Mega_Space_Molly_Series_2", "Coca_Cola_Classic.jpg"),
    543: ("Mega_Space_Molly_Series_2", "Glacier.jpg"),
    544: ("Mega_Space_Molly_Series_2", "Heartbeat.jpg"),
    545: ("Mega_Space_Molly_Series_2", "Jean_Michel_Basquiat.jpg"),
    546: ("Mega_Space_Molly_Series_2", "Meilin_Panda.jpg"),
    547: ("Mega_Space_Molly_Series_2", "Mint_Chocolate.jpg"),
    548: ("Mega_Space_Molly_Series_2", "Patrick_Star.jpg"),
    549: ("Mega_Space_Molly_Series_2", "Pink_Panther.jpg"),
    # MSM Series 3
    550: ("Mega_Space_Molly_Series_3", "Louis_De_Guzman.jpg"),
    551: ("Mega_Space_Molly_Series_3", "Starry.jpg"),
    552: ("Mega_Space_Molly_Series_3", "Team_Coca_Cola.jpg"),
    553: ("Mega_Space_Molly_Series_3", "Garfield.jpg"),
    554: ("Mega_Space_Molly_Series_3", "Gary_Baseman.jpg"),
    555: ("Mega_Space_Molly_Series_3", "Good_Luck_Bear.jpg"),
    556: ("Mega_Space_Molly_Series_3", "Graffiti.jpg"),
    557: ("Mega_Space_Molly_Series_3", "Heartfelt_Words.jpg"),
    558: ("Mega_Space_Molly_Series_3", "Peach_2016.jpg"),
    559: ("Mega_Space_Molly_Series_3", "Ted_2.jpg"),
    560: ("Mega_Space_Molly_Series_3", "Tenderheart_Bear.jpg"),
    561: ("Mega_Space_Molly_Series_3", "TETRIS.jpg"),
    # MSM Series 4
    562: ("Mega_Space_Molly_Series_4", "Angel.jpg"),
    563: ("Mega_Space_Molly_Series_4", "Celebration.jpg"),
    564: ("Mega_Space_Molly_Series_4", "Bedtime_Bear.jpg"),
    565: ("Mega_Space_Molly_Series_4", "Christmas_2024.jpg"),
    566: ("Mega_Space_Molly_Series_4", "Christmas_2024_Green.jpg"),
    567: ("Mega_Space_Molly_Series_4", "Durianman.jpg"),
    568: ("Mega_Space_Molly_Series_4", "Funshine_Bear.jpg"),
    569: ("Mega_Space_Molly_Series_4", "Jon_Burgerman.jpg"),
    570: ("Mega_Space_Molly_Series_4", "Optimus_Prime.jpg"),
    571: ("Mega_Space_Molly_Series_4", "Orange_Juice.jpg"),
    572: ("Mega_Space_Molly_Series_4", "Palmer_House.jpg"),
    573: ("Mega_Space_Molly_Series_4", "Purple_Sweet_Potato.jpg"),
    574: ("Mega_Space_Molly_Series_4", "Smitten_Love.jpg"),
    575: ("Mega_Space_Molly_Series_4", "Smitten_Love_White.jpg"),
    576: ("Mega_Space_Molly_Series_4", "Trevor_Andrew.jpg"),
    # MSM Emoji (577 = Ms. Billionaire - no image, skip)
    578: ("Mega_Space_Molly_Emoji", "Open_Minded.jpg"),
    579: ("Mega_Space_Molly_Emoji", "Unicorn.jpg"),
    580: ("Mega_Space_Molly_Emoji", "55555.jpg"),
    581: ("Mega_Space_Molly_Emoji", "886.jpg"),
    582: ("Mega_Space_Molly_Emoji", "A_Trying_Situation.jpg"),
    583: ("Mega_Space_Molly_Emoji", "Admiration.jpg"),
    584: ("Mega_Space_Molly_Emoji", "All_In_Green.jpg"),
    585: ("Mega_Space_Molly_Emoji", "Bad_Words.jpg"),
    586: ("Mega_Space_Molly_Emoji", "Caution_The_Ghost_Is_Here.jpg"),
    587: ("Mega_Space_Molly_Emoji", "Confession.jpg"),
    588: ("Mega_Space_Molly_Emoji", "Cow_On_Me.jpg"),
    589: ("Mega_Space_Molly_Emoji", "Frozen_Smile.jpg"),
    590: ("Mega_Space_Molly_Emoji", "Happy_Puppy.jpg"),
    591: ("Mega_Space_Molly_Emoji", "Lil_Devil.jpg"),
    592: ("Mega_Space_Molly_Emoji", "LMAO.jpg"),
    593: ("Mega_Space_Molly_Emoji", "Monkey_Business.jpg"),
    594: ("Mega_Space_Molly_Emoji", "Pissed_Off.jpg"),
    595: ("Mega_Space_Molly_Emoji", "So_What.jpg"),
    596: ("Mega_Space_Molly_Emoji", "Why_So_Serious.jpg"),
    597: ("Mega_Space_Molly_Emoji", "Worn_Out.jpg"),
    # Carb Lover
    598: ("Carb_Lover", "Pretend_Bear_Bread.jpg"),
    599: ("Carb_Lover", "Afternoon_Tea.jpg"),
    600: ("Carb_Lover", "Baker_or_Gardener.jpg"),
    601: ("Carb_Lover", "Crocodile_Bread.jpg"),
    602: ("Carb_Lover", "Croissant_Balaclava.jpg"),
    603: ("Carb_Lover", "Elegant_Waffle.jpg"),
    604: ("Carb_Lover", "Heart_To_Heart_Toast.jpg"),
    605: ("Carb_Lover", "Lets_Go_Hot_Dog.jpg"),
    606: ("Carb_Lover", "Pick_a_Boo_Burger.jpg"),
    607: ("Carb_Lover", "Soft_Punch.jpg"),
    608: ("Carb_Lover", "Sweet_Ballet.jpg"),
    609: ("Carb_Lover", "Taiyaki_Princess.jpg"),
    610: ("Carb_Lover", "Yummy_Bread_Shoes.jpg"),
    # My Childhood
    611: ("My_Childhood", "The_Earth_Began_To_Melt.jpg"),
    612: ("My_Childhood", "A_Snapshot_In_Time.jpg"),
    613: ("My_Childhood", "Caught_In_A_Thunderstorm.jpg"),
    614: ("My_Childhood", "I_Discovered_You_In_The_Deep_Sea.jpg"),
    615: ("My_Childhood", "I_Found_a_Mini_Me.jpg"),
    616: ("My_Childhood", "I_Met_You_In_the_Skating_Rink.jpg"),
    617: ("My_Childhood", "I_Needed_To_Cool_Down.jpg"),
    618: ("My_Childhood", "I_Never_Gave_Up.jpg"),
    619: ("My_Childhood", "My_First_Summer_Rainbow.jpg"),
    620: ("My_Childhood", "The_Three_Of_Us_Playing.jpg"),
    621: ("My_Childhood", "The_Wind_Was_Whistling.jpg"),
    622: ("My_Childhood", "You_Became_So_Sweet.jpg"),
    623: ("My_Childhood", "You_Stayed_With_Me.jpg"),
    # Zootopia 2
    624: ("Zootopia_2", "Judy_in_Uniform.jpg"),  # Finnick - no individual image
    625: ("Zootopia_2", "Bellwether.jpg"),
    626: ("Zootopia_2", "Clawhauser.jpg"),
    627: ("Zootopia_2", "Flash.jpg"),
    628: ("Zootopia_2", "Gary.jpg"),
    629: ("Zootopia_2", "Gazelle.jpg"),
    630: ("Zootopia_2", "Judy_in_Uniform.jpg"),
    631: ("Zootopia_2", "Nick_in_Uniform.jpg"),
    632: ("Zootopia_2", "Nibbles.jpg"),
    633: ("Zootopia_2", "Polar_Bear_and_Mr_Big.jpg"),
    634: ("Zootopia_2", "Russ.jpg"),
    635: ("Zootopia_2", "Undercover_Judy.jpg"),
    636: ("Zootopia_2", "Undercover_Nick.jpg"),
    # My Huggable Discovery
    637: ("My_Huggable_Discovery", "A_Bear_Hug.jpg"),  # Hug Rescue Plan - secret, use A_Bear_Hug placeholder
    638: ("My_Huggable_Discovery", "A_Bear_Hug.jpg"),
    639: ("My_Huggable_Discovery", "A_Forced_Hug.jpg"),
    640: ("My_Huggable_Discovery", "A_Free_Hug.jpg"),
    641: ("My_Huggable_Discovery", "A_Little_Hug.jpg"),
    642: ("My_Huggable_Discovery", "Hug_My_Dream.jpg"),
    643: ("My_Huggable_Discovery", "Hug_Stubbornness.jpg"),
    644: ("My_Huggable_Discovery", "Hug_the_Hedgehog.jpg"),
    645: ("My_Huggable_Discovery", "Hug_the_Nature.jpg"),
    646: ("My_Huggable_Discovery", "Hug_the_Ocean.jpg"),
    647: ("My_Huggable_Discovery", "Hug_the_Sky.jpg"),
    648: ("My_Huggable_Discovery", "Hug_the_Universe.jpg"),
    649: ("My_Huggable_Discovery", "Just_One_Hug.jpg"),
    # Pocket Friends
    650: ("Pocket_Friends", "Leave_Me_Alone.png"),  # Don't Mess With Me - secret, no image
    651: ("Pocket_Friends", "Enjoy_the_Sunshine.png"),
    652: ("Pocket_Friends", "Feeling_Blue.png"),
    653: ("Pocket_Friends", "Its_Snack_Time.png"),
    654: ("Pocket_Friends", "Leave_Me_Alone.png"),
    655: ("Pocket_Friends", "Pet_My_Head.png"),
    656: ("Pocket_Friends", "Whos_the_Good_Girl.png"),
}

# Output as JSON for processing
output = []
for row, (folder, fname) in sorted(mapping.items()):
    url = f"{base}/{folder}/{fname}"
    output.append({"row": row, "cell": f"K{row}", "url": url})

with open(r'D:\VSRepos\ThrilljoyImages\figurines\sheet_urls.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Generated {len(output)} URL mappings")
# Skip secrets that share images with other figures
skip = {624, 637, 650}  # Finnick, Hug Rescue Plan, Don't Mess With Me
actual = [x for x in output if x['row'] not in skip]
print(f"After removing duplicate-image secrets: {len(actual)}")
