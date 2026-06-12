Contents lists available at SciVerse [ScienceDirect](http://www.sciencedirect.com/science/journal/03783774)

Agricultural Water Management

![](_page_0_Picture_3.jpeg)

journal h om epage: [www.elsevier.com/locate/agwat](http://www.elsevier.com/locate/agwat)

# Performance evaluation of AquaCrop model for maize crop in a semi-arid environment

# M. Abedinpour a, A. Sarangi b,∗, T.B.S. Rajput b, Man Singhb, H. Pathakc, T. Ahmadd

a Div. of Agricultural Engg, IARI, New Delhi 12, India

b WTC, IARI, New Delhi 12, India

c Div. of Environmental Sciences, IARI, New Delhi 12, India

d IASRI, New Delhi 12, India

#### a r t i c l e i n f o

Article history: Received 3 August 2011 Accepted 1 April 2012 Available online 25 April 2012

- Keywords: AquaCrop model Calibration Validation Maize crop Deficit irrigation Nitrogen
#### a b s t r a c t

Crop growth simulation models of varying complexity have been developed for predicting the effects of soil, water and nutrients on grain and biomass yields and water productivity of different crops. These models are calibrated and validated for a given region using the data generated from field experiments. In this study, a water-driven crop model AquaCrop, developed by FAO was calibrated and validated for maize crop under varying irrigation and nitrogen regimes. The experiment was conducted atthe research farm of the Water Technology Centre, IARI, New Delhi during kharif 2009 and 2010. Calibration was done using the data of 2009 and validation with the data of 2010. Irrigation applications comprised rainfed, i.e. no irrigation (W1) irrigation at 50% of field capacity (FC) (W2) at 75% FC (W3) and full irrigation (W4). Nitrogen application levels were no nitrogen (N1), 75 kg ha−1 (N2) and 150 kg ha−1 (N3). Model efficiency (E), coefficient of determination (R2), Root Mean Square error (RMSE) and Mean Absolute Error (MAE) were used to testthe model performance. The model was calibrated for simulating maize grain and biomass yield for alltreatmentlevels with the prediction error statistics 0.95 < E < 0.99, 0.29 < RMSE < 0.42, 0.9 < R2 < 0.91 and 0.17 < MAE < 0.51 t ha−1. Upon validation, the E was 0.95 and 0.98; MAE was 0.11 and 1.08 and RMSE was 0.1 and 0.75 for grain and biomass yield, respectively. The prediciton error in simulation of grain yield and biomass under all irrigation and nitrogen levels ranged from a minimum of 0.47% to 5.91% and maximum of 4.36% to 11.05%, respectively. The highest and the lowest accuracy to predict yield and biomass was obtained at W4N3 and W1N1 treatments, respectively. The model prediciton error in simulating the water productivity (WP) varied from 2.35% to 27.5% for different irrigation and nitrogen levels. Over all, the FAO AquaCrop model predicted maize yield with acceptable accuracy under variable irrigation and nitrogen levels.

© 2012 Elsevier B.V. All rights reserved.

### **1. Introduction**

Fresh water is an indispensable natural resource, which plays a vital role in the development of any country. Presently, many countries and regions of the world are experiencing scarcity of fresh water. Water demand for drinking and hygiene by the ever growing population, agricultural water demand to feed the population, demand from industry and to sustain ecology, are all competing with one another, aggravating the scarcity situation. As a result, water allocation has become one of the most vexing problems faced by policy makers. Water scarcity originates not only from the physical constraints of fresh water resources, but also due to its inefficient use and poor management. The increasing demand on the one hand and inefficient use on the other are likely to widen the gap between water supply and demand in most parts of the world ([FAO,](#page-11-0) [2008).](#page-11-0)

In many water scarce countries, and even otherwise, irrigation is the dominant user of water. Water withdrawal for agricultural purposes accounts for about 75% of all usages in developing countries and the FAO has predicted a 14% netincrease in use of water to meet the food demands by the year 2030 as compared to year 2000 [(FAO,](#page-11-0) [2008).](#page-11-0) At the same time, irrigation is widely criticized as a wasteful user of water, especially in the water-scarce regions. Under different water availability situations, judicious managementis essential to enhance water productivity. Hence, search for sustainable methods to increase crop water productivity is gaining importance in arid and semiarid regions [(Debaeke](#page-11-0) [and](#page-11-0) [Aboudrare,](#page-11-0) [2004).](#page-11-0) Traditionally, agricultural research has focused on maximizing total production. But, in recent years the focus has shifted to the limiting

![](_page_0_Picture_24.jpeg)

<sup>∗</sup> Corresponding author. Tel.: +91 9811400885.

E-mail addresses: [arjamadutta.sarangi@elf.mcgill.ca,](mailto:arjamadutta.sarangi@elf.mcgill.ca) ads [wtc@rediffmail.com](mailto:ads_wtc@rediffmail.com) (A. Sarangi).

<sup>0378-3774/\$</sup> – see front matter © 2012 Elsevier B.V. All rights reserved. [http://dx.doi.org/10.1016/j.agwat.2012.04.001](dx.doi.org/10.1016/j.agwat.2012.04.001)

factors in production systems, notably the availability of either land or water. Within this context, deficitirrigation (DI) has been widely investigated as a valuable strategy where water is the limiting factor in crop cultivation ([Pereira,](#page-11-0) [2006;](#page-11-0) [Fereres](#page-11-0) [and](#page-11-0) [Soriano,](#page-11-0) [2007).](#page-11-0) Simulation models are designed to imitate the behavior of a system. For time-variant systems, the time step of operating the corresponding simulation model should match the real lifetime intervals during which there is a measurable and meaningful variation in the causative factors that determine the output. Often a 1-day time stem is considered adequate for simulation models because the climatological database comprising rainfall, temperature, wind speed and many others are for a minimum time interval of 1 day. The short simulation time-step demands that a large amount of input data (viz. climate parameters, soil characteristics and crop parameters) be available for the model to run. These models usually offer the possibility of specifying management options and they can be used to investigate a wide range of management strategies at low costs [(Kumar](#page-11-0) [and](#page-11-0) [Ahlawat,](#page-11-0) [2004).](#page-11-0) Crop growth models in general contain a set of equations that estimates the production rate of biomass from the captured resources such as carbon dioxide, solar radiation, and water [(Azam](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [1994).](#page-11-0) Accordingly, three main crop growth modules can be distinguished: (i) carbon-driven, (ii) radiation-driven and (iii) water-driven ([Steduto,](#page-11-0) [2003).](#page-11-0)

The water-driven crop growth models assume a linear relation between biomass growth rate and transpiration through a water productivity (WP) parameter [(Tanner](#page-11-0) [and](#page-11-0) [Sinclair,](#page-11-0) [1983;](#page-11-0) [Steduto](#page-11-0) [and](#page-11-0) [Albrizio,](#page-11-0) [2005)T](#page-11-0)his approach avoids the subdivision into different hierarchical levels, which results in a less complex structure and reduces the number of input parameters ([Steduto](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2009).](#page-11-0) The water driven growth conceptis used in CropSyst and AquaCrop model [(Steduto](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2009;](#page-11-0) [Raes](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2009).](#page-11-0) One of the major advantages of the water-driven module over radiation-driven is the opportunity to normalize the WP parameter for climate (both the evaporative demand and the atmospheric CO2 concentration) in the former which, therefore, has a greater applicability in different locations under varying spatio-temporal settings ([Steduto](#page-11-0) [and](#page-11-0) [Albrizio,](#page-11-0) [2005;](#page-11-0) [Steduto](#page-11-0) et [al.,](#page-11-0) [2007).](#page-11-0)

Crop models viz. CERES-Maize ([Jones](#page-11-0) [andKiniry,](#page-11-0) [1986),](#page-11-0)WOFOST model, CropSyst [(Stockle](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2003),](#page-11-0) and the Hybrid-Maize model [(Yang](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2004)](#page-11-0) have been used for prediction of yield of maize crop. Most of these models, however, are quite sophisticated; require advanced modeling skills for their calibration and subsequent operation, and require large number of model input parameters. Some models are cultivar-specific and are not easily amenable for general use. In this context, the recently developed FAO AquaCrop model [(Raes](#page-11-0) et [al.,](#page-11-0) [2009;](#page-11-0) [Steduto](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2009)](#page-11-0) is a user-friendly and practitioner oriented type of model, because it maintains an optimal balance between accuracy, robustness, and simplicity, and requires a relatively small number of model input parameters.AquaCrop has been parameterized and tested on maize by using experimental data of six cropping seasons in the University of California Davis, USA [(Hsiao](#page-11-0) [et](#page-11-0) [al](#page-11-0)., [2009).](#page-11-0) [Hsiao](#page-11-0) [et](#page-11-0) [al](#page-11-0). [(2009)](#page-11-0) observed that AquaCrop was able to simulate the Canopy cover (CC), biomass development, and grain yield of four maize cultivars over six different cropping seasons that differed in plant density, planting date, and evaporative demands. [Araya](#page-11-0) et [al.](#page-11-0) [(2010)](#page-11-0) evaluated AquaCrop model for simulating biomass and yield of water deficient and irrigated barley in northern Ethiopia. They reported that the AquaCrop model performed well with model efficiency ranging from0.5 to 0.95 for grain yield under various planting dates. [Stricevic](#page-11-0) et [al.](#page-11-0) [(2011)](#page-11-0) evaluated the AquaCrop model under rainfed and supplemental irrigated maize, sugar beet and sunflower in Serbia. They reported that the maximum prediction error for maize was 3.6% and for sugar beat 12.2%. However, they concluded that the AquaCrop model can be used in impartial decision-making and in the selection of crops to be given irrigation priority in areas where water resources are limited. [Evett](#page-11-0) [and](#page-11-0) [Tolk](#page-11-0) [(2009)](#page-11-0) evaluated the performance of different crop models viz. AquaCrop, CERES-Maize, CropSyst, DSSAT 4.0 and WOFOST in simulating water use efficiency (WUE) for cotton, maize, sunflower, soybean, dry bean and peanut, etc. It was revealed that the WUE was primarily governed by the evaporation (E) and transpiration (T) components of crop evapotranspiration. However, non-availability of experimental data segregating the E and T components restricts the investigations to evaluate the model performances on estimation of WUE by using separate E and T values. Therefore, it was suggested that WUE simulation should include E or T measurements so that effects of conservation agriculture technologies that reduce E can be studied. [Todorovic](#page-11-0) et [al.](#page-11-0) [(2009)](#page-11-0) compared the performance of water drivenAquaCrop model with CropSyst and the carbon-driven WOFOST models for Sunflower using deficit irrigation methods in Southern Italy. They suggested that the simpler model AquaCrop using limited input information should be preferred due to its minimal input data requirement and prediction accuracy pertaining to crop yield and WUE. [Teklu](#page-11-0) [and](#page-11-0) [Awulachew](#page-11-0) [(2009)](#page-11-0) simulated the WP of maize under varying soil fertility scenarios (poor, near optimal and non-limiting) under rainfed conditions using theAquaCrop model in Blue Nile Basin, sub-Saharan Africa. The result indicated that grain yield of maize increased from 2500 kg ha−1 under poor to 6400 kg ha−1 and 9200 kg ha−1 with near optimal and non-limiting soil fertility conditions, respectively. It was revealed from the literature that AquaCrop model released during 2009 has not been evaluated for simulating the maize growth and yield in the semi arid region of Northern India. Keeping this in view, the investigation was undertaken to calibrate and validate AquaCrop model for kharif maize grown in experimental farm of Indian Agricultural research Institute (IARI), New Delhi and evaluate its performance under rainfed, deficit and full irrigation conditions.

#### **2. Materials and methods**

#### 2.1. Site description

The experimental fields of one ha block in the research farm of Water Technology Centre, IARI [(Fig.](#page-2-0) 1) was selected for conduction of maize experiment during kharif season of 2009 and 2010. IARI farm is located between 77◦09 36E longitude and 28◦37 55N latitude at an average elevation of 167.17 m above mean sea level. The experimental field has surface irrigation facility with a sump to store pumped up ground water and provides assured irrigation during the crop growth period. Climate data during the experiment period for use in the model was acquired from the observatories located within the IARI farm. Rainfall depth and variations of temperature during the experiment are shown in [Figs.](#page-2-0) 2 and 3 for 2009 and 2010, respectively.

#### 2.2. Field layout, cultural practice and measurements

The experiment was laid in randomized complete block design (RCBD) comprised rainfed, i.e. no irrigation: W1; irrigation at 50% of field capacity (FC): W2; at 75% FC: W3; and full irrigation (W4). The Nitrogen application levels were no Nitrogen: N1; 50% of recommended dose: N2 and 100%of recommended dose of Nitrogen:(N3). There were five furrows in each plot of 3.5 m × 3.75 m size and the replications were separated by 2.5 m to ensure that the treatments in plots were independent to each other. The furrows were 75 cm apart with plant spacing of 20 cm in each furrow. The maize hybrid BIO9681 cultivar was sown at a depth of 3–5 cm with a population density of 66,667 plants per hectare on 22nd and 16th July during 2009 and 2010, respectively. Physical and chemical properties of soil and the experiment details are presented in [Table](#page-3-0) 1.

<span id="page-2-0"></span>![](_page_2_Figure_1.jpeg)

**Fig. 1.** Location of field experiment site at Water Technology Center (WTC), Indian Agricultural Research Institute (IARI), New Delhi, India.

![](_page_2_Figure_3.jpeg)

![](_page_2_Figure_4.jpeg)

![](_page_2_Figure_5.jpeg)

**Fig. 3.** Weather parameters during the crop growth period in 2010.

<span id="page-3-0"></span>**Table 1** Physical and chemical properties of the soil of experimental field.

| Determination         | Soil depth (cm) |            |       |       |           |  |  |
|-----------------------|-----------------|------------|-------|-------|-----------|--|--|
|                       | 0–15            | 15–30      | 30–45 | 45–75 | 75–105    |  |  |
| Sand (%)              | 52.4            | 53.7       | 44    | 39    | 38        |  |  |
| Silt (%)              | 21              | 19         | 23    | 25    | 27        |  |  |
| Clay (%)              | 26.6            | 27.3       | 33    | 36    | 34        |  |  |
| Soil texture          | Sandy loam      | Sandy loam | Loam  | Loam  | Clay loam |  |  |
| FC (w/w)              | 21.3            | 25.6       | 27.9  | 32.8  | 33.0      |  |  |
| PWP (w/w)             | 9.5             | 10.2       | 13.7  | 14.7  | 15.0      |  |  |
| K (cm day−1)          | 27.4            | 26.2       | 18.6  | 19.1  | 19.5      |  |  |
| Bd (g cm−3)           | 1.41            | 1.43       | 1.39  | 1.37  | 1.36      |  |  |
| EC (dS m−1)           | 0.24            | 0.25       | 0.35  | 0.37  | 0.38      |  |  |
| PH                    | 7.7             | 8.1        | 8.01  | 8.05  | 8.50      |  |  |
| Organic matter<br>(%) | 0.56            | 0.50       | 0.42  | 0.39  | 0.40      |  |  |
| N (ppm)               | 171             | 152        | 124   | 118   | 121       |  |  |
| P (ppm)               | 3.2             | 3.5        | 4.1   | 3.9   | 4.2       |  |  |
| K (ppm)               | 165             | 170        | 174.6 | 180   | 183       |  |  |

Bd, bulk density; Ks, saturated hydraulic conductivity; FC, field capacity; PWP, permanent wilting point; EC, electrical conductivity.

Measured quantity of irrigation water based on soil moisture content was directly applied to the furrows using HDPE pipes to eliminate conveyance loss of water. The N fertilizer was applied in three split doses with one-third given as basal, one-third at 21 days after sowing (DAS) and the remaining at 42 DAS. The yield was measured at the physiological maturity stage by selecting three middle rows of each experimental plot representing 7.8 m2 area. After harvesting,the cobs were air-dried and grains were separated from the cobs. Further,the grain weight was measured for each plot and the yield per ha was estimated.

#### 2.3. Scheduling of irrigation in the experiment

Soil moisture content of 15 cm profiles and up to crop root zone were monitored periodically for irrigation scheduling, i.e. deciding the date and quantity of irrigation water during the crop growth period. The date of irrigation was decided when the soil moisture of the root zone reached 50% of the total available water (TAW), i.e. when half the moisture between the field capacity (FC) and permanent wilting point (PWP) gets depleted. The quantity of irrigation water for each treatment was calculated based on the soil moisture content before irrigation and root zone depth of the plant using Eq. (1).

$$\mathbf{SMD} = \{\theta_{\text{Fc}} - \theta_{l}\} \times \mathbf{D} \times \mathbf{Bd} \times f \tag{1}$$

where SMD: soil moisture deficit (mm), -Fc: soil water content at field capacity, i: soil water content before irrigation (weight percent basis), D: depth of root development (mm), Bd: bulk density of the particular soil layer (g cm−3), f: coefficient for each irrigation treatment levels in the experiment. The coefficient of each treatmentf(W1) = 0 (rainfed condition), f(W2) = 0.5 (50% FC), f(W3) = 0.75 (75% FC) and f(W4) = 1 (full irrigation up to FC without any deficit), were used for different treatments to estimate the quantity of irrigation water. In the irrigation treatments (50 and 75% of FC), water was applied on the same day as that of the fully irrigated plot, but the irrigation depths were reduced to 50% and 75% of the full irrigation for W2 and W3 treatments, respectively.

### 2.4. Estimation of crop evapotranspiration

Soil water budget method was used to estimate the actual crop evapotranspiration (ETa). The components of the water balance equation for a control volume of soil profile up to root zone depth were estimated using Eq. (2).

$$\text{ET}_{\mathbb{C}} = P + \text{lR} + \text{Cp} - \text{Dp} - \text{Ro} \pm \Delta \mathcal{W} \tag{2}$$

where IR, P and Dp are total irrigation depth (mm), precipitation (mm) and deep percolationfromthe bottomof root zone (mm),W is the change in soil water content (final-initial) of each soil layer (mm), Ro is the runoff, (mm) and Cp is the capillary contribution from the ground water table to the crop root zone (mm).

The furrows in the experimental plots were closed by bunds and the water table depth was below 8 m from the ground surface. Therefore, the surface runoff and the vertical upward seepage or the capillary flow to the root zone was assumed negligible in the calculation of ETc using Eq. (2). Besides this, the drainage below root zone, after a number of soil–water content measurements, was considered to be negligible. So Eq. (2) was reduced to:

$$\text{INT} = \text{IR} + P \pm \text{DW} \tag{3}$$

The field water budgeting as mentioned above is commonly used to measure total actual water use or crop evapotranspiration (ETc) when lysimeter facilities are not available ([Farahani](#page-11-0) et [al.,](#page-11-0) [2009).](#page-11-0)

### 2.5. Input data requirement of AquaCrop model

Operation of AquaCrop model requires input data consisting of climatic parameters, crop, soil and field and irrigation management data. However, the model contains a complete set of input parameters that can be selected and adjusted for different soil or crop types.

### 2.5.1. Climate data

The weather data required by AquaCrop model are daily values of minimum and maximum air temperature, reference crop evapotranspiration (ETo), rainfall and mean annual carbon dioxide concentration (CO2). ETo was estimated using ETo calculator using the daily maximum and minimum temperature, wind speed at 2 m above ground surface, solar radiation and mean relative humidity (RH). The weather parameters were collected from automatic weather station located at a distance of 150 m from WTC-01 experimental farm. Rainfall depths of 502 mm and 713 mm during the crop growth season were recorded during 2009 and 2010, respectively. The temperature variations, ETo and rainfall depths during the experiment of 2009 and 2010 have been shown in [Figs.](#page-2-0) 2 and 3, respectively.

### 2.5.2. Crop parameters

Canopy development was measured in terms of growth stages, leaf area, root length, and above ground biomass on biweekly basis by removing two plants per plot. Date of emergence, maximum canopy cover (CC), duration of flowering, start of senescence, and maturity were also recorded. In each crop growth stages, green leaves were separated and leaf area of each plant measured by leaf area meter to obtain leaf area index (LAI), which was converted to crop canopy cover (CC). Dry biomass of above ground plant at each crop growth stages was obtained by weighing it after keeping in the oven for 48 h at 65 ◦C. Besides this, the canopy decline coefficient, crop coefficient for transpiration at full canopy cover, soil water depletion thresholds for inhibition of leaf growth and stomatal conductance, acceleration of canopy senescence were used from [Hsiao](#page-11-0) [et](#page-11-0) [al](#page-11-0). [(2009).](#page-11-0) These parameters were presumed to be applicable to a wide range of conditions and not specific for a given crop cultivar [(Heng](#page-11-0) et [al.,](#page-11-0) [2009).](#page-11-0) Relationship between LAI and CC used for maize crop is presented in Eq. [(4)](#page-4-0) [(Hsiao](#page-11-0) et [al.,](#page-11-0) [2009;](#page-11-0) [Heng](#page-11-0)

<span id="page-4-0"></span>

| Input data of crop parameters used in AquaCrop model. |  |  |  |  |  |  |
|-------------------------------------------------------|--|--|--|--|--|--|
|-------------------------------------------------------|--|--|--|--|--|--|

| Description                                       | Value | Unit                                                                    |
|---------------------------------------------------|-------|-------------------------------------------------------------------------|
| Base temperature                                  | 8.0   | ◦C                                                                      |
| Cut-off temperature                               | 30.0  | ◦C                                                                      |
| Canopy growth coefficient<br>(CGC)                | 19.9  | % day−1                                                                 |
| Canopy decline coefficient<br>(CDC) at senescence | 1.06  | % day−1                                                                 |
| Leaf growth threshold (Pupper )                   | 0.14  | % of TAW [fraction of total<br>available water (TAW)],                  |
| Leaf growth threshold (Plower )                   | 0.72  | % of TAW                                                                |
| Leaf growth stress coefficient                    | 2.9   | Unit less (moderately convex                                            |
| curve shape                                       |       | curve)                                                                  |
| Expansion stress coefficient<br>(Pupper )         | 0     | % of TAW                                                                |
| Expansion stress coefficient<br>(PLower )         | 0.3   | % of TAW                                                                |
| Expansion stress coefficient<br>curve shape       | 1.3   | % of TAW                                                                |
| Stomatal conductance<br>threshold (Pupper )       | 0.5   | Unit less                                                               |
| Stomatal stress coefficient<br>curve shape        | 1.8   | Unit less (high convex curve)                                           |
| Senescence stress coefficient<br>curve shape      | 1.3   | Unit less (moderately convex<br>curve)                                  |
| Senescence stress coefficient<br>(Pupper )        | 0.19  | Unit less (Initiation of canopy<br>senescence)                          |
| Coefficient, inhibition of leaf<br>growth on HI   | 7.0   | Unit less (HI increased by<br>inhibition of leaf growth at<br>anthesis) |
| Coefficient, inhabitation of<br>stomata on HI     | 3.0   | Unit less (HI increased by<br>inhibition of stomata at<br>anthesis)     |
| Maximum basal crop<br>coefficient (Kcb)           | 1.15  | Unit less                                                               |
| Time from sowing to<br>emergence                  | 6     | days                                                                    |
| Time from sowing to start<br>flowering            | 52    | days                                                                    |
| Time from sowing to start<br>senescence           | 72    | days                                                                    |
| Time from sowing to maturity                      | 97    | days                                                                    |
| Length of the flowering stage                     | 10    | days                                                                    |
|                                                   |       |                                                                         |

et [al.,](#page-11-0) [2009).](#page-11-0) The crop parameters used as input to AquaCrop are presented in Table 2.

$$\text{CC} = 1.005[1 - \exp(-0.6 \times \text{LAl})]^{1.2} \tag{4}$$

The upper and lower thresholds and the shape of the response curve are the parameters for each type of stress that define the sensitivity and severity of a depleted soil profile. The upper threshold determines when the stress begins, while the lower threshold is the point at which the physiological process completely ceases. The shape factor used in AquaCrop model describes the amplitude of the stresses which affect the crop yield. A shape factor of zero indicated highest sensitivity of crop to water stress and more than zero is an indicative of less sensitiveness to water stress. The water stress is divided to expansion stress, stomatal closure stress and senescence stress coefficients. These coefficients were calibrated using the experimental data to obtain a better match between the AquaCrop simulated and observed data.

### 2.5.3. Soil parameters

Data pertaining to the soil of experiment site required as input parameters for AquaCrop are viz. number of soil horizons, soil texture, field capacity (-FC), permanent wilting point (-PWP), saturated hydraulic conductivity (Ksat) and volumetric water content at saturation (sat). The experiment site did not contain any impervious or restrictive soil layer to obstruct the expansion of root growth. The curve number (CN) of the site was used to estimate surface runoff from rainfall that occurred during the experiment.

### 2.5.4. Irrigation and field management parameters

Irrigation and field management during the experiment are two important components considered in the AquaCrop model. Irrigation management comprised data pertaining to both the situations of rainfed (no irrigation), and irrigation. In full irrigation treatment (i.e. 100%), water was applied up to field capacity level when soil moisture in the root zone approached 50% of total available water (TAW). In the deficit irrigation treatments (i.e. 50 and 75% of full irrigation), water was applied on the same day as the fully irrigated plot, but the irrigation depths were reduced to 50 and 75% of the full irrigation. There was no irrigation in the rainfed plots of the experiment. The field management components were the fertility levels, mulching to reduce evaporation from soil and furrow end bunds to eliminate surface runoff. In this study theAquaCrop model was evaluated through calibration and validation to estimate yield, biomass and canopy cover (CC) under different water and nitrogen levels.

### 2.6. Calibration of AquaCrop model

Calibration or fine tuning of the AquaCrop model was accomplished by using the observed values from the field experiment during 2009 as model input and then simulating the model to predict the output viz. the yield, biomass and canopy cover (CC). Subsequently, the predicted output values were compared with the observed yield and biomass of the experimental plot. The difference between the model predicted and experimental data was minimized by using trial and error approach in which one specific input variable was chosen as the reference variable at a time and adjusting only those parameters that were known to influence the reference variable the most. The procedure is repeated to arrive at the closest match between the model simulated and observed value of the experiment for each treatment combination.

### 2.6.1. Calibration of crop parameters

The crop file in AquaCrop contained crop-specific parameters pertaining to 13 phenological crop growth stages with canopy and root development, evapotranspiration, water,fertility, and temperature stress parameters ([Steduto](#page-11-0) et [al.,](#page-11-0) [2009).](#page-11-0) The canopy cover (CC) is an important componentin calculating crop transpiration, which is directly related to leaf area index (LAI) and estimated by using Eq.(4). There are six parameters that determine the development of canopy cover viz. canopy growth coefficient (CGC), canopy decline coefficient(CDC), maximum canopy cover, days to emergence, days to senescence, and days to full maturity. The CGC controls the rate at which the canopy expands and the CDC controls how fast the canopy dies off at the end of the growing season. These parameter values were iteratively determined using trial and error approach by fitting the canopy cover to the measured LAI and CO2 concentration. During the calibration process, the simulated canopy cover was compared with the observed canopy cover at different DAS of the crop. Next the biomass and yield was compared with the measured data using the water productivity and the transpiration crop coefficient.Atthe same time the simulated water use efficiency was compared with the observed data in the field experiment during 2009. Finally, the harvest index was adjusted to match with measured yields. This process was repeated several times to list out a set of parameters that produced results in line with the measured data.

The calibrated values of CGC and CDC for the experiment were 19.9% day−1 and 14.5% day−1, respectively. The calibrated maximum canopy cover was 95% for full irrigation and recommended nitrogen (W4N3) treatment. The days to emergence, max canopy, senescence and maturity were 5, 45, 78 and 97 days, respectively.

The reproductive growth period consists of flowering, yield formation, and harvest index (HI) development stages. These are controlled by days to flowering (52 DAS), flowering period (10 days), and days for initiation of harvesting. The flowering stage was triggered to start as the crop attains full canopy cover. The maximum CC is reached by the middle ofthe flowering stage after which further canopy expansion ceases. The effective rooting depth was iteratively set at 1.2 m with maximum root depth achieved during the flowering period. The maximum transpiration crop coefficient (Kcbx) was calibrated to standardize ETo during the growing-season where the CC was equal to the maximum canopy cover (CCx). The (Kcbx) value thus obtained was 1.15 under full irrigation and no fertilizer stress conditions (i.e. W4N3 treatment). This value of Kcbx for the maize crop was in line with the crop coefficients for the midseason as per FAO-56 ([Allen](#page-11-0) et [al.,](#page-11-0) [1998).](#page-11-0)

The calibrated value of WP was obtained as 34 g m−2, which was in the range suggested for the AquaCrop for C4 crops (i.e. crops that produces the 4-carbon compound oxalocethanoic (oxaloacetic) acid as the first stage of photosynthesis). The maize being the C4 crop, the calibrated water productivity matched with the experimental data. The harvestable yield produced by the crop was the product of the biomass and the harvest index (HI). The harvest index was obtained as 34% on a dry biomass basis and 39% on wet basis with grain moisture content of 15.5% at harvest. Subsequently, under the crop water stress category, factors pertaining to expansion stress were calibrated to have the upper threshold, lower threshold, and shape factor to be 0.0, 0.3, and 1.3, respectively. Also, the stomatal closure stress, the upper threshold and shape factor were 0.5 and 1.8, respectively, while the lower threshold was set at the permanent wilting point (PWP).

Moreover, for the early senescence stress, the upper threshold and shape factor were 0.19 and 1.3, respectively, while the lower threshold was set at the permanent wilting point (PWP). All these eight calibrated coefficients were related to the crop water stress function in the AquaCrop model, which was used to simulate the yield from different experimental plots.

#### 2.6.2. Calibration of irrigation management

AquaCrop model contains several user-specific options for simulating irrigation, such as determining net irrigation requirement, generation of an irrigation schedule based upon irrigated and rainfed management strategies. The irrigation scheduling option also provides alternatives for different application methods [viz. sprinkler irrigation, surface irrigation (i.e. basin, furrow, and border) and drip irrigation]. The major difference between the application methods is the portion of the surface that is wetted during irrigation. In the present study, the experiment was conducted with furrow irrigation and 80% wetted area option was selected. However, the provision for inputting the irrigation water application efficiency or uniformity is not available in AquaCrop model. But, the application efficiency can be estimated outside the model to determine gross irrigation application for taking up the experiment based on the field layout and the source of irrigation. AquaCrop can be used to develop an irrigation schedule based upon either management allowed depletion (MAD) or a fixed time interval based scheduling. The MAD of 50% was considered as initial condition in the model. The depletion level and depth of irrigation can be designated at differenttimes throughoutthe simulated period to achieve management goals. An irrigation schedule was directly inputted into the model by specifying the date and depth of the irrigation.

### 2.6.3. Calibration of field management

The field management file ofAquaCrop contained the data of soil fertility, crop residue, and surface practices. For each treatment of nitrogen levels, soil fertility was considered and inputted as per different levels of treatments. Runoff from the surface of the field was considered in the model with a curve number of 72 pertaining to the experimental site ([Rajput](#page-11-0) et [al.,](#page-11-0) [2009).](#page-11-0) But, no storage of water on top of the field was considered, which corroborated the real field situation observed during the experimental years. Also, the mulching practice during non-growing season was not considered as there were no crop residues or mulches in the experimental field.

### 2.7. Validation of AquaCrop model

AquaCrop model was validated using data of 2010 to predict grain yield and biomass under different water and N-fertilizer application levels in the experiment. Calibrated AquaCrop model was simulated with the input data of the experiment during the year 2010 to predict the grain yield, biomass and water productivity. Further, these predicted values were compared with the observed values of the experiment and the model validation performance statistics were analysed.

### 2.8. Model evaluation criterion

AquaCrop model simulation results of maize yield, biomass and WP were compared with the observed values form the experiment during both calibration and validation processes. The goodness of fit between the simulated and observed values was corroborated by using the prediction error statistics. The prediction error (Pe), coefficient of determination (R2), mean absolute error (MAE) and root mean square error (RMSE) and model efficiency (E) were used as the error statistics to evaluate both the calibration and validation results ofthe model. The R2 and E were used to access the predictive power ofthe model while the Pe, MAE and RMSE indicated the error in model prediction.

In this study, the model output in terms of prediction for canopy cover, grain yield and above ground biomass during harvest was considered for evaluation of the model. The following statistical indicators were used to compare the measured and simulated values. Model performance was evaluated using the following statistical parameters such as prediction error (Pe) model efficiency (E) ([Nash](#page-11-0) [and](#page-11-0) [Sutcliffe,](#page-11-0) [1970),](#page-11-0) given by:

$$P_{\text{\textquotedblleft}} = \frac{(\text{S}_{\text{l}} - \text{O}_{\text{l}})}{\text{O}_{\text{l}}} \times 100\tag{5}$$

$$E = 1 - \frac{\sum_{i=1}^{N} \left(\mathbf{O}_{i} - \mathbf{S}_{i}\right)^{2}}{\sum_{i=1}^{N} \left(\mathbf{O}_{i} - \mathbf{\bar{O}}_{i}\right)^{2}}\tag{6}$$

where Si and Oi are predicted and actual(observed) data, O¯ i is mean value of Oi and N is the number of observations.

$$\text{RMSE} = \sqrt{\frac{1}{\text{(N)} \sum_{i=1}^{N} \text{(O}_{i} - \text{S}_{i}\text{)}^{2}}} \tag{7}$$

$$\text{MAE} = \sqrt{\sum_{i=1}^{n} \frac{(\mathbb{S}_{i} - \mathcal{O}_{i})}{n}} \tag{8}$$

Model efficiency (E) and R2 approaching one and Pe, MAE and RMSE close to zero were indicators for better model performance.

### **3. Results and discussion**

Crop water use, irrigation water depth, grainyield, above ground biomass, water productivity (WP), irrigation water use efficiency (IWUE) and harvest index (HI) under non limiting fertilized (N3), moderate fertilized (N2) and poor fertilized (N1) conditions for 2009 and 2010 experiments are shown in [Table](#page-6-0) 3. It was observed from [Table](#page-6-0) 3 that during 2 years of experiment, the lowest grain yields and biomass was observed to be 1430 and 6430 kg ha−1 in

<span id="page-6-0"></span>Crop water use, irrigation water depths, grain yield, above ground biomass, water productivity (WP), irrigation water use efficiency (IWUE)and harvest index (HI) under varying N-fertilizer levels during 2009 and 2010.

| Year | Treatment                               | Irrigation water<br>applied (mm) | Crop water<br>use (mm) | Grain yield<br>(kg ha−1) | WP<br>(kg ha−1 mm−1) | IWUE<br>(kg ha−1 mm−1) | Biomass<br>(kg ha−1) | HI (%) |
|------|-----------------------------------------|----------------------------------|------------------------|--------------------------|----------------------|------------------------|----------------------|--------|
|      | Non-limiting fertilizer level (N3)      |                                  |                        |                          |                      |                        |                      |        |
|      | W1                                      | 0                                | 250                    | 2360                     | 9.4                  | NA                     | 10,240               | 23.0   |
|      | W2                                      | 105                              | 355                    | 3625                     | 10.2                 | 12.56                  | 14,010               | 25.9   |
| 2009 | W3                                      | 158                              | 408                    | 4250                     | 10.4                 | 10.25                  | 14,670               | 29.0   |
|      | W4                                      | 210                              | 460                    | 5930                     | 12.9                 | 15.7                   | 18,140               | 32.7   |
|      | W1                                      | 0                                | 423.4                  | 5250                     | 12.4                 | NA                     | 16,430               | 31.9   |
|      | W2                                      | 24                               | 447.4                  | 5422                     | 12.1                 | 7.16                   | 16,370               | 34.3   |
| 2010 | W3                                      | 39                               | 462.1                  | 5525                     | 11.9                 | 7.05                   | 17,370               | 31.8   |
|      | W4                                      | 58                               | 481.4                  | 5775                     | 12.0                 | 9.05                   | 17,600               | 32.8   |
|      | Moderate-limiting fertilizer level (N2) |                                  |                        |                          |                      |                        |                      |        |
|      | W1                                      | 0                                | 250                    | 1950                     | 7.8                  | NA                     | 7950                 | 24.5   |
|      | W2                                      | 105                              | 355                    | 3190                     | 9.0                  | 11.81                  | 10,540               | 30.3   |
| 2009 | W3                                      | 158                              | 408                    | 4450                     | 10.2                 | 13.92                  | 12,390               | 33.5   |
|      | W4                                      | 210                              | 460                    | 5120                     | 11.1                 | 15.1                   | 14,900               | 34.4   |
|      | W1                                      | 0                                | 423.4                  | 4535                     | 10.7                 | NA                     | 14,100               | 32.2   |
|      | W2                                      | 24                               | 447.4                  | 4685                     | 10.5                 | 6.25                   | 14,230               | 32.9   |
| 2010 | W3                                      | 39                               | 462.1                  | 4815                     | 10.4                 | 7.17                   | 14,620               | 32.9   |
|      | W4                                      | 58                               | 481.4                  | 4785                     | 9.9                  | 4.31                   | 14,650               | 32.7   |
|      | Poor fertilizer level (N1)              |                                  |                        |                          |                      |                        |                      |        |
|      | W1                                      | 0                                | 250                    | 1430                     | 5.7                  | NA                     | 6400                 | 22.3   |
|      | W2                                      | 105                              | 355                    | 2535                     | 7.1                  | 10.52                  | 8950                 | 28.3   |
| 2009 | W3                                      | 158                              | 408                    | 3015                     | 7.39                 | 10.03                  | 9360                 | 32.2   |
|      | W4                                      | 210                              | 460                    | 3395                     | 7.38                 | 9.35                   | 10,420               | 32.6   |
|      | W1                                      | 0                                | 423.4                  | 3160                     | 7.5                  | NA                     | 10,170               | 31.1   |
|      | W2                                      | 24                               | 447.4                  | 3245                     | 7.3                  | 3.54                   | 10,100               | 32.1   |
| 2010 | W3                                      | 39                               | 462.1                  | 3180                     | 6.9                  | 5.1                    | 10,200               | 31.2   |
|      | W4                                      | 58                               | 481.4                  | 3315                     | 6.9                  | 2.67                   | 10,390               | 31.9   |

rainfed (W1) and non-fertilized (N1) treatment and the highest was 5930 and 18,150 kg ha−1under full irrigation (W4) and recommended dose of nitrogen (N3), respectively. Water productivity (WP) ranged from a minimum of 5.7 kg ha−1 mm−1 to a maximum of 12.9 kg ha−1 mm−1 in 2009. Water productivity for full irrigation (W4) under N3 treatment was the highest, where as that for rainfed (W1) treatment under non fertilized (N1) was the lowest. Moreover, during 2010, the highest, i.e. 12.4 kg ha−1 mm−1 and lowest 6.9 kg ha−1 mm−1 water productivity (WP) were obtained for W1N3 and both W4N1 and W3N1 treatment combinations, respectively. The highest WP for rainfed condition W1N3 may be attributed to high rainfall received during the growing period of 2010. The irrigation water use efficiency (IWUE) ranged fromaminimum of 8.8 kg ha−1 mm−1 to a maximum of 15.7 kg ha−1 mm−1 in 2009. Irrigation water use efficiency for full irrigation W4N3 treatment was observed to be the highest and the lowest IWUE was for 25% deficit irrigation (W3) with N2 level. Moreover, during 2010, the highest IWUE amounting 9.05 kg ha−1 mm−1 and lowest 2.67 kg ha−1 mm−1 were obtained for W4N3 and W4N1 treatment combinations, respectively. These results were the average of three replications pertaining to the experiments conducted during 2009 and 2010.

#### 3.1. AquaCrop model calibration results

AquaCrop model was calibrated using experiment data of 2009 to predict canopy cover (CC), grain yield and biomass under different water and fertilizer application levels in the experiment. The calibrated CC under different irrigation and nitrogen levels is shown in [Figs.](#page-7-0) 4–6. It was observed from [Fig.](#page-7-0) 4 that under nonlimiting fertilizer condition, the calibration results for different irrigation levels were better (0.89 < E < 0.91) than the rainfed condition (E = 0.81). Moreover, for the poor fertilized (N1) condition, the model agreed well for the rainfed condition besides the deficit and full irrigation condition. Therefore it was observed that the AquaCrop model calibration results for the canopy cover under poor and moderate fertilized scenario for the rainfed situation was better than the non-limiting fertilized condition. Model simulated and measured above ground biomass under non limiting and poor fertilized conditions are shown in [Figs.](#page-8-0) 7 and 8.It was observed from these figures that the model predictions for above ground biomass were very close to the observed values under non-limiting fertilizer level for rainfed and all irrigation treatments. However, under poor fertilized condition, the model performance indicators for rainfed condition (i.e. R2 = 0.86 and E = 0.81) was less as compared to all irrigation levels ([Fig.](#page-9-0) 8). This may be attributed to the rainfed condition using only 250 mm of effective rainfall during the crop growth period (Table 3). Subsequently, calibrated and observed data of biomass for all treatment combinations were plotted in [Fig.](#page-9-0) 9. The model was calibrated with model efficiency E of 0.95 ([Fig.](#page-9-0) 9).

The results of model performance pertaining to grain yield is shown in [Fig.](#page-9-0) 10. The model was callibrated for grain yiled with E and R2 of 0.99 and 0.9, respectively. It was observed that, the maximum and minimum error in grain yield prediction was in W2N2 and W4N3 treatments amounting to 16% and 0.84%, respectively [(Table](#page-9-0) 4). The prediction error in biomass for W1N1 and W4N3 treatments were 30.6% and 1.82%, respectively ([Table](#page-9-0) 4). The best calibrated AquaCrop model was obtained with prediction error ranging from a minimum of 0.07% for the full irrigation treatment (W4) to the maximum of 4.1% in W2 (50% FC) for all nitrogen levels. Similarly, the highest (13.4%) and the lowest prediction error (2.5%) for biomass were in rainfed and in (W3) treatment (i.e.75% FC or 25% DI), respectively at all nitrogen levels. The best calibrated AquaCrop model for water productivity was obtained with prediction error ranging from the maximum of 27.5% in W1N3 treatment to the minimum of 2.35% in W4N3 treatment, respectively [(Table](#page-9-0) 4). The prediction error statistics of the calibrated model is presented in [Table](#page-10-0) 5. It was observed from [Table](#page-10-0) 5 that the model was calibrated for simulation of yield and biomass for all treatment levels with the prediction error statistics 0.95 < E < 0.99, 0.29 < RMSE < 0.42 and 0.17 < MAE < 0.51 t ha−1. AquaCrop model predictions for grain yield and biomass were in line with the observed data corroborated with E and R2 values approaching one. However, the water

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

**Fig. 4.** Simulated and measured canopy cover (CC) for maize crop under non-limiting fertilized (N3) for the callibrated model.

![](_page_7_Figure_3.jpeg)

**Fig. 5.** Simulated and measured canopy cover (CC) for maize crop under moderate-limiting fertilized (N2) for the calibrated model.

<span id="page-8-0"></span>![](_page_8_Figure_1.jpeg)

**Fig. 6.** Simulated and measured canopy cover (CC) for maize crop under poor fertilized (N1) for the calibrated model.

productivity during calibration was with E of 0.66 and R2 of 0.8 [(Table](#page-10-0) 5). The graphical plot of the model calibrated and observed values for all treatment combinations pertaining to grain yield and water productivity are presented in [Figs.](#page-9-0) 10 and 11, respectively.

### 3.2. AquaCrop model validation results

It was observed that the maximum and minimum error of grain yield prediction during model validation with the data of 2010 was for W1N1 and W4N3 treatments amounting to 9.9% and 1.35%,

![](_page_8_Figure_6.jpeg)

**Fig. 7.** Simulated and measured above ground biomass of maize with non-limiting fertilizer doses under different irrigation regimes of calibrated model.

<span id="page-9-0"></span>![](_page_9_Figure_1.jpeg)

**Fig. 8.** Simulated and measured above ground biomass of maize under poor fertilizer doses under different irrigation regimes of calibrated model.

Calibration results of biomass, grain yield of maize under different irrigation water and fertilizer regimes Non-limiting fertilized dose (N3).

| Treatments                              | Yield (t ha−1) |      | Pe    | Biomass (t ha−1) |       | Pe    | WP (kg mm −1 ha−1) |      | Pe   |
|-----------------------------------------|----------------|------|-------|------------------|-------|-------|--------------------|------|------|
|                                         | Obs.           | Sim. | (±%)  | Obs.             | Sim.  | (±%)  | Obs.               | Sim. | (±%) |
| Rainfed                                 | 2.36           | 2.22 | 5.93  | 10.24            | 10.82 | 5.66  | 10.5               | 7.8  | 25.7 |
| W2 (50% FC)                             | 3.62           | 3.96 | 9.39  | 14.01            | 13.45 | 3.99  | 10.2               | 11.4 | 11.8 |
| W3 (75% FC)                             | 4.25           | 4.6  | 8.23  | 14.67            | 14.36 | 2.1   | 10.4               | 12.1 | 16.3 |
| W4 (100% FC)                            | 5.93           | 5.88 | 0.84  | 18.14            | 17.81 | 1.82  | 12.9               | 13.2 | 2.35 |
| Moderate-limiting fertilizer level (N2) |                |      |       |                  |       |       |                    |      |      |
| Rainfed                                 | 1.95           | 2.19 | 12.31 | 7.95             | 10.6  | 25.28 | 7.8                | 8.2  | 5.1  |
| W2 (50% FC)                             | 3.19           | 3.70 | 16.0  | 10.54            | 12.48 | 18.41 | 9.0                | 10.1 | 12.2 |
| W3 (75% FC)                             | 4.15           | 4.27 | 2.9   | 12.39            | 13.23 | 6.78  | 10.2               | 11.1 | 8.8  |
| W4 (100% FC)                            | 5.12           | 4.92 | 3.9   | 14.9             | 13.84 | 7.11  | 11.0               | 12.1 | 10.0 |
| Poor fertilizer level (N1)              |                |      |       |                  |       |       |                    |      |      |
| Rainfed                                 | 1.43           | 1.57 | 9.79  | 6.4              | 8.36  | 30.6  | 5.7                | 6.0  | 7.1  |
| W2 (50% FC)                             | 2.54           | 2.78 | 9.45  | 8.95             | 9.63  | 7.6   | 7.1                | 8.1  | 14.1 |
| W3 (75% FC)                             | 3.01           | 2.82 | 6.31  | 9.36             | 9.63  | 2.88  | 7.4                | 8.6  | 16.2 |
| W4 (100% FC)                            | 3.39           | 3.51 | 3.54  | 10.42            | 9.87  | 5.28  | 7.4                | 8.9  | 20.3 |

Obs., observed; Sim., simulated; Pe, prediction error.

![](_page_9_Figure_7.jpeg)

![](_page_9_Figure_8.jpeg)

![](_page_9_Figure_9.jpeg)

**Fig. 10.** Model calibration results for grain yield under all irrigation and nitrogen levels.

respectively ([Table](#page-10-0) 6). Morever, the maximum and minimum error for biomass was obserevd to be in W1N1 and W4N2 treatments with 17.5% and 0.48%, respectively [(Table](#page-10-0) 6). AquaCrop model was validated with prediction error ranging from a minimum of 0.47%

<span id="page-10-0"></span>Prediction error statistics of the calibrated AquaCrop model.

![](_page_10_Figure_3.jpeg)

**Fig. 11.** Model callibration results of water productivity under all irrigation and nitrogen levels.

for the full irrigation treatment (W4) to the maximum of 5.91% in rainfed (W1) under all nitrogen levels. Similarly, the highest (11.06%) and the lowest prediction error (4.36%) for biomass were observed for rainfed condition and in (W4) treatment (i.e.100% FC), respectively (Table 6). The prediction error statistics of model validation is shown in Table 7. It was observed from Table 7 that the model was validated for yield and biomass with all treatment combinations with prediction error statistics values 0.95 < E < 0.98, 0.1 < RMSE < 0.75, 0.9 < R2 < 0.96and 0.11 < MAE < 1.08 t ha−1. Moreover,the model was validated for simulating the water productivity for all irrigation levels with the prediction error statistics E and R2 value of 0.74 and 0.77, respectively. Moreover, the model validation results and the observed values of grain yield, biomass and water productivity for all treatment combinations were plotted in Figs. 12–14, respectively. It was observed from the E and R2 values that the grain yield and biomass prediction by AquaCrop model under different irrigation water and nitrogen regimes were in line with the observed values. Moreover, the water productivity

![](_page_10_Figure_6.jpeg)

**Fig. 12.** Model validation results in simulating grain yield of maize.

![](_page_10_Figure_8.jpeg)

**Fig. 13.** Model validation results in simulating biomass yield of maize.

## **Table 7**

| Prediction error statistics of the validated AquaCrop model. |  |  |  |  |
|--------------------------------------------------------------|--|--|--|--|
|--------------------------------------------------------------|--|--|--|--|

| Model output<br>parameters               | Mean          | RMSE           | E            | MAE          | R2           |              |
|------------------------------------------|---------------|----------------|--------------|--------------|--------------|--------------|
|                                          | Measured      | Simulated      |              |              |              |              |
| Grain yield (t<br>ha−1)                  | 4.51          | 4.63           | 0.1          | 0.98         | 0.11         | 0.96         |
| ha−1)<br>Biomass (t<br>WP (kg ha−1 mm−1) | 13.85<br>9.87 | 14.92<br>11.22 | 0.75<br>1.20 | 0.95<br>0.74 | 1.08<br>0.71 | 0.90<br>0.77 |

predictions by AquaCrop for all treatments were with E and R2 of 0.68 and 0.77, respectively Fig. 13. Overall, the simulation results of AquaCrop model for canopy cover (CC), biomass and grain yield of kharif Maize BIO9681 showed a close match with the observed values under varying irrigation and nirogen regimes.

**Table 6**

| Validation results of biomass and grain yield of maize under different irrigation water and nitrogen regimes non-limiting fertilized dose (N3). |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|-------------------------------------------------------------------------------------------------------------------------------------------------|--|--|

| Yield (t ha−1)<br>Treatments |                                    | Pe                                              | Biomass (t ha−1) |       | Pe    | WP (kg mm−1 ha−1) |      | Pe    |
|------------------------------|------------------------------------|-------------------------------------------------|------------------|-------|-------|-------------------|------|-------|
| Obs.                         | Sim.                               | (±%)                                            | Obs.             | Sim.  | (±%)  | Obs.              | Sim. | (±%)  |
| 5.52                         | 5.92                               | 7.30                                            | 16.43            | 18.19 | 10.7  | 12.4              | 11.3 | 8.6   |
| 5.62                         | 5.89                               | 4.94                                            | 16.37            | 18.09 | 10.5  | 12.6              | 11.6 | 7.4   |
|                              |                                    |                                                 |                  |       |       |                   |      | 9.2   |
| 5.77                         | 5.85                               | 1.35                                            | 17.60            | 17.97 | 2.1   | 12.0              | 11.2 | 6.7   |
|                              |                                    |                                                 |                  |       |       |                   |      |       |
| 4.53                         | 4.59                               | 1.43                                            | 14.1             | 14.05 | 6.74  | 10.70             | 12.2 | 14.01 |
| 4.68                         | 4.55                               | 2.82                                            | 14.23            | 14.87 | 4.3   | 10.50             | 11.8 | 12.45 |
| 4.80                         | 4.52                               | 5.83                                            | 14.62            | 14.80 | 1.67  | 10.40             | 11.6 | 11.54 |
| 4.78                         | 4.51                               | 5.65                                            | 14.63            | 14.72 | 0.84  | 9.90              | 10.7 | 8.08  |
|                              |                                    |                                                 |                  |       |       |                   |      |       |
| 3.16                         | 3.47                               | 9.9                                             | 10.17            | 11.95 | 17.5  | 7.50              | 9.1  | 21.3  |
| 3.24                         | 3.45                               | 6.35                                            | 10.10            | 11.84 | 17.2  | 7.30              | 8.8  | 20.5  |
| 3.18                         | 3.44                               | 8.7                                             | 10.20            | 11.84 | 16.0  | 6.90              | 8.2  | 18.8  |
| 3.31                         | 3.43                               | 3.6                                             | 10.39            | 11.78 | 13.3  | 6.90              | 7.8  | 13.04 |
|                              | 5.52<br>Poor fertilizer level (N3) | 5.86<br>Moderate-limiting fertilizer level (N2) | 6.11             | 17.37 | 18.01 | 3.7               | 11.9 | 10.8  |

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

**Fig. 14.** Model validation results in simulating water productivity of maize.

#### **4. Conclusion**

AquaCrop model calibrated for grain yield under full irrigation and all nitrogen levels resulted in prediction error ranging from 0.67% to 4.1%. Simulated biomass under 75% FC (W3) had the lowest prediciton error of 2.5%, whereas rainfed conditions exhibited highest prediction error of 13.4%. It was observed that, the AquaCrop model calibrated the grain yield and biomass with the prediction error statistics of 0.99 < E < 0.95, 0.29 < RMSE < 0.42 and 0.17 < MAE < 0.51 t ha−1 for irrigation and nitrogen treatment levels. Subsequently, the model was validated and the performance was in line (i.e. 0.95 < E < 0.98, 0.11 < MAE < 1.08 and 0.1 <RMSE < 0.75) with the observed data of yield and biomass for all irrigation and nitrogen levels during the year 2010.Also,the simulations results for canopy cover (CC) and biomass showed a close match with the observed values for all irrigation treatments. It was obserevd thatthe Aquacrop model was more accurate in predicitng the maize yield under full and 75% FC as compared to the rainfed and 50% FC. AquaCrop model required lesser number of inputs data in simulating the maize growth and yield under different water and fertilizer availability scenarios, as compared to other crop models. Nonetheless, from the results of field experiment and modeling, it can be concluded that the water driven FAO AquaCrop model could be used to predict the maize yield with acceptable accuracy under variable irrigation and field management situations in the semi arid regions of northern India.

#### **Acknowledgments**

The authors wish to acknowledge the National Agricultural Innovation Project (NAIP) funding agency of Indian Council of Agricultural Research (ICAR) for providing the financial assistance for undertaking the experiment atWater Technology Centre, IARI, New Delhi, India.

### **References**

- Allen, R.G., Pereira, L.S., Raes, D., Smith, M., 1998. Crop Evapotranspiration—Guidelines for Computing Crop Water Requirements, No. 56. FAO, Rome, FAO Irrigation and Drainage Paper.
- Araya, A., Habtu, S., Hadgu, K.M., Kebede, A., Dejene, T., 2010. Test of AquaCrop model in simulating biomass and yield of water deficit and irrigated barley.Agricultural Water Management 97, 1838–1846.
- Azam, A., Crout, S.N., Bradley, R.G., 1994. Perspectives in modeling resource capture by crops.In:Monteith,J.L., Unsworth,M.H., Scott,R.K.(Eds.),ResourceCapture by Crops, Proceedings ofthe 52nd Univ. of Nottingham Eastern School. Nottingham University Press, p. 125-14.
- Debaeke, P., Aboudrare, A., 2004. Adaptation of crop management to water-limited environments. European Journal of Agronomy 21, 433–446.
- Evett, S.R., Tolk, J.A., 2009. Introduction: can water use efficiency be modeled well enough to impact crop management? Agronomy Journal 101 (3), 423–425.
- FAO, 2008. Hot Issues: Water Scarcity, FAO web link: <http://www.fao.org/nr/water/issues/scarcity.html> (last accessed 24.07.11).
- Farahani, H.J., Izzi, G., Oweis, T.Y., 2009. Parameterization and evaluation of the AquaCrop model for full and deficit irrigated cotton. Agronomy Journal 101, 469–476.
- Fereres, E.M., Soriano, A., 2007. Deficit irrigation for reducing agricultural water use: integrated approaches to sustain and improve plant production under drought stress special issue. Journal of Botany 58, 147–159.
- Heng, L.K., Hsiao, T.C., Evett, S., Howell, T., Steduto, P., 2009. Validating the FAO AquaCrop model for irrigated and water deficient field maize. Agronomy Journal 101, 488–498.
- Hsiao, T.C., Heng, L.K., Steduto, P., Rojas-Lara, B., Raes, D., Fereres, E., 2009. AquaCrop—the FAO crop model to simulate yield response to water III. Parameterization and testing for maize. Agronomy Journal 101, 448–459.
- Jones, C.A., Kiniry, J.R., 1986. Ceres-N Maize: a simulation model of maize growth and development. Texas A&M University Press, College Station, Temple, TX, pp. 49–111.
- Kumar, V., Ahlawat, I.P.S., 2004. Carry-over of biofertilizers and nitrogen applied to wheat (Triticum aestivum L.) and direct applied N in maize (Zea mays L.) in wheat-maize cropping system. Indian Journal of Agronomy 49 (4), 233–236.
- Nash, J.E., Sutcliffe, J.V., 1970. River flow forecasting through conceptual models. I. A discussion of principles. Journal of Hydrology 10, 282–290.
- Pereira, L.S., 2006. Irrigated agriculture: facing environmental and water scarcity challenges. In: International Symposium on Water and land management for Sustainable Irrigated Agriculture, Cukurova University, April 4–8, Turkey.
- Raes, D., Steduto, P., Hsiao, T.C., Fereres, E., 2009. AquaCrop—the FAO crop model to simulate yield response to water II. Main algorithms and soft ware description. Agronomy Journal 101, 438–447.
- Rajput, T.B.S., Yadav, B.R., Babu, R., Singh, M., Khanna, M., Singh, D.K., Mishra, A.K., Sarangi, A., Patel, N., 2009. Report on Water Resources of IARI Campus and its Augmentation Plan—A Technical Bulletin. Water Technology Centre, Indian Agricultural Research Institute, New Delhi, pp. 38.
- Steduto, P., Albrizio, R., 2005. Resource-use efficiency of field-grown sunflower, sorghum, wheat and chickpea. II. Water use efficiency and comparison with radiation use efficiency. Agricultural Meteorology 130, 269–281.
- Steduto, P., Hsiao, T.C., Fereres, E., 2007. On the conservative behavior of biomass water productivity. Irrigation Science 25, 189–207, [http://dx.doi.org/10.1007/s00271-007-0064-1.](dx.doi.org/10.1007/s00271-007-0064-1)
- Steduto, P., 2003. Biomass water-productivity. Comparing the growth-engines of cropmodels.In: FAO ExpertMeeting onCropWater Productivity Under Deficient Water Supply, Rome, February 26–28.
- Steduto, P., Hsiao, T.C., Raes, D., Fereres, E., 2009. AquaCrop—the FAO Crop Model to Simulate Yield Response to Water I. Concepts and Underlying Principles. Agronomy Journal 101, 426–437.
- Stockle, C.O., Donatelli, M., Nelson, R., 2003. CropSyst a cropping systems simulation model. European Journal of Agronomy 18, 289–307.
- Stricevic, R., Cosic, M., Djurovic, N., Pejic, B., Maksimovic, L., 2011. Assesment of the FAO AquaCrop model in the simulation of rainfed and supplementally irrigated maize sugar beet and sunflower. Agricultural Water Management 98, 1615–1621.
- Tanner, C.B., Sinclair, T.R., 1983. Efficient water use in crop production: research or re-search? In: Taylor, H.M., Jordan, W.A., Sinclair, T.R. (Eds.), Limitations to EfficientWater Use inCropProduction,AmericanSociety ofAgronomy,Madison.
- Teklu, E., Awulachew, S.B., 2009. Soil fertility effect on water productivity of maize and potato. AquaCrop Workshop, Cairo, 25–29 October.
- Todorovic, M., Albrizio, R., Zivotic, L., Saab, M.T.A., Stockle, C., Steduto, P., 2009. Assessment of Aqua Crop, CropSyst, and WOFOST models in the simulation of sunflower growth under different water regimes. Journal of Agronomy 101 (3), 509–521.
- Yang, H.S., Dobermann, A., Lindquist, J.L., Walters, D.T., Arkebauer, T.J., Cassman, K.G., 2004. Hybrid-maize—a maize simulation model that combines two crop modeling approaches. Field Crops Research 87, 131–154.