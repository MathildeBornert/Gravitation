import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

n=2
G=1
m=np.random.randint(1,5,(1,n))
pos=np.random.randint(-5,6,(n,2))
v= np.zeros((n,2))
dt=0.01
pos=np.concatenate(pos,v)

ax.axis('equal')
#ax.set(xlim=[-1, 1000], ylim=[-1,1000])

def d(P1,P2):
    return (P1[0]-P2[0])**2 +(P1[1]**2 - P2[1]**2)


#pos = [[0, 1000], [0,0]]

def get_new_position(pos):
    pos1 = pos[0][:, np.newaxis, :]
    pos2 = pos[1][np.newaxis, :, :]
    Diff = pos1-pos2
    D= np.sum(np.square(Diff), axis=2)**3/2
    F= np.dot(m, D)

    #return [[P[0]+1, P[1]-1], [V[0]+1, V[1]+1]]

scat = ax.scatter(positions[0], positions[1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(positions)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
#plt.show()


