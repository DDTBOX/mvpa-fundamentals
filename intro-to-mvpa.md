---
title: An introduction to multivariate pattern analysis
author: Phillip M. Alday
date: 4 March 2015
---

# Why MVPA?

## How many clusters are there?
\centering
\includegraphics[width=0.75\textwidth]{scatter.pdf}

## Two, right?
\centering
\includegraphics[width=0.75\textwidth]{cluster.pdf}

## Two, because I made it that way
\centering
\includegraphics[width=0.75\textwidth]{color_scatter.pdf}


## MultiVariate Pattern Analysis
- multivariate life is hard, so we often go univariate on our dependent measure, e.g. mean ERP voltage in a given time window
- it's often possible to 'fake' multivariate analysis by including additional independent measures, e.g. ROI
- this doesn't imply anything about causality, but some of the mathematical details differ
- e.g. how do we test ERP topographies against each other?
- MVPA is a modern approach drawing from computational advances of the last few decades

## The Two Cultures [@breiman2001a]

### Data modelling (*statistics*)
- assumes that the structure of the statistical model somehow reflects the structure of reality
- focus on estimation
- interpretability of model parameters important
- often expressed as "Is $x$ a significant predictor of $y$?"

### Algorithmic modelling (*machine learning*)
- assumes that the structure of the statistical model is irrelevant because the structure of reality is not known
- focus on prediction
- interpretability of model parameters not important
- often expressed as "How accurate is my model (when applied to new data)"?

## Multivariate "statistics"
- PCA and its reincarnation factor analysis
- MANOVA
- Linear discriminant analysis
- simultaneous equation modles (e.g. $(Y_1, Y_2) = \beta{}X + \beta_0 + \varepsilon$)

## Multivariate "machine learning"
- classification
    - neural networks
    - support vector machines (SVM)
    - naive Bayes
- clustering (automatic grouping of similar objects into sets)
    - $k$-means
    - and many others

# Machine learning

## Machine learning

### Supervised learning
The computer is "taught" via a training set where we already know the answers, i.e. what's right and wrong.

### Unsupervised learning
The computer must "explore" the training set to find the solution best matching our assumptions (often expressed via algorithmic choice).

. . .

**Both types of machine learning involve a number of assumptions. While they are arguably more "data-driven" than traditional statistical modelling in the sense that the model structure is selected algorithmically, the ultimate shape of the model is dependent on both the data and the assumptions!**

## Clustering with $k$-means
\includegraphics[width=\textwidth]{kmeans.pdf}

## There is no ideal clustering method

\includegraphics[width=\textwidth]{plot_cluster_comparison_0011.png}

\vfill\tiny\hfill{} \url{http://scikit-learn.org/stable/modules/clustering.html}

# Support vector machines

## Classifying with Support Vector Machines
- in our experiments, we typically know what the categories are (conditions), but we need to find the prototypical "geography" / topography
- supervised-learning with support vector machines (SVM)

## Partition the space up
\begin{columns}
\column{0.7\textwidth}
\includegraphics[width=\textwidth]{color_scatter.pdf}

\pause
\column{0.4\textwidth}
\begin{itemize}
\item find a dividing line between groups \pause
\item (this example is somewhat trivial as the cluster centers mirrored across $y=x$)
\end{itemize}

\end{columns}

## How could you do this with PCA?
### What will the components be?
\begin{columns}
\column{0.5\textwidth}
\includegraphics[width=\textwidth]{color_scatter.pdf}
\pause

\column{0.5\textwidth}
\includegraphics[width=\textwidth]{color_scatter_pca.pdf}
\end{columns}

\pause
This only works because we have two categories in two dimensions and thus the border is one-dimensional, i.e. the same size as a single component.

## Support Vector Machines
- SVM works by constructing a separating hyperplane between groups
- SVM-based classification is inherently **binary**
- but it is possible to combine binary decisions to make complex decisions
    - one-vs-one: construct an SVM for every pairwise combination of group
    - one-vs-all: construct an SVM for every group
- The further away the separating hyperplane is from the nearest elements of each group, the better this works.

## The theory behind this (or check your assumptioms)

\begin{theorem}[Hahn-Banach]
There exists a hyperplane between any two disjoint, convex sets in Euclidean space.
\end{theorem}

In other words, if the two groups do not overlap and are not intertwined / wrapped around each other, then we can construct a linear border between them.

\begin{theorem}
Every permutation can be written as the product of transpositions.
\end{theorem}

It is possible to express arbitrarily complex multiple choice questions as a series of yes-no questions.

##  Our easy example

\begin{columns}
\column{0.8\textwidth}
\includegraphics[width=\textwidth]{svm_train.pdf}

\column{0.4\textwidth}
\begin{itemize}
\item no overlap
\item circular blobs are convex \pause
\item perfect accuracy when applied back to itself
\end{itemize}

\end{columns}

## But does it have predictive power?
\begin{columns}
\column{0.7\textwidth}
\includegraphics<1>[width=\textwidth]{color_scatter_test.pdf}
\includegraphics<2->[width=\textwidth]{svm_test.pdf}

\column<3>{0.4\textwidth}
\begin{itemize}
\item small amount of overlap
\item new data -- ``memorization" not possible
\item high predictive power
\end{itemize}
\end{columns}

## A more complex example
### Training data


\begin{columns}

\column{0.5\textwidth}
\centering Ground truth \\
\includegraphics[width=\textwidth]{scatter_big_train.pdf}

\column{0.5\textwidth}
\centering SVM classification \\
\includegraphics[width=\textwidth]{scatter_big_train_svm.pdf}

\end{columns}

SVM is pretty good for such ideal data. Linear regression doesn't need the points to lie exactly on a line, and SVM doesn't need exactly separable data, but both do better the closer you are to meeting these assumptions.

## A more complex example
### Test data
\begin{columns}

\column{0.5\textwidth}
\centering Ground truth \\
\includegraphics[width=\textwidth]{scatter_big_test.pdf}

\column{0.5\textwidth}
\centering SVM classification \\
\includegraphics[width=\textwidth]{scatter_big_test_svm.pdf}

\end{columns}

It's particularly important that we look at the predictive power and not just the model fit when dealing with high-parameter models. These data were constructed to be quite similar, so the predictive power is good, but the real-world is rarely so clean.


## Cross-validation
- Training and testing on the same data is cheating -- it hides "memorizing" the exam without understanding the material.
- Cross-validation allows you get around this with one dataset.
- Many different ways to do this, related to the jacknife in non-parametric statistics, such as
    - Leave-one-out (LOO)
    - $k$-fold validation




## There is no ideal classifier

\includegraphics[width=\textwidth]{plot_classifier_comparison_001.png}

\vfill\tiny\hfill{} \url{http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html}



## References {.allowframebreaks}
