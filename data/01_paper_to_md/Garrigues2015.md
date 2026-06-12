<span id="page-0-1"></span>Hydrol. Earth Syst. Sci., 19, 3109–3131, 2015 www.hydrol-earth-syst-sci.net/19/3109/2015/ doi:10.5194/hess-19-3109-2015 © Author(s) 2015. CC Attribution 3.0 License.

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

# **Evaluation of land surface model simulations of evapotranspiration over a 12-year crop succession: impact of soil hydraulic and vegetation properties**

**S. Garrigues**[1,2](#page-0-0) **, A. Olioso**[1,2](#page-0-0) **, J. C. Calvet**[3](#page-0-0) **, E. Martin**[3](#page-0-0) **, S. Lafont**[5](#page-0-0) **, S. Moulin**[1,2](#page-0-0) **, A. Chanzy**[1,2](#page-0-0) **, O. Marloie**[4](#page-0-0) **, S. Buis**[1,2](#page-0-0) **, V. Desfonds**[1,2](#page-0-0) **, N. Bertrand**[1,2](#page-0-0) **, and D. Renard**[1,2](#page-0-0)

EMMAH (UMR1114), INRA, Avignon, France Université d'Avignon et des Pays de Vaucluse, UMR1114 – EMMAH, 84000 Avignon, France CNRM-GAME (UMR3589), Météo-France, CNRS, Toulouse, France URFM, INRA, Avignon, France 5 ISPA, INRA, Bordeaux, France

*Correspondence to:* S. Garrigues (sebastien.garrigues@paca.inra.fr)

Received: 8 August 2014 – Published in Hydrol. Earth Syst. Sci. Discuss.: 23 October 2014 Revised: 22 May 2015 – Accepted: 28 May 2015 – Published: 16 July 2015

<span id="page-0-0"></span>**Abstract.** Evapotranspiration has been recognized as one of the most uncertain terms in the surface water balance simulated by land surface models. In this study, the SURFEX/ISBA-A-gs (Interaction Sol–Biosphere– Atmosphere) simulations of evapotranspiration are assessed at the field scale over a 12-year Mediterranean crop succession. The model is evaluated in its standard implementation which relies on the use of the ISBA pedotransfer estimates of the soil properties. The originality of this work consists in explicitly representing the succession of crop cycles and inter-crop bare soil periods in the simulations and assessing its impact on the dynamics of simulated and measured evapotranspiration over a long period of time. The analysis focuses on key parameters which drive the simulation of ET, namely the rooting depth, the soil moisture at saturation, the soil moisture at field capacity and the soil moisture at wilting point. A sensitivity analysis is first conducted to quantify the relative contribution of each parameter on ET simulation over 12 years. The impact of the estimation method used to retrieve the soil parameters (pedotransfer function, laboratory and field methods) on ET is then analysed. The benefit of representing the variations in time of the rooting depth and wilting point is evaluated. Finally, the propagation of uncertainties in the soil parameters on ET simulations is quantified through a Monte Carlo analysis and compared with the uncertainties triggered by the mesophyll conductance which is a key above-ground driver of the stomatal conductance.

This work shows that evapotranspiration mainly results from the soil evaporation when it is continuously simulated over a Mediterranean crop succession. This results in a high sensitivity of simulated evapotranspiration to uncertainties in the soil moisture at field capacity and the soil moisture at saturation, both of which drive the simulation of soil evaporation. Field capacity was proved to be the most influencing parameter on the simulation of evapotranspiration over the crop succession. The evapotranspiration simulated with the standard surface and soil parameters of the model is largely underestimated. The deficit in cumulative evapotranspiration amounts to 24 % over 12 years. The bias in daily daytime evapotranspiration is −0.24 mm day−1 . The ISBA pedotransfer estimates of the soil moisture at saturation and at wilting point are overestimated, which explains most of the evapotranspiration underestimation. The use of field capacity values retrieved from laboratory methods leads to inaccurate simulation of ET due to the lack of representativeness of the soil structure variability at the field scale. The most accurate simulation is achieved with the average values of the soil properties derived from the analysis of field measurements of soil moisture vertical profiles over each crop cycle. The representation of the variations in time of the wilting point and the maximum rooting depth over the crop succession has little impact on the simulation performances. Finally, we show that the uncertainties in the soil parameters can generate substantial uncertainties in ET simulated over 12 years (the 95 % confidence interval represents 23 % of cumulative ET over 12 years). Uncertainties in the mesophyll conductance have lower impact on ET. Measurement random errors explain a large part of the scattering between simulations and measurements at half-hourly timescale. The deficits in simulated ET reported in this work are probably larger due to likely underestimation of ET by eddy-covariance measurements. Other possible model shortcomings include the lack of representation of soil vertical heterogeneity and root profile along with inaccurate energy balance partitioning between the soil and the vegetation at low leaf area index.

#### **1 Introduction**

Land surface models (LSMs) are relevant tools to analyse and predict the evolution of the water balance at various spatial and temporal scales. They describe water, carbon and energy fluxes between the surface and the atmosphere at an hourly timescale. Most LSMs consist of 1-D column models describing the non-saturated soil (mainly the root zone), the vegetation and the surface–atmosphere interaction processes. The LSM complexity mainly differs in (1) the number of sources involved in the surface energy balance, (2) the representation of water and thermal soil transfers, and (3) the representation of stomatal conductance (see reviews in Olioso et al., 1999; Arora, 2002; Pitman, 2003; Overgaard et al., 2006; Bonan, 2010). For example, the original version of the Interactions between Soil, Biosphere, and Atmosphere (ISBA; Noilhan and Planton, 1989) computes a single energy budget assuming a unique "big leaf" layer. It is a simple bucket model based on the force-restore method with two or three soil layers. The stomatal conductance is simply represented by the Jarvis (1976) empirical formulation. More advanced LSMs resolve a double-source energy budget (e.g. Sellers and Dorman, 1987) and implement a multi-layer soil diffusion scheme (e.g. Braud et al., 1995b). They can also explicitly simulate photosynthesis (Olioso et al., 1996) and its functional coupling with plant transpiration and they represent vegetation dynamics (Calvet et al., 2008; Egea et al., 2011). Progress in LSMs led to more accurate estimations of energy and water fluxes. This resulted in more realistic simulations of air temperature and humidity of the surface boundary layer in atmospheric models (Noilhan et al., 2011). The improvement of the surface water budget in hydrological models permitted more accurate streamflow forecasts (Habets et al., 2008) and drought monitoring (Vidal et al., 2010). LSMs also proved their usefulness for agronomy application such as irrigation monitoring (Olioso et al., 2005).

This work focuses on the evaluation of the evapotranspiration (ET) simulated from a land surface model over a crop site for a long period of time. ET has been recognized as one of the most uncertain terms in the surface water balance (Dolman and de Jeu, 2010; Mueller and Seneviratne, 2014). Uncertainties in simulated ET may propagate large errors in both LSM–atmosphere and LSM–hydrological coupled models. ET uncertainties can arise from (1) errors in the large-scale data sets used to force LSMs, (2) shortcomings in the model structure, and (3) errors in the parameter values. Since LSMs were originally designed to be coupled with atmospheric or hydrological models over large areas, their parametrization is generally parsimonious and their spatial integration is generally based on coarse-resolution (∼ 1– 10 km) maps of parameters. Surface parameters drive a large part of LSM uncertainties and explain most discrepancies between models (Chen et al., 1997; Gupta et al., 1999; Olioso et al., 2002; Boone et al., 2004). The representation of cropland and their temporal dynamics over a long period of time need to be improved in LSMs (Lafont et al., 2011; Bonan and Santanello, 2013). Past evaluation studies focused on particular crop types for limited periods of time. They disregarded the succession of crop and inter-crop periods and its impact on the simulated water balance over a long period of time.

The uncertainties in soil hydraulic properties can be large due to significant spatiotemporal variability (Braud et al., 1995a), uncertainties in the estimation method (Baroni et al., 2010; Steenpass et al., 2011) and spatial scale mismatch between the local measurements and the operational scale of the model (Mertens et al., 2005). Errors in soil hydraulic properties can have significant impact on LSM simulations of ET and soil water content (Jacquemin and Noilhan, 1990; Braud et al., 1995a; Cresswell and Paydar, 2000). Their impact on the model can be larger than the structural model uncertainties (Workmann and Skaggs, 1994; Baroni et al., 2010). Since the soil hydraulic properties are rarely known over large areas, they are generally derived from empirical pedotransfer functions which relate the soil hydrodynamic properties to readily available variables such as soil texture and bulk density (Cosby et al., 1984; Vereecken et al., 1989; Schaap et al., 2001). These functions may not be accurate enough to describe the spatial variability of the soil hydrodynamic characteristics across soil types and their impact on LSM simulations need to be assessed locally (Espino et al., 1996; Baroni et al., 2010).

In this study, the ISBA-A-gs version (Calvet et al., 1998) of the ISBA LSM (Noilhan and Planton, 1989) is considered. ISBA-A-gs includes a coupled stomatal conductancephotosynthesis scheme. Local site studies demonstrated that ISBA (Noilhan and Mahfouf, 1996) and ISBA-A-gs (Gibelin et al., 2008) are able to correctly simulate the diurnal and seasonal time courses of energy fluxes and soil water content, over contrasted soil and vegetation types. More variable performances were obtained by Olioso et al. (2002) over wheat fields with possible underestimation of ET.

### **S. Garrigues et al.: Evaluation of land surface model simulations of evapotranspiration 3111**

This paper aims at evaluating the ISBA-A-gs simulations of ET over a 12-year Mediterranean crop succession. We focus on key drivers of simulated ET:

- **–** the soil moisture at saturation (θs) which is involved in the simulation of soil evaporation;
- **–** the soil moisture at field capacity (θfc), the soil moisture at wilting point (θwp) and the maximum rooting depth (Zroot-zone, referred to as rooting depth hereafter). These parameters define the maximum water stock available for the crop which controls the plant transpiration. The wilting point and the rooting depth are two cropdependent parameters which can lead to large variations in time of the root-zone water reservoir over the crop succession (Wetzel and Chang, 1987; Verhoef and Egea, 2014).

In the rest of the text, the term "soil parameter" refers to θs , θfc, θwp and Zroot-zone. The simulations are assessed over the Avignon "remote sensing and fluxes" crop site where 14 arable crop cycles and 14 inter-crop periods were monitored through continuous measurements of soil water content and surface fluxes between April 2001 and December 2012. We represent the succession of crop cycles and inter-crop bare soil periods in the simulations. We address the following aspects.

- **–** The impact of crop rotation on the dynamics of ET and root-zone soil moisture.
- **–** The overall performances of the ISBA-A-gs simulations achieved with the standard soil and vegetation parameters over a 12-year Mediterranean crop succession.
- **–** The relative influence of each soil parameter on the simulation of ET and its soil/vegetation components, over a crop succession through a sensitivity analysis.
- **–** The impact of the method used to retrieve the soil parameters on simulated ET. We test pedotransfer function, laboratory measurement and field monitoring methods. While constant values in time of the soil parameters are generally used in LSM, we assess whether the representation of the variations in time of the wilting point and the maximum rooting depth over the crop succession improves the simulation of ET.
- **–** The propagation of uncertainties in the soil parameters on ET predictions. We quantified it through a Monte Carlo analysis and we compared it with the uncertainties triggered by the mesophyll conductance which is a key above-ground vegetation parameter involved in the stomatal conductance.

In discussion, we explain how the investigated soil parameters influence the simulation of ET over the crop succession, we discuss the sources of uncertainties related to each soil

![](_page_2_Figure_11.jpeg)

**Figure 1.** Map of the field site and locations of the instruments. Image from Google Earth, 2009.

parameter retrieval method and we put into perspective the model performances by quantifying the uncertainties in measured ET.

#### **2 Site and measurements**

#### **2.1 Site characteristics**

The "remote sensing and flux site" of INRA (National Institute of Agronomic Research) Avignon1 (France; 43◦55000.400 N, 4◦52041.000 E (WGS84 system); alt = 32 m a.s.l.) is characterized by a Mediterranean climate with a mean annual temperature of 14 ◦C and a mean annual precipitation of 687 mm. Rainfall mainly occurs in autumn (43 % of yearly rainfall). It is a flat agricultural field oriented north–south in the prevailing wind direction (Fig. 1). The field size is 1.9 ha. In this work, we study a 12-year crop succession from April 2001 to December 2012 (Fig. 2, Table 1). The crop succession consists in a succession of winter arable crops (wheat, peas) and summer arable crops (sorghum, maize, sunflower). Periods between two consecutive crop cycles lasted ∼ 1–1.5 months in the case of a summer crop followed by a winter crop and ∼ 9–10 months in the reverse case. During inter-crop periods, the soil is mostly bare. Limited wheat regrowths occurred over short periods of time. Irrigation is triggered only for summer crops (every 2 years) and concerns the May–July period.

#### **2.2 Field measurements**

Soil moisture, plant characteristics and micrometeorological observations were continuously monitored over the 12-year

<sup>1</sup>[https://www4.paca.inra.fr/emmah_eng/Facilities/](https://www4.paca.inra.fr/emmah_eng/Facilities/In-situ-facilities/Remote-Sensing-Fluxes) [In-situ-facilities/Remote-Sensing-Fluxes](https://www4.paca.inra.fr/emmah_eng/Facilities/In-situ-facilities/Remote-Sensing-Fluxes)

crop succession. A map of the field with the location of the instruments is given in Fig. 1.

# **2.2.1 Soil measurements**

A neutron probe was used to retrieve volumetric soil moisture in three (0–1.90 m) soil profiles with a vertical resolution of 10 cm. To implement the measurements, three neutron probe access tubes, spaced 40 m apart, were installed along a north–south transect located at the centre of the field. A calibration was done for every access tube and soil layer by relating neutron count rates to soil moisture measured by gravimetric method. The average soil moistures at given depth over the soil profiles were then used. The measurements were performed on a weekly basis.

Surface ground heat flux (G) was derived from four heat flux plate measurements located at 5 cm depth. One plate was located along the crop row and the others were equally spaced apart in the inter-row. We accounted for heat storage estimated from temperature and soil moisture measured within the 5 cm layer.

# **2.2.2 Plant measurements**

Plant characteristics (leaf area index (LAI), height, biomass) were monitored over all the crop cycles between April 2001 and December 2012. Canopy height was measured every 10 days using a standard measuring tape. Leaf area index and plant biomass were measured at key crop phenological stages (five to six measurements per crop cycle) using destructive methods and sampling schemes adapted to each crop. LAI was retrieved using a planimeter device and plant biomass was measured using a high-precision scale device. Plant characteristics were measured at four locations in the field (Fig. 2) to sample the within field variability. Average values were recorded. Vegetation height was linearly interpolated on a daily basis. Daily interpolation of LAI was achieved using a functional relationship between LAI and the sum of degree days (Duveiller et al., 2011).

# **2.2.3 Micrometeorological measurements**

Half-hourly observations of air temperature and humidity, wind speed, and atmospheric pressure were continuously monitored at a height of 2 m above the ground or the canopy from a micro-meteorological station located at the centre of the field. Cumulative rainfall was measured from a standard meteorological station located at 150 m apart from the centre of the field. Net radiation (RN) was computed from shortwave and longwave upwelling and downwelling radiations which are measured from a net radiometer device located at the centre of the field and oriented southward.

Sensible (H) and latent (LE) heat fluxes were computed from an eddy-covariance system oriented northward in the prevailing wind direction. The latter was composed of a 3-D sonic anemometer set up in 2001 and of an open-path gas (H2O, CO2) analyser set up in November 2003. The system was monitored following the state-of-the-art guidelines for cropland sites (Rebmann et al., 2012; Moureaux et al., 2012). Fluxes were computed on 30 min intervals using the EDIRE software2 . The flux data processing included spike detection on raw data and standard eddy-covariance corrections (coordinate rotation, density fluctuations, frequency loss). The ECPP3 software (Beziat et al., 2009) was used to discard spurious flux (e.g. friction velocity and footprint controls) and to apply the Foken et al. (2004) quality control tests on the temporal stationarity and the development of turbulence conditions. In this work, only the best quality class of data (Mauder et al., 2013) were used. An additional threshold of 100 W m−2 on the energy balance nonclosure was applied to eradicate very inconsistent fluxes. Direct eddy-covariance measurements of LE are used over the 20 November 2003–18 December 2012 period. They represent 60 % of the period (71 % if we consider only daytime). When no direct measurement of LE was available (2001– 2003 period), LE was estimated as the residue of the energy balance (LE = RN − G − H). Valid direct and indirect LE measurements represent 65 % of the 25 April 2001–18 December 2012 period (77 % of daytime). Cumulative ET in millimetres over a given period of time was computed from LE half-hourly measurements.

# **2.3 Soil properties**

Table 2 presents the values of the soil parameters averaged over the 0–1.2 m soil layer, where most of the root-zone processes occur. The soil moisture at saturation (θs) was derived from soil bulk density measurements performed within the 0–1.2 m layer at different field locations and times over the 12-year period. We used the average value of θs to be representative of the soil structure at the field scale at which the simulations were conducted. The soil moisture at field capacity (θfc) and wilting point (θwp) were retrieved using laboratory or field methods.

- 1. Laboratory method: it consisted in adjusting a Brooks and Corey (1966) retention curve model over soil matric potential (h) and soil water content measured in laboratory. These measurements were obtained from the Richard pressure plate apparatus at matric potentials of −1, −2, −3, −5, −10, −30, −50, −100, and −150 m (Bruckler et al., 2004). They were collected for three soil layers at depths of 0–0.4, 0.4–0.8 and 0.8– 1.2 m. A retention model was adjusted for each soil layer and was used to retrieve θfc and θwp for each soil layer. θwp was computed for h = −150 m. Most studies agree on this definition (Boone et al., 1999; Olioso et
<sup>2</sup>Robert Clement, ©1999, University of Edinburgh, UK, [http:](http://www.geos.ed.ac.uk/abs/research/micromet/EdiRe) [//www.geos.ed.ac.uk/abs/research/micromet/EdiRe.](http://www.geos.ed.ac.uk/abs/research/micromet/EdiRe)

<sup>3</sup>Eddy Covariance Post-Processing, Pierre Béziat, CESBIO, Toulouse, France.

**Table 1.** 2001–2012 crop succession.

| Year | Crop       | Sowing      | Harvest     | Irrigation | Rain  | T    |
|------|------------|-------------|-------------|------------|-------|------|
|      |            | date        | date        | (mm)       | (mm)  | (◦C) |
| 2001 | Maize      | 25 Apr 2001 | 28 Sep 2001 | 375        | 232.0 | 20.7 |
| 2002 | Wheat      | 23 Oct 2001 | 2 Jul 2002  | 0          | 399.0 | 11.6 |
| 2003 | Sunflower1 | 16 Apr 2003 | 26 May 2003 | 40         | 68.0  | 17.1 |
| 2003 | Sunflower  | 2 Jun 2003  | 19 Sep 2003 | 225        | 68.5  | 24.8 |
| 2004 | Wheat      | 7 Nov 2003  | 28 Jun 2004 | 0          | 422.0 | 11.2 |
| 2005 | Peas       | 13 Jan 2005 | 22 Jun 2005 | 100        | 203.5 | 11.9 |
| 2006 | Wheat      | 27 Oct 2005 | 27 Jun 2006 | 20         | 256.0 | 10.7 |
| 2007 | Sorghum    | 10 May 2007 | 16 Oct 2007 | 80         | 168.5 | 20.6 |
| 2008 | Wheat      | 13 Nov 2007 | 1 Jul 2008  | 20         | 502.5 | 11.7 |
| 2009 | Maize2     | 23 Apr 2009 | 15 Jun 2009 | 80         | 110.5 | 19.2 |
| 2009 | Sorghum    | 25 Jun 2009 | 22 Sep 2009 | 245        | 89.0  | 23.6 |
| 2010 | Wheat      | 19 Nov 2009 | 13 Jul 2010 | 0          | 446.5 | 11.6 |
| 2011 | Sorghum    | 22 Apr 2011 | 22 Sep 2011 | 60         | 268.5 | 21.4 |
| 2012 | Wheat      | 19 Oct 2011 | 25 Jun 2012 | 0          | 437.0 | 12.0 |
|      |            |             |             |            |       |      |

The first sunflower in 2003 (1) was stopped and replaced by a new one. The 2009 maize (2) was stopped and replaced by sorghum because the emergence of maize was too heterogeneous. T and rain are the mean temperature and cumulative precipitation, respectively, over the crop cycle.

![](_page_4_Figure_5.jpeg)

**Figure 2.** Illustration of the typical succession of winter and summer crop over the Avignon site and implementation of the crop succession in the simulations. θ and T represent soil moisture and soil temperature transmitted from one sub-simulation to the following one.

al., 2002). For wfc two definitions were used. We estimated θfc at h = −3.3 m, which corresponds to the agronomic definition (Olioso et al., 2002) and for a hydraulic conductivity of K = 0.1 mm day−1 which can be found in hydrological applications (Wetzel and Chang, 1987; Bonne et al., 1999). θwp and θfc estimates were averaged over the 0–1.2 m soil profile and their values are reported in Table 2.

- 2. Field method: θfc and θwp were inferred from field measurements of soil moisture. The time evolution of the root-zone (0–1.2 m) soil moisture was analysed over each crop cycle. Under Mediterranean climate, the rootzone soil moisture generally starts from an upper-level which approximates θfc. It generally reaches a lowerlevel at the end of the growing season which often ap-
proaches θwp. The typical evolution of the root-zone soil moisture over the growing season is illustrated in Fig. 5b for wheat. To be consistent with the previous method, we integrated the soil moisture measurements over the 0–0.4, 0.4–0.8 and 0.8–1.2 m soil layers. θfc and θwp were estimated for each soil layer as the maximum and the minimum, respectively, soil moisture over the growing season. θfc and θwp values were averaged over the 0–1.2 m soil profile for each crop cycle (Table 3). θwp varies from one crop to another, but its mean value is close to the one derived from the retention curve. θfc shows lower temporal variability but its mean value significantly differs from the retention curve estimate.

The maximum rooting depth (Zroot-zone) was estimated from the analysis of the evolution in time of the vertical profiles

**Table 2.** Mean soil properties over the 0–1.2 m soil profile. Density is the soil bulk density. θs is the soil moisture at saturation derived from bulk density measurements. θwp and θfc are the soil moisture at wilting point and field capacity, respectively, derived from laboratory methods for given hydraulic conductivity (K) or matric potential (h) levels. The second and third rows represent the vertical (σV) and the spatiotemporal (σST) variability of these measurements, respectively. NA means not available.

|           | Clay<br>(%) | Sand<br>(%) | Density<br>(g cm−3<br>) | θs<br>(m3 m−3<br>) | θwp<br>(h = −150 m)<br>(m3 m−3<br>) | θfc<br>(h = −3.3 m)<br>(m3 m−3<br>) | θfc<br>0.1 mm day−1<br>(K =<br>)<br>(m3 m−3<br>) |
|-----------|-------------|-------------|-------------------------|--------------------|-------------------------------------|-------------------------------------|--------------------------------------------------|
| Mean      | 33.15       | 13.95       | 1.57                    | 0.390              | 0.170                               | 0.344                               | 0.268                                            |
| σV<br>σST | 0.58<br>NA  | 1.14<br>NA  | 0.16<br>0.05            | 0.056<br>0.019     | 0.011<br>NA                         | 0.021<br>NA                         | 0.027<br>NA                                      |

**Table 3.** Estimates of the rooting depth (Zroot-zone), the soil moisture at field capacity (θfc) and the soil moisture at wilting point (θwp) derived from the time evolution of vertical profiles of fieldmeasured soil moisture. MaxAWC (maximum available soil water capacity; in mm) represents the maximum root-zone water stock available for the crop. When no measurements were available, the mean value (in italic) from a similar crop type was used. The last two rows are the mean and the SD (standard deviation) computed over all crop cycles.

| Crop      | Year | Zroot-zone<br>(m) | θfc<br>(m3 m−3<br>) | θwp<br>(m3 m−3<br>) | MaxAWC<br>(mm) |  |
|-----------|------|-------------------|---------------------|---------------------|----------------|--|
| Maize     | 2001 | 1.45              | 0.320               | 0.174               | 212            |  |
| Wheat     | 2002 | 1.55              | 0.314               | 0.126               | 291            |  |
| Sunflower | 2003 | 1.80              | 0.311               | 0.209               | 184            |  |
| Wheat     | 2004 | 1.65              | 0.314               | 0.183               | 216            |  |
| Peas      | 2005 | 1.00              | 0.308               | 0.218               | 90.0           |  |
| Wheat     | 2006 | 1.85              | 0.309               | 0.179               | 241            |  |
| Sorghum   | 2007 | 1.65              | 0.306               | 0.183               | 203            |  |
| Wheat     | 2008 | 1.00              | 0.279               | 0.202               | 77.0           |  |
| Maize     | 2009 | 1.45              | 0.320               | 0.174               | 212            |  |
| Sorghum   | 2009 | 1.65              | 0.306               | 0.183               | 203            |  |
| Wheat     | 2010 | 1.75              | 0.327               | 0.182               | 254            |  |
| Sorghum   | 2011 | 1.65              | 0.306               | 0.183               | 203            |  |
| Wheat     | 2012 | 1.50              | 0.309               | 0.174               | 203            |  |
| Mean      |      | 1.50              | 0.310               | 0.184               | 189            |  |
| SD        |      | 0.30              | 0.012               | 0.025               | 56.0           |  |

of soil moisture field measurements over the growing season of each crop period. Zroot-zone was approximated by the depth at which the soil moisture change in time vanished (Table 3). We assumed that at a given depth, the time variations in soil moisture due to the vertical diffusion and gravitational drainage were smaller than those generated by the plant water uptake (Olioso et al., 2002). This is a reasonable hypothesis for low hydraulic conductivity soil as the one under study. The Zroot-zone = 1.85 m obtained for wheat in 2006 can be related to the dryness of the crop period (256 mm of rain). The shallower Zroot-zone = 1.0 m obtained for wheat in 2008 can be related to the wetness of the crop period (500 mm of rain).

#### **3 The ISBA-A-gs model**

#### **3.1 Model description**

The ISBA model (Noilhan and Planton, 1989; Noilhan and Mahfouf, 1996) is developed at the CNRM (National Centre for Meteorological Research)/Météo France within the SUR-FEX surface modelling platform (Masson et al., 2013). In this study, we used the version 6.1 of SURFEX. ISBA relies on a single surface energy budget of a soil–vegetation composite. The surface temperature is simulated using the Bhumralkar (1975) and Blackadar (1976) force restore scheme for heat transfers. A horizontal soil/snow/ice/vegetation surface partitioning is used to simulate the evapotranspiration. The soil water transfers are simulated using a force-restore scheme adapted from Deardoff (1977) with three reservoirs: the superficial layer of thickness dsurf = 0.01 m designed to regulate the soil evaporation, the root zone which extends from the surface to the depth Zroot-zone and the deep reservoir which extends from the base of the root zone to the total soil depth. The force restore coefficients were parameterized as a function of the soil hydrodynamic properties which were derived from the Brooks and Corey (1966) retention model. θfc and θwp are defined for K = 0.1 mm day−1 and for h = −150 m, respectively. The soil parameters are derived from clay and sand fractions using the ISBA pedotransfer functions. The latter were built upon on the Clapp and Hornberger (1978) soil texture classification using statistical multiple regressions (Noilhan and Laccarère, 1994). The forcerestore equations and coefficient formulas are given in Boone et al. (1999). Regarding the vegetation processes, we used the A-gs version of ISBA (Calvet et al., 1998, 2008). A-gs is a coupled stomatal conductance–photosynthesis scheme. It uses a CO2 responsive parametrization of photosynthesis based on the model of Goudriaan et al. (1985) and modified by Jacobs et al. (1996). It computes the stomatal conductance as a function of the net assimilation of CO2. The CO2 mesophyll conductance at a leaf temperature of 25◦ (gm) is the main tunable parameter of the A-gs scheme (Calvet et al., 1998, 2012). It represents the response curve of the lightsaturated net rate of CO2 assimilation to the internal CO2

concentration. The simulation of the plant response to water stress (Calvet, 2000; Calvet et al., 2012) is mainly driven by the maximum root-zone water stock available for the plant (MaxAWC) which is defined by

$$\text{MaxAWC} = Z_{\text{root-zone}} \left( \theta_{\text{fc}} - \theta_{\text{wp}} \right) . \tag{1}$$

The model is parametrized through 12 generic land surface patches using the ECOCLIMAP-II database which provides the ISBA surface parameters for ∼ 273 distinct land cover types over Europe (Faroux et al., 2013).

#### **3.2 Model implementation at the Avignon site**

The simulations were conducted at the field scale. ISBA-Ags was run at a 5 min time step and 30 min outputs of the state variables were analysed. Continuous simulations were performed from 25 April 2001 up to 18 December 2012. The 12 year period was split into sub-simulations corresponding to crop and inter-crop periods (Fig. 2). The simulation was initialized once on 25 April 2001 using in situ soil temperature and soil moisture measurements for each soil layer. To ensure the continuity between two contiguous sub-simulations, each sub-simulation was initialized using the simulated soil moisture and soil temperature of the last time step of the previous sub-simulation. The C3 crop patch was used to represent wheat, pea and sunflower crops. The C4 crop patch was used for maize and sorghum crops. Inter-crop periods were represented by the bare soil patch. ISBA-A-gs was driven by local meteorological observations. It was forced by in situ LAI and vegetation height measurements averaged over 10 days. Crop irrigation was not simulated by the model and the actual amount of irrigation water was added to the local rainfall. The simulations were designed to be representative of the field scale. The values of the in situ soil and vegetation parameters used in the simulations correspond to the field average.

#### **4 Methodology**

This paper focuses on the evaluation of the ISBA-A-gs simulations of ET over the 12-year crop succession of the Avignon site. We focus on key soil parameters for the simulation of ET.

- **–** The soil moisture at saturation (θs) which is involved in the simulation of soil evaporation.
- **–** The field capacity (θfc), the wilting point (θwp) and the rooting depth (Zroot-zone) which control the plant transpiration through MaxAWC (Eq. 1). Table 3 shows that θwp and Zroot-zone are two crop-dependent parameters which can trigger large variations in time of MaxAWC over the crop succession. The variations in time of θfc are much lower than for θwp and Zroot-zone. We thus investigate the impact of using time-variable θwp and

**Table 4.** Values of the soil parameters used in the simulations. PTF corresponds to the standard implementation of the model achieved with the ECOCLIMAP-II rooting depth (Zroot-zone) and the pedotransfer estimates of the wilting point (θwp), the field capacity (θfc) and the saturation (θs). Distinct in situ estimates of these parameters are used in the other simulations. CV means time-variable values of Zroot-zone and θwp retrieved over each crop cycle (see Table 3). MaxAWC is the maximum root-zone water stock available for the crop.

|                                                                                                      | Simulation cases                      |                                       |                                       |                                  |  |  |  |  |  |  |
|------------------------------------------------------------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------|--|--|--|--|--|--|
| Soil parameters                                                                                      | PTF                                   | LAB                                   | FIELDcst                              | FIELDvar                         |  |  |  |  |  |  |
| (m3 m−3<br>θs<br>)<br>(m3 m−3<br>θfc<br>)<br>(m3 m−3<br>θwp<br>)<br>Zroot-zone<br>(m)<br>MaxAWC (mm) | 0.479<br>0.303<br>0.214<br>1.5<br>134 | 0.390<br>0.268<br>0.170<br>1.5<br>147 | 0.390<br>0.310<br>0.184<br>1.5<br>189 | 0.390<br>0.310<br>CV<br>CV<br>CV |  |  |  |  |  |  |

| Zroot-zone |                                                 |  | parameters over the crop succession and we |  |
|------------|-------------------------------------------------|--|--------------------------------------------|--|
|            | assume a constant in time field capacity value. |  |                                            |  |

Distinct simulations are performed and compared (Table 4) to test the influence of these soil parameters on simulated ET.

#### **4.1 Simulation cases**

The simulation PTF corresponds to the standard implementation of the model. The above-ground vegetation parameters, the rooting depth (1.5 m) and the deep reservoir size (0.5 m) are provided by the ECOCLIMAP-II database (Gibelin et al., 2006; Faroux et al., 2013). The soil hydraulic properties (θs , θfc, θwp) are derived from the local soil texture using the ISBA pedotransfer functions (Noilhan and Laccarère, 1994). No local calibration of the standard parameters is performed to test the portability of the parameters over a typical Mediterranean crop succession. The soil parameters are constant over the crop succession.

The simulations LAB, FIELDcst and FIELDvar use in situ values of Zroot-zone, θs , θfc and θwp (Table 4). The rest of parameters are those used in PTF. The Zroot-zone value used in LAB and FIELDcst is the average value of the rooting depths estimated from the soil moisture measurements over each crop cycle (Sect. 2.2). Its value (1.5 m) is equal to the ECOCLIMAP-II value used in PTF. LAB, FIELDcst and FIELDvar use the same field-average estimate of θs derived from soil bulk density measurements. They mainly differ in the method used to retrieve θfc and θwp:

- **–** LAB uses θfc and θwp retrieved from the retention curve model established from laboratory measurements (Table 2). θwp corresponds to the matric potential h = −150 m. θfc corresponds to the hydraulic conductivity K = 0.1 mm day−1 to be consistent with the definition used by the ISBA pedotransfer method (PTF case).
- **–** FIELDcst and FIELDvar use θfc and θwp estimated from the monitoring of field soil moisture measurements over each crop cycle (Table 3). FIELDcst uses a constant in time values of θwp and Zroot-zone. It takes their temporal average values computed over the crop succession (Table 3). FIELDvar accounts for the variations in time of θwp and Zroot-zone over the crop succession (Table 3). Both FIELDcst and FIELDvar use the average value of θfc over the crop succession.
# **4.2 Experiment analyses**

We conduct the following analyses.

- **–** *The first analysis* consists in assessing the impact of the crop succession on the dynamics of simulated and measured ET and θroot-zone.
- **–** *In the second analysis*, we assess the overall performances of the standard simulation PTF over the 12-year crop succession.
- **–** *The third analysis* aims at quantifying the influence of each soil parameter (θs , θfc, θwp) on ET over the crop succession. We conduct a sensitivity analysis based on the PTF case. The parameters are tested one by one. We do not explore the interactions between parameters which are investigated in the following analysis. We explore similar variations in θs , θfc and θwp around their standard values used in the simulation PTF (±0.015, ±0.03). We also investigate the sensitivity of simulated ET to errors in these parameters by testing their in situ values used in the FIELDcst experiment. We do not consider variations in Zroot-zone. If the latter lead to similar variations in MaxAWC (Eq. 1) as those triggered by θwp, its impact on ET will be similar than the impact of θwp. In this work a 0.25 m variation in Zroot-zone leads to a similar increase in MaxAWC and transpiration as a decrease of θwp by 0.015 m3 m−3 .
- **–** *In the fourth analysis*, we investigate the impact of the method used to retrieve θs , θfc and θwp. We compare the PTF, LAB and FIELDcst simulation cases. By comparing FIELDcst and FIELDvar, we evaluate whether the representation of the variation in time of the wilting point and the rooting depth over the crop succession improves the simulation of ET. Finally, we select the estimation method that leads to the best representation of ET over the crop succession at the field scale.
- **–** *The last analysis* consists in quantifying the propagation of uncertainties in the soil parameters on ET predictions. To assess the relative importance of the impact of uncertainties in the soil parameters, we compare it with the impact of uncertainties in the mesophyll conductance which is a key above-ground vegetation parameter involved in the simulation of the stomatal conductance

and the transpiration (Calvet et al., 2012). To address these issues, we conducted two Monte Carlo analyses to generate two ensembles of 100 ET simulations for the FIELDcst simulation case.

- The Monte Carlo scheme was first applied to the soil parameters tested in this work (Zroot-zone, θs , θfc and θwp). We chose to represent the uncertainties in the soil parameters by their temporal and spatial variability at the field scale quantified in Tables 2 and 3. The distribution of the soil parameters is assumed to be Gaussian (Table 8).
- The Monte Carlo scheme was then applied to the mesophyll conductance (gm). We assumed a Gaussian probability distribution function for gm (Table 8). The mean is the standard value given by Gibelin et al. (2006) and used in FIELDcst and the standard deviation is derived from literature metaanalysis (Calvet, 2000; Calvet et al., 2004).

# **4.3 Simulation performance metrics**

The simulations were qualitatively evaluated comparing measured and simulated ET cumulated over the 25 April 2001–18 December 2012 period. Cumulative ET data were concomitantly analysed with the root-zone soil moisture (θroot-zone) changes in time over selected crop cycles or inter-crop periods to identify the deficiencies in ET modelling. Cumulative values were computed over the time steps for which valid ET measurements were available. Daily daytime ET (ETd) were computed when 90 % of daytime measurements were valid for each day.

The simulation performance scores were quantified using the root mean square error (RMSE), the bias (BIAS), the standard deviation of the differences between simulations and measurements (SDD) and the correlation coefficient (r). These metrics were applied to half-hourly energy fluxes, θroot-zone and ETd. They were computed over the 20 November 2003–18 December 2012 period using only direct eddycovariance measurements of LE.

# **5 Results**

# **5.1 Impact of the crop succession on the dynamics of evapotranspiration and soil water content**

Figure 3 illustrates the influence of the succession of crop periods and bare soil inter-crop periods on the temporal evolution of simulated and measured ET and root-zone soil moisture (θroot-zone).

The early stages of crop periods show high θroot-zone which results from rainfall for winter crops and irrigation in May– June for summer crops. Crop growing periods are marked by abrupt increases in ET which is related to plant transpiration. This is concomitant with the depletion of θroot-zone

![](_page_8_Figure_1.jpeg)

**Figure 3.** Evolution of simulated and measured evapotranspiration (ET in mm), simulated soil evaporation (E in mm), simulated plant transpiration (T in mm), simulated and measured daily daytime ET (ETd in mm), simulated and measured daily mean of root-zone soil moisture (θroot-zone in m3 m−3 ), 10-day rainfall plus irrigation (in mm), daily mean of in situ LAI (in m2 m−2 ) over the 2001–2012 period. For clarity, the average of daily values over 10 days are displayed. The simulation corresponds to the standard implementation of the model (PTF). Crop and inter-crop periods are represented by grey and white backgrounds, respectively. Meas and Sim mean measured and simulated, respectively.

which usually reaches its lower level at the end of the crop cycles. Daily ET reaches its highest values at maximum LAI (up to ∼ 6 mm day−1 ).

Inter-crop periods which follow winter crop cycles are characterized by a dry period in July–August. The low soil water content directly results from the crop water uptake during the previous crop cycle. The soil moisture reaches its upper level in fall which comprises 43 % of yearly rainfall. During inter-crop periods, the cumulative rate of ET is low. It is mostly influenced by soil evaporation. Daily ET generally keeps values lower than 1.5 mm day−1 . Larger values can be obtained after heavy rain events.

This experiment shows that simulated soil evaporation represents 64 % of cumulative ET over 12 years. It comprises more than 50 and 95 % of daily ET for 80 and 60 % of the days, respectively. While plant transpiration may generate significant daily ET during crop growing periods, it concerns only short time periods compared to soil evaporation.

**Table 5.** Performances of the simulated energy fluxes for the standard simulation PTF. RN is the net radiation. H, LE and G are the sensible, latent and ground heat fluxes. The metrics were computed over the valid measurements available for each variable. For LE, only the 2004– 2012 period is used. N and r are the number of samples and the correlation coefficient, respectively.

| RN (W m−2<br>) |      |      |      | H (W m−2<br>) |      |      | LE (W m−2<br>) |        |      |      | G (W m−2<br>) |         |      |      |      |
|----------------|------|------|------|---------------|------|------|----------------|--------|------|------|---------------|---------|------|------|------|
| N              | r    | RMSE | BIAS | N             | r    | RMSE | BIAS           | N      | r    | RMSE | Bias          | N       | r    | RMSE | BIAS |
| 197 255        | 0.99 | 27.7 | 0.2  | 103 886       | 0.85 | 56.2 | 17.6           | 96 214 | 0.80 | 52.4 | −11.8         | 191 619 | 0.88 | 46.9 | −1.3 |

![](_page_9_Figure_4.jpeg)

**Figure 4.** Sensitivity analysis: impact of variations in soil moisture at saturation (θs), soil moisture at field capacity (θfc) and soil moisture at wilting point (θwp) on simulated **(a)** evapotranspiration (ET) and **(b)** soil evaporation (E) and plant transpiration (T ), cumulated over the 12-year period. We display the difference in cumulative flux between the simulation PTF and the simulation PTF with modified soil parameters. FIELD means that the in situ values of the soil parameters (0.390, 0.310, 0.184 for θs, θfc, θwp, respectively) are tested one by one.

# **5.2 Evaluation of the standard simulation (PTF) over the 12-year crop succession**

#### **5.2.1 Evaluation of energy fluxes**

Table 5 shows the overall performances of simulated energy fluxes. RN is properly simulated (r = 0.99) with a low RMSE of 28 W m−2 . The latter probably falls within the range of the expected measurement errors. H and LE show substantial RMSE (56 W m−2 for H and 52 W m−2 for LE). LE has a negative bias of −12 W m−2 . H shows a larger positive bias of 18 W m−2 . G is markedly overestimated during daytime (daytime bias of 28 W m−2 ).

#### **5.2.2 Evaluation of simulated evapotranspiration**

Figure 3 shows large underestimation in ET simulated using the ISBA standard vegetation and soil parameters. The deficit in cumulative ET computed over 65 % of the 12-year period amounts to 1490 mm (24 % of the measured cumulative ET). The overall bias in daily ET is −0.24 mm day−1 . This results in an overestimation of the root-zone soil water content which has an overall positive bias of 0.024 m3 m−3 .

Table 6 provides the performance scores for crop and intercrop periods. The bias and RMSE are lower for inter-crop periods due to a lower flux magnitude. The correlations for daily ET are 0.8 and 0.6 for crop and inter-crop periods, respectively.

For crop cycles, ET and θroot-zone are generally properly simulated during the early growing period. ET underestimation occurs during the water stress periods at the end of the crop cycles. The simulated ET shows an early decrease compared to the measured ET. The resulting θroot-zone is overestimated at the end of most crop cycles.

For inter-crop periods, ET is mainly underestimated over wet bare soils. Over dry soils, the magnitude of soil evaporation is low and falls within the range of measurement errors. The overestimation of θroot-zone at the end of most crop cycles can propagate through the subsequent inter-crop period

![](_page_10_Figure_1.jpeg)

**Figure 5.** Evolution of **(a)** measured and simulated evapotranspiration (ET) and **(b)** measured and simulated root-zone soil moisture (θroot-zone) over the wheat cycle in 2006. In **(a)**, the simulated transpirations (T ) are represented by dashed lines and ET by solid lines. The LAI cycle is represented by green dash-dot lines. In **(b)**, Meas (1.50 m) is the measured soil moisture integrated between 0 and 1.50 m and is used to evaluate the PTF and FIELDcst θroot-zone which were simulated with Zroot_zone = 1.5 m. Meas (1.85 m) is the measured soil moisture integrated between 0 and 1.85 m and is used to evaluate FIELDvar θroot-zone which was simulated with Zroot_zone = 1.85 m for wheat crops in 2006.

as illustrated in 2004 and 2006 in Fig. 3. The induced bias in θroot-zone persists during the dry period and is generally removed at the rainy period.

#### **5.3 Impact of the soil parameters on ET simulations**

#### **5.3.1 Sensitivity analysis**

Figure 4 shows the impacts of variations in θs , θfc and θwp on cumulative ET, cumulative soil evaporation and cumulative transpiration over the 12-year simulation period.

θfc has the greatest impact on total ET, followed by θwp and θs . ET increases with increasing values of θfc while it decreases with increasing values of θwp and θs . Soil evaporation increases with increasing values of θfc and decreasing values of θs . θfc has a larger impact on soil evaporation than θs . Transpiration increases with increasing values of θfc and decreasing values of θwp. The impact of θfc on soil evaporation is larger than on transpiration. The impact of using in situ field values of the soil parameters instead of the pedotransfer estimates is largest for θs , followed by θfc and θwp.

#### **5.3.2 Impact of the estimation method**

We compare the PTF, LAB and FIELDcst simulations cases.

Figure 5 shows the underestimation of ET and the concomitant overestimation of θroot-zone at the end of the crop cycle for PTF achieved with the pedotransfer estimate of θwp. The use of the lower in situ θwp in FIELDcst leads to higher cumulative ET and greater depletion in θroot-zone which are both in better agreement with measurements. No effects are observed for irrigated crops (e.g. maize in Fig. 6).

Figure 7 shows the underestimation of soil evaporation over wet bare soil for PTF achieved with the pedotransfer estimate of θs . For FIELDcst, which was achieved with a lower in situ θs , the soil evaporation is increased and the decrease in θroot-zone is steeper than for PTF (days 255–295 in Fig. 7). This in better agreement with the measurements. The improvement of the simulated soil evaporation is also illustrated at the start of the maize crop cycle in Fig. 6.

The low θfc value estimated from the laboratory retention curve at K = 0.1 mm day−1 and used in LAB leads to the underestimation of simulated ET (Fig. 7a, Table 6). MaxAWC is underestimated (Table 4). The use of θfc estimated from the soil moisture measurements in FIELDcst leads to better agreement between simulated and measured soil evaporation (Fig. 7a and Table 6) .

#### **5.3.3 Impact of time-variable rooting depth and wilting point**

We compare FIELDcst based on a constant in time values of Zroot-zone and θwp with FIELDvar which uses time-variable values of these parameters. FIELDcst and FIELDvar show similar cumulative ET over 12 years and close simulation performances (Table 6). The use of Zroot-zone estimated for each crop cycle can locally improve the simulation of ET. This is observed for the dry wheat cycle in 2006 (Fig. 5a) for which the actual rooting depth (1.85 m) is much greater

![](_page_11_Figure_1.jpeg)

**Figure 6.** Evolution of **(a)** measured and simulated evapotranspiration (ET) and **(b)** measured and simulated root-zone soil moisture (θroot-zone) over the irrigated maize in 2001. In **(a)** the simulated transpirations (T ) are represented by dashed lines and ET by solid lines. The LAI cycle is represented by green dash-dot lines.

![](_page_11_Figure_3.jpeg)

**Figure 7.** Evolution of **(a)** measured and simulated evapotranspiration (ET) and **(b)** measured and simulated root-zone soil moisture (θroot-zone) over the inter-crop period in 2010. ET corresponds to the soil evaporation since the soil is bare.

than the 1.5 m mean value used in FIELDcst. The use of θwp estimated for each crop cycle has little impact.

#### **5.3.4 Selection of the best simulation over the crop succession**

The FIELD cases achieved with the soil parameters derived from the field soil moisture measurements show substantial reductions in biases in LE, daily ET and θroot-zone compared to PTF (Table 6). FIELDcst achieved with the average values of the soil parameters shows the lowest biases in ET. The deficit in cumulative ET over 12 years which amounts to 24 % for PTF is reduced to 6.7 % for FIELDcst. It is 22 % for PTF and 0.45 % for FIELDcst if only direct measurements of LE are used over the 2004–2012 period. Figure 8 shows that FIELDcst properly reproduces the time evolution of measurements over the crop succession.

The RMSE for LE and daily ET are not reduced in FIELDcst compared to PTF. They mostly represent random differences between measurements and simulations. For

**Table 6.** Performances of simulated latent heat flux (LE), daily daytime evapotranspiration (ETd) and root-zone soil moisture (θroot-zone) computed over the 20 November 2003–18 December 2012 period for which direct measurements of LE were available. ETd was computed when 90 % of daytime measurements were valid for each day. PTF, LAB, FIELDcst and FIELDvar are the simulation cases defined in Table 4. N is the number of samples used to evaluate each variable. Meas is the mean value of the measured variable.

|                                    | Crop cycle                   |                               |                              |                                |                                  |                                   | Inter-crop                   |                              |                              |                                |                                  |                                   |
|------------------------------------|------------------------------|-------------------------------|------------------------------|--------------------------------|----------------------------------|-----------------------------------|------------------------------|------------------------------|------------------------------|--------------------------------|----------------------------------|-----------------------------------|
|                                    | LE (W m−2<br>)               |                               | ETd                          | (mm day−1<br>)                 | θroot-zone (m3 m−3<br>)          |                                   | LE (W m−2<br>)               |                              | (mm day−1<br>ETd<br>)        |                                | θroot-zone (m3 m−3<br>)          |                                   |
| N<br>Meas                          | 52 260<br>70.1               |                               | 944<br>1.64                  |                                | 179<br>0.255                     |                                   | 43 954<br>35.6               |                              | 853<br>0.85                  |                                | 135<br>0.247                     |                                   |
|                                    | RMSE                         | BIAS                          | RMSE                         | BIAS                           | RMSE                             | BIAS                              | RMSE                         | BIAS                         | RMSE                         | BIAS                           | RMSE                             | BIAS                              |
| PTF<br>LAB<br>FIELDcst<br>FIELDvar | 61.6<br>60.7<br>61.8<br>61.3 | −14.3<br>−11.8<br>−0.3<br>1.0 | 1.07<br>1.03<br>1.00<br>1.00 | −0.30<br>−0.24<br>0.07<br>0.10 | 0.034<br>0.030<br>0.024<br>0.022 | 0.022<br>−0.015<br>0.012<br>0.012 | 38.6<br>37.7<br>40.7<br>38.8 | −8.9<br>−7.6<br>−0.2<br>−1.2 | 0.58<br>0.55<br>0.60<br>0.55 | −0.17<br>−0.14<br>0.06<br>0.04 | 0.033<br>0.024<br>0.026<br>0.029 | 0.026<br>−0.011<br>0.017<br>0.021 |

FIELDcst, the standard deviation of these random differences amounts to 53 W m−2 .

#### **5.3.5 Impact of uncertainties of in situ soil parameters and comparison with the mesophyll conductance**

We represent the uncertainties in simulated ET using cumulative values over the 2004–2012 period for which direct ET measurements are available. We display the simulation FIELDcst, the ensemble of the Monte Carlo simulations and the 95th percentile interval of simulated ET. The percentiles are computed over the empirical distribution of cumulative ET values. Figure 8 shows the following.

- **–** The spatiotemporal variability of the soil parameters can generate large uncertainties in ET. The 95th percentile interval represents 867 mm (23 %) of cumulative ET over 12 years.
- **–** The uncertainties in the mesophyll conductance have a lower impact. The 95th percentile interval represents 70 mm (2 %) of cumulative ET over 12 years.

# **6 Discussion**

We tested three types of soil parameter estimates derived from

- **–** the ISBA pedotransfer functions,
- **–** the retention curve model adjusted over laboratory measurements,
- **–** the analysis of field measurements of soil moisture vertical profiles.

First, we explain the role of the investigated soil parameters in the simulation of soil evaporation and plant transpiration to understand how they influence the simulation of ET over the crop succession. Then, we discuss the sources of uncertainties related to each soil parameter retrieval method. Finally, we put into perspective the simulation performances obtained in this work by discussing the uncertainties in measured ET.

#### **6.1 Impact of the soil parameters on simulated ET over the crop succession**

#### **6.1.1 Impact on soil evaporation**

Soil evaporation decreases with increasing values of soil moisture at saturation (θs). This is related to the modelled superficial hydraulic diffusivity which decreases with increasing value of θs (see Eq. (B4) in Appendix B). This depletes the superficial soil moisture and the resulting soil evaporation is reduced (Eq. (B4) in Appendix B).

Soil evaporation increases with increasing field capacity (θfc) values. θfc increases the upper level of θroot-zone during the wet bare soil period, leading to increased capillary rise supply of the superficial soil moisture and enhanced soil evaporation (Eq. (B5) in Appendix B).

### **6.1.2 Impact on transpiration**

The field capacity and the wilting point, (θwp) have similar effects on plant transpiration through their symmetrical role in the water stock available for the crop's growth (Max-AWC, Eq. 1). Transpiration increases with increasing value of MaxAWC. When MaxAWC is underestimated due to the overestimation of θwp (PTF simulation) or the underestimation of θfc (LAB simulation), early water stress is simulated which conducts to the underestimation of the simulated plant transpiration at the end of the crop cycle. This effect is not observed for irrigated crops (e.g. maize in Fig. 6). In these cases, the supply of water by irrigation is sufficient to satisfy crop water needs over the growing season. θwp is not reached and no water stress occurs.

![](_page_13_Figure_2.jpeg)

**Figure 8.** Propagation of the uncertainties in **(a)** the soil parameters (Zroot-zone, θs, θfc, θwp) and **(b)** the mesophyll conductance, on simulated ET. FIELDcst is the simulation achieved with the mean values of Zroot-zone, θs, θfc, θwp derived from the field measurements of soil moisture and the standard value of gm (Gibelin et al., 2006). The grey curves represent the 100 simulations generated by the Monte Carlo (MC) scheme. The 95th percentile interval (PI) of the MC simulations is computed over the empirical distributions of cumulative ET values.

#### **6.1.3 Hierarchy of the impact of the soil parameters**

The soil moisture at field capacity (θfc) is largely the most influencing soil parameter on the simulation of ET over the crop succession. This is due to its impact on both soil evaporation and transpiration. It is followed by the wilting point (θwp) and the soil moisture at saturation (θs) which have smaller effects.

The dynamics of crop rotation lead to long inter-crop periods between winter and summer crops. As a result, soil evaporation is the prevailing component of ET over the crop succession, which explains the high sensitivity of ET to uncertainties in θfc and θs despite the low magnitude of soil evaporation flux.

#### **6.2 Uncertainties in the soil parameters**

#### **6.2.1 Pedotransfer estimates**

Most of ET underestimation reported for the standard implementation of the model (PTF) is due to the overestimation of both the soil moisture at wilting point and the soil moisture at saturation by the ISBA pedotransfer functions (Table 4). The error in θs is the largest and has the strongest impact on ET. The use of in situ values of θs and θwp in FIELDcst substantially reduces the bias in ET (Fig. 8). The deficit in simulated ET for the PTF simulation triggers an increase of the simulated drainage that is probably overestimated. The increase in simulated ET from PTF to FIELDcst is 1375 mm over 12 years. The decrease in simulated drainage from PTF to FIELDcst is 1418 mm.

Large discrepancies have been reported between pedotransfer functions which are prone to distinct sources of uncertainties (Espino et al., 1996; Baroni et al., 2010; Gijsman et al., 2002). The first shortcoming concerns their representativeness of soil property variability. The ISBA pedotransfer functions were established upon the Clapp and Hornberger (1978) database. These functions were calibrated using mean values of soil properties over few classes of soil texture and do not represent the variability within each soil class. Moreover, maps of soil texture may not be accurate enough at a regional scale. The second source of uncertainty is related to the estimation method. Pedotransfer functions were designed to be applied over readily available variables such as soil texture. Improvements of the prediction equations may require the use of additional predictors related to soil structure (Vereecken et al., 1989). Most pedotransfer fucntions are based on simple statistical regressions such as the ISBA ones (Noilhan and Laccarère, 1994). The moreadvanced ROSETTA pedotransfer functions (Schaap et al., 2001) addresses the uncertainty in the predicted soil parameters through the use of an ensemble of functions calibrated over distinct soil data sets. Such model provides essential information on the variance and covariance of the hydraulic properties (Scharnagl et al., 2011) which are required to propagate the uncertainties in the LSM simulations.

#### **6.2.2 Laboratory estimates**

The θfc estimate at K = 0.1 mm day−1 used in LAB is too low and leads to the underestimation of of both soil evaporation and transpiration. This partly compensates for the increase in soil evaporation triggered by the use of in situ θs and explains that the resulting soil evaporation of LAB keeps values close to the PTF soil evaporation in Fig. 7a. The definition of θfc for K = 0.1 mm day−1 is not appropriate to represent crop water needs.

Various studies have questioned the use of hydraulic properties inferred from laboratory techniques to simulate water transfers at the field scale (Basile et al., 2003; Mertens et al., 2005; Scharnagl et al., 2011). Laboratory experiments may not be representative of field conditions. Gravimetric measurements can disturb the actual soil structure. Small soil samples cannot capture the spatial and vertical heterogeneity of the soil structure at the field scale which can be substantially influenced by macroporosity and soil operations (Mertens et al., 2005). Single measurements cannot resolve the changes in soil structure caused by crop development and tillage operations (Baroni et al., 2010).

#### **6.2.3 Field estimates**

The most accurate simulation is achieved with the average values of Zroot-zone, θfc and θwp derived from the analysis of soil moisture measurements over each crop cycle (FIELDcst). Field measurements of soil moisture better resolve the intrafield spatial variability through four neutron probes compared to the laboratory measurements. The analysis in time of the vertical profiles of soil moisture over the growing season provides meaningful estimates of the wilting point, the field capacity and the rooting depth for each crop cycle. Their mean values are accurate enough to represent the crop water needs and accurately simulate ET at the field scale over the 12-year crop succession. The variations in time of wilting point and rooting depth over the crop succession are low and their representation in the simulation has little impact on the overall model performances. The use of constant soil depths over the crop succession is preferable to ensure the conservation of mass in the force-restore simulation of the water balance over a long period of time. To account for time-variable rooting depth, an explicit soil multi-layer diffusion scheme would be required.

However, one can question the representativeness of field average in situ estimates of soil parameters which can be spatially and temporally variable. For example, the soil moisture at saturation is prone to large spatiotemporal variations due to macroporosity and impact of soil operations on the structure of the 0–0.4 m soil layer. We showed in Fig. 8 that the spatiotemporal variability in the soil parameters can generate large uncertainties in simulated ET over 12 years. These uncertainties are much larger than those generated by the mesophyll conductance. This is consistent with the findings of Calvet et al. (2012), who showed that ISBA-A-gs simulations are more sensitive to the root-zone reservoir (Max-AWC) than the mesophyll conductance. However, our results depend on the assumptions made on the distributions of the tested parameters. The selected ranges of variations in the soil parameters are representative of the spatial variations in soil depth and soil structure according to our knowledge of the site. However, the spatial variability of these parameters should be properly quantified using adequate spatial sampling protocols and geostatistic methods (Garrigues et al., 2006). Besides, the variations in the soil hydrodynamic parameters may be larger when the model is integrated at a regional scale (Braud et al., 1995). Finally, other vegetation parameters (e.g. water stress parameters, Verhoef and Egea., 2014) may be sources of uncertainties and should be investigated in further works.

#### **6.3 Uncertainties in eddy covariance measurements**

Random errors in eddy covariance measurements arise from turbulence sampling errors, instrument errors and flux footprint uncertainties (Richardson et al., 2006). We applied the Richardson et al. (2006) method (explained in Appendix C) to compute the standard deviation of the measurement random error for various classes of LE values. Results are given in Table C1. Random errors are very likely to cancel out when measurements are cumulated over a long period of time. However, they can explain a large part of the unresolved random differences between the simulations and the measurements at half-hourly and daily timescales.

Eddy covariance is also prone to systematic errors. Particularly, the eddy-covariance system could fail to resolve low frequency turbulence structures that could lead to the underestimation of eddy fluxes (Foken, 2008). This results in the non-closure of the measured energy balance (EB) which is a critical source of uncertainties when these measurements are compared to LSM simulations. Other reasons for the EB non-closure include horizontal and vertical advection, inaccuracies in the eddy covariance processing and footprint mismatch between the eddy fluxes and the other energy fluxes (RN, G) (Foken, 2008; Leuning et al., 2012). The application of an energy imbalance threshold of 100 W m−2 minimized the magnitude of the EB non-closure of our data set. The mean and the standard deviation of the absolute value of the EB non-closure are 28 and 22 W m−2 , respectively. This is comparable to the non-closure reported for cropland in Wilson et al. (2002), Hendricks et al. (2010) and Ingwersen et al. (2011).

The uncertainties in eddy-covariance measurements are further assessed comparing the direct measurement of LE with two other estimates. The first estimate is computed as the residue of the energy balance assuming that H is errorfree. The second estimate is derived from the Bowen ratio (ratio between H and LE) assuming that the Bowen ratio is correctly estimated (Twine et al., 2000). The SD of the differences in LE between the direct measurement and the other estimates fall between 24 and 36 W m−2 (Table 7). The MD (mean difference) at a half-hourly timescale falls between 3 and 7 W m−2 . The MD in cumulative ET over 12 years between the Bowen ratio estimate and the direct measurement represents 727 mm (12 %). It is 310 mm (5 %) between the estimate derived from the residue of the energy balance and the direct measurement. The deficits in simulated ET reported in this work are thus probably larger due to likely underestimation of ET by eddy-covariance measurements.

**Table 7.** Comparison of the direct measurement of LE (direct), the energy balance residue estimate of LE (residue) and the Bowen ratio estimate of LE (Bowen). RMSD is the root mean square of the differences between the LE estimates. SDD is the SD of the differences between the LE estimates. For Y versus X, MD is computed as Y − X. In the last row, the MD in cumulative ET over 12 years is computed relatively to X.

| Residue<br>Bowen |
|------------------|
| versus           |
| residue          |
| 29.3             |
| 28.9             |
| 4.3              |
| 417              |
| 6.5              |
|                  |

#### **7 Summary**

In this study, the SURFEX/ISBA-A-gs simulations of evapotranspiration (ET) are assessed at the field scale over a 12 year Mediterranean crop succession. The model is evaluated in its standard implementation which relies on the use of the ISBA pedotransfer function estimates of the soil properties. The analysis focuses on key parameters which drive the simulation of ET, namely the rooting depth, the soil moisture at saturation, the soil moisture at field capacity and the soil moisture at wilting point. A sensitivity analysis is first conducted to quantify the relative contribution of each parameter on ET simulated over the crop succession. The impact of the estimation method used to retrieve the soil parameters (pedotransfer function, laboratory and field methods) on ET is then analysed. The benefit of representing the variations in time of the rooting depth and the wilting point is evaluated. Finally, the propagation of uncertainties in the soil parameters on ET simulations is quantified through a Monte Carlo analysis and compared with the uncertainties triggered by the mesophyll conductance which is a key above-ground driver of the stomatal conductance.

Evapotranspiration mainly results from the soil evaporation when it is simulated over a succession of crop cycles and inter-crop periods for Mediterranean croplands. The crop transpiration generates high ET over short time periods while the soil evaporation represents more than 50 % of ET for 80 % of the days. This results in a high sensitivity of simulated evapotranspiration to uncertainties in the soil moisture at field capacity and the soil moisture at saturation, both of which drive the simulation of soil evaporation. Field capacity was proved to be the most influencing parameter on the simulation of evapotranspiration over the crop succession due to its impact on both transpiration and soil evaporation.

ET simulated with the standard surface and soil parameters of the model is largely underestimated. The deficit in cumulative ET amounts to 24 % over 12 years. The biases in daily daytime ET and root-zone soil moisture are −0.24 mm day−1 and 0.024 m3 m−3 . ET underestimation is mainly related to the overestimation of the soil moisture at saturation and the soil moisture at wilting point by the ISBA pedotransfer functions. The overestimation of the wilting point triggers the underestimation of the water stock available for the crop's growth which conducts to the underestimation of the simulated plant transpiration at the end of the crop cycle. The overestimation of the soil moisture at saturation triggers an underestimation of the water diffusivity in the superficial layer which reduces the soil evaporation during wet periods.

The field capacity estimate derived from laboratory measurements at K = 0.1 mm day−1 is too low and leads to the underestimation of evapotranspiration. This is related to the lack of representativeness of the soil structure variability by the laboratory samples and inappropriate definition of the field capacity at K = 0.1 mm day−1 to represent crop water needs.

The most accurate simulation is achieved with the average values of the soil parameters derived from the temporal analysis of field measurements of soil moisture vertical profiles over each crop cycle. The representation of the variations in time of the wilting point and the maximum rooting depth over the crop succession has little impact on the ET simulation performances.

The uncertainties in the soil parameters, related to the use of field average estimates, generate substantial uncertainties in simulated ET (the 95 % confidence interval represents 23 % of cumulative ET over 12 years) which are much larger than the uncertainties triggered by the mesophyll conductance.

The measurement random errors tend to cancel out when measurements are cumulated over a long period of time. They explain a large part of the unresolved scattering between simulations and measurements at half-hourly timescales. The deficits in simulated ET reported in this work are probably larger due to likely underestimation of ET by eddy-covariance measurements.

Other model shortcomings could concern the lack of root profile representation in the force-restore water transfer scheme which can affect the representation of the effect of water stress on plant transpiration (Desborough, 1997; Braud et al., 2005; Fan et al., 2006). A multi-layer diffusion scheme may represent the soil vertical heterogeneity and the interactions between plant and soil more accurately (Decharme et al., 2011). However, the performances of such detailed models rely on accurate parametrization of root profile and soil vertical heterogeneity which may not be available at a large scale and could trigger larger uncertainties in ET than the parameters of the force–restore model (Olioso et al., 2002). Other sources of uncertainties in the model structure include inaccurate ET partitioning between the soil and the vegetation at low LAI which may require a double-source energy balance (Olioso et al., 2002), inaccurate representation

| Table 8. Mean and SD of the parameters used in the Monte Carlo analysis. gm | C3 and gm<br>C4 denote the mesophyll conductance for C3 and |
|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| C4 crops. The mean values are those used in the simulation FIELDcst.        |                                                             |

|      | Zroot-zone<br>(m) | θs<br>(m3 m−3<br>) | θfc<br>(m3 m−3<br>) | θwp<br>(m3 m−3<br>) | gm<br>C3<br>m s−1 | gm<br>C4<br>m s−1 |
|------|-------------------|--------------------|---------------------|---------------------|-------------------|-------------------|
| Mean | 1.5               | 0.390              | 0.310               | 0.184               | 0.001             | 0.009             |
| SD   | 0.3               | 0.019              | 0.012               | 0.025               | 0.0007            | 0.007             |

of the resistance of a drying soil to water vapour diffusion which depends on both soil structure and texture (Kondo et al., 1990; Merlin et al., 2011) and shortcomings in the parametrization of water stress functions (Verhoef and Egea, 2014).

Finally, this work highlights the prevailing role of the soil parameters in the simulation of ET dynamics over a multiyear crop succession. Accounting for uncertainties in soil properties is of paramount importance for the spatial integration of land surface models. Methods need to be developed to spatially retrieve the soil parameters and their uncertainties at regional scale. We showed that pedotransfer functions can be inaccurate. Field measurements of soil moisture are generally not available at a regional scale. Satellite observations of soil moisture and vegetation status offer great promise to retrieve the soil properties over large areas. Bayesian inverse modelling is an appropriate approach to calibrate the soil parameters and translate their uncertainties into uncertainties in the simulated fluxes (Mertens et al., 2004; Vrugt et al., 2009; Scharnagl et al., 2011). All sources of modelling (forcing data, vegetation and soil parameters, model structure) and measurement uncertainties can be adequately incorporated into the analysis. Our results will serve as a basis to implement such a method in order to monitor ET and its uncertainties over cropland.

#### **Appendix A: Definition of the main symbols**

**Table A1.** Definition of the main symbols.

| BIAS       | Mean difference between simulated and measured values                             |  |  |  |  |  |  |
|------------|-----------------------------------------------------------------------------------|--|--|--|--|--|--|
| E          | Soil evaporation (mm)                                                             |  |  |  |  |  |  |
| EB         | Energy balance                                                                    |  |  |  |  |  |  |
| ET:        | Cumulative evapotranspiration (mm)                                                |  |  |  |  |  |  |
| ETd        | Daily daytime evapotranspiration (mm day−1<br>)                                   |  |  |  |  |  |  |
| FIELD      | Simulation case achieved with θfc<br>and θwp<br>retrieved from the                |  |  |  |  |  |  |
|            | temporal analysis of field soil moisture measurements                             |  |  |  |  |  |  |
| G          | Ground heat flux (W m−2<br>)                                                      |  |  |  |  |  |  |
| h          | Matric potential (m)                                                              |  |  |  |  |  |  |
| H          | Sensible heat flux (W m−2<br>)                                                    |  |  |  |  |  |  |
| K          | Hydraulic conductivity (m s−1<br>)                                                |  |  |  |  |  |  |
| LAB        | Simulation case achieved with θfc<br>and θwp<br>retrieved from laboratory methods |  |  |  |  |  |  |
| LE         | Latent heat flux (W m−2<br>)                                                      |  |  |  |  |  |  |
| MaxAWC     | Maximum root-zone water stock available for the crop (mm)                         |  |  |  |  |  |  |
| MD         | Mean difference                                                                   |  |  |  |  |  |  |
| Meas       | Measurement                                                                       |  |  |  |  |  |  |
| PTF        | Simulation case achieved with θs, θfc, and θwp<br>retrieved from                  |  |  |  |  |  |  |
|            | the ISBA pedotransfer function                                                    |  |  |  |  |  |  |
| RMSE       | Root mean square error between simulated and measured values                      |  |  |  |  |  |  |
| RMSD       | Root mean square difference between two types of measurement                      |  |  |  |  |  |  |
| RN         | Net radiation (W m−2<br>)                                                         |  |  |  |  |  |  |
| Sim        | Simulation                                                                        |  |  |  |  |  |  |
| SDD        | Between two simulations or two types of measurement                               |  |  |  |  |  |  |
| T          | Transpiration flux (mm)                                                           |  |  |  |  |  |  |
| Zroot-zone | Rooting depth (m)                                                                 |  |  |  |  |  |  |
| θfc        | Volumetric soil moisture at field capacity (m3 m−3<br>)                           |  |  |  |  |  |  |
| θroot-zone | d2) (m3 m−3<br>Root-zone volumetric soil moisture (0 −<br>)                       |  |  |  |  |  |  |
| θsat       | Volumetric soil moisture at saturation (m3 m−3<br>)                               |  |  |  |  |  |  |
| θsurf      | Superficial volumetric soil moisture (0–0.01 m) (m3 m−3<br>)                      |  |  |  |  |  |  |
| θwp        | Volumetric soil moisture at wilting point (m3 m−3<br>)                            |  |  |  |  |  |  |

#### **Appendix B: The soil evaporation in the force-restore scheme**

The ISBA soil evaporation (E) is given by

$$E = (\mathbf{l} - \mathbf{v}\mathbf{e}\mathbf{g})\rho_\mathbf{a}C_HV\left[h_uq_{\rm sat} - q_\mathbf{a}\right],\tag{\rm B1}$$

where "veg" is the fraction of vegetation cover, ρa is the dry air density, CH is the drag coefficient, V is the wind speed, qsat is the surface specific humidity at saturation, and qa is the air specific humidity at the reference height. hu is the air relative humidity at the surface and is computed as

$$h_{\rm th} = 0.5 \left[ 1 - \cos \left( \min \left( \frac{\theta_{\rm surf}}{\theta_{\rm fc}}, 1 \right) \pi \right) \right], \tag{B2}$$

where θsurf is the superficial soil moisture and θfc is the soil moisture at field capacity. E is at its potential rate when θsurf > θfc (hu = 1). It depletes as θsurf drops below θfc. For hu qsat < qa, if qsat < qa a dew flux is triggered and if qsat > qa the soil evaporation is set to zero.

The time course of θsurf is given by the force-restore equation:

$$\frac{\partial \theta_{\rm surf}}{\partial t} = \frac{C_1}{\rho_{\rm w} d_{\rm l}} (P - E) - \frac{C_2}{\pi} \left(\theta_{\rm surf} - \theta_{\rm cq}\right) \,. \tag{B3}$$

In Eq. (B3), ρw is the liquid water density, P is the flux of water reaching the surface, and τ is the restore constant of 1 day.

The coefficient C1 is driving the moisture exchange between the surface and the atmosphere. It is an inverse function of the hydraulic diffusivity (Noilhan and Planton, 1989; Eq. B.4).

$$C_{\rm l} = C_{\rm l,s} d_{\rm surf} \left( \frac{\theta_{\rm s}}{\theta_{\rm surf}} \right)^{0.5b+1} \tag{B4}$$

In Eq. (B4), C1,s is the value of C1 at saturation (in m−1 ) calibrated as a function of clay fraction and b is the slope of the Brooks and Corey (1966) retention curve. C1 is minimum at saturation and increases as the soil surface dries out. It reaches its maximum for θsurf = θwp. For θsurf lower than θwp, water vapour phase transfers are prevailing. C1 is represented by a Gaussian formulation (Giordani et al., 1996; Giard and Bazile, 2000) and decreases with increasing soil temperature and decreasing soil moisture.

The second term in the right-hand side of Eq. (B3) represents the vertical water diffusion between the root zone and the superficial layer. It is ruled by the diffusion coefficient C2 (Eq. B5) which quantifies the rate at which the soil moisture profile between layers 1 and 2 is restored to the equilibrium θeq (water content at the balance between the gravity and the capillary forces).

$$C_2 = C_{2\text{ref}} \left( \frac{\theta_{\text{root-zone}}}{\theta_\text{s} - \theta_{\text{root-zone}} + \theta_l} \right) \tag{B5}$$

**Table C1.** Standard deviation (σδ ) of the random error of the LE measurements computed for distinct classes of LE values. N is the number of measurement pairs used to estimate the random error.

|    | Ranges of LE flux (W m−2<br>) |         |           |            |       |  |  |  |  |
|----|-------------------------------|---------|-----------|------------|-------|--|--|--|--|
|    | < 0                           | [0, 50] | [50, 100] | [100, 200] | > 200 |  |  |  |  |
| N  | 627                           | 2592    | 615       | 233        | 117   |  |  |  |  |
| σδ | 4.8                           | 7.8     | 14.9      | 23.4       | 53.4  |  |  |  |  |

In Eq. (B5), θroot-zone is the root-zone soil moisture, θl is a numerical constant. C2ref is the mean value of C2 for θ2 = 0.5 θs and is computed as a function of clay fraction. C2 is an increasing function of θroot-zone.

In ISBA, the force-restore water transfer scheme and the resulting soil evaporation strongly depend on soil texture (Jacquemin and Noilhan, 1990). Coarse soil textures are characterized by high soil hydraulic diffusivity and conductivity which are represented in the model by low C1 and high C2, respectively. For sandy soil, a low value of C1 reduces the depletion of θsurf due to soil evaporation and high C2 enhances the supply of θsurf by capillary rises. The resulting daily variations of θsurf are low and the values of θsurf are frequently higher than θfc. The resulting soil evaporation is frequently at its potential rate. Conversely, clay soils have higher C1 and lower C2. This leads to more rapid depletion of θsurf which keeps lower values compared to sandy soil. The subsequent soil evaporation drops since it is more rapidly limited by the soil water supply.

#### **Appendix C: Characterization of the random errors in the eddy covariance measurements**

The Richardson et al. (2006) method to assess the random errors in eddy-covariance measurements consists in selecting 24 h apart pairs of measurements acquired under equivalent environmental conditions. The latter are defined by differences in vapour pressure deficit within 0.15 kPa, wind speed within 1 m s−1 , air temperature within 3 ◦C and photosynthetic photon flux within 75 µmol m−2 s −1 . Compared to the original method, additional criteria were implemented: wind direction within ±15◦ , footprint within 30 %, surface soil moisture within 0.03 m3 m−3 , and incoming solar radiation within 50 W m−2 . The measurement pairs (x1 and x2) are assumed to be two measurements of the same flux F at two distinct times.

$$\hat{\mathbf{x}}_{\text{l}} = \hat{F} + \hat{\boldsymbol{\delta}}_{\text{l}} \tag{\text{Cl}}$$

$$
\lambda \mathbf{x}_2 = F + \delta_2 \tag{C2}
$$

δ represents the random error which is assumed to be uncorrelated in time and identically distributed in time. Richardson et al. (2006) showed that the standard deviation of the random error (σδ) is

$$
\sigma_{\delta} = \sigma \left(\chi_1 - \chi_2\right) / \sqrt{2},\tag{C3}
$$

where σ (x1 − x2) is the standard deviation of the differences between the values of the measurement pairs. In our experiment, we assume that x1 − x2 follows a Gaussian distribution. Table C1 provides σδ computed for distinct classes of LE values.

# **S. Garrigues et al.: Evaluation of land surface model simulations of evapotranspiration 3129**

Edited by: J. Vrugt

#### **References**

- Arora, V. K.: Modeling vegetation as a dynamic component in soil- vegetation-atmosphere transfer schemes and hydrological models, Rev. Geophys., 40, 1006, doi[:10.1029/2001RG000103,](http://dx.doi.org/10.1029/2001RG000103) 2002.
- Basile, A., Ciollaro, G., and Coppola, A.: Hysteresis in soil water characteristics as a key to interpreting comparisons of laboratory and field measured hydraulic properties, Water Resour. Res., 39, 1355, doi[:10.1029/2003WR002432,](http://dx.doi.org/10.1029/2003WR002432) 2003.
- Baroni, G., Facchi, A., Gandolfi, C., Ortuani, B., Horeschi, D., and van Dam, J. C.: Uncertainty in the determination of soil hydraulic parameters and its influence on the performance of two hydrological models of different complexity, Hydrol. Earth Syst. Sci., 14, 251–270, doi[:10.5194/hess-14-251-2010,](http://dx.doi.org/10.5194/hess-14-251-2010) 2010.
- Beziat, P., Ceschia, E., and Dedieu, G.: Carbon balance of a three crop succession over two cropland sites in South West France, Agr. Forest Meteorol., 149, 1628–1645, 2009.
- Bhumralkar, C. M.: Numerical experiments on the computation of ground surface temperature in an atmospheric general circulation model, J. Appl. Meteorol., 14, 1246–1258, 1975.
- Blackadar, A. K.: Modeling the nocturnal boundary layer, Preprints, Third Symp. on Atmospheric Turbulence, Diffusion and Air Quality, Raleigh, NC, 46–49, 1976.
- Bonan, G. B.: Land surface processes in climate models, in: Ecological Climatology, edited by: Bonan, G., Cambridge University Press, Cambridge, 2010.
- Bonan, G. B. and Santanello, J. A.: Modelling the land-atmosphere interface across scales: from atmospheric science to Earth system science, ILEAPS Newslett., 13, 6–8, 2013.
- Boone, A., Calvet, J.-C., and Noilhan, J.: Inclusion of a Third Soil Layer in a Land Surface Scheme Using the Force–Restore Method, J. Appl. Meteorol., 38, 1611–1630, 1999.
- Boone, A., Habets, F., Noilhan, J., Clark, D., Dirmeyer, P., Fox, S., Gusev, Y., Haddeland, I., Koster, R., Lohmann, D., Mahanama, S., Mitchell, K., Nasonova, O., Niu, G.-Y., Pitman, A., Polcher, J., Shmakin, A. B., Tanaka, K., van den Hurk, B., Verant, S., Verseghy, D., Viterbo, P., and Yang, Z.-L.: The Rhone-Aggregation Land Surface Scheme Intercomparison Project: an overview, J. Climate, 17, 187–208, 2004.
- Braud, I., Dantas-Antonio, A. C., and Vauclin, M.: A stochastic approach to studying the influence of the spatial variability of soil hydraulic properties on surface fluxes, temperature and humidity, J. Hydrol., 165, 283–310, 1995a.
- Braud, I., Dantas-Antonino, A. C., Vauclin, M., Thony, J,-L., and Ruelle, P.: A simple soil-plant atmosphere transfer model (SiS-PAT) development and field verification, J. Hydrol., 166, 213– 250, 1995b.
- Braud, I., Varado, N., and Olioso, A.: Comparison of root water uptake modules using either the surface energy balance or potential transpiration, J. Hydrol., 301, 267–286, 2005.
- Brooks, R. H. and Corey, A. T.: Properties of porous media affecting fluid flow, J. Irrig. Drain. Am. Soc. Civil Eng., 2, 61–88, 1966.
- Bruckler, L., Lafolie, F., Doussan, C., and Bussières, F.: Modeling soil-root water transport with non-uniform water supply and heterogeneous root distribution, Plant Soil, 260, 205–224, 2004.
- Calvet, J.-C.: Investigating soil and atmospheric plant water stress using physiological and micrometeorological data, Agr. Forest Meteorol., 103, 229–247, 2000.
- Calvet, J.-C., Noilhan, J., Roujean, J.-L., Bessemoulin, P., Cabelguenne, M., Olioso, A., and Wigneron, J.-P.: An interactive vegetation SVAT model tested against data from six contrasting sites, Agr. Forest Meteorol., 92, 73–95, 1998.
- Calvet, J.-C., Rivalland, V., Picon-Cochard, C., and Guehl, J.-M.: Modelling forest transpiration and CO2 fluxes – Response to soil moisture stress, Agr. Forest Meteorol., 124, 143–156, 2004.
- Calvet, J.-C., Gibelin, A.-L., Roujean, J.-L., Martin, E., Le Moigne, P., Douville, H., and Noilhan, J.: Past and future scenarios of the effect of carbon dioxide on plant growth and transpiration for three vegetation types of southwestern France, Atmos. Chem. Phys., 8, 397–406, doi[:10.5194/acp-8-397-2008,](http://dx.doi.org/10.5194/acp-8-397-2008) 2008.
- Calvet, J.-C., Lafont, S., Cloppet, E., Souverain, F., Badeau, V., and Le Bas, C.: Use of agricultural statistics to verify the interannual variability in land surface models: a case study over France with ISBA-A-gs, Geosci. Model Dev., 5, 37–54, doi[:10.5194/gmd-5-](http://dx.doi.org/10.5194/gmd-5-37-2012) [37-2012,](http://dx.doi.org/10.5194/gmd-5-37-2012) 2012.
- Chen, T. H., Henderson-Sellers, A., Milly, P. C. D., Pitman, A. J., Beljaars, A. C. M., Polcher, J., Abramopoulos, F., Boone, A., Chang, S., Chen, F., Dai, Y., Desborough, C. E., Dickinson, R. E., Dümenil, L., Ek, M., Garratt, J. R., Gedney, N., Gusev, Y. M., Kim, J., Koster, R., Kowalczyk, E. A., Laval, K., Lean, J., Lettenmaier, D., Liang, X., Mahfouf, J.-F., Mengelkamp, H.-T., Mitchell, K., Nasonova, O. N., Noilhan, J., Robock, A., Rosenzweig, C., Schaake, J., Schlosser, C. A., Schulz, J.-P., Shao, Y., Shmakin, A. B., Verseghy, D. L., Wetzel, P., Wood, E. F., Xue, Y., Yang, Z.-L., and Zeng, Q.: Cabauw experimental results from the project for intercomparison of land-surface parameterization schemes, J. Climate, 10, 1194–1215, doi[:10.1175/1520-](http://dx.doi.org/10.1175/1520-0442(1997)010<1194:CERFTP>2.0.CO;2) [0442(1997)010<1194:CERFTP>2.0.CO;2,](http://dx.doi.org/10.1175/1520-0442(1997)010<1194:CERFTP>2.0.CO;2) 1997.
- Clapp, R. and Hornberger, G.: Empirical equations for some soil hydraulic properties, Water Resour. Res., 14, 601–604, 1978.
- Cosby, B. J., Hornberger, G. M., Clapp, R. B., and Ginn, T. R.: A statistical exploration of the relationships of soil moisture characteristics to the physical properties of soils, Water Resour. Res., 20, 682–690, 1984.
- Cresswell, H. P. and Paydar, Z.: Functional evaluation of methods for predicting the soil water characteristic, J. Hydrol., 227, 160– 172, 2000.
- Deardorff, J. W.: A parameterization of ground surface moisture content for use in atmospheric prediction models, J. Appl. Meteorol., 16, 1182–1185, 1977.
- Decharme, B., Boone, A., Delire, C., and Noilhan, J.: Local evaluation of the Interaction between Soil Biosphere Atmosphere soil multilayer diffusion scheme using four pedotransfer functions, J. Geophys. Res., 116, D20126, doi[:10.1029/2011JD016002,](http://dx.doi.org/10.1029/2011JD016002) 2011.
- Desborough, C. E.: The Impact of Root Weighting on the Response of Transpiration to Moisture Stress in Land Surface Schemes, Mon. Weather Rev., 125, 1920–1930, 1997.
- Dolman, A. J. and De Jeu, R. A. M.: Evaporation in Focus, Nat. Geosci., 3, 296, doi[:10.1038/ngeo849,](http://dx.doi.org/10.1038/ngeo849) 2010.
- Duveiller, G., Weiss, M., Baret, F., and Defourny, P.: Retrieving wheat Green Area Index during the growing season from optical time series measurements based on neural network radiative transfer inversion, Remote Sens. Environ., 115, 887–896, 2011.
- Egea, G., Verhoef, A., and Vidale, P. L.: Towards an improved and more flexible representation of water stress in coupled photosynthesis-stomatal conductance models, Agr. Forest Meteorol., 151, 1370–1384, 2011.
- Espino, A., Mallants, D., Vanclooster, M., and Feyen, J.: Cautionarynotes on the use of pedotransfer functions for estimating soil hydraulic properties, Agric. Water Manage., 29, 235–253, 1996.
- Fan, Y., Van den Dool, H. M., Lohmann, D., and Mitchell, K.: 1948– 98 U.S. hydrological reanalysis by the NOAH land data assimilation system, J. Climate, 19, 1214–1237, 2006.
- Faroux, S., Kaptué Tchuenté, A. T., Roujean, J.-L., Masson, V., Martin, E., and Le Moigne, P.: ECOCLIMAP-II/Europe: a twofold database of ecosystems and surface parameters at 1 km resolution based on satellite information for use in land surface, meteorological and climate models, Geosci. Model Dev., 6, 563– 582, doi[:10.5194/gmd-6-563-2013,](http://dx.doi.org/10.5194/gmd-6-563-2013) 2013.
- Foken, T.: The energy balance closure problem: an overview, Ecol. Appl., 18, 1351–1367, 2008.
- Foken, T., Göcked, M., Mauder, M., Mahrt, L., Amiro, B., and Munger, W.: Post-field data quality control, in: Handbook of Micrometeorology, edited by: Lee, X., Massman, W., and Law, B., Kluwer Academic Publishers, Dordrecht, the Netherlands, 181– 208, 2004.
- Garrigues, S., Allard, D., Baret, F., and Weiss, M.: Influence of landscape spatial heterogeneity on the non linear estimation of leaf area index from moderate spatial resolution remote sensing data, Remote Sens. Environ., 105, 286–298, doi[:10.1016/j.rse.2006.07.013,](http://dx.doi.org/10.1016/j.rse.2006.07.013) 2006.
- Giard, D. and Bazile, E.: Implementation of a New Assimilation Scheme for Soil and Surface Variables in a Global NWP Model, Mon. Weather Rev., 128, 997–1015, 2000.
- Gibelin, A.-L., Calvet, J.-C., Roujean, J.-L., Jarlan, L., and Los, S. O.: Ability of the land surface model ISBA-A-gs to simulate leaf area index at the global scale: Comparison with satellites products, J. Geophys. Res., 111, 1–16, 2006.
- Gibelin, A.-L., Calvet, J.-C., and Viovy, N.: Modelling energy and CO2 fluxes with an interactive vegetation land surface model-Evaluation at high and middle latitudes, Agr. Forest Meteorol., 148, 1611–1628, 2008.
- Gijsman, A. J., Jagtap, S. S., and Jones, J. W.: Wading through a swamp of complete confusion: how to choose a method for estimating soil water retention parameters for crop models, Eur. J. Agron., 18, 77–106, 2002.
- Giordani, H., Noilhan, J., Lacarrère, P., Bessemoulin, P., and Mascart, P.: Modelling the surface processes and the atmospheric boundary layer for semi-arid conditions, Agr. Forest Meteorol., 80, 263–287, 1996.
- Goudriaan, J., van Laar, H. H., van Keulen, H., and Louwerse, W.: Photosynthesis, CO2 and plant production, in: Wheat Growth and Modelling, edited by: Day, W. and Atkin, R. K., NATO ASI Series, Plenum Press, New York, 107–122, 1985.
- Gupta, H. V., Bastidas, L. A., Sorooshian, S., Shuttleworth, W. J., and Yang, Z. L.: Parameter estimation of a land surface scheme using multicriteria methods, J. Geophys. Res., 104, 19491, doi[:10.1029/1999JD900154,](http://dx.doi.org/10.1029/1999JD900154) 1999.
- Habets, F., Boone, A., Champeaux, J. L., Etchevers, P., Franchisteguy, L., Leblois, E., Ledoux, E., Moigne, P. L., Martin, E., Morel, S., Noilhan, J., and Viennot, P.: The SAFRAN-ISBA-

MODCOU hydrometeorological model applied over France, J. Geophys. Res., 113, 1–18, 2008.

- Hendricks Franssen, H. J., Stöckli, R., Lehner, I., Rotenberg, E., and Seneviratne, S. I.: Energy balance closure of eddy-covariance data: A multisite analysis for European FLUXNET stations, Agr. Forest Meteorol., 150, 1553–1567, 2010.
- Ingwersen, J., Steffens, K., Högy, P., Zhunusbayeva, D., Poltoradnev, M., Gäbler, R., Wizemann, H., Fangmeier, A., Wulfmeyer, V., and Streck, T.: Comparison of Noah simulations with eddy covariance and soil water measurements at a winter wheat stand, Agr. Forest Meteorol., 151, 345–355, 2011.
- Jacobs, C. M. J., Van den Hurk, B. J. J. M., and De Bruin, H. A. R.: Stomatal behaviour and photosynthetic rate of unstressed grapevines in semi-arid conditions, Agr. Forest Meteorol., 80, 111–134, 1996.
- Jacquemin, B. and Noilhan, J.: Sensitivity study and validation of a land surface parameterization using the hapex-mobilhy data set, Bound.-Lay. Meteorol., 52, 93–134, 1990.
- Jarvis, P. G.: The interpretation of the variations in water potential and stomatal conductance found in canopies in the field, Philos. T. Roy. Soc. Lond. B, 273, 593–610, 1976.
- Kondo, J., Nobuko, S., and Takeshi, S.: A parameterization of evaporation from bare soil surfaces, J. Appl. Meteorol., 29, 385–389, 1990.
- Lafont, S., Zhao, Y., Calvet, J.-C., Peylin, P., Ciais, P., Maignan, F., and Weiss, M.: Modelling LAI, surface water and carbon fluxes at high-resolution over France: comparison of ISBA-A-gs and ORCHIDEE, Biogeosciences, 9, 439–456, doi[:10.5194/bg-](http://dx.doi.org/10.5194/bg-9-439-2012)[9-439-2012,](http://dx.doi.org/10.5194/bg-9-439-2012) 2012.
- Leuning, R., Van Gorsel, E., Massman, W. J., and Isaac, P. R.: Reflections on the surface energy imbalance problem, Agr. Forest Meteorol., 156, 65–74, 2012.
- Masson, V., Le Moigne, P., Martin, E., Faroux, S., Alias, A., Alkama, R., Belamari, S., Barbu, A., Boone, A., Bouyssel, F., Brousseau, P., Brun, E., Calvet, J.-C., Carrer, D., Decharme, B., Delire, C., Donier, S., Essaouini, K., Gibelin, A.-L., Giordani, H., Habets, F., Jidane, M., Kerdraon, G., Kourzeneva, E., Lafaysse, M., Lafont, S., Lebeaupin Brossier, C., Lemonsu, A., Mahfouf, J.-F., Marguinaud, P., Mokhtari, M., Morin, S., Pigeon, G., Salgado, R., Seity, Y., Taillefer, F., Tanguy, G., Tulet, P., Vincendon, B., Vionnet, V., and Voldoire, A.: The SURFEXv7.2 land and ocean surface platform for coupled or offline simulation of earth surface variables and fluxes, Geosci. Model Dev., 6, 929–960, doi[:10.5194/gmd-6-929-2013,](http://dx.doi.org/10.5194/gmd-6-929-2013) 2013.
- Mauder, M., Cuntz, M., Drüe, C., Graf, A., Rebmann, C., Schmid, H. P., Schmidt, M., and Steinbrecher, R.: A strategy for quality and uncertainty assessment of long-term eddy-covariance measurements, Agr. Forest Meteorol., 169, 122–135, 2013.
- Merlin, O., Al Bitar, A., Rivalland, V., Béziat, P., Ceschia, E., and Dedieu, G.: An Analytical Model of Evaporation Efficiency for Unsaturated Soil Surfaces with an Arbitrary Thickness, J. Appl. Meteorol. Clim., 50, 457–471, 2011.
- Mertens, J., Madsen, H., Feyen, L., Jacques, D., and Feyen, J.: Including prior information and its relevance in the estimation of effective soil parameters in unsaturated zone modelling, J. Hydrol., 294, 251–269, 2004.
- Mertens, J., Madsen, H., Kristensen, M., Jacques, D., and Feyen, J.: Sensitivity of soil parameters in unsaturated zone modelling and

#### **S. Garrigues et al.: Evaluation of land surface model simulations of evapotranspiration 3131**

the relation between effective, laboratory and in situ estimates, Hydrol. Process., 19, 1611–1633, 2005.

- Moureaux C., Ceschia, E., Arriga, N., Beziat, P., Eugster., Kutsch, W L., Pattey, E.: Eddy covariance measurements over crops, in: Eddy Covariance: A practical guide to measurement and data analysis, edited by: Aubinet, M., Vesala, T., and Papale, D., Springer, Dordrecht, the Netherlands, 319–332, 2012.
- Mueller, B. and Seneviratne, S. I.: Systematic land climate and evapotranspiration biases in CMIP5 simulations, Geophys. Res. Lett., 41, 128–134, 2014.
- Noilhan, J. and Lacarrère, P.: GCM Grid-Scale Evaporation from Mesocale Modeling, J. Climate, 8, 206–223, 1994.
- Noilhan, J. and Mahfouf, J.-F.: The ISBA land surface parameterisation scheme, Global Planet. Change, 13, 145–159, 1996.
- Noilhan, J. and Planton, S.:. A simple parameterization of land surface processes for meteorological models, Mon. Weather Rev., 117, 536–549, 1989.
- Noilhan, J., Donier, S., Sarrat, C., and Moigne, P. L.: Regional-scale evaluation of a land surface scheme from atmospheric boundary layer observations, J. Geophys. Res., 116, 1–17, 2011.
- Olioso, A., Carlson, T. N., and Brisson, N.: Simulation of diurnal transpiration and photosynthesis of a water stressed soybean crop, Agr. Forest Meteorol., 81, 41–59, 1996.
- Olioso, A., Chauki, H., Courault, D., and Wigneron, J.-P.: Estimation of Evapotranspiration and Photosynthesis by Assimilation of Remote Sensing Data into SVAT Models, Remote Sens, Environ" 68, 341–356, 1999.
- Olioso, A., Braud, I., Chanzy, A., Courault, D., Demarty, J., Kergoat, L., Lewan, E., Ottlé, C., Prévot, L., Zhao, W., Calvet, J.-C., Cayrol, P., Jongshaao, R., Moulin, S., Noilhan, J., and Wigneron, J.-P.: SVAT modeling over the Alpilles-ReSeDA experiment: comparing SVAT models over wheat fields, Agronomie, 22, 651– 668, 2002.
- Olioso, A., Inoue, Y., Ortega-Farias, S., Demarty, J., Wigneron, J.- P., Braud, I., Jacob, F., Lecharpentier, P., Ottle, C., Calvet, J.-C., and Brisson, N.: Future directions for advanced evapotranspiration modeling: Assimilation of remote sensing data into crop simulation models and SVAT models, Irrig. Drain. Syst., 19, 377–412, 2005.
- Overgaard, J., Rosbjerg, D., and Butts, M. B.: Land-surface modelling in hydrological perspective – a review, Biogeosciences, 3, 229–241, doi[:10.5194/bg-3-229-2006,](http://dx.doi.org/10.5194/bg-3-229-2006) 2006.
- Pitman, A. J.: The evolution of, and revolution in, land surface schemes designed for climate models, Int. J. Climatol., 23, 479– 510, doi[:10.1002/joc.893,](http://dx.doi.org/10.1002/joc.893) 2003.
- Rebmann, C., Kolle, O., Heinesch, B., Queck, R, Ibrom, A., and Aubinet, M.: Data acquisition and flux calculation, in: Eddy Covariance: A practical guide to measurement and data analysis, edited by: Aubinet, M., Vesala, T., and Papale, D., Springer, Dordrecht, the Netherlands, 59–84, 2012.
- Richardson, A. D., Hollinger, D. Y., Burba, G. G., Davis, K. J., Flanagan, L. B., Katul, G. G., William Munger, J., Ricciuto, D. M., Stoy, P. C., Suyker, A. E., Verma, S. B., and Wofsy, S. C.: A multi-site analysis of random error in tower-based measurements of carbon and energy fluxes, Agr. Forest Meteorol., 136, 1–18, 2006.
- Schaap, M. G., Leij, F. J., and van Genuchten, M. T.: ROSETTA: a computer program for estimating soil hydraulic parameters with hierarchical pedotransfer functions, J. Hydrol., 251, 163–176, 2001.
- Scharnagl, B., Vrugt, J. A., Vereecken, H., and Herbst, M.: Inverse modelling of in situ soil water dynamics: investigating the effect of different prior distributions of the soil hydraulic parameters, Hydrol. Earth Syst. Sci., 15, 3043–3059, doi[:10.5194/hess-15-](http://dx.doi.org/10.5194/hess-15-3043-2011) [3043-2011,](http://dx.doi.org/10.5194/hess-15-3043-2011) 2011.
- Sellers, P. J. and Dorman, J. L.: Testing the Simple Biosphere Model (SiB) Using Point Micrometeorological and Biophysical Data, J. Clim. Appl. Meteorol., 26, 622–651, 1987.
- Steenpass, C., Vanderborght, J., Herbst, M., Simonek, J., and Vereecken, H.: Estimating soil hydraulic properties from infrared measurements of soil surface temperatures and TDR data, Vadose Zone J., 9, 910–924, 2011.
- Twine, T. E., Kustas, W. P., Norman, J. M., Cook, D. R., Houser, P. R., Meyers, T. P., Prueger, J. H., Starks, P. J., and Wesely, M. L.: Correcting eddy-covariance flux underestimates over a grassland, Agr. Forest Meteorol., 103, 279–300, 2000.
- Vereecken, H., Maes, J., and Darius, P.: Estimating the soil moisture retention characteristic from texture, bulk density and carbon content, Soil Sci., 148, 389–403, 1989.
- Verhoef, A. and Egea, G.: Modeling plant transpiration under limited soil water: Comparison of different plant and soil hydraulic parameterizations and preliminary implications for their use in land surface models, Agr. Forest Meteorol., 191, 22–32, 2014.
- Vidal, J.-P., Martin, E., Franchistéguy, L., Habets, F., Soubeyroux, J.-M., Blanchard, M., and Baillon, M.: Multilevel and multiscale drought reanalysis over France with the Safran-Isba-Modcou hydrometeorological suite, Hydrol. Earth Syst. Sci., 14, 459–478, doi[:10.5194/hess-14-459-2010,](http://dx.doi.org/10.5194/hess-14-459-2010) 2010.
- Vrugt, J. A., Braak, C. J. F., Gupta, H. V., and Robinson, B. A.: Equifinality of formal (DREAM) and informal (GLUE) Bayesian approaches in hydrologic modeling, Stoch. Environ. Res. Risk A., 23, 1011–1026, 2009.
- Wetzel, P. J. and Chang, J. T.: Concerning the relationship between evapotranspiration and soil moisture, J. Clim. Appl. Meteorol., 26, 18–27, 1987.
- Wilson, K., Goldstein, A., Falge, E., Aubinet, M., Baldocchi, D., Berbigier, P., Bernhofer, C., Ceulemans, R., Dolman, H., Field, C., Grelle, A., Ibrom, A., Law, B.E., Kowalski, A., Meyers, T., Moncrieff, J., Monson, R., Oechel, W., Tenhunen, J., Valentini, R., and Verma, S.: Energy balance closure at FLUXNET sites, Agr. Forest Meteorol., 113, 223–243, 2002.
- Workmann, S. R. and Skaggs, R. W.: Sensitivity of water management models to approaches for determining soil hydraulic properties, T. ASAE, 37, 95–102, 1994.