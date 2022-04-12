
def to_roman(val):
        number=''
        one = val//1000
        if one < 4 and one!=0:
            number = ''.join('M'*one)
        rest = val%1000
        two = rest//100
        if two < 4 and two!=0:
            number = number+''.join('C'*two)
        elif two == 4:
            number = number+''.join('CD')
        elif two == 5:
            number = number+''.join('D')
        elif two > 5 and two < 9:
            number = number+''.join('D'+('C')*(two-5))
        elif two == 9:
            number = number+''.join('CM')
        rest_sec=rest%100
        three = rest_sec//10
        if three!=0 and three < 4: 
            number = number+''.join('X'*three)
        elif three == 4:
            number = number+''.join('XL')
        elif three == 5:
            number = number+''.join('L')
        elif three > 5 and three < 9:
            number = number+''.join('L'+('X')*(three-5))
        elif three == 9:
            number = number+''.join('XC')
        four = rest_sec%10
        if four !=0 and four<4: 
            number = number+''.join('I'*four)
        elif four == 4:
            number = number+''.join('IV')
        elif four == 5:
            number = number+''.join('V')
        elif four > 5 and four < 9: 
            number = number+''.join('V'+('I')*(four-5))
        elif four == 9:
            number = number+''.join('IX')
        return number

def from_roman(roman_num):
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000
        for i in roman_num:
            if roman_num[i]<roman_num[i+1]:
                result = roman_num[i+1]-roman_num[i]
            else:
                result = roman_num[i+1]+roman_num[i]
print(from_roman('MM'))