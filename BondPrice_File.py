import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)                         
    t = np.arange(1, n + 1)                   
    r = y / ppy                               
    c = face * couponRate / ppy               
    df = (1 + r) ** (-t)                      
    price = c * df.sum() + face * df[-1]      
    return float(price)