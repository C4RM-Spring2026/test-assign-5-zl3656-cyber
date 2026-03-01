import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)                   
    t = np.arange(1, n + 1)            
    t_years = t / ppy                 
    r = y / ppy                        
    c = face * couponRate / ppy        
    cf = np.full(n, c, dtype=float)
    cf[-1] += face
    df = (1 + r) ** (-t)               
    pvcf = cf * df                     
    price = pvcf.sum()
    duration = (t_years * pvcf).sum() / price
    return float(duration)

