---
title: An introduction to multivariate pattern analysis
author: Phillip M. Alday
date: 4 March 2015
---

# Why MVPA?

## How many clusters are there?
\includegraphics[width=0.8\textwidth]{scatter.pdf}

## Two, right?
\includegraphics[width=0.8\textwidth]{cluster.pdf}

## Two, because I made it that way
\includegraphics[width=0.8\textwidth]{color_scatter.pdf}


## MultiVariate Pattern Analysis
- multivariate life is hard, so we often go univariate on our dependent measure, e.g. mean ERP voltage in a given time window
- it's often possible to 'fake' multivariate analysis by including additional independent measures, e.g. ROI
- this doesn't imply anything about causality, but some of the mathematical details differ
- e.g. how do we test ERP topographies against each other?
- MVPA is a modern approach drawing from computational advances of the last few decades

## The Two Cultures: Statistics and Machine Learning
@breiman2001a suggests that there are two cultures in statistics.

### Data modelling (*statistics*)
- assumes that the structure of the statistical model somehow reflects the structure of reality
- focus on estimation
- interpretability of model parameters important
- often expressed in practice as "Is $x$ a significant predictor of $y$?"

### Algorithmic modelling (*machine learning*)
- assumes that the structure of the statistical model is irrelevant because the structure of reality is not and potentially *cannot* be known
- focus on prediction
- interpretability of model parameters not important
- often expressed in practice as "How accurate is my model (when applied to new data)"?

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

# 20th century mathematics

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
\begin{columns}
\column{0.5\textwidth}
\includegraphics[width=\textwidth]{color_scatter.pdf}
\pause

\column{0.5\textwidth}
\includegraphics[width=\textwidth]{color_scatter_pca.pdf}
\end{columns}

\pause
This only works because we have two categories in two dimensions and thus the border is one-dimensional, i.e. the same size as a single component.


## The theory behind this
\begin{columns}
\column{0.5\textwidth}
\includegraphics[width=\textwidth]{color_scatter.pdf}

\column{0.5\textwidth}
\begin{itemize}
\item basic idea: 
\item 
\end{itemize}

\end{columns}


## There is no ideal classifier

\includegraphics[width=\textwidth]{plot_classifier_comparison_001.png}

\vfill\tiny\hfill{} \url{http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html}



## References {.allowframebreaks}