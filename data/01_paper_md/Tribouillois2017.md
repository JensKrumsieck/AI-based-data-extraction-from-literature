![](_page_0_Picture_1.jpeg)

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/11610301)

European Journal of Agronomy

![](_page_0_Picture_4.jpeg)

journal homepage: [www.elsevier.com/locate/eja](https://www.elsevier.com/locate/eja)

# Analysis and modeling of cover crop emergence: Accuracy of a static model and the dynamic STICS soil-crop model

![](_page_0_Picture_7.jpeg)

#### Hélène Tribouillois[⁎](#page-0-0) , Julie Constantin[⁎](#page-0-0) , Eric Justes[1](#page-0-1)

INRA, UMR 1248 AGIR, CS 52 627, Université de Toulouse, INPT, 31326 Castanet-Tolosan Cedex, France

# ARTICLE INFO

Keywords: Calibration Catch crop Evaluation Sowing Water

ABSTRACT

Cover crops are increasingly used in agriculture to provide a variety of ecosystem services (e.g. reducing nitrogen leaching, storing carbon in soils) during fallow periods, but it can be challenging to successfully establish them in summer, when water availability may be low. Thus, it is crucial to better quantify, understand and predict the emergence date of a variety of cover crops from multiple contexts in impact assessment studies. The objectives of this study were to 1) analyze variability in emergence dynamics among cover crops grown in fields, 2) identify variables that influence emergence the most and use them to develop a simple model to predict emergence date and 3) calibrate the STICS model to improve its predictions of cover crop emergence. STICS was chosen because it is a dynamic soil-plant model widely validated in the literature for simulating the production of cover crop services. We analyzed emergence dynamics of ten cover crop species sown under a variety of soil, climate and sowing conditions from 18 experimental sites across France. We developed and independently evaluated a static model based on these data to predict the number of days until emergence. We then calibrated STICS using the same data. Results revealed a mean emergence duration of 12 days for all species, but with high variability among experimental sites and years. The simple static model contained only three variables, with the number of consecutive days without significant water input after sowing the most significant. Overall, both the model and STICS predicted emergence date well in the calibration and validation datasets. Accurate prediction of soil moisture in the seedbed and soil water balance is a key factor to accurately predict cover crop emergence. Accurately predicting emergence of cover crops in crop models will help to assess the former's ability to provide ecosystem services in cropping systems in current and future climates.

# 1. Introduction

Cover cropping is an agroecological practice that is increasingly used in agriculture to provide a variety of ecosystem services during fallow periods (i.e. between two cash crops). They are commonly used to decrease nitrate leaching in autumn and winter and thus decrease water pollution (e.g. [Teixeira et al., 2016](#page-8-0)). They can also increase nitrogen (N) availability for the subsequent cash crop due to mineralization of cover crop residues incorporated into the soil. Legume species increase this "green manure" service by fixing atmospheric N2 ([Thorup-Kristensen et al., 2003;](#page-8-1) [Tonitto et al., 2006](#page-8-2)). In the long-term, cover crops increase organic carbon (C) and N in agricultural soil (e.g. [Poeplau and Don, 2015](#page-8-3)) and can decrease net greenhouse gas emissions to mitigate climate change ([Basche et al., 2016](#page-8-4); [Kaye and Quemada,](#page-8-5) [2017](#page-8-5)). In temperate European climates, cover crops are usually sown in summer and grow for two or more months, depending on the duration of the fallow period, which is determined by the cash-crop succession ([Justes et al., 2012](#page-8-6)). One major challenge to obtaining desired ecosystem services within a few months in regions with dry summers is to establish a cover crop with sufficient plant density in summer, when water availability in the seedbed may be low due to high temperatures, high evaporation and low rainfall ([Dorsainvil et al., 2005](#page-8-7); [Jacobsen](#page-8-8) [et al., 2010](#page-8-8)). Seedling emergence is a crucial process that depends on soil and climate conditions and species characteristics. In dry areas where water is often scarce, cover crop emergence is especially challenging because the seedbed after the preceding cash crop may be dry and the rainfall erratic during summer. Climate conditions in these areas can delay emergence of the cover crop greatly, cause it to have heterogeneous plant density or fail to establish ([Constantin et al.,](#page-8-9) [2015a](#page-8-9)). Delayed emergence can decrease greatly the ecosystem services that cover crops produce, which needs to be considered when estimating cover crop impacts. It is crucial to be able to accurately predict the date of cover crop emergence for a wide range of species, especially under summer sowing conditions. Cover crop species differ in their

<span id="page-0-0"></span>⁎ Corresponding authors.

E-mail addresses: [helene.tribouillois@inra.fr](mailto:helene.tribouillois@inra.fr) (H. Tribouillois), [julie.constantin@inra.fr](mailto:julie.constantin@inra.fr) (J. Constantin).

<span id="page-0-1"></span>1 Current address: CIRAD, UMR SYSTEM, 2 Place Pierre Viala, 34060 Montpellier, France.

<https://doi.org/10.1016/j.eja.2017.12.004>

Received 19 July 2017; Received in revised form 20 November 2017; Accepted 15 December 2017 Available online 23 December 2017

1161-0301/ © 2017 Elsevier B.V. All rights reserved.

ability to germinate under thermal and hydrological stresses. In a previous laboratory study ([Tribouillois et al., 2016](#page-8-10)), we demonstrated the diverse germination abilities of a variety of cover crop species; however, emergence under field conditions remains unexplored.

Implementing cover crops as an agroecological practice is increasingly found in the literature, and crop models are used to estimate their ability to provide ecosystem services, especially in crop rotations or under climate change scenarios ([Plaza-Bonilla et al., 2015;](#page-8-11) [Quemada](#page-8-12) [and Cabrera, 1995;](#page-8-12) [Schipanski et al., 2014;](#page-8-13) [Teixeira et al., 2016)](#page-8-0). The STICS soil-crop model is a dynamic model that simulates, at a daily time-step, crop development and C and N uptake as a function of climate conditions, permanent and initial soil characteristics, and crop management. For a wide range of soils, climates and cropping systems, studies have validated STICS predictions of water, N and C balances and, in particular, cover crop development, growth, N uptake and supply of ecosystem services related to the N cycle ([Constantin et al.,](#page-8-14) [2015b, 2012;](#page-8-14) [Justes et al., 2009;](#page-8-15) [Plaza-Bonilla et al., 2017)](#page-8-16).

This study had three objectives:

- Analyze variability in emergence dynamics among cover crop species from multiple botanical families under field conditions and a variety of sowing conditions.
- Identify variables that influence emergence duration the most and use them to develop a static model to predict emergence duration and date.
- Assess the ability of STICS to predict the date of cover crop emergence and then calibrate STICS to improve these predictions.

We first analyzed emergence dynamics of ten cover crop species grown in different experimental fields under both stress-free and, more commonly, stressful conditions in which water stress was strong enough to delay emergence. We then used general linear modeling (GLM) to develop a simple static model of emergence duration. After assessing the current accuracy of STICS in predicting cover crop emergence, we calibrated and validated its parameters to improve these predictions.

#### 2. Materials and methods

# 2.1. Field experiment

A field experiment was performed in Auzeville, France (43.53°N, 1.58°E), in 2012 to obtain key emergence data of cover crops, such as emergence duration under non-limiting water conditions and maximum percentage of emerged plants. Ten species were studied: white mustard (Sinapis alba), vetch (Vicia sativa and V. benghalensis), bristle oat (Avena strigosa), Italian ryegrass (Lolium multiflorum), crimson clover (Trifolium incarnatum), faba bean (Vicia faba), foxtail millet (Setaria italica), turnip rape (Brassica rapa), forage pea (Pisum sativum) and phacelia (Phacelia tanacetifolia). Plots of 14 m2 were sown on 16 August and irrigated on 17, 20 and 29 August (20 mm each) to optimize emergence without water stress. The sowing density was 100 plants/m2 for white mustard, 110 plants/m2 for vetch, 220 plants/m2 for bristle oat, 550 plants/m2 for Italian ryegrass, 320 plants/m2 for crimson clover, 50 plants/m2 for faba bean, 680 plants/m2 for foxtail millet, 150 plants/m2 for turnip rape, 60 plants/m2 for forage pea and 390 plants/m2 for phacelia. Emerged epicotyls along one linear meter were counted daily until the maximum percentage of emerged plants was reached. Observed data were fitted with a Gompertz function as a function of degree days to obtain continuous dynamics and compare them among species.

# 2.2. Data from previous field experiments

We analyzed emergence dynamics of the ten cover crop species sown under a wide range of soil, climate and sowing conditions at 18 experimental sites across France ([Table 1](#page-2-0)). Experiments lasted for 1–9 years depending on the site, which provided contrasting climate conditions, even for the same site. Cover crops were sown in summer or early autumn at all sites, from 1 August (day of year or DOY 213) to 2 October (DOY 275). Mean sowing depth was 3 cm (range = 1–5 cm). Mean soil moisture on the sowing date in the seedbed layer (0–10 cm) varied from 1.3% (extremely dry) to 25.9%, (close to field capacity), depending on the site and year. Daily mean temperature for 15 days after sowing ranged from 16 to 25 °C, and water input (rainfall + irrigation) within seven days of sowing ranged from 1 to 45 mm, depending on the site ([Table 1](#page-2-0)). Weather data (including air temperature and rainfall) were obtained from an automatic meteorological station inside each experimental site. The cumulative degree days were calculated from sowing (time 0) as the sum of the daily air temperature minus base temperature of each species. Soil properties varied among sites: clay content from 10 to 27%, CaCO3 from 0 to 64% and maximum water holding capacity in the seedbed layer from 13 to 48 mm. Emergence date was determined as the date when epicotyls of at least 80% of the seeds sown were visible at the soil surface. Emergence date was recorded for 53 "situations" (i.e. combinations of site × year × management) for white mustard; 31 for vetch; 20 for bristle oat; 13 for Italian ryegrass; 5 for crimson clover, faba bean, foxtail millet and turnip rape; and 4 for forage pea and phacelia.

# 2.3. Simple static model to predict emergence duration

We used the General Linear Modeling (GLM) statistical procedure to develop a simple static model to predict duration of cover crop emergence. The database of experimental field data was divided into one calibration and one validation dataset ([Table 2](#page-2-1)), each with a similar combination of sites and sowing situations (e.g. dry or wet). We calibrated the model for all ten cover crop species combined to obtain a generic model that can be used for multiple species. In contrast, we validated the model only for the four species with the largest numbers of situations: white mustard, vetch, bristle oat and Italian ryegrass.

We performed the GLM procedure with the "Modern Applied Statistics with S" package in R software (version 2.14.0). Backward stepwise regression based on Akaike's Information Criterion (StepAIC) was used to select variables for the final model. Non-significant (P > 0.05) candidate variables were excluded. Candidate variables for the model included:

- 1) climate variables: water input (rain + irrigation), potential evapotranspiration and the difference between them within 7, 14, 21 and 30 days of sowing; number of consecutive days without significant water input after sowing; and cumulative degree days 14 and 30 days after sowing (°C);
- 2) soil properties: clay content (%), CaCO3 content (%), soil moisture in the seedbed layer (%) at sowing, available soil water in the seedbed layer (mm) at sowing, and wilting point and field capacity of the seedbed layer (%);
- 3) management practice: sowing depth (cm);
- 4) species characteristics: degree days required to emerge without stress (calculated with specific species base temperature), base temperature (°C) and base water potential (MPa) for emergence ([Tribouillois et al., 2016)](#page-8-10).

If not measured, soil moisture in the seedbed at sowing was predicted by STICS based on initial soil moisture measured in the field before sowing and the subsequent daily climate. STICS has been evaluated as accurate for predicting soil moisture in the seedbed ([Constantin et al., 2015a;](#page-8-9) [Coucheney et al., 2015)](#page-8-17). Degree days required to achieve emergence were calculated from the experimental data for each species, using a base temperature of 11 °C for foxtail millet, 1.5 °C for crimson clover and 0 °C for other species [(Tribouillois et al., 2016)](#page-8-10). The species values of this parameter were calculated mostly based on the field experiment of Auzeville 2012, excepted for phacelia, bristle oat, faba bean and white mustard for which the emergence durations

#### <span id="page-2-0"></span>Table 1

Experimental site characteristics in France, climate ( ± 1 standard deviation among years), and cover crop species assessed at each site.

| Site          | Latitude (longitude) (°N<br>(°E)) | No. of<br>years | Total rainfall + irrigation within 7 days of<br>sowing (mm) | Mean daily temperature for 15 days<br>after sowing (°C) |                                |
|---------------|-----------------------------------|-----------------|-------------------------------------------------------------|---------------------------------------------------------|--------------------------------|
| St-Hilaire    | 49.2 (4.5)                        | 1               | 01 ± 0                                                      | 20 ± 0                                                  | Cl/Fa/Mi/Oa/Pe/Ph/Ry/<br>Tu/Ve |
| Montpellier   | 43.6 (3.9)                        | 2               | 02 ± 1                                                      | 20 ± 1                                                  | Mu/Oa/Ve                       |
| Boult         | 49.4 (4.1)                        | 1               | 05 ± 0                                                      | 17 ± 0                                                  | Mu                             |
| Bignan        | 47.9 (−2.8)                       | 3               | 06 ± 2                                                      | 18 ± 1                                                  | Cl/Fa/Mi/Oa/Pe/Ry/Tu/          |
|               |                                   |                 |                                                             |                                                         | Ve                             |
| Estrées-Mons  | 49.9 (3.0)                        | 2               | 06 ± 7                                                      | 16 ± 2                                                  | Mu/Ve                          |
| La-Chapelle   | 47.4 (−1.0)                       | 2               | 11 ± 17                                                     | 19 ± 0                                                  | Mu/Ve                          |
| Vienne-en-Val | 47.8 (2.1)                        | 2               | 13 ± 3                                                      | 17 ± 1                                                  | Mu/Oa/Ve                       |
| Warmeriville  | 49.3 (4.2)                        | 2               | 14 ± 9                                                      | 17 ± 4                                                  | Mu/Ry/Ve                       |
| Chéry         | 49.7 (3.6)                        | 1               | 16 ± 0                                                      | 17 ± 0                                                  | Mu/Oa/Ve                       |
| Somme         | 49.1 (4.7)                        | 1               | 16 ± 0                                                      | 18 ± 0                                                  | Mu                             |
| Sermaise      | 48.5 (2.1)                        | 2               | 16 ± 15                                                     | 16 ± 2                                                  | Mu/Oa/Ve                       |
| Boigneville   | 48.3 (2.4)                        | 6               | 19 ± 16                                                     | 18 ± 1                                                  | Mu/Ry/Ve                       |
| Lyon          | 45.8 (4.8)                        | 1               | 20 ± 0                                                      | 25 ± 0                                                  | Ve                             |
| Orchies       | 50.5 (3.2)                        | 2               | 23 ± 19                                                     | 18 ± 2                                                  | Mu/Oa/Ve                       |
| Auzeville     | 43.5 (1.5)                        | 9               | 24 ± 20                                                     | 20 ± 2                                                  | Cl/Fa/Mi/Mu/Oa/Ph/Pe/          |
|               |                                   |                 |                                                             |                                                         | Ry/Tu/Ve                       |
| Lusignan      | 46.4 (0.1)                        | 4               | 27 ± 36                                                     | 16 ± 2                                                  | Mu/Oa/Ry/Ve                    |
| La Pouëze     | 47.6 (−0.8)                       | 2               | 44 ± 33                                                     | 18 ± 1                                                  | Mu/Oa/Ve                       |
| Colmar        | 48.1 (7.4)                        | 1               | 45 ± 0                                                      | 19 ± 0                                                  | Ry                             |

<span id="page-2-2"></span>* Cl is 'crimson clover', Fa is 'faba bean', Mi is 'foxtail millet', Mu is 'white mustard', Oa is 'bristle oat', Ph is 'phacelia', Pe is 'forage pea', Ry is 'Italian ryegrass', Tu is 'turnip rape' and Ve is 'vetch'.

2.4. Calibration and validation of STICS for cover crop emergence

STICS model simulates emergence duration by taking into account three main factors: temperature, water status of the soil in the seedbed and sowing depth. STICS predicts emergence as three successive processes: 1) seed imbibition, 2) germination and 3) shoot elongation. Temperature, soil moisture and species parameters (i.e. i) sensitivity to water as base water potential, ii) thermal stresses, and iii) shoot elongation) determine the emergence date. The first step is a passive process influenced by the species-specific water potential in the seedbed, which determines seed imbibition. Once seeds are moistened, rootlets emerge from seeds within a few days, as a function of temperature. Each species completes germination once it has accumulated a species-specific number of degree days after sowing. STICS model takes into account the variability of soil temperature according to sowing depth since the germination is function of soil temperature in the seedbed in the model, the seedbed depth being defined as sowing depth + 1 cm. Sensitivity of seed rootlets to soil dryness (drought and base temperature) also

were shorter in other experimental fields of the database (e.g. thermic stress for phacelia…) where we thus calculated the parameter value based on measurements. Base temperatures and water potentials were determined in the laboratory for all species ([Tribouillois et al., 2016](#page-8-10)). Minimum and base temperature represent both the same process (minimal temperature at which species can germinate) but not using the same equation, such as a classical linear equation for base temperature and a non-linear function for the minimum temperature of germination (see [Tribouillois et al., 2016](#page-8-10) for details). The method used for minimum temperature allows a more accurate estimation due to the fact the response of germination to the temperature increase is not linear. We thus chose to use minimum temperatures as base temperatures (instead of the base temperatures themselves). The temperature used to calculate degree days was air temperature, since we did not have measurements of the temperature in the seedbed for all experiments and that the air temperature was close to the seedbed temperature, as shown by [Dorsainvil et al. (2005)](#page-8-7) for cover crop sowing in summer conditions.

### <span id="page-2-1"></span>Table 2

Ranges of site, soil, and weather data for ten species in calibration and validation datasets.

|             | Characteristic                                                                                                                                                                                                              | White<br>mustard                                            | Vetch                                                       | Bristle oat                                                  | Italian ryegrass                                          | Crimson clover, Faba bean Phacelia Forage<br>pea, Foxtail millet, Turnip rape |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------|
| Calibration | Number of situations*<br>Sowing date<br>Initial soil moisture (%)<br>Soil moisture at sowing (%)<br>Rainfall + irrigation within 7 days of sowing<br>(mm)<br>Number of consecutive days without water<br>input after sowing | 14<br>3 Aug–21 Sept<br>7.4–20.3<br>4.6–24.2<br>0–47<br>0–20 | 13<br>1 Aug–23 Sept<br>7.2–22.4<br>1.3–21.9<br>0–58<br>1–32 | 8<br>10 Aug–16 Sept<br>11.2–30.0<br>5.8–24.2<br>1–41<br>1–33 | 8<br>6 Aug–2 Oct<br>10.8–25.9<br>8.9–22.4<br>0–28<br>0–33 | 5<br>10–22 Aug<br>11.2–30.0<br>8.9–24.2<br>1–41<br>1–33                       |
| Validation  | Number of situations*<br>Sowing date<br>Initial soil moisture (%)<br>Soil moisture at sowing (%)<br>Rainfall + irrigation within 7 days of sowing<br>(mm)<br>Number of consecutive days without water<br>input after sowing | 39<br>5 Aug–12 Sept<br>3.7–25.9<br>4.3–25.9<br>0–80<br>0–25 | 18<br>5 Aug–12 Sept<br>4.8–30.0<br>4.4–24.2<br>1–79<br>1–33 | 12<br>5 Aug–12 Sept<br>10.0–19.0<br>4.8–21.6<br>1–80<br>1–22 | 5<br>10–27 Aug<br>11.2–20.7<br>11.0–22.7<br>8–45<br>1–7   | N/A<br>N/A<br>N/A<br>N/A<br>N/A<br>N/A                                        |

<span id="page-2-3"></span>* The number of "situations" (site × year × management) corresponds to the number of simulations.

influences germination. Subsoil plantlet growth begins after germination, as shoots and roots begin to grow; elongation of the former is a logistic function of degree days that may slow down with unsuitable soil moisture. The emergence occurs when elongation is greater than sowing depth. [Brisson et al. (2008)](#page-8-18) describe all processes and equations of STICS. Since STICS does not consider certain biotic and abiotic processes that cause plant density to decrease (e.g. damping-off, low seed germination), sowing density was considered to equal the density of emerged plants measured in the experiments at Auzeville.

For calibrating cover crops in STICS, we first fixed the parameters values for water potential and germination base temperature taken from a previous laboratory study of multiple cover crop species ([Tribouillois et al., 2016](#page-8-10)). Likewise, degree days required for germination were calculated from that study's data. The temperature used to calculate degree days was air temperature as a proxy of seedbed temperature. Root sensitivity to drought and two shoot elongation parameters were mathematically calibrated using the method of [Guillaume](#page-8-19) [et al. (2011)](#page-8-19) as a simplex algorithm adapted to non-smooth functions in the OptimiSTICS tool ([Wallach et al., 2011](#page-8-20)).

STICS was calibrated using the same calibration dataset as that used to develop the static model, representing a wide range of conditions across France. Unlike the static model, STICS was calibrated for each species by considering species-specific parameters. STICS' predicted emergence dates were evaluated using the same validation dataset as that used to evaluate the static model ([Table 2](#page-2-1)). The model was initialized with soil moisture in the seedbed layer and just below (0–10 cm measured on experimental sites on the sowing date) and with the corresponding sowing depth practiced on experimental sites: mean sowing depth of 3 cm (range = 1–5 cm).

#### 2.5. Statistical criteria used for calibration and evaluation

Three statistical criteria – model efficiency (EF), root mean square error (RMSE) and mean deviation (MD) – were calculated to assess the quality of calibration and validation:

$$EF = 1 - \frac{\sum_{l=1}^{n} \text{ (
$$P_l - O_l$$
)}^2}{\sum_{l=1}^{n} \text{ (
$$O_l - \overline{o}$$
)}^2} \tag{1}$$

$$RMSE = \sqrt{\frac{1}{n}} \sum_{l=1}^{n} \text{ (
$$P_l - O_l$$
)}^2 \tag{2}$$

$$MD = \frac{1}{n} \sum_{l=1}^{n} \text{ (
$$P_l - O_l$$
)}\tag{3}$$

where n is the number of observations, Oi and Pi are observed and predicted values, respectively, and *o* is the mean of observed values. EF (ranges = −∞ to 1) represents model accuracy relative to the mean of observed data. As it approaches 1, the match between observed and predicted values increases; it becomes negative when the mean of observed values lies closer to observed values than predicted values do. RMSE provides absolute error, while MD provides model deviation from the line x=y. We also calculated the median difference in absolute values between the observed and the predicted values.

#### 3. Results

# 3.1. Experimental field emergence under optimal conditions

In the Auzeville experiment, species showed high variability in emergence dynamics ([Fig. 1)](#page-4-0). Under these conditions we distinguished species with short emergence durations, such as crimson clover and turnip rape (6 days to reach maximum emergence) from those with long emergence durations, such as phacelia, faba bean and bristle oat (> 13 days to reach maximum emergence). Maximum percentage of emerged plants differed among species because three of them had low emergence: phacelia (23%), foxtail millet (33%), and Italian ryegrass (48%).

# 3.2. Experimental field emergence under contrasting conditions

For all species combined, mean and median emergence durations were 12 and 9.5 days, respectively; emergence duration being the number of days from sowing to emergence. Median emergence duration among different experimental sites ranged from 7 to 8 days for turnip rape and crimson clover to 12 days for faba bean and phacelia ([Fig. 2](#page-4-1)). Emergence duration tended to vary greatly among experimental sites and years (e.g. 4–38 days for purple). The four species with the largest sample sizes (white mustard, vetch, bristle oat, and Italian ryegrass) had the highest variability in emergence duration. Emergence duration varied greatly among situations except for Italian ryegrass, which had the longest mean duration and no extremely long duration. The shortest durations were observed for vetch (4 days); turnip rape and bristle oat (5 days); and crimson clover, white mustard and foxtail millet (6 days). Emergence dates depended on emergence duration and sowing date, which differed among species due to the multiple experimental sites.

#### 3.3. Simple static model to predict emergence duration

Applying GLM to the calibration dataset identified three influential variables for the simple static model to predict emergence duration:

Emergence duration 6.9 0.29 0.44 0.03 =− × + × + × *SM DWR DDe*

where SM is soil moisture (%) in the seedbed layer at sowing, DWR is the number of consecutive days without significant water input (daily rainfall or irrigation < 3 mm) after sowing and "DDe" is the number of degree days required for each species to emerge without stress. The values of DDe for each species are given in Appendix. According to the GLM, DWR, SM and DDe were significant (P < 0.001, =0.001 and =0.05, respectively) and explained 52%, 6% and 4% of the variability, respectively.

For predicted emergence duration with the calibration dataset, the model obtained EF of 0.57, RMSE of 4.6 days and MD of 0.3 days ([Fig. 3](#page-4-2)a). The model predicted both long and short durations ranging from 4 to 27 days. The model predicted most situations well (mean difference between observed and predicted durations = 3.5 days) but underpredicted the longest observed emergence by 15.7 days. For predicted emergence date with the calibration dataset, the model obtained EF of 0.91 ([Fig. 3](#page-4-2)b), ranging from early emergence (11 August or DOY 223) to late (11 October or DOY 284).

The static model predicted emergence duration and date nearly as well with the validation dataset, obtaining EF of 0.47 and 0.91, respectively, RMSE of 4.6 days for both and MD of 0.4 days for both ([Fig. 4](#page-5-0)a and b). Predictions of long and short emergence durations ranged from 5 to 25 days (mean difference between observed and predicted durations = 3.5 days). As with the calibration dataset, the longest durations observed (26, 25 and 30 days) in the validation dataset were underpredicted the most (by 13.6, 12.8 and 11.9 days, respectively) ([Fig. 4](#page-5-0)a). The static model predicted early and late emergence dates from the validation dataset well in summer and early autumn ([Fig. 4](#page-5-0)b).

For the four species individually, the static model predicted emergence date well with the validation dataset ([Fig. 5](#page-5-1)). For bristle oat and Italian ryegrass, it obtained EF of 0.98 for both and a mean difference between observed and predicted dates of 1.2 and 2.6 days, respectively (maximum difference = 4.4 and 4.6 days, respectively). For white mustard and vetch, it obtained EF of 0.88 and 0.80, respectively, and a mean difference between observed and predicted dates of 3.7 and 4.7 days, respectively

3.4. STICS prediction of emergence

grass', Tu is 'turnip rape' and Ve is 'vetch'.

Calibrating STICS significantly increased the accuracy of its pre-

<span id="page-4-1"></span>Fig. 2. Emergence duration after sowing in the experimental field database for each cover crop species. Error bars represent a standard deviation of the variability among experimental sites and years. Cl is 'crimson clover', Fa is 'faba bean', Mi is 'foxtail millet', Mu is 'white mustard', Oa is 'bristle oat', Ph is 'phacelia', Pe is 'forage pea', Ry is 'Italian rye-

<span id="page-4-0"></span>![](_page_4_Figure_1.jpeg)

Fig. 1. Observed emergence dynamics (points) in days after sowing for the ten cover crop species in the irrigated experimental field in Auzeville, France, in 2012. Lines are fitted curves.

![](_page_4_Figure_4.jpeg)

As a result, the calibrated STICS obtained EF for emergence date of at least 0.80 for all species, except foxtail millet, faba bean and phacelia, mainly due to their small sample size (n = 4) ([Fig. 7](#page-6-1)).

With the validation dataset, STICS predicted emergence dates of the four species combined relatively well, with EF of 0.84 ([Fig. 8](#page-7-0)), which was as high as that with the calibration dataset. STICS predicted both early and late emergence dates well, with a mean difference between observed and predicted emergence dates of 4 days (maximum difference = 19 days for one white mustard situation). When predicting emergence duration with the validation dataset, STICS had low EF (0.07) and low MD (0.3) but was able to predict well short and long durations that ranged from 4 to 34 days. Species with the highest observed variability in emergence duration, such as white mustard, vetch and bristle oat, had the highest predicted variability, but STICS predicted their emergence dates well [(Fig. 7](#page-6-1)e–g), with EF greater than 0.77.

# 4. Discussion

# 4.1. Species emergence variability and influences on model accuracy

![](_page_4_Figure_9.jpeg)

Cover crop emergence is a crucial process that directly influences

Fig. 3. Observations versus predictions of the static model for a) emergence duration and b) emergence date (day of year or DOY) for all cover crop species based on the calibration dataset (n = 72). Dashed lines represent y = x, while solid lines represent linear regression. 'EF' is the model efficiency, "RMSE" is the root mean square error and "MD" is the mean deviation.

<span id="page-4-2"></span>dictions of emergence date for all species (calibrated parameter values in the Appendix), greatly decreasing differences between observed and predicted dates ([Fig. 6](#page-6-0)). Mean difference between observed and

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

Fig. 4. Observations versus predictions of the static model for a) emergence duration and b) emergence date (day of year or DOY) for all cover crop species based on the validation dataset (n = 74). Dashed lines represent y = x, while solid lines represent linear regression. "EF" is the model efficiency, "RMSE" is the root mean square error and "MD" is the mean deviation.

cover establishment and thus the production of ecosystem services. Our results, representing multiple experimental fields with contrasting soil, climate data and sowing dates, show that emergence duration varied greatly depending on situations of each species. This is consistent with results of [Dorsainvil et al. (2005)](#page-8-7), who observed that emergence duration of white mustard lasted from 5 days to several weeks. We found that crucifer species (e.g. white mustard) tended to have short emergence durations, which is consistent with a previous laboratory study on cover crop germination ([Tribouillois et al., 2016](#page-8-10)). This indicates that crucifer species are generally well adapted to late summer

<span id="page-5-1"></span>![](_page_5_Figure_6.jpeg)

Fig. 5. Observed versus predicted emergence dates (day of year or DOY) of cover crop species using the static model based on the validation dataset. Dashed lines represent y = x, while solid lines represent linear regression. "EF" is model efficiency, "RMSE" is root mean square error and "MD" is mean deviation.

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

Fig. 6. Distribution of differences between observed and predicted emergence dates with the calibration dataset using a) the original set of parameters (before calibration) and b) the new set of parameters (after calibration).

sowing, even under dry conditions, because they can germinate and emerge in a few days after rainfall or in moderately wet seedbeds. Conversely, legumes such as faba bean had longer emergence durations due to slower seed imbibition caused by their large seeds. Phacelia also tended to have longer emergence durations, probably because its thick waxy cuticle makes it sensitive to high temperatures and water stress (due to low water potential) at sowing ([Tribouillois et al., 2016)](#page-8-10). Species-specific sensitivities to temperature and water availability at sowing may explain the large variability in emergence duration observed among experimental fields. Temperature and water availability are the main drivers of germination and emergence and are widely represented in models by base temperature and base water potential, respectively ([Dürr et al., 2015](#page-8-21); [Gonzalez-Andujar et al., 2016;](#page-8-22) [Renzi](#page-8-23) [et al., 2017](#page-8-23)). The Auzeville experiment in 2012 allowed all species to be compared at the same time under similar soil conditions. Although most species had high maximum percentages of emerged plants (80–100%), some had percentages below 50%, indicating a final plant density much lower than expected. This low emergence can be explained by lowquality seed lots (e.g. high variability in emergence potential, presence of hard seeds…) ([Uzun and Aydin, 2004](#page-8-24)), which must be considered in simulations to accurately predict plant density.

<span id="page-6-1"></span>It is necessary to consider the main drivers of variability in

emergence observed among cover crop species in the field to accurately predict emergence dates under a wide range of conditions. In our study, the emergence duration was driven by the number of degree days required to reach emergence (static model) or germination (STICS). In STICS, parameters for species sensitivity to temperature and water availability were used as plant parameters. Consequently, STICS was parametrized for each species, while the static model was developed for all cover crop species but has one species-specific parameter that considers species behavior as degree days to emerge.

#### 4.2. Water availability: main driver of emergence

The simple static model was built from several management, soil and climate variables. Of these, water availability variables (two of the model's three variables) had the greatest influence on its emergence predictions. This influence is consistent with other crop emergence models, which identify soil water potential as particularly important for predicting crop emergence ([Bullied et al., 2012](#page-8-25)). In weed science, several emergence models based mainly on degree-day and hydrothermal time have been developed ([Guillemin et al., 2013](#page-8-26); [Martinson](#page-8-27) [et al., 2007](#page-8-27); [Renzi et al., 2017](#page-8-23)). The most influential variable was the number of consecutive days without significant rain or irrigation after

![](_page_6_Figure_9.jpeg)

Fig. 7. Observed versus predicted emergence dates (day of year or DOY) of cover crop species using the STICS soil-crop model based on the (a-b-c-d) calibration dataset and (e-f-g) validation dataset. Dashed lines represent y = x. "EF" is model efficiency, "RMSE" is root mean square error and "MD" is mean deviation.

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

Fig. 8. Observed versus predicted a) emergence duration and b) emergence date (day of year or DOY) for all cover crop species using the STICS soil-crop model based on the validation dataset (n = 74). Dashed lines represent y = x, while solid lines represent linear regression for all species combined. "EF" is "efficiency", "RMSE" is "root mean scare error" and "MD" is "mean deviation".

sowing, of which the former can be calculated from easily available climate data. The second most influential variable was soil moisture at sowing, which although not always available, is simple to measure in the seedbed or to estimate using a dynamic model, such as STICS. Even without this variable, the static model predicts emergence date well (results not shown), since soil moisture at sowing had much less variability in our database than rainfall or irrigation after sowing. This is consistent with [Constantin et al. (2015a)](#page-8-9), who predicted cover crop emergence with the mechanistic emergence model SIMPLE. They found that water stress was the main cause of delayed emergence in summer under temperate French conditions. This high sensitivity of emergence earliness to water availability indicates the need to adapt the sowing date to weather conditions by closely monitoring rainfall forecasts. However, the sowing date also depends strongly on when the preceding cash crop was harvested; thus, it cannot always occur during the most suitable weather period. Irrigating cover crops after sowing could help ensure sufficient cover crop establishment to provide optimum production of ecosystem services during fallow periods.

#### 4.3. Two complementary emergence-modeling approaches

We developed two modeling approaches that accurately predicted emergence dates of cover crops. One was based on statistical modeling, which has the advantage of being simple to use for many users and requiring few input data. The model developed could be integrated into simple empirical soil-crop models as an emergence module without greatly increasing the number of parameters. Another potential use is as a stand-alone model to study cover crop emergence under contrasting conditions. In contrast, improving the emergence module of STICS was particularly useful, because the model can predict 1) impacts of cover crops beyond emergence, growth and resource acquisition during fallow periods and 2) some ecosystem services (N, C and water) produced by cover crops under a wide range of conditions. Nevertheless, both modeling approaches predicted emergence dates with similar accuracy, with most differences between observed and predicted dates being less than 5 days. The static model, however, tended to underestimate long emergence durations and could continue to underpredict them outside of our database. Underestimates could be due to the coefficients and variables in the static model and the fact that the calibration dataset included mainly short emergence durations; its did not have enough long emergence durations to influence parameter values greatly. In contrast, STICS predicted durations with low deviation, probably because its emergence module is dynamic and more processbased. But STICS predictions are sensitive to initial soil conditions, especially soil moisture of the seedbed. Dry weather could explain some of the variability in its predicted emergence durations. The observed data, however, may have had some inaccuracies due to factors such as 1) spatial variability in experimental fields as soil surface structure and low accuracy in measuring sowing depth and soil moisture in the seedbed, 2) too few observations to determine exact dates of emergence, and 3) variability of determining dates of emergence among observers. Moreover, cover crops can experience biotic stress such as damping-off ([Dorsainvil et al., 2005](#page-8-7)) or pest damage ([Ichihara et al.,](#page-8-28) [2011](#page-8-28)), which was not always accurately measured in the experiments in our database. Few empirical data are available on emergence, especially for cover crops, which limits progress in modeling emergence date and emerged plant density. Thus, future studies are needed to obtain more data on crop emergence, which strongly influences crop establishment.

#### 5. Conclusion

Emergence dates of cover crop species were predicted well by developing a simple static model and calibrating the STICS process-based soil-crop model. Emergence is particularly crucial for cover crop establishment, especially in dry areas. Since water availability influences emergence the most, accurate measurement or prediction of soil moisture in the seedbed or soil water balance is key to accurately predicting cover crop emergence, which is essential to assess the ability of cover crops to provide ecosystem services in cropping systems in current and future climates.

#### Acknowledgments

This research was supported by the French ADEME agency (REACTIF program) which granted the CiCC project and the Adour-Garonne Water Agency through funding for supporting the BAG'AGES project. We thank those who produced or made available the data used in this study, from INRA, Arvalis – Institut du Végétal and GEVES project (CASDAR program). We thank M.L. and M.S. Corson for improving the English in the manuscript.

# Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at <https://doi.org/10.1016/j.eja.2017.12.004>.

#### References

- <span id="page-8-4"></span>Basche, A.D., Archontoulis, S.V., Kaspar, T.C., Jaynes, D.B., Parkin, T.B., Miguez, F.E., 2016. Simulating long-term impacts of cover crops and climate change on crop production and environmental outcomes in the Midwestern United States. Agric. Ecosyst. Environ. 218, 95–106. <http://dx.doi.org/10.1016/j.agee.2015.11.011>.
- <span id="page-8-18"></span>[Brisson, N., Launay, M., Mary, B., Beaudoin, N., 2008. Conceptual basis, formalisations](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0010) [and parameterization of the STICS crop model, Quae edition. Versailles, France, ISBN](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0010) [978-2-7592-0 290-4, 171p.](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0010)
- <span id="page-8-25"></span>Bullied, W.J., van Acker, R.C., Bullock, P.R., 2012. Hydrothermal modeling of seedling emergence timing across topography and soil depth. Agron. J. 104, 423–436. [http://](http://dx.doi.org/10.2134/agronj2011.0257) [dx.doi.org/10.2134/agronj2011.0257.](http://dx.doi.org/10.2134/agronj2011.0257)
- Constantin, J., Beaudoin, N., Launay, M., Duval, J., Mary, B., 2012. Long-term nitrogen dynamics in various catch crop scenarios: test and simulations with STICS model in a temperate climate. Agric. Ecosyst. Environ. 147, 36–46. [http://dx.doi.org/10.1016/j.](http://dx.doi.org/10.1016/j.agee.2011.06.006) [agee.2011.06.006.](http://dx.doi.org/10.1016/j.agee.2011.06.006)
- <span id="page-8-9"></span>Constantin, J., Dürr, C., Tribouillois, H., Justes, E., 2015a. Catch crop emergence success depends on weather and soil seedbed conditions in interaction with sowing date: a simulation study using the SIMPLE emergence model. Field Crop Res. 176, 22–33. [http://dx.doi.org/10.1016/j.fcr.2015.02.017.](http://dx.doi.org/10.1016/j.fcr.2015.02.017)
- <span id="page-8-14"></span>Constantin, J., Le Bas, C., Justes, E., 2015b. Large-scale assessment of optimal emergence and destruction dates for cover crops to reduce nitrate leaching in temperate conditions using the STICS soil–crop model. Eur. J. Agron. 69, 75–87. [http://dx.doi.org/](http://dx.doi.org/10.1016/j.eja.2015.06.002) [10.1016/j.eja.2015.06.002.](http://dx.doi.org/10.1016/j.eja.2015.06.002)
- <span id="page-8-17"></span>Coucheney, E., Buis, S., Launay, M., Constantin, J., Mary, B., Ripoche, D., Beaudoin, N., Ruget, F.F., Garcia de Cortazar, I., Andrianarisoa, S., Justes, E., Léonard, J., García de Cortázar-Atauri, I., Ripoche, D., Beaudoin, N., Ruget, F.F., Andrianarisoa, K.S., Le Bas, C., Justes, E., Léonard, J., 2015. Accuracy, robustness and behavior of the STICS v-8 soil-crop model for plant, water and nitrogen outputs: evaluation over a wide range of agro-environmental conditions. Environ. Model. Softw. 64, 177–190. [http://](http://dx.doi.org/10.1016/j.envsoft.2014.11.024)
- <span id="page-8-21"></span>[dx.doi.org/10.1016/j.envsoft.2014.11.024.](http://dx.doi.org/10.1016/j.envsoft.2014.11.024) Dürr, C., Dickie, J.B., Yang, X.-Y., Pritchard, H.W., 2015. Ranges of critical temperature
- and water potential values for the germination of species worldwide: contribution to a seed trait database. Agric. For. Meteorol. 200, 222–232. [http://dx.doi.org/10.](http://dx.doi.org/10.1016/j.agrformet.2014.09.024) [1016/j.agrformet.2014.09.024.](http://dx.doi.org/10.1016/j.agrformet.2014.09.024)
- <span id="page-8-7"></span>Dorsainvil, F., Dürr, C., Justes, E., Carrera, A., 2005. Characterisation and modelling of white mustard (Sinapis alba L.) emergence under several sowing conditions. Eur. J. Agron. 23, 146–158. [http://dx.doi.org/10.1016/j.eja.2004.11.002.](http://dx.doi.org/10.1016/j.eja.2004.11.002)
- <span id="page-8-22"></span>Gonzalez-Andujar, J.L., Chantre, G.R., Morvillo, C., Blanco, A.M., Forcella, F., Freckleton, R., 2016. Predicting field weed emergence with empirical models and soft computing techniques. Weed Res. 56, 415–423. [http://dx.doi.org/10.1111/wre.12223.](http://dx.doi.org/10.1111/wre.12223)
- <span id="page-8-19"></span>Guillaume, S., Bergez, J.-E.E., Wallach, D., Justes, E., 2011. Methodological comparison of calibration procedures for durum wheat parameters in the STICS model. Eur. J. Agron. 35, 115–126. [http://dx.doi.org/10.1016/j.eja.2011.05.003.](http://dx.doi.org/10.1016/j.eja.2011.05.003)
- <span id="page-8-26"></span>Guillemin, J.-P., Gardarin, A., Granger, S., Reibel, C., Munier-Jolain, N., Colbach, N., 2013. Assessing potential germination period of weeds with base temperatures and base water potentials. Weed Res. 53, 76–87. [http://dx.doi.org/10.1111/wre.12000.](http://dx.doi.org/10.1111/wre.12000)
- <span id="page-8-28"></span>Ichihara, M., Maruyama, K., Yamashita, M., Sawada, H., Inagaki, H., Ishida, Y., Asai, M., 2011. Quantifying the ecosystem service of non-native weed seed predation provided by invertebrates and vertebrates in upland wheat fields converted from paddy fields. Agric. Ecosyst. Environ. 140, 191–198. [http://dx.doi.org/10.1016/j.agee.2010.12.](http://dx.doi.org/10.1016/j.agee.2010.12.002) [002](http://dx.doi.org/10.1016/j.agee.2010.12.002).
- <span id="page-8-8"></span>Jacobsen, K.L., Gallagher, R.S., Burnham, M., Bradley, B.B., Larson, Z.M., Walker, C.W., Watson, J.E., 2010. Mitigation of seed germination impediments in hairy vetch. Agron. J. 102, 1346–1351. <http://dx.doi.org/10.2134/agronj2010.0002n>.
- <span id="page-8-15"></span>Justes, E., Mary, B., Nicolardot, B., 2009. Quantifying and modelling C and N mineralization kinetics of catch crop residues in soil: parameterization of the residue

#### decomposition module of STICS model for mature and non mature residues. Plant Soil 325, 171–185. <http://dx.doi.org/10.1007/s11104-009-9966-4>.

- <span id="page-8-6"></span>[Justes, E., Beaudoin, N., Bertuzzi, P., Charles, R., Constantin, J., Dürr, C., Hermon, C.,](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0080) [Joannon, A., Le Bas, C., Mary, B., Mignolet, C., Montfort, F., Ruiz, L., Sarthou, J.-P.,](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0080) [Souchère, V., Tournebize, J., Savini, I., Réchauchère, O., 2012. The use of cover crops](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0080) to reduce nitrate leaching: eff[ect on the water and nitrogen balance and other eco](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0080)[system services. In: The International Fertiliser Society Meeting. Cambridge. pp.](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0080) 4–[43.](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0080)
- <span id="page-8-5"></span>Kaye, J.P., Quemada, M., 2017. Using cover crops to mitigate and adapt to climate change. A review. Agron. Sustain. Dev. 37, 4. [http://dx.doi.org/10.1007/s13593-](http://dx.doi.org/10.1007/s13593-016-0410-x) [016-0410-x.](http://dx.doi.org/10.1007/s13593-016-0410-x)
- <span id="page-8-27"></span>Martinson, K., Durgan, B., Forcella, F., Wiersma, J., Spokas, K., Archer, D., 2007. An emergence model for wild oat (Avena fatua). Weed Sci. 55, 584–591. [http://dx.doi.](http://dx.doi.org/10.1614/WS-07-059.1) [org/10.1614/WS-07-059.1.](http://dx.doi.org/10.1614/WS-07-059.1)
- <span id="page-8-11"></span>Plaza-Bonilla, D., Nolot, J.M., Raffaillac, D., Justes, E., 2015. Cover crops mitigate nitrate leaching in cropping systems including grain legumes: field evidence and model simulations. Agric. Ecosyst. Environ. 212, 1–12. [http://dx.doi.org/10.1016/j.agee.](http://dx.doi.org/10.1016/j.agee.2015.06.014) [2015.06.014.](http://dx.doi.org/10.1016/j.agee.2015.06.014)
- <span id="page-8-16"></span>Plaza-Bonilla, D., Léonard, J., Peyrard, C., Mary, B., Justes, E., 2017. Precipitation gradient and crop management affect N2O emissions: simulation of mitigation strategies in rainfed Mediterranean conditions. Agric. Ecosyst. Environ. 238, 89–103. [http://dx.](http://dx.doi.org/10.1016/j.agee.2016.06.003) [doi.org/10.1016/j.agee.2016.06.003.](http://dx.doi.org/10.1016/j.agee.2016.06.003)
- <span id="page-8-3"></span>Poeplau, C., Don, A., 2015. Carbon sequestration in agricultural soils via cultivation of cover crops—a meta-analysis. Agric. Ecosyst. Environ. 200, 33–41. [http://dx.doi.org/](http://dx.doi.org/10.1016/j.agee.2014.10.024) [10.1016/j.agee.2014.10.024.](http://dx.doi.org/10.1016/j.agee.2014.10.024)
- <span id="page-8-12"></span>[Quemada, M., Cabrera, M.L., 1995. CERES-N model predictions of nitrogen mineralized](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0110) [from cover crop residues. Soil Sci. Soc. Am. J. 59, 1059](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0110)–1065.
- <span id="page-8-23"></span>Renzi, J.P., Chantre, G.R., Cantamutto, M.A., 2017. Vicia villosa ssp. villosa Roth field emergence model in a semiarid agroecosystem. Grass Forage Sci. 0, 1–13. [http://dx.](http://dx.doi.org/10.1111/gfs.12295) [doi.org/10.1111/gfs.12295.](http://dx.doi.org/10.1111/gfs.12295)
- <span id="page-8-13"></span>Schipanski, M.E., Barbercheck, M., Douglas, M.R., Finney, D.M., Haider, K., Kaye, J.P., Kemanian, A.R., Mortensen, D. a., Ryan, M.R., Tooker, J., White, C., 2014. A framework for evaluating ecosystem services provided by cover crops in agroecosystems. Agric. Syst. 125, 12–22. [http://dx.doi.org/10.1016/j.agsy.2013.11.004.](http://dx.doi.org/10.1016/j.agsy.2013.11.004)
- <span id="page-8-0"></span>Teixeira, E.I., Johnstone, P., Chakwizira, E., de Ruiter, J., Malcolm, B., Shaw, N., Zyskowski, R., Khaembah, E., Sharp, J., Meenken, E., Fraser, P., Thomas, S., Brown, H., Curtin, D., 2016. Sources of variability in the effectiveness of winter cover crops for mitigating N leaching. Agric. Ecosyst. Environ. 220, 226–235. [http://dx.doi.org/](http://dx.doi.org/10.1016/j.agee.2016.01.019) [10.1016/j.agee.2016.01.019.](http://dx.doi.org/10.1016/j.agee.2016.01.019)
- <span id="page-8-1"></span>[Thorup-Kristensen, K., Magid, J., Jensen, L.S., 2003. Catch crops and green manures as](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0130) [biological tools in nitrogen management in temperate zones. Adv. Agron. 79,](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0130) 227–[302.](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0130)
- <span id="page-8-2"></span>Tonitto, C., David, M.B.B., Drinkwater, L.E.E., 2006. Replacing bare fallows with cover crops in fertilizer-intensive cropping systems: a meta-analysis of crop yield and N dynamics. Agric. Ecosyst. Environ. 112, 58–72. [http://dx.doi.org/10.1016/j.agee.](http://dx.doi.org/10.1016/j.agee.2005.07.003) [2005.07.003.](http://dx.doi.org/10.1016/j.agee.2005.07.003)
- <span id="page-8-10"></span>Tribouillois, H., Dürr, C., Demilly, D., Wagner, M., Justes, E., 2016. Determination of germination response to temperature and water potential for a wide range of cover crop species and related functional groups. PLoS One 11, e0161185. [http://dx.doi.](http://dx.doi.org/10.1371/journal.pone.0161185) [org/10.1371/journal.pone.0161185.](http://dx.doi.org/10.1371/journal.pone.0161185)
- <span id="page-8-24"></span>[Uzun, F., Aydin, I., 2004. Improving germination rate of Medicago and Trifolium species.](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0145) [Asian J. Plant Sci. 3, 714](http://refhub.elsevier.com/S1161-0301(17)30185-5/sbref0145)–717.
- <span id="page-8-20"></span>Wallach, D., Buis, S., Lecharpentier, P., Bourges, J., Clastre, P., Launay, M., Bergez, J.- E.E., Guerif, M., Soudais, J., Justes, E., 2011. A package of parameter estimation methods and implementation for the STICS crop-soil model. Environ. Model. Softw. 26, 386–394. [http://dx.doi.org/10.1016/j.envsoft.2010.09.004.](http://dx.doi.org/10.1016/j.envsoft.2010.09.004)