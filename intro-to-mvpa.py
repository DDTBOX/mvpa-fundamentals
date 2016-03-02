import numpy as np
import pandas as pd
import sklearn as sk
from sklearn import datasets
import seaborn as sns
from matplotlib import pyplot as plt

sns.set(style="white",palette="muted",color_codes=True)

blobs = datasets.make_blobs(n_samples=100,
                            n_features=2,
                            centers=[(-2,2),(2,-2)],
                            cluster_std=[1.3,1.5],
                            random_state=42)
df = pd.DataFrame(blobs[0],columns=["x","y"])
df["group"] = blobs[1]
df["group_color"] = [sns.categorical.color_palette("muted")[_] for _ in blobs[1]]

scatter = sns.jointplot(x="x",y="y",data=df, kind="scatter")
scatter.savefig("scatter.pdf")

cluster = sns.jointplot(x="x",y="y",data=df, kind="kde")
cluster.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
cluster.savefig("cluster.pdf")

def distplot_color(a,color=None,**kwargs):
    if "ax" in kwargs:
        ax = kwargs["ax"]
        del kwargs["ax"]
    else:
        ax = None
    for c in color.unique():
        selection = (color == c)
        ax = sns.distplot(a[selection],color=c,ax=ax,**kwargs)
    
    return ax

color_scatter = sns.JointGrid(x="x",y="y",data=df)
color_scatter  = color_scatter.plot_joint(plt.scatter,color=df.group_color)
color_scatter  = color_scatter.plot_marginals(distplot_color,color=df.group_color)
color_scatter; plt.show()