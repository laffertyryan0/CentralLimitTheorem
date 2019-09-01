import matplotlib.pyplot as plt
import random

#function to generate a sample from a given distribution
def get_sample(sample_size, dist = 'uniform'):
    sample = []
    if(dist == 'uniform'):
        sample = [random.uniform(0,1) for i in range(sample_size)]
    elif(dist == 'exponential'):
        sample = [random.expovariate(1) for i in range(sample_size)]
    elif(dist == 'triangular'):
        sample = [random.triangular(0,1,.5) for i in range(sample_size)]
    else:
        raise(Exception('Distribution not found.'))
    return sample

def get_sample_dist(sample_size = 30,
                    trials = 10000,
                    dist = 'uniform',
                    x_min = 0,
                    x_max = 1,
                    dx = .01):
    samples = [get_sample(sample_size,dist) for i in range(trials)]

    #compute sample means
    means = [sum(sample)/len(sample) for sample in samples]

    x_min = x_min
    x_max = x_max
    dx = dx

    xvals = []
    pdf = []


    #compute pdf using the following approximation
    #p(x) dx = Pr(x-dx/2<mean<x+dx/2)

    for i in range(round((x_max - x_min)/dx)):
        x = x_min + i * dx
        xvals.append(x)
        filt = lambda y: x-dx/2 < y < x + dx/2
        prob = len(list(filter(filt,means)))/trials
        pdf.append(prob/dx)

    return [xvals,pdf]


#plot the sample distribution
def plot_dist(sample_size = 30,
                    trials = 10000,
                    dist = 'uniform',
                    x_min = 0,
                    x_max = 1,
                    dx = .01):
    xvals, pdf = get_sample_dist(sample_size,trials,dist,x_min,x_max)
    #display the distribution of sample mean
    plt.plot(xvals,pdf)
    plt.show()
        
def main():
    plot_dist(100,10000,dist = 'triangular')

if __name__ == '__main__':
    main()
