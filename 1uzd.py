"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""

class AAA:
    def __init__ (self):
            self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'x',
            40:'XL',
            50:'L',
            90:'XC',
            100:'c',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
      }
      
    def to_roman(self, num):
        result = "" 
        for value, numeral in sorted(self.roman_numerals.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value
            return result
        
#pimērs
skaitlis=2023
#definējam objektu
kk=AAA()
#jaunajam objekta jāizsauc klases metode
romieshu=kk.to_roman(skaitlis)
#noformēt izdruku

print(f"{skaitlis} ar romiešu cipariem ir {romieshu}.")