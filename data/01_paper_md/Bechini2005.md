![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

Environmental Modelling & Software 21 (2006) 1042e1054

[www.elsevier.com/locate/envsoft](http://www.elsevier.com/locate/envsoft)

# Parameterization of a crop growth and development simulation model at sub-model components level. An example for winter wheat (Triticum aestivum L.)

Luca Bechini a, *, Stefano Bocchi a , Tommaso Maggiore a , Roberto Confalonieri b

a Department of Crop Science, Section of Agronomy, University of Milano, Via Celoria 2, 20133 Milano, Italy b Institute for the Protection and Security of the Citizen, Joint Research Centre of the European Commission, AGRIFISH Unit, MARS-STAT Sector, TP 268 e 21020 Ispra (VA), Italy

> Received 2 June 2004; received in revised form 5 May 2005; accepted 9 May 2005 Available online 18 July 2005

#### Abstract

Dynamic simulation models are frequently used for assessing agronomic and environmental effects of different management practices, under various pedo-climatic conditions. CropSyst is a suitable cropping systems simulation model for such applications. However, available CropSyst crop parameters for winter wheat, one of the most important cereals in the world, are limited. In this work we show that it is possible to parameterize separate sub-model components by using existing experimental data and literature. The experiments, carried out in northern Italy between 1986 and 2001, quantified the dynamics of aboveground biomass (AGB),

plant nitrogen (N) concentration (PNC) and N uptake (UPTK) by means of periodical measurements.

The relative root mean square error (calculated by dividing the root mean square error by the average of observations) obtained after model calibration and validation on an independent data set was, respectively, in the range 9e30% and 17e32% for AGB, 10% and 6e40% for PNC, 8e28% and 9e24% for UPTK. AGB was frequently underestimated. Despite the limited accuracy of simulations, we argue that calibrated crop parameters are adequate for scenario analysis as most differences between years and fertilization levels were reproduced by the model and final AGB and cumulative UPTK were also correctly simulated. 2005 Elsevier Ltd. All rights reserved.

Keywords: Plant nitrogen concentration; Nitrogen uptake; Aboveground biomass; CropSyst; Crop growth rate; Temperature response function

#### 1. Introduction

Simulation models are nowadays widely applied in agriculture to make predictions about the agronomical, environmental and economic consequences of the complex interactions between crop management, soil and atmosphere (e.g. [Acutis et al., 2000; Bechini et al.,](#page-11-0) [2003; Donatelli et al., 2002; Go¨mann et al., 2005;](#page-11-0) [Johnsson et al., 2002; Lewis et al., 2003; Rossing et al.,](#page-11-0) [1997; Sousa and Pereira, 1999; Ten Berge et al., 2000;](#page-11-0) [Wise and Cacho, 2005; Wolf et al., 2003)](#page-11-0).

Because models allow the simulation of stochastic scenarios ([Badini et al., 1997; Acutis et al., 2000; Peralta](#page-11-0) [and Sto¨ckle, 2001; Bechini et al., 2003)](#page-11-0), they can be useful in the estimation of probabilities associated with the occurrence of events. Processes requiring scenario simulations in many intensive agricultural areas include the environmental impact of rural development plans, of manure and fertilizer management, and of agrotechniques involving the use of agrochemicals. CropSyst ([Sto¨ckle et al., 2003)](#page-12-0) is a cropping system simulation model which is distributed free of charge and provides: a platform for simulating crop rotations, an automatic

<sup>*</sup> Corresponding author. Tel.: C39 0250316590; fax: C39 0250316575. E-mail address: [luca.bechini@unimi.it](mailto:luca.bechini@unimi.it) (L. Bechini).

<sup>1364-8152/\$ -</sup> see front matter 2005 Elsevier Ltd. All rights reserved. doi:10.1016/j.envsoft.2005.05.006

management events scheduler, the possibility to run multiple simulations in connection with a Geographical Information System. All of the aforementioned characteristics make CropSyst particularly suitable for scenario simulations ([Peralta and Sto¨ckle, 2001; Bechini et al.,](#page-12-0) [2003)](#page-12-0); other models simulate crop growth processes with more detail but have lower or no flexibility in specifying routine management techniques (e.g. SUCROS, [Goudriaan and van Laar, 1994)](#page-12-0).

Realistic and accurate sets of crop parameters needed to correctly apply the models should be obtained from crop-specific field conditions. Such model parameters have been already published for several cultivated species in Italy [(Donatelli et al., 1997; Giardini et al.,](#page-11-0) [1998; Bellocchi et al., 2002; Bocchi et al., 2003;](#page-11-0) [Confalonieri and Bechini, 2004; Confalonieri and](#page-11-0) [Bocchi, in press)](#page-11-0).

Wheat (Triticum aestivum L.) is one of the most important cereals both in Italy and globally ([FAOSTAT](#page-11-0) [data, 2004)](#page-11-0). Despite the fact that wheat crop simulation models are now widely applied in monitoring and planning agricultural resources, CropSyst parameters for wheat are limited in the sense that they refer to older model versions [(Giardini et al., 1998)](#page-11-0), to specific pedoclimatic environments ([Sto¨ckle et al., 1994; Pannkuk](#page-12-0) [et al., 1998)](#page-12-0), and sometimes lack the complete list of crop parameters.

Considering the difficulty of performing serious, long-term experimental studies to set up and update species- and cultivar-specific sets of crop parameters, possible approaches for the estimation of crop model parameters include: (i) parameterize the models at species levels or, in the best cases, for sub-species groups (e.g. maturity classes for cereals such as rice, wheat and corn or plant morpho-physiological types for rice); (ii) recover, assess and use data collected for other purposes to derive the maximal amount of information for crop parameterization. Within this second approach, we may also consider specific sub-model components to determine the values of the main crop parameters.

The present study was performed: (i) to set up crop parameters required by CropSyst for winter wheat simulation; (ii) to assess the plausibility of reaching this objective through the integration of information recovered from relatively limited existing experimental data sets and from available literature; (iii) to highlight the potentials and the limitations of CropSyst as a tool for scenario analyses with winter wheat.

#### 2. Material and methods

# 2.1. Experimental data

Experimental data were collected in 4 experiments (Table 1 and 2) carried out between 1986 and 2002 in Table 1

| sets<br>data<br>The                   | this<br>in<br>used               | work                                   |                                |                          |                                                                                            |                                                                                                                                            |            |                       |                      |                                                       |
|---------------------------------------|----------------------------------|----------------------------------------|--------------------------------|--------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------|----------------------|-------------------------------------------------------|
| Experiment<br>no.                     | Location                         | longitude,<br>Latitude,<br>altitude    | Years                          | Sowing<br>date           | Treatments                                                                                 | Experimental<br>design                                                                                                                     | Replicates | Measured<br>variables | samples<br>of<br>No. | size<br>Sample                                        |
| 1                                     | Lodigiano<br>Angelo<br>S.        | a.s.l.<br>4515#N,<br>922#E,<br>m<br>73 | e1987<br>e1988<br>1986<br>1987 | 20/10/1986<br>25/10/1987 | )<br>1<br>ha<br>levels<br>N<br>140,<br>kg<br>N<br>210<br>(0,<br>3                          | block<br>randomized<br>Complete                                                                                                            | 3          | AGBc<br>PNCd          | 6                    | m)<br>linear<br>1.0<br>!<br>m<br>(0.18<br>m2<br>0.180 |
| 2                                     | Lodigiano<br>Angelo<br>S.        | a.s.l.<br>4515#N,<br>922#E,<br>m<br>73 | e1990<br>e1991<br>1989<br>1990 | 02/11/1989<br>16/11/1990 |                                                                                            | species;<br>cultivars)<br>(plot:<br>Split-plot<br>subplot:                                                                                 | 4          | AGBc<br>PNCd          | 15<br>16             | m)<br>linear<br>1.0<br>!<br>m<br>(0.18<br>m2<br>0.180 |
| 3                                     | Lodi                             | a.s.l.<br>4519#N,<br>928#E,<br>m<br>80 | e1997<br>1996                  | 14/10/1996               |                                                                                            | species;<br>cultivars)<br>(plot:<br>Split-plot<br>subplot:                                                                                 | 3          | AGBc<br>PNCd          | 8                    | m)<br>linear<br>1.0<br>!<br>m<br>(0.18<br>m2<br>0.180 |
| 4                                     | Lodigiano<br>Angelo<br>S.        | a.s.l.<br>4515#N,<br>922#E,<br>m<br>73 | e2002<br>2001                  | 16/11/2001               | 40,<br>0,<br>)<br>1<br>!<br>ha<br>100a<br>levels<br>N<br>kg<br>50,<br>N<br>80b<br>(0,<br>9 | fertilization;<br>fertilization;<br>cultivars)<br>top-dressing<br>preseeding<br>esplit-plot<br>sub-subplot:<br>subplot:<br>(plot:<br>Split | 3          | AGBc                  | 5                    | m)<br>linear<br>1.2<br>!<br>m<br>(0.18<br>m2<br>0.216 |
| Top-dressing<br>Pre-seeding<br>a<br>b | fertilization.<br>fertilization. |                                        |                                |                          |                                                                                            |                                                                                                                                            |            |                       |                      |                                                       |

c AGB d PNC

Z plant nitrogen

Z

aboveground

 biomass. concentration.

Table 2 Characteristics of the soils

| Experiment | Location  | Years     | Soil<br>layer (m) | Sand<br>(g kg<br>1<br>) | Clay<br>(g kg<br>1<br>) | Silt<br>(g kg<br>1<br>) | pH (water) | C.E.C.a<br>(cmol kg<br>1<br>) | SOMb<br>(g kg<br>1<br>) |
|------------|-----------|-----------|-------------------|-------------------------|-------------------------|-------------------------|------------|-------------------------------|-------------------------|
| 1          | S. Angelo | 1986e1987 | 0.00e0.40         | 550                     | 30                      | 420                     | 6.2        | 10.0                          | 26                      |
|            |           |           | 0.40e0.60         | 580                     | 20                      | 400                     |            |                               | 18                      |
|            |           |           | 0.60e0.80         | 540                     | 30                      | 430                     |            |                               | 15                      |
|            |           |           | 0.80e1.00         | 550                     | 30                      | 420                     |            |                               | 14                      |
| 1          | S. Angelo | 1987e1988 | 0.00e0.20         | 630                     | 40                      | 330                     | 6.7        | 13.0                          | 15                      |
|            |           |           | 0.20e0.40         | 650                     | 40                      | 310                     |            |                               | 15                      |
|            |           |           | 0.40e0.60         | 700                     | 40                      | 260                     |            |                               | 9                       |
|            |           |           | 0.60e0.80         | 600                     | 50                      | 350                     |            |                               | 8                       |
|            |           |           | 0.80e1.00         | 540                     | 30                      | 130                     |            |                               | 6                       |
| 2          | S. Angelo | 1989e1990 | 0.00e0.20         | 540                     | 90                      | 370                     | 5.9        | 12.0                          | 18                      |
|            |           |           | 0.20e0.40         | 670                     | 160                     | 170                     |            |                               | 17                      |
|            |           |           | 0.40e0.60         | 580                     | 20                      | 400                     |            |                               | 11                      |
|            |           |           | 0.60e0.80         | 540                     | 30                      | 430                     |            |                               | 9                       |
|            |           |           | 0.80e1.00         | 550                     | 30                      | 420                     |            |                               | 8                       |
| 2          | S. Angelo | 1990e1991 | 0.00e0.20         | 700                     | 50                      | 250                     | 6.7        | 10.9                          | 11                      |
|            |           |           | 0.20e0.40         | 710                     | 80                      | 210                     |            |                               | 7                       |
|            |           |           | 0.40e0.60         | 620                     | 50                      | 330                     |            |                               | 10                      |
|            |           |           | 0.60e0.80         | 550                     | 30                      | 420                     |            |                               | 8                       |
|            |           |           | 0.80e1.00         | 520                     | 20                      | 460                     |            |                               | 5                       |
| 3          | Lodi      | 1996e1997 | 0.00e0.30         | 720                     | 100                     | 180                     | 6.5        | 10.0                          | 15                      |
|            |           |           | 0.30e0.50         | 650                     | 130                     | 220                     |            |                               | 13                      |
|            |           |           | 0.50e1.00         | 540                     | 190                     | 270                     |            |                               | 10                      |
| 4          | S. Angelo | 2001e2002 | 0.00e0.20         | 690                     | 150                     | 160                     | 6.4        | 9.0                           | 13                      |
|            |           |           | 0.20e0.40         | 650                     | 150                     | 200                     |            |                               | 15                      |
|            |           |           | 0.40e0.60         | 550                     | 40                      | 410                     |            |                               | 11                      |
|            |           |           | 0.60e0.80         | 520                     | 20                      | 460                     |            |                               | 6                       |
|            |           |           | 0.80e1.00         | 540                     | 30                      | 430                     |            |                               | 7                       |

a C.E.C. Z cation exchange capacity. b SOM Z soil organic matter.

2 locations in northern Italy. This area is characterized by a moderate continental climate, with a mean annual temperature of about 13 C; the absolute minimum temperature occurs between January and February and the absolute maximum between July and August. Total precipitation (about 800 mm year-1 ) is relatively well distributed and the average wind speed is about 1.5 m s-1 .

For all the experiments considered, the soils had high phosphorus and low potassium content. Daily meteorological data (rainfall, maximum and minimum air temperatures, global solar radiation) were collected with automatic weather stations near the fields. Plant samples were dried in oven at 70 C (until constant weight) to determine the aboveground biomass (AGB).

The first experiment was carried out with the aim of verifying the effects of nitrogen (N) fertilization on winter wheat (cv. Gemini) growth. The second experiment had the purpose of describing the spring dynamics of biomass accumulation and forage quality of five species [winter wheat, Italian ryegrass (Lolium multiflorum Lam.), barley (Hordeum vulgare L.), rye (Secale cereale L.), triticale (Triticum ! Secale)]. Two cultivars were used for each species (Pandas and Centauro for wheat). AGB samples were collected every 10 days until head emergence [Decimal Code (DC) 55], every 3 days between earing and late milk maturity (DC77) and every 10 days between late milk maturity and physiological maturity (DC89). The third experiment was conducted to study the spring dynamics of forage quality and biomass accumulation of winter wheat, barley and Italian ryegrass. Two cultivars were grown for each species (Eridano and Soissons for wheat). The fourth experiment was carried out to compare the effects of N fertilization on the growth of three wheat cultivars (Guadalupe, Enesco and Eureka). In this experiment, aboveground plant biomass accumulation was measured only for the optimal N treatment. Plant sample size for AGB measurements was determined by using the following method. An elementary sub-sample size (S ) was chosen (0.20 linear m Z 0.036 m2 ). Nine biomass samples of size aS (with a integer from 2 to 10) were weighted, recording separately the values for each elementary sub-sample. For each sample the mean weight of the a sub-samples and its standard deviation were calculated. The means and the standard deviations were plotted against a. The minimum sample size for the experiment corresponded to the value of a with stable means and reasonably low standard deviations.

<span id="page-3-0"></span>![](_page_3_Figure_1.jpeg)

Fig. 1. Plant nitrogen concentration versus accumulated aboveground biomass: data used in this study for calibration and validation, and comparison between the maximum, critical and minimum nitrogen dilution curves proposed by [Justes et al. (1994)](#page-12-0) and calculated by CropSyst with our parameters set.

Overall, 80 average measurements of AGB and 75 of plant N concentration (PNC) were available in the data set (Fig. 1), covering a wide range of growth stages, biomasses and N concentrations. The experimental data were analyzed with the software CoLiDaTa [(Confalonieri](#page-11-0) [and Scaglia, 2002)](#page-11-0), which automatically applies many statistical tests for the validation of analytical data. In particular, the Grubbs's test ([Grubbs, 1969; ISO 5725-2,](#page-12-0) [1994)](#page-12-0) was used to discard outliers.

#### 2.2. Simulation model

CropSyst ([Sto¨ckle et al., 2003)](#page-12-0) is a multi-year, multicrop, daily time step cropping systems simulation model developed to evaluate the effects of different pedoclimatic and management conditions on crop growth and on environmental impact.

Crop development is simulated through thermal time accumulation, by computing the growing degree days (GDDs), using Tb (base temperature; C) as a lower threshold and Tcutoff ( C; optimum temperature for thermal time accumulation) as an upper threshold. Photoperiodical effects for long-day plants between emergence and flowering are implemented by multiplying GDDs by fphoto, a dimensionless variable: fphotoZ L - Lif- = Lins - Lif- where L is daylength (h), Lif (h) is daylength to inhibit flowering (no development occurs when daylength is below Lif), Lins (h) is daylength for insensitivity (above Lins the maximum development rate occurs). fphoto equals 0 below Lif and 1 above Lins.

The potential daily AGB production (AGBP) is calculated as the minimum of the values computed with Eqs. (1) and (2) proposed, respectively, by [Tanner and](#page-12-0) [Sinclair (1983)](#page-12-0) and by [Monteith (1977)](#page-12-0):

$$\text{AGB}_{\text{PT}} = \frac{K_{\text{BT}} T_{\text{P}}}{\text{VPD}} \tag{1}$$

where AGBPT (kg m-2 day-1 ) is the crop potential transpiration-dependent biomass production, TP (kg m-2 day-1 ) is crop potential transpiration, VPD (kPa) is the daytime mean atmospheric vapor pressure deficit and KBT (kPa kg kg-1 ) is a biomass-transpiration coefficient, which corresponds to the water use efficiency (WUE: aboveground biomass accumulated/water transpired) multiplied by the VPD.

$$\text{AGB}_{\text{iPAR}} = \text{RUE} \times \text{iPAR} \times T_{\text{lim}} \tag{2}$$

where AGBiPAR (kg m-2 day-1 ) is the intercepted PARdependent biomass production, RUEPAR (kg MJ-1 ) is the PAR use efficiency, iPAR (MJ m-2 day-1 ) is the daily amount of crop-intercepted photosynthetically active radiation and Tlim is a factor which describes the effect of temperature on radiation-dependent biomass accumulation, calculated as:

$$T_{\rm lim} = \begin{cases} 0 & T_{\rm m} < T_{\rm b} \\ \frac{T_{\rm m} - T_{\rm b}}{T_{\rm opt} - T_{\rm b}} & T_{\rm b} \le T_{\rm m} \le T_{\rm opt} \\ 1 & T_{\rm m} > T_{\rm opt} \end{cases} \tag{3}$$

where Tm ( C) is the average air daily temperature and Topt ( C) is the optimum temperature for growth.

The Eq. (2) is necessary because of the instability of Eq. (1) at low values of VPD. Water and nitrogen limitations are then applied to AGBP to calculate actual daily AGB production. Water limited growth (AGBT) is calculated by multiplying AGBP for the ratio of actual to potential transpiration; subsequently, actual daily AGB production is calculated by applying the concept <span id="page-4-0"></span>of critical nitrogen concentration [(Sto¨ckle and Debaeke,](#page-12-0) [1997](#page-12-0)) to AGBT.

Leaf area growth is calculated on the basis of Eq. (4):

$$\text{LAI} = \frac{\text{SLA} \times \text{AGB}}{\text{l} + p \times \text{AGB}} \tag{4}$$

where LAI (m2 m-2 ) is the green leaf area index, AGB is the accumulated aboveground biomass (kg m-2 ), SLA (m2 kg-1 ) is the mean of specific leaf area values measured at early growth stages and p is an empirical partitioning coefficient.

CropSyst uses the following equations to identify the maximum, critical and minimum nitrogen concentrations from emergence to flowering for the aboveground part of the plant:

$$N_{\text{max}} = \min\left(N_{\text{max}_{\text{\textd}}}, a_{\text{max}} \mathbf{AGB}^{-\delta}\right) \tag{5}$$

$$N_{\rm crit} = \min\left(0.8N_{\rm max_{\varepsilon}}, a_{\rm crit} \text{AGB}^{-\delta}\right) \tag{6}$$

$$N_{\rm min} = \min\left(0.4N_{\rm max_c}, a_{\rm min} \text{AGB}^{-b}\right) \tag{7}$$

where

$$a_{\text{max}} = \frac{N_{\text{max}_{\mathbf{e}}}}{2^{-b}} \tag{8}$$

$$a_{\rm crit} = \frac{0.8N_{\rm max_c}}{1.5^{-b}} \tag{9}$$

$$a_{\rm min} = \frac{0.4N_{\rm max_c}}{0.S^{-b}}\tag{10}$$

and Nmax, Ncrit and Nmin (%) are, respectively, the plant maximum, critical and minimum nitrogen concentrations; Nmaxe (%) is the plant maximum nitrogen concentration during early growth, AGB (kg ha-1 ) is the aboveground plant biomass; amax, acrit, amin represent thresholds at which plant nitrogen concentrations begin to decrease, and b Z 0.4. For the period between flowering and physiological maturity, maximum and minimum nitrogen concentrations decrease linearly to ''maximum nitrogen concentration at maturity'' (Nmaxm ) and ''minimum nitrogen concentration at maturity'' (Nminm ) input parameters.

#### 2.3. Model parameterization and validation

CropSyst version 3.02.23 (January 8, 2002) was used. Potential evapotranspiration was calculated by using the PriestleyeTaylor equation; the default value used (1.26) was already applied in the same area for rice simulation ([Confalonieri and Bocchi, in press)](#page-11-0); the aridity factor was set to 0.030 (default). Soil water redistribution was simulated with the cascade sub-model.

Due to the relatively limited amount of available data, calibration of crop parameters was carried out without distinctions among cultivars. Far from being correct for a subsequent experimental application of CropSyst, this approach is in our opinion coherent with the purpose of deriving a set of crop parameters for scenario simulations at species level.

Data from the second and fourth experiments were used for the calibration of crop parameters, while data from the first and third were used for validation. During the first experiment, cultivar Gemini was grown; for the second, data collected for Centauro and Pandas cultivars were averaged, as in the third experiment for the cultivars Soissons and Eridano; for the fourth experiment, only data collected for the cultivar Eureka were used. We were not interested in specifically calibrating most of the crop N parameters, because an extensive work on N dilution curves for winter wheat has been already carried out by [Justes et al. (1994):](#page-12-0) for this reason, we included only non-N limited treatments in the calibration data set. All experiments fulfilled this requirement; the second experiment was chosen for calibration because it is the one with the highest number of AGB measurements; experiment no. 3 was used for validation, having measurements of PNC, while no. 4 was used for calibration (no measurements of PNC available). Nitrogen simulation was activated for all the simulations, using the parameterization of nitrogen transformations set up by [Confalonieri et al. (2001)](#page-11-0) on similar soils.

The calibration of crop parameters was carried out separately for each simulation module, i.e. crop phenology (thermal time, photoperiod) and crop growth (water- and radiation-dependent growth, nitrogendependent growth). We underline that CropSyst is not a modular simulator, but we reproduced simple model components in a spreadsheet, to calculate specific rate equations outside the model. This procedure was intended to avoid problems derived from a ''blackbox'' calibration (carried out on the whole simulation model) where the error in one parameter value could be compensated by errors in other parameter values and, despite reasonable simulation results, the parameterization obtained could be inaccurate and unrealistic.

## 2.3.1. Crop development e thermal time and photoperiod modules

With two exceptions, all the parameters were calibrated on the basis of our experimental data set. Thermal time required for emergence was taken from literature, because we did not have recorded emergence dates; phenologic sensitivity to water stress was left to the default value because our data set did not include situations that allowed calibration of this parameter. Tb, Tcutoff, Lif and Lins were calibrated using the Microsoft

Excel Solver ([Flystra et al., 1998)](#page-11-0), such that the coefficient of variation (CV) among the GDDs required from emergence to flowering and from emergence to physiological maturity, was minimized (following [Bonhomme et al., 1994)](#page-11-0).

## 2.3.2. Crop growth e water- and radiation-dependent growth modules

From our experience and a previous sensitivity analysis carried out with the same model [(Confalonieri](#page-11-0) [and Bechini, 2004)](#page-11-0), we decided, for the less important parameters, to set several of them at their default values and to take others from literature. We calibrated RUEPAR, by isolating the calculation of radiationdependent biomass from the calculation of transpirationdependent biomass. To do this, because CropSyst is not a modular model, we decided to separately reproduce the two sub-models for the calculation of AGBiPAR and AGBPT, by calculating Eqs. (1) and (2) in a spreadsheet. These equations were used to simulate daily AGB accumulation for the period between the closed canopy stage (full radiation interception) and flowering: in this period, AGBiPAR depends only on solar radiation, RUEPAR and air temperature. Because CropSyst uses the minimum of AGBiPAR and AGBPT as the potential daily AGB production, the periods in which AGBiPAR was lower than AGBPT were selected. The Microsoft Excel Solver was then used to calibrate RUEPAR, with the objective of minimizing the difference between measured and calculated AGB increments. We further improved the goodness of simulations for the whole crop growing period by calibrating KBT, SLA, Topt, leaf duration and p, within reasonable ranges drawn from the literature.

# 2.3.3. Crop growth e N-dependent growth module

In accordance with Eq. [(9)](#page-4-0), Nmaxe was calculated as acrit/0.8, with acrit Z 4.4% (critical N concentration during early stages, with AGB ! 1.55 t DM ha-1 ; [Justes](#page-12-0) [et al., 1994)](#page-12-0). Moreover, Nminm was set as the minimum concentration reached with AGB of 14 t DM ha-1 ([Justes et al., 1994)](#page-12-0). Nmaxm was calibrated by using our experimental data. We further calibrated the empirical parameters ''N uptake adjustment'' and ''N availability adjustment'' to reduce the errors in the simulations of PNC.

The agreement between measured and simulated values of accumulated AGB, PNC and accumulated UPTK was expressed by using several of the indices proposed by [Loague and Green (1991)](#page-12-0) and recently reviewed by [Fila et al. (2003):](#page-11-0) the relative root mean square error (RRMSE, ranges from 0 to CN, optimum Z 0%), the coefficient of determination (CD, ranges from 0 to CN, optimum Z 1, indicates whether the model reproduces the trend of measured values or not), the modelling efficiency (EF, ranges from -N to 1, optimum Z 1, if positive, indicates that the model is a better predictor than the average of measured values), the coefficient of residual mass (CRM, ranges from -N to CN, optimum Z 0, if positive indicates model underestimation). The parameters of the linear regression equation between measured and predicted values were also calculated with the least squares method; because these data are not independent ([Donatelli et al.,](#page-11-0) [2003)](#page-11-0), no conclusions were drawn about their statistical significance.

#### 3. Results and discussion

#### 3.1. Calibration of crop model parameters

Calibrated crop model parameters are shown in [Table 3.](#page-6-0)

#### 3.1.1. Crop development modules

With the values of -1 C and 20 C for Tb and Tcutoff, a coefficient of variation of 6% among the GDDs to reach physiological maturity was obtained for the three data sets used for calibration. The calibrated values for Tb and Tcutoff are coherent with what reported by [Porter and Gawith (1999)](#page-12-0) (optimal temperatures for development between sowing and emergence, around anthesis and during grain filling of 22.0, 21.0 and 20.7 C, respectively; minimum temperatures of 1.9 C for leaf growth and of -1 C for leaf initiation) and by [Slafer and Rawson (1995)](#page-12-0) (0 C for Tb-development during early stages). In general, however, values of Tb reported in the literature [(Porter and Gawith, 1999)](#page-12-0) are greater than the value calibrated in this work and highly variable for the last part of the crop cycle.

# 3.1.2. Crop growth e water- and

#### radiation-dependent growth modules

The calibrated value of the optimum temperature for growth (Topt Z 19 C) is equal to the one reported by [Slafer and Rawson (1995)](#page-12-0) for wheat shoot growth. The calibrated value for RUEPAR (3.1 g MJ-1 ) is in good agreement with values reported by many authors. [Kiniry](#page-12-0) [et al. (1989)](#page-12-0), in a review about radiation use efficiency, report values for wheat RUEPAR ranging from 2.6 to 3.1 g MJ-1 , with an average value of 2.8 g MJ-1 . [Yunusa et al. (1993)](#page-12-0) obtained a value of 2.93 g MJ-1 from continuous measurements during the vegetative growing period. This work was also cited by [Sinclair and](#page-12-0) [Muchow (1999)](#page-12-0) as an accurate measurement of potential RUEPAR, because most of the other works reviewed by them are related to spot measurements or to absorbed PAR measurements: none of them can be used with the modelling approach of CropSyst. In other papers about wheat simulations with CropSyst, RUEPAR was maintained at the default value of 3 g MJ-1 ([Sto¨ckle](#page-12-0) [et al., 1994; Pannkuk et al., 1998](#page-12-0)) while [Giardini et al.](#page-11-0) <span id="page-6-0"></span>Table 3

| Crop model parameters for winter wheat: their values and source of information (C: calibrated parameters; D: CropSyst default values; L: derived |  |  |  |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|
| from literature)                                                                                                                                 |  |  |  |  |  |

| Parameter                                                            | Source | Value         | Units            |
|----------------------------------------------------------------------|--------|---------------|------------------|
| Thermal time accumulation                                            |        |               |                  |
| Degree days emergence                                                | La     | 100           | C-days           |
| Degree days peak LAI                                                 | C      | 550           | C-days           |
| Degree days begin flowering                                          | C      | 564           | C-days           |
| Degree days begin grain filling                                      | C      | 715           | C-days           |
| Degree days physiological maturity                                   | C      | 1352          | C-days           |
| Base temperature (Tb)                                                | C      | 1<br>         | C                |
| Cutoff temperature (Tcutoff)                                         | C      | 20            | C                |
| Phenologic sensitivity to water stress                               | D      | 0.5           | e                |
| Photoperiod                                                          |        |               |                  |
| Photoperiod simulation                                               | e      | Activated     | e                |
| Day length photoperiod to inhibit flowering                          | C      | 10            | h                |
| Day length photoperiod for insensitivity                             | C      | 18            | h                |
| Morphology                                                           |        |               |                  |
| Specific leaf area (SLA)                                             | C      | 25            | m2 kg<br>1       |
| Fraction of maximum LAI at physiological maturity                    | D      | 0.5           | e                |
| Maximum rooting depth                                                | D      | 1.6           | m                |
| Stem/Leaf partition coefficient ( p)                                 | C      | 1.5           | m2 kg<br>1       |
| Leaf duration                                                        | C      | 1000          | C-days           |
| Extinction coefficient for solar radiation (k)                       | D      | 0.48          | e                |
| ET crop coefficient at full canopy                                   | Lb     | 1.15          | e                |
| Growth                                                               |        |               |                  |
| Photosynthetic pathway                                               | e      | C3            | e                |
| Light to above ground biomass conversion (RUEPAR)                    | C      | 3.1           | 1<br>g MJ        |
| Optimum mean daily temperature for growth (Topt)                     | C      | 19            | C                |
| Aboveground biomass-transpiration coefficient (KBT)                  | C      | 5.8 ! 10<br>3 | kPa kg kg<br>1   |
| Maximum water uptake                                                 | D      | 10            | mm day<br>1      |
| Leaf water potential at the onset of stomatal closure                | D      | 1300<br>      | 1<br>J kg        |
| Wilting leaf water potential                                         | D      | <br>2000      | 1<br>J kg        |
| Actual to potential transpiration ratio that limits leaf area growth | D      | 0.95          | e                |
| Actual to potential transpiration ratio that limits root growth      | D      | 0.5           | e                |
| Nitrogen-dependent growth                                            |        |               |                  |
| Nitrogen uptake adjustment                                           | C      | 0.06          | e                |
| Nitrogen availability adjustment                                     | C      | 0.16          | e                |
| Maximum N concentration during early growth (Nmaxe<br>)              | Lc     | 0.055         | kg N kg AGB<br>1 |
| Maximum N concentration at maturity (Nmaxm<br>)                      | C      | 0.015         | kg N kg AGB<br>1 |
| Minimum N concentration at maturity (Nminm<br>)                      | Lc     | 0.007         | kg N kg AGB<br>1 |

AGB Z aboveground biomass. a [Pannkuk et al. (1998).](#page-12-0)

b [Allen et al. (1998).](#page-11-0) c [Justes et al. (1994).](#page-12-0)

[(1998)](#page-11-0) used a value of 3.5 g MJ-1 . Measurements of radiation use efficiency normally derive from field experiments only rarely carried out in non-limiting temperature conditions, while the RUEPAR used by CropSyst is a potential value (temperature limitation is applied separately). For this reason, the calibrated value was considered correct, although it lies at the upper limit of the range of values discussed.

The calibrated value for KBT (5.8 ! 10-3 kPa kg kg-1 , Table 3) is hardly comparable with values from literature, because the water use efficiency (WUE) is usually calculated by dividing yield by transpired (or evapotranspired) water. However, CropSyst uses the VPD e corrected WUE ([Tanner and Sinclair, 1983;](#page-12-0) [Amir and Sinclair, 1991, 1996)](#page-12-0). Our selected value is that which was calibrated by [Sto¨ckle et al. (1994)](#page-12-0) and reported by [Amir and Sinclair (1991, 1996).](#page-11-0)

The default extinction coefficient for solar radiation (k Z 0.48) is in good agreement with the value of 0.49 G 0.018 calculated by [Abbate et al. (1997)](#page-11-0) for spring wheat and with the value of 0.45 used by [Sto¨ckle](#page-12-0) [et al. (1994)](#page-12-0) for winter wheat and by [Donatelli et al.](#page-11-0) [(1997)](#page-11-0) for durum wheat.

The calibrated value of SLA (25 m2 kg-1 ) is consistent with the one assumed by [Sinclair and Amir](#page-12-0) [(1992)](#page-12-0) for a model with a fixed value of this parameter. No measured data of LAI were available in our data sets; therefore, it was not possible to carry out a proper model evaluation of leaf area simulations. Nonetheless, we checked that the simulated maximum LAI never exceeded the value of 9 m2 m-2 , a reasonable maximum threshold for this crop ([Bindraban, 1999; Olesen et al.,](#page-11-0) [2002)](#page-11-0); this, together with the goodness of AGB simulations, affords confidence in the calibrated value for the empirical Stem/Leaf partition coefficient ( pZ1.5).

# 3.1.3. Crop growth e N-dependent growth module

The coefficients of the nitrogen dilution equations used by CropSyst and by [Justes et al. (1994)](#page-12-0) show small differences, and therefore the resulting curves are very similar; CropSyst's equation only slightly underestimates Nmax and Nmin [(Fig. 1)](#page-3-0). This confirms the suitability of the value of Nmaxe (5.5%). The calibrated Nmaxm value (1.5%) is equal to the CropSyst default.

### 3.1.4. Model performance

With respect to the calibration data set, the good agreement between measured and simulated AGB and PNC is shown in [Figs. 2 and 3](#page-8-0) and in [Table 4.](#page-10-0) The model was accurate in the simulation of AGB accumulation ([Fig. 2](#page-8-0)b and c), with the exception of S. Angelo Lodigiano e 1989 ([Fig. 2](#page-8-0)a). AGB is clearly underestimated for early growth until the beginning of June, when lodging decreased the measured AGB. The underestimation in 1989e1990 cannot be corrected by further modifying the parameters involved with AGB accumulation (e.g. by using a lower value for Topt or a higher value for RUEPAR and/or KBT) because these parameters are already set to the most extreme values found in the literature. Moreover, a comparison of the results obtained (for 2 years) with a more extended weather data set for the same location (including relative humidity and wind speed data) has shown that the use of PenmaneMonteith equation to estimate the reference evapotranspiration did not improve AGB simulations. This might indicate that the use of the PriestleyeTaylor equation did not cause a significant underestimation of transpiration and therefore of AGB accumulation (Eq. [(1)](#page-3-0)). The problem of AGB underestimation will be further discussed in the next section.

The agreement between measured and simulated UPTK (kg N ha-1 ; [Table 4](#page-10-0)) is not always satisfactory because the errors in the simulation of AGB and PNC are in general not compensating each other, yielding similar or higher errors for the simulation of UPTK.

## 3.2. Validation of crop model parameters

The agreement between measured and simulated values of AGB, PNC and UPTK for the validation data set is shown in [Figs. 2 and 3](#page-8-0) and in [Table 4.](#page-10-0) For AGB, the validation has confirmed the applicability of the proposed parameter set, even if there is a systematic underestimation of crop growth rates in spring (linear phase of growth, with average monthly (June) temperatures ranging from 16.2 to 18.1 C), particularly with respect to the 1986e1987 data ([Table 5](#page-10-0)). For PNC, the model has in general reproduced the trend of measured data with a reasonable approximation of the absolute values; for UPTK the simulations are in most cases acceptable, with a compensation effect in several cases (opposite errors in the simulation of AGB and PNC partially improve the simulations of UPTK).

The underestimation of crop growth rates in spring can possibly be explained by looking at the shape of the relation between average air temperature and radiationdependent biomass accumulation (Eq. [(3))](#page-3-0). CropSyst adopts a linear relationship, which determines two abrupt transitions at the lower (Tb) and upper (Topt) limits; this does not accurately describe a biological phenomenon [(Yin et al., 1995)](#page-12-0). Compared to a smoothed logistic function [(Fig. 4](#page-11-0)), the linear relationship overestimates Tlim for temperatures slightly higher than Tb and underestimates for temperatures near Topt. The over- and underestimation of Tlim generates over- and underestimation of the crop growth rate when potential transpiration is high (Eq. [(2)](#page-3-0)). For this reason, we compared the logistic function proposed by [Yan and](#page-12-0) [Hunt (1999)](#page-12-0) (Eq. (11)) with the one used by CropSyst, by calculating AGBiPAR in a spreadsheet.

$$T_{\rm lim} = \left[ \left( \frac{T_{\rm m} - T_{\rm b}}{T_{\rm opt} - T_{\rm b}} \right) \left( \frac{T_{\rm max} - T_{\rm m}}{T_{\rm max} - T_{\rm opt}} \right)^{\frac{T_{\rm max} - T_{\rm opt}}{T_{\rm opt} - T_{\rm b}}} \right]^c \tag{11}$$

The parameter c has been set to 1.8 in order to constrain the two functions to the same value at T Z 0.5 (Topt C Tb) ([Fig. 4)](#page-11-0). The comparison of the AGBiPAR values calculated using the linear function for Tlim (AGBLin; Eq. [(3)](#page-3-0)) and using the logistic approach (AGBLog; Eq. (11)) has shown a systematic underestimation of AGBLin during the linear phase of biomass accumulation [Tm O 0.5(Topt C Tb)]. The use of a logistic instead of a linear function to relate radiationdependent biomass accumulation and average air temperature could probably reduce the underestimation of simulated crop growth rates in this work.

Finally, although CropSyst uses a single equation of N dilution for all herbaceous crops (i.e. the b parameter used in Nmax, Ncrit and Nmin equations is not userdefined and is by default set to 0.4), it should be noted that other authors found different values for it in the Ncrit curve. [Bechini et al. (2001)](#page-11-0) found a value of 0.76 for Italian ryegrass, while [Tei et al. (2001)](#page-12-0) found a lower value for tomato (0.327). Therefore, although the value used by CropSyst is very similar to the one proposed by

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Fig. 2. Measured (points) and simulated (lines) AGB values after calibration (a, b, c) and after validation (d, e, f, g, h, i, j): (a) S. Angelo Lodigiano e e1990; (b) S. Angelo Lodigiano e 1990e1991; (c) S. Angelo Lodigiano e 2001e2002; (d, e and f) S. Angelo Lodigiano e 1986e1987: (d) nitrogen fertilization: 0 kg N ha- , (e) nitrogen fertilization: 140 kg N ha- , (f) nitrogen fertilization: 210 kg N ha- ; (g, h and i) S. Angelo Lodigiano e e1988: (g) nitrogen fertilization: 0 kg N ha- , (h) nitrogen fertilization: 140 kg N ha- , (i) nitrogen fertilization: 210 kg N ha- ; (j) Lodi e e1997. The vertical bars indicate the standard deviation of measured data.

[Justes et al. (1994)](#page-12-0) for wheat and to the values proposed by other authors for other crops (e.g. 0.37 for maize, [Ple´net and Lemaire, 1999)](#page-12-0), a possible improvement of CropSyst would be to give the user the option of changing this parameter.

## 3.3. Model adequacy for scenario simulations

Model performance was not always satisfactory, and therefore this crop parameter set cannot be used for applications requiring very good simulation accuracy.

![](_page_9_Figure_1.jpeg)

Fig. 3. Measured (points) and simulated (lines) PNC values after calibration (a, b) and after validation (c, d, e, f, g, h, i): (a) S. Angelo Lodigiano e1990; (b) S. Angelo Lodigiano 1990e1991; (c, d and e) S. Angelo Lodigiano 1986e1987: (c) 0 kg N ha- , (d) 140 kg N ha- , (e) 210 kg N ha- ; (f, g and h) S. Angelo Lodigiano 1987e1988: (f) 0 kg N ha- , (g) 140 kg N ha- , (h) 210 kg N ha- ; (i) Lodi 1996e1997.

04/03/97 22/03/97 09/04/97 27/04/97 15/05/97 02/06/97

However, when used for comparing scenarios, the model is required to reproduce the ranking of real values and to correctly simulate simple and synthetic variables across a range of simulations. For this purpose, we evaluated the overall model performance by calculating the indices of agreement between measured and simulated values of AGB and UPTK (for the last sampling date) in order to describe the goodness of the results when yearly or seasonal statistics are compiled with the model (biomass produced, cumulative N uptake). The results ([Table 4)](#page-10-0) can be considered satisfactory. Moreover, the Spearman correlation coefficient (data not normally distributed) between measured and simulated values on a merged set of all our data (across years, locations and treatments) is <span id="page-10-0"></span>Table 4

Indices of agreement between measured and simulated values of aboveground biomass (AGB), plant N concentration (PNC), aboveground plant nitrogen uptake (UPTK), during calibration and validation

| Variable | Process     | Location                      | Sowing year | Treatment        | RRMSE | EF       | CRM      | CD    | Slope | Intercept | R2   |
|----------|-------------|-------------------------------|-------------|------------------|-------|----------|----------|-------|-------|-----------|------|
| AGB      | Calibration | S. Angelo                     | 1989        | Optimal N        | 30    | 0.57     | 0.21     | 1.26  | 0.92  | 1.28<br>  | 0.80 |
|          |             |                               | 1990        |                  | 9     | 0.98     | 0.06<br> | 0.89  | 0.93  | 0.97      | 0.99 |
|          |             |                               | 2001        |                  | 15    | 0.96     | 0.10     | 0.87  | 0.91  | <br>0.15  | 0.98 |
|          | Validation  | S. Angelo                     | 1986        | 1<br>0 kg N ha   | 32    | 0.49     | 0.28     | 0.79  | 0.93  | <br>0.56  | 0.87 |
|          |             |                               |             | 140 kg N ha<br>1 | 26    | 0.59     | 0.20     | 0.84  | 1.09  | <br>2.68  | 0.85 |
|          |             |                               |             | 210 kg N ha<br>1 | 24    | 0.62     | 0.22     | 1.00  | 1.09  | <br>2.20  | 0.95 |
|          |             |                               | 1987        | 0 kg N ha<br>1   | 26    | 0.69     | 0.23     | 0.91  | 0.61  | 1.76      | 0.96 |
|          |             |                               |             | 140 kg N ha<br>1 | 22    | 0.75     | 0.22     | 1.21  | 0.76  | 0.84      | 0.98 |
|          |             |                               |             | 210 kg N ha<br>1 | 19    | 0.83     | 0.17     | 1.31  | 0.81  | 0.38<br>  | 0.97 |
|          |             | Lodi                          | 1996        | Optimal N        | 17    | 0.69     | 0.12<br> | 0.87  | 0.93  | 0.56<br>  | 0.84 |
| PNC      | Calibration | S. Angelo                     | 1989        | Optimal N        | 10    | 0.95     | <br>0.03 | 0.86  | 0.90  | 0.00      | 0.96 |
|          |             |                               | 1990        |                  | 10    | 0.95     | <br>0.05 | 0.82  | 0.88  | 0.00      | 0.97 |
|          | Validation  | S. Angelo                     | 1986        | 0 kg N ha<br>1   | 27    | 0.17     | <br>0.21 | 2.11  | 0.58  | 0.85      | 0.66 |
|          |             |                               |             | 140 kg N ha<br>1 | 8     | 0.86     | 0.01<br> | 1.42  | 0.94  | 0.08      | 0.92 |
|          |             |                               |             | 1<br>210 kg N ha | 6     | 0.91     | 0.01<br> | 0.84  | 0.88  | 0.26      | 0.92 |
|          |             |                               | 1987        | 0 kg N ha<br>1   | 40    | 7.67<br> | 0.28<br> | 11.63 | 1.97  | 0.92<br>  | 0.54 |
|          |             |                               |             | 1<br>140 kg N ha | 26    | 0.32     | <br>0.11 | 3.09  | 1.89  | <br>1.70  | 0.98 |
|          |             |                               |             | 210 kg N ha<br>1 | 25    | 0.56     | <br>0.17 | 2.25  | 1.53  | <br>0.75  | 0.96 |
|          |             | Lodi                          | 1996        | Optimal N        | 16    | 0.70     | <br>0.02 | 0.42  | 0.46  | 0.94      | 0.98 |
| UPTK     | Calibration | S. Angelo                     | 1989        | Optimal N        | 28    | 0.29<br> | 0.25     | 2.14  | 0.92  | 38.65<br> | 0.74 |
|          |             |                               | 1990        |                  | 8     | 0.95     | 0.07<br> | 1.13  | 1.04  | 4.75      | 0.97 |
|          | Validation  | S. Angelo                     | 1986        | 0 kg N ha<br>1   | 10    | 0.75     | 0.08     | 1.02  | 0.62  | 37.00     | 0.94 |
|          |             |                               |             | 1<br>140 kg N ha | 20    | 0.52     | 0.17     | 0.84  | 0.69  | 26.91     | 0.90 |
|          |             |                               |             | 210 kg N ha<br>1 | 13    | 0.79     | 0.09     | 0.69  | 0.79  | 33.08     | 0.94 |
|          |             |                               | 1987        | 1<br>0 kg N ha   | 23    | 0.72     | 0.03     | 0.26  | 0.53  | 52.55     | 0.94 |
|          |             |                               |             | 140 kg N ha<br>1 | 20    | 0.54     | 0.20     | 1.36  | 0.72  | 4.22      | 0.99 |
|          |             |                               |             | 210 kg N ha<br>1 | 24    | 0.40     | 0.22     | 1.50  | 0.95  | 35.28<br> | 0.91 |
|          |             | Lodi                          | 1996        | Optimal N        | 9     | 0.19     | 0.02     | 0.28  | 0.32  | 66.67     | 0.25 |
| AGB      |             | For the last<br>sampling date |             |                  | 7     | 0.73     | 0.03     | 0.75  | 0.74  | 3.51      | 0.79 |
| UPTK     |             | of each data set              |             |                  | 20    | 0.48     | 0.13     | 1.06  | 0.77  | 22.88     | 0.71 |

equal to 0.94, 0.97 and 0.89 for AGB, PNC and UPTK, respectively, all highly significant (n Z 71; P ! 0.001). These results show that this set of crop parameters can be already used for scenario simulations in the study area because seasonal outputs (total biomass produced at harvest, cumulative N uptake) are simulated with sufficient accuracy and because the ranking of measured and simulated values is approximately the same.

| Table 5 |  |
|---------|--|

| Measured and simulated mean daily crop growth rates related to average air temperature during the linear growth phase |  |  |  |
|-----------------------------------------------------------------------------------------------------------------------|--|--|--|
|-----------------------------------------------------------------------------------------------------------------------|--|--|--|

| Figure | Dataset           | Period    | Mean daily crop growth rate<br>1 day<br>1<br>a<br>(t AGB ha<br>) |           | Percent model<br>error (%) | Average air<br>temperature ( C) |
|--------|-------------------|-----------|------------------------------------------------------------------|-----------|----------------------------|---------------------------------|
|        |                   |           | Measured                                                         | Simulated |                            |                                 |
| 2a     | S. Angelo 1989e90 | 30/4e23/5 | 0.30                                                             | 0.18      | 39                         | 16.7                            |
| 2b     | S. Angelo 1990e91 | 17/5e30/5 | 0.31                                                             | 0.24      | 21                         | 18.1                            |
| 2c     | S. Angelo 2001e02 | 12/4e29/5 | 0.22                                                             | 0.18      | 20                         | 16.2                            |
| 2f     | S. Angelo 1986e87 | 10/5e7/6  | 0.35                                                             | 0.22      | 37                         | 16.4                            |
| 2i     | S. Angelo 1987e88 | 21/4e26/5 | 0.12                                                             | 0.15      | <br>26                     | 17.1                            |
| 2j     | Lodi 1996e97      | 28/4e16/5 | 0.26                                                             | 0.17      | 37                         | 17.1                            |

Percent model error is positive in case of underestimation, negative for overestimation.

a AGB is aboveground biomass.

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

Fig. 4. Comparison of the relationship between average air temperature and the effect on radiation-dependent biomass accumulation proposed by CropSyst (linear) and by [Yan and Hunt (1999)](#page-12-0) (logistic).

#### 4. Conclusions

The cropping systems simulation model CropSyst could be satisfactorily parameterized for winter wheat by using existing experimental data collected for purposes other than modelling and the wide range of available literature. The set of crop parameters obtained allowed reasonable estimates of aboveground biomass, plant nitrogen concentration and plant nitrogen uptake at different times during spring crop growth, for various locations/years/treatments in northern Italy. The simulated values were characterized by different estimation errors (in the range 6e40%). A systematic underestimation of aboveground biomass could not be corrected without the use of unreasonable model inputs. Ranking of model results was similar to that of measured values; in particular, crop response to model inputs (radiation, temperature, N fertilizer application) was correctly simulated.

This suggests that the proposed set of crop parameters, while still sub-optimal, can be used for scenario simulations in the study area and in similar locations. Also, this work shows how the increasing need of realistic model parameters can be partly satisfied by properly combining calibration of separate simulation modules, existing data sets collected during traditional agronomic experiments and extensive literature review.

#### References

- Abbate, P.E., Andrade, F.H., Culot, J.P., Bindraban, P.S., 1997. Grain yield in wheat: effects of radiation during spike growth period. Field Crops Research 54, 245e257.
- Acutis, M., Ducco, G., Grignani, C., 2000. Stochastic use of LEACHN model to forecast nitrate leaching in different maize cropping systems. European Journal of Agronomy 13, 191e206.
- Allen, R.G., Pereira, L.S., Raes, D., Smith, M., 1998. Crop Evapotranspiration - Guidelines for Computing Crop Water Requirements - FAO Irrigation and Drainage Paper 56. FAO e Food and Agriculture Organization of the United Nations, Rome.
- Amir, J., Sinclair, T.R., 1991. A model of water limitation on spring wheat growth and yield. Field Crops Research 28, 59e69.
- Amir, J., Sinclair, T.R., 1996. A straw mulch system to allow continuous wheat production in an arid climate. Field Crops Research 47, 21e31.
- Badini, O., Sto¨ckle, C.O., Franza, E.H., 1997. Application of crop simulation modeling and GIS to agroclimatic assessment in Burkina Faso. Agriculture, Ecosystems and Environment 64, 233e244.
- Bechini, L., Bocchi, S., Maggiore, T., 2003. Spatial interpolation of soil physical properties for irrigation planning. A simulation study in Northern Italy. European Journal of Agronomy 19, 1e14.
- Bechini, L., Borreani, G., Tabacco, E., 2001. Maximum, minimum and critical N concentration curves for Italian ryegrass. In: Proceedings of the Second International Symposium ''Modelling Cropping Systems''. Florence, 16e18 July, 2001, Italy, pp. 45e46.
- Bellocchi, G., Silvestri, N., Mazzoncini, M., Menini, S., 2002. Using the CropSyst model in continuous rainfed maize (Zea mais L.) under alternative management options. Italian Journal of Agronomy 6, 43e56.
- Bindraban, P.S., 1999. Impact of canopy nitrogen profile in wheat on growth. Field Crops Research 63, 63e77.
- Bocchi, S., Confalonieri, R., Genovese, G., Mariani, L., Martin, S., Orlandi, S., 2003. An integrated rice yield forecasting system in Europe. In: CD of Proceedings of the Third International Temperate Rice Conference. 10e13 March, Punta del Este e Uruguay.
- Bonhomme, R., Derieux, M., Edmeades, G.O., 1994. Flowering of diverse maize cultivars in relation to temperature and photoperiod in multilocation field trials. Crop Science 34, 156e164.
- Confalonieri, R., Bechini, L., 2004. A preliminary evaluation of the simulation model CropSyst for alfalfa. European Journal of Agronomy 21, 223e237.
- Confalonieri, R., Bocchi, S. Evaluation of CropSyst for simulating the yield of flooded rice in northern Italy. European Journal of Agronomy, in press.
- Confalonieri, R., Maggiore, T., Bechini, L., 2001. Application of the simulation model CropSyst to an intensive forage system in northern Italy, Second International Symposium ''Modelling Cropping Systems''. European Society for Agronomy, pp. 59e60.
- Confalonieri, R., Scaglia, B., 2002. CoLiDaTa User's Manual. Department of Crop Science, University of Milan, Milan, Italy.
- Donatelli, M., Acutis, M., Danuso, F., 2003. Valutazione dei modelli di simulazione. Quaderno PANDA n. 2. Mobilita` dei prodotti fitosanitari nel suolo. Agricoltura e Ricerca 190, 75e97.
- Donatelli, M., Acutis, M., Danuso, F., Mazzetto, F., Nasuelli, P., Nelson, R., Omicini, A., Speroni, M., Trevisan, M., Tugnoli, V., 2002. Integrated procedures for evaluating technical, environmental and economical aspects in farms: the SIPEAA project. In: Villalobos, F.J., Testi, L. (Eds.), Book of Proceedings of the Seventh Congress of the European Society for Agronomy. Cordoba, Spain, 15e18 July 2002, pp. 271e272.
- Donatelli, M., Sto¨ckle, C.O., Ceotto, E., Rinaldi, M., 1997. Evaluation of CropSyst for cropping systems at two locations of northern and southern Italy. European Journal of Agronomy 6, 35e45.
- FAOSTAT data, 2004. !<http://faostat.fao.org/faostat/collections>O, (accessed March 30, 2005).
- Fila, G., Bellocchi, G., Acutis, M., Donatelli, M., 2003. IRENE_DLL: a class library for evaluating numerical estimates. Agronomy Journal 95, 1330e1333.
- Flystra, D., Lasdon, L., Watson, J., Waren, A., 1998. Design and use of the Microsoft Excel Solver. Interfaces 28, 29e55.
- Giardini, L., Berti, A., Morari, F., 1998. Simulation of two cropping systems with EPIC and CropSyst models. Italian Journal of Agronomy 2, 29e38.
- Go¨mann, H., Kreins, P., Kunkel, R., Wendland, F., 2005. Model based impact analysis of policy options aiming at reducing diffuse

<span id="page-12-0"></span>pollution by agriculture e a case study for the river Ems and a subcatchment of the Rhine. Environmental Modelling and Software 20, 261e271.

- Goudriaan, J., van Laar, H., 1994. Modelling Potential Crop Growth Processes. Kluwer, Dordrecht, The Netherlands, 238 pp.
- Grubbs, F.E., 1969. Procedures for detecting outlying observations in samples. Technometrics 11, 1e21.
- ISO 5725-2, 1994. Accuracy (Trueness and Precision) of Measurement Method and Results e Part 2: Basic Method for the Determination of Repeatability and Reproducibility of a Standard Measurement Method. International Organization for Standardization, Gene`ve, Switzerland, 42 pp.
- Johnsson, H., Larsson, M., Ma˚rtensson, K., Hoffmann, M., 2002. SOILNDB: a decision support tool for assessing nitrogen leaching losses from arable land. Environmental Modelling and Software 17, 505e517.
- Justes, E., Mary, B., Meynard, J.M., Machet, J.M., Thelier-Huche´, L., 1994. Determination of a critical nitrogen dilution curve for winter wheat crops. Annals of Botany 74, 397e407.
- Kiniry, J.R., Jones, C.A., O'Toole, J.C., Blanchet, R., Cabelguenne, M., Spanel, D.A., 1989. Radiation-use efficiency in biomass accumulation prior to grain-filling for five grain-crop species. Field Crops Research 20, 51e64.
- Lewis, D.R., McGechan, M.B., McTaggart, I.P., 2003. Simulating field-scale nitrogen management scenarios involving fertiliser and slurry applications. Agricultural Systems 76, 159e180.
- Loague, K.M., Green, R.E., 1991. Statistical and graphical methods for evaluating solute transport models: overview and application. Journal of Contaminant Hydrology 7, 51e73.
- Monteith, J.L., 1977. Climate and the efficiency of crop production in Britain. Philosophical Transactions of Royal Society of London B 281, 277e294.
- Olesen, J.E., Berntsen, J., Hansen, E.M., Petersen, B.M., Petersen, J., 2002. Crop nitrogen demand and canopy area expansion in winter wheat during vegetative growth. European Journal of Agronomy 16, 279e294.
- Pannkuk, C.D., Sto¨ckle, C.O., Papendick, R.I., 1998. Evaluating CropSyst simulations of wheat management in a wheat-fallow region of the US Pacific Northwest. Agricultural Systems 57, 121e134.
- Peralta, J.M., Sto¨ckle, C.O., 2001. Dynamics of nitrate leaching under irrigated potato rotation in Washington State: a long-term simulation study. Agriculture, Ecosystems and Environment 88, 23e34.
- Ple´net, D., Lemaire, G., 1999. Relationships between dynamics of nitrogen uptake and dry matter accumulation in maize crops. Determination of critical N concentration. Plant and Soil 216, 65e82.
- Porter, J.R., Gawith, M., 1999. Temperatures and the growth and development of wheat: a review. European Journal of Agronomy 10, 23e36.
- Rossing, W.A.H., Meynard, J.M., Van Ittersum, M.K., 1997. Modelbased explorations to support development of sustainable farming systems: case studies from France and the Netherlands. European Journal of Agronomy 7, 271e283.
- Sinclair, T.R., Amir, J., 1992. A model to assess nitrogen limitations on the growth and yield of spring wheat. Field Crops Research 30, 63e78.
- Sinclair, T.R., Muchow, R.C., 1999. Radiation use efficiency. Advances in Agronomy 65, 215e265.
- Slafer, G.A., Rawson, H.M., 1995. Rates and cardinal temperatures for processes of development in winter wheat: effects of temperature and thermal amplitude. Australian Journal of Plant Physiology 22, 913e926.
- Sousa, V., Pereira, L.S., 1999. Regional analysis of irrigation water requirements using kriging. Application to potato crop (Solanum tuberosum L.) at Tra´s-os-Montes. Agricultural Water Management 40, 221e233.
- Sto¨ckle, C.O., Debaeke, P., 1997. Modeling crop nitrogen requirements: a critical analysis. European Journal of Agronomy 7, 161e169.
- Sto¨ckle, C.O., Donatelli, M., Nelson, R., 2003. CropSyst, a cropping systems simulation model. European Journal of Agronomy 18, 289e307.
- Sto¨ckle, C.O., Martin, S.A., Campbell, G.S., 1994. CropSyst, a cropping systems simulation model: water/nitrogen budgets and crop yield. Agricultural Systems 46, 335e359.
- Tanner, C.B., Sinclair, T.R., 1983. Efficient water use in crop production: research or re-search? In: Taylor, H.M., Jordan, W.R., Sinclair, T.R. (Eds.), Limitations to Efficient Water Use in Crop Production. American Society of Agronomy, Madison, WI, pp. 1e27.
- Tei, F., Benincasa, P., Guiducci, M., 2001. Determination of a critical nitrogen dilution curve for processing tomato. In: Proceedings of the Second International Symposium ''Modelling Cropping Systems''. Florence, 16e18 July, 2001, Italy, pp. 33e34.
- Ten Berge, H.F.M., Van Ittersum, M.K., Rossing, W.A.H., Van de Ven, G.W.J., Schans, J., Van de Sanden, P.A.C.M., 2000. Farming options for The Netherlands explored by multi-objective modelling. European Journal of Agronomy 13, 263e277.
- Wise, R., Cacho, O., 2005. Treeecrop interactions and their environmental and economic implications in the presence of carbon-sequestration payments. Environmental Modelling and Software 20, 1139e1148.
- Wolf, J., Beusen, A.H.W., Groenendijk, P., Kroon, T., Ro¨tter, R., van Zeijts, H., 2003. The integrated modeling system STONE for calculating nutrient emissions from agriculture in the Netherlands. Environmental Modelling and Software 18, 597e617.
- Yan, W., Hunt, L.A., 1999. An equation for modelling the temperature response of plants using only the cardinal temperatures. Annals of Botany 84, 607e614.
- Yin, X., Kropff, M.J., McLaren, G., Visperas, R.M., 1995. A non linear model for crop development as a function of temperature. Agricultural and Forest Meteorology 77, 1e16.
- Yunusa, I.A.M., Siddique, K.H.M., Belford, R.K., Karimi, M.M., 1993. Effect of canopy structure on efficiency of radiation interception and use in spring wheat cultivars during the preanthesis period in a Mediterranean-type environment. Field Crops Research 35, 113e122.