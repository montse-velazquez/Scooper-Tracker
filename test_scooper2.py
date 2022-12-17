from statistics import mean
from Mathematics import Mathematics

flavours={"pistacho": 9, "cookies and cream": 10, "chocolate": 0, "vanilla": 14, "strawberry": 2, "dulce de leche": 3, "chocalte chip": 5, "chocolate mint": 7, "mango": 4, "coffee": 10}
specials={"caramel": 3}

###ACTUAL FUNCTION###
# def get_media(self):
#         average = (float(mean(list(self.listes.values()))))
#         sum_up = sum(list(self.listes.values())) 
#         return print("From ", sum_up, "scoops sold of the", self.name, ",at least", average, "of the scoops were of this same flavour"   )

###VARIATON DONE FOR TESTING THE MAIN FUNCTIONS INSIDE OF THE METHOD###
#def get_media():
average = (float(mean(list(flavours.values()))))
sum_up = sum(list(flavours.values())) 
print("From ", sum_up, "scoops sold of the classic flavours at least", average, "of the scoops were of this same flavour"   )

def test_sumUp():
    assert sum_up == 64 
    
