import  numpy
import matplotlib.pyplot as plt
import get_coordinates


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a,b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))
    @staticmethod
    def get_total_distance(coord):
        dist = 0
        for first, second in zip(coord[:-1],coord[1:]):
            dist+= Coordinate.get_distance(first,second)
        dist += Coordinate.get_distance(coord[0],coord[-1])
        return  dist

if __name__ == '__main__':
    #coordinates
    n = 50
    coord = get_coordinates.coordinates(n)


    #plotting the coordinates
    fig = plt.figure(figsize=(12,6))
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,4)
    ax4 = fig.add_subplot(2,2,3)
    for first, second in zip(coord[:-1], coord[1:]):
        ax1.plot([first.x, second.x],[first.y,second.y],'b')

    ax1.plot([coord[0].x,coord[-1].x],[coord[0].y,coord[-1].y],'b')
    for c in coord:
        ax1.plot(c.x,c.y, 'ro')

    # Simulated annealing algo
    cost0 = Coordinate.get_total_distance(coord)

    T = 20
    alpha = 0.99
    T_init = T
    cost_val = []
    cost_print = []
    prob = []
    step = []
    for i in range(1000):
        cost_val.append(T)
        cost_print.append(cost0)
        p=1
        step.append(i)


        T = T*alpha
        for j in range(500):
            #Exchange 2 coordinates and get neighbouring soln
            r1,r2 = numpy.random.randint(0,len(coord),size=2)

            temp = coord[r1]
            coord[r1] = coord[r2]
            coord[r2] = temp

            cost1 = Coordinate.get_total_distance(coord)
            p= numpy.exp((cost0-cost1)/T)

            #New cost

            if cost1 < cost0:
                cost0 = cost1
                p=1
            else:
                x = numpy.random.uniform()
                if x < p:
                    cost0 = cost1
                else:
                    temp = coord[r1]
                    coord[r1] = coord[r2]
                    coord[r2] = temp
        prob.append(p)

    # Result

    print(cost0)
    for first, second in zip(coord[:-1], coord[1:]):
        ax2.plot([first.x, second.x], [first.y, second.y], 'b')

    ax2.plot([coord[0].x, coord[-1].x], [coord[0].y, coord[-1].y], 'b')
    for c in coord:
        ax2.plot(c.x, c.y, 'ro')

    ax3.plot(cost_val,cost_print)
    ax4.plot(step,prob,'ro')

    plt.show()



