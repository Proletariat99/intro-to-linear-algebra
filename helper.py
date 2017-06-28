import matplotlib.pyplot as plt
import numpy as np
import seaborn

def initialize_2d_plot(x_min=-1, x_max=8, y_min=-1, y_max=8):
    """Default values: x_min=-1, x_max=8, y_min=-1, y_max=8"""
    plt.xlim([x_min,x_max])
    plt.ylim([y_min,y_max])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black') 
        
def draw_vector(np_array, tail=np.array([0,0]), kwargs=None):
    """Pass a vector of length 2 and a figure.
       Optionally, specify a start point. Defaults to the origin.
       """
    u_1 = np_array[0]
    u_2 = np_array[1]
    tail_1 = tail[0]
    tail_2 = tail[1]
    if kwargs:
        plt.arrow(tail_1,tail_2,u_1,u_2, **kwargs, head_width=0.25, head_length=0.25)
    else:
        plt.arrow(tail_1,tail_2,u_1,u_2, head_width=0.25, head_length=0.25)