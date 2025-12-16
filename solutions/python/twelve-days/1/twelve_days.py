
def recite(start_verse, end_verse):
    cases = [("first", "a Partridge in a Pear Tree"),
             ("second", "two Turtle Doves"),
             ("third",  "three French Hens"),
             ("fourth", "four Calling Birds"),
             ("fifth", "five Gold Rings"),
             ("sixth", "six Geese-a-Laying"),
             ("seventh", "seven Swans-a-Swimming"),
             ("eighth", "eight Maids-a-Milking"),
             ("ninth", "nine Ladies Dancing"),
             ("tenth", "ten Lords-a-Leaping"),
             ("eleventh", "eleven Pipers Piping"),
             ("twelfth", "twelve Drummers Drumming")]

    verses = []
    
    for i in range(start_verse-1, end_verse):
        sub_verse = ""
        for j in range(i, 0, -1):
            sub_verse += f"{cases[j][1]}, "
        sub_verse += f"and {cases[0][1]}" if i > 0 else f"{cases[0][1]}" 
        verse = f"On the {cases[i][0]} day of Christmas my true love gave to me: {sub_verse}."
        verses.append(verse)

       
    return verses
