from math import *
from Composer_with_GA.Otherutils.otherutil import *

def calculate_fitness(chord, mel, prmel, refmel, curfit):
    mel = notecalc(mel)
    prmel = notecalc(prmel)

    rml = notecalc(refmel).ReturnNote_abs() #reference melody's Note
    mnote = mel.ReturnNote() #melody's Current Note
    mna = mel.ReturnNote_abs() #melody's Current Note absolute(0~88)
    pnote = prmel.ReturnNote()
    pna = prmel.ReturnNote_abs()
    moct = mel.ReturnOct()
    poct = prmel.ReturnOct()
    ccurfit = curfit
    for c in chord:
        c = notecalc(chr(c)).ReturnNote()
        if mnote == c:
            ccurfit *= 0.95
    if (mna == refmel) :
            ccurfit *= 0.93
    elif (mna - pna) == (0 or 4 or 7 or 10) :
            ccurfit *= 0.95
    elif ((mnote == (2 or 7) and (mna == pna -1)) or ((mnote != (2 or 7) and (mna - pna == 2)))) :
            ccurfit *= 0.955

    if (abs(mna - pna) < 8):
            ccurfit *= 0.95
    else :
        ccurfit * (abs((mna-pna)/88)+1)

    ccurfit = ccurfit*(1.25-0.25*cos(((5-moct)/8)*pi))

    return ccurfit*1.09

