"""
Movie Lists for Feature Engineering
===================================

This file contains curated lists of movies for feature detection in the box office analysis.
Lists are organized by franchise, studio, and content type for easy maintenance.
"""

# Utility --------------------------------------------------------------------

def _dedupe_preserve_order(values):
    """Return ``values`` minus duplicates while preserving original order."""

    seen = set()
    deduped = []
    for item in values:
        key = item.lower() if isinstance(item, str) else item
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped


# Disney Live-Action Remakes
DISNEY_LIVE_ACTION_REMAKES = _dedupe_preserve_order([
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
])

# Other Studio Live-Action Remakes/Adaptations
OTHER_LIVE_ACTION_REMAKES = _dedupe_preserve_order([
    "How to Train Your Dragon (2025)",  # DreamWorks/Universal
])

# Marvel Cinematic Universe Films
MARVEL_MCU_FILMS = _dedupe_preserve_order([
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
])

# DC Extended Universe / DC Films
DC_FILMS = _dedupe_preserve_order([
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
    "The Batman",
    "Joker",
    "Joker: Folie à Deux",
    "Superman",
])

# Star Wars Films (Disney Era)
STAR_WARS_FILMS = _dedupe_preserve_order([
    "Star Wars: The Force Awakens",
    "Rogue One: A Star Wars Story",
    "Star Wars: The Last Jedi",
    "Solo: A Star Wars Story",
    "Star Wars: The Rise of Skywalker",
])

# Fast & Furious Franchise
FAST_FURIOUS_FILMS = _dedupe_preserve_order([
    "Fast Five",
    "Fast & Furious 6",
    "Furious 7",
    "The Fate of the Furious",
    "Hobbs & Shaw",
    "F9: The Fast Saga",
    "Fast X",
])

# Other Franchise Sequels (sequels or spin-offs to established franchises)
FRANCHISE_SEQUELS = _dedupe_preserve_order([
    # Jurassic World (sequels to Jurassic Park)
    "Jurassic World",
    "Jurassic World: Fallen Kingdom",
    "Jurassic World Dominion",

    # Despicable Me / Minions
    "Despicable Me 2",
    "Despicable Me 3",
    "Minions",
    "Minions: The Rise of Gru",

    # Pixar sequels and spin-offs
    "Finding Dory",
    "Ralph Breaks the Internet",
    "Lightyear",

    # Franchise continuations and spin-offs
    "Bad Boys for Life",
    "Beetlejuice Beetlejuice",
    "Bumblebee",
    "Blade Runner 2049",
    "Creed",
    "Doctor Sleep",
    "Glass",
    "Godzilla vs. Kong",
    "Halloween",
    "Indiana Jones and the Dial of Destiny",
    "Jason Bourne",
    "John Wick: Chapter 2",
    "John Wick: Chapter 3 - Parabellum",
    "Kingdom of the Planet of the Apes",
    "Logan",
    "Mamma Mia! Here We Go Again",
    "Maleficent: Mistress of Evil",
    "Happy Death Day 2U",
    "Maze Runner: The Death Cure",
    "Maze Runner: The Scorch Trials",
    "Now You See Me 2",
    "Ocean's Eight",
    "10 Cloverfield Lane",
    "Pacific Rim: Uprising",
    "Split",
    "Scream",
    "Scream VI",
    "Star Trek Beyond",
    "The Equalizer 2",
    "The Equalizer 3",
    "The Nun",
    "The Nun II",
    "28 Years Later",
    "Twisters",
    "War for the Planet of the Apes",
    "Jurassic World: Rebirth",

    # Animated franchise entries
    "Hotel Transylvania 3: Summer Vacation",

    # Musical franchises
    "Frozen II",

    # Live-action fairy tale spin-offs
    "Puss in Boots: The Last Wish",

    # Horror franchises
    "A Quiet Place Part II",
    "Annabelle: Creation",
    "Annabelle Comes Home",

    # Bond films
    "Spectre",
    "Skyfall",
    "No Time to Die",
])

# Harry Potter / Wizarding World
WIZARDING_WORLD_FILMS = _dedupe_preserve_order([
    "Fantastic Beasts and Where to Find Them",
    "Fantastic Beasts: The Crimes of Grindelwald",
    "Fantastic Beasts: The Secrets of Dumbledore",
])

# Other Media Adaptations (TV Shows, Games, Toys, Book/Franchise Sequels)
MEDIA_ADAPTATIONS = _dedupe_preserve_order([
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
    "Barbie",
    "The Super Mario Bros. Movie",
    "The Super Mario Bros. Movie 2",

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
    "The Secret Life of Pets 2",
    "Finding Dory",
    "Puss in Boots: The Last Wish",
    "The Lego Batman Movie",
    "The Minecraft Movie",
    "Minecraft",

    # Jumanji franchise
    "Jumanji: Welcome to the Jungle",
    "Jumanji: The Next Level",

    # James Bond franchise (action/spy IP)
    "Spectre",
    "No Time to Die",
    "Skyfall",
])

# Non-MCU Superhero Films
NON_MCU_SUPERHERO_FILMS = _dedupe_preserve_order([
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
])

# Combined lists for easy access
ALL_LIVE_ACTION_REMAKES = _dedupe_preserve_order(
    DISNEY_LIVE_ACTION_REMAKES + OTHER_LIVE_ACTION_REMAKES
)
ALL_SUPERHERO_FILMS = _dedupe_preserve_order(
    MARVEL_MCU_FILMS + DC_FILMS + NON_MCU_SUPERHERO_FILMS
)

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
        'Sonic', 'Pokemon', 'Detective.*Pikachu',
    'Transformers', 'G.I. Joe', 'Teenage Mutant Ninja Turtles',
        'The Smurfs', 'Garfield', 'Scooby', 'Tom.*Jerry', 'Angry Birds',
        'Battleship', 'Clue', 'Monopoly', 'Jurassic.*World', 'Minions',
        'Despicable.*Me', 'Finding.*Dory', 'Jumanji',
        'Spectre', 'Bond', 'James.*Bond', 'Minecraft', 'Mario'
    ],
    'superhero': [
        'Spider.*Man', 'Batman', 'Superman', 'Wonder Woman', 'Aquaman',
        'Flash', 'Green.*Lantern', 'Fantastic.*Four', 'X.*Men', 'Deadpool',
        'Wolverine', 'Venom', 'Ghost.*Rider', 'Punisher', 'Daredevil',
        'Hellboy', '\\bBlade(?!\\sRunner)\\b', 'Iron.*Man', 'Thor', 'Captain.*America',
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

# Titles that can trip superhero pattern matching but are not superhero films
SUPERHERO_EXCLUSIONS = [
    "Blade Runner 2049",
]

# Title corrections for data quality
TITLE_CORRECTIONS = {
    "Jungle": "Jumanji: Welcome to the Jungle",
    "Singing with Angels": "Sing",
    # Fix common truncated or incorrect titles
    'Hedgehog': 'Sonic the Hedgehog 3',
    'The Wild': 'The Wild Robot',
    'Deadpool': 'Deadpool & Wolverine',  # If truncated
    'Transformer': 'Transformers',
}

def apply_title_corrections(df):
    """
    Apply systematic title corrections to fix data quality issues

    Args:
        df: DataFrame with 'title' and 'release_year' columns

    Returns:
        DataFrame with corrected titles
    """
    corrections_applied = 0

    for incorrect_title, correct_title in TITLE_CORRECTIONS.items():
        # Look for exact matches or partial matches that might be truncated
        mask = df['title'].str.contains(incorrect_title, case=False, na=False) & (df['title'] != correct_title)

        if mask.any():
            # Only fix if the found title is significantly shorter (likely truncated)
            problematic_entries = df[mask]
            for idx, row in problematic_entries.iterrows():
                if len(row['title']) < len(correct_title) * 0.8:  # Title is much shorter than expected
                    df.loc[idx, 'title'] = correct_title
                    corrections_applied += 1
                    print(f"✅ Title correction: '{row['title']}' → '{correct_title}' ({row['release_year']})")

    if corrections_applied > 0:
        print(f"Applied {corrections_applied} title corrections")
    else:
        print("No title corrections needed")
    # Contextual correction for "Deadpool & Wolverine"
    if 'release_year' in df.columns:
        m = df['title'].str.contains(r'Deadpool\s*&\s*Wolverine', case=False, na=False)
        df.loc[m & (df['release_year'] == 2016), 'title'] = 'Deadpool'
        df.loc[m & (df['release_year'] == 2018), 'title'] = 'Deadpool 2'


    return df
def tag_ip_and_sequels(df):
    """Tag IP and sequels with minimal hard-coded rules used by the notebook post-processing.
    Expects columns: 'title', optional 'is_ip', 'is_sequel'.
    """
    import pandas as pd
    if df is None or df.empty or 'title' not in df.columns:
        return df

    if 'is_ip' not in df.columns:
        df['is_ip'] = False
    if 'is_sequel' not in df.columns:
        df['is_sequel'] = False

    # 2023 specific labels
    mask_2023 = (df.get('release_year', pd.Series([None]*len(df))) == 2023)
    df.loc[mask_2023 & df['title'].str.fullmatch(r'Barbie', case=False, na=False), 'is_ip'] = True
    df.loc[mask_2023 & df['title'].str.contains(r'Super\s*Mario\s*Bros', case=False, na=False), 'is_ip'] = True
    df.loc[mask_2023 & df['title'].str.contains(r'Indiana\s*Jones', case=False, na=False), 'is_sequel'] = True
    return df
