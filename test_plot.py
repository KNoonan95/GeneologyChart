# test_plot.py
import os

def test_plot_file_exists():
    assert os.path.exists('output/plot.html'), "Plot HTML file was not created."
