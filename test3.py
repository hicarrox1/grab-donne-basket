def trie(lol):
    return lol.a

class lol():


    def __init__(self,a) -> None:
        
        self.a = a

    def get_number(self):
        return ord(self.a)


mp = lol('france')

lo = lol('france')

dc = lol('ukraine')

mp = lol('france')

ju = lol('nba')

ml = lol('france')

da = lol('ukraine')

liste = [mp,lo,dc,mp,ju,ml,da]

trier = sorted(liste,key=trie)

liste_name = [lol.a for lol in trier]

print(liste_name)
