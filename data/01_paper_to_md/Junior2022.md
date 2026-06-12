![](_page_0_Picture_1.jpeg)

Contents lists available at [ScienceDirect](www.sciencedirect.com/science/journal/11610301) 

European Journal of Agronomy

![](_page_0_Picture_4.jpeg)

journal homepage: [www.elsevier.com/locate/eja](https://www.elsevier.com/locate/eja)

# Assimilating leaf area index data into a sugarcane process-based crop model for improving yield estimation

![](_page_0_Picture_7.jpeg)

Izael Martins Fattori Junior a,* , Murilo dos Santos Vianna b , Fabio ´ Ricardo Marin a

a *University of Sao* ˜ *Paulo, "Luiz de Queiroz" College of Agriculture (Esalq), Piracicaba, SP, Brazil* b *Institute of Crop Science and Resource Conservation (INRES), University of Bonn, Bonn 53111, Germany* 

## ARTICLE INFO

*Keywords:*  Ensemble Kalman filter Ensemble smoother Weighted mean DSSAT/SAMUCA

#### ABSTRACT

The ability to estimate sugarcane yield is an important factor to improving the planning capacity of public and private sectors, and so food and energy security. One way of achieving this is by employing process-based crop models (PBM), which can be coupled to data assimilation (DA) algorithms to correct predictions along the crop season. While the application of PBMs often need careful parameterization or genotype-specific parameters, few studies focus on understanding the impacts of crop parametrization with different crop genotypes with DA. Moreover, dimensioning the number and timing of observations is key to effectively improve predictions with DA. This study assess the performance of a new sugarcane PBM (DSSAT/SAMUCA) coupled to three DA methods, and when the genotype-specific parameters are available or not. Data from 22 field experiments is utilized to compare the performance of using the ensemble Kalman filter (EnKF), ensemble smoother (ES) and weighted mean (WM) for assimilating leaf area index (LAI) to improve yields estimates. We also quantify the impact of using one genotype-specific calibration (cv. RB867515) on yield predictions of four non-calibrated genotypes (cv. NCo376, SP832847, R570, RB72454). Simulations of DA methods had better performance than employing the PBM without DA, so called open-loop (OP). The ES method resulted in the best performance (R2 = 0.498 and RMSE = 20.268 Mg ha− 1 ) followed by EnKF and WM. Utilizing a genotype-specific calibration showed substantially smaller RMSE for the three DA methods (EnKF = 16.76, ES = 16.70 and WM = 15.36 Mg ha− 1 ) compared to non-calibrated (EnKF = 21.44–26.23, ES = 21.50–26.27 and WM = 23.38–28.37 Mg ha− 1 ). Nevertheless, we also verified a higher improvement of model performance when applying EnKF and ES method to experiments where the cultivar does not match the genotype-specific calibration employed. While the WM had the opposite results, with the calibrated cultivar showing a higher improvement of model performance. As the number of LAI data assimilation increases, the DA methods tend to outperform the OP, but observations at late crop phenological stage of development showed a higher positive influence on SFY predictions.

# **1. Introduction**

Sugarcane yield estimations are key for agricultural development and planning in public and private sectors, and so to food and energy security as the crop is a major feedstock of sugar and ethanol. Brazil is the largest sugarcane producer in the world, accounting for ca. 40% of the global production, and ca. 50% of global sugar exports ([FAO, 2019)](#page-10-0). It is also the second largest ethanol producing country after the USA, thus sugarcane production chain is crucial for food security and for the country's energy matrix production ([Goldemberg et al., 2014)](#page-10-0).

Sugarcane grown in Brazil shows a great seasonal and spatial yield variability ([Marin et al., 2008; Marin and de Carvalho, 2012)](#page-11-0), which can be attributed to interannual climate variability, pests and diseases, soil fertility, as well as to the intensive sequential harvesting practice (e.g. ratooning) ([Lisboa et al., 2018; Marin et al., 2019, 2021](#page-11-0)). Thus, the significance of Brazil's production and the yield variability emphasizes the importance of accurate crop yield predictions for assisting decision-makers and ensuring better market planning and regulation ([Marin, 2016](#page-11-0)).

Process-based crop models (PBM) are widely used tools to predict crop yield as a product of Genotype × Environment × Management interactions ([Wang et al., 2019](#page-11-0)). These models consist of organized algorithms that describe physical and biological processes that occur in crop growth and development, and so mimic the interactions among

* Corresponding author. *E-mail address:* [Izael.fattori@usp.br](mailto:Izael.fattori@usp.br) (I.M. Fattori Junior).

<https://doi.org/10.1016/j.eja.2022.126501>

Available online 22 March 2022 1161-0301/© 2022 Elsevier B.V. All rights reserved. Received 20 August 2021; Received in revised form 5 February 2022; Accepted 9 March 2022 soil, plant, and atmosphere components ([Jones et al., 2017)](#page-11-0). For sugarcane, several PBMs were developed and evaluated against observed data across the world, such as AUSCANE [(Jones et al., 1989](#page-11-0)); CANEGRO ([Inman-Bamber and Thompson, 1989; Singels et al., 2008)](#page-11-0); QCANE ([Liu](#page-11-0) [and Kingston, 1995)](#page-11-0); APSIM ([Holzworth et al., 2014; Keating et al.,](#page-10-0)  [2003)](#page-10-0); MOSICAS (Martin´[e, 2003)](#page-11-0); SAMUCA [(Marin and Jones, 2014;](#page-11-0)  [Marin et al., 2017; Vianna et al., 2020)](#page-11-0); and CASUPRO ([Villegas et al.,](#page-11-0)  [2005)](#page-11-0). The DSSAT/SAMUCA (DS) model considers physiological processes such as biomass partitioning at phytomer level and canopy carbon assimilation using leaf assimilation rates and carboxylation efficiency. Furthermore, DS was recently updated and evaluated considering the effect of the green cane trash blanket effect, an arising management practice in Brazil [(Vianna et al., 2020)](#page-11-0).

The deterministic approach employed in most PBMs generally relies on a substantial amount of input data and coefficients to characterize the soil-plant-atmosphere and management system. This information is sometimes difficult to be determined and may vary within the spatial and temporal domain, transferring this uncertainty to simulations of crop yields ([Marin et al., 2017; Zhao et al., 2013](#page-11-0)). In addition, PBMs are not yet ready to account for the reduction factors in yield simulations because of the high complexity in measuring the various biotic and abiotic interactions, which is generally accounted as an empirical yield-gap factor ([Van Ittersum et al., 2003;](#page-11-0) [Lobell et al., 2009](#page-11-0)). For instance, biotic factors such as pests and diseases, lodging, and storms can damage the sugarcane canopy by reducing the leaf area index (LAI), which is not well simulated by most of available PBMs ([Hu et al., 2019)](#page-11-0). Such factors considerably affect two key crop physiological processes: (i) plant canopy light interception and potential photosynthesis; and (ii) soil water content and evapotranspiration, which in turn determine the actual photosynthesis rate ([de Wit and van Diepen, 2007](#page-11-0)).

An option to reduce uncertainty in yield prediction by PBMs is the use of data assimilations methods (DA) that incorporate observations into the PBM simulations, to produce more accurate estimates of state variables ([Huang et al., 2019)](#page-11-0). In this regard, updating methods are among the most used tools because they are computationally less expensive and capable of accounting for both model and observation uncertainty ([Ines et al., 2013](#page-11-0)). The most used update method is the Ensemble Kalman filter (EnKF) (Kang and Ozdo ¨ gan, ˘ [2019; Pan et al.,](#page-11-0)  [2019)](#page-11-0), a Bayesian approach of the Monte Carlo method developed by [Evensen (2003)](#page-10-0), which sequentially accounts for uncertainties from crop simulation and measured data ([Xie et al., 2017)](#page-11-0).

The EnKF is flexible and fits well with PBMs frameworks but updating only a few state variables may affect the model integrity and cause undesired model states in some circumstances ([Nearing et al.,](#page-11-0)  [2012; Tewes et al., 2020a)](#page-11-0). To overcome such limitations, other DA methods were proposed such as the weighted mean (WM), which can account for observational errors without changing the PBM state variables ([Tewes et al., 2020a](#page-11-0)). A third DA is the ensemble smoother (ES), which uses similar assumptions of EnKF, but assimilates all available observations simultaneously, ensuring consistency between the PBM state variables and DA state vector ([Lee et al., 2016; Van Leeuwen and](#page-11-0)  [Evensen, 1996; Yu et al., 2020](#page-11-0)).

Recently, DA methods were tested for sugarcane crop models through LAI, soil moisture and plant height data assimilation, for all showed improved crop growth simulations, mainly in water-limited environments ([Hu et al., 2019; Yu et al., 2020](#page-11-0)). However, these two previous studies used the PBM SWAP-WOFOST adapted for sugarcane ([Supit et al., 1994; van Dam et al., 1997)](#page-11-0), which lacks the representation of some key physiological and morphological process, such as tillering and sucrose accumulation. Thus, a more generalist PBM is more practical for applying DA due to the lower number of parameters and simplicity of the plant process included [(Kang and Ozdo](#page-11-0) ¨ gan, ˘ 2019). Crop-specific PBMs, like those available in the DSSAT platform, have more detailed descriptions of plant physiological processes, which may lead to less uncertain simulations ([Jones and Singels, 2018; Vianna](#page-11-0)  [et al., 2020)](#page-11-0). Nevertheless, the use of DA in such sophisticated models may also cause model inconsistency due to the model's complexity and the number of parameters involved ([Nearing et al., 2012)](#page-11-0).

Moreover, due to the difficulty of quantifying the variability of genotypes in large areas, this information is commonly resumed to just one calibration in DA simulations ([Huang et al., 2016; Tewes et al., 2020a](#page-11-0)). [Lu et al. (2021)](#page-11-0) proposed a framework to use the EnKF to simulate Maize, without using a specific genotype calibration and presented satisfactory improvement compared to open-loop (OP) simulations. However, recent studies emphasized that calibrating the model parameters that are specific for cultivar or region should be targeted before DA methods ([Huang et al., 2021)](#page-11-0), and this should be more stressed in crop-specific PBM, due to a large number of parameters to describe the crops cultivar ([Kang and Ozdo](#page-11-0) ¨ gan, ˘ 2019). To our knowledge, no other studies explored how the use of one genotype-based calibration for sugarcane, affected other cultivars on DA methods performance. This study aimed to assess the performance of using crop specific PBM in conditions of no or indirect calibrations based on sugarcane cultivars, and also analyses other factors that could impact the PBM performance, e.g. the amount and timing of LAI observations. To fill this knowledge gap, we developed a framework to assimilate sugarcane LAI measurements in the DS model using three different DA methods: EnKF, ES, and WM. A dataset of field experiments conducted with five cultivars in a diversity of soils and climates across Brazil was utilized, part of them to calibrate the DS for the cultivar RB867515, and other to evaluate and compare the three techniques in estimating stalk fresh yield (SFY).

## **2. Material and methods**

## *2.1. Field experiments description*

In total, we used a dataset of 22 experiments described in [Table 1](#page-2-0). Experiments 1–3 were conducted at the College of Agriculture "Luiz de Queiroz" (Esalq) of University of Sao ˜ Paulo (USP) in Piracicaba, Brazil (Lat. 22◦41′ 55′′ S, long. 47◦38′ 34′′ W, alt. 540 m a.m.s.l.). Chopped stalks of the RB867515 cultivar (Exps. 1 and 2) were used for planting 13–15 buds m− 1 at 1.4 m row spacing down to a depth of 0.2 m. Experiment 3 was conducted in the first ratoon of experiment 1 (sugarcane re-growth). Agricultural practices were adopted to represent high-yield farming systems and to ensure the crop was free from pests, diseases, and nutritional stress. The climate is characterized by a hot and humid summer with dry winter (Cwa - Koppen ¨ classification), and the soil of the three experiments is classified as Typic Hapludox. For these experiments, daily solar radiation, maximum and minimum air temperature, rainfall, wind speed, and relative air humidity were collected adjacent to the experiment site using an automatic weather station. The experimental area was irrigated by a center-pivot. The water balance was monitored to manage the water applications and ensure crops were not exposed to water stress throughout the growing cycle; for these, irrigation was triggered every time the soil moisture reached 80% of the total available soil water. Five locations were randomly selected at the beginning of each season, where LAI samples were taken with an LAI-2200 instrument (LI-COR Bioscience), following user manual recommendations for row crops ([Gonçalves et al., 2020)](#page-10-0). LAI measurements were taken in a frequency of 5–20 days in experiments 1–3. Stalk fresh yield (SFY, Mg ha− 1 ) was measured only at the end of the crop season by mechanical harvesting for the three experiments. Experiments 1 and 2 during the crop season suffered from lodging, after heavy rain events and after the crop reaches a high SFY and stalks height. This caused changes in LAI during the season and accelerate the decrease in LAI at the late stage.

We also used experimental data of previous studies (Experiments 4–22, [Table 1](#page-2-0)) conducted in a diversity of environments and using different cultivars ([Marin et al., 2015, 2011; Suguitani, 2006; Vianna](#page-11-0)  [et al., 2020)](#page-11-0), and following a similar protocol of the experiments 1–3 above described. Experiments 4–15 had the LAI sampled 1–7 times during the crop season, and SFY sampled only at the end of the crop

## <span id="page-2-0"></span>**Table 1**

|  | Description of experimental datasets used in the simulations. Only experiments 16–22 were used for model calibration. |  |  |
|--|-----------------------------------------------------------------------------------------------------------------------|--|--|
|--|-----------------------------------------------------------------------------------------------------------------------|--|--|

| Experiment<br>Number | Location                                      | Planting<br>date       | Harvest<br>date        | Planting<br>Type      | Weather†                 | Soil‡                      | Water<br>treatment | Variety  | Ref.          |
|----------------------|-----------------------------------------------|------------------------|------------------------|-----------------------|--------------------------|----------------------------|--------------------|----------|---------------|
| 1                    | Piracicaba/SP 22◦41' S,<br>47◦38'W, 560 m     | 10/05/<br>2018         | 11/30/<br>2019         | Plant                 | 21.6 ◦C, 1230<br>mm, CWa | Typic<br>Hapludox          | Irrigated          | RB867515 | ¥             |
| 2                    |                                               | 11/06/                 | 11/30/                 | Plant                 |                          | Typic                      | Irrigated          | RB867515 |               |
| 3                    |                                               | 2018<br>11/31/         | 2019<br>11/04/         | 1st                   |                          |                            | Irrigated          | RB867515 |               |
| 4                    |                                               | 2019<br>10/29/         | 2020<br>07/15/         | Ratoon*<br>Plant      |                          |                            | Irrigated          | R570     | Suguitani     |
| 5                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | R570     | (2006)        |
| 6                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Irrigated          | RB72454  |               |
| 7                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | RB72454  |               |
| 8                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Irrigated          | SP832847 |               |
| 9                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | SP832847 |               |
| 10                   |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Irrigated          | NCo376   |               |
| 11                   |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | NCo376   |               |
| 12                   | Aparecida do Taboado/MS                       | 2004<br>07/01/         | 2005<br>09/08/         | Plant                 | 23.5 ◦C, 1560            | Typic                      | Rainfed            | RB867515 | Marin et al.  |
|                      | 20◦05 S, 51◦18′<br>W, 335 m                   | 2006                   | 2007                   |                       | mm, Aw                   | Hapludox<br>Typic          |                    |          | (2015)        |
| 13                   | Colina/SP 20◦25′<br>S,<br>48◦19′<br>W, 590 m  | 02/10/<br>2004         | 06/15/<br>2005         | Plant                 | 22.8 ◦C, 1363<br>mm, Cwa | Typic<br>Hapludox          | Rainfed            | RB867515 |               |
| 14                   | Olimpia/SP 20◦26′<br>S,<br>48◦32′<br>W, 500 m | 02/10/<br>2004         | 06/15/<br>2005         | Plant                 | 23.3 ◦C, 1349<br>mm, Cwa | Typic<br>Typic<br>Hapludox | Rainfed            | RB867515 |               |
| 15                   | Coruripe/AL 10◦07′<br>S,                      | 08/16/                 | 09/15/                 | Plant                 | 21.6 ◦C, 1401            | Typic<br>Fragiudult        | Rainfed            | RB867515 |               |
| 16                   | 36◦10'W, 16 m<br>Piracicaba/SP 22◦41' S,      | 2005<br>12/06/         | 2006<br>10/15/         | Plant                 | mm, As<br>21.6 ◦C, 1230  | Typic<br>Typic             | Irrigated          | RB867515 | Vianna et al. |
| 17                   | 47◦38'W, 560 m                                | 2012<br>10/15/         | 2013<br>07/15/         | 1st                   | mm, CWa                  | Hapludox<br>Typic          | Irrigated          | RB867515 | (2020)        |
| 18                   |                                               | 2013<br>10/15/         | 2014<br>07/15/         | Ratoon*<br>1st Ratoon |                          |                            | Irrigated          | RB867515 |               |
| 19                   |                                               | 2013<br>07/15/         | 2014<br>06/08/         | 2nd                   |                          |                            | Irrigated          | RB867515 |               |
| 20                   |                                               | 2014<br>07/15/         | 2015<br>06/08/         | Ratoon*<br>2nd        |                          |                            | Irrigated          | RB867515 |               |
| 21                   |                                               | 2014<br>06/08/         | 2015<br>06/08/         | Ratoon<br>3rd         |                          |                            | Irrigated          | RB867515 |               |
| 22                   |                                               | 2015<br>06/08/<br>2015 | 2016<br>06/08/<br>2016 | Ratoon*<br>3rd Ratoon |                          |                            | Irrigated          | RB867515 |               |

† Respectively: mean annual temperature, annual total rainfall, Koeppen Classification.

‡ U.S. Soil Taxonomy.

¥ Experimental data collected for this study and not previously published.

* With mulch cover.

season. The experiments 16–22 were only used for DS calibrations and had tiller population, stalk diameter, stalk height, LAI, SFY, stalk, and leaf dry mass, and sucrose content on fresh cane basis (POL) obtained by regular sampling ([Vianna et al., 2020](#page-11-0)).

Soil characteristics and management practices such as planting and harvesting dates, row spacing, mulch cover and irrigation applications (mm d− 1 ) on each site were prescribed to the model as input information. Also, for experiments 3, 17, 19 and 21 a total of 12 Mg ha− 1 of green cane straw were considered for simulations. All other experiments were conducted at bare soil conditions.

The experiments 1–3 and 16–22 had the LAI sampled with the LAI-2200 and LAI-2000 respectively, which had an accuracy of 4%, according to the user manual ([Gonçalves et al., 2020)](#page-10-0). The other experiments had their LAI sampled with different sensors and methodology ([Marin et al., 2015, 2011; Suguitani, 2006)](#page-11-0); to maintain the response of the DA methods with the DS, we assumed the same accuracy for all observations.

# *2.2. Brief description of DSSAT/SAMUCA and calibration process*

The SAMUCA model is a PBM firstly developed by [Marin and Jones](#page-11-0)  [(2014)](#page-11-0), which is capable to simulate the growth and development of sugarcane crop, implementing an algorithm to describe processes related to phenology, canopy development, tillering, biomass accumulation, root growth, and water stress ([Marin et al., 2017](#page-11-0)). [Vianna et al.](#page-11-0)  [(2020)](#page-11-0) improved the SAMUCA model by including recent scientific findings on sugarcane growth at phytomer level, canopy assimilation, and tillering. In this new version, the model was adapted to operate the one-dimensional "tipping bucket" soil water balance and to incorporate the soil temperature to account for the trash blanket effect on sugarcane growth and water use. This presented a superior performance compared with the previous version and was comparable to other widely used PBMs for sugarcane. For this study, we used the SAMUCA model incorporated into the Decision Support System for Agrotechnology Transfer (DSSAT) platform version 4.8 [(Jones et al., 2003; Hoogenboom](#page-11-0) 

[et al., 2019; Vianna et al., 2020)](#page-11-0), namely DSSAT/SAMUCA (DS).

The model was calibrated for cultivar RB867515 by [Vianna at al.](#page-11-0)  [(2020),](#page-11-0) using experiments 16–22. A routine was designed to find crop parameters that minimize simulation errors by means of the RMSE ([Wallach et al., 2018)](#page-11-0). To avoid unrealistic parameters estimation, the constrained BFGS ("Broyden–Fletcher–Goldfarb–Shanno") optimization method ([Byrd et al., 1996)](#page-10-0) was employed assigning plausible range of parameters based on field observation and literature. To adapt the plant-module of SAMUCA within the soil-plant-atmosphere framework of DSSAT, the root growth parameters SRLMAX (Specific Root Length at Root Front), SRLMIN (Specific Root Length at Inner Roots Profile), and DSHOOT_EXT (Below ground shoots expansion rate) were re-calibrated (Table S1). The procedure was performed by eye-fitting using the same set of observations employed by [Vianna et al. (2020)](#page-11-0) (experiments 16–22) for which we obtained similar performance (Table S2).

#### *2.3. Description of data assimilation procedure*

Three different updating methods of DA were investigated in this study: EnKF, ES, and WM, which are described below. Also, standard DS simulations without DA were performed, which are thereafter called open-loop (OP) simulations. For each DA, the ability to deal with LAI assimilation and their performance with DS simulations were assessed, by comparing the simulation results of SFY at the end of the crop cycle. Therefore, the DS was adapted to read an input file with a new estimated vector of state variables at any time, regardless of the method. When new LAI values were assimilated by DS, the leaf area and dry weight were also updated at phytomer and field level to ensure the consistency of canopy representation.

## *2.3.1. Ensemble Kalman filter method*

The EnKF employs an analytic solution based on two related sources of information, in this case: PBM's outputs and field observations. These are synthesized to provide a better estimation, with lower variance. For that, the EnKF assumes that the observed data can be related to the state variable *xt* (LAI in the case of this study) at time *t* as shown in Eq. (1):

$$\mathbf{y} = \mathbf{H}\mathbf{x}_t + \mathbf{e} \tag{1}$$

where y is the observations vector; *H* is the observation operator that relates to *y*; *ε* is a Gaussian random error vector with a mean of zero and observation error covariance *R*. Also, the forecast of *xt* at *t* = *k* is Gaussian with mean *xf t*=*k* and error covariance *Pf t*=*k*. Under these assumptions, the estimated state and error covariance (*P*) are updated as:

$$\mathbf{x}_{r=k}^{\mu} = \begin{array}{c} \mathbf{x}_{r=k}^{\circ} + \mathbf{K}(\mathbf{y}_{r=k} \quad -H\mathbf{x}_{r=k}^{\circ}) \end{array} \tag{2}$$

$$P_{t=k}^{*} = \quad (I - KH)P_{t=k}^{\ell} \tag{3}$$

where *t* is the time index; *k* is the time of the observed data; *f* represents the prior state (called forecast) and *a* is the posterior state (called analysis); *I* is the identity matrix; and *K* represents the Kalman gain calculated by Eq. (4):

$$\mathbf{K} = \quad \quad P_{t=k}^{\zeta} H^T \left( H P_{t=k}^{\zeta} H^T + \mathcal{R}_{t=k} \right)^{-1} \tag{4}$$

The EnKF forecast and analysis error covariance *Pf* come directly from an ensemble of the model simulations:

$$P^{\ell}H^{T} = \left(N_{\pi} - 1\right)^{-1} \sum_{n=1}^{N_{\pi}} \left(\mathbf{x}_{n}^{\ell} - \overline{\mathbf{x}}^{\ell}\right) \left(H\mathbf{x}_{n}^{\ell} - H\overline{\mathbf{x}}^{\ell}\right)^{T} \tag{5}$$

where *Ne* is the number of ensemble members, *n* is a running index for an ensemble member, and *xf* are the ensemble mean calculated as:

$$\overline{\mathbf{x}}' = \quad N_{\mathbf{e}}^{-1} \sum_{n=1}^{N_{\mathbf{e}}} \mathbf{x}_{n}' \tag{6}$$

In our study, we only used the LAI retrieved from ground

measurements as a state variable for DA methods. Thus, *H* can be taken as an identity matrix (*H* = 1), with that we can rewrite the Eqs. (2), (4) and (5) as Eqs. (7)–(9).

$$\mathbf{x}_{r=k}^{\boldsymbol{\mu}} = \mathbf{x}_{r=k}^{\boldsymbol{\ell}} + \mathbf{K} \left( \mathbf{y}_{r=k} - \mathbf{x}_{r=k}^{\boldsymbol{\ell}} \right) \tag{7}$$

$$K = \quad P_{t=k}^{\ell} \left( P_{t=k}^{\ell} + R_{t=k} \right)^{-1} \tag{8}$$

$$P^{\ell} = \quad \left(N_r - 1\right)^{-1} \sum_{n=1}^{N_r} \left(\mathfrak{x}_n^{\ell} - \quad \mathfrak{x}^{\ell}\right) \left(\mathfrak{x}_n^{\ell} - \quad \mathfrak{x}^{\ell}\right)^T \tag{9}$$

In EnKF, the observed data are perturbed with the Monte Carlo approach to generate an ensemble, based on the data uncertainty represented by the variance. When used together with PBMs, there are two methods to generate the ensemble members ([Zhuo et al., 2019)](#page-12-0): the first method adds a Gaussian perturbation to the PBM state variables output. The second, add a Gaussian perturbation to the model input parameters.

In this study, we used the second method to generate the ensemble members. Thus, we selected the most sensitive parameters to LAI based on a sensitivity analysis, using the Fourier amplitude sensitivity test (FAST) ([Cukier et al., 1973; Saltelli et al., 1999)](#page-10-0) from the SALlib library (<https://salib.readthedocs.io/en/latest/index.html>). These were MAXGL (maximum number of green leaves a tiller can hold), MLA (maximum leaf area), PLASTOCHRON (thermal time required for the appearance of one new phytomer), INIT_LF_AREA (initial leaf area of first appeared leaf), and MID_TT_LF_GRO (thermal time where leaves can achieve half of its maximum biomass) (Table S1). These parameters were then perturbed to generate an ensemble (40 members), with a gaussian distribution and an uncertainty level of 10% before the simulation starts, as recommended for [Ines et al. (2013)](#page-11-0) and [Curnel et al.](#page-10-0)  [(2011)](#page-10-0) to optimize the time of the simulation and model accuracy.

After generating the set of parameters, DS runs until the first observed LAI is available. At this point, we calculated in sequence *K* and the vector *xa t*=*k* (Eqs. (7) and (8)), that was considered the optimal estimation of LAI. This step also included small inflation of 1.5 for LAI in ensemble members, in the case of their variability becoming too low ([Ines et al., 2013)](#page-11-0). This step ensured that the observations were not systematically rejected during assimilation. After that, the estimated LAI is stored in an input file for the next simulations, and runs were re-initialized until the next observations became available.

# *2.3.2. Ensemble smoother method*

The ES has the same assumptions and equations as the EnKF. The difference between them is the number of assimilations. The ES assimilates all observed data at once, regardless of the acquisition time. Thus, the DS predicted all the state variables until the end of the simulations, using 40 ensemble members and considering the parameter perturbation procedure. At the prediction step, the DS output is then compared with all observations. For each observation, the Eqs. (7)–(9) were applied, and the term *xa t*=*k* was estimated. Thereafter, the DS was reinitialized and the *xa t*=*k* was assimilated at each time, which reduces the number of model re-initialization and made it easier to couple with any program that was not created to DA adaptation, like the majority of PBM ([Lee et al., 2016; Yu et al., 2020](#page-11-0)).

# *2.3.3. Weighted mean method*

The WM methodology follows the approach proposed by [Tewes et al.](#page-11-0)  [(2020a),](#page-11-0) which assumes that the PBMs OP ensemble simulation runs from the beginning to the end of the crop growing cycle. One or a few members of the PBMs simulations that were close to the observed variable receive a greater weight for the state vector estimation.

The same crop parameters used for EnKF and ES were used to create the ensemble members in this method. However, different from the other DA, a uniform distribution is assumed to create the 40 sets of parameters, and the maximum and the minimum values of the distribution range were assumed to be ± 10% of the selected parameters <span id="page-4-0"></span>mean value (Table S1). After the ensemble simulations run, a Python script reads the output file of the DS and performs the WM calculation as follows.

To predict the state *X*̂(*t*) of the system, we used the weighted mean of the ensemble *Xi*(*t*):

$$\widehat{X}(t) = \begin{array}{c} \frac{\sum_{i=1}^{N} \boldsymbol{w}_{i}(t)X_{i}(t)}{\sum_{i=1}^{N} \boldsymbol{w}_{i}(t)} \end{array} \tag{10}$$

where each weight *w* of ensemble member *i* at day *t* is calculated as follow:

$$\rho_i(t) = P(O(t_k)|X_i(t_k)) \quad \text{for} \quad t_k \quad \le t \quad \le \quad t_{k+1} \tag{11}$$

where *P* is the likelihood from that the observational *O* at time *tk* approximates the simulated value. The observational error was assumed as a normal distribution, where *O*(*tk*) is mean and *σk* the standard deviation of the distribution. Thus, we applied the following equation for the calculation of the likelihood *P*:

$$P(O(t_k)|X_i(t_k)\ ) = \frac{1}{\sqrt{2\pi\sigma_k^2}} \exp\left(-\frac{\left(h(\left(t_k\right)) - \quad O(t_k)\right)^2}{\sigma_k^2}\right) \tag{12}$$

where *h* mapped the states to the observational variables.

The calculated weights for the first observation were then propagated until the next observation, and they were also used to calculate the weighted mean of other state variables. For example, the SFY retrieved from the simulation members that have LAI closer to the observations will receive more weight. When a new observation is available, the weighted mean is recalculated, and when observations were outside the ensemble members, the entire weights were given to the closest member. Contrary to other existing DA updating methods, no state variables are updated during the simulation runs. Therefore, observations are used to select the output simulations' members of the PBM, not change the state variable directly in the PBM, during the run, which is common for the other DA methods.

## *2.4. Data analysis*

The performance of each DA was evaluated by comparing simulated and observed SFY by using root mean squared error (RMSE) and coefficient of determination (R2 ). We also compared each DA with OP simulation to select the best approach for each experiment. It should be noted that we used the absolute error (AE) to compare the SFY at the end of the crop cycles for each experiment. To quantify if and how much each DA method reduced the SFY simulation error, the difference between the AE of three DA methods against the AE of OP simulations is calculated. Negative differences between DA and OP error, indicate better performance in DA method than the OP simulation.

## *2.5. Effect of genotype-specific calibration on DA methods*

The DS model was previously calibrated and evaluated for the RB867515 cultivar, with experiments 16–22 ([Table 1)](#page-2-0). This cultivar is one of the main Brazilian cultivars present in more than 20% of sugarcane plantations in Brazil [(Vianna et al., 2020](#page-11-0)); and which is also present in seven of the fifteen field experiments not utilized in the calibration procedure [(Table 1)](#page-2-0). The remaining experiments (4–11) used four different cultivars, where three were also commonly planted in Brazil (R570, RB72454, and SP832847). The NCo376 is one of the main South African cultivars for which the DSSAT/Canegro model was extensively tested ([Marin et al., 2011; Singels et al., 2008)](#page-11-0).

Therefore, this analysis aimed to investigate the influence of assimilating data from different genotypes but considering fixed crop parameters previously calibrated for the RB867515 cultivar. For that, we performed simulations for OP and three DA methods (EnKF, ES, and

WM) using the same calibration for all experiments (Table S1). The effect of employing genotype-specific calibration was then evaluated by grouping the experiments by cultivar type and comparing the RMSE of the cultivar group with the calibrated cultivar (RB867515). This resulted in two groups of experiments: (i) the experiments with cultivar RB867515, considering in this group only those not directly used for calibration (1–3 and 12–15); (ii) the experiments with different cultivars, with no genotype-specific calibration. These results provide practical information to whether PBMs must be calibrated prior to being used with DA methods across cultivars, and what is the level of uncertainty of this procedure.

## *2.6. Effect of the number and timing of observations on DA methods*

To assess the impact of number and timing of LAI observations on the performance of SFY simulations, we ran a simulation experiment omitting and prescribing LAI observations to DA methods at different combinations of crop developmental stages. We divided the crop cycle in three main stages: stage 1 – early stage of development from planting to the maximum number of tillers; stage 2 – medium stage of development from a maximum number of tillers to the maximum LAI; and stage 3 – late stage of development from maximum LAI to harvest. Seven study cases scenarios were tested (Table 2) considering these three stages. Cases 1–3 assimilated LAI observations from only one specific stage. For verifying the relationship between crop stages, we performed study cases 4–6, which grouped LAI observations two at a time. Finally, we simulated DAs considering all observations (Case 7). For this analysis, we only used experiments 1 and 2 ([Table 1](#page-2-0)), because they presented enough observations in each stage, different from the other experiments. For each stage of development, we used only four observations, to maintain the same number of observations for all stages (Table S3).

## **3. Results**

## *3.1. Influence of using fixed crop parameters in the performance of DA methods across different cultivars*

The RMSE simulated by the DS model with OP and three DA methods was grouped by cultivar ([Table 3](#page-5-0)). Amongst the DA methods, the WM had the best accuracy for the calibrated cultivar (RB867515) (RMSE = 15.36 Mg ha− 1 ), followed by ES (RMSE = 16.70 Mg ha− 1 ) and EnKF (RMSE = 16.76 Mg ha− 1 ) ([Table 3](#page-5-0)). For the other cultivars, the WM presented a lower accuracy compared to EnKF and ES. Between EnKF and ES, the RMSE per cultivars were very similar ([Table 3](#page-5-0)).

For the OP simulations, our results showed that the calibrated cultivar (RB867515), had the best accuracy for OP simulations (RMSE = 19.94 Mg ha− 1 ), followed by R570 (RMSE = 21.26 Mg ha− 1 ). However, the other cultivars presented a larger RMSE, with cultivar RB72454 showing the worse accuracy (RMSE = 32.79 Mg ha− 1 , [Table 3](#page-5-0)).

Nevertheless, the cultivars NCo376, R72454 and SP832847 presented a higher RMSE reduction compared to the experiments with cultivar RB867515, for ES and EnKF, with an average reduction of

#### **Table 2**

Study cases based on the sugarcane crop development and the number of leaf area index (LAI) observations presented in each stage for experiments 1 and 2. The description of crop phenological stages is shown in Section 2.6.

| Case | Description                         | Number of LAI observations |        |  |  |
|------|-------------------------------------|----------------------------|--------|--|--|
|      |                                     | Exp. 1                     | Exp. 2 |  |  |
| 1    | Observations only at stage 1        | 4                          | 4      |  |  |
| 2    | Observations only at stage 2        | 4                          | 4      |  |  |
| 3    | Observations only at stage 3        | 4                          | 4      |  |  |
| 4    | Observations only at stages 1 and 2 | 8                          | 8      |  |  |
| 5    | Observations only at stages 1 and 3 | 8                          | 8      |  |  |
| 6    | Observations only at stages 2 and 3 | 8                          | 8      |  |  |
| 7    | All observations                    | 12                         | 12     |  |  |

#### <span id="page-5-0"></span>**Table 3**

Root mean squared error (RMSE Mg ha− 1 ) for stalk fresh yield grouped by cultivar, simulated with open-loop (OP) and three data assimilation methods: weighted mean (WM), ensemble Kalman filter (EnKF), and ensemble smoother (ES). The values in brackets are the RMSE reduction compared to the OP simulations.

| Cultivar                                          | RMSE (Mg ha− 1<br>)                       |                                                                                           |                                                                                          |                                                                                          |  |  |  |
|---------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--|--|--|
|                                                   | OP                                        | WM                                                                                        | EnKF                                                                                     | ES                                                                                       |  |  |  |
| NCo376<br>R570<br>RB72454<br>SP832847<br>RB867515 | 29.36<br>21.26<br>32.79<br>27.45<br>19.94 | 24.90 (− 15.2%)<br>23.38 (10.0%)<br>28.37 (− 13.5%)<br>23.87 (− 13.0%)<br>15.36 (− 23.0%) | 21.83 (− 25.7%)<br>21.82 (2.6%)<br>26.23 (− 20.0%)<br>21.44 (− 21.9%)<br>16.76 (− 15.9%) | 21.85 (− 25.6%)<br>21.79 (2.5%)<br>26.27 (− 19.9%)<br>21.50 (− 21.7%)<br>16.70 (− 16.2%) |  |  |  |

− 22.4% and − 22.5%, whereas the RB867515 showed a reduction of − 16.2% and − 15.9%, respectively (Table 3). For the WM method, the error reduction was lower than other methods, for the non-calibrated cultivars, and obtained the higher reduction in RMSE (− 23.0%) for the RB867515 (Table 3). For the cultivar R570, the three DA methods resulted in an RMSE increase of 2.5%, 2.6% and 10%, respectively for ES, EnKF and WM. This may be caused to the distinct traits of R570, compared to the other cultivars and RB867515. We describe possible reasons for these differences in Section 3.3.

The correlation between the RMSE of the three DA with the OP was higher (R2 = 0.650, p *<* 0.01, Fig. 1), which demonstrates that OP simulations had a direct relation with results of DA methods. As result, DA methods had their simulation performance linked to the DS parametrization capacity of capturing the dynamics of key model states variables and influencing the ensemble spread.

## *3.2. Comparing data assimilation methods*

The regression analyses between DS simulations and observations of all experiments showed that OP simulations of SFY presented an agreement of R2 = 0.323 and an RMSE = 24.588 Mg ha− 1 . The DA methods improved the accuracy for SFY simulation, being the best results observed with ES (R2 = 0.498, RMSE = 20.268 Mg ha− 1 ), followed by EnKF (R2 = 0.497, RMSE = 20.276 Mg ha− 1 ) and WM (R2 = 0.458, RMSE = 21.588 Mg ha− 1 ) ([Fig. 2](#page-6-0)) Also, all the simulations presented a high significance (p *<* 0.01) ([Fig. 2](#page-6-0)). The EnKF and ES had similar values of RMSE and slope coefficient (b) [(Fig. 2](#page-6-0)), as well as closer R2 values corresponding to an increase of 54% as compared to OP [(Fig. 2](#page-6-0)). This suggested that, for our data, the ES method, which performs just one global assimilation, resulted in similar accuracy and precision to the multiples model re-initialization used by EnKF method. The WM had a

![](_page_5_Figure_8.jpeg)

**Fig. 1.** Relation between the root mean squared error (RMSE Mg ha− 1 ) for stalk fresh yield, grouped by cultivar, simulated with open-loop (OP) and three data assimilation methods: weighted mean (WM), ensemble Kalman filter (EnKF), and ensemble smoother (ES). Dashed black line represent the 1:1 adjustment, whereas the red dashed line is the regression between RMSE OP and RMSE DA.

lower RMSE and R2 compared to the other DA methods but presented an increase in simulations precision of 41.54% and a decrease on RMSE of 13.82%.

# *3.3. Analyzing DA methods for different experiments*

We compared the AE of SFY simulations individually for each experiment ([Table 4](#page-6-0)) and found DA methods having better results than OP simulations in most cases. The WM presented the best accuracy for six experiments (1, 2, 3, 6, 10 and 12), but in average it showed the highest AE average (17.17 Mg ha− 1 , [Table 4)](#page-6-0). The EnKF approach was the best method for four experiments (7, 9, 11, and 15), and showed an average AE of 16.58 Mg ha− 1 ([Table 4](#page-6-0)); the ES performed best for only one experiment (5), however presented the lower average AE (16.55 Mg ha− 1 ) ([Table 4](#page-6-0)) and for four experiments (4, 8, 13 and 14) the OP simulation showed the best accuracy. Across experiments, EnKF and ES outperformed the OP in the 11 experiments and the WM for 10 experiments.

Between those experiments for which OP showed the best performance, experiments 8 and 13 presented low AE values (1.25 and 0.77 Mg ha− 1 ) ([Table 4](#page-6-0)). This can be attributed to the fact that DA methods, when generating their ensembles, made the simulations more spread than OP, which resulted in higher errors compared to the OP simulations that had very high accuracy. As a result, in the assimilation step of the DA methods, the dispersion of the ensemble resulted in a high analysis error variance compared to the LAI observations variance. This led the DA methods to estimate LAI closer to the observed values, which in this case, resulted in less accurate estimation of SFY.

We also verified an increase of AE for Experiment 4, where we employed the DS parameters calibrated for the RB867515 to simulate R570 cultivar under irrigated conditions. Experiment 5 was also conducted in parallel to Experiment 4 to evaluate the growing performance of cultivar R570 under rainfed and irrigated conditions, yet both trials showed very similar SFY values (≈ 110 Mg ha− 1 ). In contrast, the DS simulations resulted in substantially different SFY values ([Table 4](#page-6-0)), where the irrigated experiment 4 showed higher yields (SFY = 139–143 Mg ha− 1 ) than the rainfed experiment 5 (SFY = 101–110 Mg ha− 1 ). This could indicate that cultivars RB867515 and R570 have distinct traits which may require a specific calibration for cultivar R570.

Experiments 13 and 14 had only one LAI measurement in the database that was not enough to improve model accuracy by any DA method ([Table 4](#page-6-0)). For these experiments, one LAI observation resulted in increased AE values as compared to the OP simulations. The number of LAI observations had a significant correlation with the difference of AE between OP and the three DA methods, 1% for WM (p *<* 0.01) and 5% for ES and EnKF (p *<* 0.05) ([Fig. 3](#page-7-0)). The WM presented the highest correlation (R2 = 0.508), followed by ES (R2 = 0.372) and EnKF (R2 = 0.368) ([Fig. 3](#page-7-0)).

Moreover, Experiments 1 and 2 presented a higher number of LAI observations compared to others, 22 and 23 respectively, in these conditions the DA methods promoted the best absolute improvements in SFY simulations ([Figs. 4 and 5](#page-8-0)). The WM had the best accuracy (AE = 1.68 and 2.63 Mg ha− 1 ) followed by ES (AE = 2.88 and 4.61 Mg ha− 1 ) and EnKF (AE = 4.86 and 2.99 Mg ha− 1 ) ([Figs. 4 and 5](#page-8-0)). For experiments with 4 LAI observations (e.g. Experiments 4–11), the AE differences were positive for two (Experiments 4 and 8) and negative in the others, for all DA methods. For the experiments with 5 and 7 LAI observations, the AE differences were negative for all experiments. In Experiment 15, where 6 LAI observations were available, the AE difference was negative for EnKF and ES and positive for WM.

However, excluding experiments 1 and 2, and considering the EnKF and ES methods, the higher reduction on SFY's AE was for experiment 11, with 4 LAI observations (AE difference = − 10.50 and − 10.47 Mg ha− 1 ), followed by experiments 3, with 7 LAI observations (AE difference = − 9.15 and − 9.60 Mg ha− 1 ) and experiment 7 with 4 LAI observations (AE difference = − 8.77 and − 8.71 Mg ha− 1 ). Moreover, the

<span id="page-6-0"></span>![](_page_6_Figure_1.jpeg)

**Fig. 2.** Comparison of observed and simulated stalk fresh yield (SFY) (a) with open-loop simulations (OP) and three data assimilation methods: (b) ensemble Kalman filter (EnKF), (c) ensemble smoother (ES), and (d) weighted mean (WM). Dashed black line represents the 1:1 adjustment, whereas the red dashed line is the regression between RMSE OP and RMSE DA methods. Squared symbols represent the experiments with cultivar RB867515 and triangles represent the experiments with no genotype-specific set of parameters (NCo376, R570, RB72454, and SP832847).

#### **Table 4**

Absolute error (AE Mg ha− 1 ) for different experiments used for open-loop (OP) and data assimilations methods: weighted mean (WM), ensemble Kalman filter (EnKF) and ensemble smoother (ES) for final stalk fresh yield simulations.

| Experiment | Location | Number of LAI observations | AE (Mg ha− 1<br>) |       |       |       | Best simulation method |
|------------|----------|----------------------------|-------------------|-------|-------|-------|------------------------|
|            |          |                            | OP                | WM    | EnKF  | ES    |                        |
| 1          | PIRA     | 22                         | 17.27             | 1.68  | 4.86  | 2.88  | WM                     |
| 2          | PIRA     | 23                         | 18.35             | 2.63  | 2.99  | 4.61  | WM                     |
| 3          | PIRA     | 7                          | 28.41             | 13.51 | 19.26 | 18.81 | WM                     |
| 4          | PIRA     | 4                          | 28.76             | 32.88 | 30.85 | 30.81 | OP                     |
| 5          | PIRA     | 4                          | 8.79              | 3.58  | 0.13  | 0.07  | ES                     |
| 6          | PIRA     | 4                          | 15.25             | 10.96 | 12.20 | 12.21 | WM                     |
| 7          | PIRA     | 4                          | 43.79             | 38.60 | 35.03 | 35.08 | EnKF                   |
| 8          | PIRA     | 4                          | 1.25              | 3.15  | 1.36  | 1.35  | OP                     |
| 9          | PIRA     | 4                          | 38.79             | 33.61 | 30.29 | 30.37 | EnKF                   |
| 10         | PIRA     | 4                          | 19.25             | 15.73 | 16.17 | 16.19 | WM                     |
| 11         | PIRA     | 4                          | 36.79             | 31.51 | 26.29 | 26.32 | EnKF                   |
| 12         | APTA     | 5                          | 29.61             | 21.84 | 25.07 | 24.84 | WM                     |
| 13         | COSP     | 1                          | 0.77              | 3.89  | 2.56  | 2.56  | OP                     |
| 14         | OLSP     | 1                          | 9.25              | 22.04 | 26.44 | 26.44 | OP                     |
| 15         | COAL     | 6                          | 19.46             | 21.94 | 15.15 | 15.72 | EnKF                   |
| Mean       |          |                            | 21.05             | 17.17 | 16.58 | 16.55 | ES                     |
| SD         |          |                            | 12.70             | 12.42 | 11.68 | 11.70 |                        |

PIRA: Piracicaba/SP, APTA: Aparecida do Taboado/MS, COSP: Colina/SP, OLSP: Olímpia/SP, COAL: Coruripe/AL, LAI: Leaf area index.

higher relative reduction was for experiment 5, with 4 observations (98% and 99%) followed by experiment 1 (72% and 83%) and 2 (84% and 75%). Despite the increase in the number of LAI observations tended to reduce AE for DA simulations, the magnitude of these reductions was not directly affected by the number of LAI observations, mainly for

experiments with 4–7 observations. Furthermore, considering experiments 6–12, and 15, there was a high correlation between the AE of OP simulations to the AE reduction. Thus, the initial errors of the model influenced the AE reduction, because it should be easier to reduce higher values of AE than lower values, due to the model structure.

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Fig. 3.** Relation between the number of leaf area index observations assimilated in each experiment and the absolute error (AE) difference between stalk fresh yield (SFY) simulated with one of the three data assimilation methods: (a) weighted mean (WM), (b) ensemble Kalman filter (EnKF) or (c) ensemble smoother (ES) and the open-loop simulation (OP).

#### *3.4. Impact of leaf area index observations in sugarcane growth stage*

Seven cases were studied to investigate the impact of timing of LAI observations in DA simulations ([Fig. 6](#page-10-0)). Differences in DA performances among development stages (cases 1–3) were observed. For stages 1 and 2 (case 1 and 2) there was an accuracy improvement only for experiment 1, for the three methods ([Fig. 6](#page-10-0)), with AE values lower than OP simulations. However, at stage 3 (case 3), for both experiments and three methods, there was a substantial accuracy improvement ([Fig. 6](#page-10-0)) compared to OP simulations.

When the LAI observations of stages 1 and 2 were assimilated together (case 4), it increased the AE compared to other cases and OP simulations. Also, case 4 presented the highest AE for experiments 1 and 2 for the ES and EnKF methods ([Fig. 6](#page-10-0)). Nevertheless, the assimilation of LAI data at stages 1 and 3 in case 5 improved the accuracy of DS simulations for all methods, and presented the lower AE, as compared to all cases. In Case 6, assimilation of LAI observations at stages 2 and 3, also presented an accuracy improvement compared to OP to cases 1–4, for all methods. Across crop stages, the observations assimilated at stage 3 showed a high influence for the accuracy improvement of the DS simulations, for all DA methods. However, LAI observations assimilated at stages 1 and 2 did not always result in better accuracy than OP simulations. Cases 1, 2 and 4 presented higher AE than OP simulations in experiment 2 and were not optimal in experiment 1 ([Fig. 6](#page-10-0)). This may have occurred because the sugarcane growing season is long, and assimilating LAI observations only at early stages may not be able to correct factors occurring in the remaining part of the cycle. Conversely, assimilating LAI measurements only at stage 2, when the crop is experiencing full canopy development still may not correct simulations after the onset of tillering senescence process, leading to overestimated LAI simulations. On the other hand, data assimilation during stage 3, covers most of the stalk formation stage of sugarcane which largely characterizes SFY. Moreover, at stage 3, is common for sugarcane, with high SFY and height, to suffer from lodging, which can reduce the LAI and the final SFY.

#### **4. Discussion**

In this study, three DA methods were used (WM, EnKF, and ES) to assimilate LAI observations along the growing cycle to improve SFY simulations as compared to the OP method. The ES and EnKF had very similar results and presented the best beneficial impact on the accuracy of SFY simulations across all field experiments and cultivars [(Fig. 2)](#page-6-0). Nevertheless, for experimental conditions with high LAI sampling such as those found in field experiments 1 and 2, the WM method presented the best improvements in SFY simulations, followed by ES and EnKF

([Figs. 4 and 5](#page-8-0)). Thus, our results do not show a predominance of a unique DA method for all experiments analyzed ([Table 4)](#page-6-0).

The WM performs the assimilation without updating model's internal variables, only utilizing the assimilated observation to select the ensemble member that is closer to crop state. This method works well with DS, and this agreed with the results found by [Tewes et al. (2020a),](#page-11-0) for wheat simulations with LINTUL5 model. In addition, WM can be easily applied with DS, because it did not require adaptations in the code for DA. However, our data showed that this method resulted in a low accuracy gain, compared to others DA methods when the DS was run for not calibrated cultivars.

The EnKF and ES presented very similar results. Part of this can be attributed to the lower error of LAI observations (4%), which narrows the EnKF and ES estimates around the observations ([Figs. 4 and 5)](#page-8-0). A derivation method of ES, the iterative ensemble smoother, was applied by [Yu et al. (2020)](#page-11-0) and resulted in an interesting improvement of stalk dry mass accuracy, for sugarcane simulated with SWAP-WOFOST with plant-high observations. However, more studies are required to understand the ES dynamic with remote sensing data for large areas.

The assimilation of LAI within the DS model improved the accuracy of SFY simulations for the majority of experiments, highlighting the potential for using DA methods with crop models. However, despite the improvements some experiments and DA methods did not show superior performance than the OP simulations or presented a lower accuracy gain. Therefore, this can be linked to three key factors for DA methods performance: number of observations, model parametrization and the state variables assimilated.

Because sugarcane crop remains in the field for longer periods, this may increase the need for observations throughout the crop cycle to be assimilated in the model. [Morel at al. (2014)](#page-11-0) recommended more than five LAI observations for forcing methods. For this study, almost all the experiments with four observations resulted in improved SFY simulations, for the three DA methods tested. However, the absolute decrease in AE was only partly explained by the number of LAI observations. Moreover, the crop phenological stage has high importance for the DA methods [(Pan et al., 2019; Tewes et al., 2020b; Xie et al., 2017](#page-11-0); [Yu et al.,](#page-11-0)  [2020)](#page-11-0). Our results demonstrated that the late stage was the more important, which corroborate with [Yu et al. (2020)](#page-11-0).

Our results showed that the performance of the DA methods, in situations where there were no previous cultivar-specific calibration, resulted in lower accuracy likely due to the uncertainty of OP simulations. This agrees with [Kang and Ozdo](#page-11-0) ¨ gan ˘ (2019), which showed that the EnKF had better yield estimation for maize when calibration was applied prior to LAI data assimilation. In contrast, [Lu et al. (2021)](#page-11-0)  improved the accuracy of maize yield estimation without prior genotype-specific calibration. In their study, the EnKF method was

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

**Fig. 4.** Comparison between simulated (lines) and observed (circles) leaf area index (LAI) and stalk fresh yield (SFY) for experiment 1, (a, e) open-loop simulations (OP) and three methods of data assimilations: (b, f) weighted mean (WM), (c, g) ensemble smoother (ES) and (d, h) ensemble Kalman filter (EnKF).

employed to assimilate canopy cover data for adjusting the phenological parameters of the AquaCrop model for each crop season. [Huang et al.](#page-11-0)  [(2016)](#page-11-0) also improved wheat yield estimations of the WOFOST model using the EnKF with LAI observations and fixed crop parameters for an entire region in China. Although an overall improvement of performance was found across cultivars using a fixed set of parameters for DS, the simulation performance was superior in experiments involving the calibrated cultivar (RB867515) ([Fig. 1](#page-5-0) and [Table 3](#page-5-0)). The DS model is a PBM which simulates various processes specific to the sugarcane crop system, with good performance ([Vianna et al., 2020)](#page-11-0). Thus, it is recommended for this type of model a previous calibrated set of parameters, differently from that observed for more generic crop models, which obtained more accurate results using DA even without any previous calibration ([Hu et al., 2019)](#page-11-0).

The observation's ability to correct the PBM imperfections is the success of DA methods ([Huang et al., 2019)](#page-11-0). However, updating one state variable only (e.g. LAI) does not always fully correct model behavior and may not properly translate the effects of limiting and reducing factors to other physiological processes simulated. Hence, mechanistically consistent simulations of SFY are unguaranteed, despite the use of LAI in DA having already been tested and demonstrated a more considerable relevance than others for yield estimates ([Ines et al.,](#page-11-0) 

![](_page_9_Figure_2.jpeg)

**Fig. 5.** Comparison between simulated (lines) and observed (circles) leaf area index (LAI) and stalk fresh yield (SFY) for experiment 2, (a, e) open-loop simulations (OP) and three methods of data assimilations: (b, f) weighted mean (WM), (c, g) ensemble smoother (ES) and (d, h) ensemble Kalman filter (EnKF).

[2013; Pan et al., 2019)](#page-11-0). Still, the use of LAI allied with other variables might improve the performance of DA methods. [Hu et al. (2019)](#page-11-0) demonstrated that when the water stress is high, assimilating LAI with soil moisture presents better results compared to LAI alone.

Moreover, comparing our results to [Hu et al. (2019)](#page-11-0), the EnKF methods with SWAP-WOFOST and LAI assimilations had an R2 = 0.45 and RMSE = 8.73 Mg ha− 1 , which was more accurate than those found in our study ([Fig. 2](#page-6-0)). However, these results were conducted with an LAI frequency of 8–16 days and part of the experiment was conducted at water stress and with leaf strip ([Hu et al., 2019)](#page-11-0), which differs from most of all our experiments. Compared to experiments 1 and 2, which have a

similar number of LAI observations, the AE showed similar results ([Figs. 3 and 4](#page-7-0)). Furthermore, the OP simulation of the SWAP-WOFOST showed a lower agreement with R2 = 0.05, compared with DS, despite the great accuracy (RMSE = 10.16 Mg ha− 1 ). However, more studies are needed to intercompare sophisticated and generalist crop models at the same conditions and calibration. Understanding in which cases the robustness of the PBM affects the DA simulations could be useful for choosing the best DA methods and configurations in different conditions.

Although the DA techniques employed in this study showed improved performance of SFY simulations, we found some limitations in

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Fig. 6.** Absolute error (AE, Mg ha− 1 ) for stalk fresh yield for seven study cases [(Table 2](#page-4-0)), for (a) experiment 1 and (b) experiment 2, and for three data assimilation methods: weighted mean (WM), ensemble smoother (ES) and ensemble Kalman filter (EnKF). Dashed lines represent the open-loop AE.

our study. As follows, we emphasize some points that can be attributed to improving the use of DA with DS for subsequent studies. Firstly, the calibration of the model should be better explored, apparently requiring one set of calibrated parameters for each cultivar because of the complexity of the PBM considered in our study. Secondly, the experiments used in our study followed a strict protocol to ensure there was no interference of reducing factors, and these are required conditions for PBM to simulate more efficiently. Therefore, studies with this methodology in areas where the reduction factors are present, or there would be data flaws in describing the environment, such as soil characterization and climate data, may result in a more pronounced accuracy gain due to the use of DA methods (Gilardelli et al., 2019). Thirdly, other state variables simulated by DS, such as above ground biomass ([Lu et al.,](#page-11-0)  [2021)](#page-11-0) plant height [(Yu et al., 2020)](#page-11-0), soil moisture [(Hu et al., 2019; Zhuo](#page-11-0)  [et al., 2019)](#page-11-0), canopy nitrogen accumulation ([Li et al., 2015)](#page-11-0), and canopy cover ([Lu et al., 2021)](#page-11-0) could be also used to enhance the model accuracy. Yet, the used PBM was developed to run without assimilations from start to end, for this study we just adjusted the state variables directly related to the LAI, plant weight, and leaf area. However, further studies could explore the allometric relations between LAI with the number of stalks, stalk height, and other related crop variables to simultaneously update these variables without direct measurements.

#### **5. Conclusion**

This study aimed to investigate the performance of DA methods when a genotype-specific calibration for a PBM is not available, as well as the combination of data amount and timing. This was done by means of a robust experimental field database for sugarcane, comprising 5 cultivars across different edaphoclimatic conditions in Brazil. The three DA methods obtained a better accuracy (RMSE) and precision (R2 ) if compared to the OP simulations. In general, considering all experiments the best results can be attributed to ES followed by EnKF and WM. The high accuracy occurred, for the three DA methods, when the cultivarspecific calibration was used to corresponding cultivar (e.g. RB867515). Moreover, the three DA methods outperformed the OP for three of four non-calibrated cultivars. However, the response for relative reduction on SFY's RMSE, changed between the methods, with EnKF and ES presenting higher reduction for the non-calibrated cultivars and WM for the calibrated cultivar. As the number of LAI observations increase, the DA methods tend to outperform the OP, nevertheless, this just explained part of the accuracy improvement by applying DA methods. In addition, we observed that LAI measurements at late stages more strongly influence the SFY accuracy. This study provides a potential methodology that can be applied for regional applications with LAI retrieved from remote sensing techniques.

#### **CRediT authorship contribution statement**

**Izael Martins Fattori Junior**: Conceptualization, Methodology,

Software, Formal analysis, Writing – original draft, Writing – review & editing. **Murilo Dos Santos Vianna**: Software, Data curation, Writing – review & editing, Investigation, Conceptualization. **Fabio** ´ **Ricardo Marin**: Supervision, Conceptualization, Funding acquisition, Writing – review & editing.

#### **Declaration of Competing Interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

#### **Acknowledgments**

Primary funding sources of this research include the S˜ ao Paulo Research Foundation - Brazil (FAPESP, Grants 2021/00720-0 and 2014/ 05887-6), and Brazilian Research Council (CNPq, 100094/2019-8, 301424/2015-2, 300916/2018-3, 401662/2016-0 and 425174/2018- 2). We also thank Leticia G. Gasparotto and to the staff of the Group of Experimentation and Research on Agriculture and Modeling (ESALQ-CLIMA) for the support in conducting part of the field experiments.

## **Appendix A. Supplementary material**

Supplementary data associated with this article can be found in the online version at [doi:10.1016/j.eja.2022.126501.](https://doi.org/10.1016/j.eja.2022.126501)

#### **References**

- Byrd, R.H., Peihuang, L., Nocedal, J., 1996. A limited-memory algorithm for boundconstrained optimization. SIAM J. Sci. Comput. <https://doi.org/10.2172/204262>.
- Cukier, R.I., Fortuin, C.M., Shuler, K.E., Petschek, A.G., Schaibly, J.H., 1973. Study of the sensitivity of coupled reaction systems to uncertainties in rate coefficients. I Theory. J. Chem. Phys. 59, 3873–3878. <https://doi.org/10.1063/1.1680571>.
- Curnel, Y., de Wit, A.J.W., Duveiller, G., Defourny, P., 2011. Potential performances of remotely sensed LAI assimilation in WOFOST model based on an OSS experiment. Agric. For. Meteorol. 151, 1843–1855. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.agrformet.2011.08.002)  [agrformet.2011.08.002](https://doi.org/10.1016/j.agrformet.2011.08.002).
- Evensen, G., 2003. The ensemble Kalman filter: theoretical formulation and practical implementation. Ocean Dyn. 53, 343–367. [https://doi.org/10.1007/s10236-003-](https://doi.org/10.1007/s10236-003-0036-9) [0036-9.](https://doi.org/10.1007/s10236-003-0036-9)
- FAO, 2019. Food and Agriculture Organization of the United Nations. FAOSTAT. 〈<http://www.fao.org/faostat/en/#home>〉.
- Gilardelli, C., Stella, T., Confalonieri, R., Ranghetti, L., Campos-Taberner, M., García-Haro, F.J., Boschetti, M., 2019. Downscaling rice yield simulation at sub-field scale using remotely sensed LAI data. Eur. J. Agron. 103, 108–116. [https://doi.org/](https://doi.org/10.1016/j.eja.2018.12.003)  [10.1016/j.eja.2018.12.003](https://doi.org/10.1016/j.eja.2018.12.003).
- Goldemberg, J., Mello, F.F.C., Cerri, C.E.P., Davies, C.A., Cerri, C.C., 2014. Meeting the global demand for biofuels in 2021 through sustainable land use change policy. Energy Policy 69, 14–18. <https://doi.org/10.1016/j.enpol.2014.02.008>.
- Gonçalves, A.O., Silva, E.H.F.M.D., Gasparotto, L.G., Rosa, J.M., Carmo, S.D., Fattori Junior, I.M., Marin, F.R., 2020. Improving indirect measurements of the leaf area index using canopy height. Pesqui. Agropecu. Bras. 55, 1–9. [https://doi.org/](https://doi.org/10.1590/S1678-3921.PAB2020.V55.01894)  [10.1590/S1678-3921.PAB2020.V55.01894](https://doi.org/10.1590/S1678-3921.PAB2020.V55.01894).
- Holzworth, D.P., Huth, N.I., deVoil, P.G., Zurcher, E.J., Herrmann, N.I., McLean, G., Chenu, K., van Oosterom, E.J., Snow, V., Murphy, C., Moore, A.D., Brown, H., Whish, J.P.M., Verrall, S., Fainges, J., Bell, L.W., Peake, A.S., Poulton, P.L.,

<span id="page-11-0"></span>Hochman, Z., Thorburn, P.J., Gaydon, D.S., Dalgliesh, N.P., Rodriguez, D., Cox, H., Chapman, S., Doherty, A., Teixeira, E., Sharp, J., Cichota, R., Vogeler, I., Li, F.Y., Wang, E., Hammer, G.L., Robertson, M.J., Dimes, J.P., Whitbread, A.M., Hunt, J., van Rees, H., McClelland, T., Carberry, P.S., Hargreaves, J.N.G., MacLeod, N., McDonald, C., Harsdorf, J., Wedgwood, S., Keating, B.A., 2014. APSIM - Evolution

- towards a new generation of agricultural systems simulation. Environ. Model. Softw. 62, 327–350. <https://doi.org/10.1016/j.envsoft.2014.07.009>.
- [Hoogenboom, G., Porter, C.H., Boote, K.J., Shelia, V., Wilkens, P.W., Singh, U., White, J.](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref9)  [W., Asseng, S., Lizaso, J.I., Moreno, L.P., Pavan, W., Ogoshi, R., Hunt, L.A., Tsuji, G.](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref9)  [Y., Jones, J.W., 2019. The DSSAT crop modeling ecosystem. In: Boote, K.J. (Ed.),](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref9)  [Advances in Crop Modeling for a Sustainable Agriculture. Burleigh Dodds Science](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref9) [Publishing, Cambridge, United Kingdom, pp. 173](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref9)–216.
- Hu, S., Shi, L., Huang, K., Zha, Y., Hu, X., Ye, H., Yang, Q., 2019. Improvement of sugarcane crop simulation by SWAP-WOFOST model via data assimilation. Field Crop. Res. 232, 49–61. <https://doi.org/10.1016/j.fcr.2018.12.009>.
- Huang, J., Sedano, F., Huang, Y., Ma, H., Li, X., Liang, S., Tian, L., Zhang, X., Fan, J., Wu, W., 2016. Assimilating a synthetic Kalman filter leaf area index series into the WOFOST model to improve regional winter wheat yield estimation. Agric. For. Meteorol. 216, 188–202. [https://doi.org/10.1016/j.agrformet.2015.10.013.](https://doi.org/10.1016/j.agrformet.2015.10.013)
- Huang, J., Gomez-Dans, ´ J.L., Huang, H., Ma, H., Wu, Q., Lewis, P.E., Liang, S., Chen, Z., Xue, J.H., Wu, Y., Zhao, F., Wang, J., Xie, X., 2019. Assimilation of remote sensing into crop growth models: current status and perspectives. Agric. For. Meteorol. 276–277, 107609 [https://doi.org/10.1016/j.agrformet.2019.06.008.](https://doi.org/10.1016/j.agrformet.2019.06.008)
- Huang, X., Zhao, G., Zorn, C., Tao, F., Ni, S., Zhang, W., Tu, T., Hoglind, ¨ M., 2021. Grass modelling in data-limited areas by incorporating MODIS data products. Field Crop. Res. 271, 108250 [https://doi.org/10.1016/j.fcr.2021.108250.](https://doi.org/10.1016/j.fcr.2021.108250)
- Ines, A.V.M., Das, N.N., Hansen, J.W., Njoku, E.G., 2013. Assimilation of remotely sensed soil moisture and vegetation with a crop simulation model for maize yield prediction. Remote Sens. Environ. 138, 149–164. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.rse.2013.07.018)  [rse.2013.07.018](https://doi.org/10.1016/j.rse.2013.07.018).
- Inman-Bamber, N.G., Thompson, G.D., 1989. Models of dry matter accumulation by sugarcane. In: Proceedings of the South African Sugarcane Technology, 63, pp. 212–216.
- [Jones, C.A., Wegener, M.K., Russell, J.S., McLeod, I.M., Williams, J., 1989. AUSCANE-](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref15)[Simulation of Australian Sugarcane with EPIC. CSIRO](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref15).
- Jones, J.W., Hoogenboom, G., Porter, C., Boote, K., Batchelor, W., Hunt, L., Wilkens, P., Singh, U., Gijsman, A., Ritchie, J., 2003. The DSSAT cropping system model. Eur. J. Agron. 18, 235–265. <https://doi.org/10.1016/S1161-0301(02)00107-7>.
- Jones, J.W., Antle, J.M., Basso, B., Boote, K.J., Conant, R.T., Foster, I., Godfray, H.C.J., Herrero, M., Howitt, R.E., Janssen, S., Keating, B.A., Munoz-Carpena, R., Porter, C. H., Rosenzweig, C., Wheeler, T.R., 2017. Brief history of agricultural systems
- modeling. Agric. Syst. 155, 240–254. [https://doi.org/10.1016/j.agsy.2016.05.014.](https://doi.org/10.1016/j.agsy.2016.05.014) Jones, M.R., Singels, A., 2018. Refining the Canegro model for improved simulation of climate change impacts on sugarcane. Eur. J. Agron. 100, 76–86. [https://doi.org/](https://doi.org/10.1016/j.eja.2017.12.009)  [10.1016/j.eja.2017.12.009.](https://doi.org/10.1016/j.eja.2017.12.009)
- Kang, Y., Ozdo ¨ gan, ˘ M., 2019. Field-level crop yield mapping with Landsat using a hierarchical data assimilation approach. Remote Sens. Environ. 228, 144–163. [https://doi.org/10.1016/j.rse.2019.04.005.](https://doi.org/10.1016/j.rse.2019.04.005)
- Keating, B.A., Carberry, P.S., Hammer, G.L., Probert, M.E., Robertson, M.J., Holzworth, D., Huth, N.I., Hargreaves, J.N.G., Meinke, H., Hochman, Z., McLean, G., Verburg, K., Snow, V., Dimes, J.P., Silburn, M., Wang, E., Brown, S., Bristow, K.L., Asseng, S., Chapman, S., McCown, R.L., Freebairn, D.M., Smith, C.J., 2003. An overview of APSIM, a model designed for farming systems simulation. Eur. J. Agron. 18, 267–288. <https://doi.org/10.1016/S1161-0301(02)00108-9>.
- Lee, K., Jung, S., Choe, J., 2016. Ensemble smoother with clustered covariance for 3D channelized reservoirs with geological uncertainty. J. Pet. Sci. Eng. 145, 423–435. [https://doi.org/10.1016/j.petrol.2016.05.029.](https://doi.org/10.1016/j.petrol.2016.05.029)
- Li, Z., Wang, J., Xu, X., Zhao, C., Jin, X., Yang, G., Feng, H., 2015. Assimilation of two variables derived from hyperspectral data into the DSSAT-CERES model for grain yield and quality estimation. Remote Sens. 7, 12400–12418. [https://doi.org/](https://doi.org/10.3390/rs70912400)  [10.3390/rs70912400.](https://doi.org/10.3390/rs70912400)
- Lisboa, I.P., Cherubin, M.R., Lima, R.P., Cerri, C.C., Satiro, L.S., Wienhold, B.J., Schmer, M.R., Jin, V.L., Cerri, C.E.P., 2018. Sugarcane straw removal effects on plant growth and stalk yield. Ind. Crop. Prod. 111, 794–806. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.indcrop.2017.11.049)  [indcrop.2017.11.049](https://doi.org/10.1016/j.indcrop.2017.11.049).
- [Liu, D.L., Kingston, G., 1995. QCANE: a simulation model of sugarcane growth and sugar](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref24)  [accumulation. In: Research and Modelling Approaches to Assess Sugercane](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref24) [Production Opportunities and Constraints. University of Queensland, St. Lucia,](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref24) 29–[25.](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref24)
- Lobell, D.B., Cassman, K.G., Field, C.B., 2009. Crop yield gaps: their importance, magnitudes, and causes. Annu. Rev. Environ. Resour. 34, 179–204. [https://doi.org/](https://doi.org/10.1146/annurev.environ.041008.093740)  [10.1146/annurev.environ.041008.093740.](https://doi.org/10.1146/annurev.environ.041008.093740)
- Lu, Y., Chibarabada, T.P., Ziliani, M.G., Onema, J.M.K., McCabe, M.F., Sheffield, J., 2021. Assimilation of soil moisture and canopy cover data improves maize simulation using an under-calibrated crop model. Agric. Water Manag. 252, 106884 [https://doi.org/10.1016/j.agwat.2021.106884.](https://doi.org/10.1016/j.agwat.2021.106884)
- Marin, F., Jones, J.W., Boote, K.J., 2017. A stochastic method for crop models: Including uncertainty in a sugarcane model. Agron. J. 109, 483–495. [https://doi.org/10.2134/](https://doi.org/10.2134/agronj2016.02.0103)  [agronj2016.02.0103](https://doi.org/10.2134/agronj2016.02.0103).
- Marin, F.R., 2016. Understanding sugarcane production, Biofuels, and market volatility in Brazil—a research perspective. Outlook Agric. 45, 75–77. [https://doi.org/](https://doi.org/10.1177/0030727016649802)  [10.1177/0030727016649802.](https://doi.org/10.1177/0030727016649802)
- Marin, F.R., de Carvalho, G.L., 2012. Spatio-temporal variability of sugarcane yield efficiency in the state of Sao ˜ Paulo, Brazil. Pesqui. Agropecu. Bras. 47, 149–156. [https://doi.org/10.1590/S0100-204](https://doi.org/10.1590/S0100-204×2012000200001)×2012000200001.
- Marin, F.R., Jones, J.W., 2014. Process-based simple model for simulating sugarcane growth and production. Sci. Agric. 71, 1–16. [https://doi.org/10.1590/S0103-](https://doi.org/10.1590/S0103-90162014000100001)  [90162014000100001](https://doi.org/10.1590/S0103-90162014000100001).
- Marin, F.R., Lopes-Assad, M.L., Assad, E.D., Vian, C.E., Santos, M.C., 2008. Sugarcane crop efficiency in two growing seasons in S˜ ao Paulo State, Brazil. Pesqui. Agropecu. Bras. 43, 1449–1455. [https://doi.org/10.1590/s0100-204](https://doi.org/10.1590/s0100-204×2008001100002)×2008001100002.
- Marin, F.R., Jones, J.W., Royce, F., Suguitani, C., Donzeli, J.L., Filho, W.J.P., Nassif, D.S. P., 2011. Parameterization and evaluation of predictions of DSSAT/CANEGRO for Brazilian sugarcane. Agron. J. 103, 304–315. [https://doi.org/10.2134/](https://doi.org/10.2134/agronj2010.0302) [agronj2010.0302](https://doi.org/10.2134/agronj2010.0302).
- Marin, F.R., Thorburn, P.J., Nassif, D.S.P., Costa, L.G., 2015. Sugarcane model intercomparison: structural differences and uncertainties under current and potential future climates. Environ. Model. Softw. 72, 372–386. [https://doi.org/](https://doi.org/10.1016/j.envsoft.2015.02.019) [10.1016/j.envsoft.2015.02.019](https://doi.org/10.1016/j.envsoft.2015.02.019).
- Marin, F.R., Rattalino Edreira, J.I., Andrade, J., Grassini, P., 2019. On-farm sugarcane yield and yield components as influenced by number of harvests. Field Crop. Res. 240, 134–142. [https://doi.org/10.1016/j.fcr.2019.06.011.](https://doi.org/10.1016/j.fcr.2019.06.011)
- Marin, F.R., Rattalino Edreira, J.I., Andrade, J.F., Grassini, P., 2021. Sugarcane yield and yield components as affected by harvest time. Sugar Tech. [https://doi.org/10.1007/](https://doi.org/10.1007/s12355-020-00945-5) [s12355-020-00945-5](https://doi.org/10.1007/s12355-020-00945-5).
- Martin´e, J.-F., 2003. Mod´elisation de la production potentielle de la canne a ` sucre en zone tropicale, sous conditions thermiques et hydriques contrast´ees. Applications du mod`ele. Institut national agronomique Paris-Grignon.
- Morel, J., Todoroff, P., B´egu´e, A., Bury, A., Martin´e, J.F., Petit, M., 2014. Toward a satellite-based system of sugarcane yield estimation and forecasting in smallholder farming conditions: a case study on reunion island. Remote Sens. 6, 6620–6635. <https://doi.org/10.3390/rs6076620>.
- Nearing, G.S., Crow, W.T., Thorp, K.R., Moran, M.S., Reichle, R.H., Gupta, H.V., 2012. Assimilating remote sensing observations of leaf area index and soil moisture for wheat yield estimates: an observing system simulation experiment. Water Resour. Res. 48, 1–13. <https://doi.org/10.1029/2011WR011420>.
- Pan, H., Chen, Z., de Allard, W., Ren, J., 2019. Joint assimilation of leaf area index and soil moisture from sentinel-1 and sentinel-2 data into the WOFOST model for winter wheat yield estimation. Sensors 19. [https://doi.org/10.3390/s19143161.](https://doi.org/10.3390/s19143161)
- [Saltelli, A., Tarantola, S., Chan, K.P.S., 1999. A quantitative model-independent method](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref39) [for global sensitivity analysis of model output. Technometrics 41, 39](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref39)–56.
- Singels, A., Jones, M., Van Der Berg, M., 2008. DSSAT v4.5-Canegro Sugarcane Plant Module: Scientific Documentation.
- Suguitani, C., 2006. Entendendo o crescimento e produçao ˜ da cana de açúcar: avaliaçao ˜ do modelo MOSICAS. Universidade de Sao ˜ Paulo, Escola Superior de Agricultura "Luiz de Queiroz."
- [Supit, I., Hooijer, A., van Diepen, C., 1994. Improvement of Sugarcane Crop Simulation](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref40) [by SWAP-WOFOST Model Via Data Assimilation Volume 1: Theory and Algorithms.](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref40)
- Tewes, A., Hoffmann, H., Krauss, G., Sch¨ afer, F., Kerkhoff, C., Gaiser, T., 2020a. New approaches for the assimilation of LAI measurements into a crop model ensemble to improve wheat biomass estimations. Agronomy 10, 1–21. [https://doi.org/10.3390/](https://doi.org/10.3390/agronomy10030446) [agronomy10030446](https://doi.org/10.3390/agronomy10030446).
- Tewes, A., Montzka, C., Nolte, M., Krauss, G., Hoffmann, H., Gaiser, T., 2020b. Assimilation of sentinel-2 estimated LAI into a crop model: influence of timing and frequency of acquisitions on simulation of water stress and biomass production of winter wheat. Agronomy 10, 1813. [https://doi.org/10.3390/agronomy10111813.](https://doi.org/10.3390/agronomy10111813)
- van Dam, J.C., Huygen, J., Wesseling, J.G., Feddes, R.A., Kabat, P., van Walsum, P.E.V., Groenendijk, P., van Diepen, C.A., 1997. Theory of SWAP Version 2.0; Simulation of Water Flow, Solute Transport and Plant Growth in the Soil-water-atmosphere-plant Environment.
- Van Ittersum, M.K., Leffelaar, P.A., Van Keulen, H., Kropff, M.J., Bastiaans, L., Goudriaan, J., 2003. On approaches and applications of the Wageningen crop models. Eur. J. Agron. 18, 201–234. [https://doi.org/10.1016/S1161-0301(02)](https://doi.org/10.1016/S1161-0301(02)00106-5) [00106-5.](https://doi.org/10.1016/S1161-0301(02)00106-5)
- [Van Leeuwen, P.J., Evensen, G., 1996. Data assimilation and inverse methods in terms of](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref44) [a probabilistic formulation. Mon. Weather Rev. 124, 2898](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref44)–2913 https://doi.org/doi. [org/10.1175/1520-0493(1996)124](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref44)*<*2898:DAAIMI*>*2.0.CO;2.
- Vianna, M., dos, S., Nassif, D.S.P., dos Santos Carvalho, K., Marin, F.R., 2020. Modelling the trash blanket effect on sugarcane growth and water use. Comput. Electron. Agric. 172, 105361 <https://doi.org/10.1016/j.compag.2020.105361>.
- Villegas, F.D., Daza, O.H., Jones, J.W., Royce, F.S., 2005. CASUPRO: An industry-driven sugarcane model. In: Proceedings of the 2005 ASAE Annual International Meeting, p. 0300. 〈<https://doi.org/10.13031/2013.19062>〉.
- [Wallach, D., Makowski, D., Jones, J.W., Brun, F., 2018. Working with Dynamic Crop](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref46)  [Models: Methods, Tools and Examples for Agriculture and Environment. Academic](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref46)  [Press.](http://refhub.elsevier.com/S1161-0301(22)00049-1/sbref46)
- Wang, E., Brown, H.E., Rebetzke, G.J., Zhao, Z., Zheng, B., Chapman, S.C., 2019. Improving process-based crop models to better capture genotype× environment× management interactions. J. Exp. Bot. 70, 2389–2401. [https://doi.org/10.1093/jxb/](https://doi.org/10.1093/jxb/erz092)  [erz092.](https://doi.org/10.1093/jxb/erz092)
- de Wit, A.J.W., van Diepen, C.A., 2007. Crop model data assimilation with the ensemble Kalman filter for improving regional crop yield forecasts. Agric. For. Meteorol. 146, 38–56. [https://doi.org/10.1016/j.agrformet.2007.05.004.](https://doi.org/10.1016/j.agrformet.2007.05.004)
- Xie, Y., Wang, P., Bai, X., Khan, J., Zhang, S., Li, L., Wang, L., 2017. Assimilation of the leaf area index and vegetation temperature condition index for winter wheat yield estimation using Landsat imagery and the CERES-Wheat model. Agric. For. Meteorol. 246, 194–206. [https://doi.org/10.1016/j.agrformet.2017.06.015.](https://doi.org/10.1016/j.agrformet.2017.06.015)
- Yu, D., Zha, Y., Shi, L., Jin, X., Hu, S., Yang, Q., Huang, K., Zeng, W., 2020. Improvement of sugarcane yield estimation by assimilating UAV-derived plant height

## <span id="page-12-0"></span>*I.M. Fattori Junior et al.*

observations. Eur. J. Agron. 121, 126159 [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.eja.2020.126159)  [eja.2020.126159.](https://doi.org/10.1016/j.eja.2020.126159)

- Zhao, Y., Chen, S., Shen, S., 2013. Assimilating remote sensing information with crop model using Ensemble Kalman Filter for improving LAI monitoring and yield estimation. Ecol. Model. 270, 30–42. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ecolmodel.2013.08.016)  [ecolmodel.2013.08.016](https://doi.org/10.1016/j.ecolmodel.2013.08.016).
- Zhuo, W., Huang, J., Li, L., Zhang, X., Ma, H., Gao, X., Huang, H., Xu, B., Xiao, X., 2019. Assimilating soil moisture retrieved from sentinel-1 and sentinel-2 Data into WOFOST model to improve winter wheat yield estimation. Remote Sens. 11, 1618. [https://doi.org/10.3390/rs11131618.](https://doi.org/10.3390/rs11131618)