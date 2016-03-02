from __future__ import division

import numpy as np
import pandas as pd
import sklearn as sk
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.svm import SVC

import statsmodels.api as sm
import statsmodels.formula.api as smf

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

scatter = sns.jointplot(x="x",y="y",data=df, kind="scatter",stat_func=None)
scatter.savefig("scatter.pdf")

cluster = sns.jointplot(x="x",y="y",data=df, kind="kde",stat_func=None)
cluster.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
cluster.savefig("cluster.pdf")

def distplot_color(a,color=None,ax=None,**kwargs):
    if "kde_kws" not in kwargs:
        kwargs["kde_kws"] = dict()
   
    for c in color.unique():
        selection = np.asarray(color == c,dtype=bool)
        kwargs["kde_kws"]["color"] = c
        sns.distplot(a[selection],color=c,ax=ax,**kwargs)
        
    return ax

color_scatter = sns.JointGrid(x="x",y="y",data=df)
color_scatter  = color_scatter.plot_joint(plt.scatter,color=df.group_color)
color_scatter  = color_scatter.plot_marginals(distplot_color,color=df.group_color)
color_scatter.savefig("color_scatter.pdf")

da = df[["x","y"]].as_matrix()
#kmlabels = [KMeans(n_clusters=i+1).fit_predict(da) for i in xrange(4)]
for i in xrange(4):
    df["kmeans_{}".format(i+1)] = KMeans(n_clusters=i+1).fit_predict(da)   

kmeans = plt.figure()
for i in xrange(4):
    ax = kmeans.add_subplot(2,2,i+1)
    labels = [sns.categorical.color_palette("muted")[_] for _ in df["kmeans_{}".format(i+1)]]
    ax.scatter(df.x,df.y,c=labels)
    #accuracy = np.sum(df["kmeans_{}".format(i+1)] == df["group"]) / df.shape[0]
    #kmeans.text(4,4,accuracy)
    ax.set_title("{} cluster{}".format(i+1,"s" if i else "" ))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    
kmeans.savefig("kmeans.pdf")

pca = PCA().fit_transform(da)
df["pca1"] = pca[:,0]
df["pca2"] = pca[:,1]
color_scatter_pca = sns.JointGrid(x="pca1",y="pca2",data=df)
color_scatter_pca  = color_scatter_pca.plot_joint(plt.scatter,color=df.group_color)
color_scatter_pca  = color_scatter_pca.plot_marginals(distplot_color,color=df.group_color)
color_scatter_pca.savefig("color_scatter_pca.pdf")

svm = SVC(kernel="linear").fit(da,df.group)
df["svm"] = svm.predict(da)
df["svm_color"] = [sns.categorical.color_palette("muted")[_] for _ in df["svm"]]

xx, yy = np.meshgrid(np.arange(df.x.min() - 0.5, df.x.max() + 0.5, 0.1),
                         np.arange(df.y.min() - 0.5, df.y.max() + 0.5, 0.1))
# Plot the decision boundary.
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
# Put the result into a color plot
Z = Z.reshape(xx.shape)
svm_train = plt.figure()
ax = svm_train.gca()
ax.contourf(xx, yy, Z, alpha=.8)
ax.scatter(df.x,df.y,c=df.group_color)
accuracy = "Accuracy: {}".format(svm.score(df[["x","y"]].as_matrix(),df.group))
ax.text(2,5.0,accuracy)
svm_train.savefig("svm_train.pdf")

# test set
blobs = datasets.make_blobs(n_samples=100,
                            n_features=2,
                            centers=[(-2,2),(2,-2)],
                            cluster_std=[1.3,1.5],
                            random_state=43)
test = pd.DataFrame(blobs[0],columns=["x","y"])
test["group"] = blobs[1]
test["group_color"] = [sns.categorical.color_palette("muted")[_] for _ in blobs[1]]

color_scatter_test = sns.JointGrid(x="x",y="y",data=test)
color_scatter_test  = color_scatter_test.plot_joint(plt.scatter,color=test.group_color)
color_scatter_test  = color_scatter_test.plot_marginals(distplot_color,color=test.group_color)
color_scatter_test.savefig("color_scatter_test.pdf")

xx, yy = np.meshgrid(np.arange(test.x.min() - 0.5, test.x.max() + 0.5, 0.1),
                         np.arange(test.y.min() - 0.5, test.y.max() + 0.5, 0.1))
# Plot the decision boundary.
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
# Put the result into a color plot
Z = Z.reshape(xx.shape)
svm_test = plt.figure()
ax = svm_test.gca()
ax.contourf(xx, yy, Z, alpha=.8)
ax.scatter(test.x,test.y,c=test.group_color)
accuracy = "Accuracy: {}".format(svm.score(test[["x","y"]].as_matrix(),test.group))
ax.text(2,5.5,accuracy)
svm_test.savefig("svm_test.pdf")


blobs = datasets.make_blobs(n_samples=1000,
                            n_features=2,
                            centers=[(0,0),(2,1),(-3,-1.5),(-2,0.5),(2,-3)],
                            random_state=42)
big_train = pd.DataFrame(blobs[0],columns=["x","y"])
big_train["group"] = blobs[1]
big_train["group_color"] = [sns.categorical.color_palette("muted")[_] for _ in blobs[1]]

scatter_big_train   = sns.JointGrid(x="x",y="y",data=big_train)
scatter_big_train   = scatter_big_train.plot_joint(plt.scatter,color=big_train.group_color)
scatter_big_train   = scatter_big_train.plot_marginals(distplot_color,color=big_train.group_color)
scatter_big_train.savefig("scatter_big_train.pdf")

btda = big_train[["x","y"]].as_matrix()

svm = SVC(kernel="linear").fit(btda,big_train.group)
big_train["svm"] = svm.predict(btda)
big_train["svm_color"] = [sns.categorical.color_palette("muted")[_] for _ in big_train["svm"]]

scatter_big_train_svm   = sns.JointGrid(x="x",y="y",data=big_train)
scatter_big_train_svm   = scatter_big_train_svm.plot_joint(plt.scatter,color=big_train.svm_color)
scatter_big_train_svm   = scatter_big_train_svm.plot_marginals(distplot_color,color=big_train.svm_color)
accuracy = "Accuracy: {}".format(svm.score(big_train[["x","y"]].as_matrix(),big_train.group))
scatter_big_train_svm.fig.get_children()[1].text(3,5,accuracy)
scatter_big_train_svm.savefig("scatter_big_train_svm.pdf")

blobs = datasets.make_blobs(n_samples=1000,
                            n_features=2,
                            centers=[(0,0),(2,1),(-3,-1.5),(-2,0.5),(2,-3)],
                            random_state=43)
big_test = pd.DataFrame(blobs[0],columns=["x","y"])
big_test["group"] = blobs[1]
big_test["group_color"] = [sns.categorical.color_palette("muted")[_] for _ in blobs[1]]

scatter_big_test   = sns.JointGrid(x="x",y="y",data=big_test)
scatter_big_test   = scatter_big_test.plot_joint(plt.scatter,color=big_test.group_color)
scatter_big_test   = scatter_big_test.plot_marginals(distplot_color,color=big_test.group_color)
scatter_big_test.savefig("scatter_big_test.pdf")

btda = big_test[["x","y"]].as_matrix()

svm = SVC(kernel="linear").fit(btda,big_test.group)
big_test["svm"] = svm.predict(btda)
big_test["svm_color"] = [sns.categorical.color_palette("muted")[_] for _ in big_test["svm"]]

scatter_big_test_svm   = sns.JointGrid(x="x",y="y",data=big_test)
scatter_big_test_svm   = scatter_big_test_svm.plot_joint(plt.scatter,color=big_test.svm_color)
scatter_big_test_svm   = scatter_big_test_svm.plot_marginals(distplot_color,color=big_test.svm_color)
accuracy = "Accuracy: {}".format(svm.score(big_test[["x","y"]].as_matrix(),big_test.group))
scatter_big_test_svm.fig.get_children()[1].text(3,5,accuracy)
scatter_big_test_svm.savefig("scatter_big_test_svm.pdf")
