---
title: An introduction to EEG/ERP
subtitle: unabashedly stolen and adapted from Schlesewsy & Bornkessel
author: Phillip M. Alday, 
date: 4 March 2015
---

# Discovery of the EEG 

## Hans Berger (1873-1941)

\begin{columns}

\column{0.5\textwidth}
\begin{itemize}
\item German psychiatrist
\item  First measured human EEG
\item 1929: \emph{Über das Elektrenkephalogramm des Menschen} (On the human electroencephalogram) 
\end{itemize} 

\column{0.5\textwidth}
\includegraphics[width=0.8\textwidth]{hans_berger.jpg}

\end{columns}

## Berger's EEG lab

\includegraphics[width=\textwidth]{berger_lab.jpg}

## An early EEG trace

\includegraphics[width=\textwidth]{berger_recording.png}

## Early discoveries

- $\alpha$ (~8--12 Hz) and $\beta$ (~12-30 Hz) rhythms
- Power changes in different frequency bands depending on cognitive state:
    * $\alpha$ decreases during problem solving (e.g. mental arithmetic)
    * $\alpha$ increases during relaxed wakefulness 
    
# Physiological Prerequisites

## The physiological basis of the EEG

The (scalp) EEG reflects summed postsynaptic activity of pyramidal cells perpendicular to the surface of the scalp

- dipole moments between different cortical layers
- activity of cell assemblies rather than single cells

## Cortical vs. scalp potentials

\begin{columns}
\column{0.4\textwidth}
The surface activity is the sum of the underlying cortical activity. 
No net surface activity is apparent when the cortical sources cancel each other out. 

\column{0.7\textwidth}
\includegraphics[width=\textwidth,trim=0 24mm 0 0mm]{cortical_v_scalp.pdf}
\end{columns}

\vfill
\tiny\hfill adapted from Rösler (2005) 

## Coulomb's law: the distance between electrode and source

\begin{columns}
\column{0.4\textwidth}

\begin{itemize}
\item $\vec{F} = k_e\frac{q_1 q_2}{r^2}\hat{r} $ 
\item $ \Rightarrow \vec{E} = k_e \frac{q}{r^2} \hat{r}$ 

\item the distance between the  source of the current and the electrode determines scalp distribution
\item under certain circumstances, the potentials of distinct sources may merge at the surface
\end{itemize}

\column{0.7\textwidth}
\includegraphics[width=\textwidth]{coulomb.pdf}
\end{columns}

\vfill
\tiny\hfill adapted from Rösler (2005) 

## Gauss's law, equivalent dipoles and the inverse problem

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item $ \oiint_S \vec{E} \cdot d\vec{A} \Leftrightarrow \nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$
\item scalp-recorded EEG activity does not allow any conclusions as to its underlying sources
\item there are mathematical models to address the inverse problem, but all solutions remain approximations!
\end{itemize}

\column{0.6\textwidth}
\includegraphics[width=\textwidth]{forward.png} \\
\includegraphics[width=\textwidth]{inverse.png}
\end{columns}

\vfill
\tiny\hfill adapted from Rösler (2005) 

## From EEG to ERP

\includegraphics{eeg_to_erp.pdf}

Event-related potentials are summed postsynaptic *potentials* timelocked to cognitive or sensory stimuli (*events*).

\tiny\hfill Bornkessel-Schlesewsky \& Schlesewsky, \emph{Processing Syntax and Morphology: A Neurocognitive Perspective} (2009) 

## ERPs
- Small potential changes (between approx. 2--8 $\mu{}V$ for language) in comparison to the spontaneous electrical activity of the brain (approx. 10--100 $\mu{}V$)
- On account of this low signal-to-noise ratio, averaging over a relatively high number of trials (30--40 for language) is required for isolation of the stimulus-related response

# Electro-technical Aspects

## Voltage, reference and ground 
- voltage is by definition the difference in electrical potential (the magnitude of the E-field)  between two points
- electrodes record potential difference between two electrodes
	* the electrode you care about 
	* the reference electrode (called "CMS" for *common mode sensor* in some setups)
- \alert{there is no such thing as reference-free measurement of voltage!}
- "Reference-free" systems use mathematical trickery to avoid the issues inherent in the choice of reference
- the ground electrode provides an additional connection and reference to *ground*, which is considered zero in some sense
	*  the ground electrode also has other important functions related to electrical safety (both for the equipment and the participant)
	* the "zero" of ground is like zero on the Celsius scale when talking about water -- it has a useful meaning, but it is not zero in any truly absolute sense 


## The reference electrode {.allowframebreaks}
- The choice of reference electrode determines the resulting signal.
- Bipolar electrodes (often used for the eyes) are referenced to each other.
	- This effectively creates a single channel for both electrodes
	- Which makes for larger effects
	- But this destroys our ability to localize the effect to one electrode or the other.
	- This is Bad\texttrademark{} for things like independent-component analysis (ICA) and other methods that rely on topography for their interpretation.
- It is possible to calculate bipolar channels from unipolar recordings, but not the other way around.
- It is possible to calculate every common (in the sense of "shared between more than two electrodes") reference from every other.
- The average reference is calculated from a common reference by setting the average across all electrodes as the reference point.
- Choice of reference determined by practical concerns and traditions in the field.
- Common choice for language experiments:
	- left or right mastoid
	- referenced offline to the average of both mastoids to  avoid topographical distortions
	
## Why the choice of reference is important

\begin{columns}
\column{0.5\textwidth}
Average reference (30 electrodes)

\includegraphics[width=\textwidth]{lau_average_ref.pdf} 


\column{0.5\textwidth}
Linked mastoid reference

\includegraphics[width=\textwidth]{lau_mastoid_ref.pdf} 

\end{columns}

\vfill
\tiny\hfill Lau. et al. (2006). \emph{Brain and Language} 98, 74--88

# Acquisition and Analysis

## Raw EEG data
\centering
\includegraphics[width=\textwidth]{raw_eeg.pdf} 

## Steps in data analysis 
1. Preprocessing
	a. Rereferencing
	b. Raw data filtering 
	c. Artefact rejection or correction (automatic + manual)
	d. Epoching
2. Averaging (nowadays mostly for display purposes)
	a. single subject average (per electrode, condition and time window)
	b. grand average (average over single subject averages)
3. Statistical analysis

(DB will discuss this more after the break)

## Why filter?

\begin{columns}
\column{0.5\textwidth}

\includegraphics[width=\textwidth]{drift.png} 

\column{0.5\textwidth}

\includegraphics[width=\textwidth]{filtered.png} 

\end{columns}

## Filtering I

### High pass
- removes frequencies *lower* than a specified frequency
- good for removing signal drifts from raw data (see last slide)
- generally between 0.1 and 0.3 Hz (not higher!)
- must be applied to raw (not epoched) data!

### Low pass
- removes frequencies *higher* than a specified frequency
- good at removing electrical noise (such as mains hum and certain types of muscular activity)

## Filtering II

### Band pass
- combination of high and low pass filters, i.e. selects a frequency band

### Notch
- removes a specific frequency range from the data
- most common application: removal of 50 or 60 Hz (mains power frequency) 

## Best practice in filtering is massively controversial

\tiny

- Acunzo, D. J., MacKenzie, G., and van Rossum, M. C. W. (2012). Systematic biases in early ERP and ERF components as a result of high-pass filtering. Journal of Neuroscience Methods, 209(1):212–218.
- Maess, B., Schröger, E., and Widmann, A. (2016). High-pass filters and baseline correction in M/EEG analysis. commentary on: “how inappropriate high-pass filters can produce artefacts and incorrect conclusions in ERP studies of language and cognition”. Journal of Neuroscience Methods, pages –.
- Maess, B., Schröger, E., and Widmann, A. (2016). High-pass filters and baseline correction in M/EEG analysis–continued discussion. Journal of Neuroscience Methods, pages –.
- Rousselet, G. A. (2012). Does filtering preclude us from studying ERP time-courses? Frontiers in Psychology, 3(00131).
- Tanner, D., Morgan-Short, K., and Luck, S. J. (2015). How inappropriate high-pass filters can produce artifactual effects and incorrect conclusions in ERP studies of language and cognition. Psychophysiology, 52(8):997–1009.
- Tanner, D., Norton, J. J. S., Morgan-Short, K., and Luck, S. J. (in press). On high-pass filter artifacts (they’re real) and baseline correction (it’s a good idea) in erp/ermf analysis. Journal of Neuroscience Methods, pages –.
- Vanrullen, R. (2011). Four common conceptual fallacies in mapping the time course of recognition. Frontiers in Psychology, 2(00365).
- Widmann, A. and Schröger, E. (2012). Filter effects and filter artifacts in the analysis of electrophysiological data. Frontiers in Psychology, 3(00233).
- Widmann, A., Schröger, E., and Maess, B. (2015). Digital filter design for electro- physiological data – a practical approach. Journal of Neuroscience Methods, 250:34–46.

## Artefacts I: ECG
\centering
\includegraphics[width=0.85\textwidth]{artefact_ecg.pdf} 

## Artefacts II: Blinks
\centering
\includegraphics[width=0.85\textwidth]{artefact_blink.pdf} 

## Artefacts III: Saccades
\centering
\includegraphics[width=0.85\textwidth]{artefact_saccade.png} 


## Averaging I 

### Compute single-subject average
- per electrode
- per condition
- per time point / window in the epoch)

### Options:
- absolute (relative to reference) values 
- relative to a baseline (e.g. -200-0 ms "pre-stimulus" or 0-100 within stimulus)

## Averaging II

### Rejections 
- exclude trials that contain artefacts 
- (optional) exclude trials for which the control task was not performed correctly)

### Result
- Reduction of noise and background activity
- increase in signal-to-noise ratio (SNR)

### Compute grand average
- average over single-subject averages

## Single-subject average
\centering
\includegraphics[width=0.7\textwidth]{sisuavr_onecond.png}

## Grand average
\centering
\includegraphics[width=0.7\textwidth]{grandavr_onecond.png}

## Statistical analysis 
- Many aspects to examine, e.g.
	- latency of component peak
	- amplitude of component peak
	- mean amplitude in a given time-window
	- etc. etc. 
- Traditionally with factorial repeated-measures ANOVA:
	- group of electrodes divided up into "regions of interest" (ROIs) on the scalp
	- ANOVA over condition factors * topographical factors
- Nowadays:
	- with mixed-effects models (coming soon to a Melbourne near you!)
	- or MVPA (coming even sooner to an Adelaide near you!)
	
# Components and effects

## The ``finished product''
\begin{columns}
\column{0.5\textwidth}
An ERP \emph{component} can be described in terms of

\begin{description}
\item[latency] time to component onset/peak after critical stimulus onset 
\item[polarity] negative or positive deflection relative to control
\item[topography] electrode positions (ROIs) at which the wave/deflection is observable
\item[amplitude] the strength of the electric field
\end{description}

\column{0.6\textwidth}
\includegraphics[width=\textwidth]{KF_tulip.png}

\end{columns}


## Everything is relative

\begin{columns}
\column{0.5\textwidth}
\includegraphics[width=0.6\textwidth]{neg01.png}

\column{0.5\textwidth}
\includegraphics[width=0.6\textwidth]{neg02.png}

\end{columns}

\begin{itemize}
\item ERP \emph{effects} are relative measures between a critical condition and a control condition
\item Absolute potential shifts cannot (yet) be interpreted!
\end{itemize}

## Components vs. Effects

\begin{columns}
\column{0.5\textwidth}
An ERP \emph{component} can be described in terms of

\begin{itemize}
\item An ERP \emph{component} is typically associated with a functional interpretation
\item Components may also appear in control conditions (e.g. N400 for every word)
\item Differences between two instances of the same component (and more generally between two conditions): ERP \emph{effects}
\end{itemize}

\column{0.6\textwidth}
\includegraphics[width=\textwidth]{KF_tulip.png}

\end{columns}
