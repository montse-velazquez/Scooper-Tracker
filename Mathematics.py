
import os
from datetime import date   
from statistics import mean
from math import isnan
from itertools import filterfalse

#Class where it will be stored with fucntions about stadistics, such as the trend, flavors most time scooped and others.
class Mathematics: 
    def __init__(self, listes, name):
        self.listes = listes
        self.name = name
    
    def sort_list(self):
        sort_lists = []
        for flavs in self.listes:
            sort_lists.append(self.listes[flavs])
        sort_lists = sorted(sort_lists)
        key_list = list(self.listes.keys())
        val_list = list(self.listes.values())
        try:
            position = val_list.index(sort_lists[-1])
        except IndexError:
            print("there haven't been selling so far in", self.name)
        
        print("The flavour with bigger selling today was", key_list[position].capitalize(), "by selling: ", sort_lists[-1], "Scoops")
        return sort_lists

    def get_media(self):
        average = (float(mean(list(self.listes.values()))))
        sum_up = sum(list(self.listes.values())) 
        return print("From ", sum_up, "scoops sold of the", self.name, ",at least", average, "of the scoops were of this same flavour"   )

    def get_less_favorite(self):
        for i in self.listes:
            if self.listes[i] == 0:
                self.listes[i] = float('NaN')
            else: 
                pass
        print(sum(map(isnan, list(self.listes.values()))), '/', len(self.listes), "flavours in", self.name, "didnt sold any scoop at all")


        clean = list(filterfalse(isnan, list(self.listes.values())))
        key_list = list(self.listes.keys())
        val_list = list(self.listes.values())
        print("The next flavours were the only ones that made sales today")
        for i in clean: 
            position = val_list.index(i)
            print("- ", key_list[position].capitalize()) 

