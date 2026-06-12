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


# ==============================================================
# DETAILED PARAGRAPH-LEVEL PLAN (each bullet = one paragraph)
# Target ~5000 words ≈ ~25 paragraphs @ ~200 words
# Sub-bullets = key points / citations to fold into that paragraph
# ==============================================================

## 1.0 Opening preamble (paragraphs BEFORE Section 1.1)
[Inspired by the broad-to-narrow funnel that opens thesis_example.pdf, adapted to this thesis's ML / assembly-history focus]


- **P3 — The foundational question and the Milky Way as a test-bed.** "How did the Milky Way form and assemble its mass?" is the defining question of Galactic Archaeology.
    - Star-by-star access lets us fully characterise structure and history from fossil records imprinted in stars.
    - Under the assumption the MW is a typical L*/spiral galaxy, insights generalise to galaxy formation at large and test ΛCDM itself. Hedge the "typical" claim: the MW appears atypically merger-quiet for its mass (Hammer 2007), so it is a uniquely accessible benchmark but not necessarily representative — state this caveat explicitly.

- **P4 — The central tension this thesis addresses.** A data revolution has outpaced the methods used to interpret it.
    - Gaia + large spectroscopic surveys delivered single-star chemo-dynamics for ~10^9 stars, yet the analysis still leans on techniques/intuitions developed at the start of the century.
    - The two-step standard workflow (separate accreted vs in-situ stars → cluster accreted debris into progenitors) carries simplifying assumptions that modern data and simulations can now move beyond.

- **P5 — The approach taken in this thesis.** State the thesis's contribution at a high level.
    - Use cosmological hydrodynamical zoom-in simulations of MW-mass halos (ARTEMIS, Auriga), where the origin of every star is known, to develop and validate data-driven / machine-learning methodologies, then apply them to MW data.
    - Frame the four-step arc: classify → cluster → characterise progenitors → apply to the Galaxy.

- **P6 — Roadmap of the introduction chapter.** Brief signpost paragraph.
    - 1.1 theory background (galaxy formation in ΛCDM, the stellar halo, archaeology tools); 1.2 the MW assembly history; 1.3 cosmological simulations; 1.4 ML for Galactic Archaeology; 1.5 thesis outline.

## 1.1 Theory background: galaxy formation in ΛCDM  (~6 paragraphs, ~1200 w)

- **P1 — Hierarchical structure formation in ΛCDM and its evidence.** Set the cosmological frame: large galaxies like the MW grow "bottom-up" by progressive merging of smaller structures.
    - Distinguish what each reference establishes: early evidence against monolithic collapse / for fragment accretion of the halo (Searle & Zinn 1978); cooling + galaxy formation inside dark halos (White & Rees 1978); the full hierarchical CDM semi-analytic framework (White & Frenk 1991). Don't lump them as one undifferentiated "bottom-up" cite.
    - The number/properties of mergers depend on the underlying cosmology → reconstructing assembly histories is a quantitative cosmological constraint (Bullock & Boylan-Kolchin 2017).
    - Mention the diversity of accretion histories predicted across MW-mass halos.

- **P2 — Formation of the stellar halo as a "fossil record".** A natural consequence of hierarchical assembly is a diffuse, extended stellar halo built from tidally stripped satellites.
    - Stellar populations retain memory of the environment in which they formed (Eggen, Lynden-Bell & Sandage 1962; Searle & Zinn 1978).
    - The halo as a bridge between a galaxy's past and present; long phase-mixing timescales preserve information (Helmi 2020 review; Deason & Belokurov 2024 review).

- **P3 — The multi-dimensional parameter space where signatures are imprinted.** Accretion signatures live in positions + kinematics + chemical abundances.
    - From this space one reconstructs the assembly history: timing, progenitor masses, SFHs, orbital properties (Freeman & Bland-Hawthorn 2002).
    - Collisionless dynamics → the distribution function is conserved along orbits in phase space (collisionless Boltzmann / Vlasov equation; Binney & Tremaine 2008); equivalently, phase-space density is incompressible (Liouville's theorem for Hamiltonian systems). This motivates the integrals-of-motion approach: stars from a common progenitor cluster in spaces defined by (quasi-)conserved quantities.

- **P4 — The dual nature of the stellar halo and the in-situ problem.** Halo is not purely accreted: it has an in-situ component too.
    - Observational evidence for "dual halo" (Carollo 2007, 2010; Beers 2012): in-situ more centrally concentrated, prograde, more metal-rich; accreted more randomly distributed, metal-poor.
    - In-situ halo formation channels (keep distinct, cite separately): (i) disc stars dynamically heated by major mergers — the "Splash" (Belokurov 2020); (ii) stars formed in-situ from accreted/cooling gas (Zolotov 2009; Cooper 2015); (iii) stars formed in cold filaments or wakes of stripped satellite gas (Font 2011; Brook 2004). Do NOT attribute Belokurov 2020 to (ii)/(iii). [PHYS-CHECK: "Brook 2004" for channel (iii) is drawn from general knowledge and not cited explicitly in any of the four papers — verify the intended reference before committing to it; Font 2011 (font_cosmological_2011) is confirmed in Ch. 2.]
    - Why this is a problem: assumption that halo = accreted only holds in the far outer halo (≳20 kpc); contamination biases substructure searches.

- **P5 — Components of the stellar halo: streams vs phase-mixed debris.** Two morphological regimes set by phase-mixing.
    - Recent / cold streams remain spatially coherent (Sagittarius-like; special geometries — Johnston 1996; Bullock & Johnston 2005).
    - Over many dynamical times debris phase-mixes (stream dispersal and geometry: Tremaine 1999; broader collisionless dynamics framework: Binney & Tremaine 2008) and becomes indistinguishable from the field in position–velocity space — but information survives in (quasi-)conserved integrals of motion.
    - Caveat to state here: integrals of motion are strictly conserved only in a static, spherically symmetric potential; the real MW potential is non-spherical and time-evolving, so E and L_z are only quasi-conserved (and L_perp not strictly conserved).
    - Foreshadow the morphological classification used later (intact / stream / phase-mixed; Riley 2025, Shipp 2025).

- **P6 — Tools of Galactic Archaeology to recover information from phase-mixed stars.** Introduce the three pillars used throughout the thesis.
    - *Chemical tagging*: independent chemical evolution of each satellite imprints a "fingerprint"; stars sharing a birth site share abundances (Freeman & Bland-Hawthorn 2002).
    - *Integrals of motion*: E, L_z, L_perp (quasi-)conserved → debris appears as clumps in IoM space (Helmi & White 1999; Helmi 2000); caveat that L_perp not strictly conserved and potential evolves (Gómez 2010, 2013).
    - *Stellar ages*: trace SFH / chemical-enrichment rate; from asteroseismology, isochrone & CMD fitting (Gallart 2019, 2024; Montalbán 2021). Be precise: [α/Fe] is not a direct age indicator — it traces the SF timescale of the birth environment (short burst → high [α/Fe]; extended SF → lower [α/Fe]) via the relative SNII/SNIa enrichment rate (SNII timescale ~few Myr; SNIa timescale ~Gyr; McWilliam 1997); it correlates with age only statistically.

## 1.2 The Milky Way assembly history  (~6 paragraphs, ~1200 w)

- **P1 — Why the Milky Way?** It is the only galaxy with large samples of accurate single-star 6D phase-space + chemical-abundance measurements.
    - Contrast with external galaxies (only integrated/photometric halo properties, e.g. GHOSTS — Monachesi 2016).
    - This unique data volume is what makes detailed, star-by-star archaeology possible — and what motivates simulation-informed methods.

- **P2 — Sagittarius: the first direct evidence of ongoing hierarchical accretion.** The Sgr stream as the archetypal recent merger.
    - Ibata, Gilmore & Irwin 1994; spatially coherent tidal tails wrapping the Galaxy.
    - Established that the MW is still cannibalising satellites today.

- **P3 — The Helmi streams: first inference of accretion from phase-mixed debris.** Demonstrated the IoM method on real data.
    - Helmi et al. 1999 — substructure in velocity space of solar-neighbourhood stars; first phase-mixed accretion event identified.
    - Proof of concept that ancient, spatially mixed mergers can still be recovered.

- **P4 — The Gaia revolution (I): discovery of Gaia–Enceladus–Sausage.** DR2 transforms the field.
    - Gaia DR1/DR2 (2016, 2018): astrometry + photometry for ~10^9 stars.
    - GES: large population of radial, eccentric-orbit stars; the last *significant* merger (NOT "last major merger" — Sgr is an ongoing minor merger), accreted ~8–10 Gyr ago (Belokurov 2018; Helmi 2018). Harmonise the lookback time across the thesis (Ch. 2 says ~8–9 Gyr, Ch. 4 says ~10 Gyr → use 8–10 Gyr; cf. GalactiKit 9.5⁺⁰·⁸₋₁·₄ Gyr).
    - Earlier hints — distinguish nature: observational identification of the retrograde metal-poor component (Chiba & Beers 2000) vs. simulation/re-simulation predictions of a past major merger (Brook 2003; Meza 2005).
    - Dynamical/chemical impact: (a) disc heating — in-situ disc stars scattered onto halo-like orbits, the "Splash" (Belokurov 2020; Mackereth 2019); (b) gas brought in by GES triggering a burst of in-situ star formation (Bignone 2019; Grand 2020; Ciucă 2024); (c) subsequent gas depletion / quenching possibly linked to the thick→thin disc transition. Hedge: the thick disc likely predates GES and was not created by it — GES heated an already-existing thick disc population (Haywood 2013; Di Matteo 2019); the quenching/transition attribution (c) is more speculative and should be flagged as such. [PHYS-CHECK: Bignone 2019, Grand 2020 (Grand_GES_2020), and Ciucă 2024 (Ciuca_GES_2024) are all confirmed in Ch. 4 for the burst-of-SF claim; ensure "Grand 2020" refers to Grand_GES_2020 specifically and not the Auriga paper (Grand_auriga_2017/2024).]

- **P5 — The Gaia revolution (II): the "gold rush" of substructures.** Gaia + spectroscopy → proliferation of claimed progenitors.
    - Spectroscopic complements: APOGEE, GALAH, LAMOST, H3, Gaia-ESO.
    - Catalogue of *accreted* substructures: Sequoia (Myeong 2019), Thamnos (Koppelman 2019b), LMS-1/Wukong (Yuan 2020), Helmi streams, Arjuna/I'itoi (Naidu 2020), Heracles (Horta 2021) — possibly the same very early merger as the GC-inferred "Kraken" (Kruijssen 2019, 2020), but the equivalence is debated, so present them as "Heracles/Kraken — possibly the same object" rather than equating them; Shakti/Shiva (Malhan 2024).
    - Extension inward to the proto-Galaxy. NOTE: Aurora (Belokurov & Kravtsov 2022) is the *in-situ* pre-disc proto-Galactic population, NOT an accreted substructure — discuss it as the in-situ proto-Galaxy (it belongs conceptually with §1.1-P4), not in the accreted-progenitor list above.

- **P6 — Growing complexity and open problems.** The census is increasingly hard to interpret — motivates the thesis.
    - Debris from one progenitor spans large regions of chemo-dynamical space (Jean-Baptiste 2017; Mori 2024); some retrograde systems chemically indistinguishable from GES (Horta 2023).
    - Clustering can return spurious / contaminated substructures if not optimised (Thomas 2025; Sante 2025).
    - Traditional progenitor characterisation (CMD/age fitting, density-profile fitting, chemical-evolution-model fitting) is single-structure and decoupled from the cosmological context.
    - "Although data quality improved dramatically, analysis still rests on early-2000s techniques/intuitions" → the gap this thesis addresses.

## 1.3 Cosmological simulations  (~2 paragraphs + 2 sub-sections, ~900 w)

- **P1 — Simulations as a theoretical model and an inference tool.** Why hydrodynamical zoom-ins of MW-mass halos are needed.
    - They forward-model the coupled processes (cosmological assembly, chemical evolution of host+satellites, phase-mixing in an evolving potential) that no analytic model captures.
    - Dual haloes arise naturally (Zolotov 2009; McCarthy 2012; Tissera 2013; Cooper 2015; Pillepich 2015, 2018).
    - They reproduce observed scaling relations (M*–Mhalo, mass–metallicity, halo surface-brightness/metallicity profiles) → realistic enough for direct comparison with the MW (Monachesi 2019).

- **P2 — Two roles in this thesis: ground truth + training data.** Frame how simulations are used.
    - In simulations the accreted/in-situ origin and the progenitor of every star particle is known → an objective "ground truth" to train/test methods (impossible with observations).
    - Caveat / limitation: subgrid-physics choices affect in-situ halo properties and chemical yields → systematic offsets vs the MW (motivates the calibration model in Ch. 5).

### 1.3.1 The ARTEMIS simulations  (1 paragraph)
- **P — Describe ARTEMIS (used in Ch. 2).**
    - 45 MW-mass zoom-ins, GADGET-3 + EAGLE subgrid physics, WMAP9 cosmology (Font 2020, 2021).
    - Mass range 8×10^11–2×10^12 M_sun; resolution: DM particle mass ~1.17×10^5 M_sun/h, initial gas particle mass ~2.23×10^4 M_sun/h, force resolution 125 pc/h; 11-species chemical enrichment from AGB stars, stellar winds, SNII and SNIa — the thesis-relevant tracers are Fe (produced *mainly* in SNIa) and Mg (an α-element produced in SNII).
    - Accreted/in-situ labels in post-processing; optical photometry available (PARSEC isochrones, Chabrier IMF).
    - Disc-like subsample selected via co-rotation parameter κ_co.

### 1.3.2 The Auriga simulations  (1 paragraph)
- **P — Describe Auriga (used in Ch. 3, 4, 5).**
    - 39 MHD zoom-ins with AREPO moving-mesh; haloes drawn from EAGLE DM-only L100N1504; Planck Collaboration XVI (2014) [= Planck 2013] cosmology (Grand 2017, 2024).
    - "Level 4" resolution (typical particle masses ~3×10^5 M_sun DM, ~5×10^4 M_sun baryons); rotation-supported discs; reproduce MW-analogue scaling relations and GHOSTS halo properties (Monachesi 2019). [PHYS-CHECK: Ch. 3 quotes ~4×10^5 M_sun for DM particles; Ch. 4 quotes ~3×10^5 M_sun. Pick one value and make it consistent across the thesis — Ch. 4 is the dedicated GalactiKit paper so its value (~3×10^5) may be preferred, but verify against Grand 2017 Table 1.]
    - Merger trees (SUBFIND + LHaloTree); accreted-particle lists with RootIndex / PeakMassIndex; PeakMassIndex defines progenitors. Peak stellar mass is reached typically at or just after first crossing of R_200, when tidal/ram-pressure stripping quenches star formation (Kawata 2008; Simpson 2018; Font 2022) — so it is a close proxy for, but not exactly, the infall time.
    - Public data release enables the merger–debris pairing used in GalactiKit.

## 1.4 Machine learning for Galactic Archaeology  (~5 paragraphs, ~1000 w)

- **P1 — Why ML now?** Two enabling factors.
    - The data deluge: Gaia + large spectroscopic surveys provide the volume ML needs.
    - Maturation of open ML software infrastructure (TensorFlow, scikit-learn, xgboost, sbi/LtU-ILI) and hardware.
    - ML excels exactly where the two halo populations overlap and no analytic boundary exists.

- **P2 — ML application 1: finding stellar streams.** Pattern-finding in high-D space.
    - STREAMFINDER (Malhan & Ibata 2018) — does *not* require knowledge of the gravitational potential (unlike most stream-finding methods that do); Via Machinae (Shih 2022) — conditional density estimation / sideband interpolation for local overdensities; match-filter methods (Grillmair & Rockosi; Balbinot 2011) and gradient-boosted-tree halo finders (Veljanoski 2019).

- **P3 — ML application 2: classifying accreted vs in-situ stars.** The first methodological step (→ Ch. 2).
    - Ostdiek 2020 (ANN on FIRE mock Gaia DR2 kinematics → discovery of Nyx, Necib 2020); Tronrud 2022 (GANN on Auriga chemistry+ages); Trujillo-Gomez 2023 (accreted vs in-situ globular clusters in E-MOSAICS).
    - Limitation these share: trained on specific assembly histories → domain shift.

- **P4 — ML application 3: finding accreted substructures with clustering.** Grouping debris by progenitor (→ Ch. 3).
    - Density-based (DBSCAN, HDBSCAN) and single-linkage methods on IoM/chemistry (Koppelman 2019; Borsato 2020; Lövdal 2022; Ruiz-Lara 2022; Dodd 2023).
    - Also mention self-organising maps and other unsupervised embeddings (cite an actual application, e.g. Carrillo 2024 — or drop if the thesis doesn't engage with SOMs, to avoid padding).
    - Known failure modes: sensitivity to internal parameters, fragmentation/over-merging, spurious in-situ-dominated clusters (Thomas 2025; Kim 2025). Rely on assumption that halo is fully made of accreted stars.

- **P5 — ML application 4: reconstructing progenitor properties with SBI.** Characterising the systems (→ Ch. 4, 5).
    - SBI/likelihood-free inference (Cranmer 2020) — Bayesian inference for models with intractable likelihoods; normalizing flows / MAFs (Papamakarios 2017). In MAF, complex posterior distributions are approximated as a sequence of parameterised invertible transformations (flows) applied to a Gaussian base distribution; training minimises the negative log-likelihood of the joint simulation-data distribution.
    - Astrophysics precedents: cosmology from clusters/weak lensing (Hahn 2023; Jeffrey 2021), SED fitting (Hahn 2022), gravitational waves (Green 2020).
    - Closest related: Kruijssen 2020 (ANN regression, E-MOSAICS GCs → orbital parameters, no probabilistic degeneracies); CASBI (Viterbo 2024, oxygen + iron abundances only, NIHAO); Widmark 2025 (perturbed-dwarf orbits). Gap → a self-consistent, simulation-grounded SBI of merger properties from field-star debris.

## 1.5 Thesis outline  (~6 paragraphs, ~800 w)

- **P1 — Aim of the thesis.** One framing paragraph.
    - Extend the corpus of modern, data-driven ML techniques for reconstructing the MW assembly history, replacing early-2000s heuristics; develop and validate each step (classify → cluster → characterise → apply) on cosmological simulations with known ground truth, then apply to MW data.

- **P2 — Chapter 2.** Accreted vs in-situ classification (ARTEMIS).
    - Assumption-free ML classifier informed by chemo-dynamical patterns; broad comparison of ANNs, decision trees (XGBoost), TML, UMAP visualisation; optimal observable feature set (kin+chem+phot); galaxy-specific features to combat domain shift; outperforms observational selection cuts → smaller, purer accreted sample; feature-importance guidance for future surveys.

- **P3 — Chapter 3.** Optimised HDBSCAN clustering (Auriga).
    - Data-driven tuning of HDBSCAN via Optuna against an external (V-measure) and an internal (DBCV) metric; 12-D chemo-dynamical feature space; clusters dominated by single progenitors (vs traditional in-situ-dominated clusters); first explicit quantification of how in-situ contamination degrades sensitivity (mergers recoverable to z≈3 in accreted-only vs only z<1 when contaminated).

- **P4 — Chapter 4.** GalactiKit: SBI reconstruction of progenitor properties (Auriga).
    - MAF-based SBI mapping z=0 debris (E, L, [Fe/H], [α/Fe]) → infall time, stellar mass, halo mass, MMR; leave-one-out cross-validation; first model to self-consistently predict infall times and masses consistent with known relations: the mass–metallicity relation (Kirby 2013 as the dwarf-galaxy empirical benchmark covering 10^3.5–10^12 M_sun; Harmsen 2017 cited in Ch. 4 in the context of the stellar-halo MZR — [PHYS-CHECK: verify whether Harmsen 2017 is used as the primary MZR reference in Ch. 4/5 or only as a secondary check; Kirby 2013 is the main empirical anchor in Ch. 5]) and the infall-time–binding-energy relation (Rocha 2012, established for *surviving satellites*; García-Bethencourt 2023 — Ch. 4 extends it to phase-mixed debris). Applicable to the smallest substructures lacking a GC population.

- **P5 — Chapter 5.** Applying GalactiKit to the Milky Way (Auriga + Gaia/APOGEE).
    - Calibration (noise) model marginalising sim–obs discrepancies; Fishnets (Makinen 2023) information-optimal aggregation that compresses the per-star score vector and Fisher information matrix into a fixed-size summary statistic before posterior estimation; most complete self-consistent inference of MW progenitors' infall times & masses to date; rapid stellar-halo assembly dominated by GES. State the mass comparison carefully (don't just say "consistent"): total accreted stellar mass *excluding* Sgr (1.4⁺¹·¹₋₀·₄ ×10⁹ M_sun) agrees with halo-mass measurements (Deason 2019: 1.4±0.4 ×10⁹ M_sun; Mackereth 2020: 1.3⁺⁰·³₋₀·₂ ×10⁹ M_sun), while the *full* estimate including Sgr (2.2⁺¹·¹₋₀·₆ ×10⁹ M_sun) exceeds them — note that Mackereth 2020 explicitly excludes Sagittarius, so the without-Sgr comparison is the physically appropriate one for that reference; plus reconstruction of MW dark-matter halo-mass growth.

- **P6 — Closing / roadmap paragraph.** Optional.
    - Brief note on the logical thread (each chapter feeds the next), the appendices, and the broader outlook for upcoming surveys (4MOST, WEAVE, Gaia DR4, Rubin/LSST).



