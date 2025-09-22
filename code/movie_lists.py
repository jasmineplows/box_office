"""
Movie Lists for Feature Engineering
===================================

This file contains curated lists of movies for feature detection in the box office analysis.
Lists are organized by franchise, studio, and content type for easy maintenance.
"""

# Disney Live-Action Remakes
DISNEY_LIVE_ACTION_REMAKES = [
    "101 Dalmatians (1996)",
    "Alice in Wonderland (2010)",
    "Cinderella (2015)",
    "The Jungle Book (2016)",
    "Beauty and the Beast (2017)",
    "Dumbo (2019)",
    "Aladdin (2019)",
    "The Lion King (2019)",
    "Lady and the Tramp (2019)",
    "Mulan (2020)",
    "Pinocchio (2022)",
    "Peter Pan & Wendy (2023)",
    "The Little Mermaid (2023)",
    "Mufasa: The Lion King (2024)",
    "Snow White (2025)",
    "Lilo & Stitch (2025)",
    "Moana (2026)"
]

# Other Studio Live-Action Remakes/Adaptations
OTHER_LIVE_ACTION_REMAKES = [
    "How to Train Your Dragon (2025)",  # DreamWorks/Universal
]

# Marvel Cinematic Universe Films
MARVEL_MCU_FILMS = [
    # Phase One
    "Iron Man",
    "The Incredible Hulk",
    "Iron Man 2",
    "Thor",
    "Captain America: The First Avenger",
    "The Avengers",

    # Phase Two
    "Iron Man 3",
    "Thor: The Dark World",
    "Captain America: The Winter Soldier",
    "Guardians of the Galaxy",
    "Avengers: Age of Ultron",
    "Ant-Man",

    # Phase Three
    "Captain America: Civil War",
    "Doctor Strange",
    "Guardians of the Galaxy Vol. 2",
    "Spider-Man: Homecoming",
    "Thor: Ragnarok",
    "Black Panther",
    "Avengers: Infinity War",
    "Ant-Man and the Wasp",
    "Captain Marvel",
    "Avengers: Endgame",
    "Spider-Man: Far From Home",

    # Phase Four
    "Black Widow",
    "Shang-Chi and the Legend of the Ten Rings",
    "Eternals",
    "Spider-Man: No Way Home",
    "Doctor Strange in the Multiverse of Madness",
    "Thor: Love and Thunder",
    "Black Panther: Wakanda Forever",

    # Phase Five
    "Ant-Man and the Wasp: Quantumania",
    "Guardians of the Galaxy Vol. 3",
    "The Marvels",
    "Deadpool & Wolverine",
    "Captain America: Brave New World",
    "Thunderbolts*",
    "The Fantastic Four: First Steps",

    # Phase Six and Beyond
    "Spider-Man: Brand New Day",
    "Avengers: Doomsday",
    "Avengers: Secret Wars",
]

# DC Extended Universe / DC Films
DC_FILMS = [
    "Man of Steel",
    "Batman v Superman: Dawn of Justice",
    "Suicide Squad",
    "Wonder Woman",
    "Justice League",
    "Aquaman",
    "Shazam!",
    "Birds of Prey",
    "Wonder Woman 1984",
    "Zack Snyder's Justice League",
    "The Suicide Squad",
    "Black Adam",
    "Shazam! Fury of the Gods",
    "The Flash",
    "Blue Beetle",
    "Aquaman and the Lost Kingdom",
]

# Star Wars Films (Disney Era)
STAR_WARS_FILMS = [
    "Star Wars: The Force Awakens",
    "Rogue One: A Star Wars Story",
    "Star Wars: The Last Jedi",
    "Solo: A Star Wars Story",
    "Star Wars: The Rise of Skywalker",
]

# Fast & Furious Franchise
FAST_FURIOUS_FILMS = [
    "Fast Five",
    "Fast & Furious 6",
    "Furious 7",
    "The Fate of the Furious",
    "Hobbs & Shaw",
    "F9: The Fast Saga",
    "Fast X",
]

# Other Franchise Sequels (sequels to established franchises)
FRANCHISE_SEQUELS = [
    # Jurassic World (sequels to Jurassic Park)
    "Jurassic World",
    "Jurassic World: Fallen Kingdom",
    "Jurassic World Dominion",

    # Despicable Me sequels/spinoffs
    "Despicable Me 2",
    "Despicable Me 3",
    "Minions",
    "Minions: The Rise of Gru",

    # Pixar sequels
    "Finding Dory",
    "The Secret Life of Pets",
    "The Secret Life of Pets 2",

    # Other franchise sequels
    "Jumanji: Welcome to the Jungle",
    "Jumanji: The Next Level",
    "Twisters",  # Sequel to Twister (1996)
]

# Harry Potter / Wizarding World
WIZARDING_WORLD_FILMS = [
    "Fantastic Beasts and Where to Find Them",
    "Fantastic Beasts: The Crimes of Grindelwald",
    "Fantastic Beasts: The Secrets of Dumbledore",
]

# Other Media Adaptations (TV Shows, Games, Toys, Book/Franchise Sequels)
MEDIA_ADAPTATIONS = [
    "Transformers",
    "Transformers: Revenge of the Fallen",
    "Transformers: Dark of the Moon",
    "Transformers: Age of Extinction",
    "Transformers: The Last Knight",
    "Bumblebee",
    "Transformers: Rise of the Beasts",
    "G.I. Joe: The Rise of Cobra",
    "G.I. Joe: Retaliation",
    "Teenage Mutant Ninja Turtles",
    "Teenage Mutant Ninja Turtles: Out of the Shadows",
    "The Smurfs",
    "The Smurfs 2",
    "Sonic the Hedgehog",
    "Sonic the Hedgehog 2",
    "Sonic the Hedgehog 3",
    "Detective Pikachu",
    "Angry Birds Movie",
    "The Angry Birds Movie 2",
    "Battleship",

    # Jurassic World franchise (sequels to original Jurassic Park)
    "Jurassic World",
    "Jurassic World: Fallen Kingdom",
    "Jurassic World Dominion",

    # Despicable Me/Minions franchise
    "Despicable Me 2",
    "Despicable Me 3",
    "Minions",
    "Minions: The Rise of Gru",

    # Other animated sequels/franchises
    "The Secret Life of Pets",
    "The Secret Life of Pets 2",
    "Finding Dory",

    # Jumanji franchise
    "Jumanji: Welcome to the Jungle",
    "Jumanji: The Next Level",

    # James Bond franchise (action/spy IP)
    "Spectre",
    "No Time to Die",
    "Skyfall",

    # Video game adaptations
    "The Minecraft Movie",
    "Minecraft",
]

# Non-MCU Superhero Films
NON_MCU_SUPERHERO_FILMS = [
    # Sony Spider-Man (pre-MCU collaboration)
    "The Amazing Spider-Man",
    "The Amazing Spider-Man 2",
    "Venom",
    "Venom: Let There Be Carnage",
    "Morbius",
    "Madame Web",
    "Kraven the Hunter",

    # Fox X-Men/Fantastic Four
    "X-Men: Days of Future Past",
    "X-Men: Apocalypse",
    "Dark Phoenix",
    "The New Mutants",
    "Deadpool",
    "Deadpool 2",
    "Logan",
    "Fantastic Four (2015)",
    "Fantastic Four",

    # DC Films (already covered in DC_FILMS list)
    # Warner Bros Batman
    "The Dark Knight",
    "The Dark Knight Rises",
    "Batman Begins",
    "Batman v Superman: Dawn of Justice",
    "Justice League",
    "Zack Snyder's Justice League",

    # Other DC
    "Superman Returns",
    "Green Lantern",
    "Catwoman",
    "Jonah Hex",

    # Other Studios
    "The Punisher",
    "Punisher: War Zone",
    "Ghost Rider",
    "Ghost Rider: Spirit of Vengeance",
    "Blade: Trinity",
    "Elektra",
    "Daredevil",
    "The Spirit",
    "Hellboy",
    "Hellboy II: The Golden Army",
    "The Rocketeer",
    "The Phantom",
    "The Shadow",
    "Dick Tracy",
]

# Combined lists for easy access
ALL_LIVE_ACTION_REMAKES = DISNEY_LIVE_ACTION_REMAKES + OTHER_LIVE_ACTION_REMAKES
ALL_SUPERHERO_FILMS = MARVEL_MCU_FILMS + DC_FILMS + NON_MCU_SUPERHERO_FILMS

# Title patterns for flexible matching (when exact titles don't match)
REMAKE_PATTERNS = {
    'live_action_remakes': [
        # Disney remakes
        'Beauty and the Beast', 'Aladdin', 'The Lion King', 'Mulan', 'Dumbo',
        'Cinderella', 'The Jungle Book', 'Alice in Wonderland', 'Maleficent',
        'Christopher Robin', 'Lady and the Tramp', 'Pinocchio', 'Peter Pan',
        'Snow White', 'Mufasa', 'Lilo.*Stitch', 'Little.*Mermaid', 'Moana',
        # DreamWorks/Universal remakes
        'How to Train Your Dragon'
    ],
    'other_adaptations': [
        'How to Train Your Dragon', 'Sonic', 'Pokemon', 'Detective.*Pikachu',
        'Transformers', 'G.I. Joe', 'Teenage Mutant Ninja Turtles',
        'The Smurfs', 'Garfield', 'Scooby', 'Tom.*Jerry', 'Angry Birds',
        'Battleship', 'Clue', 'Monopoly', 'Jurassic.*World', 'Minions',
        'Despicable.*Me', 'Finding.*Dory', 'Jumanji', 'Secret.*Life.*Pets',
        'Spectre', 'Bond', 'James.*Bond', 'Minecraft'
    ],
    'superhero': [
        'Spider.*Man', 'Batman', 'Superman', 'Wonder Woman', 'Aquaman',
        'Flash', 'Green.*Lantern', 'Fantastic.*Four', 'X.*Men', 'Deadpool',
        'Wolverine', 'Venom', 'Ghost.*Rider', 'Punisher', 'Daredevil',
        'Hellboy', 'Blade', 'Iron.*Man', 'Thor', 'Captain.*America',
        'Hulk', 'Avengers', 'Guardians.*Galaxy', 'Ant.*Man', 'Doctor.*Strange',
        'Black.*Panther', 'Captain.*Marvel', 'Shazam', 'Suicide.*Squad',
        'Justice.*League', 'Dark.*Knight', 'Man.*of.*Steel'
    ],
    'star_wars': [
        'Star Wars', 'Rogue One', 'Solo.*Star Wars', 'Force Awakens',
        'Last Jedi', 'Rise.*Skywalker'
    ],
    'fast_furious': ['Fast', 'Furious'],
    'harry_potter': ['Harry Potter', 'Hogwarts', 'Fantastic Beasts']
}

# Remake indicators in titles
REMAKE_TITLE_INDICATORS = [
    'Reboot', 'Remake', 'Origins', 'Begins', 'Returns', 'Forever', 'Rising'
]