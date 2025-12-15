## 5. Experimental Design

### Block 1

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 3. Statistical Foundations > 3.5 Sample Size Determination

**Mapping:** score=0.61 reason=keyword:cluster|head='3.5 Sample Size Determination'

#### 3.5.1 Minimum Detectable Effect (MDE/MEI)
#### 3.5.2 Minimum Sample Size Calculation
#### 3.5.3 Average Sample Size (ASD)
#### 3.5.4 Test Duration Estimation
#### 3.5.5 Baseline Rate Uncertainty
#### 3.5.6 Cluster Design Effect & ICC

---

### Block 2

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 5. Experimental Design > 5.1 Design of Experiments (DOE)

**Mapping:** score=0.61 reason=keyword:design of experiments|head='5.1 Design of Experiments (DOE)'

#### 5.1.1 Factor Levels & Variables
##### 5.1.1.1 Independent Variables
##### 5.1.1.2 Dependent Variables
##### 5.1.1.3 Extraneous Variables
#### 5.1.2 Main Effects vs Interaction Effects
#### 5.1.3 Orthogonality & Confounding
#### 5.1.4 Aliasing in Fractional Designs
#### 5.1.5 Design Resolution

---

### Block 3

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 5. Experimental Design > 5.2 Randomization & Assignment

**Mapping:** score=0.61 reason=keyword:randomization|head='5.2 Randomization & Assignment'

#### 5.2.1 Randomization Units (User/Session/Geo)
#### 5.2.2 Simple Randomization
#### 5.2.3 Stratified Randomization & Blocking
#### 5.2.4 Cluster Randomization
#### 5.2.5 Matched Pairs Design
#### 5.2.6 Re-randomization for Balance
#### 5.2.7 Hash-Based Bucketing
#### 5.2.8 Sticky Assignment

---

### Block 4

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 5. Experimental Design > 5.4 Eligibility & Exposure

**Mapping:** score=0.61 reason=keyword:eligibility|head='5.4 Eligibility & Exposure'

#### 5.4.1 Eligibility Criteria
#### 5.4.2 Exposure & Trigger Events
#### 5.4.3 Attribution Windows
#### 5.4.4 Intention-to-Treat (ITT) vs Compliers (CACE)

---

### Block 5

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 5. Experimental Design > 5.6 Test Planning & Pre-Registration

**Mapping:** score=0.61 reason=keyword:pre-registration|head='5.6 Test Planning & Pre-Registration'

#### 5.6.1 Objective Definition
#### 5.6.2 Success Criteria & Decision Rules
#### 5.6.3 Pre-Registration & Analysis Plans
#### 5.6.4 Experiment Charter
#### 5.6.5 Resource Allocation

---

### Block 6

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 6. Implementation & Execution > 6.3 Data Collection & Tracking

**Mapping:** score=0.61 reason=keyword:exposure|head='6.3 Data Collection & Tracking'

#### 6.3.1 Event Tracking & Schema
#### 6.3.2 Exposure Logging
#### 6.3.3 Trigger Logging
#### 6.3.4 Data Pipeline Architecture (Telemetry/ETL)
#### 6.3.5 Telemetry Latency & SLAs
#### 6.3.6 Sampling for Cost Efficiency

---

### Block 7

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 8. Statistical Analysis Methods > 8.4 Standard Errors & Confidence Intervals

**Mapping:** score=0.61 reason=keyword:cluster|head='8.4 Standard Errors & Confidence Intervals'

#### 8.4.1 Robust Standard Errors (HC3)
#### 8.4.2 Cluster-Robust SE
#### 8.4.3 Delta Method for Ratios
#### 8.4.4 Fieller's Method for Ratio CIs
#### 8.4.5 Bootstrap Methods

---

### Block 8

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 14. Advanced Experimentation Topics > 14.1 Quasi-Experimental Methods

**Mapping:** score=0.642 reason=heading_fuzzy|head='14.1 Quasi-Experimental Methods'

#### 14.1.1 Difference-in-Differences (DiD)
#### 14.1.2 Synthetic Control Methods
##### 14.1.2.1 Traditional Synthetic Control
##### 14.1.2.2 SCUL (Lasso-Based)
##### 14.1.2.3 Bayesian Structural Time Series (BSTS)
##### 14.1.2.4 CausalImpact
#### 14.1.3 Regression Discontinuity (RD)
#### 14.1.4 Interrupted Time Series
#### 14.1.5 Instrumental Variables (IV)
#### 14.1.6 Propensity Score Methods
#### 14.1.7 Doubly Robust Estimation (AIPW)
#### 14.1.8 Sensitivity Analysis (Rosenbaum)

---

### Block 9

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 16. Incrementality & Media Testing > 16.2 Geo-Based Experiments

**Mapping:** score=0.61 reason=keyword:cluster|head='16.2 Geo-Based Experiments'

#### 16.2.1 Geo Experiment Design
#### 16.2.2 Market Clustering & Matching
#### 16.2.3 Pre/Post Normalization
#### 16.2.4 Matched Markets
#### 16.2.5 GeoLift Frameworks
#### 16.2.6 Spillover & Contamination
#### 16.2.7 Halo Effects

---

### Block 10

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 1\. Experiment Type Selection

**Mapping:** score=0.627 reason=heading_fuzzy|head='1\. Experiment Type Selection'

| Experiment Type | Use Cases | Complexity | Affirm Example |
| :---- | :---- | :---- | :---- |
| **A/B Testing** | • Single variable change • Clear binary choices • Simple implementation | Low | Testing two checkout button colors |
| **A/B/n Testing** | • Multiple variants • Exploring optimization curve • Finding local maxima | Medium | Testing 5 different payment plan displays |
| **Multivariate Testing (MVT)** | • Multiple variables simultaneously • Interaction effects • Complex UX changes | High | Testing button color × copy × position |
| **Multi-Armed Bandit** | • Dynamic allocation • Minimize opportunity cost • Continuous optimization | High | Optimizing interest rate offers in real-time |
| **Factorial Design** | • Full factorial (all combinations) • Fractional factorial • Systematic interaction study | Very High | Testing all combinations of 4 factors |
| **Sequential Testing** | • Early stopping rules • Adaptive designs • Resource optimization | High | Stopping test early if clear winner emerges |
| **Switchback Testing** | • Time-based allocation • Network effects • Market-level changes | Medium | Testing new merchant onboarding flow |
| **Synthetic Control** | • No randomization possible • Market-level rollouts • Causal inference | Very High | Launching in new geographic market |

---

### Block 11

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 4\. Monitoring & Quality Assurance > 4.1 Pre-Launch Checks

**Mapping:** score=0.61 reason=keyword:randomization|head='4.1 Pre-Launch Checks'

| Check Type | Methods | Critical Metrics | Affirm Example |
| :---- | :---- | :---- | :---- |
| **AA Testing** | Run control vs control | • Type I error rate • Randomization balance | 5% false positive rate confirmed |
| **Sample Ratio Mismatch** | Chi-square test on assignment | • Expected vs actual ratio • P-value \< 0.001 flags issue | 50.1% vs 49.9% (acceptable) |
| **Covariate Balance** | • T-tests on features • Standardized differences | • Age, income, credit score • \<0.1 std dev difference | All user attributes balanced |
| **Technical Validation** | • Logging verification • Event tracking • Edge cases | • 100% event capture • No data loss | All checkout events tracked |
| **Canary Deployment** | Gradual rollout | • Error rates • Performance metrics | 1% → 5% → 25% → 50% |

---

### Block 12

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 8\. Advanced Topics & Considerations > 8.1 Network Effects & Interference

**Mapping:** score=0.61 reason=keyword:randomization|head='8.1 Network Effects & Interference'

| Type | Detection Method | Mitigation | Affirm Example |
| :---- | :---- | :---- | :---- |
| **Direct Network Effects** | • Cluster randomization • SUTVA violations | • Market-level randomization • Synthetic control | Merchant referral programs |
| **Indirect Effects** | • Spillover analysis • Spatial models | • Buffer zones • Cluster designs | User word-of-mouth |
| **Competitive Effects** | • Game theory models • Market share analysis | • Simultaneous moves • Strategic timing | Competitor response to pricing |
| **Platform Effects** | • Two-sided markets • Feedback loops | • Careful measurement • Dynamic models | Merchant-consumer interactions |

---

### Block 13

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 10\. Example End-to-End Experiment: Affirm Checkout Optimization > Stage 2: Design

**Mapping:** score=0.61 reason=keyword:randomization|head='Stage 2: Design'

**Type:** A/B test with 50/50 split

**Randomization:** Hash-based on user ID

**Duration:** 3 weeks (full purchase cycle)

---

### Block 14

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Experiment Target Types & Examples > Stage 1: Experiment Objectives

**Mapping:** score=0.61 reason=keyword:exposure|head='Stage 1: Experiment Objectives'

| Target Type | Experiment Sample Targeting |
| :---- | :---- |
| **Conversion Rate Optimization (CRO)** | Test new page layout for prequalification form to increase completion rate (Single Item Profiling, Mad-Libs Engagement) |
| **Email & Lifecycle Marketing** | A/B test email subject lines with vs. without personalized loan limit offers to increase open and click rates |
| **Landing Page UX/UI** | Multivariate test of CTA button color, placement, and messaging on merchant checkout pages |
| **Merchant Integration Testing** | Test adding "As low as $X/mo with Affirm" messaging under product listings vs. only on the product detail page |
| **Checkout Funnel Optimization** | Run holdout test: remove Affirm as a payment option from 10% of merchant checkouts to measure incremental lift |
| **Cross-Sell & Upsell Campaigns** | Test impact of promoting second loan offer at different lifecycle stages (e.g., right after full repayment) |
| **Loan Approval Journey** | Test different order of disclosures or rephrased questions in the application process to reduce drop-off |
| **Push Notification Timing** | Experiment with delivery times (e.g., lunch vs. evening) to maximize tap-through and engagement rate |
| **Merchant Category Messaging** | Test customized financing terms (e.g., "No payments for 6 months") messaging in specific categories like travel |
| **Ad Channel Performance** | Split-test display vs. social media remarketing to determine highest downstream loan conversion per dollar spent |
| **Pricing Sensitivity** | Test impact of offering 0% APR promotional loans vs. standard 10–30% APR options on take rate and default rate |
| **Fraud Prevention and Risk Modeling** | Test identity verification steps (e.g., selfie \+ ID match) for new users vs. relaxed flow on drop-off rate |
| **Merchant Widget Optimization** | A/B test embedded monthly installment calculator on merchant PDPs vs. static monthly pricing copy |
| **Product Feature Adoption** | Test exposure to BNPL explainer video vs. static FAQ on user education and engagement |
| **Personalization / Segmentation** | Test personalized financing term recommendations (based on user profile) vs. default offer to improve uptake |
| **Nudges & Behavioral Design** | Test adding scarcity language ("Last chance for 0% financing\!") in email footers to improve click-to-apply rate |
| **App vs. Web Performance** | Test identical email-to-checkout journeys routed to mobile app vs. mobile web to measure channel conversion lift |
| **Trust Signal Placement** | Test positioning of FDIC insurance badge and data privacy seals during financing to increase user confidence |
| **Checkout Form Field Order** | Test alternative sequences of form fields (e.g., income → employment vs. employment → income) to reduce friction |
| **Incentive Testing** | Test $10 Affirm credit vs. no credit for completing onboarding to increase loan origination volume |

---

### Block 15

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 2\. Experiment Design (The Engine Room) > **2.3. Control Mechanisms**

**Mapping:** score=0.61 reason=keyword:randomization|head='**2.3. Control Mechanisms**'

* Randomization: Avoid bias.

* Stratification: Ensure balance across segments (e.g. new vs. returning users).

* Blinding (if applicable): Prevent knowledge of assignment.

---

### Block 16

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 5\. Advanced Topics in Experimentation > **5.3. Experimentation Platforms**

**Mapping:** score=0.61 reason=keyword:trigger|head='**5.3. Experimentation Platforms**'

* Internal vs. External tools (e.g., Optimizely, Google Optimize, Meta Experiments)

* Requirements for event tracking, group assignment, trigger logic, and result pipelines

---

### Block 17

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 9\) Measuring the incrementality of Facebook retargeting for Airbnb

**Mapping:** score=0.61 reason=keyword:randomization|head='9\) Measuring the incrementality of Facebook retargeting for Airbnb'

Gold-standard options:

A) Facebook Conversion Lift (randomized holdouts)

* Randomly hold out a % of eligible users from auction. Measure treatment vs. holdout conversions on Airbnb’s site (server-to-server conversion API ideal).

* Compute incremental conversions (=) (C\_{\\text{exposed}} \- C\_{\\text{holdout}}).

* iROAS (= \\frac{\\text{Incremental revenue}}{\\text{Ad spend}}). Consider attribution windows, post-view vs. post-click.

B) Ghost Ads (if platform supports)

* Everyone is auctioned as if; some who would have been shown ads are withheld (ghosted). This preserves equal auction intent, minimizing selection bias.

C) Geo-level experiments (Geo-Lift / SCM)

* Turn spend on vs. off across matched DMAs/countries; analyze with Geo-Lift or synthetic control over multiple weeks. Good when user-level randomization isn’t possible.

Airbnb example numbers (illustrative):

* Exposed group uplift in bookings vs. holdout: \+0.8pp (from 5.2% → 6.0%).

* Incremental bookings \= (N \\times 0.008). Multiply by average incremental booking revenue (be careful with cannibalization/organic).

* If spend \= $500k and incremental revenue \= $650k ⇒ iROAS \= 1.3.

* Layer saturation curves (Diminishing returns) and carryover (adstock) if looking at multi-week effects.

Pitfalls to mention in interview:

* Cross-device identity match, cookie loss.

* Auction interference across experiments.

* Post-view conversions: ensure viewability standards.

* Contamination (users in both test and holdout across campaigns). Use consented, durable IDs and exposure bucketing.

---

### Block 18

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Experiment Design

**Mapping:** score=0.872 reason=heading_fuzzy|head='Experiment Design'

5\. Null Hypothesis – Inferential statistics is based on the premise that you cannot prove something to be true but you can disprove something by finding an exception. You decide what you are trying to provide evidence for – which is the alternate hypothesis, then you set up the opposite as the null hypothesis and find evidence to disprove that. In our A/B test example, the null hypothesis is that the population CTR on the original page and the page variation are not different.

![Image by Author][image9]Image by Author

6\. Key Metric/s – A set of metrics that you are trying to optimize through the experiment. Some commonly used metrics are click through rates (CTR), sign up rate, engagement rate, average revenue per order, retention rates etc. As you can imagine key metrics are going to relate to the priorities of the business, OKRs and goals. Many organizations examine multiple key metrics, and have a mental model of the trade offs they are willing to accept when they see a particular combination. For e.g., they may have a good idea about how much they are willing to lose users (increase in churn) if the remaining users increase their engagement and revenue. This brings us to OEC explained below.

7\. Overall Evaluation Criteria (OEC) – When there are multiple metrics to be optimized through the experiment, it is helpful to formulate trade-offs by devising a single metric called an Overall Evaluation Criteria (OEC) – which is essentially a weighted combination of such objectives. One way to do this is to normalize each metric to a predefined range, say 0–1, and assign each a weight. Your OEC then is the weighted some of the normalized metrics. In the example above with needing to evaluate trade-off between churn and revenue, LTV can be used as an OEC.

8\. Guardrail Metrics – These are metrics that are important for the company and should not be negatively impacted by the experiment. For e.g. our goal may be to get as many users as possible to register, but we don’t want the per-user engagement level to drop drastically. Or we may want to increase app engagement but at the same time ensure that app uninstalls do not increase.

9\. Randomization Unit – This is the unit e.g. users or pages that a randomization process is applied to map them to either control or treatment. Proper randomization is important to ensure that populations assigned to the different variants are similar statistically. Randomization unit should be chosen such that Stable unit treatment value assumptions (SUTVA) are satisfied. SUTVA states that experiment units do not interfere with one another i.e. the behavior of units in test and control is independent of each other. User-level randomization is the most common as it avoids inconsistent experience for the user and allows for long-term measurement such as user retention.

10\. Interference – Sometimes also called spillover or leakage occurs when the behavior of the control group is influenced by the treatment given to the test group. This leads to a violation of SUTVA assumption which results in potentially incorrect conclusions. There are two ways inference may arise –

* Direct – two units can be directly connected if they are friends on a social network or if they visited the same physical space at the same time. If one of these is assigned to Treatment and other to control, this will cause interference between variants

* Indirect – indirect connections are connections that exist because of certain shared resources. For e.g. If the Airbnb marketplace improved conversion flow for treatment users, resulting in more bookings, it would naturally lead to less inventory for Control users. Similarly marketplaces such as Lyft/Uber/Doordash where users in control and treatment might share the same pool of drivers/dashers will also face interference

---

### Block 19

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Key Sections in Detail** > **4\. Design and Execution of Experiments**

**Mapping:** score=0.61 reason=keyword:exposure|head='**4\. Design and Execution of Experiments**'

The process involves:

* **Define Goals**: Be precise about what success looks like.

* **Identify Units of Analysis**: User, session, cookie, etc.

* **Randomize and Assign**: With stable identifiers.

* **Triggering Logic**: Decide who qualifies for the experiment.

* **Run and Ramp Up**: Start small (1% exposure) and increase only if things are stable.

* **Analyze Results**: Use pre-registered hypotheses and don’t peek at the data.

Technical details like **exposure logging**, **bucketing**, and **triggering** are crucial to execution. Incorrect logging can lead to false insights.

---

### Block 20

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Next-Level A/B Testing: Repeatable, Rapid, and Flexible Product Experimentation > In-Depth Summary of Key Topics > **Chapter 5: Verifying and Monitoring Experiments**

**Mapping:** score=0.61 reason=keyword:ramp|head='**Chapter 5: Verifying and Monitoring Experiments**'

This chapter focuses on the tools and processes needed to ensure experiment quality.

• Pre-Launch Verification:

    \- Internal QA Tool: An application that allows engineers to spot-check the experience of a single user for any test variant without affecting live users.

    \- Experiment Canaries: Launching a test to a very small percentage of traffic (e.g., 1%) for a short duration to validate its technical performance and catch issues before a full-scale ramp-up.

• Platform Health: The source recommends running periodic A/A tests (exposing two identical groups to the same experience) to verify that the underlying experimentation infrastructure is working correctly and not introducing bias.

• Active Monitoring: The importance of automated systems to monitor active experiments for issues like metric degradations or data quality problems is emphasized, allowing teams to catch problems early.

---

### Block 21

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Ace A/B Testing Interview Question: A Data-driven Approach for Data Scientists > My Videos on A/B Testing

**Mapping:** score=0.61 reason=keyword:randomization|head='My Videos on A/B Testing'

In my AB testing playlist. You can see I have talked about topics such as choosing randomization units, metric selection, sample size estimation, common AB testing mistakes and AB testing, real life example. So this playlist will be helpful for you to build up the foundation on AB testing.

---

### Block 22

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Ace A/B Testing Interview Question: A Data-driven Approach for Data Scientists > The Design Question

**Mapping:** score=0.61 reason=keyword:randomization|head='The Design Question'

question and that is the design question. As you can tell from the diagram I showed you earlier, it is by large the most important AB testing interview question. I will make follow-up videos to cover other topics, so stay tuned for future videos and let's dive into the most common AB testing interview question: the design question. As we talked about earlier, the design question accounts for over 30% of AB testing interview questions. That's one out of three. So it's a pretty big percentage, right?

A typical format of this type of question is a company is considering designing a new feature or changing something in the product. How do you design a test to evaluate the effectiveness of this change? The goal is to make sure this change is beneficial for the users or the business. For example, Uber is considering launching a new referral program to get new riders. How do you design a test to evaluate the effectiveness of this program? Another example could be TikTok is thinking about launching this new repost feature that allows users to amplify their videos by sending those videos to their followers. How do you design a test to evaluate the effectiveness of this new feature? This sounds to be a very broad question. Is it? Designing a test involves multiple steps such as selecting the right metric, choosing the right randomization unit, calculating the sample size and test duration, determining the minimum detectable effect, et cetera.

So how do you handle this type of broad question? Now, before we dive into the strategy to handle this type of question, if you need refreshers on different components that involves

Refresher in designing a test, I have this playlist that covers different topics such as choosing randomization units, metric selection, sample size estimation, and common mistakes in AB testing. So feel free to watch those videos to refresh your memory on how to design a test.

---

### Block 23

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > When (and when not) to do product experimentation > Experiment when…

**Mapping:** score=0.684 reason=heading_fuzzy|head='Experiment when…'

You’re making decisions that are uncertain, reversible, and measurable. If you’re launching a new onboarding flow, tweaking pricing strategies, or testing different layouts for a conversion-critical page, experimentation will give you the clarity to move forward with confidence.

One company running effective experiments efficiently and systematically is Bolt, the first European super-app offering ride-hailing, shared vehicles, food delivery, and more across over 500 cities. The team needed a reliable way to understand user behavior and make faster, smarter product decisions. Experimentation became a core part of their strategy to optimize features, reduce friction, and align product improvements with key business outcomes.

“On the consumer side, our teams used Mixpanel to determine if removing surge pricing for ride-hailing would result in higher conversion rates,” [says Nikita Strezhnev](https://mixpanel.com/customers/bolt-the-first-european-super-app-uses-mixpanel-to-fuel-its-growth-strategy/), Data Analytics Manager at Bolt. 

“This was difficult to see at a high level, but Mixpanel provided the granularity and certainty to move beyond the ‘should we do it, or should we not’ question that often holds up so much product development.”

The result? Bolt reduced ride cancellations by 3%, freed up 15% of Android developer capacity, and doubled the number of internal users accessing product data, while deepening a culture of experimentation and insight-driven decision making.

---

### Block 24

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Product experimentation frameworks: The basics > Common experiment types

**Mapping:** score=0.622 reason=heading_fuzzy|head='Common experiment types'

Different problems call for different testing methods. Here are the most common types of product experiments:

* A/B testing: The classic test: show two versions (A and B) to separate user groups and measure which performs better. Ideal for testing single-variable changes like a CTA, image, or layout.

* Multivariate testing: Test multiple elements (like headline \+ button \+ color) simultaneously to see how combinations perform. Best for high-traffic areas where you can afford the complexity.

* Feature flags: Turn features on or off for certain users, without deploying new code. Flags make it easy to test behind the scenes, personalize experiences, or gradually introduce changes.

* Phased rollouts: Slowly release a feature to an increasing percentage of users while monitoring key metrics in real time. Great for managing risk when you have to move fast.

Mixpanel tip: Not every experiment needs to be flashy or complex. Sometimes, a small tweak to copy, button placement, or micro-interactions can lead to major wins.

---

### Block 25

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Step-by-step guide to running an experiment > 4\. Implement your experiment (feature flags \+ tracking)

**Mapping:** score=0.61 reason=keyword:exposure|head='4\. Implement your experiment (feature flags \+ tracking)'

Once the experiment is defined, it’s time to build and ship it safely.

* Use [feature flags](https://mixpanel.com/blog/feature-flags-and-product-analytics-working-together/) to control exposure. Look for tools that make it easy to roll out new features to just a portion of your users and answer questions like, “What did my users do after being exposed to an experiment?” and “Did users who were exposed convert better than users who didn’t?”

* Add analytics tracking upfront. Make sure your events and properties are firing properly before going live. Tag the experiment ID or variant name for segmentation later.

* QA everything. Double-check that both control and variant experiences work as expected across devices and user segments.

---


