# **The distribution of water and nitrogen in the soil-crop system: a simulation study with validation from a winter wheat field trial**

# **R.F.** Grant

*Department of Soil Science, University of Alberta, Edmonton, Alberta, Canada T6G 2E3* 

- *Key words:* Water uptake, nitrogen uptake, mass flow, diffusion, rooting distribution, crop growth, nitrogen partitioning
# **Abstract**

The realistic simulation of uptake processes for water and nitrogen, and of partitioning processes for nitrogen, are necessary to the accurate reproduction of water and nitrogen deficit effects on crop growth and yield. Mathematical descriptions of these processes, based on the findings of detailed studies, were used as part of a larger simulation model to calculate the extraction and uptake of water and nitrogen, and the distribution of nitrogen, by a winter wheat crop from a multi-layered soil profile over a growing season. Descriptions of water uptake processes allowed the model to reproduce the hourly dynamics of water uptake and redistribution through the root system, and to estimate the yearly dynamics of water depletion from the soil profile consistent with field data. Descriptions of nitrogen uptake processes allowed the model to reproduce the hourly dynamics of mass flow, diffusion and active uptake, but estimates of the yearly dynamics of mineral nitrogen depletion did not closely follow field data. This inconsistency arose largely from the partial disappearance of fertilizer nitrogen in the field plots shortly after application. This disappearance was not reproduced in the model. The model was able to reproduce the seasonal accumulation and redistribution of dry matter and nitrogen within the crop for fertilizer applications from 0 to 16 g m -2. These applications gave dry matter and nitrogen yields of phytomass from 1340 to 1600 and from 13.4 to 23.4 g m -a respectively, and of grain from 673 to 810 and from 11.5 to 20.4 g m -2 respectively. However, the model tended to overestimate both dry matter and nitrogen yields under high rates of fertilizer application. This simulation study demonstrates that results from more detailed studies of water and nitrogen uptake may be used to understand the annual dynamics of water and nitrogen distribution in the soil-crop system.

# **Introduction**

The accurate simulation of water and nutrient uptake by root systems is necessary in models used to study the use of irrigation and fertilizers in crop production. Mathematical equations for the uptake of water by root systems have been in use for many years [9]. These equations describe the movement of water along hydraulic potential gradients from the soil through the roots to the plant canopy as determined by hydraulic resistances in the soil and roots. However, these equations are not included in many models used

in the study of water deficit effects on crop growth. Some such models [25] use dimensionless factors to reduce uptake from dry soil while others [4, 10] normalize water uptake according to soil depth. In some crop models [22] water uptake is simulated as radial flow to single roots uniformly distributed through a soil layer, but it is not linked to dynamic estimates of transpiration rates based on canopy water potentials. These models cannot reproduce the entire hydraulic gradient by which extraction rates are determined. More detailed models of water uptake [43] represent the entire hydraulic gradient,

allowing dynamic estimates of crop water status under changing atmospheric conditions. Such models need to be incorporated into larger models of agroecosystem behavior if these latter models are to be based on more fundamental processes.

Mathematical equations for the uptake of nutrient ions by root systems have also been available for many years [2, 6, 7, 33]. These equations describe the movement of ions by mass flow and diffusion to root surfaces, and their absorption by active uptake processes at the root surfaces. The translocation, assimilation and storage of uptaken N has also been reviewed in detail [24]. However, in some models of crop growth [18, 22] uptake is simulated from empirical estimates for the supply and demand of inorganic N based on concentrations in the soil and crop, rather than from explicit representations of the component processes. If studies of nitrogen cycling at the ecosystem level of resolution are to be based on studies of nitrogen behavior at higher levels of spatial and biological resolution, then mathematical treatments of these processes need to be included in simulation models.

In this simulation study, the behavior of process-based equations for the movement and uptake of water and nitrogen are examined as part of an agroecosystem model. The objective of this study was (1) to determine whether the observed short-term behavior of root systems in the uptake of water and nitrogen could be reproduced by these equations, and (2) to determine whether the use of these equations in an agroecosystem model would allow the model to reproduce seasonal trends in the uptake of water and nitrogen, and in the yield of nitrogen and dry matter (DM) observed in a fertilizer experiment. An important part of this second objective was the reproduction of the dynamics of nitrogen and DM distribution within the growing crop.

### **Methods**

### *Simulation technique*

*Dynamics of soil C and N.* The dynamics of water and nitrogen uptake are simulated as part of a larger submodel for the movements and

transformations of carbon, nitrogen, and phosphorus in organic and inorganic phases in the soil and crop (Fig. 1). These dynamics are based on explicit finite different approximations to partial differential equations describing movement and transformations of C, N, P, O, water and heat through a horizontally layered soil profile on a fixed time step of 1 h. Subsequent discussion of the model will be limited to C and N.

In the soil organic phase, C and N undergo first order decomposition and mineralization from each of four subcomponents of crop residue [5], and three components of manure [11] into soluble C and NH 4 pools. These pools are the substrates for the formation of two pools of microbial biomass of differing activity, through either aerobic [29] or anaerobic [27] processes based on Michaelis-Menten kinetics. Microbial activity is fully coupled to the movement of O in gaseous and soluble forms through the soil profile. The microbial pools undergo first order decomposition [23], releasing some C into the soluble C pool for recycling to the microbial biomass [30] and some into humads, with associated mineralization and fixation of NH 4. Similarly, humads undergo first order hydrolysis [34], with partial solubilization and partial reformation of C and N as humus, again with associated mineralization and fixation of NH 4. Humus also undergoes first order hydrolysis and mineralization.

In the soil inorganic phase, soluble NH 4 may be adsorbed into exchangeable NH 4 [38], volatilized into gaseous NH 3 [8] and nitrified [28] into soluble NO3. When oxygen is deficient at the microbial microsites, soluble NO 3 is used as an alternative electron acceptor for microbial respiration, causing denitrification for which soluble C is the substrate.

Both soluble NH~- and soluble NO~ are fully coupled to submodels for water movement through the soil profile. The vertical movement of each N species i between adjacent layers *(Fv,N, i* in g m -2 h -1) is calculated as the sum of convective and diffusive fluxes:

$$F_{V,N,i} = F_{V,W}C_{N,i} + D_e \,\partial C_{N\varepsilon,i} / \partial z \tag{1}$$

where *Fv, W* = vertical water flux (m 3 m -2 h-l), *Cus,i* = concentration of N in soil water (g m 3), *D e* = effective dispersion-diffusion coefficient of

![](_page_2_Figure_0.jpeg)

*Fig. 1.* Flow diagram for nitrogen cycle in the agroecosystem simulation model, showing processes for nitrogen movement and uptake in the soil profile.

N ion (m 2 h-t), and z = soil depth (m). The flux *Fv, w* is calculated from vertical gradients of soil water potential (4',) and hydraulic conductivity between adjacent soil layers as described elsewhere [17]. The diffusive flux *D e OQv,,jOz* is calculated from vertical gradients of concen-

N flow ~-

tration and effective diffusivity between adjacent layers.

*Uptake of mineral N.* The distribution of root DM growth through a horizontally layered soil profile is calculated recursively from current uptake rates of water and N per unit root surface area in each layer. From this distribution, root length and surface area are calculated from an assumed root radius of 0.15.10-3m, a DM content of 0.075 g g-l, and an internal porosity of 0.10 m 3 m -3 [32]. The radial movement of N to crop roots within each horizontal soil layer *(FR,N, i* in g m -2 h -1) is calculated as the sum of convective and diffusive radial fluxes:

$$F_{R,N,l} = F_{R,W} \mathcal{C}_{Ns,l} + D_e \left\| \mathcal{C}_{Ns,l} / \partial r \right\| \tag{2}$$

where *FR, w* =transpiration flux (m 3 m -2 h-~), calculated from radial gradients of hydraulic potential and conductivity between the soil and cylindrical roots in each soil layer. This calculation involves an iterative convergence solution for the canopy water potential (Oc) at which *X FR, w* for all soil layers equals the canopy transpiration rate *(Fc,w).* The transpiration rate is calculated from hourly meteorological data and from canopy stomatal resistance (r~), itself an indirect function of ~. Within the convergence solution, a value for the root water potential (qJr) of each soil layer is calculated such that FR,v¢ from the soil to the roots, as controlled by the soil-root potential gradient ~,- *Or,* is equal to that from the roots to the canopy, as controlled by the root-canopy potential gradient Or-O~, for each layer. The equations used in the convergence solution are given elsewhere [15].

The diffusive flux *D~ OCNs,i/Or* in Eq. 2 is calculated from radial gradients of concentration and effective diffusivity between the soil and cylindrical roots:

$$\begin{aligned} \,^jD_\epsilon \, \left\| \,^jC_{Ns,i} / \right\| &= \\ &= \left\{ 2\pi D_\epsilon (C_{Ns,i} - C_{Nr,i}) / \ln(r_2/r_1) \right\} \, L_r \end{aligned} \tag{3}$$

where *CN~* = N concentration in the rhizosphere (g m-3), r 2 = mean half-distance between root axes (m) as calculated from root length density *(L d* in m m-3), with a maximum value equal to the mean distance for ion diffusion during each time step as calculated from *De,* and where r 1 = root radius and *L r* = root length per layer (ram 2).

Active uptake of N by crop roots *(UN, ~* in g m -2 h -1) is calculated according to Barber [3]:

$$U_{N,i} = \{U_{N,i \text{ min}} (C_{Nr,i} - C_{Nr,i \text{ min}})\} / $$

$$\{C_{KNr,i} + (C_{Nr,i} - C_{Nr,i \text{ min}})\} \tag{4}$$

where U~,i max = maximum uptake rate at saturating *CNr,i* (gm -2 h -1) calculated as the product of an experimental rate constant (gm --2 root area h -1) and the root surface area *(2vrrlL r*  in m z root area m -2 ground area), *CNr,i* min = minimum *CNr,i* for N uptake (g m -z) and *CKNr,i = (CNr,i -- CNr,i* min) at which *UN, i =*  1/2 *UN, i* max (g m-3) • An Arrhenius equation is used to describe the sensitivity of *UN, ~ max* to temperature [26]. Parameters for Eq. 4 were taken from the experimental data of Barber [3] for both NH2 and NO2.

In order to calculate N uptake, *FR,N, ~* from Eq. 2 is equilibrated with *UN, i* from Eq. 4 by iteratively solving for CNr,~ with a convergence criterion of 0.001. The movement and uptake of soluble P and O are calculated in the same way as those of NH~ and NO 3.

*Storage and assimilation of crop* N. N taken up as either NH 4 or NO~- is stored in an inorganic pool *(Np* in g m -2) from which N is withdrawn according to crop growth requirements calculated from the nitrogen : dry matter ratios *(RN, I)Mo* in g g-l) and the DM growth rates *(dDMo/dt* in g m -2 h 1) of each organ (o):

$$\mathbf{d}N_p/\mathbf{d}t = \sum_i U_{N,i} - \sum_o \left\{ \left( \mathbf{d} DM_o/\mathbf{d}t \right) R_{N, DMo} \right\} \tag{5}$$

If the nitrogen concentration in an inorganic pool *(CN, p* in g(N) g(DM)-I), calculated as *Np/*  {leaf DM + sheath DM + stalk structural DM + root DM}, exceeds a threshold value (set at 0.01 for crop plants), *UN, i* max in Eq. 4 is reduced [37].

The term *dDMo/dt* is calculated from the soluble carbohydrate pool of the crop (Cp in g m -2, stored in the leaves as the primary product of photosynthesis), calculated from leaf and canopy level algorithms [13, 16], and from the maintenance respiration rate *(R m* in g m -2 h-a), the dry matter:carbohydrate (CH20) ratio of organ synthesis *(RDM,CH~Oo* in g g-a) and phenology-dependent partitioning coefficients *(Po)* [14]:

$$\text{d}\,\text{D}\,\text{M}_o/\text{d}\,t = \left(d\text{C}_p/\text{d}t - \text{R}_m\right)P_o\,\text{R}_{DM,\text{CH}_2\text{O}o} \quad (6)$$

If *Np* is less than 2 *{(dDMo/dt ) RN,DMo}* from Eq. 5 (i.e. the N reserves present during a given hour are inadequate to meet N demands during the hour), then *dDMo/dt* is reduced to that enabled by *Np,* such that all Np is withdrawn during the hour:

$$\text{d}D\!M_o/\text{d}t = P_o N_p / \left\{ t \sum_o \left( P_o R_{N,DMo} \right) \right\} \tag{7}$$

where t = time step (1 h).

*Remobilization of crop N.* During the pre- and post-anthesis period, reserves of soluble CH20 and N are accumulated in the stalk for subsequent translocation to the grain, as determined by the balance between crop uptake and grain demand [21]. Under conditions of reduced uptake, or of rapid translocation of CH20 or N, these reserves may decline, under which conditions CH20 and N in the model may be transferred from *Cp* and *Np* to the reserves, such that *Ccp,* calculated as Cp/{leaf DM}, and *CNp* also decline. When *Ccp* declines below a threshold value, additional CH20 may be remobilized to Cp from leaf DM of the simulated crop, with accompanying remobilization of leaf N at current leaf *RN,DM o.* This remobilization is intended to allow the model to reproduce the accelerated leaf DM senescence observed under conditions of rapid translocation of CH20 to the grain [39], as may occur during water deficits. Similarly if *CNp* declines below a threshold value of 1.0.10-3g N g-1 DM [41], additional N may be remobilized to *Np* from leaf N. This remobilization is intended to allow the model to reproduce the accelerated loss of leaf N observed under low N fertilization [40]. Up to 67% of leaf N may be remobilized as simulated amino acids with accompanying remobilization of leaf DM at a *RN,DM o* of 16%, Remaining leaf N may be remobilized with leaf DM only at current leaf *RN,DM o* which is much lower, causing accelerated leaf DM senescence. Additional remobilization of leaf DM may occur if the CH20 production of a leaf is insufficient to meet its maintenance respiration requirement over a 24h period, as may occur in the lower canopy layers. Only 25% of leaf DM is recovered as CP during simulated remobilization of leaf DM, while the rest is lost to crop residue on the soil surface. Remobilization of DM and N occurs first in the lower leaves of the simulated canopy, and proceeds upwards. In the model, remobilization of N proceeds in advance of that of DM, as observed experimentally [21].

Leaf photosynthetic capacity is calculated as the product of RuBP carboxylase activity and superficial N density, assuming a constant relationship between RuBP carboxylase and total leaf N. Reductions in leaf *RN,DM o* arising from remobilization of leaf N cause reductions in superficial N density, such that CO 2 fixation [42] and hence Cp is reduced. In this way, a dynamic balance between Cp and *Np* arises within the simulated crop. Within each hourly time step, Eq. 6 is first calculated for root growth, and then for shoot growth, such that the latter is more sensitive to inadequate Np. Under these conditions, *Ccp* and Cp partitioned to the roots increase, such that root : shoot ratios shift in favour of the roots as observed experimentally [21].

# *Experimental technique*

Winter wheat (cv Arminda) was planted at Bouwing (51°57 ' N, 5°45 ' E) on 21 October, 1982 as part of an N fertilizer response study carried out at three sites over two years. Plant density after emergence was 200m -2. Soil characteristics at the site are presented in Table 1. Data for maximum and minimum temperature, global radiation, vapor pressure, windspeed and rainfall were recorded daily. Data for the distribution of carbon, nitrogen and water through the soil-crop system were collected in the field every two to three weeks from February through July 1983, for three fertilizer treatments (Table 2) ranging from 0.0 (N1) to 16.0 (N3) g N m 2. Experimental methods and results are presented by Groot and Verberne [20].

Recorded data for soil, weather and management were used in the model to reproduce the experimental conditions under which the field data were recorded. Because weather data were collected daily, hourly values used in the model were estimated [14]. Model runs were begun on 1 October 1982, and ended on 1 August 1983. A simulated manure application of 750 g DM m -2

| Layer                            | I    | 2    | 3    | 4    | 5    | 6    | 7    |
|----------------------------------|------|------|------|------|------|------|------|
| Depth to bottom (m)              | 0.10 | 0.20 | 0.30 | 0.40 | 0.60 | 0.80 | 1.00 |
| Sand (%)                         | 2.0  | 2.0  | 2.0  | 3.5  | 4.0  | 4.5  | 4.5  |
| Silt (%)                         | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 |
| Clay (%)                         | 35.0 | 35.0 | 35.0 | 35.0 | 35.0 | 35.0 | 35.0 |
| Organic Matter (%)               | 2.8  | 2.8  | 2.8  | 1.4  | 1.4  | 0.7  | 0.0  |
| Saturated conductivity (mm h -z) | 0.28 | 0.28 | 0.28 | 0.28 | 0.10 | 0.10 | 0.10 |
| VWC at 0.03 MPa (m 3 m 3)        | 0.38 | 0.38 | 0.38 | 0.38 | 0.40 | 0.40 | 0.40 |
| VWC at 1.5 MPa (m 3 m -3)        | 0.17 | 0.17 | 0.17 | 0.17 | 0.18 | 0.18 | 0.18 |
| Bulk Density (Mg m -3)           | 1.35 | 1.35 | 1.35 | 1.40 | 1.40 | 1.35 | 1.35 |

*Table 1.* Physical and chemical characteristics of the clay at Bouwing

*Table 2.* Fertilizer treatments (g m -2) at Bouwing. N1 = lowest level, N2 = intermediate level, and N3 = highest level

|           | Date (ddmmyy) |        |       |  |  |  |
|-----------|---------------|--------|-------|--|--|--|
| Treatment | 130583        | 220683 | total |  |  |  |
| N1        | 0             | 0      | 0     |  |  |  |
| N2        | 6.0           | 0      | 6.0   |  |  |  |
| N3        | 12.0          | 4.0    | 16.0  |  |  |  |

was added to the uppermost soil layer on 1 October 1982 to enable apparent mineralization rates for the soil profile that were consistent with those estimated for these soils [31]. Output from the model was studied at two levels of temporal resolution: (1) hourly, to study the behavior of the algorithms for water and nutrient uptake by the simulated root system, and (2) seasonal, to compare the longer term distributions of carbon, nitrogen and water arising from these algorithms in the model with corresponding distributions recorded in the field experiment.

## **Results**

# *Hourly*

*Water uptake.* Hourly simulated profiles of 0s, 0s- 0r, La, and *FR, w* are presented at 0300 h, 0900 h, 1500 h and 2100 h on 4 July 1983 for the N1 treatment (Fig. 2). At 0300h (Fig. 2a), qJc was -0.40MPa and *Fc, w* was very low, while 0s - 0r was close to zero through the soil profile. Such equilibrium conditions in the model arise from high *r c* in the absence of solar irradiance. At 0900 h (Fig. 2b), 0c was -0.47 MPa, and *Fc, w*  was 0.08* 10 -3 m 3 m -2 h -1 of which the greater

part was taken up from the 0.20-0.50m soil zone. Because 0,, and hence hydraulic conductivity, increased with depth, the vertical distribution of *FR, w* was deeper than that of L d. Only a very small 0s - Or was necessary to generate the *FR, w* in each soil layer required to meet *Fc, w.* In fact, because 0s in the uppermost layer was lower than 0c, 0, - 0r, and hence *FR,w,* was negative, such that some redistribution of water in the soil profile occurred through the root system. Such redistribution has been observed experimentally [1]. At 1500 h (Fig. 2c), 0c was -0.62 MPa, and *Fc, w* was 0.28.10 -3 m 3 m -2 h -1. In comparison with those at 0900h, 0s-0r and *FR, w* were increased, most notably in the soil layers above 0.30 m. The small size of 0s - Or in comparison with 0r-0c indicates that under these conditions, the root hydraulic resistance was the greatest component of the soil- root-canopy resistance pathway in the model. At 2100 h (Fig. 2d), 0c was -0.45 MPa, and *Fc, w* was 0.004.10 .3 m 3 m -2 h-1. Negative 0s - Or gradients developed in the upper 0.20 m of the soil profile, causing some redistribution of water to this zone from lower in the profile where 0s - 0r remained slightly positive. The simulated profile of *L a* was similar in magnitude and distribution with that recorded at the same site and crop growth stage during the following year [20].

*N uptake.* The simulated dynamics of NH 4 and NO2 uptake through the soil profile are presented in Table 3 for treatments N1 and N3 at 0300 and 1500 h on 4 July 1983. Below 0.10 m, NH2 had been extracted in almost all layers to the minimum concentration (0.012g m -3 [3]) above which uptake can occur (Table 3a). At 0300 h, *FR,N, i* in treatment N1 was entirely diffu-

![](_page_6_Figure_0.jpeg)

*Fig. 2.* **Soil water potentials, soil-root water potential differences, root length densities, and water uptake simulated through the soil profile at (a) 0300 h, (b) 0900 h, (c) 1500 h, and (d) 2100 h on 4 July 1983 for the N1 treatment at Bouwing.** 

**sive, while at 1500 h, about 3% of** *FR,N, i* **was by mass flow. Diurnal changes in total** *UN, i* **(2.25 VS. 1.71 mg m -2 h -I) for all layers reflected declining concentrations in the uppermost layer. The simulated fertilizer treatments had little effect on NH4, so that the dynamics of NH 4 uptake in treatment N3 (Table 3b) were similar to those in treatment N1.** 

**NO 3 in the upper 0.40 m of the soil profile has been extracted in treatment N1 to the minimum** 

**concentration (0.030 g m -3 [3]) above which uptake can occur (Table 3c). Below 0.40 m, NO2 was still available. At 0300 h,** *FR,N, i* **in this zone was entirely diffusive, while 30% of FR.u, i at 1500 h was by mass flow. The ratio of mass flow to diffusion varied with** *FR, w* **and L a in each layer. Concentration gradients** *(CNs,i--CNr,i)* **were reduced by mass flow such that diffusion was reduced and total movement was little affected by time of day (4.92 vs 5.11 mg m -2 h-~).** 

206

| Depth<br>(m) |        | Movement<br>(g N m -3 soil h -~ * 103) |       |        |                          | Concentration<br>(g N m -3 water) |        |        |  |
|--------------|--------|----------------------------------------|-------|--------|--------------------------|-----------------------------------|--------|--------|--|
|              | 0300 h |                                        |       | 1500 h |                          | 0300 h                            |        | 1500 h |  |
|              | MF     | DF                                     | MF    | DF     | C~                       | Cur                               | C~     | Cur    |  |
| (a) NH: N1   |        |                                        |       |        |                          |                                   |        |        |  |
| 0.10         | 0.00   | 21.23                                  | 0.56  | 15.30  | 0.541                    | 0.095                             | 0.411  | 0.079  |  |
| 0.20         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| 0.30         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| 0.40         | 0.00   | 0.04                                   | 0.00  | 0.03   | 0.015                    | 0.013                             | 0.015  | 0.013  |  |
| 0.60         | 0.00   | 0.59                                   | 0.01  | 0.60   | 0.096                    | 0.027                             | 0.095  | 0.027  |  |
| 0.80         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| 1.00         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| Total uptake |        | 2.25                                   |       |        | 1.71 (g m -2 h-1103)     |                                   |        |        |  |
| (b) NH; N3   |        |                                        |       |        |                          |                                   |        |        |  |
| 0.10         | 0.00   | 31.20                                  | 0.77  | 30.50  | 1.159                    | O. 299                            | 1.053  | 0.138  |  |
| 0.20         | 0.00   | 0.04                                   | 0.01  | 0.02   | 0.014                    | 0.013                             | 0.013  | 0.013  |  |
| 0.30         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| 0.40         | 0.00   | 0.37                                   | 0.04  | 0.35   | 0.055                    | 0.019                             | 0.054  | 0.020  |  |
| 0.60         | 0.00   | 0.29                                   | 0.04  | 0.29   | 0.191                    | 0.053                             | 0.191  | 0.056  |  |
| 0.80         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| 1.00         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.012                    | 0.012                             | 0.012  | 0.012  |  |
| Total uptake |        | 3.22                                   |       |        | 3.24 (g m -2 h -~ * 103) |                                   |        |        |  |
| (c) NO~ N1   |        |                                        |       |        |                          |                                   |        |        |  |
| 0.10         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.030                    | 0.030                             | 0.030  | 0.030  |  |
| 0.20         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.030                    | 0.030                             | 0.030  | 0.030  |  |
| 0.30         | 0.00   | 0.00                                   | 0.00  | 0.00   | 0.030                    | 0.030                             | 0.030  | 0.030  |  |
| 0.40         | 0.00   | 0.00                                   | 0.01  | 0.25   | 0.030                    | 0.030                             | 0.042  | 0.032  |  |
| 0.60         | 0.00   | 14.61                                  | 1.03  | 13.89  | 8.179                    | 7.014                             | 7.587  | 6.501  |  |
| 0.80         | 0.01   | 7.93                                   | 3.42  | 4.89   | 23.816                   | 22.862                            | 23.628 | 23.061 |  |
| 1.00         | 0.00   | 2.06                                   | 1.57  | 0.63   | 33.297                   | 32.495                            | 33.313 | 33.081 |  |
| Total uptake |        | 4.92                                   |       |        | 5.11 (g m 2 h 1 . 103)   |                                   |        |        |  |
| (d) NO 3 N3  |        |                                        |       |        |                          |                                   |        |        |  |
| 0.10         | 0.09   | 64.14                                  | 48.91 | 70.39  | 69.857                   | 68.626                            | 66.716 | 65.309 |  |
| 0.20         | -0.00  | 2.64                                   | 0.10  | 2.43   | 0.091                    | 0.042                             | 0.087  | 0.040  |  |
| 0.30         | 0.00   | 0.92                                   | 0.05  | 0.77   | 0.066                    | 0.037                             | 0.062  | 0.036  |  |
| 0.40         | 0.01   | 18.46                                  | 4.48  | 13.59  | 6.133                    | 4.915                             | 5.667  | 4.760  |  |
| 0.60         | 0.01   | 2.79                                   | 5.31  | -2.32  | 25.905                   | 25.009                            | 25.975 | 26.722 |  |
| 0.80         | 0.00   | 0.55                                   | 1.36  | - 0.77 | 28.093                   | 27.386                            | 28.133 | 29.114 |  |
| 1.00         | 0.00   | 0.05                                   | 0.16  | -0.10  | 33.669                   | 33.054                            | 33.702 | 35.019 |  |
| Total uptake |        | 9.29                                   |       |        | 14.80 (g m : h 1,103)    |                                   |        |        |  |

*Table 3.* Simulated movement through mass flow (MF) and diffusion (DF), and solution concentrations in the bulk soil *(Cup)* and rhizosphere *(Cur.)* of winter wheat for NH2 under (a) low (N1) and (b) high (N3) and for NO2 under (c) low (N1) and (d) high (N3) N fertilization treatments at 0300 and 1500 h on 4 July 1983

Treatment N3 caused a large increase of *CNs,i ,*  and consequently of *FR,N, i* in the top soil layer (Table 3d), and smaller increases below. Because *Cur,i* in the top layer (68.6g m -3) was much higher than *Cxur,i* (0.40g m-3 [3]), only a small *(Cm, i -Cur,i )* was necessary to sustain high *UN, i.* Diurnal changes in the temperature of the upper 0.10m of soil between 0300 and 1500 h caused some change in *UN, i* max

(Eq. 4) and hence in *FR,N,i.* Below 0.40 m, high *Cus,i* caused mass flow to exceed *UN, i* at 1500 h, such that negative *(Cus,i- Cur,i )* and hence negative diffusion occurred. Higher ion concentrations in the rhizosphere than in the soil solution have been observed experimentally when mass flow exceeds uptake [35]. In the absence of mass flow, however, similar uptake rates were maintained by diffusion alone in this zone.

#### *Seasonal*

*Water uptake.* **Water uptake at the seasonal level is represented for treatment N1 in Fig. 3. Model runs began on 1 October 1982 with a stable water table at 1.50 m, and an initial volumetric water content (4, in m 3 m -3) at field capacity through the soil profile. By 7 February 1983, ~b of the entire soil profile was estimated to be 0.43-0.45, although lower values were recorded lower in the profile. In general, both simulated and recorded q5 remained near 0.40 until the end of May, after which depletion of water occurred at all depths. Some depletion was simulated from the 0.0-0.3 m soil zone before the end of May, such that 4, from April through July was underestimated by about 0.03. However, the simulated rate of ,depletion was consistent with that recorded for this zone. Depletion from the lower soil zones was not simulated before the end of May, although rates of depletion simulated during June and July were higher than those recorded. Consequently, 0 at 0.3-0.6 m was underestimated in later July. Seasonal trends in q5 were similar for the other two treatments.** 

*N uptake.* **Nitrogen uptake at the seasonal level is represented in Fig. 4 for the soil and Fig. 5 for the crop. Model runs were initialized on 1 October 1982 with an assumed NH 4 and NO 3** 

![](_page_8_Figure_3.jpeg)

*Fig. 3.* **Seasonal trends in volumetric water content simulated (lines) and recorded (symbols) for** 0.0-0.3 m, 0.3- 0.6 m, and 0.6-1.0 **in at Bouwing during** 1983.

![](_page_8_Figure_5.jpeg)

*Fig. 4.* **Seasonal trends in mineral N content simulated (lines) and recorded (symbols) for** (a) 0.0-0.3 m, (b) 0.3- 0.6 m, and (c) 0.6-1.0 m **at Bouwing during** 1983,

c

![](_page_9_Figure_0.jpeg)

*Fig. 5.* **Seasonal trends in mineral N uptake simulated (lines) and recorded (symbols) at Bouwing during 1983 for (a) shoots, (b) leaves, (c) stems + sheaths, and (d) grain.** 

**content of 1 /xg g-1 in each soil layer above 0.60 m and 15/xg g-1 in each soil layer below. The mineral N content in the upper 0.30m of soil (Fig. 4a) was overestimated by the model until mid-May due to mineralization from the simulated manure application. The rapid depletion of mineral N simulated from this soil zone during May was not apparent in the field data, such that N reached lower values than those** 

**recorded after mid-May. The model indicated an increase in soil N following the 6.0g m -2 of mineral N applied in treatment N2 on 13 May (day 133) and following the 12.0 g m -2 applied on 13 May and the 4.0g m 2 on 22 June (day 172) in treatment N3. However, almost none of the applied N was recovered in the field data. With the addition of 16.0 g m -2 of mineral N in treatment N3, cumulative denitrification simu-**  lated from 1 October 1982 to 1 August 1983 increased from 1.4 to 1.8 g m 2, while cumulative net leaching increased from 5.1 to 6.0 g m 2 over that of treatment N1. These increases did not account for the apparent disappearance of the mineral N in the field.

Mineral N levels in the 0.3-0.6m soil zone were overestimated by 1 to 2 g m -2 until mid-June (Fig. 4b). Simulated values remained between 3 and 4 g m ~ until mid-May, and then declined to less than 0.5g m -2 by the end of June, while recorded values declined from 3 g m -2 m-2 to 0.5 g from early March to mid-June. Fertilizer treatment had only a small effect on these levels in both the simulated and recorded data. The model did not reproduce the partial recovery of mineral N levels during July.

Mineral N levels simulated in the 0.6-1.0m soil zone were close to those recorded until the end of May (Fig. 4c). However, the model did not reproduce the rapid disappearance of mineral N from this zone during May, such that N levels in this zone were overestimated thereafter. As for the higher soil zone, the model did not reproduce the partial recovery of mineral N levels during July.

*N assimilation and remobilization.* The time integrals of the net N uptake rates for the shoots are shown in Fig. 5a as the cumulative N uptake by the crop over the growing season. These net rates are equivalent to the gross rates, examples of which were shown in Table 3, less the N retained in the roots and lost in senescent material. These integrals are compared with determinations of total above-ground N for the three treatments. The model accurately reproduced the rapid increase in uptake following the fertilizer applications in May and June. About 75 % of the simulated cumulative N uptake at the end of the season had been taken up before anthesis (day 170), as commonly observed in field trials [21]. Uptake in the N3 treatment was overestimated during late June and July.

The time integrals of N partitioned to and withdrawn from the leaves are shown with field data for total leaf N content in Fig. 5b. The model was able to reproduce the time course of leaf N content for the three treatments, as well as the delayed withdrawal of leaf N for treatments N2 and N3, which was apparent in this field trial and others [40]. However, the rate of N withdrawal during July was underestimated. Similarly, while the time course of N accumulation in the stalks was reproduced (Fig. 5c), N withdrawal from the stalks during July was underestimated, notably for treatment N3. The accumulation of N in the grain, however, was accurately simulated (Fig. 5d), indicating that late season uptake of N may have been overestimated. Such an overestimation is consistent with the overestimated depletion of mineral N in the 0 to 0.6 m soil zone during July (Fig. 4a and b), indicating that the values for *Cur.i min* in Eq. 4 may be too low for field applications, or that some mineral N is not available to the root system. The simulated N harvest index was about 0.75, as recorded in this and other field trials [21].

The effect of fertilizer treatment on crop DM accumulation (Fig. 6a) was less than that on N accumulation (Fig. 5a), as apparent in both the field and simulated results. The reduced rate of DM growth simulated for treatment N1 during July was caused by reduced content of simulated leaf N (Fig. 5b) and consequent reduced CO 2 fixation. Accumulated DM for treatment N3 was overestimated during July, as was accumulated N uptake. The model reproduced seasonal trends in leaf DM (Fig. 6b), although the rate of leaf senescence during mid and late July was underestimated. Stem + sheath (Fig. 6c) and grain (Fig. 6d) growth were relatively less affected by N treatment than was leaf growth, and seasonal trends were more closely reproduced by the model. Grain DM accumulation was overestimated for treatment N3 during July.

Values between 0.05 and 0.10% have been suggested as the critical range of *Cup* below which N may limit wheat yields [41]. Simulated *CNp* in treatment N1 declined below this range by mid-April, and remained low for the rest of the season (Fig. 7a). Treatments N2 and N3 allowed *CNp* to remain above this range until the end of June and July respectively. Treatment N1 caused simulated Ccp to remain above those of treatments N2 and N3 (Fig. 7b), although reduced CH20 production eventually caused *Ccp* to deline. Higher Ccp under lower N fertilization has been recorded experimentally in wheat [40].

![](_page_11_Figure_0.jpeg)

*Fig. 5.* Seasonal trends in DM growth simulated (lines) and recorded (symbols) at Bouwing during 1983 for (a) shoots, (b) leaves, (c) stems + sheaths, and (d) grain.

![](_page_11_Figure_2.jpeg)

*Fig. 7.* Seasonal trends in simulated (a) mineral N and (b) carbohydrate stored by the crop as the primary products of uptake and fixation.

### **Discussion**

The objective of simulation modelling is to integrate the findings of research at higher levels of spatial, temporal and biological resolution into representations of system behavior at lower levels of resolution. The first objective of this simulation study was thus to examine model behavior at the spatial and temporal resolution of the horizon and the hour, and to determine whether this behavior was consistent with that observed in detailed experiments.

The redistribution of water through the root system from wetter to drier soil zones (Fig. 2b and 2d) provides a theoretical basis for experimental observations [1], and indicates that short term patterns of water uptake by root systems were reproduced in the model. Under the conditions of this experiment, the rate of this redistribution was less than 0.1 mm h -~ for the entire profile and occurred when crop water potential was higher than those of the drier soil zones near the surface. This simulated rate was insufficient to replace water uptake by roots during the day, as also found experimentally [1].

The short term root dynamics reproduced in the model allowed it to simulate longer term patterns of water uptake (Fig. 3), although some evidence of excessive removal from the upper soil zones was apparent. More detailed validation of simulated water uptake is limited by uncertainty in the estimation of related phenomena (e.g. transpiration rates, unsaturated hydraulic conductivity), and the low temporal and spatial resolution at which uptake can be recorded.

The simulated short term dynamics of N uptake by root systems (Table 3) indicated that uptake was little influenced by transpiration, as changes in diffusion rates caused by altered concentration gradients partially offset changes in mass flow. The limited role of mass flow in N uptake is in agreement with theoretical findings [36]. The simulated accumulation of nutrient ions in the rhizosphere when both transpiration and nutrient concentrations are high (Table 3d) provides a theoretical basis for the accumulation of ions about the root observed in radioisotope studies [35]. The time integrals of the simulated short term uptake rates allowed the model to reproduce seasonal trends in crop N content (Fig. 5) for the fertilizer treatments in this study. However, a longer-term validation of the uptake algorithms could not be carried out from the field data.

The cause of the divergence between simulated and recorded data for the mineral N content of the upper soil zone (Fig. 4a) is not clear. In other such fertilizer experiments, most mineral N applied to the soil in early spring was recovered in samples taken two months later [19]. However, applications in later spring were consistently not recovered in later soil samples taken from this and other sites in the field study [20]. Further study is required to identify the cause of this apparent disappearance. The extent to which the model reproduced seasonal trends in soil mineral N was limited by an apparent underestimation of both its downward movement over winter, and its uptake from the lower part of the soil profile during spring (Fig. 4c). The accurate simulation of seasonal water movement is an important prerequisite for that of seasonal N uptake.

Underlying validation of the estimated rates of water and N uptake by root systems is validation of the estimated geometry of root systems, notably the spatial distribution of L~ and r 1. Profiles of La simulated in this study (Fig. 2) were consistent with those recorded at the same stage of crop growth from the same site the following year [20]. Because values arising from this distribution are used in estimating water and nutrient uptake (Eqs 2 to 4), there is a real need for a better understanding of the geometry of root proliferation, and of the processes that control it. The accurate reproduction of rooting patterns through the soil profile, in conjunction with basic algorithms for the uptake and assimilation of nutrients, will allow modelling to become an effective tool in the study of nutrient dynamics in the agroecosystem.

#### **Conclusions**

This simulation study indicates that the understanding of component processes that occur at a higher level of resolution in the agroecosystem may be used to understand the integrated behavior of the agroecosystem at a lower level of resolution. It also indicates that there are some areas where our understanding of these processes limits the extent to which we may understand this behavior.

#### **Acknowledgements**

This research was partially supported by a grant from the National Science Foundation and utilized the CRAY-2 facility of the National Center for Supercomputing Applications at the University of Illinois in Urbana-Champaign.

#### **References**

- 1. Baker JM and van Bavel CHM (1988) Water transfer through cotton plants connecting soil regions of differing water potentials. Agron J 80:993-997
- 2. Barber SA (1962) A diffusion and mass-flow concept of soil nutrient availability. Soil Sci 99:39-49
- 3. Barber SA (1984) Soil Nutrient Bioavailability: a Mechanistic Approach. Wiley & Sons New York, 398 p
- 4. Barfield BJ, Duncan WG and Haan CT (1977) Simulating the response of corn to irrigation in humid areas. paper no 77-2005 Am Soc Agric Eng annual meeting North Carolina State Univ Raleigh NC
- 5. Beek J and Frissel MJ (1973) Simulation of nitrogen behavior in soils. PUDOC Wageningen Netherlands
- 6. Caassen N and Barber SA (1976) Simulation model for nutrient uptake from soil by a growing plant root system. Agron J 68:961-964
- 7. Cushman JH (1979) An analytical solution to solute transport near root surfaces for low initial concentration. Soil Sci Soc Am J 43:1087-1095
- 8. Fleisher Z, Kenig A, Ravina I and Hagin J (1987) Model of ammonia volatilization from calcareous soils. Plant and Soil 103:205-212
- 9. Gardner WR (1960) Dynamic aspects of water availability to plants. Soil Sci 89:63-73
- 10. Gardner WR (1983) Soil properties and efficient water use: an overview. In: Limitations to Efficient Water Use in Crop Production. Taylor HM, Jordan WR and Sinclair TR (eds) pp 45-64 Am Soc Agron
- 11. Gilmour JT, Clark MD and Sigua GC (1985) Estimating net nitrogen mineralization from carbon dioxide evolution. Soil Sci Soc Am J 49:1398-1402
- 12. Grant RF (1989) Simulation of carbon accumulation and partitioning in maize. Agron J 81:563-571
- 13. Grant RF (1989) Test of a simple biochemical model for photosynthesis of maize and soybean leaves. Agric For Meteorol 48:59-74
- 14. Grant RF (1989) Simulation of maize phenology. Agron J 81:451-457
- 15. Grant RF (1990) Dynamic simulation of water deficit effects upon maize yield. Agric Systems, in press
- 16. Grant RF, Peters DB, Larson EM and Huck MG (1989) Simulation of canopy photosynthesis in maize and soybean. Agric For Meteorol 48:75-91
- 17. Grant RF, Izaurralde RC and Chanasyk DS (1990) Soil temperatures under different residue covers: simulation and experimental verification. Can J Soil Sci, in press
- 18. Greenwood DJ, Neeteson JJ and Draycott A (1985a) Response of potatoes to N fertilizer: dynamic model. Plant Soil 85:185-203
- 19. Greenwood DJ, Neeteson JJ and Draycott A (1985b) Response of potatoes to N fertilizer: quantitative relations for components of growth. Plant Soil 85:163-183
- 20. Groot JJR and Verberne ELJ (1991) Response of wheat to nitrogen fertilization, a data set to validate simulation models for nitrogen dynamics in crop and soil. Fert Res 27:349-383
- 21. Herzog H (1986) Source and sink during the reproductive period in wheat, Adv Agron and Crop Sci supplment 8 Paul Parey Scientific Publishers Berlin, 104 p
- 22. Jones CA and Kiniry JR (1986) CERES-maize. Texas A & M University Press College Sta TX
- 23. Juma NG and McGill WB (1986) Decomposition and nutrient cycling in agro-ecosystems. In: Microfloral and Faunal Interactions in Natural and Agro-ecosystems. Mitchell MJ and Nakas JP (eds) pp 74-136 Nijhoff/ Junk Netherlands
- 24. Kenig A (1987) The problem of quantifying limits to nitrogen use in relation to crop growth modeling. In Plant Growth Modeling for Resource Management. Wisiol K and Hesketh JD (eds) CRC Press Inc Boca Raton FL
- 25. Keulen H van (1981) Simulation of water use and herbage growth in arid regions- a reevaluation and further development of the model 'Arid Crop'. Agric Systems 6:159-193
- 26. Lauchli A (1984) Mechanisms of nutrient fluxes at membranes of the root surface and their regulation in the whole plant. In: Roots, Nutrient and Water Influx, and Plant Growth. pp 1-25 Amer Soc Agron special publication no 49 Madison WI
- 27. Leffelaar PA and Wessel WW (1988) Denitrification in a homogeneous, closed system: experiment and simulation. Soil Sci 146:335-349
- 28. Mahli SS and McGill WB (1982) Nitrification in three Alberta soils: Effect of temperature, moisture, and substrate concentration. Soil Biol Biochem 14:393-399
- 29. McGill WB, Hunt HW, Woodmansee RG and Reuss JO (1981) Phoenix, a model of the dynamics of carbon and nitrogen in grassland soils. In: Terrestrial Nitrogen Cycles. Clark FE and Rosswall T (eds) Ecol Bull 33: 49-115
- 30. Molina JAE, Clapp CE, Shaffer MJ, Chichester FW and Larson WE (1983) NCSOIL, a model of nitrogen and carbon transformations in soil: description, calibration and behavior. Soil Sci Soc Am J 47:85-91
- 31. Neeteson JJ (1989) Assessment of Fertilizer Nitrogen Requirement of Potatoes and Sugar Beet. Ph.D. Thesis Wageningen Agricultrual University Netherlands, 141 p
- 32. Noordwijk M van (1987) Methods for quantification of root distribution pattern and root dynamics in the field. In: Proc 20th Colloq Int Potash Insitute Bern, pp 263-281
- 33. Nye PH and Mariott FHC (1969) A theoretical study of the distribution of substances around roots resulting from simultaneous diffusion and mass flow. Plant and Soil 30:459-472
- 34. Paul EA and Juma NG (1981) Mineralization and immobilization of soil nitrogen by microorganisms. In: Terrestrial Nitrogen Cycles. Clark FE and Rosswall T (eds) Ecot Bull 33:179-195
- 35. Rendig VV and Taylor HM (1989) Principles of Soil-Plant Interrelationships. McGraw-HiU NY, 275 p
- 36. Seligman NG, van Keulen H and Goudriaan J (1975) An elementary model of nitrogen uptake and redistribution by annual plant speices. Oecologia 21:243-261
- 37. Siddiqi MY and Glass ADM (1982) Simultaneous consideration of tissue and substrate potassium concentration in K ÷ uptake kinetics: a model. Plant Physiol 69: 283-285
- 38. Smith OL (1982) Soil Microbiology: A Model of Nutrient Decomposition and Nutrient Cycling. CRC Press Inc Boca Raton FL
- 39. Spiertz JHJ (1974) Grain growth and distribution of dry matter in the wheat plant as influenced by temperature, light energy and ear size. Neth J Agric Sci 22:207-220
- 40. Spiertz JHJ and Ellen J (1978) Effects of nitrogen on crop development and grain growth of winter wheat in relation to assimilation and utilization of assimilates and nutrients. Neth J Agric Sci 21:210-231
- 41. Vlassak K and Verstraeten LMJ (1985) Nitrogen nutrition of winter wheat. In: Wheat Growth and Modelling. Day W and Atkin RK (eds) pp 217-236 Plenum Publishing
- 42. Wareing PF, Khalifa MM Treharne KJ (1968) Ratelimiting processes in photosynthesis at saturating light intensities. Nature 220:453-455
- 43. Zur B and Jones JW (1981) A model for the water relations, photosynthesis an expansive growth of crops. Water Resour Res 17:311-320