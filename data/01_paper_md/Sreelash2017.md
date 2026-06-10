[Journal of Hydrology 546 (2017) 166–178](http://dx.doi.org/10.1016/j.jhydrol.2016.12.049)

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/00221694)

Journal of Hydrology

journal homepage: [www.elsevier.com/locate/jhydrol](http://www.elsevier.com/locate/jhydrol)

Research papers

# Estimation of available water capacity components of two-layered soils using crop model inversion: Effect of crop type and water regime

![](_page_0_Picture_6.jpeg)

K. Sreelash a,b,c,d , Samuel Buis a,⇑ , M. Sekhar b,d , Laurent Ruiz b,d,e,f , Sat Kumar Tomer b,d,g , Martine Guérif a

aUMR EMMAH, INRA, UAPV, F-84 914 Avignon, France

b Indo-French Cell for Water Sciences, Indian Institute of Science, IRD, Bangalore, India

cNational Centre for Earth Science Studies, Thiruvananthapuram, India

dDepartment of Civil Engineering, Indian Institute of Science, Bangalore, India

e INRA, UMR 1069 SAS, AGROCAMPUS OUEST, F-35000 Rennes, France

f GET, CNRS, UPS, IRD, CNES, 31400 Toulouse, France

g Aapah Innovations Private Limited, Hyderabad 500 032, India

## article info

Article history: Received 21 March 2016 Received in revised form 22 December 2016 Accepted 24 December 2016 Available online 27 December 2016 This manuscript was handled by Tim McVicar Editor-in-Chief, with the assistance

of Yongqiang Zhang, Associate Editor

Keywords: Soil hydraulic properties Available water capacity STICS Soil water content GLUE Inverse modelling

# abstract

Characterization of the soil water reservoir is critical for understanding the interactions between crops and their environment and the impacts of land use and environmental changes on the hydrology of agricultural catchments especially in tropical context. Recent studies have shown that inversion of crop models is a powerful tool for retrieving information on root zone properties. Increasing availability of remotely sensed soil and vegetation observations makes it well suited for large scale applications. The potential of this methodology has however never been properly evaluated on extensive experimental datasets and previous studies suggested that the quality of estimation of soil hydraulic properties may vary depending on agro-environmental situations. The objective of this study was to evaluate this approach on an extensive field experiment. The dataset covered four crops (sunflower, sorghum, turmeric, maize) grown on different soils and several years in South India. The components of AWC (available water capacity) namely soil water content at field capacity and wilting point, and soil depth of twolayered soils were estimated by inversion of the crop model STICS with the GLUE (generalized likelihood uncertainty estimation) approach using observations of surface soil moisture (SSM; typically from 0 to 10 cm deep) and leaf area index (LAI), which are attainable from radar remote sensing in tropical regions with frequent cloudy conditions. The results showed that the quality of parameter estimation largely depends on the hydric regime and its interaction with crop type. A mean relative absolute error of 5% for field capacity of surface layer, 10% for field capacity of root zone, 15% for wilting point of surface layer and root zone, and 20% for soil depth can be obtained in favorable conditions. A few observations of SSM (during wet and dry soil moisture periods) and LAI (within water stress periods) were sufficient to significantly improve the estimation of AWC components. These results show the potential of crop model inversion for estimating the AWC components of two-layered soils and may guide the sampling of representative years and fields to use this technique for mapping soil properties that are relevant for distributed hydrological modelling.

2017 Elsevier B.V. All rights reserved.

# 1. Introduction

The capacity of the soil to store water available for plants, generally referred as available water capacity (AWC) is a key parameter for modelling the catchment-scale water balance. In particular, in tropical semi-arid contexts, where potential evapotranspiration equals or exceeds rainfall, recharge to groundwater is difficult to estimate from vadose-zone water balance [(De Vries and](#page-11-0) [Simmers, 2002](#page-11-0)) and it is particularly sensitive to the size of the soil water storage [(Anuraga et al., 2006; Sreelash et al., 2013)](#page-11-0). Therefore, accurate estimates of AWC and its spatial variability at the catchment scale are needed to improve the sustainable management of groundwater resources. The increasing availability of high frequency and high resolution remote-sensing data now allows retrieving precise soil hydraulic properties maps of the top few centimeters of the soil [(Montzka et al., 2011)](#page-12-0) but estimating

![](_page_0_Picture_26.jpeg)

<sup>⇑</sup> Corresponding author at: UMR EMMAH, INRA, UAPV, F-84 914 Avignon, France. E-mail address: [samuel.buis@paca.inra.fr](mailto:samuel.buis@paca.inra.fr) (S. Buis).

AWC of the entire root zone at the catchment scale remains a challenge.

AWC depends on soil hydraulic properties (SHPs), soil depth and plant rooting characteristics. It may be defined from different points of view - pedologists, soil scientists, ecophysiologists - with different approaches and different levels of complexity, considering one or several layers corresponding to pedological horizons. A common definition of the AWC is the difference between the soil water content at field capacity and wilting point [(Bruand et al.,](#page-11-0) [2003](#page-11-0)). Those parameters can be determined in the field, which minimizes soil disturbance or in the laboratory which requires soil sampling and sample preparation that could distort the soil sample and increase the margins of errors. All methods are highly timeconsuming and expensive [(Steele-Dunne et al., 2010; Botula](#page-12-0) [et al., 2012](#page-12-0)). Therefore, it is impractical to use them to obtain soil properties for catchments larger than a few hectares. For larger areas SHPs are generally estimated from soil characteristics that are easily available from soil maps (mainly textural properties) using pedotransfer functions (PTFs). However, PTFs are often sitespecific and may lead to crude estimates of SHPs with large uncertainties when extrapolated over large areas [(Vereecken et al., 1989,](#page-12-0) [1990; Wösten et al., 2001; Stumpp et al., 2009)](#page-12-0) or beyond the specific context (geomorphic regions or soil type) under which they are developed [(McBratney et al., 2002)](#page-11-0). A more recent technique is Digital Soil Mapping (DSM) that couples field and laboratory observational methods with spatial and non-spatial soil inference systems [(Lagacherie and McBratney, 2007)](#page-11-0). DSM makes an extensive use of technological and computational advances such as remote sensing and geostatistics for producing digital maps of soil types and soil properties [(Lagacherie et al., 2008;](#page-11-0) [Vaysse and Lagacherie, 2015)](#page-11-0). However, approaches based on DSM estimate basic soil properties such as soil texture, bulk density, and pH and still rely on PTFs to translate them into more functional properties [(McBratney et al., 2003)](#page-11-0). They are thus also limited by the quality of the PTFs and their adequacy to the studied situation.

As AWC components are important parameters for hydrological models, model inversion is another alternative for retrieving them. The principle is to use in situ or remotely sensed observations corresponding to model outputs strongly linked with AWC components to estimate them using parameter estimation or data assimilation methods. Such approach has been carried out in several studies for estimating SHPs and soils depth using various types of models: hydrological models [(Ritter et al., 2003; Ines and](#page-12-0) [Mohanty, 2008; Charoenhirunyingyos et al., 2011)](#page-12-0), crop models [(Guérif et al., 2006; Varella et al., 2010a,b; Sreelash et al., 2012)](#page-11-0), agro-hydrological models [(Ferrant et al., 2016)](#page-11-0), Land Surface Models [(Bandara et al., 2013, 2014, 2015)](#page-11-0) or SVAT (soil vegetation atmosphere transfer) models [(Jhorar et al., 2002, 2004)](#page-11-0). Several studies have shown that SHPs of vertically homogeneous soils can be estimated through model inversion using surface soil moisture (see for example [Montzka et al., 2011; Nagarajan et al., 2011)](#page-12-0). For multi-layered soils, profile soil moisture observations allow assessing SHPs [(Ritter et al., 2003; Braga and Jones, 2004;](#page-12-0) [Wohling and Vrugt, 2011; Li and Ren, 2011)](#page-12-0) but this requires large experimental settings which limits its spatial application. On the other hand, using only surface soil moisture measurements that can be spatially available from remote sensing, is not sufficient to provide unique and physically reasonable estimates of hydraulic properties for multi-layered soils through model inversion [(Vereecken et al., 2008; Ines and Mohanty, 2008;](#page-12-0) [Charoenhirunyingyos et al., 2011)](#page-12-0) because of the poor connection in the hydraulic processes between layers ([Montzka et al., 2011)](#page-12-0), except in some particular situations [(Shin et al., 2012; Bandara](#page-12-0) [et al., 2013)](#page-12-0). [Shin et al. (2012)](#page-12-0) also reported that the weakness of hydrological models in simulating plant root activities in the root zone results in relatively larger errors in the estimation of SHPs in crop land as compared to bare soil. As crop lands represent a large contribution to hydrologic processes within agricultural catchments, precise knowledge of AWC components is critical for managing water resources to maintain agricultural production. The known projections of climate change make this objective even more essential.

Recently, crop model inversion has been proposed by several authors to retrieve AWC components [(Guérif et al., 2006; Varella](#page-11-0) [et al., 2010a, 2010b; Sreelash et al., 2012)](#page-11-0). The main interest of using crop models for retrieving AWC components in crop lands is that they are more efficient than hydrological models, Land Surface Models or SVAT models in describing the specificity of crop behavior with regards to water processes (effect of crop type on rooting system characteristics and water needs, effect of crop management practices on the water balance). This is partly because they account AWC components impacts not only on the soil water balance, but also on the coupled carbon and nitrogen cycling [(Ruget et al., 2002; Satti et al., 2004; Breda et al., 2006)](#page-12-0). The increasing availability of high frequency and high resolution vegetation and soil moisture data from remote sensing makes crop model inversion approach a potentially powerful tool for spatial applications, especially for parameterizing catchment-scale hydrological models.

However, accuracy of the parameter estimates strongly depends on environmental conditions such as climate and crop type [(Varella et al., 2010b)](#page-12-0). [Charoenhirunyingyos et al. (2011)](#page-11-0) and [Sreelash et al. (2012)](#page-12-0) show that combining surface soil moisture and vegetation measurements in model inversion, by bringing information on both surface and root zone SHPs, improves substantially parameter estimation. However, these conclusions are based on synthetic experiments or very limited field datasets. In fact, few studies based on field data have been carried out to evaluate the potential of model inversion methods for estimating AWC components on multi-layered soils with observations potentially accessible from remote sensing and this problem is still considered as challenging [(Mohanthy, 2013)](#page-12-0).

In this paper, we used an extensive field dataset from a tropical agricultural catchment in South India involving four types of crops across 3 years. The objectives are:

- (i) to analyze the potential of model inversion methods for estimating AWC components (water content at field capacity and wilting point, soil depth) on two-layered soils with observations potentially accessible from remote sensing on a large set of field situations; and
- (ii) to investigate the influence of the crop type and water regimes experienced by the crops on the accuracy of these estimations.

## 2. Materials and methods

## 2.1. Site information

The experimental catchment of Berambadi (84 km2 ) is located in the Kabini river basin in South India (AMBHAS Site, [www.amb](http://www.ambhas.com)[has.com](http://www.ambhas.com), long term environmental observatory BVET [http://bvet.](http://bvet.obs-mip.fr) [obs-mip.fr](http://bvet.obs-mip.fr); [Braun et al., 2009; Ruiz et al., 2010; Violette et al.,](#page-11-0) [2010](#page-11-0)). It is intensively used for agro-hydrological, remote sensing and hydrological investigations [(Kumar et al., 2009)](#page-11-0). The land is used for agriculture and the crops are mostly rainfed or irrigated with groundwater. We used a total of 60 crop/soil/climate situations covering 4 crops across 3 years from May 2011 to Dec 2013 and 42 agricultural plots each approximately 1 ha in size, monitored for soil moisture and crop growth. Among them, 15 <span id="page-2-0"></span>crop/soil/climate situations from 12 plots were used for the calibration of STICS plant parameters (see Section 2.4). The inversions were performed on 45 crop/soil/climate situations from 33 plots. The results presented in the following will only concern the situations/plots used for the inversions.

The 4 crops studied have distinct characteristics (Table 1). Turmeric is an irrigated 8 months crop (May–December) while the 3 others are rainfed crops grown over 4 months (May to August for sunflower and sorghum and September–December for maize).

The climate is tropical semi-arid, dominated by south-west monsoon with a mean annual rainfall of 800 mm (coefficient of variation 0.28), and an annual Potential Evapotranspiration (PET Penman Method, [Penman, 1948)](#page-12-0) of 1100 mm (coefficient of variation 0.05), computed over 2005–2015. Daily records of air humidity, wind velocity, maximum and minimum air temperatures, precipitation and global radiation were obtained from an automatic weather station (CIMEL, type ENERCO 407 AVKP) and a meteorological flux tower (Astra Microwave, India) located in the study area. Measurements from the closest station were considered for each plot.

For the study period, the amount and distribution of rainfall and (Rain + Irrigation)/PET ratio varied across years and cropping seasons [(Table 2](#page-3-0)). This led to a varying degree of crop water stress experienced by the crops. 2012 was relatively dry as compared to 2011 and 2013 which can be classified as ʻnormal years'.

#### 2.2. Crops: management and LAI measurements

Information on management activities such as date and dose of sowing, fertilizing, irrigation and date of harvest were obtained during field visits. Sowing dates (expressed as day of the year) vary between 130 to 150 for sunflower and sorghum, between 110 and 124 for turmeric and between 250 and 262 for maize. Fertilizer is applied once at the beginning of the season, the quantity varying between 20 to 30 kg N/ha for sunflower, 30–50 kg N/ha for sorghum, 100–200 kg N/ha for turmeric and 25–50 kg N/ha for maize.

LAI was measured using a CI-202 Portable Leaf Area meter (CID Bioscience) and a LAI-2000 Plant Canopy Analyzer (LI-COR) every 10 days in 2011 and 2012, and every 20 days in 2013, concurrently with soil moisture measurements (see next section). Three measurements of LAI were taken in one representative sample area of 2 m2 and the mean value was used as representative of the plot.

Time series of LAI [(Fig. 1)](#page-3-0) obtained by interpolation of the measurements using a parametric growth curve approach [(Baret, 1986)](#page-11-0) revealed a large variability resulting mainly from interactions between crop, climate and soil type. It provides the basis for the determination of root zone soil water content properties from crop model inversion.

## 2.3. Soils: pedology, soil moisture measurements, reference AWC parameters values

Soils in the studied area are roughly classified as red soils (Alfisols, FAO) or black soils (Vertisols, FAO). According to the 1:50,000 scale soil map of the area prepared by Karnataka State Remote Sensing Application Center (KSRSAC), six categories are considered based on the particle size distribution of the top layer: Clay and Clay Loam for vertisols, Gravelly Loam Sand, Loamy Sand, Sandy Clay Loam and Sandy Loam for Alfisols. Sandy Clay Loam is the major soil class, covering 50% of the area. The soil is gravelly sandy loam at the hill slopes, sandy loam and sandy clay loam in the plains and clay loam and clay in the valley.

Surface soil moisture (SSM; typically from 0 to 10 cm deep) used for model inversion was measured with a ML2x Theta Probe Soil Moisture Sensor (Delta-T devices, sampling volume: 2.5 cm diameter, 6 cm long) and the mean of 3 measurements used as representative of each field plot. Additionally three soil samples per plot were collected for gravimetric soil moisture measurements. Theta Probe devices were calibrated twice a year using the gravimetric measurements: once during period of low soil moisture (before the start of the cropping season) and other during period of high soil moisture (during or at the end of the first cropping season). Profiles of soil moisture - used to determine in situ soil hydraulic properties – were also measured using soil moisture sensors (Trime-FM Field Portable TDR Meter, IMKO Micromodultechnik GmbH, sampling volume: 15 cm diameter, 18 cm long). The measurements were made at an increment of 10 cm from surface up to 1 m deep for shallow soils and up to 2 m for deeper soils. Both surface and profile soil moisture were measured throughout the year at a frequency of 10 days in 2011 to 2012 and 20 days in 2013. To capture the extreme values of soil moisture in both dry and wet conditions, surface and profile soil moisture were measured daily for a 30 days period once in October 2011 and once in August 2013.

To compare the estimated values of soil properties retrieved from model inversion to 'observed values', water content at field capacity (hFC), wilting point (hWP) and soil depth (DL) were determined from in situ measurements on the monitored plots [(Table 3)](#page-3-0). As proposed by [Hunt et al. (2009)](#page-11-0) and [Martinez-Fernandez et al.](#page-12-0) [(2015),](#page-12-0) hFC and hWP were inferred from long term soil moisture data: hFC as the 'minimum of maximum value' of the layer soil moisture in the growing season, while discarding soil moisture data immediately after a rainfall event (or irrigation event), and hWP as the '5th percentile of the minimum values' of the layer soil moisture in the growing season. Our time series of soil moisture exhibited alternate wetting and drying cycles, thus capturing both maximum and minimum soil water content. Bulk density was determined as the ratio of volumetric soil moisture (from TDR measurements) to gravimetric soil moisture (measured on soil samples). The depth of soil layers was determined by soil augering. The depth of soil from surface to weathering zone varied from 70 cm to 150 cm and was independent of the soil type.

## 2.4. Model and parameters

The STICS crop model [(Brisson et al., 1998; Coucheney et al.,](#page-11-0) [2015](#page-11-0)) is a daily time-step model which simulates the functioning of a soil-crop system over a single or several successive crop cycles. It has been successfully used for spatial applications and coupled with hydrological models at the catchment scale [(Beaujouan](#page-11-0) [et al., 2001](#page-11-0)). The upper boundary conditions are governed by standard climatic variables (radiation, maximum and minimum air temperatures, rainfall, potential evapotranspiration) and the lower boundary condition is the soil/sub-soil interface. We used the Pen-

Table 1

Monitored plots and vegetation measurements from 2011 to 2013. (LAI – Leaf Area Index; SSM – Surface Soil Moisture).

| Crop      | Number of situations monitored | Growing season        | Average length of the growing period | Avg. number of LAI/SSM Observations per situation |
|-----------|--------------------------------|-----------------------|--------------------------------------|---------------------------------------------------|
| Turmeric  | 17                             | May to December       | 240 days                             | 10                                                |
| Sunflower | 11                             | May to August         | 110 days                             | 8                                                 |
| Sorghum   | 9                              | May to August         | 110 days                             | 8                                                 |
| Maize     | 8                              | September to December | 100 days                             | 7                                                 |

#### <span id="page-3-0"></span>Table 2

Cumulated Rain, Potential Evapotranspiration (PET Penman Method, [Penman, 1948](#page-12-0)), Irrigation and (Rain + Irrigation)/PET ratio over the corresponding growing season for turmeric, sunflower, sorghum and maize crops for 2011, 2012 and 2013 in the Berambadi catchment.

| Variable                | 2011 |      | 2012    |      |      |         | 2013 |      |         |
|-------------------------|------|------|---------|------|------|---------|------|------|---------|
|                         | S1   | S2   | S1 + S2 | S1   | S2   | S1 + S2 | S1   | S2   | S1 + S2 |
| Rain (mm)               | 520  | 321  | 841     | 302  | 282  | 584     | 557  | 301  | 858     |
| Irrigation (mm)         | 0    | 0    | 170     | 0    | 0    | 165     | 0    | 0    | 90      |
| PET (mm)                | 347  | 351  | 698     | 366  | 341  | 707     | 342  | 344  | 686     |
| (Rain + Irrigation)/PET | 1.50 | 0.91 | 1.45    | 0.83 | 0.83 | 1.06    | 1.63 | 0.88 | 1.38    |

S1 - Season-1: May to August (sunflower and sorghum).

S2 - Season-2: September to December (maize).

S1 + S2: May to December (turmeric).

![](_page_3_Figure_7.jpeg)

Fig. 1. LAI curves for (a) sunflower, (b) sorghum, (c) turmeric and (d) maize showing the variability of LAI between plots and crops. Abcissa represents time expressed in Thermal Degree Days (summation of air temperature above a crop-specific base temperature) from sowing to maturity.

#### Table 3

Range of observed values of Field Capacity and Wilting Point obtained from long term soil moisture observations (2011–2014) and AWC (computed using Eq. [(1)](#page-4-0)) for different soil types in the 33 plots. Field Capacity and Wilting Point values are presented in gravimetric unit, the unit used in the model STICS.

| Soil type/parameter | No of plots | Soil moisture at field capacity hFC (g/g) | Soil moisture at wilting point hWP (g/g) | Available water content AWC (mm) |
|---------------------|-------------|-------------------------------------------|------------------------------------------|----------------------------------|
| Sandy Loam          | 11          | 14.0–19.5                                 | 4.5–7.5                                  | 127.0–215.0                      |
| Sandy Clay Loam     | 15          | 17.5–23.5                                 | 6.5–11.0                                 | 139.0–231.0                      |
| Clay Loam           | 7           | 22.5–30.0                                 | 10.5–12.5                                | 129.0–198.0                      |

man method to calculate potential evapotranspiration (PET; [Penman, 1948)](#page-12-0). Crops are described by their LAI, above-ground biomass and nitrogen content and the number and biomass of harvested organs. The main processes described are carbon assimilation and allocation to different organs and water and nitrogen balances (for detailed description, see [Brisson et al., 1998, 2008)](#page-11-0).

The different components of actual evapotranspiration (ET) are calculated from the potential evapotranspiration: soil evaporation (Es), plant transpiration (Tp) and evaporation from the water intercepted by the foliage that contributes to reducing the evaporative demand at the plant level. For Es, two stages are considered following rainfall: a first stage where the soil evaporates at the potential rate, and a second stage where evaporation is lower and decreases according to climate and type of soil. Crop water requirements (or maximum transpiration) are determined according to a crop coefficient approach which is well adapted to the crops considered herein [(Brisson et al., 1998, 2008)](#page-11-0). The actual plant transpiration Tp is based on the water physically available in the soil and the capacity of the plant to extract it, due to its root characteristics, corresponding to the concept of AWC (amount of water between field capacity hFC and wilting point hWP). The ratio of actual transpiration to maximal transpiration, is a bilinear function of the amount of water available in the rooting zone (with a minimum value of 0 when the soil water content is equal to hWP and a maximum value equal to (hFC-hWP)). The soil water content regarded as being the threshold between the maximal transpiration stage and the reduced transpiration stage depends on root density, stomatal functioning of the plant and climatic demand. Water stress indices are derived from those calculations and affect transpiration and different components of plant growth.

The soil is considered as a reservoir and is defined as a succession of up to five homogeneous layers characterized each by its retention capacity characteristics (hFC and hWP, bulk density and thickness). Water transfer downwards in the soil microporosity is <span id="page-4-0"></span>simulated on a one-dimensional regular mesh discretized per 1 cm step with a functional reservoir type model according to the tipping bucket concept. Incoming water fills the layers by downward flow, assuming that the upper limit of each single reservoir corresponds to the layer's field capacity.

The STICS model contains about 200 input parameters which are related to the characteristics of the plant, soil and crop management activities. The plant parameters for sunflower, sorghum, turmeric and maize related to leaf growth, biomass, yield, and root growth were calibrated with the OptimiSTICS software ([Buis](#page-11-0) [et al., 2011](#page-11-0)), using all the available data on a restricted number of plots that were therefore not used for inversions. With the calibrated model, the crop specific parameters can be assumed constant for the given crop for the study area. The parameters related to the agricultural practices (sowing dates, fertilization dates and doses, irrigation dates and doses and harvest dates) were set in accordance with the information collected from farmers.

In order to reduce the number of soil parameters to be potentially estimated, we adopted the simplified representation of the soil proposed by [Varella et al. (2010a):](#page-12-0) a surface layer and a second layer mainly representing the root zone. The first layer depth was set at 10 cm which is compatible both with our field measurements of SSM and the order of magnitude of SSM retrievals from radar remote sensing ([Jackson et al., 1995; Baghdadi and Zribi,](#page-11-0) [2006)](#page-11-0) for further applications at larger scale. Here we considered only the permanent soil properties related to water storage and transfers in the soil and restricted the estimation to five parameters: soil moisture at field capacity (hFC) and wilting point (hWP) of both layers and thickness of the second layer (DL2) (Table 4). These parameters describe the AWC (expressed in mm) of each layer which determines maximum water storage and available water for plant uptake as follow:

$$\mathbf{A}\mathbf{W}\mathbf{C} = (\theta_{\mathbf{f}\mathbf{C}} - \theta_{\mathbf{W}\mathbf{P}}) \cdot \mathbf{B}\mathbf{D} \cdot \mathbf{D}_{\mathbf{L}} \cdot \mathbf{1}\mathbf{0}^{-1} \tag{1}$$

where BD is the bulk density (g/cm3 ) and DL is the thickness (cm) of the layer.

These parameters influence also other processes such as soil evaporation, carbon and nitrogen cycle in the soil [(Brisson et al.,](#page-11-0) [2008)](#page-11-0). They are involved separately in some of these processes which bring independent constraints for their estimation. The soil input parameters non-estimated in the inversion process were obtained from local soil maps, soil experiments and standard values for soil classes (details are provided in Appendix-A).

## 2.5. Inversion method

Generalized Likelihood Uncertainty Estimation (GLUE) approach is an informal Bayesian method using prior information of parameter values for estimating model parameters [(Beven and](#page-11-0) [Binley, 1992; Makowski et al., 2002)](#page-11-0). Based on Monte Carlo simulation, GLUE transforms the problem of searching an optimal parameter set into searching sets of parameter values which would produce reliable simulations of the variables of interest ([Aronica](#page-11-0) [et al., 2002](#page-11-0)). GLUE based approaches have been successfully applied to hydrological models (e.g. [Li et al., 2010)](#page-11-0) and dynamic

## crop models [(Makowski et al., 2004; Guérif et al., 2006; Varella](#page-11-0) [et al., 2010a, 2010b; Sreelash et al., 2012)](#page-11-0).

Sets of parameters values are randomly chosen in a prior distribution representing the potential parameter space. These sets are then used in model simulations, which produce multiple sets of values of output variables of interest. These outputs are compared with measured values with an appropriate likelihood measure. The parameters values corresponding to the highest likelihoods are called acceptable or ''behavioural" values. The size of this ensemble is defined as a proportion of the total number of parameters values: the acceptable sample rate (ASR). The behavioural values are then used to determine the estimates of the parameters and their uncertainty bounds.

Prior information was defined here as independent uniform distributions whose bounds are the minimum and maximum of the observed values measured on a wide set of 60 plots (larger than the 33 considered in this study) in different soil types of the Berambadi catchment (Table 4). These lower and upper bounds of the parameters were decreased/increased by 10% to account for any errors in the measured soil moisture. The parameters sets were sampled in the prior distributions using Latin Hypercube Sampling (LHS; [McKay et al., 1979)](#page-12-0). An initial sample of size 20,000 was produced and then filtered to remove parameter combinations which were considered as not reasonable. The sampled combinations in which (hFC1 hWP1) 6 7.0 g/g and (hFC2 hWP2) 6 7.0 g/g were removed since these situations were never observed in the field experimental data. The simulations were carried out for the 9500 remaining samples.

We used the sum of absolute errors (SAE), proposed by [Brazier](#page-11-0) [et al. (2000)](#page-11-0) as the likelihood metric. SAE was calculated for each variable considered in the inversion for each model run as,

$$\mathbf{SAE}_i^k = \sum_{j=1}^{M_i} |\hat{\mathbf{y}}_{ij}^k - \mathbf{y}_{ij}| \tag{2}$$

where SAEk i is the sum of absolute errors for parameter set k, with k = 1 to N (N being the number of sets), variable i, with i = 1 to n (n being the total number of variables considered), and measurement date j, with j = 1 to Mi (Mi being the total measurements dates for the variable i), y^k i;j is the simulated value of variable i at date j for the parameter set k and yi;j is the measured value of variable i at date j.

Observations used to estimate soil parameters were made of a combination of two STICS output variables: SSM and LAI. On average, 10 observations of LAI and SSM were used in case of turmeric plots and 7 observations in the case of sunflower, sorghum and maize plots [(Table 1)](#page-2-0). The SAE values of SSM and LAI were normalized (RSAE) to take into account their varying units and magnitudes (Eq. (3)). We used a combined likelihood function by assigning weights to RSAE of LAI and SSM so as to take into account in an appropriate way the relative influence of these variables (Eq. [(4)](#page-5-0)). Based on the results of preliminary experiments carried out to study the influence of each variable on the parameter estimation (not reported here), we set w1 to 0.4 and w2 to 0.6.

Table 4

| The soil parameters of STICS model selected for estimation along with their initial ranges of values used as prior information. |  |  |  |
|---------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|---------------------------------------------------------------------------------------------------------------------------------|--|--|--|

| Parameter (name in STICS) | Definition                                 | Unit | Initial Range |
|---------------------------|--------------------------------------------|------|---------------|
| hFC1 (HCC(1))             | Water content at field capacity of layer 1 | g/g  | 10–32         |
| hFC2 (HCC(2))             | Water content at field capacity of layer 2 | g/g  | 10–32         |
| hWP1 (HMINF(1))           | Water content at wilting point of layer 1  | g/g  | 5–15          |
| hWP2 (HMINF(2))           | Water content at wilting point of layer 2  | g/g  | 5–15          |
| DL2 (EPC(2))              | Thickness of layer 2                       | cm   | 70–150        |

<span id="page-5-0"></span>
$$R\text{SAE}_i^k = \frac{\text{SAE}_i^k}{\sum_{k=1}^N \text{SAE}_i^k} \tag{3}$$

$$\text{CL}^k = \left(\text{w}_1 \ast \text{RSA}_{\text{LAl}}^k + \text{w}_2 \ast \text{RSA}_{\text{SSM}}^k\right)^{-1} \tag{4}$$

where w1 þ w2 ¼ 1.

ASR was set to 4% based on these preliminary experiments. The medians of the behavioural values were taken as the estimates of the parameters.

#### 2.6. Statistical criteria for assessing inversion performance

Several criteria are used for assessing the performance of the inversion process:

For each parameter and each inversion situation, a relative absolute error (RAE) was computed, based on the difference between estimated and observed values:

$$RAE_{i,p} = \text{abs}\left(\frac{\left(\chi_{i,p}^{\text{obs}} - \bar{\chi}_{i,p}^{\text{post}}\right)}{\chi_{i,p}^{\text{obs}}}\right) \tag{5}$$

where xobs i;p is the observed value of the soil parameter xi for a given plot p and xpost i;p is the corresponding value of the estimate obtained from the GLUE method.

A mean absolute error (MRAE) was computed as the mean of RAE of a given parameter xi for the different plots.

$$\text{MRAE}_{i} = \frac{1}{\mathcal{P}} \sum_{p=1}^{p} \text{RAE}_{i,p} \tag{6}$$

A relative error (REi) was used to quantify the improvement brought by the inversion process with respect to prior information. REi was computed here as the ratio of the MRAE calculated for the estimated parameter xpost i to that calculated for the prior information xprior i .

$$RE_i = \frac{\text{MRAE}(\bar{\mathbf{x}}_i^{\text{post}})}{\text{MRAE}(\bar{\mathbf{x}}_i^{\text{prior}})} \tag{7}$$

REi quantifies the improvement (REi < 1) or degradation (REi P 1) in the estimate of parameter xi with respect to prior information [(Varella et al., 2010a)](#page-12-0).

As an alternative to RE, the information brought by the inversion process in the parameter estimate was also assessed, for each parameter and each inversion situation, by comparing the standard deviation of the prior and posterior parameter distributions, using a normalized standard deviation given in Eq. (8):

$$
\sigma_{\text{norm}_{i,p}} = \frac{\sigma_{\text{s}^{\text{sout}}_{i,p}}}{\sigma_{\text{s}^{\text{stor}}_{i,p}}} \tag{8}
$$

rnormi;p quantifies the reduction (rnormi;p < 1Þ or increase (rnormi;p > 1Þ in the uncertainty of the estimate of parameter xi with respect to this of its prior information.

## 2.7. Sensitivity analysis

We performed a sensitivity analysis to assess the information content of LAI and SSM observations for estimating AWC components [(Varella et al., 2010a](#page-12-0)). Sobol' main sensitivity indices [(Saltelli et al., 2008](#page-12-0)), which measure the part of variance of simulated outputs explained by the parameters independently from each other, were estimated using the EASI (effective algorithm for computing global sensitivity indices) method [(Plischke, 2010](#page-12-0)). The main advantage of this method is that it does not require any specific numerical experiment design for the estimation of the indices. They have thus been computed at no extra cost using all the simulations performed for the model inversions. Nonnormalized Sobol' indices were used (i.e. Sobol' indices multiplied by the total variance of SSM/LAI) to visualize the variance explained by each parameter and not ʻjust' the proportion of total variance they explain.

## 3. Results

#### 3.1. Accuracy of estimated soil properties

The mean value of RAE on the 45 situations ranged between 0.13 and 0.21 depending on the estimated parameter (Fig. 2). Estimation of field capacity of both layers (hFC1 and hFC2) showed relatively lower RAE (mean RAE < 0.15) as compared to the other parameters (0.19 for hWP1 and DL2, 0.21 for hWP2). The standard deviation of RAE varied between 0.1 and 0.24. hFC1 and hFC2 exhibited relatively lower error variability than the other parameters. However, the quality of estimation of all the parameters varied significantly depending on the situations and RAE inferior to 10% could be obtained for all parameters.

The RE in the estimations was less than 1.0 for all parameters [(Fig. 3)](#page-6-0), indicating that the inversion improved the accuracy of all the estimated parameters with respect to the mean of the joint prior distribution. The RE in the estimation was the lowest for hFC1 (0.58) and similar for hWP1, hFC2 and DL2 (mean value approximately 0.76). For all the parameters RE was less than 0.80, which is a substantial improvement in the estimation of the parameters with respect to their prior information.

Normalized standard deviation (rnorm) was largely inferior to 1 for hFC1 and hWP1 [(Fig. 4](#page-6-0)), which means a significant reduction in the uncertainty of their estimated values as compared to the uncertainty associated with the prior information. The reduction of uncertainty for the second layer parameters (hFC2, hWP2 and DL2) was not so significant. The relatively larger variability of rnorm in the case of hWP1, hFC2 and hWP2 shows that under certain conditions the uncertainty in the estimates reduced significantly while in some cases the reduction in uncertainty is only marginal or nil. The level of uncertainty in DL2 is globally closer to that of prior information even if it can reach 70–80% of prior information uncertainty in some cases.

![](_page_5_Figure_26.jpeg)

Fig. 2. Boxplot of the Relative Absolute Error (RAE, Eq. (5)) in the estimation of soil parameters for 45 situations (All Crops), * is the mean value of the RAE (MRAE), + represents outliers.

<span id="page-6-0"></span>![](_page_6_Figure_1.jpeg)

Fig. 3. Relative error (RE, Eq. [(7))](#page-5-0) in the estimation of soil parameters.

![](_page_6_Figure_3.jpeg)

Fig. 4. Boxplot of the normalized standard deviation (rnorm, Eq. [(8))](#page-5-0) of the parameter estimates on the 45 situations, * is the mean value, + represents outliers.

3.2. Effect of crop type

The crop type used for inversion plays an important role in the quality of estimation of the parameters. This is evident from the consistently lower MRAE of the parameters, except for hFC1, obtained with maize crop as compared to those obtained with the other crops (Fig. 5).

The MRAE in the estimation of all parameters except hFC1 were nearly half for maize than that of the other crops, reaching values of about 10%. One of the main differences between maize and the other crops concerning the link between root zone hydraulic properties and crop growth is the water regime experienced by these crops. Due to both climatic conditions (sunflower and sorghum are grown in rainy season) and management options (irrigation is mainly devoted to turmeric as it is a cash crop), maize faces drier conditions than the other crops. Average (Rain + irrigation)/PET ratio was 0.87 for maize against 1.32 for sunflower and sorghum, and 1.3 for turmeric. STICS model simulations [(Fig. 6)](#page-7-0) confirmed that maize experienced the maximum stress (both in intensity and duration) as compared to other crops. All maize plots experienced water stress, while for the other crops, the variability of water stress index values is relatively higher, indicating that they experienced different levels of stress depending on year, soil type or farming practices.

The quality of estimation of hFC1 was on the contrary better with sunflower and sorghum as compared to turmeric and maize. Higher rainfall (and hence higher frequency of high moisture content conditions in the first layer) occurred during the cropping season of sunflower and sorghum which would have favored the estimation of hFC1 since SSM observations can be seen as a proxy of hFC1 in these conditions. For maize, soil moisture data used for inversion have not attained the actual values of field capacity for all situations (results not shown).

#### 3.3. Effect of water regime

[Fig. 7](#page-7-0) shows dynamics of sensitivity indices of LAI and SSM simulated by the STICS model to the estimated parameters for a maize

![](_page_6_Figure_11.jpeg)

Fig. 5. Boxplot of RAE in estimation of (a) hFC1, (b) hWP1, (c) hFC2, (d) hWP2 and (e) DL2, for (i) sunflower, (ii) sorghum, (iii) turmeric and (iv) maize, * is the mean value (MRAE), + represents outliers.

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

Fig. 6. Variability of simulated water stress between plots in terms of (a) maximum water stress index during crop cycle, (b) minimum water stress index during crop cycle and (c) percentage number of days S of the crop cycle for which stress index is inferior to 0.6, for (i) all crops (45 situations), (ii) sunflower, (iii) sorghum, (iv) turmeric and (v) maize. The water stress index in STICS model expresses the reduction of plant transpiration as compared to a potential and varies from 0 to 1, 0 being the highest stress and 1 indicating no stress. * is the mean stress, + represents outliers.

![](_page_7_Figure_3.jpeg)

Fig. 7. Temporal variations of (non-normalized) Sobol' main sensitivity indices of (a) SSM and (b) LAI to soil hydraulic parameters and 2nd layer depth during the entire simulation period for one plot of maize crop. Solid black curves represent the mean of simulated (a) SSM and (b) LAI. Bar chart in (a) represents the rainfall (in cm). Dashed black curve in (b) represents the mean of simulated water stress.

plot, representative of the maize plots used in this study. The variance of SSM explained by the variations of hFC1 clearly follows the dynamic of simulated SSM: the wetter is the first layer the more the simulated soil moisture is sensitive to hFC1. This confirms that SSM observed during wet situations contains more information to estimate this parameter.

The influence of the other parameters (hWP1 and second layer parameters) on simulated SSM starts with the first period of dryness faced by the crop (days 80–95) which coincides with the beginning of a long water stress period (Fig. 7a). It increases significantly during the senescence period (days 100–150) which is marked by a second period of dryness and a continuous increase of water stress. In dry conditions the level of hWP1 limits plant water uptake in layer one and thus directly affects its moisture content. Second layer parameters also affect SSM by limiting available water capacity and plant water uptake in second layer and thus by modifying the repartition of plant water uptake between both layers.

The dynamics of sensitivity indices of LAI to the estimated parameters follow that of the simulated water stress. In this case, LAI is only sensitive to parameters relative to the second layer indicating that AWC2 (available water capacity of layer-2, which represents the major part of total AWC) plays a major role in the dynamics of LAI when the crop is affected by water stress, as it occurs in this case after the maximum LAI (days 100–150, Fig.7b). Before this period, the water stress is nil and the sensitivity of LAI to the estimated parameters is very low.

These results show that the levels of information content in LAI and SSM observations to estimate AWC components are strongly linked with the water regime and its interaction with the crop growth. This has been observed for all the situations although the dynamics and levels of sensitivity indices vary depending on the situations and crops (not shown here).

The impact of the water regime and its interaction with crop growth on the quality of AWC components estimation is illustrated and quantified in the following subsections.

#### 3.3.1. Surface layer properties

As a consequence of the linked patterns of sensitivity of simulated SSM to first layer parameters and SSM value, the quality of estimation of hFC1 and hWP1 showed a high dependence on the status of water content in the first layer [(Fig. 8)](#page-8-0).

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Fig. 8. Boxplot of RAE in the estimation of (a) hFC1 for different situations of N, (i) N = 0 (17 Plots), (ii) N = 1–2 (14 Plots) and (iii) N > 2 (14 Plots), N being the number of observations of SSM measured when the first layer water content simulated by the model from measured SHPs falls within ±10% of hFC1 values and (b) hWP1 for different situations of N, (i) N = 0 (21 Plots), (ii) N = 1–2 (14 Plots) and (iii) N > 2 (10 Plots), N being the number of observations of SSM measured when the first layer water content simulated by the model from measured SHPs was less than half of hFC1. * is the mean value (MRAE), + represents outliers.

Inversions performed on dry situations (where SSM values were always far from hFC1) yielded poor estimates of hFC1. On the contrary, situations where at least 3 SSM observations were available when the first layer was wet (SSM values close to hFC1) provided particularly good estimates of hFC1 with an error of about 5% in mean and inferior to 10% in most cases.

As expected, the opposite behavior was observed for hWP1 since the sensitivity of simulated SSM to hWP1 was found to be negatively correlated to SSM values [(Fig. 7](#page-7-0)a). Situations in which at least one observation of SSM was available during period of dryness provided better estimates of hWP1 than the other situations (Fig. 8b), with errors reduced by approximately half.

#### 3.3.2. Second layer properties

Fig. 9 shows that the quality of estimation of the second layer properties was related to the water stress experienced by the crop. Better results were obtained on situations experiencing large water stress compared to those obtained on situations with nil or limited water stress. The level of water stress experienced by the crop was quantified by S, the proportion of days in the crop cycle when the simulated water stress index was less than 0.6 (1 corresponds to no

![](_page_8_Figure_8.jpeg)

Fig. 9. MRAE in the estimation of 2nd layer parameters (hFC2, hWP1 and DL2) for three levels of water stress experienced by the crops. 'S' is the percentage number of days of the cropping seasons that undergo significant water stress (stress index value below 0.6).

stress and values tending to 0 to very high stress). The error, expressed as MRAE, was relatively lower in situations where S > 20% as compared to situations where S < 20%. In situations where S > 20% there was a substantial improvement in the quality of estimation of hFC2 and hWP2, while DL2 showed only a marginal improvement. The MRAE in the estimation of hWP2 was reduced by more than half in case of S > 20% as compared to situations where S = 0, reaching a value inferior to 15%. MRAE of hFC2 was about 10% for S > 20%. Similar results were obtained when considering MRAE as a function of minimum stress values (not shown).

[Fig. 10](#page-9-0) shows that the RAE of the estimation of second layer properties was negatively correlated with the number of observations of LAI available when the simulated water stress index was below 0.60. Situations in which at least one LAI observation was available during a period of crop stress considerably improved the estimation of hWP2. For hFC2 at least 2 observations of LAI during a period of crop stress were necessary to obtain results significantly better than when using observations done during periods without stress. We still notice that the estimation of DL2, even though it is slightly better when LAI observation are made during stressed periods, still remains poorer than that of hFC2 and hWP2.

## 4. Discussion

#### 4.1. Accuracy of estimated soil properties

We have shown that in favorable conditions crop model inversion using observations potentially available from remote sensing may lead to reasonably accurate estimations of AWC components of two-layered soils and this even using limited number of observations. Most of the studies dedicated to the estimation of soil hydraulic properties or AWC components from model inversion using observations potentially available from remote sensing are based on synthetic dataset [(Jhorar et al., 2002, 2004; Montzka](#page-11-0) [et al., 2011; Bandara et al., 2013](#page-11-0)) or on very limited number of real cases [(Charoenhirunyingyos et al., 2011; Sreelash et al., 2012; Shin](#page-11-0) [et al., 2012; Bandara et al., 2014, 2015)](#page-11-0). However, assessing the interest of such methods requires their evaluation on large and diverse datasets. This study represents a contribution toward this assessment and confirms the potential utility of this method.

<span id="page-9-0"></span>![](_page_9_Figure_1.jpeg)

Fig. 10. Box plot shows the RAE in the estimation of (a) hFC2 (b) hWP2 and (c) DL2 for different situations of N, (i) N = 0 (26 Plots), (ii) N = 1 (7 Plots) and (iii) N > 1 (12 Plots). N is the number of observations of LAI measured when simulated water stress index is below 0.6. * is the mean value (MRAE), + represents outliers.

Further improvements of the estimation errors are still attainable by increasing the level of information used for the inversion. In addition to observations of model outputs, prior information on estimated parameters may be used in the inversion process to better constrain the estimations. A few recent studies [(Scharnagl](#page-12-0) [et al., 2011; Scholer et al., 2011](#page-12-0)), mainly using hydrological models, have proposed to use soil maps or local texture measurements combined with hydraulic properties databases or pedotransfer functions to constrain the inversion problem by using informative prior distributions in Bayesian inversion systems. This may be particularly helpful for reducing equifinality problems. Thanks to the various - and sometimes independent - roles played by AWC components in the model, the decoupling in space and time of the hydric processes affecting the two layers, and the availability of both SSM and LAI observations in humid and dry conditions, the potential compensation effects between AWC components were limited. However, compensative effects may still occur in some situations and such an additional information could also help in estimating additional parameters such as bulk density. The evaluation of the potential of such approaches on large real datasets and using commonly available data as source of constraints constitutes one of the next key methodological challenges for the estimation of AWC components from crop model inversion.

#### 4.2. Effect of water regime and its interaction with crop type

We found that the quality of estimation of AWC components was largely dependent on the water regime and its interaction with crop type: field capacity of surface layer was better estimated in wet conditions whereas wilting point of surface layer and deeper layer properties were better estimated in dry conditions and with crops facing water stress. This confirms on a large set of real data what was partially suggested in [Jhorar et al. (2002), Varella](#page-11-0) [et al. (2010b) and Bandara et al. (2013)](#page-11-0) mostly on synthetic datasets. Our sensitivity analysis suggested that this was due to the variation of the level of information content in LAI and SSM observations. If water inputs from rain or irrigation are not sufficient for ensuring optimal crop growth then crop growth is highly dependent to AWC and vegetation measurements bring significant information, particularly on the layers mostly representative of the root zone. On the contrary if SSM can be seen as a proxy of surface field capacity in wet conditions, its information content to estimate this property decreases in dry conditions. This sensitivity analysis also shed light on the results obtained by [Sreelash et al. (2012)](#page-12-0) about the complementarity of SSM and LAI observations. In a more general way, these results confirm the interest of using multiple remotely-sensed constraints for the estimation of root-zone soil moisture and associated soil properties in model-data fusion systems and the dependency of their information content on the vegetation state and soil moisture conditions [(Barrett and Renzullo,](#page-11-0) [2009; Van Dijk and Renzullo, 2011](#page-11-0)).

Situations which experience large water stress and include wetting and drying cycles are thus optimal observational objects for estimating AWC components of multi-layered soils from crop model inversion. The complementary use of a few SSM observations in wet conditions and LAI observations during water stress period bring significant level of information for their estimation.

#### 4.3. Impact of errors on the results

The results of the inversions presented in this study are also impacted by different types of error:

- (i) model errors (including both errors in the values set for input parameters that are not estimated in the inversions and errors in model equations);
- (ii) observation errors, i.e. errors on measured LAI and SSM used in the inversions; and
- (iii) reference values errors, i.e. errors on the 'observed' values of the AWC components that are compared to the estimated parameters for assessing their quality.

Model errors may be linked with model complexity. Complex crop models have been built to mimic as realistically as possible the different processes involved in crop growth and its interaction with its environment but the resulting high number of parameters increases the degrees of freedom in model calibration process and the amount of information needed to feed the model. This may contribute to decrease model robustness [(Confalonieri et al.,](#page-11-0) [2012](#page-11-0)). The crop model used in this study is representative of the the way parameters and input variables non estimated in the inversion process are set is conform to the usual practices. Obviously, the limits of the plant parameters calibration process and the errors on the information used to set its other entries impact the model simulations as well as do the errors in its equations. The inversions are based on the computation of the differences between simulated and observed values of SSM and LAI (SAESSM and SAELAI, Eq. [(2)](#page-4-0)). This computation is affected in the same way by model and observation errors and these errors may be compensated by unrealistic values of the inversed parameters. Errors on SAESSM and SAELAI have been approximated for each situation by comparing the observed and simulated values of LAI and SSM, using the reference values of AWC components in simulations. As expected, large SAE errors on LAI and/or SSM often lead to large errors in the estimated parameters that are sensitive to these variables (results not shown). As practical applications of the method are likely to include situations with large model and/or observation errors, we didn't remove such situations from our analysis, to evaluate as fairly as possible the performance we can expect from this method. Ensemble modelling has recently shown to be an efficient way of improving crop simulation [(Martre et al., 2015)](#page-12-0). Although it would be cumbersome to implement, using several models could be considered in an inversion process to reduce the impact of model error.

Reference values errors may impact the evaluation of the quality of parameters estimate. Particularly, the lesser reliability of DL2 measurements in field conditions, as it is difficult to estimate by augering the precise depth of the base of the soil profile, may partly explain that its estimation still remains poorer than that of hFC2 and hWP2. In addition, DL2 estimate from inversion represents an effective soil thickness that might be far from the value assessed in field conditions. Some particular situations may create such discrepancy between effective and measured values: presence of an obstacle that prevents the roots to attain the base of the soil profile and limits the effective AWC, or presence of a transient perched water table connected with the base of the profile that allows a larger effective AWC than observed.

# 4.4. Practical application of the method on agricultural catchments

The results presented in this study contribute to evaluate the potential of AWC components retrieval from crop model inversion and may help to define optimal configuration for the application of this method on agricultural catchments. This next step is challenging but necessary to bring solutions to the issue of monitoring water resources in irrigated agricultural catchments.

Application of this method for deriving soil maps of AWC components would require the use of SSM and LAI data retrieved from remote sensing. The method presented here is directly applicable with remote sensed data and the benefit of using them has already been shown in other studies [(Santanello et al., 2007;](#page-12-0) [Charoenhirunyingyos et al., 2011; Ines et al., 2013; Bandara et al.,](#page-12-0) [2015](#page-12-0)). In tropical regions, where cloudy conditions are frequent, SSM and LAI are attainable from radar remote sensing (e.g. [Wagner et al., 1999; Tomer et al., 2015](#page-12-0) for SSM; [Kim et al., 2012;](#page-11-0) [Hirooka et al., 2015](#page-11-0) for LAI).

Crop model inputs such as climate or farming practices are often less precisely known at the territory scale than at point scale. The level of precision of the available information on these inputs may impact crop models simulations [(Jégo et al., 2015)](#page-11-0). Additional studies would be required to assess the influence of these uncertainties on the results of the inversions to evaluate to what extent they impact the quality of AWC components retrieval.

Finally, systematic multi-local application of this method in its current configuration for deriving soil maps of AWC components in agricultural catchments may face the problem of vegetation types or crops non-represented in the model and of the dependence of its performance to the agro-pedo-climatic conditions on which it is applied. It may thus advantageously be combined with advanced geostatistical methods able to take into account in an optimal way all kind of existing soil information [(McBratney et al., 2003)](#page-11-0). In this context, the results presented in this study may guide the sampling of representative fields over a territory to use this technique for soil mapping exercise.

# 5. Conclusion

In this study we evaluated on an extensive field experiment the potential of crop model inversion for estimating AWC components on two-layered soils with observations potentially accessible from remote sensing.

We have shown that:

- (1) the quality of estimation of AWC components varied depending on the situations on which it was estimated. These estimations were however systematically better than the prior information used although this prior information was already of relatively good quality;
- (2) the quality of estimation of AWC components was found to largely depend on the water regime and its interaction with crop type: field capacity of surface layer was better estimated in wet conditions and irrigated or rainy season crops whereas wilting point of surface layer and deeper layer properties were better estimated in dry conditions and with crops facing water stress;
- (3) using simultaneously LAI and SSM observations allowed to obtain mean relative absolute error of 5% for field capacity of surface layer, 10% for field capacity of root zone, 15% for wilting point of surface layer and root zone, and 20% for soil depth, in favorable conditions; and
- (4) a few observations of LAI and SSM available in favorable conditions were sufficient to largely improve the estimation of AWC components.

We confirmed the utility of the inversion of crop-models to provide realistic soil-water properties and further improvements such as inclusion of informative prior distributions or reduction of model error are still conceivable. Further studies are however needed to apply this method for deriving soil maps of AWC components at agricultural catchment scale. Such improvements will allow deriving accurate maps of soil AWC at the catchment scale, which are essential for distributed hydrological models aimed at studying the impact of agriculture on water resource in tropical catchments.

# Acknowledgements

The funding provided by CNES (Centre National d'Etudes Spatiales) to the first author for carrying out post-doctoral research is gratefully acknowledged. Apart from the specific support from the French Institute of Research for Development (IRD), the Embassy of France in India and the Indian Institute of Science, the research was funded by the Environmental Research Observatory BVET [(http://bvet.obs-mip.fr/en)](http://bvet.obs-mip.fr/en), the Indo-French program IFCPAR (Indo-French Center for the Promotion of Advanced Research) through the project 4700WA ''Adaptation of Irrigated Agriculture to Climate Change" (AICHA) and by the INRA Metaprogramme ACCAF. The authors would like to thank the members of the field team: Amit Kumar Sharma, Arun Raju, P. Giriraj and K. N. Sanjeeva Murthy and the farmers for the help provided during <span id="page-11-0"></span>the field experiments. Finally, the authors thank the editor, the associate editor and two anonymous reviewers for their constructive comments which helped us to substantially improve this manuscript.

#### Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at [http://dx.doi.org/10.1016/j.jhydrol.2016.12.](http://dx.doi.org/10.1016/j.jhydrol.2016.12.049) [049](http://dx.doi.org/10.1016/j.jhydrol.2016.12.049).

#### References

- [Anuraga, T.S., Ruiz, L., Kumar, M.S.M., Sekhar, M., Leijnse, A., 2006. Estimating](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0005) [groundwater recharge using land use and soil data: a case study in South India.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0005) [Agric. Water Manage. 84, 65–76.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0005)
- Aronica, G., Bates, P.D., Horritt, M.S., 2002. Assessing the uncertainty in distributed model predictions using observed binary pattern information within GLUE. Hydrol. Process. 16 (10), 2001–2016. [http://dx.doi.org/10.1002/hyp.398.](http://dx.doi.org/10.1002/hyp.398)
- Baghdadi, N., Zribi, M., 2006. Evaluation of radar backscatter models IEM, Oh and Dubois using experimental observations. Int. J. Remote Sens. 27 (18), 3831– 3852. [http://dx.doi.org/10.1080/01431160600658123.](http://dx.doi.org/10.1080/01431160600658123)
- Bandara, R., Walker, J.P., Rudiger, C., 2013. Towards soil property retrieval from space: a one dimensional twin experiment. J. Hydrol. 497, 198–207. [http://dx.](http://dx.doi.org/10.1016/j.jhydrol.2013.06.004) [doi.org/10.1016/j.jhydrol.2013.06.004](http://dx.doi.org/10.1016/j.jhydrol.2013.06.004).
- Bandara, R., Walker, J.P., Rudiger, C., 2014. Towards soil property retrieval from space: proof of concept using in situ observations. J. Hydrol. 512, 27–38. [http://](http://dx.doi.org/10.1016/j.jhydrol.2014.02.031) [dx.doi.org/10.1016/j.jhydrol.2014.02.031](http://dx.doi.org/10.1016/j.jhydrol.2014.02.031).
- Bandara, R., Walker, J.P., Rudiger, C., Merlin, O., 2015. Towards soil property retrieval from space: an application with disaggregated satellite observations. J. Hydrol. 522, 582–593. <http://dx.doi.org/10.1016/j.jhydrol.2015.01.018>.
- Baret, F., 1986. Contribution au suivi radiométrique de cultures de céréales. Phd Thesis Submitted to University of Paris South (Université Paris Sud).
- [Barrett, D.J., Renzullo, L.J., 2009. On the efficacy of combining thermal and](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0040) [microwave satellite data as observational constraints for root-zone soil](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0040) [moisture estimation. J. Hydrometeorol. 10 (5), 1109–1127.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0040)
- Beaujouan, V., Durand, P., Ruiz, L., 2001. Modelling the effect of the spatial distribution of agricultural practises on nitrogen fluxes in rural catchments. Ecol. Model. 137 (1), 93–105. [http://dx.doi.org/10.1016/S0304-3800(00)00435-X.](http://dx.doi.org/10.1016/S0304-3800(00)00435-X)
- Beven, K.J., Binley, A.M., 1992. The future of distributed models: model calibration and uncertainty prediction. Hydrol. Process. 6 (3), 279–298. [http://dx.doi.org/](http://dx.doi.org/10.1002/hyp.3360060305) [10.1002/hyp.3360060305](http://dx.doi.org/10.1002/hyp.3360060305).
- Botula, Y.D., Cornelis, W.M., Van Ranst, E., 2012. Evaluation of pedotransfer functions for predicting water retention of soils in Lower Congo (D.R. Congo). Agric. Water Manag. 111, 1–10. <http://dx.doi.org/10.1016/j.agwat.2012.04.006>.
- Braga, R.P., Jones, J.W., 2004. Using optimization to estimate soil inputs of crop models for use in site-specific management. Trans. ASAE 47 (5), 1821–1831. <http://dx.doi.org/10.13031/2013.17599>.
- Braun, J.J., Descloitres, M., Riotte, J., Fleury, S., Barbiero, L., Boeglin, J.L., Violette, A., Lacarce, E., Ruiz, L., Sekhar, M., Kumar, M.S.M., Subramanian, S., Dupre, B., 2009. Regolith mass balance inferred from combined mineralogical, geochemical and geophysical studies: Mule Hole gneissic watershed, South India. Geochim. Cosmochim. Acta 73 (4), 935–961. <http://dx.doi.org/10.1016/j.gca.2008.11.013>.
- Brazier, R.E., Beven, K.J., Freer, J., Rowan, J.S., 2000. Equifinality and uncertainty in physical based soil erosion models: application of the GLUE methodology to WEPP-The Water Erosion Prediction Project-for sites in the UK and USA. Earth Surf. Proc. Land. 25, 825–845. [http://dx.doi.org/10.1002/1096-9837(200008)](http://dx.doi.org/10.1002/1096-9837(200008)25:8<825::AID-ESP101>3.0.CO;2-3) [25:8<825::AID-ESP101>3.0.CO;2-3](http://dx.doi.org/10.1002/1096-9837(200008)25:8<825::AID-ESP101>3.0.CO;2-3).
- Breda, N., Huc, R., Granier, A., Dreyer, E., 2006. Temperate forest trees and stands under severe drought: a review of ecophysiological responses, adaptation processes and long-term consequences. Ann. Forest Sci. 63 (6), 625–644. [http://](http://dx.doi.org/10.1051/forest:2006042) [dx.doi.org/10.1051/forest:2006042](http://dx.doi.org/10.1051/forest:2006042).
- Brisson, N., Mary, B., Ripoche, D., Jeuffroy, M.H., Ruget, F., Nicoullaud, B., Gate, P., Devienne-Baret, F., Antonioletti, R., Durr, C., Richard, G., Beaudoin, N., Recous, S., Tayot, X.P.D., Cellier, P., Machet, J.-M., Meynard, J.-M., Delecolle, R., 1998. STICS: a generic model for simulating crops and their water and nitrogen balances. I. Theory and parameterization applied to wheat and corn. Agronomie 18 (5–6), 311–346. <http://dx.doi.org/10.1051/agro:19980501>.
- [Brisson, N., Launay, M., Mary, B., Beaudoin, N., 2008. Conceptual Basis,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0085) [Formalisations and Parameterization of the STICS Crop Model. QUAE editions,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0085) [Versailles Cedex](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0085).
- Bruand, A., Fernandez, P.N., Duval, O., 2003. Use of class pedotransfer functions based on texture and bulk density of clods to generate water retention curves. Soil Use Manag. 19 (3), 232–242. [http://dx.doi.org/10.1111/j.1475-2743.2003.](http://dx.doi.org/10.1111/j.1475-2743.2003.tb00309.x) [tb00309.x.](http://dx.doi.org/10.1111/j.1475-2743.2003.tb00309.x)
- Buis, S., Wallach, D., Guillaume, S., Varella, H., Lecharpentier, P., Launay, M., Guerif, M., Bergez, J.-E., Justes, E., 2011. The STICS crop model and associated software for analysis, parameterization, and evaluation. In: Ahuja, L.R., Liwang Ma, dir., Methods of Introducing System Models into Agricultural Research. Advances in Agricultural Systems Modeling, vol. 2, pp. 395–426.
- Charoenhirunyingyos, S., Honda, K., Kamthonkiat, D., Ines, A.V.M., 2011. Soil moisture estimation from inverse modeling using multiple criteria functions. J. Comput. Electron. Agric. 75 (2), 278–287. [http://dx.doi.org/10.1016/](http://dx.doi.org/10.1016/j.compag.2010.12.004) [j.compag.2010.12.004.](http://dx.doi.org/10.1016/j.compag.2010.12.004)
- [Confalonieri, R., Bregaglio, S., Acutis, M., 2012. Quantifying plasticity in simulation](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0105) [models. Ecol. Model. 225, 159–166.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0105)
- Coucheney, E., Buis, S., Launay, M., Constantin, J., Mary, B., Cortazar-Atauri, I.G., Ripoche, D., Beaudoin, N., Ruget, N., Andrianarisao, K.S., Bas, C.L., Justes, E., Leonard, J., 2015. Accuracy, robustness and behaviour of the STICS soil-crop model for plant, water and nitrogen outputs: evaluation over a wide range of argo-environmental conditions in France. Environ. Modell. Software 64, 177– 190. [http://dx.doi.org/10.1016/j.envsoft.2014.11.024.](http://dx.doi.org/10.1016/j.envsoft.2014.11.024)
- [De Vries, J.J., Simmers, I., 2002. Groundwater recharge: an overview of processes](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0115) [and challenges. Hydrogeol. J. 10, 5–17](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0115).
- [Ferrant, S., Bustillo, V., Burel, E., Salmon-Monviola, J., Claverie, M., Jarosz, N., Yin, T.,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9000) [Rivalland, V., Dedieu, G., Demarez, V., Ceschia, E., Probst, A., Al-Bitar, A., Kerr, Y.,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9000) [Probst, J.L., Durand, P., Gascoin, S., 2016. Extracting Soil Water Holding Capacity](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9000) [Parameters of a Distributed Agro-Hydrological Model from High Resolution](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9000) [Optical Satellite Observations Series. Remote Sensing 8 (2), 154.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9000)
- [Guérif, M., Houlès, V., Makowski, D., Lauvernet, C., 2006. Data assimilation and](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0120) [parameter estimation for precision agriculture using the crop model STICS. In:](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0120) [Wallach, D., Makowski, D., Jones, J.W. (Eds.), Working with Dynamic Crop](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0120) [Models. Elsevier.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0120)
- [Hirooka, Y., Homma, K., Maki, M., Sekiguchi, K., 2015. Applicability of synthetic](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0125) [aperture radar (SAR) to evaluate leaf area index (LAI) and its growth rate of rice](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0125) [in farmers' fields in Lao PDR. Field Crops Res. 176, 119–122.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0125)
- Hunt, E.D., Hubbard, K.G., Wilhite, D.A., Arkebauer, T.J., Dutcher, A.L., 2009. The development and evaluation of a soil moisture index. Int. J. Climatol. 29 (5), 747–759. [http://dx.doi.org/10.1002/joc.1749.](http://dx.doi.org/10.1002/joc.1749)
- Ines, A.V.M., Mohanty, B.P., 2008. Near-surface soil moisture assimilation for quantifying effective soil hydraulic properties under different hydro-climatic conditions. Vadose Zone J. 7, 39–52. [http://dx.doi.org/10.2136/vzj2007.0048.](http://dx.doi.org/10.2136/vzj2007.0048)
- [Ines, A.V., Das, N.N., Hansen, J.W., Njoku, E.G., 2013. Assimilation of remotely sensed](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0140) [soil moisture and vegetation with a crop simulation model for maize yield](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0140) [prediction. Remote Sens. Environ. 138, 149–164.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0140)
- Jackson, T.J., Le Vine, D.M., Schmugge, T.J., Schiebe, F.R., 1995. Large area mapping of soil moisture using ESTAR passive microwave radiometer in Washita '92. Remote Sens. Environ. 53, 27–37. [http://dx.doi.org/10.1016/0034-4257(95)](http://dx.doi.org/10.1016/0034-4257(95)00084-E) [00084-E](http://dx.doi.org/10.1016/0034-4257(95)00084-E).
- [Jégo, G., Pattey, E., Mesbah, S.M., Liu, J., Duchesne, I., 2015. Impact of the spatial](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0150) [resolution of climatic data and soil physical properties on regional corn yield](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0150) [predictions using the STICS crop model. Int. J. Appl. Earth Obs. Geoinf. 41, 11–](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0150) [22.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0150)
- Jhorar, R.K., Bastiaanssen, W.G.M., Feddes, R.A., Van Dam, J.C., 2002. Inversely estimating soil hydraulic functions using evapotranspiration fluxes. J. Hydrol. 258 (1–4), 198–213. [http://dx.doi.org/10.1016/S0022-1694(01)00564-9.](http://dx.doi.org/10.1016/S0022-1694(01)00564-9)
- [Jhorar, R.K., Van Dam, J.C., Bastiaanssen, W.G.M., Feddes, R.A., 2004. Calibration of](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9005) [effective soil hydraulic parameters of heterogeneous soil profiles. Journal of](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9005) [Hydrology 285 (1), 233–247.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h9005)
- Jones, J.W., Antle, J.M., Basso, B., Boote, K.J., Conant, R.T., Foster, I., Keating, B.A., in press. Brief history of agricultural systems modeling. Agric. Syst. [http://dx.doi.](http://dx.doi.org/10.1016/j.agsy.2016.05.014) [org/10.1016/j.agsy.2016.05.014](http://dx.doi.org/10.1016/j.agsy.2016.05.014) (in press).
- [Kim, Y., Jackson, T., Bindlish, R., Lee, H., Hong, S., 2012. Radar vegetation index for](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0165) [estimating the vegetation water content of rice and soybean. IEEE Geosci.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0165) [Remote Sens. Lett. 9 (4), 564–568.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0165)
- [Kumar, S., Sekhar, M., Bandyopadhyay, S., 2009. Assimilation of remote sensing and](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0170) [hydrological data using adaptive filtering techniques for watershed modeling.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0170) [Curr. Sci. 97 (8), 1196–1202.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0170)
- [Lagacherie, P., McBratney, A.B., 2007. Spatial soil information systems and spatial](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0175) [soil inference systems: perspectives for digital soil mapping. In: Lagacherie, P.,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0175) [McBratney, A., Voltz, M. (Eds.), Digital Soil Mapping: An Introductory](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0175) [Perspective. Elsevier, Amsterdam, pp. 3–22.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0175)
- Lagacherie, P., Baret, F., Feret, J.-B., Netto, J.M., Robbez-Masson, J.M., 2008. Estimation of soil clay and calcium carbonate using laboratory, field and airborne hyperspectral measurements. Remote Sens. Environ. 112, 825–835. <http://dx.doi.org/10.1016/j.rse.2007.06.014>.
- Li, C., Ren, Li, 2011. Estimation of unsaturated soil hydraulic parameters using the ensemble kalman filter. Vadose Zone J. 10 (4), 1205–1227. [http://dx.doi.org/](http://dx.doi.org/10.2136/vzj2010.0159) [10.2136/vzj2010.0159](http://dx.doi.org/10.2136/vzj2010.0159).
- Li, L., Xia, J., Xu, C.Y., Singh, V.P., 2010. Evaluation of the subjective factors of the GLUE method and comparison with the formal Bayesian method in uncertainty assessment of hydrological models. J. Hydrol. 390 (3–4), 210–221. [http://dx.doi.](http://dx.doi.org/10.1016/j.jhydrol.2010.06.044) [org/10.1016/j.jhydrol.2010.06.044](http://dx.doi.org/10.1016/j.jhydrol.2010.06.044).
- McBratney, A.B., Minasny, B., Cattle, S.R., Vervoort, R.W., 2002. From pedotransfer functions to soil inference systems. Geoderma 109 (1–2), 41–73. [http://dx.doi.](http://dx.doi.org/10.1016/S0016-7061(02)00139-8) [org/10.1016/S0016-7061(02)00139-8](http://dx.doi.org/10.1016/S0016-7061(02)00139-8).
- McBratney, A.B., Santos, M.L.M., Minasny, B., 2003. On digital soil mapping. Geoderma 117 (1–2), 3–52. [http://dx.doi.org/10.1016/S0016-7061(03)](http://dx.doi.org/10.1016/S0016-7061(03)00223-4) [00223-4](http://dx.doi.org/10.1016/S0016-7061(03)00223-4).
- Makowski, D., Wallach, D., Tremblay, M., 2002. Using a Bayesian approach to parameter estimation; comparison of the GLUE and MCMC methods. Agronomie 22 (2), 191–203. [http://dx.doi.org/10.1051/agro:2002007.](http://dx.doi.org/10.1051/agro:2002007)
- [Makowski, D., Jeuffroy, M.H., Guérif, M., 2004. Bayesian methods for updating crop](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0210) [model predictions, applications for predicting biomass and grain protein](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0210) [content. In: van Boekel, M.A.J.S., Stein, A., Van Bruggen, A.H.C. (Eds.), Bayesian](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0210)

<span id="page-12-0"></span>[statistics and Quality Modelling in the Agro-Food Production Chain''. Kluwer](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0210) [Academic Publishers, pp. 57–68](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0210).

- Martinez-Fernandez, J., Gonzalez-Zamora, G., Sanchez, N., Gumuzzio, A., 2015. A soil water based index as a suitable agricultural drought indicator. J. Hydrol. 522, 265–273. [http://dx.doi.org/10.1016/j.jhydrol.2014.12.051.](http://dx.doi.org/10.1016/j.jhydrol.2014.12.051)
- [Martre, P., Wallach, D., Asseng, S., Ewert, F., Jones, J.W., Rötter, R.P., Hatfield, J.L.,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0220) [2015. Multimodel ensembles of wheat growth: many models are better than](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0220) [one. Glob. Change Biol. 21 (2), 911–925](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0220).
- [Mckay, M., Beckman, R., Conover, W., 1979. A comparison of three methods for](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0225) [selecting values of input variables in the analysis of output from a computer](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0225) [code. Technometrics 21, 239–245.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0225)
- Mohanthy, B.P., 2013. Soil hydraulic property estimation using remote sensing: a review. Vadose Zone J. 12 (4). [http://dx.doi.org/10.2136/vzj2013.06.0100.](http://dx.doi.org/10.2136/vzj2013.06.0100)
- Montzka, C., Moradkhani, H., Weihermuller, L., Franssen, H.H., Canty, M., Vereecken, H., 2011. Hydraulic parameter estimation by remotely-sensed top soil moisture observations with the particle filter. J. Hydrol. 399 (3–4), 410–421. [http://dx.](http://dx.doi.org/10.1016/j.jhydrol.2011.01.020) [doi.org/10.1016/j.jhydrol.2011.01.020](http://dx.doi.org/10.1016/j.jhydrol.2011.01.020).
- Nagarajan, K., Judge, J., Graham, W.D., Monsivais-Huertero, A., 2011. Particle filterbased assimilation algorithms for improved estimation of root-zone soil moisture under dynamic vegetation conditions. Adv. Water Resour. 34 (4), 433–447. <http://dx.doi.org/10.1016/j.advwatres.2010.09.019>.
- Penman, H.L., 1948. Natural evaporation from open water, bare soil and grass. Proc. Roy. Soc. London A(194), S. 120–145.
- Plischke, E., 2010. An effective algorithm for computing global sensitivity indices (EASI). Reliab. Eng. Syst. Safety 95 (4), 354–360. [http://dx.doi.org/10.1016/j.](http://dx.doi.org/10.1016/j.ress.2009.11.005) [ress.2009.11.005](http://dx.doi.org/10.1016/j.ress.2009.11.005).
- Ritter, A., Hupet, F., Munoz-Carpena, R., Lambot, S., Vanclooster, M., 2003. Using inverse methods for estimating soil hydraulic properties from field data as an alternative to direct methods. Agric. Water Manag. 59, 77–96. [http://dx.doi.org/](http://dx.doi.org/10.1016/S0378-3774(02)00160-9) [10.1016/S0378-3774(02)00160-9](http://dx.doi.org/10.1016/S0378-3774(02)00160-9).
- Ruget, F., Brisson, N., Delécolle, R., Faiver, R., 2002. Sensitivity analysis of a crop simulation model, STICS, in order to choose the main parameters to be estimated. Agronomie 22 (2), 133–158. [http://dx.doi.org/10.1051/](http://dx.doi.org/10.1051/agro:2002009) [agro:2002009](http://dx.doi.org/10.1051/agro:2002009).
- Ruiz, L., Varma, M.R.R., Kumar, M.S.M., Sekhar, M., Marechal, J.C., Descloitres, M., Riotte, J., Kumar, S., Kumar, C., Braun, J.J., 2010. Water balance modeling in a tropical watershed under deciduous forest (Mule Hole, India): regolith matric storage buffers the groundwater recharge process. J. Hydrol. 380, 460–472. <http://dx.doi.org/10.1016/j.jhydrol.2009.11.020>.
- [Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M.,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0270) [Tarantola, S., 2008. Global Sensitivity Analysis: The Primer. John Wiley & Sons,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0270) [West Sussex, England.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0270)
- Santanello Jr., J.A., Peters-Lidard, C.D., Garcia, M.E., Mocko, D.M., Tischler, M.A., Moran, M.S., Thoma, D.P., 2007. Using remotely-sensed estimates of soil moisture to infer soil texture and hydraulic properties across a semi-arid watershed. Remote Sens. Environ. 110 (1), 79–97. [http://dx.doi.org/10.1016/j.](http://dx.doi.org/10.1016/j.rse.2007.02.007) [rse.2007.02.007](http://dx.doi.org/10.1016/j.rse.2007.02.007).
- Satti, S., Jacobs, J.M., Irmak, S., 2004. Agricultural water management in a humid region: sensitivity to climate, soil and crop parameters. Agric. Water Manag. 70 (1), 51–65. [http://dx.doi.org/10.1016/j.agwat.2004.05.004.](http://dx.doi.org/10.1016/j.agwat.2004.05.004)
- Scharnagl, B., Vrugt, J., Vereecken, H., Herbst, M., 2011. Inverse modelling of in situ soil water dynamics: Investigating the effect of different prior distributions of the soil hydraulic parameters. Hydrol. Earth Syst. Sci. 15 (10), 3043–3059. [http://dx.doi.org/10.5194/hess-15-3043-2011.](http://dx.doi.org/10.5194/hess-15-3043-2011)
- [Scholer, M., Irving, J., Binley, A., Holliger, K., 2011. Estimating vadose zone hydraulic](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0290) [properties using ground penetrating radar: the impact of prior information.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0290) [Water Resour. Res. 47 (10)](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0290).
- Stumpp, C., Engelhardt, S., Hofmann, M., Huwe, B., 2009. Evaluation of pedotransfer functions for estimating soil hydraulic properties of prevalent soils in a

catchment of the Bavarian Alps. Eur. J. Forest Res. 128 (6), 609–620. [http://dx.](http://dx.doi.org/10.1007/s10342-008-0241-7) [doi.org/10.1007/s10342-008-0241-7.](http://dx.doi.org/10.1007/s10342-008-0241-7)

- Shin, Y., Mohanty, B.P., Ines, A.V.M., 2012. Soil hydraulic properties in onedimensional layered soil profile using layer-specific soil moisture assimilation scheme. Water Resour. Res. 48 (6). [http://dx.doi.org/10.1029/2010WR009581.](http://dx.doi.org/10.1029/2010WR009581)
- Sreelash, K., Sekhar, M., Ruiz, L., Kumar, Sat., Guerif, M., Buis, S., Durand, P., Gascuel-Odoux, C., 2012. Parameter estimation of a two-horizon soil profile by combining crop canopy and surface soil moisture observations using GLUE. J. Hydrol. 456–457, 57–67. [http://dx.doi.org/10.1016/j.jhydrol.2012.06.012.](http://dx.doi.org/10.1016/j.jhydrol.2012.06.012)
- [Sreelash, K., Sekhar, M., Ruiz, L., Buis, S., Bandyopadhyay, S., 2013. Improved](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0310) [modeling of groundwater recharge in agricultural watersheds using a](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0310) [combination of crop model and remote sensing. J. Indian Inst. Sci. 93 (2),](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0310) [189–207](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0310).
- Steele-Dunne, S.C., Rutten, M.M., Krzeminska, D.M., Hausner, M., Tyler, S.W., Selker, J., Bogaard, T.A., van de Giesen, N.C., 2010. Feasibility of soil moisture estimation using passive distributed temperature sensing. Water Resour. Res. 46 (3). <http://dx.doi.org/10.1029/2009WR008272>.
- [Tomer, S.K., Al Bitar, A., Sekhar, M., Zribi, M., Bandyopadhyay, S., Sreelash, K.,](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0320) [Sharma, A.K., Corgne, S., Kerr, Y., 2015. Retrieval and multi-scale validation of](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0320) [soil moisture from multi-temporal SAR data in a semi-arid tropical region.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0320) [Remote Sens. 7 (6), 8128–8153.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0320)
- [Van Dijk, A., Renzullo, L.J., 2011. Water resource monitoring systems and the role of](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0325) [satellite observations. Hydrol. Earth Syst. Sci. 15 (1), 39–55.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0325)
- Varella, H., Guerif, M., Buis, S., 2010a. Global sensitivity analysis measures the quality of parameter estimation: the case of soil parameters and a crop model. Environ. Modell. Software 25 (3), 310–319. [http://dx.doi.org/10.1016/j.](http://dx.doi.org/10.1016/j.envsoft.2009.09.012) [envsoft.2009.09.012.](http://dx.doi.org/10.1016/j.envsoft.2009.09.012)
- Varella, H., Guerif, M., Buis, S., Beaudoin, N., 2010b. Soil properties estimation by inversion of a crop model and observations on crops improves the prediction of agro-environmental variables. Eur. J. Agron. 33, 139–147. [http://dx.doi.org/](http://dx.doi.org/10.1016/j.eja.2010.04.005) [10.1016/j.eja.2010.04.005.](http://dx.doi.org/10.1016/j.eja.2010.04.005)
- Vaysse, K., Lagacherie, P., 2015. Evaluating Digital Soil Mapping approaches for mapping GlobalSoilMap soil properties from legacy data in Languedoc-Roussillon (France). Geoderma 4, 20–30. [http://dx.doi.org/10.1016/](http://dx.doi.org/10.1016/j.geodrs.2014.11.003) [j.geodrs.2014.11.003](http://dx.doi.org/10.1016/j.geodrs.2014.11.003).
- Vereecken, H., Maes, J., Feyen, J., Darius, P., 1989. Deriving pedotransfer functions of soil hydraulic properties. In: ISSS Symposium, Wageningen, pp. 121–124.
- [Vereecken, H., Maes, J., Feyen, J., 1990. Estimating unsaturated hydraulic](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0350) [conductivity from easily measured soil properties. Soil Sci. 149 (1), 1–12.](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0350)
- Vereecken, H., Huisman, J.A., Bogena, H., Vanderborght, J., Vrugt, J.A., Hopmans, J.W., 2008. On the value of soil moisture measurements in vadose zone hydrology: a review. Water Resour. Res. 44 (4). [http://dx.doi.org/10.1029/2008WR006829.](http://dx.doi.org/10.1029/2008WR006829)
- Violette, A., Godderis, Y., Marechal, J.C., Riotte, J., Oliva, P., Kumar, M.S.M., Sekhar, M., Braun, J.J., 2010. Modelling the chemical weathering fluxes at the watershed scale in the Tropics (Mule Hole, South India): relative contribution of the smectite/kaolinite assemblage versus primary minerals. Chem. Geol. 277 (1–2), 42–60. <http://dx.doi.org/10.1016/j.chemgeo.2010.07.009>.
- [Wagner, W., Lemoine, G., Rott, H., 1999. A method for estimating soil moisture from](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0365) [ERS scatterometer and soil data. Remote Sens. Environ. 70 (2), 191–207](http://refhub.elsevier.com/S0022-1694(16)30846-0/h0365).
- Wohling, T., Vrugt, J.A., 2011. Multiresponse multilayer vadose zone model calibration using markov chain monte carlo simulation and field water retention data. Water Resour. Res. 47 (4). [http://dx.doi.org/10.1029/](http://dx.doi.org/10.1029/2010WR009265) [2010WR009265](http://dx.doi.org/10.1029/2010WR009265).
- Wösten, J.H.M., Pachepsky, Ya.A., Rawls, W.J., 2001. Pedotransfer functions: bridging the gap between available basic soil data and missing hydraulic characteristics. J. Hydrol. 251 (3–4), 123–150. [http://dx.doi.org/10.1016/S0022-1694(01)](http://dx.doi.org/10.1016/S0022-1694(01)00464-4) [00464-4](http://dx.doi.org/10.1016/S0022-1694(01)00464-4).