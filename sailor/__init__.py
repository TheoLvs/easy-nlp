

# Default matplotllib
import matplotlib.pyplot as plt

plt.style.use("seaborn-white")
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['figure.figsize'] = (15,6)

# import pandas.plotting as pdplot

# def plot_with_matplotlib_cmap(*args, **kwargs):
#     kwargs.setdefault("colormap", matplotlib.rcParams.get("image.cmap", "Spectral"))
#     return pdplot.plot_frame_orig(*args, **kwargs)

# pdplot.plot_frame_orig = pdplot.plot_frame
# pdplot.plot_frame = plot_with_matplotlib_cmap
# pd.DataFrame.plot = pdplot.plot_frame

