**Original article**

# **Evaluation of the ability of the crop model STICS to recommend nitrogen fertilisation rates according to agro-environmental criteria**

Vianney HOULÈSa *, Bruno MARYa , Martine GUÉRIFb, David MAKOWSKIc , Eric JUSTESd

> a INRA, Unité d'Agronomie, rue Fernand Christ, 02007 Laon Cedex, France b INRA, Unité CSE, Domaine St-Paul, Site Agroparc, 84914 Avignon Cedex 9, France c INRA/INA-PG, UMR Agronomie, BP 01, 78850 Thiverval-Grignon, France d INRA, Unité d'Agronomie, Auzeville, BP 27, 31326 Castanet-Tolosan Cedex, France

> > (Received 16 July 2003; accepted 11 March 2004)

**Abstract** – The use of crop models for nitrogen fertiliser management raises several issues. A first problem is to define suitable criteria for optimising nitrogen fertilisation in function of economic, quality and environmental objectives. A second issue is to assess the capacity of the crop model to predict the variables involved in the calculation of the criteria such as grain yield, grain protein content, residual soil mineral nitrogen or nitrogen balance. A third issue is to evaluate the results obtained by applying the decision rules selected by the crop model. The three problems are considered in this paper in the case of winter wheat and the STICS model. Fourteen field experiments with various N fertilisation strategies were used for evaluating the model. STICS predicted grain yield and nitrogen balance more accurately than protein content and soil mineral N at harvest. Among the eight criteria tested for optimising N fertilisation, those using a maximal threshold on nitrogen balance seem to be the most valuable for satisfying agricultural and environmental objectives. Under conditions of environmental constraint, STICS was more efficient than the reference method (AZOBIL) at selecting the optimal nitrogen fertilisation scenario.

**crop model / agro-environmental criteria / evaluation / nitrogen fertilisation**

# **1. INTRODUCTION**

The balance-sheet method is one of the most popular for nitrogen fertiliser management [34, 37]. With this method, nitrogen rate recommendations are calculated on the basis of a potential yield objective and using measurements of soil mineral nitrogen over the potential rooting depth at the end of winter. This type of method is scientifically-based, can be easily used by practitioners and gives satisfying results. It is routinely used in the Netherlands [5, 30] and in France where the AZO-BIL computer program [26] is currently used by farmers for the main crops, particularly cereals. The method allows the optimisation of N fertilisation and the reduction of the amount of residual mineral nitrogen in the soil at harvest.

A commonly recognised drawback of this method is that the soil-plant interactions are not taken into account, particularly in the case of water stress. To cope with these situations, the combination of the recommendations of the balance-sheet method with plant indicators measured during the growing period has been suggested [36]. Two readily measurable indicators have been developed: the 'nitrate sap test', more exactly, the nitrate concentration in the stem base (e.g. the JUBIL® method in France, [21]) and the chlorophyll content in upper leaves, based either on transmittance [32] or reflectance measurements. Both indicators can provide an on-time diagnosis of nitrogen nutrition and can confirm or modify the recommendations made with the balance-sheet method several weeks earlier.

A promising approach for calculating nitrogen fertiliser requirements and optimal N rates consists of using crop models. One reason for their adoption in advisory systems is that crop models can account for several factors and their possible interactions. This is useful when several practices have to be optimised at the same time [20, 22, 25] or if the objective is not simply to optimise crop production but also to take into account environmental aspects [28].

Whatever the model employed and the techniques used to define the optimum practices, the results greatly depend on the criterion that is to be optimised. Complex criteria have been proposed in systems dealing with practice management on the farm or regional scales [2, 25, 35] and can be optimised by using artificial intelligence techniques. The classical approach to define nitrogen recommendation is to calculate the minimal rate giving the maximum yield, assuming that the function relating grain yield to N fertiliser rate reaches a plateau. However, the environmental and economic objectives are not accounted for explicitly with this method, which cannot be used to adapt nitrogen recommendations to grain and nitrogen prices or to environmental objectives. A second approach consists of maximising farmers' gross margin (e.g. [27, 31]). This method

<sup>*</sup> Corresponding author: houles@avignon.inra.fr

| Experiment# | Location    | Soil type               | Year | Cultivar | N fertiliser rates tested (kg ha–1) * | SN** |
|-------------|-------------|-------------------------|------|----------|---------------------------------------|------|
| 1           | Boigneville | Stony loam              | 1998 | Soissons | 0-120-160-200-240                     | Yes  |
| 2           | Boigneville | Shallow stony loam      | 1998 | Soissons | 0-120-160-200-240                     | Yes  |
| 3           | Boigneville | Very shallow stony loam | 1998 | Soissons | 0-120-160-200-240                     | Yes  |
| 4           | Boigneville | Shallow stony loam      | 1999 | Soissons | 0-120-160-200-280                     | Yes  |
| 5           | Boigneville | Stony loam              | 1999 | Soissons | 0-140-180-220-300                     | Yes  |
| 6           | Boigneville | Very shallow stony loam | 1999 | Soissons | 0-120-160-200-280                     | Yes  |
| 7           | Thibie      | Chalk                   | 1994 | Forby    | 80-120-160-200-240-280-320            | –    |
| 8           | Thibie      | Chalk                   | 1995 | Apollo   | 0-80-120-160-200-240-280-320          | Yes  |
| 9           | Thibie      | Chalk                   | 1998 | Shango   | 0-100-135-150-200-210-250-300-350-400 | –    |
| 10          | Thibie      | Chalk                   | 1999 | Shango   | 0-100-135-150-200-210-250-300-350-400 | –    |
| 11          | La Minière  | Deep loam               | 2002 | Shango   | 0-110-150-190-230                     | –    |
| 12          | La Cheppe   | Chalk                   | 2002 | Shango   | 0-140-220-300                         | Yes  |
| 13          | Chambry     | Sandy loam              | 2000 | Shango   | 0-60-120-180-240-300                  | –    |
| 14          | Chambry     | Loam                    | 2001 | Shango   | 0-120-160-220-240-280                 | –    |

**Table I.** Characteristics of the N fertiliser experiments performed on winter wheat analysed in this study.

* The recommended N fertiliser rates (AZOBIL software, [26]) are written in bold.

** Experiments in which the soil mineral nitrogen at harvest (*SN*) was measured.

can be used to adapt the nitrogen fertiliser recommendations to the economic context. A refinement of the method consists of including environmental criteria in the gross margin function. For instance, Makowski et al. [28] consider a penalty function based on soil mineral nitrogen at harvest (*SN*). In their example, the penalty is nil when *SN* is below a given threshold, and equal to the cost of establishing a cover crop in autumn when *SN* exceeds the threshold. Booltink et al. [5] proposed removing from the possible scenarios those leading to a high nitrate leaching probability during the winter following the considered crop. Once the criterion is elaborated, another important methodological problem is to evaluate the model ability, not only to simulate properly the criterion values but also to generate satisfactory management strategies. Antoniadou and Wallach [1] have proposed a method that consists of evaluating the results obtained when model-based decision rules are applied. Makowski et al. [28] extended this method to compare the performances of the true optimal strategies (evaluated from experimental data) and the performances of model-based decision rules. These methods were applied to evaluating only simple static models predicting crop response to applied nitrogen fertiliser.

The objective of our paper is to evaluate the ability of a dynamic crop model to select satisfactory nitrogen fertilisation scenarios from among a set of candidate scenarios, in the case of winter wheat. The selected crop model is STICS [7]. The evaluation is performed by using a data set including several nitrogen fertiliser experiments. Several agro-environmental criteria are compared to evaluate the scenarios through the crop model. These criteria were elaborated as possible candidates since no taxation for nitrogen pollution risk is applied at the moment in France.

### **2. MATERIALS AND METHODS**

This study is organised into three parts. First, we perform a data-based evaluation of several agro-environmental criteria that may be used to select appropriate N fertilisation scenarios from various experimental treatments. At this stage, the criteria, named hereafter as 'decision criteria', are calculated from the measured values at harvest of three variables of agronomic and environmental interest: grain yield, grain protein content and soil mineral nitrogen. Second, the STICS crop model is used to predict the different variables taken into account by the agro-environmental criteria and the predicted values are compared with the observations. Finally, we evaluate the capacity of STICS to select appropriate N fertilisation scenarios.

### **2.1. Field experiments**

The data analysed in this study come from 14 nitrogen fertilisation experiments carried out on winter wheat in several sites in northern France. A description of the main characteristics of these experiments is given in Table I. The nitrogen treatments varied primarily in total N rates and secondarily in splitting schemes. In each site, N rates varied from 0 to a maximum that reached 240 to 400 kg ha–1. The Boigneville experiments were realised during two successive years on 15 locations within a heterogeneous field [24]. In order to limit the influence of this site among the databases used, we retained only three locations per year, chosen from among the most different soils according to their available water reserve. In La Cheppe and La Minière, several N treatments led to the same total N rate but had different types of splitting. In each experiment, a recommended N rate was calculated at the end of winter using the AZOBIL balance-sheet method [26] and was one of the N treatments (Tab. I). These different N rates and splitting patterns represent in this study the different scenarios to be evaluated, from among which the best will have to be selected according to agro-environmental criteria. The Chambry experiments were used in a previous study to estimate some parameters of the STICS model (v5) for the cultivar *Shango* according to the methodology used by Dorsainvil [11].

Three variables of agronomic and environmental interest were measured at harvest: grain yield, *GN* (Mg dry matter ha–1),

grain protein content, *GP* (% of grain dry matter), and soil mineral nitrogen content in the 0–90 cm layer, *SN* (kg N ha–1). The latter measurement was not performed in all treatments (see Tab. I). Mineral nitrogen in soil was extracted with KCl M solution (soil:solution = 1:2) and measured by continuous flow colorimetry. The amounts of ammonium N were always small, so that only nitrate is considered in the results. Grain nitrogen content was measured using the Kjeldahl or Dumas methods and multiplied by 5.7 to obtain grain protein content [12, 17].

### **2.2. Agro-environmental decision criteria**

We defined and compared 8 agro-environmental decision criteria with respect to N fertilisation strategies by taking into account simultaneously the grain yield, the grain protein content (as an indicator of crop quality) and an environmental variable related to the risk of N loss. Each criterion can be characterised by a 'gross margin' (*GM*) and a 'gross income' (*GI*), defined as follows. *GM* (€ ha-1) is the difference between the income associated with grain production and the cost of the N fertiliser applied. It is the same for all criteria and is calculated as follows [28]:

$$GM = \mathbf{g} \left( GP \right) \cdot GY - \mathbf{c} \cdot NR \tag{1}$$

where *NR* is the total nitrogen rate (kg ha–1), *GP* is the grain protein content (%), *GY* is the grain yield (Mg ha–1) obtained for the rate *NR*, *g* is the function (€ Mg–1) that gives the price of wheat versus *GP* and *c* is the cost of the N fertiliser (€ kg–1). Grain prices were set equal to current values used by cooperatives in 2002. We used the following values:

*g(GP)* = 86.25 if *GP* ≤ 9 (2)

*g(GP)* = 86.25 + 3.93 (*GP–*9) if 9 < *GP* ≤ 12.5 (3)

*g(GP)* = 100 if *GP* > 12.5 (4)

*c* = 0.60. (5)

The gross margin, *GM*, represents approximately the variable part of the farmer's income, since EU subsidies may represent about half of the farmer's income. Those are not considered because they are independent of crop production.

The 'gross income', *GI*, is a function of *GM* and a 'penalty function' related to an environmental variable (Tab. II). For some criteria, the penalty function is nil and the environmental constraint is accounted differently (see below). Eight different penalty functions were considered. The penalty function considered in the criteria 1–2 uses the nitrogen balance, *NB* (kg ha–1), defined as the difference between N inputs as fertiliser and N outputs as wheat grains. The CORPEN office1 in France has proposed this balance as a basis for evaluating the risk of nitrogen losses. It is calculated as:

$$NB = NR - 10. \, GY. \, GP\% . \, \text{7.} \tag{6}$$

The N balance is converted into a penalty function using the taxation coefficient α (Tab. II). We considered two values for the parameter, α: 0.23 and 1.50 € kg–1. The first one corre-

**Table II.** Expression of eight agro-environmental criteria for evaluating nitrogen fertilisation strategies. GI = 'gross income', GM = 'gross margin', NB = N balance, SN = soil mineral nitrogen at harvest, TNB = threshold for N balance, TSN = threshold for soil mineral nitrogen at harvest (see definitions in the text).

| Criterion # | Criterion expression | Constraint | Parameter value  |
|-------------|----------------------|------------|------------------|
| 1           | GI = GM – α NB       | –          | α = 0.23 € kg–1  |
| 2           | GI = GM – α NB       | –          | α = 1.50 € kg–1  |
| 3           | GI = GM –<br>β<br>SN | –          | β = 1.00 € kg–1  |
| 4           | GI = GM –<br>SN<br>β | –          | β = 6.00 € kg–1  |
| 5           | GI = GM              | NB < TNB   | TNB = 90 kg ha–1 |
| 6           | GI = GM              | NB < TNB   | TNB = 60 kg ha–1 |
| 7           | GI = GM              | SN < TSN   | TSN = 35 kg ha–1 |
| 8           | GI = GM              | SN < TSN   | TSN = 20 kg ha–1 |

sponds to that proposed in a French project elaborated by the CORPEN, which is a low level of taxation. It can be considered as a reference criterion, not very different from the present situation. The second one is more severe and allows us to study the effect of a higher environmental tax.

A second environmental variable is considered in criteria 3 and 4: the amount of soil mineral nitrogen at harvest (*SN*). This variable is an indicator of the risk of nitrate pollution. It is predicted by crop models such as STICS and can be measured in field experiments. It is converted into a penalty function through the taxation parameter β that has been set either to a low (1 € kg–1) or a high level (6 € kg–1). The low level corresponds approximately to the threshold given by Makowski et al. [28], and the high level is 6 times higher, similarly to the parameter α.

The best N fertilisation strategy using criteria 1–4 is the strategy maximising the gross income. Another approach consists of selecting the strategy maximising the gross margin *GM* and satisfying an environmental constraint. This approach is considered in the criteria 5–8. The constraint is defined by a maximum threshold either on N balance (criteria 5–6) or on soil mineral N at harvest (criteria 7–8). The best strategy with criteria 5–8 is the strategy maximising GM, among all the strategies satisfying the constraint. If no strategy can satisfy the constraint, the strategy giving the lowest value for the environmental variable is selected. Again, two thresholds are considered for each environmental variable: a high one (criteria 5 and 7) and a lower one, thus more severe (criteria 6 and 8). The eight decision criteria were calculated for the different nitrogen fertilisation rates applied in the experiments. The decision criteria were first calculated with the measured values of yield, grain protein content, N balance and soil mineral nitrogen at harvest, and in a second stage, with the values estimated using STICS.

# **2.3. The STICS model**

The STICS model has already been described in several papers [7, 8]. It simulates the water, carbon and nitrogen dynamics in the soil-plant system at a daily time step. It considers the effects of water and nitrogen stress on plant growth and grain yield. The nitrogen balance, *NB*, depends on nitrogen

<sup>1</sup> Comité d'Orientation pour la Réduction de la Pollution des Eaux par les Nitrates, created by the French Ministry of Agriculture.

uptake which is calculated as the result of plant demand and soil supply, the latter being affected by root growth and nitrate concentration in soil layers. Soil mineral nitrogen, *SN*, is the balance between production and consumption processes: N fertilisation and mineralisation, N uptake, N leaching and N losses from fertiliser.

# **2.4. Comparison between observed and simulated values**

We performed two sets of simulations with STICS for each of the 14 experiments. The first set uses the actual climate of the year of the experiment during the whole growing season. The resulting simulations are called 'descriptive simulations'. The second set mimics a situation of real-time selection of a fertilisation strategy: it considers the actual climate until the date of the second nitrogen application (the date at which we want to define the N rate using the model), and then a probable climate up to harvest time. The probable climate was defined by the last thirty years of actual climate at the nearest weather station. The resulting simulations were averaged over the 30 years for each experiment. This second set of simulations is called 'predictive simulations'. From a practical point of view, the predictive simulations are more interesting. However, the comparison of the predictive and descriptive simulations is useful to study the effect of climate uncertainty on the results of the crop model.

Five types of variables are calculated from the STICS simulations for each experiment: grain yield, *GY*, grain protein content, *GP*, soil mineral nitrogen at harvest, *SN*, nitrogen balance, *NB* and gross margin, *GM*. For each variable, observed and simulated values are compared according to the following criteria:

– the root mean square error (RMSE)

$$RMSE = \sqrt{\frac{1}{N} \sum_{i} (Z_i - \hat{Z})^2} \tag{7}$$

where *N* is the number of observations, and *Zi* and represent the observed and simulated variables, respectively. *Zi* ˆ

- the parameters of the linear regression: slope *a*, intercept *b* and determination coefficient r2;
- the decomposition of the mean square error between the systematic mean square error (*RMSEs*) and the unsystematic mean square error (*RMSEu*) [38]:

$$RMSE_{\bar{s}} = \sqrt{\frac{1}{N} \sum_{i} (b + a.Zi - Zi)^2} \tag{8}$$

$$RMSE = \sqrt{\frac{1}{N} \sum_{i} (b + a.Zi - \hat{Z})^2} \,. \tag{9}$$

This decomposition allows us to distinguish between the systematic component of the error, attributed to a bias, and a random error (unsystematic).

The criteria 7–9 are calculated for several variables: *GY, GP, SN* and *NB*.

# **2.5. Evaluation of the capacity of STICS to select satisfactory strategies**

The last type of evaluation consists of assessing the capacity of STICS to identify the best scenario according to a given decision criterion. We adopted, in a simplified way, the method proposed by Antoniadou and Wallach [1] and applied by Makowski and Wallach [27]. For each of the eight decision criteria displayed in Table II and for each of the two sets of simulations, we first compared the scenario selected by STICS (i.e. the scenario corresponding to the minimal N rate that maximises GI) to the best observed scenario determined from the measurements obtained in the experiment. Therefore, we evaluated the consequence of choosing a scenario with STICS by calculating, for each experiment, the difference between the value of the observed decision criterion corresponding to the N rate selected by STICS and that obtained with the true best scenario. We finally examined whether the scenario selected by STICS could satisfy the environmental constraint defined by the criteria 5–8. The same type of evaluation was also performed for the balance-sheet method (AZOBIL). This was possible because each experiment included a treatment corresponding to the AZOBIL recommended rate.

# **3. RESULTS**

# **3.1. Agro-environmental criteria based on experimental results**

Figure 1 shows the 'response curves' observed in 6 experiments: grain yield (*GY*), soil mineral nitrogen at harvest (*SN*) and nitrogen balance (*NB*) versus total rate of fertiliser N. The diversity in the response curves encountered in the 14 experiments is represented in these 6 experiments. The wide range of grain yields obtained, from 1.5 to 9.9 Mg ha–1 (grain at 0% moisture content), was mainly due to the large variation in fertiliser N rates and soil conditions. The shape of the grain yield curves is classical (e.g. [28]): a maximum yield was clearly reached in some experiments (exp. #1 and 4) but possibly not in others (exp. #8 and 13). In the latter case, we supposed that the optimal N rate (giving the highest gross margin) was equal to the maximum N rate tested experimentally. The soil mineral nitrogen at harvest varied as previously reported [9, 28]: when N rate increased, *SN* first remained stable and then increased, particularly when the fertiliser rate exceeded the optimum N rate. However, this did not occur in experiment #8, in which a regular increase was observed since the origin. The nitrogen balance increased approximately linearly versus the N rate in all experiments. The intercept varied from –72 to –21 kg ha–1 but the slope of the linear regression did not vary much: 0.55 ± 0.07. This is consistent with data reported previously e.g. Mary et al. [29]. It must be noted that the nitrogen balance corresponding to the optimum N rate was always positive (from 17 to 120 kg N ha–1).

Using the observed values of *GY, SN* and *NB*, we calculated a posteriori the gross margin and the gross income for each of the 8 decision criteria previously defined versus N rate. Figure 1 shows that the gross income calculated for decision criterion 1 (GI C1) was very similar to the gross margin, which

**Figure 1.** Response curves' observed in 6 experiments: grain yield (*GY*), soil mineral nitrogen at harvest (*SN*), nitrogen balance (*NB*), gross margin (*GM*), gross income with criterion 1 (*GI C1*) or 2 (*GI C2*) versus total N fertiliser rate added. The legend indicates the number of experiments (see Tab. I).

indicates that the decision criterion 1 exerts a very weak environmental constraint and is probably inefficient at reducing N pollution, although it corresponds to an increase of almost 50% of the present cost of fertiliser. A much higher taxation of the nitrogen balance (criterion 2, GI C2) changed the gross income curves and therefore the optimum N rate for the majority of experiments, but not all (not for experiments #1 and #8).

The maximum value of gross income for each decision criterion and the corresponding optimal fertiliser rate in each of the 14 experiments are given in Table III; the grain yields and the N balances are presented in Table IV. The results show that the optimum N rate depends on the chosen criterion in most cases (in 12 out of 14 experiments). For example, the optimum N rate varied widely in experiment 4, from 120 to 280 kg ha–1, whereas it remained the same (200 kg ha–1) in experiments 1 and 12. This difference results from the diversity of the response curves: the pattern of the *GY* and *SN* curves versus N fertiliser was flatter in experiment #4 than in #1. Using a low threshold criterion for *SN* may lead to recommending a nil rate of application: this was the case with decision criterion 8 in

experiments 8 and 12. This is due to the fact that *SN* was greater than the threshold (20 kg N ha–1) for all N rates. This example shows the difficulty of using such a criterion and a severe threshold. The higher threshold of *SN* (criterion 7) is better suited and gives more logical results. However, the use of decision criteria based on soil mineral N at harvest may be difficult to generalise for two reasons: (i) *SN* varies slowly versus the N rate, so that measurement errors may have important consequences on N recommendations, and (ii) *SN* is markedly influenced by soil type (e.g. clay soils contain higher residual mineral N than loamy or sandy soils) (e.g. [5]) so that the threshold should vary between pedological zones.

Table III also shows that the criteria which are more severe with respect to environmental concern lead to recommending lower N rates than the corresponding ones with a greater tolerance: the mean reduction was 48, 20, 40 and 67 kg N ha–1 for the criteria C1/C2, C3/C4, C5/C6 and C7/C8, respectively. The corresponding reduction in gross income was 89, 88, 38 and 77 € ha–1; for grain yield it was 0.4, 0.0, 0.5 and 0.9 Mg ha–1 (Tab. IV).

Comparing criteria in which a penalty is applied as a taxation (C1–C4) or as a threshold (C5–C8) indicates that the latter is more constrictive and always reaches the objective, whereas the first cannot always satisfy the N balance threshold. Taxation criteria led to reaching higher grain yields (0.5 Mg ha–1 in average) and to recommending higher N rates (33 kg N ha–1 in average), although they gave a smaller gross income (–20 € ha–1) and had a greater N balance (17 kg N ha–1) than threshold criteria.

Therefore it seems that the most interesting criteria, combining the interests of the farmer and improved N management, are the threshold criteria applied to soil nitrogen balance. This conclusion will be confirmed by the results of the model simulation.

# **3.2. Comparison of measured and predicted variables**

# *3.2.1. 'Descriptive' simulations*

The comparison between observed and simulated values of *GY*, *GP*, *NB* and *SN* for all experiments is shown in Figure 2. The corresponding statistics are given in Table V. The grain yield was rather well simulated by STICS: there was no bias between observed and simulated values, as shown by the low value of RMSEs (0.10 Mg ha–1), the slope of the regression line (0.97) and the small intercept (0.27 Mg ha–1). The scattering is nonetheless rather significant, as indicated by the r2 value (0.80) and by the fact that nearly all the error is explained by RMSEu (1.05 Mg ha–1). This error is non-negligible but is still lower than that obtained previously with STICS on other data sets (1.35 Mg ha–1 in [8]), or using response models (1.22 Mg ha–1 in [28]), or using different crop models for situations in which the soil was not as well described [23]. However, the yield values simulated for high nitrogen rates tend to be overestimated. The overestimation is particularly significant for experiments #4 and 6, in which no plateau is simulated (Fig. 3), whereas one is observed (Fig. 1). This also appears in Figure 2: the higher yields were often overestimated. This behaviour may lead the model to overestimate the optimal N rates.

![](_page_4_Figure_11.jpeg)

**Table III.** N fertiliser rate and gross income corresponding to the best scenario using observed values, for each experiment and each criterion tested (C1–C8). Criteria 3, 4, 7 and 8 could not be calculated in experiments without measurements of soil mineral nitrogen at harvest (see Tab. II).

| Exp. # | N fertiliser rate (kg ha–1) |     |     |     |     |     |     |     |     | Gross income (€ ha–1) |     |     |     |     |     |     |
|--------|-----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----------------------|-----|-----|-----|-----|-----|-----|
|        | C1                          | C2  | C3  | C4  | C5  | C6  | C7  | C8  | C1  | C2                    | C3  | C4  | C5  | C6  | C7  | C8  |
| 1      | 200                         | 200 | 200 | 200 | 200 | 200 | 200 | 200 | 631 | 574                   | 622 | 525 | 641 | 641 | 641 | 641 |
| 2      | 240                         | 240 | 240 | 240 | 240 | 160 | 240 | 240 | 581 | 478                   | 580 | 483 | 599 | 521 | 599 | 599 |
| 3      | 200                         | 160 | 200 | 160 | 200 | 160 | 200 | 200 | 420 | 353                   | 421 | 340 | 440 | 433 | 440 | 440 |
| 4      | 200                         | 120 | 280 | 200 | 160 | 120 | 280 | 200 | 410 | 325                   | 419 | 329 | 406 | 386 | 440 | 432 |
| 5      | 220                         | 220 | 220 | 220 | 180 | 140 | 300 | 220 | 440 | 314                   | 450 | 386 | 430 | 350 | 467 | 463 |
| 6      | 200                         | 160 | 200 | 200 | 160 | 120 | 200 | 200 | 372 | 262                   | 374 | 276 | 364 | 325 | 393 | 393 |
| 7      | 240                         | 240 | –   | –   | 240 | 160 | –   | –   | 579 | 470                   | –   | –   | 599 | 486 | –   | –   |
| 8      | 320                         | 240 | 320 | 280 | 240 | 160 | 160 | 0   | 640 | 496                   | 620 | 410 | 622 | 513 | 513 | 261 |
| 9      | 300                         | 150 | –   | –   | 250 | 200 | –   | –   | 643 | 523                   | –   | –   | 645 | 602 | –   | –   |
| 10     | 300                         | 200 | –   | –   | 250 | 200 | –   | –   | 679 | 565                   | –   | –   | 666 | 635 | –   | –   |
| 11     | 190                         | 190 | –   | –   | 190 | 190 | –   | –   | 868 | 889                   | –   | –   | 864 | 864 | –   | –   |
| 12     | 220                         | 220 | 220 | 220 | 220 | 220 | 220 | 0   | 706 | 662                   | 690 | 565 | 715 | 715 | 715 | 364 |
| 13     | 300                         | 180 | –   | –   | 240 | 180 | –   | –   | 745 | 706                   | –   | –   | 747 | 731 | –   | –   |
| 14     | 280                         | 220 | –   | –   | 120 | 120 | –   | –   | 577 | 422                   | –   | –   | 481 | 481 | –   | –   |
|        |                             |     |     |     |     |     |     |     |     |                       |     |     |     |     |     |     |
| Mean1  | 244                         | 196 |     |     | 206 | 166 |     |     | 592 | 503                   |     |     | 587 | 549 |     |     |
| Mean2  | 225                         | 195 | 235 | 215 | 200 | 160 | 225 | 158 | 525 | 433                   | 522 | 414 | 527 | 486 | 526 | 449 |

1 Mean of the 14 experiments; 2 mean of the 8 experiments in which all variables were measured.

| Table IV. Grain yield and N balance corresponding to the best scenario using observed values, for each experiment and each criterion tested    |  |  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| (C1–C8). Criteria 3, 4, 7 and 8 could not be calculated in experiments without measurements of soil mineral nitrogen at harvest (see Tab. II). |  |  |  |

| Exp.# |      |      |     |     | Grain yield (Mg ha–1) |      |     |     |     | N balance (kg ha–1) |     |     |     |     |     |     |
|-------|------|------|-----|-----|-----------------------|------|-----|-----|-----|---------------------|-----|-----|-----|-----|-----|-----|
|       | C1   | C2   | C3  | C4  | C5                    | C6   | C7  | C8  | C1  | C2                  | C3  | C4  | C5  | C6  | C7  | C8  |
| 1     | 8.1  | 8.1  | 8.1 | 8.1 | 8.1                   | 8.1  | 8.1 | 8.1 | 45  | 45                  | 45  | 45  | 45  | 45  | 45  | 45  |
| 2     | 7.6  | 7.6  | 7.6 | 7.6 | 7.6                   | 7.0  | 7.6 | 7.6 | 81  | 81                  | 81  | 81  | 81  | 44  | 81  | 81  |
| 3     | 5.9  | 5.7  | 5.9 | 5.7 | 5.9                   | 5.7  | 5.9 | 5.9 | 84  | 53                  | 84  | 53  | 84  | 53  | 84  | 84  |
| 4     | 6.2  | 5.3  | 6.2 | 6.2 | 5.8                   | 5.3  | 6.2 | 6.2 | 94  | 40                  | 148 | 94  | 67  | 40  | 148 | 94  |
| 5     | 6.4  | 6.4  | 6.4 | 6.4 | 6.2                   | 5.0  | 6.6 | 6.4 | 100 | 100                 | 100 | 100 | 80  | 60  | 161 | 100 |
| 6     | 5.4  | 5.0  | 5.4 | 5.4 | 5.0                   | 4.6  | 5.4 | 5.4 | 94  | 68                  | 94  | 94  | 68  | 48  | 94  | 94  |
| 7     | 7.8  | 7.8  | –   | –   | 7.8                   | 6.6  | –   | –   | 86  | 86                  | –   | –   | 86  | 49  | –   | –   |
| 8     | 8.6  | 8.2  | 8.6 | 8.5 | 8.2                   | 7.0  | 7.0 | 2.9 | 128 | 84                  | 128 | 109 | 84  | 47  | 47  | –50 |
| 9     | 8.5  | 7.3  | –   | –   | 8.2                   | 7.8  | –   | –   | 112 | 25                  | –   | –   | 82  | 54  | –   | –   |
| 10    | 8.8  | 8.1  | –   | –   | 8.4                   | 8.1  | –   | –   | 105 | 47                  | –   | –   | 76  | 47  | –   | –   |
| 11    | 10.1 | 10.1 | –   | –   | 10.1                  | 10.1 | –   | –   | –17 | –17                 | –   | –   | –17 | –17 | –   | –   |
| 12    | 8.5  | 8.5  | 8.5 | 8.5 | 8.5                   | 8.5  | 8.5 | 4.2 | 35  | 35                  | 35  | 35  | 35  | 35  | 35  | –59 |
| 13    | 9.7  | 9.3  | –   | –   | 9.6                   | 9.3  | –   | –   | 98  | 17                  | –   | –   | 61  | 17  | –   | –   |
| 14    | 8.6  | 8.1  | –   | –   | 6.4                   | 6.4  | –   | –   | 130 | 97                  | –   | –   | 40  | 40  | –   | –   |
|       |      |      |     |     |                       |      |     |     |     |                     |     |     |     |     |     |     |
| Mean1 | 7.9  | 7.5  |     |     | 7.6                   | 7.1  |     |     | 84  | 54                  |     |     | 62  | 40  |     |     |
| Mean2 | 7.1  | 6.9  | 7.1 | 7.1 | 6.9                   | 6.4  | 6.9 | 5.8 | 83  | 63                  | 89  | 76  | 68  | 47  | 87  | 49  |

1 Mean of the 14 experiments; 2 mean of the 8 experiments in which all variables were measured.

![](_page_6_Figure_1.jpeg)

**Figure 2.** Comparison of simulated and observed values of grain yield (*GY*), grain protein content (*GP*), nitrogen balance (*NB*) and soil mineral nitrogen at harvest (*SN*). Closed symbols represent the 'descriptive' simulations (with the actual climate) and open symbols represent the 'predictive' simulations (with climatic scenarios).

Grain protein content was poorly predicted by the model. The RMSE value (1.6%) is close to half the difference between the thresholds used for price calculation (Eqs. (2)–(4)), which could be acceptable. But the great scattering and the significant bias (RMSEs and RMSEu have nearly the same contribution in RMSE) shown, respectively, by the low r² value and the values of the slope (0.47) and intercept (4.7%), indicate that the prediction of grain protein content in the simulation was inaccurate. Grain protein content was underestimated in most situations. Furthermore, the simulated values have a lower variance than the observed values. This result is due in large part to the overestimation of yield for high yields.

Nitrogen balance was the variable best predicted by the model: the regression slope and the coefficient of determination are equal to 0.98 and 0.93, respectively. This results from the accurate predictions of the amounts of N accumulated in grains (r2 = 0.90), partly resulting from the compensation of errors (overestimation of grain yield and underestimation of protein content). The observed N balance varied widely, from –87 to +161 kg ha–1. The RMSE obtained for this variable is equal to 19 kg ha–1 and the bias is low.

Soil mineral N at harvest was poorly predicted. The slope and r² values are low; the RMSE is equal to 11 kg ha–1, whereas measured values are in the range 11–52 kg ha–1. The decomposition of RMSE shows that the errors are mostly unsystematic. The significant errors of prediction of STICS for this variable might be due to the rather low values of soil mineral N observed in these experiments and to the variability of measurement. These results indicate that, in the experimental conditions, the criteria based on the nitrogen balance, *NB*, are more reliable than those based on soil mineral N at harvest because the latter variable is not predicted well enough.

### *3.2.2. 'Predictive' simulations*

The results of the 'predictive' simulations, i.e. simulations implemented with probable climates after the date of the second N application, are presented in Figure 2 and in Table V. The results of the 'predictive' simulations are close to those of the 'descriptive' simulations, considering the true climate encountered in the experiment. The quality of fit is almost unchanged for the variable *NB*, while it is surprisingly slightly better for predictive simulations of *GY*, *GP* and *SN*. Predictive simulations reduce the RMSE from 1.06 to 0.97 Mg ha–1 in the case of grain yield, from 1.6% to 1.3% for grain protein content and from 11 to 10 kg ha–1 for soil mineral nitrogen. The weak difference between predictive and descriptive simulations can be attributed to the rather low variability of the climate during spring in the considered regions.

### **3.3. Capacity of STICS to select satisfactory scenarios**

We will now consider only decision criteria based on the nitrogen balance, namely criteria 1, 2, 5 and 6, since prediction

|           | Grain yield<br>(Mg ha–1) |            | Protein content<br>(%) |            | Nitrogen balance<br>(kg ha–1) |            | SN at harvest<br>(kg ha–1) |            |  |
|-----------|--------------------------|------------|------------------------|------------|-------------------------------|------------|----------------------------|------------|--|
|           | Descriptive              | Predictive | Descriptive            | Predictive | Descriptive                   | Predictive | Descriptive                | Predictive |  |
| 2<br>r    | 0.80                     | 0.82       | 0.34                   | 0.43       | 0.93                          | 0.91       | 0.09                       | 0.27       |  |
| Slope     | 0.97                     | 0.94       | 0.47                   | 0.50       | 0.98                          | 0.95       | 0.37                       | 0.65       |  |
| Intercept | 0.27                     | 0.34       | 4.7                    | 5.1        | 10                            | 5          | 14                         | 12         |  |
| RMSE      | 1.05                     | 0.97       | 1.6                    | 1.3        | 19                            | 19         | 11                         | 10         |  |
| RMSEs 1   | 0.10                     | 0.14       | 1.2                    | 0.9        | 9                             | 4          | 5                          | 5          |  |
| RMSEu 2   | 1.05                     | 0.96       | 1.1                    | 1.0        | 16                            | 19         | 10                         | 9          |  |

**Table V.** Statistical criteria of quality of fit between observed and simulated values of grain yield, grain protein content, nitrogen balance and soil mineral nitrogen (*SN*) at harvest. (a) Descriptive simulations (with the actual climate) and (b) predictive simulations (with climatic scenarios). The r2 , slope and intercept correspond to the linear regression between observed and simulated values. Number of observations = 159.

1 Root mean square error due to systematic errors; 2 root mean square error due to non-systematic errors.

![](_page_7_Figure_2.jpeg)

**Figure 3.** 'Response curves' simulated by STICS in 6 experiments: grain yield (*GY*), soil mineral nitrogen at harvest (*SN*), nitrogen balance (*NB*), gross margin (*GM*), gross income with criterion 1 (*GI C1*) or 2 (*GI C2*) versus total N fertiliser rate added. The legend indicates the number of experiments (see Tab. I).

of soil mineral nitrogen at harvest was poor. The simulated gross incomes were calculated from simulated values of *GY*, *GP* and *NB*.

Figure 4 compares the simulated (using the actual climate) and the observed response of gross income and nitrogen balance to the N rate, for criteria 2 and 5 and for two experiments. *NB* was accurately predicted in experiment #3, whereas GI was poorly simulated due to an overestimation of *GY* and *GP* (Figs. 1, 3). However, the best strategy selected from STICS simulations for criterion 2 was the same as the best observed strategy. This was not the case for experiment #6 and criterion 5. With this criterion, the best scenario had to satisfy the environmental constraint (*NB* < 90 kg ha–1). The nitrogen rate of the scenario selected by STICS for experiment #6 was lower than that selected from observations because *NB* was overestimated by the model.

The difference between the gross income obtained with the scenario selected by STICS and the gross income corresponding to the best observed scenario is an estimate of the expected income loss that results from using the model to select a ferti-

![](_page_7_Figure_7.jpeg)

**Figure 4.** 'Response curves' observed or simulated by STICS in experiments #3 and 6: nitrogen balance (*NB*) and gross income (*GI*). Gross income was calculated with criterion 2 in the case of experiment #3 and with criterion 5 in the case of experiment #3. Round symbols = observed data; square symbols = 'descriptive' simulations (actual climate). Right hand graphs: the N rates that are excluded by the *NB* threshold are shown in black. Upper right graph: the N balance threshold that is used in criterion 5 is indicated by a solid line. Lower right graph: the maximum N rate is given by a solid line in the case of observed data and a dotted line in the case of 'descriptive' simulations. The arrows highlight the best scenarios according to observed and simulated data.

![](_page_7_Figure_9.jpeg)

**Figure 5.** Gross incomes observed and simulated by STICS in experiment #1, either with criterion 1 (left hand side) or 2 (right hand side). The solid squares indicate the best scenarios according to STICS model; the solid circles indicate the true best scenarios and the grey circles represent the actual gross income, which would have been obtained with the N rate recommended by STICS. The arrows represent the financial losses due to STICS errors.

lisation strategy. The income loss depended on the considered criterion, as shown for experiment #1 (Fig. 5). The two different levels of taxation of the nitrogen balance considered in criteria 1 and 2 lead to different gross income responses. The fact that STICS did not predict a plateau for *GY* in the range of N rates tested and that it simulated a linear decrease in *GM* and *GI* for

**Table VI.** Mean differences in N rate, gross income (*GI*) and nitrogen balance (*NB*) and frequency of exceeding the nitrogen balance threshold, calculated for criteria 1, 2, 5 and 6 (see Tab. II) using different ways to select the best scenario: (1) with descriptive STICS simulations (using the actual climate); (2) with predictive STICS simulations (using climatic scenarios); (3) with AZOBIL recommendations [26].

|                                   | STICS       | STICS      | AZOBIL |
|-----------------------------------|-------------|------------|--------|
|                                   | Descriptive | Predictive |        |
| N rate: mean difference (kg ha–1) |             |            |        |
| C1                                | 42          | 32         | –25    |
| C2                                | 35          | –10        | 23     |
| C5                                | –10         | –1         | 13     |
| C6                                | –17         | –8         | 63     |
| GI: mean loss (€ ha–1)            | –15         | –12        | –14    |
| C1                                |             |            |        |
| C2                                | –41         | –50        | –15    |
| C5                                | –41         | –31        | 8      |
| C6                                | –37         | –30        | 59     |
| NB: mean difference (kg ha–1)     | 32          | 24         | –13    |
| C1                                |             |            |        |
| C2                                | 27          | –1         | 17     |
| C5                                | 1           | 4          | 9      |
| C6                                | –10         | –4         | 37     |
| Frequency of exceeding TNB        |             |            |        |
| C5                                | 14%         | 14%        | 29%    |
| C6                                | 0%          | 14%        | 79%    |

criteria 1 or 2 for the higher N rates (Figs. 1, 3) resulted in selecting a non-optimal scenario that led to a loss in gross income (the difference between the black and grey circles in Fig. 5). The income loss depended on the shape of the observed *GI* response curve to the N rate.

Table VI summarises the 'agro-environmental' performances of the crop model. It gives the mean differences between the simulated and the observed best scenarios for N rates, gross income and nitrogen balance, and the frequency of exceeding the *NB* threshold in the case of criteria 5 and 6, in comparison with the reference method (AZOBIL). The differences in N rates between the scenarios selected by STICS and the best observed scenarios were positive for criteria 1 (the model recommends an excessive amount of fertiliser) and generally negative for criteria 2, 5 and 6 (the model underestimates the fertiliser requirement).

With predictive simulations, the mean loss of gross income is limited to 12 € ha–1 for criterion 1 (which considers a low taxation coefficient), to 30 € ha–1 for criteria 5 and 6, and reaches 50 € ha–1 for criterion 2 (Tab. VI). The *NB* threshold was satisfied in 86% of the experiments. The mean differences in nitrogen balance varied from –4 to +24 kg·ha–1 and could then be positive. This means that the nitrogen balance could be increased by errors in the selection of N rates by STICS.

We obtained very close results in the case of descriptive simulations. However, the predictive simulations gave, as mentioned previously, slightly better results than the descriptive simulations.

STICS results compared favourably with the balance sheet (AZOBIL) used as the reference method. AZOBIL was very efficient at predicting the best N scenario since it resulted in almost no loss in gross income compared with the observed values, measured a posteriori. STICS was less efficient for the gross income but gave better results in terms of nitrogen balance: the *NB* threshold was exceeded in 29% to 79% of the situations with AZOBIL and only in 0% to 14% of the experiments with STICS. AZOBIL is a good decision tool when there is no severe environmental constraint whereas STICS satisfies the environmental constraint in most cases.

### **4. DISCUSSION**

# **4.1. Ability of STICS to simulate agro-environmental variables**

The performance of the crop model to simulate plant components, i.e. crop biomass, crop yield, grain protein and N uptake is comparable with other models. Jamieson et al. [19] compared five simulation models in a common experiment with treatments differing in water stress. They obtained a RMSE which varied according to the models from 0.64 to 1.42 Mg ha–1 and 1.5 to 6.2 t/ha for grain yield and total biomass, respectively. Our own results were 1.05 and 2.0 Mg ha–1, respectively, for a similar range of yields (1.3 to 10.1 Mg ha–1). Bannayan et al. [4] found a RMSE of 0.93 and 3.2 Mg ha–1 by using the CERES wheat model with UK field experiments. Using the APSIM model, Asseng et al. [2] obtained a lower RMSE; respectively, 0.4 and 0.8 Mg ha–1, but in Australian situations with a much lower production (1 to 4 Mg ha–1 grain yield), so that the relative RMSE was similar to ours. They simulated N uptake with a RMSE equal to 14 kg ha–1 in a range 1–112 kg ha–1, whereas we obtained a RMSE of 30 kg ha–1 in the range 27–381 kg ha–1. Concerning grain protein content, Asseng et al. [3] obtained a RMSE of 1.7% and 1.5% for CERES and APSIM (modified version), respectively, in temperate maritime conditions; this is close to the value found by STICS on our data set:1.6%.

Fewer results have been reported on the prediction of mineral N at harvest or N balance. Hansen et al. [16], using the DAISY model, obtained a good simulation of *SN* at a moderate level of fertiliser (140 kg N ha–1) but the model overestimated *SN* at the higher levels of fertiliser (240–340 kg N ha–1). Asseng et al. [2] stated that 'the pattern of soil mineral N in soil was usually predicted well by the (APSIM) model'. However their results were obtained for a much wider range of *SN* than ours since nitrate N concentrations varied from 0 to 169 mg N kg–1, which corresponds to about 240 kg N ha–1 in a 10-cm layer. The mean RMSE was 10 mg N kg–1, i.e. about 14 kg N ha–1 in this single layer, to be compared with 11 kg N ha–1 for a 0– 90 cm layer in our experiments.

The capacity of the model to predict the amounts of soil nitrogen at harvest and at the beginning of the drainage period (usually the end of autumn) has to be further evaluated on other data sets, since the range of variation encountered here was small and since these are key variables for predicting nitrate leaching. However, the N balance is also an interesting environmental variable. It is equal to the sum of leaching losses, gaseous losses and N storage in soil [29]. Therefore, it also integrates the risk of gaseous losses: denitrification and ammonia volatilisation. In agricultural systems, which have reached the equilibrium in soil organic matter, it is equal to the overall losses. Davies and Sylvester-Bradley [10] have shown that the increase in nitrate pollution was parallel to the increase in N balance during the last 50 years in the UK. The N balance, which is easily measurable and rather well predicted by the model (RMSE = 19 kg N ha–1), seems to constitute the better environmental indicator of the N budget.

### **4.2. Ability of the model to choose the best scenario**

In this study, we used a discrete approach, i.e. involving a limited number of N fertilisation rates corresponding to experimental treatments and called 'scenarios'. These scenarios differ from each other by rather large differences in N rates (from 40 to 140 kg ha–1). The purpose was to avoid using functions of yield response to nitrogen. Indeed, this approach is questionable because the optimal N rate that is determined by this method is highly dependent on the chosen function (e.g. [28]). The drawback is that the differences in model outputs may be significant when the model selects a wrong scenario. Probably, the optimal N rates predicted by STICS could have been better determined by testing a large number of N rates, varying from a small increment (e.g. 5 kg ha–1). This approach should be more favourable to the model. However, the comparison between the observed and simulated optimal N rates would remain difficult since those are calculated with a different method.

The comparison with a classical method, based on a static model, showed that AZOBIL was a suitable method, even better than STICS, for recommending N rates in the case of lowconstraint agro-environmental criteria. However, STICS performed better when the optimisation criterion included more severe environmental constraint; for example, a maximum N balance of less than 60 kg N ha–1.

Beyond these results, it can be stated that the crop model has additional advantages: it has a much greater potential than the static model to account for more severe stress conditions than those experienced here and it can be used for defining the optimum N rate for a large range of yield objectives.

Whatever the way of recommending N rates and the decision criterion adopted, decision rules require information (e.g. measurement of soil mineral N) and have a cost. It would be necessary to include this cost in the criterion calculation. As emphasised by Schröder et al. [36], all methods used to improve N fertilisation recommendation have to be economically competitive in comparison with 'insurance' practices (i.e. practices which ensure a maximum yield in all years).

### **4.3. Outlooks**

This work aimed at evaluating the benefits of using a crop model to evaluate N fertilisation strategies. The question was limited to the selection of a total N rate that is split and applied on given dates as usually recommended. The benefits of this approach appear as soon as one environmental constraint has to be satisfied and should be reinforced in the case of an exceptional climatic year. We will further test the ability of the crop model in decision-making for the whole N fertilisation strategy, including optimisation of the dates of application and the splitting scheme. This would be achieved by generalising the running of scenarios that combine dates and rates of N fertiliser applications over a range of climates, and selecting dates/rates that optimise the chosen agro-environmental criterion. It would also be achieved by directly estimating values of dates and rates expressed as continuous variables lying within prescribed ranges that optimise the criterion.

Another promising perspective is to improve the quality of prediction of the state variables involved in the criterion by the crop model. This would be achieved by using additional information on some of the state variables during the growing season, via assimilation techniques. Among the available techniques, some allow the correction of the model's prediction by re-estimating input variables that are difficult to assess. Remote-sensing observations in the solar domain give access to interesting biophysical variables of the crop and they are good candidates for performing such a correction of the model, as demonstrated at the field level with different models [6, 13, 33].

These techniques allow one to perform a site-specific calibration of the model. They are of particular interest in the context of precision agriculture, the objective of which is to recommend N rates adapted to the local characteristics within the field [14, 15]. In this context, the optimisation procedure can be realised either on each point independently or simultaneously over the whole field. Houlès et al. [18] showed that, for the decision criteria using a nitrogen balance threshold, a global optimisation procedure is preferable to a multilocal optimisation because it produces a less severe reduction in gross income while respecting the fixed threshold. We are currently working on developing a tool dedicated to a variable-rate application of nitrogen fertilisation on wheat, based on the STICS model, the assimilation of observations acquired by remote sensing and the agro-environmental criteria based on the nitrogen balance developed in this paper.

**Acknowledgments:** We are very grateful to F. Laurent, P. Gate, G. Aubrion (Arvalis – Institut du Végétal) and S. Vautrin who kindly provided the data of the Boigneville, Thibie, La Minière and La Cheppe experiments. We thank J.M. Machet and N. Beaudoin for their contribution to Chambry's experiments and help with model parameterisation, as well as F. Mahu, C. Dominiarczyk, D. Boitez, P. Devaux, E. Venet, E. Gréhan, M. Boucher and O. Delfosse for their technical assistance.

### **REFERENCES**

- [1] Antoniadou T., Wallach D., Evaluating decisions rules for nitrogen fertilizer, Biometrics 56 (2000) 420–426.
- [2] Asseng S., Keating B.A., Fillery I.R.P., Gregory P.J., Bowden J.W., Turner N.C., Palta J.A., Abrecht D.G., Performance of the APSIM-wheat model in Western Australia, Field Crops Res. 57 (1998) 163–179.
- [3] Asseng S., Bar-Tal A., Bowden J.W., Keating B.A., Van Herwaarden A., Palta J.A., Huth N.I., Probert M.E., Simulation of

grain protein content with APSIM-Nwheat, Eur. J. Agron. 16 (2002) 25–42.

- [4] Bannayan M., Crout N.M.J., Hoogenboom G., Application of the CERES-wheat model for within-season prediction of winter wheat yield in the United Kingdom, Agron. J. 95 (2003) 114–125.
- [5] Booltink H.W.G., van Alphen B.J., Batchelor W.D., Paz J.O., Stoorvogel J.J., Vargas R., Tools for optimising management of spatially-variable fields, Agric. Syst. 70 (2001) 445–476.
- [6] Bouman B.A.M., Linking physical remote sensing models with crop growth simulation models applied for sugar beet, Int. J. Remote Sens. 13 (1992) 2565–2581.
- [7] Brisson N., Ruget F., Gate Ph., Lorgeou J., Nicoullaud B., Tayot X., Plenet D., Jeuffroy M.H., Bouthier A., Ripoche D., Mary B., Justes E., STICS: a generic model for simulating crops and their water and nitrogen balances. II. Model validation for wheat and maize, Agronomie 22 (2002) 69–92.
- [8] Brisson N., Gary C., Justes E., Roche R., Mary B., Ripoche D., Zimmer D., Sierra J., Bertuzzi P., Burger P., Bussière F., Cabidoche Y.M., Cellier P., Debaeke P., Gaudillère J.P., Hénault C., Maraux F., Seguin B., Sinoquet H., An overview of the crop model STICS, Eur. J. Agron. 18 (2003) 309–332.
- [9] Chaney K., The effect of nitrogen fertiliser rate on the soil nitrate content after harvesting winter wheat, J. Agric. Sci. (Camb.) 114 (1990) 171–176.
- [10] Davies D.B., Sylvester-Bradley R., The contribution of fertiliser nitrogen to leachable nitrogen in the UK: a review, J. Sci. Food Agric. 68 (1995) 399–406.
- [11] Dorsainvil F., Evaluation par modélisation de l'impact environnemental des modes de conduite des cultures intermédiaires sur les bilans d'eau et d'azote dans les systèmes de culture, Ph.D. thesis, INA Paris-Grignon, 2002, 183 p.
- [12] Grundy A.C., Boatman N.D., Froud-Williams R.J., Effects of herbicide and nitrogen fertilizer application on grain yield and quality of wheat and barley, J. Agric. Sci. (Camb.) 126 (1996) 379–385.
- [13] Guérif M., Duke C., Calibration of the SUCROS emergence and early growth module for sugar-beet using optical remote sensing data assimilation, Eur. J. Agron. 9 (1998) 127–136.
- [14] Guérif M., Beaudoin N., Dürr C., Houlès V., Machet J.M., Mary B., Moulin S., Richard G., Bruchou C., Michot D., Nicoullaud B., Designing a field experiment for assessing soil and crop spatial variability and defining site-specific management strategies, in: Agro Montpellier (Ed.), Proceedings of the 3rd ECPA, 2001, Montpellier, France, pp. 677–681.
- [15] Guérif M., Hollecker D., Beaudoin N., Bruchou C., Houlès V., Machet J.M., Mary B., Moulin S., Nicoullaud B., Site specific calibration of a crop model by assimilation of remote sensing data: a tool for diagnosis and recommendation in precision agriculture, in: Werner A., Jarfe A. (Eds.), Proceedings of the 4th ECPA, 2003, Berlin, Germany, pp. 253–258.
- [16] Hansen S., Jensen H.E., Nielsen N.E., Svendsen H., Simulation of nitrogen dynamics and biomass production in winter wheat using the Danish simulation model DAISY, Fert. Res. 27 (1991) 245– 259.
- [17] Horwitz W., Senzel A., Reynolds H., Official methods of analysis, 12th ed. AOAC, 1975, Washington, DC.
- [18] Houlès V., Guérif M., Mary B., Machet J.M., Makowski D., A method for optimising nitrogen fertilisation of wheat within a field based on crop model approach, in: Werner A., Jarfe A. (Eds.), Proceedings of the 4th ECPA, 2003, Berlin, Germany, pp. 437–438.
- [19] Jamieson P.D., Porter J.R., Goudriaan J., Ritchie J.T., Van Keulen H., Stol W., A comparison of the models AFRCWHEAT2, CERES-Wheat, Sirius, SUCROS2 and SWHEAT with measure-

ments from wheat grown under drought, Field Crops Res. 55 (1998) 23–44.

- [20] Jones J.W., Hoogenboom G., Porter C.H., Boote K.J., Batchelor W.D., Hunt L.A., Wilkens P.W., Singh U., Gijsman A.J., Ritchie J.T., The DSSAT cropping system model, Eur. J. Agron. 18 (2003) 235–265.
- [21] Justes E., Meynard J.M., Mary B., Plénet D., Diagnosis using stem base extract: JUBIL method, in: Lemaire G. (Ed.), Diagnosis of the nitrogen status in crop, Springer-Verlag, Berlin Heidelberg, 1997, pp. 163–187.
- [22] Kropff M.J., Bouma J., Jones J.W., Systems approaches for the design of sustainable agro-ecosystems, Agric. Syst. 70 (2001) 369–396.
- [23] Landau S., Mitchell R.A.C., Barnett V., Colls J.J., Craigon J., Moore K.L., Payne R.W., Testing winter wheat simulation models' predictions against observed UK grain yields, Agric. For. Meteorol. 89 (1998) 85–99.
- [24] Laurent F., Réponses du blé à l'azote : faut-il varier la dose d'azote en parcelles hétérogènes ? Perspect. Agric. 262 (2000) 62–69.
- [25] Loyce C., Rellier J.P., Meynard J.M., Management planning for winter wheat with multiple objectives (1): the BETHA system, Agric. Syst. 72 (2002) 9–31.
- [26] Machet J.M., Dubrulle P., Louis P., AZOBIL: a computer program for fertilizer N recommendations based on a predictive balance sheet method, Proceedings of the 1st ESA Congress, Paris, 1990, pp. 21–22.
- [27] Makowski D., Wallach D., How to improve model-based decision rules for nitrogen fertilization, Eur. J. Agron. 15 (2001) 197–208.
- [28] Makowski D., Wallach D., Meynard J.M., Statistical methods for predicting responses to applied nitrogen and calculating optimal nitrogen rates, Agron. J. 93 (2001) 531–539.
- [29] Mary B., Laurent F., Beaudoin N., La gestion durable de la fertilisation azotée, Proceedings of the IIRB Colloquium, Bruxelles, 2002, pp. 59–67.
- [30] Neeteson J.J., Development of N fertiliser recommendations for arable crops in the Netherlands in relation to nitrate leaching, Fert. Res. 26 (1990) 291–298.
- [31] Paz J.O., Batchelor W.D., Babcock B.A., Colvin T.S., Logsdon S.D., Kaspar T.C., Karlen D.L., Model-based technique to determine variable rate nitrogen for corn, Agric. Syst. 61 (1999) 69–75.
- [32] Peng S., Garcia F.V., LazaR.C., SanicoA.L., VisperasR.M., Cassman K.G., Increase N-use efficiency using a chlorophyll-meter on high-yielding irrigated rice, Field Crops Res. 47 (1996) 243–252.
- [33] Prévot L., Chauki H., Troufleau D., Weiss M., Baret F., Brisson N., Assimilating optical and radar data into the STICS crop model for wheat, Agronomie 23 (2003) 297–303.
- [34] Rémy J.C., Hébert J., Le devenir des engrais azotés dans le sol, C.R. Acad. Agric. Fr. 63 (1977) 700–710.
- [35] Shaffer M.J., Brodahl M.K., Rule-based management for simulation in agricultural decision support systems, Comput. Electron. Agric. 21 (1998) 135–152.
- [36] Schröder J.J., Neeteson J.J., Oenema O., Struik P.C., Does the crop or the soil indicate how to save nitrogen in maize production? Reviewing the state of the art, Field Crops Res. 66 (2000) 151– 164.
- [37] Stanford G., Rationale for optimum nitrogen fertilization in corn production, J. Environ. Qual. 2 (1973) 159–166.
- [38] Willmott C.J., On the validation of models, Phys. Geogr. 2 (1981) 184–194.