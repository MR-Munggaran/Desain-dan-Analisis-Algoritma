#%matplotlib inline
import matplotlib.pyplot as plt

def visualize_tour(tour,style='bo-'):
    if len(tour) > 1000: plt.figure(figsize = (15,10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')

def visualize_segment (segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')

def X(city) : "X axis"; return city.real
def Y(city) : "Y axis"; return city.imag
