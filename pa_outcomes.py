"""
These functions change the present state within the core loop of the simulation according to PA outcomes.

This code is taken and slightly adapted from Ben Clemens, originally used in his article about Austin Hedges here:
https://blogs.fangraphs.com/some-fun-with-austin-hedges-a-baseball-extreme/
"""
def OneBaseSingle(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,1,0]
    elif VarState == [1,1,0]:
        VarState = [1,1,0]
        RunCount+=1
    elif VarState == [1,0,1]:
        VarState = [1,1,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,1,0]
        RunCount+=2
    elif VarState == [0,1,0]:
        VarState = [1,0,0]
        RunCount+=1
    elif VarState == [0,1,1]:
        VarState = [1,0,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [1,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def TwoBaseSingle(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,0,1]
    elif VarState == [1,1,0]:
        VarState == [1,0,1]
        RunCount +=1
    elif VarState == [1,0,1]:
        VarState == [1,0,1]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,0,1]
        RunCount +=2
    elif VarState == [0,1,0]:
        VarState = [1,0,0]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [1,0,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [1,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Double(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,1,0]
    elif VarState == [1,0,0]:
        VarState = [0,1,1]
    elif VarState == [1,1,0]:
        VarState = [0,1,1]
        RunCount +=1
    elif VarState == [1,0,1]:
        VarState = [0,1,1]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [0,1,1]
        RunCount +=2
    elif VarState == [0,1,0]:
        VarState = [0,1,0]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [0,1,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [0,1,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Triple(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,0,1]
    elif VarState == [1,0,0]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [1,1,0]:
        VarState = [0,0,1]
        RunCount +=2
    elif VarState == [1,0,1]:
        VarState = [0,0,1]
        RunCount+=2
    elif VarState == [1,1,1]:
        VarState = [0,0,1]
        RunCount +=3
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=2
    elif VarState == [0,0,1]:
        VarState = [0,0,1]
        RunCount +=1
    return VarState,RunCount,OutCount

def HomeRun(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,0,0]
        RunCount +=1
    elif VarState == [1,0,0]:
        VarState = [0,0,0]
        RunCount +=2
    elif VarState == [1,1,0]:
        VarState = [0,0,0]
        RunCount +=3
    elif VarState == [1,0,1]:
        VarState = [0,0,0]
        RunCount+=3
    elif VarState == [1,1,1]:
        VarState = [0,0,0]
        RunCount +=4
    elif VarState == [0,1,0]:
        VarState = [0,0,0]
        RunCount +=2
    elif VarState == [0,1,1]:
        VarState = [0,0,0]
        RunCount +=3
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=2
    return VarState,RunCount,OutCount

def Walk(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,1,0]
    elif VarState == [1,1,0]:
        VarState = [1,1,1]
    elif VarState == [1,0,1]:
        VarState=[1,1,1]
    elif VarState == [1,1,1]:
        VarState = [1,1,1]
        RunCount+=1
    elif VarState == [0,1,0]:
        VarState = [1,1,0]
    elif VarState == [0,1,1]:
        VarState = [1,1,1]
    elif VarState == [0,0,1]:
        VarState = [1,0,1]
    return VarState,RunCount,OutCount

def Strikeout(VarState,RunCount,OutCount):
    OutCount+=1
    return VarState,RunCount,OutCount

def Groundout(VarState,RunCount,OutCount):
    OutCount+=1
    if OutCount == 3:
        return VarState,RunCount,OutCount
    elif VarState == [0,0,0]:
        VarState = [0,0,0]
    elif VarState == [1,0,0]:
        VarState = [0,1,0]
    elif VarState == [1,1,0]:
        VarState = [0,1,1]
    elif VarState == [1,0,1]:
        VarState = [0,1,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [0,1,1]
        RunCount +=1
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def GIDP(VarState,RunCount,OutCount):
    if OutCount == 2:
        OutCount+=1
    elif VarState == [0,0,0]:
        VarState=[0,0,0]
        OutCount+=1
    elif VarState == [1,0,0]:
        VarState=[0,0,0]
        OutCount+=2
    elif VarState == [1,1,0]:
        VarState =[0,0,1]
        OutCount+=2
    elif VarState == [1,0,1]:
        VarState = [0,0,0]
        if OutCount == 1:
            OutCount+=2
        else:
            OutCount+=2
            RunCount+=1
    elif VarState == [1,1,1]:
        VarState=[0,0,1]
        if OutCount ==1:
            OutCount+=2
        else:
            OutCount+=2
            RunCount+=1
    elif VarState == [0,1,0]:
        VarState=[0,0,1]
        OutCount+=1
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=1
        OutCount+=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount+=1
        OutCount+=1
    return VarState,RunCount,OutCount

def Flyout(VarState,RunCount,OutCount):
    OutCount+=1
    if OutCount == 3:
        return VarState,RunCount,OutCount
    elif VarState == [0,0,0]:
        VarState == [0,0,0]
    elif VarState == [1,0,0]:
        VarState == [1,0,0]
    elif VarState == [1,1,0]:
        VarState = [1,0,1]
    elif VarState == [1,0,1]:
        VarState = [1,0,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,0,1]
        RunCount +=1
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Lineout(VarState,RunCount,OutCount):
    OutCount+=1
    return VarState,RunCount,OutCount
