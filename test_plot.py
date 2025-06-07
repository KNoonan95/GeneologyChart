# test_plot.py
import os

def test_plot_file_exists():
    assert os.path.exists('output/plot.html'), "Plot HTML file was not created."

def test_plot_file_not_empty():
    size = os.path.getsize('output/plot.html')
    assert size > 5000, "Plot HTML file is too small, likely blank."
