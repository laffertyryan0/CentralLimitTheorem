import matplotlib.pyplot as plt
import random

#function to generate a sample from a given distribution
def get_sample(sample_size, dist = 'uniform'):
    sample = []
    if(dist == 'uniform'):
        sample = [random.uniform(0,1) for i in range(sample_size)]
    else:
        raise(Exception('Distribution not found.'))
    return sample

def get_sample_dist(sample_size = 30, trials = 10000, dist = 'uniform'):
    samples = [get_sample(sample_size,dist) for i in range(trials)]

    #compute sample means
    means = [sum(sample)/len(sample) for sample in samples]

    #compute pdf using the following approximation
    #p(x) dx = Pr(x<mean<x+dx)

    x_min = 0
    x_max = 1
    dx = .001

    xvals = []
    pdf = []

    for i in range(round((x_max - x_min)/dx)):
        x = -x_min + i * dx
        xvals.append(x)
        filt = lambda y: x < y < x + dx
        prob = len(list(filter(filt,means)))/trials
        pdf.append(prob/dx)

    return [xvals,pdf]


#plot the sample distribution
def plot_dist(sample_size = 30, trials = 10000, dist = 'uniform'):
    xvals, pdf = get_sample_dist(sample_size,trials,dist)
    #display the distribution of sample mean
    plt.plot(xvals,pdf)
    plt.show()
        
def main():
    plot_dist(50,10000)

if __name__ == '__main__':
    main()
