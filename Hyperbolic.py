import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def do_thi_hyperbolic1(x,y):
 z1 = (((x/3)**2 + (y/5)**2 - 1)*4)**1/2
 return z1
def do_thi_hyperbolic2(x,y):
 z2 = -(((x / 3) ** 2 + (y / 5) ** 2 - 1) * 4) ** 1 / 2
 return z2
def do_thi_hyperbolic():
 x = np.linspace(-10, 10, 200)
 y = np.linspace(-10, 10, 200)
 x,y = np.meshgrid(x,y)
 z1 = do_thi_hyperbolic1(x,y)
 z2 = do_thi_hyperbolic2(x,y)
 fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
 mat_hyperbolic1 = ax.plot_surface(x, y, z1, cmap='plasma', linewidth=0, antialiased=False)
 mat_hyperbolic2 = ax.plot_surface(x, y, z2, cmap='plasma', linewidth=0, antialiased=False)
 ax.set_xlabel('truc hoanh')
 ax.set_ylabel('truc tung')
 ax.legend()
 plt.show()

def main():
    do_thi_hyperbolic()
if __name__ == '__main__':
        main()
