import numpy as np
import matplotlib.pyplot as plt

SIFS = 10  # us
slot = 20  # us slot time
DIFS = 2 * slot + SIFS
Rb = 6
Tb = 1 / Rb
CWmin = 32  # %minimal Contention Window
CWmax = 1024  # maximal Contention Window
RTS = round(20 * 8 * Tb)  # 20Byte for RTS
CTS = round(14 * 8 * Tb)  # 14Byte for CTS
ACK = round(14 * 8 * Tb)  # 14Byte for ACK
# Nnode = 2  # number of active nodes
Nlp = int(1e5)

# collision probability
def collision(CWmin, n):
    s = 0
    for i in range(1, CWmin - 1):
        si = (i / 32) ** (n - 1)
        s += si
    return 1 - n / 32 * s


nodes, p, p1 = [], [], []
for Nusr in range(1, 50):  # Num of users
    Ncln = 0
    print(Nusr)
    for i in range(Nlp):
        BC = np.random.randint(CWmin, size=Nusr)
        minBC = min(BC)
        BC = BC - minBC
        ind = np.where(BC == 0)
        if len(ind[0]) > 1:
            Ncln += 1
    nodes.append(Nusr)
    p.append(Ncln / Nlp * 100)
    # p1.append(collision(CWmin, Nusr) * 100)

fig = plt.figure(1, figsize=(24, 18))
plt.plot(p, 'ro')
plt.title('Figure 2: Collision probability versus number of active nodes')
plt.xlabel('number of active nodes')
plt.ylabel('Collision probability')
plt.show()
fig.savefig('Probability of collision')
