![](_page_0_Picture_1.jpeg)

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/01671987)

Soil & Tillage Research

![](_page_0_Picture_4.jpeg)

journal homepage: www.elsevier.com/locate/still

# Modelling of crop yields and N2O emissions from silty arable soils with differing tillage in two long-term experiments

B. Ludwig a, *, A. Bergstermann b , E. Priesack c , H. Flessa b,d

aDepartment of Environmental Chemistry, University of Kassel, Nordbahnhofstr. 1a, D-37213 Witzenhausen, Germany

b Soil Science of Temperate and Boreal Ecosystems, Bu¨sgen-Institute, University of Go¨ttingen, Bu¨sgenweg 2, D-37077 Go¨ttingen, Germany

c Institute of Soil Ecology, Helmholtz Center Mu¨nchen, Ingolsta¨dter Landstr. 1, Neuherberg D-85764, Germany

d Institute of Agricultural Climate Research, Johann Heinrich von Thu¨nen-Institut, Bundesallee 50, D-38116 Braunschweig, Germany

#### ARTICLE INFO

Article history: Received 30 July 2010 Received in revised form 19 December 2010 Accepted 20 December 2010

Keywords: Greenhouse gases N modelling

#### ABSTRACT

The choice of tillage system affects crop growth and soil nitrogen dynamics. Models help us to better understand these systems and the interaction of the processes involved. Objectives were to test a calibration and validation scheme for applications of the denitrification–decomposition (DNDC) model to describe a long-term field experiment with conventional tillage (CT) and reduced tillage (RT) at two sites (G and H, silty Haplic Luvisols) near Go¨ttingen, Germany (G-CT, G-RT, H-CT, H-RT). Crop growth of field bean (Vicia faba L.) and winter wheat (Triticum aestivum L.) as well as soil water dynamics and nitrous oxide (N2O) emissions were determined for two subsequent years. A model test was performed based on a model parameterization to best describe the case G-CT. This parameterization was then applied to the other cases as a retrospective simulation. Results of model variant v1 (no parameter optimization) indicated that soil water contents were not accurately simulated using the DNDC default values for a silt loam. After successful calibration of the soil water flow model using modified water-filled pore spaces at field capacity and wilting point and a modified hydro-conductivity that led to a good fit of the measured water content data, grain yields were markedly underestimated and modelled N2O emissions were too large (v2). An optimization of the crop properties (maximum grain yield, N fixation index, thermal degree days, transpiration coefficient) was essential for a better match of measured yields (v3). Further adjustments in the model (v4) were required to better match cumulative N2O emissions: reducing the initial soil organic carbon content and mineralization rates. Predictions of crop yields and annual cumulative N2O emissions using model variant v4 were fairly accurate for the reduced tillage system G-RT and also for the second field experiment H-CT and H-RT, but annual distributions of N2O emissions were not. Overall our results indicate that site specific calibration was an essential requirement for the silty German sites, and that the pedotransfer functions and denitrification submodel of DNDC may need further improvement.

> -2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Tillage systems affect crop yields and nitrous oxide (N2O) emissions. [Decker et al. (2009)](#page-6-0) studied the economics of five wheat (Triticum aestivum L.) production systems with no-till (NT) and conventional tillage (CT) in the Southern Plains of the United States and reported that average wheat grain yields were greater with CT, whereas average fall wheat forage yields were significantly greater on the NT plots. [Almaraz et al. (2009)](#page-6-0) reported for clay loam Alfisols in Quebec in a corn cropping system that the CT and NT systems had either no significant or only small differences in grain yields, but significantly higher forage yields

* Corresponding author. E-mail address: [bludwig@uni-kassel.de](mailto:bludwig@uni-kassel.de) (B. Ludwig). under NT. The tillage systems generally had similar cumulative carbon dioxide (CO2) emissions but NT had higher cumulative N2O emissions (3.7–5.5 kg N2O-N ha-1 ) than CT (2.3–4.1 kg N2O-N ha-1 ) in fertilized (180 kg N ha-1 ) and unfertilized treatments. Furthermore, [Rochette (2008)](#page-6-0) summarized 25 field experiments on a number of soil types with a wide range of textures by concluding that the impact of NT on N2O emissions depended markedly on the aeration of the soils: on average, N2O emissions under NT were 0.1 kg N ha-1 lower, 0.1 kg N ha-1 higher and 2.0 kg N ha-1 higher than from tilled soils with good, medium and poor aeration, respectively.

Less information is available for fields with reduced tillage (RT) or minimum tillage (MT). [Beheydt et al. (2008)](#page-6-0) reported for MT and CT systems on silty soils that N2O losses from MT maize (Zea mays L.) and MT oats (Avena sativa L.) fields (5.3 and 3.6 kg N2O-N ha-1 , respectively) were significantly higher than

<sup>0167-1987/\$ –</sup> see front matter - 2010 Elsevier B.V. All rights reserved. doi:[10.1016/j.still.2010.12.005](http://dx.doi.org/10.1016/j.still.2010.12.005)

#### <span id="page-1-0"></span>Table 1

Site characteristics for the soils (0–5 cm) of the conventional (CT) and reduced tillage (RT) treatments at Gartea (G-CT, G-RT) and Hohes Feldb (H-CT, H-RT) (means and standard errors, n = 4 for Garte and n = 3 for Hohes Feld).

|      | pH        | 3<br>Bulk density (g cm<br>) | 1<br>SOC (mg g<br>) | 1<br>Nt (mg g<br>) | Sand (%)   | Silt (%)   | Clay (%)   |
|------|-----------|------------------------------|---------------------|--------------------|------------|------------|------------|
| G-CT | 7.0 (0.1) | 1.36 (0.09)                  | 8.3 (0.8)           | 0.9 (0.1)          | 11.1 (0.5) | 74.6 (1.0) | 14.3 (0.8) |
| G-RT | 6.9 (0.1) | 1.25 (0.05)                  | 10.5 (0.9)          | 1.2 (0.1)          | 11.8 (0.6) | 78.2 (0.7) | 10.1 (1.0) |
| H-CT | 7.0 (0.1) | 1.32 (0.08)                  | 9.5 (0.4)           | 1.0 (0.0)          | 16.4 (0.9) | 65.7 (1.4) | 17.9 (0.6) |
| H-RT | 6.8 (0.1) | 1.40 (0.04)                  | 15.8 (1.0)          | 1.5 (0.1)          | 14.9 (0.7) | 67.0 (0.4) | 18.2 (1.1) |

a Garte is located at 518290 15.5000 latitude north and 98560 9.1700 longitude east. The soil type is Haplic Luvisol.

b Hohes Feld is located at 518370 14.1800 latitude north and 98560 30.9800 longitude east. The soil type is Haplic Luvisol.

those from a CT maize field (0.3 kg N2O-N ha-1 ) over a period of 1 year. [Abdalla et al. (2010)](#page-6-0) observed for Irish sandy loams that RT had no significant effect on N2O fluxes from soils and barley (Hordeum vulgare L.) grain yield in a 2-year field experiment compared to CT. Similarly, [Ussiri et al. (2009)](#page-7-0) reported no differences in N2O emissions for CT and MT systems on a silt loam for continuous corn. Overall, different tillage systems may affect crop yields and emissions of greenhouse gases, with soil aeration being one of the factors affecting the magnitude of the emissions.

Process-based models help us to understand or even predict the effects of different tillage systems on crop yields and greenhouse gas emissions. Several process-oriented models exist for this task (e.g., DAYCENT, CANDY, ExpertN or the denitrification–decomposition (DNDC) model ([Parton et al., 2001; Franko et al., 2007;](#page-6-0) [Kaharabata et al., 2003; Li, 2009](#page-6-0); for a review see [Chen et al.,](#page-6-0) [2008](#page-6-0))). Together with long-term experiments, these computer models may improve our understanding of the interactions between agricultural management, soil quality and the global environment.

The DNDC model has been successfully applied to sites with different tillage systems in several studies. [Farahbakhshazad et al.](#page-6-0) [(2008)](#page-6-0) applied the DNDC model to a row-crop field in IA, USA and carried out sensitivity tests. Model results indicated that NT significantly increased storage of soil organic carbon (SOC) and reduced nitrate–N leaching rate, but slightly decreased crop yield and increased N2O emissions. [Li et al. (2010)](#page-6-0) applied a similar sensitivity study to a winter wheat maize rotation system in China and reported that temperature, initial SOC content, tillage, and quantity and quality of the organic matter added to the soil had significant effects on simulated greenhouse gas emissions.

In contrast, [Abdalla et al. (2009)](#page-6-0) used the DNDC model less successfully for Irish agriculture. They reported that the simulations using DNDC underestimated measured N2O fluxes from RT plots up to 55%. The main problems were an overestimation of the water filled pore space (WFPS) and the effect of SOC on the flux. [Beheydt et al. (2008)](#page-6-0) reported for field experiments in Belgium a marked overestimation of N2O emissions with DNDC (CT, maize), a good agreement (MT, oats) and an underestimation (MT, maize).

The differences in performance of the DNDC model might be due to different soil and climatic conditions and may depend to a large extent on the model parameterization. Unfortunately, not in all studies cited above, model parameterization is sufficiently documented.

Therefore, the objectives of our study were to apply a proposed calibration and validation scheme for field experiments with CT and RT on silty soils near Go¨ttingen (Germany) in order to test the usefulness of the DNDC model in describing and predicting crop growth and N2O emissions.

## 2. Materials and methods

## 2.1. Study sites

We tested the DNDC model with data from two long-term trials near Go¨ttingen, Germany [(Jacobs et al., 2009; Bergstermann and](#page-6-0) [Flessa, 2009)](#page-6-0). Briefly, the experimental trials were carried out at Garte (518290 15.5000N, 98560 9.1700E) and Hohes Feld (518370 14.1800N, 98560 30.9800E). The mean temperature in the years 2007 and 2008 were 10.0 and 9.8 8C for Garte and 10.1 and 9.8 8C for Hohes Feld. The annual precipitation in 2007 and 2008 was 842 and 544 mm for Garte and 1015 and 564 mm for Hohes Feld. The soil type at both sites is a Haplic Luvisol [(WRB, 2006](#page-7-0)) derived from loess [(Ehlers](#page-6-0) [et al., 2000; Reiter et al., 2002)](#page-6-0). For soil properties see Table 1.

A field experiment was established in 1970 at Garte and in 1967 at Hohes Feld consisting of 4 and 3 field-replicates, respectively. The treatments were CT at Garte (G-CT) and Hohes Feld (H-CT) with a regular mouldboard plough to 25 cm depth followed by seedbed preparation with a rotary harrow and RT (G-RT and H-RT) with shallow cultivation down to 5–8 cm depth with a rotary harrow for seedbed preparation. Before the start of the experiment the soil had been mouldboard ploughed. At Garte, the experimental design was a randomised complete block design with four replicate plots (20 m 40 m). At Hohes Feld, a split plot design with three replicate plots (12.8 m 36 m) was established due to a smaller dimension of the field. The crops grown were the same at both sites and the crop rotation was cereal based since 1970 ([Reiter](#page-6-0) [et al., 2002)](#page-6-0). Crops in the period 2006–2008 were forage maize in 2006, field bean (Vicia faba L.) in 2007 and winter wheat in 2008. All residues were incorporated by the respective tillage operations. Timing and amount of N fertilization, timing of tillage and number of herbicide applications at G-CT are given in [Table 2.](#page-2-0)

For G-RT, management was the same as for G-CT, except that no mouldboard ploughing was carried out. Seedbed preparation with a rotary harrow was carried out on the 28th of March and 2nd of November 2007.

For H-CT, management was also the same as for G-CT, except that harvest of bean was one day later and mouldboard ploughing was carried out on the 28th of March and 31st of October 2007. Seedbed preparation was carried out on the 29th of March and 1st of November 2007. In contrast to G-CT, no N fertilizer was applied on the 6th of June, instead, the application on the 28th of May 2008 was increased to 67.5 kg N ha-1 . Thus, N fertilization of H-CT in 2008 was 170.1 kg N ha-1 , slightly less (13.6 kg N ha-1 ) than at G-CT.

Management for H-RT was the same as for H-CT, except that no mouldboard ploughing was carried out. Seedbed preparation was carried out on the 29th of March and 1st of November 2007.

## 2.2. Field N2O fluxes and water content of soil

Trace gas fluxes of N2O were measured approximately once a week from April 2007 to December 2008 ([Fig. 1](#page-2-0)). This temporal resolution allowed the estimation of the seasonal pattern of the fluxes. No specific attention was given to heavy rainfall events. However, the variation of water filled pore space (determined on the same day as the flux measurements, [Fig. 2](#page-2-0)) indicated that a large range of soil water contents was covered by the measurement scheme.

The N2O fluxes were measured using the closed chamber method with three chambers on each of the four (Garte) or three

<span id="page-2-0"></span>![](_page_2_Figure_2.jpeg)

Summary of selected input data of the denitrification–decomposition (DNDC) model for the conventional tillage (CT) treatment at Garte (G-CT).

| Data                                                      | Value                  | Data                             | Value             |
|-----------------------------------------------------------|------------------------|----------------------------------|-------------------|
| Climate data                                              |                        | Crop data                        |                   |
| Latitude (8)                                              | 51.488                 | (1) Crop: beanc (dates)          | 29.03.07–29.08.07 |
| Annual mean temperature in 2007 and 2008 (8C)             | 9.97, 9.82             | (2) Crop: winter wheatd (dates)  | 02.11.07–31.07.08 |
| Annual precipitation in 2007 and 2008 (mm)                | 842, 544               |                                  |                   |
| Atmospheric CO2 concentration (ppm)                       | 350                    | Tillage                          |                   |
| N concentration in rainfall (ppm)                         | 2.7                    | Ploughinge down to 20 cm (dates) | 27.03.07          |
|                                                           |                        |                                  | 01.11.07          |
|                                                           |                        | Ploughing slightlyf (date)       | 28.03.07          |
|                                                           |                        |                                  | 02.11.07          |
| Soil datab                                                |                        |                                  |                   |
| Soil texture                                              | Silt loam              |                                  |                   |
| Bulk density (0–10 cm) (g cm<br>3<br>)                    | 1.42                   | Irrigation and weeding           |                   |
| Fertilization                                             |                        | Irrigation                       | None              |
| Calcium ammonium nitrate applied on                       | 54.0, 48.6, 43.3, 37.8 | Application of herbicidesg       | On eight dates    |
| 31.03.08, 29.04.08, 28.05.08, 06.06.08 (kg N ha<br>1<br>) |                        |                                  |                   |

a Garte is located at 98560 9.1700 longitude east. The soil type is Haplic Luvisol.

b pH and Corg are given in [Table 1.](#page-1-0) c

Field bean (Vicia faba L.) was cultivated, the crop bean was used in DNDC.

dTriticum aestivum L.

f

e Ploughing depth was 25 cm (25 cm depth is not included in DNDC).

Soil was tilled using a rotary harrow (not included in DNDC, thus ploughing slightly was used in the model).

g Not included in the model, since weed problems on the field were minimal.

(Hohes Feld) plots per treatment (thus the number of field replicates was n = 4 (Garte) or n = 3 (Hohes Feld) for each treatment). The method is described in detail by [Ruser et al.](#page-6-0) [(2001).](#page-6-0) The circular chambers were made of dark PVC with an inner diameter of 30 cm and an initial height of 15 cm. By using extensions of the same material the height of the chamber could be adjusted to plant growth. For each gas measurement these chambers were placed on permanently installed PVC-soil collars with the same diameter and sealed with a lid. The closed chamber method was chosen because of its well known advantages – small fluxes can be measured, chambers are cheap and the disturbance of the site is limited ([FAO, 2001](#page-6-0)). However, a major disadvantage is that the area covered by the chambers is small, which results in uncertainties of the emission estimates due to the spatial variability in the field ([Laville et al., 1999)](#page-6-0).

On the same day as the flux measurements, water content of soil was determined with four replicates for each treatment. Briefly, soil samples were taken at a depth of 0–10 cm. Samples were weighed, oven dried to constant mass at 105 8C, and reweighed. The dry weight and differences between fresh and dry weight were used to

![](_page_2_Figure_15.jpeg)

Fig. 1. Modelled (lines, model variant v4) and measured (symbols, means and standard errors) N2O emissions from soils of the conventional tillage treatment at Garte (G-CT, located at 518290 15.5000 latitude north and 98560 9.1700 longitude east. The soil type is Haplic Luvisol).

![](_page_2_Figure_17.jpeg)

Fig. 2. Modelled (at 5 cm depth, lines, model variants v1 and v2) and measured (in the 0–10 cm depth range, symbols, means and standard errors) water filled pore space in soils of the conventional tillage treatment at Garte (G-CT, located at 518290 15.5000 latitude north and 98560 9.1700 longitude east. The soil type is Haplic Luvisol).

calculate the gravimetric water content. Water filled pore space is calculated by WFPS = (soil gravimetric water content bulk density) (1 - (bulk density/particle density))-1 [(Linn and Doran, 1984](#page-6-0)) and by using a particle density of 2.65 g cm-3 .

#### 2.3. DNDC model

We used the DNDC model (model version 9.3; [http://](http://www.dndc.sr.unh.edu/) [www.dndc.sr.unh.edu](http://www.dndc.sr.unh.edu/)) to describe and predict water dynamics, crop growth and N2O emissions on a field scale. The DNDC model consists of soil climate, crop growth and decomposition submodels and calculates soil temperature, water content, pH, redox potential (Eh), and substrate concentration profiles driven by ecological drivers (e.g., climate, soil, vegetation and anthropogenic activity). Additionally, nitrification, denitrification, and fermentation sub-models calculate emissions of CO2, methane (CH4), ammonia (NH3), nitric oxide (NO), N2O and dinitrogen (N2) from the plant–soil systems ([Li, 2009](#page-6-0)). In the model, denitrification is calculated by assuming the presence of an ''anaerobic balloon''. Overall, the model relies on the assumption of universal microbial parameters for the kinetics of their growth and N2O production ([Li,](#page-6-0) [2009)](#page-6-0). The following model variants were considered.

## 2.3.1. Model variant v1 – no calibration, sole use of the measured initial data and default values

No calibration was carried out. For a prediction of soil water dynamics, crop growth, and N2O emission in the G-CT treatment, the model used the measured input for the SOC content and pH [(Table 1)](#page-1-0), bulk density (0–10 cm) and the crop management [(Table 2)](#page-2-0). The hydraulic soil characteristics were estimated by the model using the implemented pedotransfer function for a silt loam. For crop growth of field bean and winter wheat, the default values for ''bean'' and ''winter wheat'' provided by DNDC were used. Weeding, as carried out at the field sites, could not be considered by the model, since the optionswere only ''noweed problem'' or ''moderateweed problems''.

## 2.3.2. Model variant v2 – adjustment of soil water dynamics using curve fitting

The model variant v2 was the same as model variant v1 except that we now used modified soil hydrology parameters in order to get an optimum agreement between measured and calibrated WFPS. Optimum agreement was achieved by setting the WFPS at field capacity to 72%, the WFPS at wilting point to 15% and the hydro-conductivity to 0.0045 m h-1 .

## 2.3.3. Model variant v3 – calibration to observed yields using literature data of crop properties

Crop growth is affected by a number of factors (site specific soil and climate conditions, crop variety used, method of pest control, use of growth promoters) and calibration of crop growth may be achieved by optimizing several combinations of parameters. In the DNDC manual ([Li, 2009)](#page-6-0), it is suggested that for a calibration of crop growth, the crop heat/water/N demands, growth curve, biomass partitioning, or yield may be adjusted.

Model variant v3 was based on model variant v2. An additional calibration was carried out based on the yield and crop growth data of the experimental treatment G-CT.

For field bean, the maximum grain yield was increased from 600 kg C ha-1 (default value in DNDC, 16.2 decitonnes (dt) dry matter (dm) ha-1 ) to 1800 kg C ha-1 (49 dt dm ha-1 ) in order to match the large yield in our field experiment. The N fixation index was increased from 1.2 (default) to 4 in order to reach an N2 assimilation in the range of 80–90 kg N ha-1 ([Schilling, 2000](#page-6-0)).

For winter wheat, maximum grain yield was increased from 2500 kg C ha-1 (default value in DNDC, 67.6 dt dm (including 14% water) ha-1 ) to 4500 kg C ha-1 (122 dt dm ha-1 ). Additionally, the biomass fractions for winter wheat were modified: the biomass fraction for grain was changed from 0.3 (default value) to 0.42 and the biomass fraction for leaf plus stem was changed from 0.53 (default value) to 0.41 since the grain:straw ratio of winter wheat is approximately 1 ([KTBL, 2005)](#page-6-0). The biomass fraction for root was thus 0.17 (same as the default value), since the sum of the three fractions equals 1. The thermal degree days (with daily averages > 10.0 8C) were decreased from 2500 (default value) to 1600 8C (the minimum value of the range reported by [Entrup and](#page-6-0) [Oehmichen, 2000)](#page-6-0), the C/N ratio of grains was increased from 30 (default value) to 40 and the transpiration coefficient was reduced from 280 (default value) to 169 kg water (kg dm)-1 (the minimum value of the range reported by [Ehlers, 1996)](#page-6-0).

## 2.3.4. Model variant v4 – calibration to observed yields and N2O emissions using additional parameter fitting

Model variant v4 was based on model variant v3 with the following additional adaptations of parameters: the decomposition rates of the three soil organic C pools were reduced by a factor of 0.3 and the initial SOC content was reduced from 8.3 mg g-1 to 2.7 mg g-1 to better match the cumulative N2O emission of the G-CT treatment in 2007 (April until December) and 2008 (January until December).

#### 2.3.5. Retrospective predictions

Retrospective predictions were carried out for the remaining treatments and sites G-RT, H-CT and H-RT based on the parameters obtained by the calibration in variant v4. The models were the same as described above with the following exceptions:

#### G-RT: RT was used in the model instead of CT.

H-CT and H-RT: the different latitude and climate data were used. The slightly different N fertilization scheme (application of 170.1 instead of 183.7 kg N ha-1 ) and the minimal changes in harvest and tillage dates described above were considered. Again, the model considered either CT (H-CT) or RT (H-RT).

#### 2.4. Statistics

The performance of the model calibration and retrospective prediction of the soil water dynamics was evaluated by calculation of the root mean square error (RMSE), model efficiency (EF), and relative error (E) as defined in [Smith et al. (1997):](#page-6-0)

$$\text{RMSE} = \frac{\mathbf{100}}{\overline{\mathbf{O}}} \sqrt{\sum_{i=1}^{n} \frac{(P_i - \mathbf{O}_i)^2}{n}},\tag{1}$$

$$\text{EF} = \frac{\sum_{i=1}^{n} \left(\mathbf{O}_{i} - \overline{\mathbf{O}}\right)^{2} - \sum_{i=1}^{n} \left(\mathbf{P}_{i} - \mathbf{O}_{i}\right)^{2}}{\sum_{i=1}^{n} \left(\mathbf{O}_{i} - \overline{\mathbf{O}}\right)^{2}},\tag{2}$$

$$E = \frac{100}{n} \sum_{i=1}^{n} \frac{\mathcal{O}_i - P_i}{\mathcal{O}_i},\tag{3}$$

where Oi is the observed (measured) value, Pi is the predicted value, O is the mean of the observed data and n is the number of paired values. RMSE ranges from 0 to 1, EF from -1 to 1 and E from -1 to 1. For an ideal fit, RMSE and E equal zero and EF equals 1.

## 3. Results and discussion

## 3.1. Yields and N2O emissions

Grain yields of field beans were almost identical for both tillage treatments and also similar between the two sites ([Tables 3 and 4)](#page-4-0). The range of 45.7–49.2 dt dm ha-1 in our study

## <span id="page-4-0"></span>Table 3

Measured (means and standard errors, n = 4) and modelled yields of bean and wheat and cumulative N2O emissions in the conventional tillage (CT) treatment at Gartea (G-CT). Statistics on the measured and modelled soil water dynamics are also given. Modelled data refer to a retrospective prediction (model variant v1) and calibration results (model variants v2–v4).

|                                                                                             | Measured                 | v1                             | v2                             | v3                             | v4                             |
|---------------------------------------------------------------------------------------------|--------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|
| Yields<br>1                                                                                 |                          |                                |                                |                                |                                |
| Field beanb grainc (dt dmd ha<br>)                                                          | 45.7 (1.2)               | 9.6                            | 10.4                           | 39.3                           | 39.3                           |
| Winter wheate grainc (dt dm ha<br>1<br>)                                                    | 103.4 (2.1)              | 5.2                            | 8.4                            | 76.8                           | 76.8                           |
| N2O emissionsf<br>1<br>Cumulative N2O emissions (g N2O-N ha<br>)<br>2007<br>2008            | 1160 (140)<br>1050 (430) | 1470<br>10,210                 | 800<br>10,530                  | 6610<br>51,210                 | 640<br>1570                    |
| Sum                                                                                         | 2210                     | 11,680                         | 11,330                         | 57,820                         | 2210                           |
| Soil water<br>Mean WFPSg (%) for all sampling dates<br>RMSE (WFPS)<br>EF (WFPS)<br>E (WFPS) | 60.1<br>–<br>–<br>–      | 26.2<br>59.4<br><br>4.5<br>167 | 63.1<br>17.0<br>0.5<br><br>2.4 | 62.2<br>16.3<br>0.6<br><br>0.9 | 62.2<br>16.3<br>0.6<br><br>0.9 |

RMSE: root mean square error, EF: model efficiency, and E: relative error.

a Garte is located at 518290 15.5000 latitude north and 98560 9.1700 longitude east. The soil type is Haplic Luvisol.

b Vicia faba L.

c Amounts include 14% water content for grain. Modelled yields were recalculated using a C content of 43% (grains, straw) and considering a water content of 14% (grains). d Decitonnes dry matter.

e Triticum aestivum L.

f Measured and modelled emissions refer to the periods from April to December (2007) and from January to December (2008).

g Water filled pore space.

#### Table 4

Measured (means and standard errors, n = 4 for the yields at Garte or n = 3 for the yields at Hohes Feld) and predicted grain yields of bean and wheat and cumulative N2O emissions in the reduced tillage treatment (RT) at Gartea (G-RT) and in the RT and conventional tillage (CT) treatments at Hohes Feldb (H-RT, H-CT). Statistics on the measured and modelled soil water dynamics are also given.

|                                                                                              | G-RT                      |              | H-CT                   |              | H-RT                     |              |
|----------------------------------------------------------------------------------------------|---------------------------|--------------|------------------------|--------------|--------------------------|--------------|
|                                                                                              | Measured                  | v4           | Measured               | v4           | Measured                 | v3           |
| Yields<br>Field beanc graind (dt dmeha<br>1<br>)<br>Winter wheatf graind (dt dm ha<br>1<br>) | 45.8 (2.0)<br>103.8 (2.3) | 39.3<br>77.1 | 49.1 (1.7)<br>75.4g    | 41.8<br>72.8 | 49.2 (0.9)<br>88.2 (1.0) | 41.8<br>73.0 |
| N2O emissionsh<br>Cumulative N2O emissions (g N2O-N ha<br>1<br>)<br>2007<br>2008             | 1360 (100)<br>1640 (290)  | 660<br>2750  | 1770 (110)<br>770 (20) | 710<br>1510  | 1260 (20)<br>2460 (490)  | 740<br>1850  |
| Sum                                                                                          | 3000                      | 3410         | 2540                   | 2220         | 3720                     | 2590         |
| Soil water<br>Mean WFPSi for all sampling dates<br>EF (WFPS)                                 | 60.0<br>–                 | 62.3<br>0.6  | 63.8<br>–              | 60.4<br>0.4  | 73.9<br>–                | 60.3<br>0.0  |

EF: model efficiency.

a Garte is located at 518290 15.5000 latitude north and 98560 9.1700 longitude east. The soil type is Haplic Luvisol.

b Hohes Feld is located at 518370 14.1800 latitude north and 98560 30.9800 longitude east. The soil type is Haplic Luvisol.

c Vicia faba L.

d Amounts include 14% water content for grain. Modelled yields were recalculated using a C content of 43% (grains, straw) and considering a water content of 14% (grains). e Decitonnes dry matter.

f Triticum aestivum L.

g Data for one subplot, yields on the other subplots were 52.7 and 55.5 dt dm ha-1 due to damages caused by wild boars.

h Measured and modelled emissions refer to the periods from April to December (2007) and from January to December (2008).

i Water filled pore space.

is above the average grain yield of 35.3 dt dm ha-1 for field beans in Germany in 2007 ([Statistisches Bundesamt Deutsch](#page-7-0)[land, 2009](#page-7-0)) and indicates a high soil fertility for both sites. For winter wheat, grain yields at Garte were high without differences between the tillage treatments, whereas for Hohes Feld, grain yield was slightly smaller (Tables 3 and 4). Again, yields were above the average yields in Germany (65.5–82.1 dt dm ha-1 in the years 2003–2007, [Statistisches](#page-7-0) [Bundesamt Deutschland, 2009)](#page-7-0).

Cumulative N2O emissions for the silty soils (Haplic Luvisols) ranged from 1.2 to 1.8 kg N2O-N in 2007 (01.04. until 31.12.) and from 0.8 to 2.5 kg N2O-N ha-1 in 2008 (01.01. until 31.12., Tables 3 and 4) and were thus in the lower range reported by [Jungkunst et al. (2006)](#page-6-0) who summarized that annual N2O emissions from fertilized German arable soils (seven Anthrosols, one Arenosol, eight Cambisols, one Chernosem, two Fluvisols, two Gleysols, ten Luvisols, and one Planosol) ranged from 0.1 to 17.1 kg N2O-N ha-1 . In our study, a marked increase of N2O emissions in 2008 due to the cropping of a legume in 2007 was expected (e.g., [Wagner-Riddle et al., 1997; Flessa et al., 2002](#page-7-0)), but was probably counterbalanced by the considerably drier conditions in 2008.

Differences between the tillage treatments were not marked in 2007. In 2008, however, the emission of 2.5 kg N2O-N ha-1 at H-RT was 2–3 times greater than emissions from the other three plots. Seasonal dynamics of N2O emissions were pronounced, especially in 2007 where the N2O emissions were largest in autumn and winter 2007. Emissions of N2O are generally associated with soil management and cropping systems, variable rainfall, especially drying/rewetting, freeze/thawing events, and amount and type of fertilizer N ([Kaiser et al., 1996; Kaiser and Ruser, 2000; Jungkunst](#page-6-0) [et al., 2006](#page-6-0)). In our study, increased N2O emissions coincided with the cropping of winter wheat after harvest of field bean and tillage in November 2007. Spatial variability of the emissions, however, was strong. Fertilization in 2008 had only small effects on N2O emissions.

## 3.2. Performance of model variant v1 – no calibration, sole use of the measured initial data and default values

Model variant v1 was applied to provide an independent simulation without any parameter optimization. The performance was poor ([Table 3)](#page-4-0), indicating that the default values given by DNDC may not always be useful. The pedotransfer function used for this site (silt loam) resulted in large deviations between modelled and measured WFPS data ([Fig. 2](#page-2-0) and [Table 3)](#page-4-0). Mean WFPS on the 75 sampling dates differed between 60% (measured) and 26% (modelled). The root mean square error RMSE and the relative error E were the largest of all four model variants tested ([Table 3)](#page-4-0). The negative efficiency value EF of -4.5 indicated that the model variant described the WFPS data less well than the mean of the data. Deviations between measured and simulated WFPS were also reported in some other studies. [Abdalla et al. (2009)](#page-6-0) applied the DNDC model for an Irish grassland soil (texture: sandy loam) and reported that WFPS was considerably overestimated by DNDC (version 9.2). Similar to our results, [Smith et al. (2008)](#page-7-0) reported for Canadian sites (textures: loam and clay loams) that DNDC underestimated soil water content particularly during the growing season.

Since soil water dynamics was not simulated correctly in model variant v1, it is not surprising that modelled crop growth was exceptional low and modelled N2O emissions in 2008 were high ([Table 3)](#page-4-0). The main reason is the strongly underestimated N uptake by winter wheat (49 kg N ha-1 ), which left large amounts of N available for losses through denitrification and nitrification.

## 3.3. Performance of model variant v2 – adjustment of soil water dynamics using curve fitting

The satisfactory agreement between modelled and measured WFPS data [(Fig. 2)](#page-2-0) indicated that the calibration of soil hydraulic characteristics using optimized WFPS data for field capacity (72%) and wilting point (15%) and an optimized hydro-conductivity (0.0045 m h-1 ) was successful: RMSE decreased to 17.0, E decreased markedly to -2.4, and EF increased to 0.5 ([Table 3](#page-4-0)). Similarly, [Tonitto et al. (2007)](#page-7-0) reported that an accurate simulation of NO3–N leaching and drainage dynamics using DNDC required significant changes to key soil physical and chemical parameters relative to their default values for arable soils in the USA.

The calibration in our study may have been required because of experimental uncertainties. For instance, additional water sources such as groundwater or aquifers in the subsoils may largely affect soil water dynamics and crop growth. However, no impact of groundwater down to 5 m depth was observed at this site. Calibration may have also been required because of uncertainties in the DNDC algorithms. For instance, inaccuracies in the estimation of the potential evapotranspiration cannot be ruled out: in DNDC, the Thornthwaite approach is implemented. However, this approach is assumed to be less accurate than the Penman–Monteith equation ([Guo et al., 2007; Mu¨ller, 1982](#page-6-0)). Additionally, inaccuracies in the calculation of the flow of soil water are likely: [Kro¨bel et al. (2010)](#page-6-0) tested the DNDC model for a soil (Calcaric Cambisol with a silty-loamy texture) in the North China Plain and concluded that the cascade model approach used by the DNDC model appeared to be unsuitable to simulate soil water dynamics at their site.

In our study, despite the improved description of soil hydrology in model variant v2, there was no overall improved performance of modelled crop growth and N2O emissions, which was still poor [(Table 3)](#page-4-0).

## 3.4. Performance of model variant v3 – calibration to observed yields using literature data of crop properties

The need for a calibration of crop properties for different sites is evident, due to differences in growth performance because of site specific soil and climate conditions and also due to ongoing improvements of crop growth by having better varieties, improved pest control and growth promoters. The adjustments made in model variant v3 – a threefold (field bean) and a 1.8-fold (winter wheat) increase of maximum grain yields, an increase of the N fixation index to 4 (bean), a change of the biomass fraction for grain and leaf plus stem, a decrease of the transpiration coefficient and thermal degree days – are backed up by the literature ([Schilling,](#page-6-0) [2000; Entrup and Oehmichen, 2000; Ehlers, 1996)](#page-6-0) and resulted in large reductions of water and nitrogen stress: simulated grain yields increased from 10.4 to 39.3 dt dm ha-1 (86% of the measured data) for field bean and from 8.4 to 76.8 dt dm ha-1 (74% of the measured data) for winter wheat ([Table 3](#page-4-0)). Overall, one has to keep in mind that several crop parameters, especially the transpiration coefficient and the thermal degree days are highly site specific. We used the ranges summarized by [Ehlers (1996)](#page-6-0) and [Entrup and Oehmichen (2000).](#page-6-0) However, the available literature merely gives overviews of ranges observed and does not give distinct minimum and maximum data for all sites and crop varieties.

Despite an improved description of crop yields, overall performance of model variant v3 was still unsatisfactory: simulated cumulative N2O emission in the 2-year period was 26-fold larger than the measured emission ([Table 3](#page-4-0)), indicating that this model variant is not usable for predictive purposes for the other three treatments. According to the model, much more nitrate is present in the soil at the beginning of 2008 (63 kg N ha-1 compared to 3 kg N ha-1 in model variant v2), which is used for denitrification and this leads to the calculated large N2O emission in 2008.

## 3.5. Performance of model variant v4 – calibration to N2O emissions using additional parameter fitting

Model variant v4 included as additional adjustments a reduction of the C content in the surface soil and of the mineralization rate of the C pools. These adjustments resulted in a matched cumulative N2O emission (the modelled sum and the measured sum amounted to 2210 g N2O-N ha-1 , [Table 3](#page-4-0)) for the entire period (April 2007 until December 2008). The sensitivity of the N2O emissions to changes of the initial SOC content in the surface soil is well known [(Abdalla et al., 2009)](#page-6-0). The main reasons for the markedly smaller N2O emissions in model variant v4 compared to v3, especially in 2008, are that less nitrate was present in the soil at the beginning of 2008 (44 instead of 63 kg N ha-1 ), that less N was mineralized in 2008 (3.9 instead of 19.4 kg N ha-1 ) and that more N was present as nitrate in the soil at the end of 2008 (95 instead of 49 kg N ha-1 ).

<span id="page-6-0"></span>Considering its overall performance for a description of crop yields and N2O emissions in treatment G-CT, variant v4 was satisfactory and markedly more accurate than variants v1–v3. This overall satisfactory performance indicates the need for site-specific calibration of the DNDC model to describe the complex plant–soil– atmosphere interactions and emphasizes the relationship between model and site (Beven, 2002; Priesack et al., 2006).

However, besides the need for parameter fitting discussed above, the main shortcomings of model variant v4 were the underestimation (in 2007) and overestimation (in 2008) of N2O emissions and a lack of agreement between simulated and observed annual distributions of the emissions ([Table 3](#page-4-0) and [Fig. 1)](#page-2-0). Thus, the assumption of universal microbial parameters for the kinetics of their growth and N2O production (Li, 2009) may be challenged and/or the denitrification sub-model of DNDC may need further improvements.

Soil water dynamics were similar for all four treatments, with slightly wetter conditions at H-RT [(Table 4)](#page-4-0). The calibration done for the G-CT had a similar performance for a prediction of soil hydrology for G-RT and H-CT (EF = 0.6 and 0.4, respectively, [Table 4)](#page-4-0) and was slightly less useful for H-RT (EF = 0.0, [Table 4)](#page-4-0).

Prediction accuracy for the grain yields of field bean was similar for all three treatments and overall satisfactory, whereas the smaller grain yields of winter wheat at Hohes Feld were closer to the modelled ones than those at Garte [(Table 4)](#page-4-0).

For the cumulative N2O emissions, modelled results for G-RT, H-CT and H-RT were similar to the experimental ones [(Table 4](#page-4-0)). Moreover, the DNDC predicted correctly that the RT treatments had slightly higher N2O emissions than the CT treatments. However, for all three cases, DNDC slightly underestimated (H-CT, H-RT) or overestimated (G-RT) the cumulative N2O emissions [(Table 4)](#page-4-0) and the annual distribution of emissions was not reproduced correctly (data not shown).

#### 4. Conclusions

The DNDC model is a very user-friendly model, requiring inputs that are generally easy to obtain. Our results for German silty arable sites indicate that site-specific calibration is essential and that calibration with experimental data and literature data available may result in approximate agreement between modelled and measured crop yields but large deviations between modelled and measured N2O emissions. If a better agreement is required then a parameter fitting procedure (as in our model variant v4) may be necessary. Thus, the pedotransfer functions and the denitrification sub-model of DNDC may need further improvement.

## Acknowledgement

This study was supported by a grant from the Deutsche Forschungsgemeinschaft in the Research Training Group 1397.

## References

- Abdalla, M., Wattenbach, M., Smith, P., Ambus, P., Jones, M., Williams, M., 2009. Application of the DNDC model to predict emissions of N2O from Irish agriculture. Geoderma 151, 327–337.
- Abdalla, M., Jones, M., Ambus, P., Williams, M., 2010. Emissions of nitrous oxide from Irish arable soils: effects of tillage and reduced N input. Nutr. Cycl. Agroecosys. 86, 53–65.
- Almaraz, J.J., Mabood, F., Zhou, X.M., Madramootoo, C., Rochette, P., Ma, B.L., Smith, D.L., 2009. Carbon dioxide and nitrous oxide fluxes in corn grown under two tillage systems in southwestern Quebec. Soil Sci. Soc. Am. J. 73, 113–119.
- Beheydt, D., Boeck, P., Ahmed, H.P., Van Cleemput, O., 2008. N2O emission from conventional and minimum-tilled soils. Biol. Fertil. Soils 44, 863–873.
- Bergstermann, A., Flessa, H., 2009. Effects of conventional and reduced tillage on GHG fluxes. In: Workshop ''Soil Organic Matter and Nutrient Turnover in Agriculture'', 12–13th November 2009, Witzenhausen, Germany.
- Beven, K., 2002. Towards an alternative blueprint for a physically based digitally simulated hydrologic response modelling system. Hydrol. Process. 16, 189– 206.
- Chen, D., Yong, L., Grace, P., Mosier, A.R., 2008. N2O emissions from agricultural lands: a synthesis of simulation approaches. Plant Soil 309, 169–189.
- Decker, J.E., Epplin, F.M., Morley, D.L., Peeper, T.F., 2009. Economics of five wheat production systems with no-till and conventional tillage. Agron. J. 101, 364– 372.
- Ehlers, W., 1996. Wasser in Boden und Pflanze. Ulmer Verlag, Stuttgart, Germany. Ehlers, W., Werner, D., Ma¨hner, T., 2000. Wirkung mechanischer Belastung auf Gefu¨ ge und Ertragsleistung einer Lo¨ ss-Parabraunerde mit zwei Bearbeitungssystemen. J. Plant Nutr. Soil Sci. 163, 321–333.
- Entrup, N.L., Oehmichen, J., 2000. Lehrbuch des Pflanzenbaus 2. Kulturpflanzen. Th. Mann Verlag, Gelsenkirchen, Germany.
- FAO, 2001. Global Estimates of Gaseous Emissions of NH3, NO and N2O from Agricultural Land. FAO and IFA, Rome.
- Farahbakhshazad, N., Dinnes, D.L., Li, C.S., Jaynes, D.B., Salas, W., 2008. Modeling biogeochemical impacts of alternative management practices for a row-crop field in Iowa. Agric. Ecosyst. Environ. 123, 30–48.
- Flessa, H., Ruser, R., Do¨ rsch, P., Kamp, T., Jimenez, M.A., Munch, J.C., Beese, F., 2002. Integrated evaluation of greenhouse gas emissions from two farming systems in southern Germany: special consideration of soil N2O emissions. Agric. Ecosyst. Environ. 91, 175–189.
- Franko, U., Kuka, K., Romanenko, I.A., Romanenkov, V.A., 2007. Validation of the CANDY model with Russian long-term experiments. Region. Environ. Change 7, 79–91.
- Guo, L., Falloon, P., Coleman, K., Zhou, B., Li, Y., Lin, E., Zhang, F., 2007. Application of the RothC model to the results of long-term experiments on typical upland soils in northern China. Soil Use Manage. 23, 63–70.
- Jacobs, A., Rauber, R., Ludwig, B., 2009. Impact of reduced tillage on carbon and nitrogen storage of two Haplic Luvisols after 40 years. Soil Till. Res. 102, 158– 164.
- Jungkunst, H.F., Freibauer, A., Neufeldt, H., Bareth, G., 2006. Nitrous oxide emissions from agricultural land use in Germany – a synthesis of available annual field data. J. Plant Nutr. Soil Sci. 169, 341–351.
- Kaharabata, S.K., Drury, C.F., Priesack, E., Desjardins, R.L., McKenney, D.J., Tan, C.S., Reynolds, D., 2003. Comparing measured and expert-N predicted N2O emissions from conventional till and no till corn treatments. Nutr. Cycl. Agroecosys. 66, 107–118.
- Kaiser, E.A., Ruser, R., 2000. Nitrous oxide emissions from arable soils in Germany an evaluation of six long-term field experiments. J. Plant Nutr. Soil Sci. 163, 249–259.
- Kaiser, E.-A., Eiland, F., Germon, J.C., Gispert, M., Heinemeyer, O., Henault, C., Lind, A.M., Maag, M., Saguer, E., van Cleemput, O., Vermoesen, A., Webster, C., 1996. What predicts nitrous oxide emissions and denitrification N-loss from European soils? Z. Pflanzenerna¨hr. Bodenk. 159, 541–547.
- Kro¨bel, R., Sun, Q., Ingwersen, J., Chen, X., Zhang, F., Mu¨ller, T., Ro¨mheld, V., 2010. Modelling water dynamics with DNDC and DAISY in a soil of the North China Plain: a comparative study. Environ. Model. Software 25, 583–601.
- KTBL, 2005. Faustzahlen fu¨ r die Landwirtschaft, 13th ed. Kuratorium fu¨ r Technik und Bauwesen in der Landwirtschaft, Darmstadt, Germany.
- Laville, P., Jambert, C., Cellier, P., Delmas, R., 1999. Nitrous oxide fluxes from a fertilised maize crop using micrometeorological and chamber methods. Agric. Forest Meteorol. 96, 19–38.
- Li, C.S., 2009. User's Guide for the DNDC Model (Version 9.3). Report of the Institute for the Study of Earth, Oceans and Space. (Durham, NH, USA).
- Li, H., Qiu, J., Wang, L., Tang, H., Li, C.S., Van Ranst, E., 2010. Modelling impacts of alternative farming management practices on greenhouse gas emissions from a winter wheat–maize rotation system in China. Agric. Ecosyst. Environ. 135, 24–33.
- Linn, D.M., Doran, J.W., 1984. Effect of water-filled pore space on carbon dioxide and nitrous oxide production in tilled and non-tilled soils. Soil Sci. Soc. Am. J. 48, 1267–1272.
- Mu¨ller, M.J., 1982. Selected Climatic Data for a Global Set of Standard Stations for Vegetation Science. Dr. W. Junk, The Hague.
- Parton, W.J., Holland, E.A., Del Grosso, S.J., Hartman, M.D., Martin, R.E., Mosier, A.R., Ojima, D.S., Schimel, D.S., 2001. Generalized model for NOx and N2O emissions from soils. J. Geophys. Res. 106, 17402–17419.
- Priesack, E., Gayler, S., Hartmann, H.P., 2006. The impact of crop growth sub-model choice on simulated water and nitrogen balances. Nutr. Cycl. Agroecosys. 75, 1– 13.
- Reiter, K., Schmidtke, K., Rauber, R., 2002. The influence of long-term tillage systems on symbiotic N2 fixation of pea (Pisum sativum L.) and red clover (Trifolium pratense L.). Plant Soil 238, 41–55.
- Rochette, P., 2008. No-till only increases N2O emissions in poorly-aerated soils. Soil Till. Res. 101, 97–100.
- Ruser, R., Flessa, H., Schilling, R., Beese, F., Munch, J.C., 2001. Effect of crop-specific field management and N fertilization on N2O emissions from a fine-loamy soil. Nutr. Cycl. Agroecosys. 59, 177–191.
- Schilling, G., 2000. Pflanzenerna¨hrung und Du¨ngung. UTB, Stuttgart/Deutschland.
- Smith, P., Smith, J.U., Powlson, D.S., McGill, W.B., Arah, J.R.M., Chertov, O.G., Coleman, K., Franko, U., Frolking, S., Jenkinson, D.S., Jensen, L.S., Kelly, R.H., Klein-Gunnewiek, H., Komarov, A.S., Li, C., Molina, J.A.E., Mueller, T., Parton, W.J., Thornley, J.H.M., Whitmore, A.P., 1997. A comparison of the performance of nine soil organic matter models using datasets from seven longterm experiments. Geoderma 81, 153–225.
- <span id="page-7-0"></span>Smith, W.N., Grant, B.B., Desjardins, R.L., Rochette, P., Drury, C.F., Li, C., 2008. Evaluation of two process-based models to estimate soil N2O emissions in Eastern Canada. Can. J. Soil Sci. 88, 251–260.
- Statistisches Bundesamt Deutschland, 2009. GENESIS-online. Available at: [https://](https://www-genesis.destatis.de/) [www-genesis.destatis.de](https://www-genesis.destatis.de/) (verified on the 20th of August 2009).
- Tonitto, C., David, M.B., Drinkwater, L.E., Li, C.S., 2007. Application of the DNDC model to tile-drained Illinois agroecosystems: model calibration, validation, and uncertainty analysis. Nutr. Cycl. Agroecosys. 78, 51–63.
- Ussiri, D.A.N., Lal, R., Jarecki, M.K., 2009. Nitrous oxide and methane emissions from long-term tillage under a continuous corn cropping system in Ohio. Soil Till. Res. 104, 247–255.
- Wagner-Riddle, C., Thurtell, G.W., Kidd, G.K., Beauchamp, E.G., Sweetman, R., 1997. Estimates of nitrous oxide emissions from agricultural fields over 28 months. Can. J. Soil Sci. 77, 135–144.
- WRB, 2006. World Reference Base for Soil Resources 2006. World Soil Resources Reports No. 103. FAO, Rome.