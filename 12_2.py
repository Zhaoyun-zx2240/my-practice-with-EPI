import re


def character_lookup(
    text: str
  ) -> dict:
    '''
    O(n)
    '''
    lookup = {}
    characters = re.findall(r'[a-zA-Z]', text)
    for character in characters:
        if lookup.get(character):
            lookup[character] += 1
        else:
            lookup[character] = 1
    return lookup


def if_anonymous_letter_constructible(
    anonymous_letter: str,
    magazine: str
  ) -> bool:
    '''
    O(n)
    '''
    anonymous_lookup = character_lookup(anonymous_letter)
    magazine_lookup = character_lookup(magazine)
    for character in anonymous_lookup.keys():
        if not magazine.get(character):
            return False
        if anonymous_lookup[character] > magazine_lookup[character]:
            return False
    return True
