# Introduction: writing plan

## Thesis overview

Galaxies experience a hierarchical formation process accreting dark and baryonic matter from smaller satellite systems over time. The expected number and properties of these merger events vary depending on the underlying cosmology, thus making a quantitative reconstruction of the assembly history of observed galaxies an important theoretical constraint \cite{Bullock_2017}. As a result of the tidal disruption of luminous satellites, stellar material is deposited in the outer regions of a galaxy forming an extended component (i.e. the stellar halo) which preserves information on its turbulent past \cite{helmi_review}. In the last ten years, the large amount of data from astrometric and spectroscopic surveys \cite{H3,gaia, sdss} allowed detailed studies of the dynamics and chemistry of the stellar halo of the Milky Way delineating the current picture of the assembly history of our Galaxy \cite{Deason_2024, helmi_review}. \textbf{Although the quality of data has improved significantly, its analysis is still based on techniques and intuitions developed at the beginning of the century}. The standard procedures adopted in Galactic Archaeology studies include: i) the definition of a sample of \textit{accreted} stars, which are separated from the ones that formed \textit{in-situ}, i.e. within the Milky Way; ii) the identification of accreted substructures through the application of clustering techniques,  under the assumption that stars that formed in a similar environment have similar chemo-dynamical properties \cite{helmi_review}. 

During my PhD I have used cosmological hydrodynamical zoom-in simulations of Milky Way-mass halos to develop data-driven methodologies which significantly improves over those traditionally adopted for the reconstruction of the assembly history of our Galaxy. 

1. (Chapter 2) Distinguishing between accreted and in-situ stars is a particularly challenging problem because there is no analytical distinction between the two populations, and accreted stars comprise a small fraction of the overall stellar content of a galaxy. Traditionally, the selection is performed through population-level selection cuts under the simplified assumption that accreted stars are uniquely found in the stellar halo \cite{Koppelman_2019}. However, the presence of the in-situ population in the stellar halo is a generic feature of the hierarchical formation of galaxies as disc stars are dynamically heated by major merger events or new stars are formed ``in-situ'' from the accreted gas \cite{Zolotov2009}. Using machine learning techniques, \textbf{I developed an assumption-free classification method informed by the chemo-dynamical patterns of the accreted and in-situ populations} from the ARTEMIS cosmological simulations \cite{artemis}.  In Figure~\ref{fig:proj1}, the distribution of accreted and in-situ stars in Solar neighborhood-like regions of four simulated galaxies (leftmost column) is compared to the one retrieved using observational criteria (columns 2-4, taken from \cite{Helmi_2008}, \cite{sequoia}, and \cite{massari}, respectively) and the one inferred using the machine learning model (rightmost column). The predicted overall fraction of accreted stars is also reported in each plot. As can be noticed visually, the developed machine learning approach best captures the complex distinction between accreted and in-situ stars, while also returning, on average, a smaller and purer accreted sample. Moreover, I evaluated the relative importance of several observable stellar properties in the classification, which is important to inform future surveys and theoretical studies of the accretion history of the Galaxy. 

2. (Chapter 3) Once the accreted stars are isolated from the in-situ background, the identification of the disrupted progenitors of the Milky Way is performed applying clustering algorithms on the energy, angular momentum, and chemical abundance ratios of the stars \cite{Koppelman_2019}. However, recent studies have shown that debris from a single progenitor can occupy extended regions of the chemo-dynamical space \cite{Mori2024}, which out-of-the-box clustering algorithms fail to identify \cite{Thomas2025}.  By selecting three galaxies with different assembly histories from the Auriga cosmological simulations \cite{auriga}, I developed a data-driven technique to optimize clustering algorithms. The methodology involves tuning the internal parameter of the clustering model to optimize a given target metric. I repeated this process both with a metric (V-measure) which directly compares the cluster with the progenitors in the simulations, and another (DBCV) which only measures the relative density of the clusters. As shown in Figure~\ref{fig:MW_merger_tree}, the clustering model obtained from both metrics can reconstruct the majority of the merger events of the simulated galaxies at a similar level of detail. Hence, intrinsic metrics can be used to optimally configure the internal parameters of clustering algorithms before their application to observations. Moreover, \textbf{the clusters obtained with this new methodology are mostly comprised by stars from a single progenitor, contrary to traditional clustering models, which return clusters dominated by in-situ stars.} \cite{hdbscan}.  
Furthermore, I have explicitly quantified for the first time the impact of in-situ stars in the identification of accreted substructures showing that their presence reduces the sensitivity of clustering approaches from mergers that happened at $z\approx3$, when applied to a sample exclusively composed of accreted stars, to events occurring at $z<1$ when in-situ stars contaminate the clustering sample.


3. Chapter (4) Once the accreted stars are grouped based on the galaxy where they formed, their properties can be used to chracterise the system inferring when and how the merger happened. Therefore, alongside working on the identification of the disrupted progenitors of the Milky Way, I have also developed a new methodology for the reconstruction of their properties at accretion. Because the $z=0$ chemo-dynamical distribution of merger debris is a ``fossil'' record of the accreted systems of origin \cite{helmi_review}, there is an unknown link between the properties of the debris and those of the progenitor galaxies. An analytical formulation of such a relationship is complex as it would need to account for several codependent processes such as the chemical evolution of the satellite galaxies, their assembly history in a cosmological context, and the phase-space mixing of the debris after accretion. However, current cosmological simulations of Milky Way-like galaxies  implement most of the relevant galaxy formation processes at a level of detail which allows for a direct comparison with observations \cite{monachesi_2019}. Thus, I developed GalactiKit \cite{proj2}, a simulation-based inference \cite[SBI,][]{Cranmer_sbi_review_2020} model to extract the information relating the merger events in the Auriga simulations to the $z=0$ chemo-dynamical properties of their debris.  This is \textbf{the first model that can self-consistently predict the infall times and masses of disrupted dwarf galaxies in agreement with known physical relations} such as the mass-metallicity relation \cite{Harmsen_massmetallicity_2017} and the relation between the infall time-binding energy of subhalos \cite{Rocha_2012}. As GalactiKit is informed by the properties of field stars, it can be used to infer the properties of the smallest accreted substructures in the Milky Way, which are not associated to a globular clusters population. 

4. (Chapter 5) More recently, I have worked on applying GalactiKit to characterize the accreted substructures in the stellar halo of the Milky Way \cite{horta_2023} combining data from the Gaia \cite{gaia} and SDSS-IV \cite{sdss} surveys. To account for differences between the simulations and observations, I explicitly modeled two main sources of discrepancies: i) the differences between the physics implemented in the Auriga subgrid models and the one governing the chemical evolution and star formation in the Milky Way; ii) errors in measured stellar properties. By creating a new, more robust training dataset that marginalizes over these uncertainties, \textbf{I have computed the most complete inference of the Milky Way's formation to date}.  As shown in Figure~\ref{fig:MW_merger_tree}, which compares the reconstructed accreted stellar mass of the Milky Way with estimates of the total mass of the stellar halo at present-day \cite{Deason_2019, Mackereth_2020}, the Galaxy experienced a rapid assembly of the stellar halo, with the Gaia-Enceladus-Sausage merger as the largest contributor. This new, robust reconstruction is important because it does not only validate the properties of currently identified accreted substructures, but also hints towards the potential presence of undiscovered mergers whose contribution would still be consistent with the total stellar halo mass. 

##  Introduction outline

1.1 Theory background: Galaxy formation in LCDM

- hierarchical structure formation and evidence
- the formation of the stellar halo and its role as a trove of the fossils of a galaxy's formation history
- the dual nature of the halo and the problem of in-situ stars. 
- components of the stellar halo: streams and phase-mixed substructures
- tools for galactic archaeology and retrive info from phase-mixed stars: 
    - chemical tagging
    - integrals of motion
    - stellar ages

1.2. The Milky Way assembly history

- Why do we focus on the Milky Way? Because it's the only system where we have access to a large number of accurate single-star observations of chemical abundancies and velocities.
- Sagittarius stream, the first direct evidence of the hierarchical formation history of the milky way
- the Helmi streams, the first inference of an accretion event from phase-mixed debris
- the Gaia revolution. 
    - The discovery of Gaia Enceladus Sausage
    - The "gold-rush" for the discovery of streams and accreted substtructures

1.3. Cosmological Simulations

- a theoretical model for galaxy formation and a different tool for inferring the formation history of the Milky Way in a cosmological context

1.3.1. The ARTEMIS simulations

1.3.2. The Auriga simulations

1.4. Application of machine learning techniques for Galacti Archaeology

- why now the application of machine learning techniques? The availability of more, accurate data and the popularisation of machine learning software infrastructure.

- main applications of machine learning techniques in Galacti Archaeology:

    - find stellar streams (streamfinder)
    - classify accreted and in-situ stars (Nyx and Tronrud paper)
    - finding accreted substructures using clustering techniques. Also mention self-organising maps
    - reconstructing the properties of these systems using simulation-based inference

1.5. Thesis outline

- aim of the thesis: extending the corpus of literature of modern machine learning techniques for the reconstruction of the formation history of our Galaxy.

- overview of the thesis and content of each chapter.



