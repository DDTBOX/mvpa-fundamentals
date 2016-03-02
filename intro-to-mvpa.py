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

scatter = sns.jointplot(x="x",y="y",data=df, kind="scatter")
scatter.savefig("scatter.pdf")

cluster = sns.jointplot(x="x",y="y",data=df, kind="kde")
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


trainsvm_test = plt.figure()
ax = svm_test.gca()
ax.contourf(xx, yy, Z, alpha=.8)
ax.scatter(test.x,test.y,c=test.group_color)
accuracy = "Accuracy: {}".format(svm.score(test[["x","y"]].as_matrix(),test.group))
ax.text(2,5.5,accuracy)
svm_test.savefig("svm_test.pdf")


blobs = datasets.make_blobs(n_samples=1000,
                            n_features=2,
                            centers=5,
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
scatter_big_train_svm.savefig("scatter_big_train_svm.pdf")

#xx, yy = np.meshgrid(np.arange(big_train.x.min() - 0.5, big_train.x.max() + 0.5, 0.1),
#                         np.arange(big_train.y.min() - 0.5, big_train.y.max() + 0.5, 0.1))
## Plot the decision boundary.
#Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
## Put the result into a color plot
#Z = Z.reshape(xx.shape)
#svm_big_train = plt.figure()
#ax = svm_big_train.gca()
#ax.contourf(xx, yy, Z, alpha=.8)
#ax.scatter(big_train.x,big_train.y,c=big_train.group_color)
#accuracy = "Accuracy: {}".format(svm.score(big_train[["x","y"]].as_matrix(),big_train.group))
#svm_big_train.savefig("svm_big_train.pdf")

