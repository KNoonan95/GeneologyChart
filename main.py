import holoviews as hv
import numpy as np

hv.extension('bokeh')

def create_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    curve = hv.Curve((x, y), 'x', 'sin(x)')
    return curve

if __name__ == "__main__":
    plot = create_plot()
    hv.save(plot, 'output/plot.html', backend='bokeh')

def dummy_test():
    pass
