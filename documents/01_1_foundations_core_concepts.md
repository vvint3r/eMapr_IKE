## 1. Foundations & Core Concepts

### Block 1

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 1. Foundations & Core Concepts > 1.1 Introduction to Experimentation

**Mapping:** score=0.61 reason=keyword:introduction|head='1.1 Introduction to Experimentation'

#### 1.1.1 What is A/B Testing
#### 1.1.2 History and Evolution
#### 1.1.3 Scientific Method Application
#### 1.1.4 Causality vs Correlation
#### 1.1.5 When to Use A/B Testing

---

### Block 2

**Source:** `md`  
**Original headings:** Marketing Experimentation > Interview Preparation Framework

**Mapping:** score=0.61 reason=keyword:what is|head='Interview Preparation Framework'

When you get an experimentation question, structure your answer using this framework:

1. **Understand the Business Goal:** "What is the product/marketing team *actually* trying to achieve?"  
2. **Formulate a Hypothesis:** "I would frame the test around the hypothesis that..."  
3. **Define the Experiment:**  
   * **Variants:** What are the control and treatment(s)?  
   * **Unit of Diversion:** Who are we randomizing? (User-ID, Listing-ID).  
   * **Population:** Who is in the experiment?  
4. **Identify Key Metrics:**  
   * Primary Metric (The decider)  
   * Guardrail & Counter Metrics (The safeguards)  
5. **Plan the Execution:**  
   * How long will you run it? (Mention weekly cycles, power analysis).  
   * What will you do first after launch? (Sanity checks on invariant metrics).  
6. **Analyze & Conclude:**  
   * How will you interpret the results? (Look at p-values, confidence intervals, and effect sizes).  
   * Will you segment the results? (By region, user type).  
   * What are potential pitfalls? (Novelty effect, network effects).

---

---

### Block 3

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Types of Analytics in Statistics > Predictive Analytics

**Mapping:** score=0.61 reason=keyword:what is|head='Predictive Analytics'

Predictive analytics forecasts what is likely to happen in the future, providing businesses with data-driven, actionable insights. Once an organization has a firm grasp on what happened (descriptive analytics) and why it happened (diagnostic analytics), it can advance to predictive analytics. This advanced form of analytics seeks to answer the question "What is likely to happen?" by utilizing data and knowledge.

**The transition from diagnostic to predictive analytics is critical for organizations:**

**Key techniques in predictive analytics include:**

- Multivariate analysis  
- Forecasting  
- Multivariate statistics  
- Pattern matching  
- Predictive modeling

**Implementing these techniques can be challenging due to:**

- The need for large amounts of high-quality data  
- A thorough understanding of data science, statistics, and programming languages like R and Python  
- Many organizations may lack the internal expertise required for effective implementation  
- The potential value of predictive analytics is significant

**For example, predictive models can:**

- Use historical data to forecast the impact of marketing campaigns on customer engagement  
- Accurately identify which actions lead to specific outcomes  
- Predict future actions that will achieve desired results

These insights are crucial for advancing in the analytics journey.

---

### Block 4

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Relationship Between Variables > Causality

**Mapping:** score=0.61 reason=keyword:causality|head='Causality'

The term "causation" refers to a relationship between two events in which one is influenced by the other. There is causality in statistics when the value of one event, or variable, increases or decreases as a result of other events.

Each of the events we observe may be thought of as a variable, and as the number of hours worked increases, so does the amount of money earned. On the other hand, if you work fewer hours, you will earn less money.

---

### Block 5

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Hypothesis Frameworks > Other Formats

**Mapping:** score=0.61 reason=keyword:scientific method|head='Other Formats'

- **Problem-Solution-Result**: Define problem → propose solution → expected result  
- **Jobs-to-be-Done**: Focus on user need fulfillment  
- **Lean Hypothesis**: Rapid testing framework  
- **Scientific Method**: Formal hypothesis testing

---

### Block 6

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 2\. Statistical Framework & Power Analysis > 2.2 Sample Size Calculation Methods

**Mapping:** score=0.61 reason=keyword:when to use|head='2.2 Sample Size Calculation Methods'

| Method | Formula/Approach | When to Use | Affirm Example |
| :---- | :---- | :---- | :---- |
| **Classical Power Analysis** | n \= 2σ²(Z\_α/2 \+ Z\_β)²/δ² | Standard A/B tests | 15,000 users per variant for 80% power |
| **Minimum Detectable Effect** | MDE \= (Z\_α/2 \+ Z\_β)√(2σ²/n) | Fixed sample constraint | Can detect 0.5% lift with current traffic |
| **Sequential Analysis** | Alpha spending functions | Continuous monitoring | Check results daily with adjusted p-values |
| **Bayesian Sample Size** | Posterior probability thresholds | Prior information available | 95% probability variant is 2% better |
| **Simulation-Based** | Monte Carlo methods | Complex designs | Simulate 10,000 experiments |
| **Adaptive Designs** | Information-based stopping | Efficient resource use | Stop when confidence interval \< 0.1% |

---

### Block 7

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 3\. Experiment Design & Implementation > 3.1 Randomization Strategies

**Mapping:** score=0.61 reason=keyword:history|head='3.1 Randomization Strategies'

| Strategy | Implementation | Pros/Cons | Affirm Use Case |
| :---- | :---- | :---- | :---- |
| **Simple Random** | Random number generator | Pro: Unbiased Con: Imbalanced groups | Basic feature tests |
| **Block Randomization** | Randomize within blocks | Pro: Balance covariates Con: Complex | Balance by merchant type |
| **Stratified Random** | Random within strata | Pro: Representative Con: Need strata info | Ensure all credit tiers represented |
| **Cluster Randomization** | Randomize groups | Pro: Avoid contamination Con: Less power | Randomize by merchant |
| **Matched Pairs** | Match then randomize | Pro: Increased power Con: Matching complexity | Match users by purchase history |
| **Hash-Based** | Deterministic hashing | Pro: Consistent Con: Predictable | User ID % 100 \< 50 |
| **Time-Based** | Temporal allocation | Pro: Simple Con: Time confounds | Day-of-week randomization |
| **Geo-Based** | Geographic clustering | Pro: Market-level Con: Spillover effects | Test in specific states |

---

### Block 8

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Marketing Experimentation

**Mapping:** score=0.61 reason=keyword:introduction|head='Marketing Experimentation'

**Introduction**

* Experimentation measures causal impact of marketing changes.

* It drives allocation, product-market fit, and growth.

**General overview**

* Types: A/B, A/B/n, multivariate, geo-holdout, switchback, staggered  
   rollout, incrementality tests, uplift modeling validations.

* Goals: estimate lift, reduce bias, inform rollout decisions.

**Key concepts**

* Units: user, session, device, geo, time.

* Randomization: stable IDs, stratification, hashing.

* Outcomes: conversion rate, revenue per user, LTV, CAC, iROAS, brand lift.

* Design: hypothesis, primary metric, guardrails, MDE, power, alpha.

* Sample size: baseline rate, MDE, power (≥80%), two-sided alpha (≤5%).

* Tracking: exposure definition, attribution window, event dedupe.

* Validity threats: SRM, interference, seasonality, novelty, selection,  
   cannibalization, attribution drift.

* Analysis: difference-in-means, regression with covariates, CUPED,  
   DiD, quantile effects, heterogeneity by segment.

* Multiple testing: Bonferroni, Holm, BH/FDR; pre-register metrics.

* Sequential looks: group-sequential, alpha spending, SPRT, Bayesian  
   monitoring with stopping rules.

* Power pitfalls: underpowering, early stopping bias, peeking.

* Decision rules: uplift \> cost threshold, guardrails within bounds,  
   risk-adjusted ROI, rollout by strata.

* Ops: experiment registry, review board, naming conventions, metrics  
   contracts, telemetry QC, SRM alarms.

* Ethics: fairness across segments, consent for brand studies.

---

---

### Block 9

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Comprehensive Guide to Experimentation in Marketing and Product: An Airbnb-Focused Framework

**Mapping:** score=0.61 reason=keyword:scientific method|head='Comprehensive Guide to Experimentation in Marketing and Product: An Airbnb-Focused Framework'

This comprehensive resource provides an end-to-end view of experimentation in the context of marketing and product development, specifically aligned with Airbnb's advanced analytics practices. Drawing from industry best practices and Airbnb's proven methodologies, this guide addresses the three core competencies essential for marketing analytics leadership: experimentation understanding, product sense, and cross-functional collaboration.

**Executive Summary**

Experimentation has evolved from simple A/B testing to a sophisticated discipline that drives strategic business decisions. At Airbnb, experimentation is foundational to product development, with the company running over 700 experiments weekly. This systematic approach has enabled Airbnb to scale from a small startup to a global platform facilitating over 2 billion guest arrivals. The key to successful experimentation lies not just in technical execution, but in building organizational capabilities that connect testing insights to business outcomes while fostering collaboration across teams.\[1\]\[2\]

**Fundamental Principles of Marketing and Product Experimentation**

**The Scientific Foundation**

Modern experimentation in marketing and product development builds upon the scientific method, requiring structured hypothesis formation, controlled testing, and evidence-based decision-making. This approach moves organizations beyond intuition-driven decisions toward data-informed strategies that can be validated, scaled, and replicated.\[3\]\[4\]

**Core Elements of Experimental Design:**

\- **Hypothesis Formation**: Developing testable predictions based on user research, business insights, and strategic objectives

\- **Variable Control**: Isolating specific changes to measure their independent impact

\- **Randomization**: Ensuring unbiased assignment to treatment and control groups

\- **Statistical Rigor**: Applying appropriate statistical methods to interpret results with confidence

**Types of Experimentation Approaches**

**A/B Testing**: The foundation of experimentation, comparing two versions to determine which performs better. A/B testing provides clear, statistically significant results when properly designed and executed.\[4\]\[5\]

**Multivariate Testing**: Simultaneously testing multiple variables to understand interaction effects and optimize complex user experiences.\[6\]\[7\]

**Multi-Armed Bandits (MAB)**: Dynamic testing approaches that automatically allocate traffic to better-performing variations, particularly valuable for optimization scenarios where learning and earning must be balanced.\[8\]\[9\]

**Interleaving**: Advanced method used by Airbnb for search ranking experiments, providing up to 50x faster results than traditional A/B testing for ranking algorithms.\[10\]\[11\]

![][image1]

Airbnb Experimentation Portfolio Dashboard \- Overview of experiment types, performance, and revenue impact

**Airbnb's Experimentation Excellence**

**Cultural Foundation and Organizational Structure**

Airbnb's experimentation success stems from embedding data-driven decision-making into the organization's DNA from its early stages. The company hired its first data scientist as employee number 10, establishing the importance of experimentation before significant scale. This early investment created a foundation where "controlled experiments are used to learn and make decisions at every step of product development, from design to algorithms".\[1\]\[2\]

**Key Cultural Elements:**

\- **Hypothesis-Led Approach**: Every experiment begins with a specific, measurable hypothesis grounded in user research or business insights

\- **Learning-Focused Mindset**: Both successful and failed experiments are valued for the insights they provide

\- **Cross-Functional Integration**: Data scientists are embedded within product teams rather than operating as a separate function

\- **Rapid Experimentation Cadence**: Maintaining velocity through systematic processes and dedicated infrastructure

**Airbnb's North Star Metric Framework**

Central to Airbnb's experimentation strategy is alignment around a clear North Star metric: **nights booked**. This metric captures the core value exchange of the platform—connecting travelers with unique places to stay—while directly linking to revenue growth and user satisfaction.\[2\]\[12\]

**Why "Nights Booked" Works:**

\- **Dual Value Capture**: Represents value for both guests (finding accommodation) and hosts (monetizing space)

\- **Revenue Alignment**: Directly correlates with platform fees and business growth

\- **Product-Led Focus**: Improvements in search, booking flow, and host tools all contribute to this metric

\- **Cross-Functional Clarity**: All teams can understand how their work impacts this outcome

![][image2]

Airbnb North Star Metrics Performance \- Nights Booked and Supporting KPIs Over Time

**Advanced Experimentation Methods at Airbnb**

**Interleaving for Search Ranking**: Airbnb developed sophisticated interleaving systems that blend results from control and treatment search algorithms, enabling direct user preference measurement. This approach provides significantly faster insights than traditional A/B testing for ranking improvements.\[10\]\[11\]

**Variance Reduction Techniques**: The company employs advanced statistical methods, including using in-experiment data for variance reduction, improving the precision and power of their experiments.\[13\]

**Multi-Level Experimentation**: Airbnb runs experiments across different organizational levels—from micro-optimizations like button colors to major product launches—ensuring comprehensive coverage of optimization opportunities.\[1\]\[14\]

**Statistical Methods and Measurement Frameworks**

**Power Analysis and Sample Size Determination**

Proper experimental design requires determining appropriate sample sizes to detect meaningful effects with sufficient statistical power. The relationship between effect size, sample size, power, and significance level forms the foundation of reliable experimentation.\[15\]\[16\]

**Key Parameters:**

\- **Power (1-β)**: Typically set at 0.8, representing 80% probability of detecting a true effect

\- **Significance Level (α)**: Usually 0.05, controlling false positive rate

\- **Minimum Detectable Effect (MDE)**: The smallest practically important difference you want to detect

\- **Baseline Conversion Rate**: Historical performance informing expected variation

**Sample Size Considerations:**

\- Larger samples provide more precise estimates but require more time and resources

\- Statistical significance alone doesn't guarantee practical significance

\- Consider clustering effects if randomizing at group rather than individual level

**Causal Inference in Marketing Attribution**

Traditional attribution models often confuse correlation with causation, leading to suboptimal budget allocation and strategy decisions. Causal inference methods help identify true incremental impact by accounting for external factors and confounding variables.\[17\]\[18\]

**Advanced Attribution Methods:**

\- **Marketing Mix Modeling (MMM)**: Analyzing historical data to understand media contribution while controlling for external factors

\- **Incrementality Testing**: Controlled experiments measuring additional impact from marketing activities

\- **Natural Experiments**: Leveraging external events that create quasi-random treatment assignment

\- **Regression Analysis**: Statistical modeling with proper controls to isolate causal relationships

![][image3]

Airbnb Customer Journey Optimization \- Conversion Funnel A/B Test Results

**Conversion Funnel Optimization**

Understanding and optimizing the customer journey requires systematic analysis of how users progress through different stages, from initial awareness to final conversion. Airbnb's complex booking funnel—from search to confirmed booking—provides multiple optimization opportunities.\[19\]\[20\]

**Funnel Analysis Framework:**

\- **Stage Definition**: Clear identification of key milestones in the user journey

\- **Conversion Rate Measurement**: Tracking percentage of users progressing between stages

\- **Drop-off Analysis**: Identifying friction points causing user abandonment

\- **Segmentation**: Understanding how different user types behave throughout the funnel

**Cross-Functional Collaboration and Communication**

**Stakeholder Alignment and Communication**

Effective experimentation requires strong collaboration across diverse stakeholders, each with different perspectives, priorities, and expertise. Success depends on establishing clear communication protocols and shared understanding of experimental goals and results.\[21\]\[22\]

**Stakeholder Categories:**

\- **Supportive Stakeholders**: Teams aligned with experimental goals (product, growth, data science)

\- **Mixed Blessing Stakeholders**: Leaders concerned about risks but supportive of learning (executives, legal)

\- **Marginal Stakeholders**: Teams indirectly affected by results (customer service, operations)

**Communication Best Practices:**

\- **Audience-Tailored Messaging**: Executive summaries focus on business impact, while technical teams need methodological details

\- **Visual Storytelling**: Charts and dashboards make complex results accessible to non-technical stakeholders

\- **Context Provision**: Explaining the business problem, methodology, and implications of findings

\- **Action-Oriented Recommendations**: Clear next steps based on experimental results

**Building Cross-Functional Experimentation Teams**

Successful experimentation requires diverse expertise working toward shared objectives. Airbnb's embedded model, where data scientists work directly within product teams, exemplifies effective cross-functional collaboration.\[23\]\[24\]

**Team Composition Elements:**

\- **Product Managers**: Define business requirements and prioritize experiments

\- **Data Scientists**: Design experiments, analyze results, and provide statistical guidance

\- **Engineers**: Implement experimental variations and measurement infrastructure

\- **Designers**: Create user experience variations while maintaining design consistency

\- **Marketing Teams**: Align experiments with customer acquisition and retention strategies

**Collaboration Success Factors:**

\- **Shared Goals**: All team members working toward common objectives and metrics

\- **Regular Communication**: Structured touchpoints throughout experimental lifecycle

\- **Clear Roles**: Defined responsibilities preventing duplication and gaps

\- **Learning Culture**: Emphasis on knowledge sharing and continuous improvement

**Implementation Framework for Systematic Experimentation**

**Experimental Design Process**

**Phase 1: Problem Definition and Hypothesis Formation**  
 Begin each experiment with clear business objectives and testable hypotheses. Successful hypotheses are specific, measurable, and grounded in user research or business insights.\[3\]\[25\]

*Example*: "Simplifying the booking form by reducing required fields from 8 to 5 will increase completion rates by 15% because user research indicates form length is a primary abandonment reason."

**Phase 2: Experimental Design and Setup**  
 Design experiments with appropriate methodology, sample sizes, and success metrics. Consider technical implementation requirements and potential confounding factors.\[4\]\[26\]

**Phase 3: Implementation and Monitoring**  
 Deploy experiments with proper tracking and monitoring systems. Establish processes for early detection of technical issues or unexpected results.\[27\]\[28\]

**Phase 4: Analysis and Interpretation**  
 Apply rigorous statistical analysis while considering business context and practical significance. Look beyond primary metrics to understand broader impact.\[29\]\[30\]

**Phase 5: Decision Making and Follow-up**  
 Make data-informed decisions about implementation, scaling, or iteration. Document learnings for future reference and organizational knowledge building.

**Metrics Selection and Measurement**

**Primary Metrics**: Core business outcomes directly related to experimental hypotheses. These should align with North Star metrics and strategic objectives.\[31\]\[32\]

**Secondary Metrics**: Supporting measurements that provide context and guard against negative unintended consequences. Examples include user experience metrics, engagement indicators, and operational metrics.

**Guardrail Metrics**: Protective measures ensuring experiments don't harm critical business functions or user experiences. These might include revenue per user, customer satisfaction scores, or system performance metrics.

Experimentation Maturity Framework \- Progression from Basic Testing to Advanced Experimentation Culture

**Advanced Experimentation Topics**

**Multi-Armed Bandits and Dynamic Allocation**

Multi-armed bandits represent a sophisticated approach to experimentation that balances exploration (learning about different options) with exploitation (capitalizing on current best performers). This methodology is particularly valuable in scenarios where opportunity cost of suboptimal allocation is high.\[8\]\[33\]

**When to Use MAB:**

\- Email subject line testing where better performance should receive more traffic

\- Dynamic pricing experiments where market conditions change rapidly

\- Content recommendation systems requiring continuous optimization

\- Seasonal campaigns with limited time windows

**MAB Algorithms:**

\- **Epsilon-Greedy**: Simple approach balancing random exploration with exploitation

\- **Upper Confidence Bound (UCB)**: Sophisticated method using confidence intervals to guide selection

\- **Thompson Sampling**: Bayesian approach sampling from posterior distributions

**Causal Inference and Observational Data**

When randomized experiments aren't feasible, causal inference methods help extract insights from observational data while accounting for confounding factors. These techniques are crucial for understanding long-term effects and complex customer journeys.\[34\]\[35\]

**Key Methods:**

\- **Difference-in-Differences**: Comparing treatment and control groups before and after intervention

\- **Regression Discontinuity**: Exploiting arbitrary cutoffs in treatment assignment

\- **Instrumental Variables**: Using external factors that affect treatment but not outcomes directly

\- **Propensity Score Matching**: Controlling for selection bias in treatment assignment

**Experimentation Infrastructure and Platforms**

Scaling experimentation requires robust technological infrastructure supporting rapid test deployment, accurate measurement, and reliable analysis. Modern platforms must handle complex scenarios including multiple concurrent experiments, sophisticated targeting, and real-time monitoring.\[14\]\[36\]

**Infrastructure Components:**

\- **Experiment Management Systems**: Platforms for designing, deploying, and managing multiple concurrent experiments

\- **Feature Flagging**: Dynamic control over experimental variations without code deployment

\- **Real-time Analytics**: Immediate feedback on experimental performance and potential issues

\- **Statistical Computing**: Automated analysis pipelines providing reliable, reproducible results

**Measurement and Success Metrics**

**Experimentation Program Metrics**

Beyond individual experiment results, organizations must measure the overall effectiveness and impact of their experimentation programs.\[31\]\[37\]

**Velocity Metrics:**

\- Experiments launched per week/month

\- Time from hypothesis to results

\- Percentage of product decisions informed by experiments

**Quality Metrics:**

\- Statistical power of experiments

\- Reproducibility of results

\- Accuracy of effect size estimates

**Impact Metrics:**

\- Revenue impact from winning experiments

\- Conversion rate improvements

\- Customer satisfaction gains

**Long-term Business Impact**

The ultimate measure of experimentation success is sustained business improvement and competitive advantage. Organizations must track how experimental insights translate into lasting business value.

**Leading Indicators:**

\- Increased user engagement and retention

\- Improved conversion rates across the funnel

\- Enhanced customer lifetime value

**Lagging Indicators:**

\- Market share growth

\- Revenue per customer increases

\- Brand perception improvements

**Future Considerations and Emerging Trends**

**AI and Machine Learning Integration**

Artificial intelligence increasingly augments experimentation through automated hypothesis generation, dynamic treatment assignment, and sophisticated analysis of complex interactions. Machine learning models can identify patterns in experimental data that humans might miss while scaling personalization efforts.\[35\]

**Privacy-First Experimentation**

Evolving privacy regulations and consumer expectations require new approaches to experimentation that protect user privacy while maintaining analytical rigor. This includes techniques like differential privacy, federated learning, and consent-based testing frameworks.\[38\]

**Cross-Platform and Omnichannel Testing**

Modern customer journeys span multiple touchpoints and devices, requiring experimentation frameworks that can measure impact across channels while accounting for interaction effects between different customer experience elements.

**Conclusion**

Experimentation in marketing and product development has evolved from a tactical testing approach to a strategic organizational capability that drives sustainable competitive advantage. Airbnb's success demonstrates how systematic experimentation, powered by strong statistical foundations and cross-functional collaboration, can scale insights from individual tests to transformative business outcomes.

The key to experimentation success lies in building organizational capabilities across three critical dimensions: technical excellence in experimental design and analysis, strategic alignment with business objectives and North Star metrics, and cultural integration that enables cross-functional collaboration and data-informed decision-making.

As experimentation continues evolving with advances in artificial intelligence, privacy-preserving techniques, and omnichannel measurement, organizations that invest in building systematic experimentation capabilities today will be best positioned to adapt and thrive in an increasingly complex and competitive landscape.

For marketing analytics professionals, mastering these experimentation principles and practices provides the foundation for driving measurable business impact while building the collaborative relationships essential for sustainable success in data-driven organizations. The combination of technical rigor, business acumen, and stakeholder engagement skills creates the complete profile of an advanced analytics leader capable of transforming experimentation insights into strategic business value.

![][image4]

**Core pillars (summary table)**

| Pillar | What it answers | Examples |
| :---- | :---- | :---- |
| Design | Is the test valid? | Unit, randomization, MDE |
| Measurement | Are metrics correct? | CR, iROAS, LTV, guardrails |
| Inference | Is lift real? | t-tests, CUPED, FDR control |
| Operations | Can we run at scale? | Registry, SRM, QA, logs |
| Decisioning | What do we ship and where? | Rollout, ramp, kill, iterate |

**Summary**

* Define the decision, choose the unit, power for MDE, randomize cleanly,  
   monitor SRM/guardrails, analyze with pre-registered methods, decide with  
   ROI and risk.

---

![][image5]

---

---

### Block 10

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > A/B Testing Foundations > I. Foundational Concepts

**Mapping:** score=0.778 reason=heading_fuzzy|head='I. Foundational Concepts'

* **What is A/B/n Testing?**  
  * Definition: A controlled experiment where variants (A, B, ...n) are presented to users to determine which performs best against a predefined goal.  
  * A/B Test (2 variants) vs. A/B/n Test (3+ variants).  
* **Core Hypothesis Framework**  
  * Formulating a testable hypothesis (e.g., "By changing the call-to-action button from 'Learn More' to 'Get Started', we will increase the click-through rate by 10%").  
  * Independent Variable (what you change) vs. Dependent Variable (what you measure).  
* **Key Terminology**  
  * **Variants:** The different versions of the element being tested (Control \= A, Treatment(s) \= B, C, etc.).  
  * **Sample:** The group of users participating in the experiment.  
  * **Traffic Allocation:** How users are split between variants (e.g., 50/50, 25/25/25/25).  
  * **Goal / Primary Metric (KPI):** The key performance indicator you are trying to improve (e.g., Conversion Rate, Revenue, Click-Through Rate, Sign-ups).  
  * **Statistical Significance:** The probability that the observed difference between variants is not due to random chance.  
  * **Confidence Level:** The probability that your experiment correctly rejects the null hypothesis (typically 95%).  
  * **p-value:** The probability of obtaining your results if there is no real difference. A p-value \< 0.05 is standard for declaring significance.  
  * **Statistical Power:** The probability of detecting a true effect (a real difference) if it exists. Typically targeted at 80%.

---

### Block 11

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 1\. Foundations of Marketing Experimentation > **1.1. What is Marketing Experimentation?**

**Mapping:** score=0.61 reason=keyword:what is|head='**1.1. What is Marketing Experimentation?**'

* Controlled tests to understand cause-and-effect relationships in marketing.

* Contrast to observational or correlational marketing analytics.

---

### Block 12

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 5\. Advanced Topics in Experimentation > INTERVIEW-OPTIMIZED REFERENCE SUMMARY

**Mapping:** score=0.61 reason=keyword:what is|head='INTERVIEW-OPTIMIZED REFERENCE SUMMARY'

| Stage | Topic | Key Concept |
| :---- | :---- | :---- |
| 1 | Foundations | What is experimentation, why use it |
| 2 | Design | Hypotheses, test/control, test types |
| 3 | Stats | Metrics, tests, sample size, pitfalls |
| 4 | Analysis | Uplift, segmentation, iteration |
| 5 | Advanced | Bandits, causal inference, lag effects |
| 6 | Strategy | Prioritization, culture, real-world cases |

---

### Block 13

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Comprehensive Experiment Testing Guide for Marketing Analytics

**Mapping:** score=0.61 reason=keyword:scientific method|head='Comprehensive Experiment Testing Guide for Marketing Analytics'

A Complete Framework Using Affirm as a Case Study

1\. Pre-Experiment Planning Phase

1.1 Business Objective Definition

| Component | Options/Approaches | Affirm Example |
| :---- | :---- | :---- |
| Goal Types | • Revenue optimization • Conversion rate improvement • Customer acquisition cost reduction • Lifetime value increase • Engagement metrics • Retention improvement • Brand awareness | Increase merchant checkout conversion rate from 3.2% to 3.8%. |
| Success Metrics | • Primary metrics (North Star) • Secondary metrics • Guardrail metrics • Counter metrics • Leading indicators • Lagging indicators | Primary: Checkout conversion Secondary: Average order value Guardrail: Customer complaints. |
| Hypothesis Frameworks | • If-Then-Because format • Problem-Solution-Result • Jobs-to-be-Done • Lean Hypothesis • Scientific Method | "If we reduce the number of form fields from 8 to 4, then checkout conversion will increase by 20%, because users abandon due to friction". |

1.2 Experiment Type Selection

| Experiment Type | Use Cases | Complexity | Affirm Example |
| :---- | :---- | :---- | :---- |
| A/B Testing | • Single variable change • Clear binary choices • Simple implementation | Low | Testing two checkout button colors. |
| A/B/n Testing | • Multiple variants • Exploring optimization curve • Finding local maxima | Medium | Testing 5 different payment plan displays. |
| Multivariate Testing (MVT) | • Multiple variables simultaneously • Interaction effects • Complex UX changes | High | Testing button color × copy × position. |
| Multi-Armed Bandit | • Dynamic allocation • Minimize opportunity cost • Continuous optimization | High | Optimizing interest rate offers in real-time. |
| Factorial Design | • Full factorial (all combinations) • Fractional factorial • Systematic interaction study | Very High | Testing all combinations of 4 factors. |
| Sequential Testing | • Early stopping rules • Adaptive designs • Resource optimization | High | Stopping test early if a clear winner emerges. |
| Switchback Testing | • Time-based allocation • Network effects • Market-level changes | Medium | Testing new merchant onboarding flow. |
| Synthetic Control | • No randomization possible • Market-level rollouts • Causal inference | Very High | Launching in a new geographic market. |

2\. Statistical Framework & Power Analysis

2.1 Statistical Test Selection

| Statistical Test | Use Cases & Assumptions | Affirm Example |
| :---- | :---- | :---- |
| Z-Test | • Large samples (n\>30), known variance • Assumptions: Independence, Normality, Equal variance | Comparing conversion rates with 100k+ users. |
| T-Test (Student's) | • Small samples, unknown variance, continuous outcomes • Assumptions: Independence, Normality, Equal variance | Comparing average order values. |
| Welch's T-Test | • Unequal variances, different sample sizes • Assumptions: Independence, Normality | Comparing segments with different sizes. |
| Mann-Whitney U | • Non-parametric, ordinal data, non-normal distribution • Assumptions: Independence, Ordinal scale | Comparing user satisfaction scores. |
| Chi-Square Test | • Categorical outcomes, independence testing • Assumptions: Expected frequency \>5, Independence | Testing payment method preferences. |
| Fisher's Exact Test | • Small sample sizes, 2x2 contingency tables • Assumption: Independence | Rare event analysis (fraud rates). |
| Kolmogorov-Smirnov | • Distribution comparison, continuous data • Assumptions: Independence, Continuous scale | Comparing entire distributions of loan amounts. |
| Bootstrap Methods | • No distribution assumptions, complex statistics • Assumption: Independence | Confidence intervals for median time to repayment. |
| Bayesian Methods | • Prior information, sequential analysis, posterior probabilities • Assumption: Prior specification | Updating conversion rate beliefs with new data. |
| CUPED/CUPAC | • Variance reduction, uses pre-experiment data • Assumption: Covariate stability | Using historical purchase data to reduce variance. |

2.2 Sample Size Calculation Methods

| Method | Formula/Approach | Use Case | Affirm Example |
| :---- | :---- | :---- | :---- |
| Classical Power Analysis | n \= 2σ²(Z\_α/2 \+ Z\_β)²/δ² | Standard A/B tests | 15,000 users per variant for 80% power. |
| Minimum Detectable Effect | MDE \= (Z\_α/2 \+ Z\_β)√(2σ²/n) | Fixed sample constraint | Can detect 0.5% lift with current traffic. |
| Sequential Analysis | Alpha spending functions | Continuous monitoring | Check results daily with adjusted p-values. |
| Bayesian Sample Size | Posterior probability thresholds | Prior information available | 95% probability variant is 2% better. |
| Simulation-Based | Monte Carlo methods | Complex designs | Simulate 10,000 experiments. |
| Adaptive Designs | Information-based stopping | Efficient resource use | Stop when confidence interval \< 0.1%. |

3\. Experiment Design & Implementation

3.1 Randomization Strategies

| Strategy | Implementation | Pros/Cons | Affirm Use Case |
| :---- | :---- | :---- | :---- |
| Simple Random | Random number generator | Pro: Unbiased Con: Imbalanced groups | Basic feature tests. |
| Block Randomization | Randomize within blocks | Pro: Balance covariates Con: Complex | Balance by merchant type. |
| Stratified Random | Random within strata | Pro: Representative Con: Need strata info | Ensure all credit tiers represented. |
| Cluster Randomization | Randomize groups | Pro: Avoid contamination Con: Less power | Randomize by merchant. |
| Matched Pairs | Match then randomize | Pro: Increased power Con: Matching complexity | Match users by purchase history. |
| Hash-Based | Deterministic hashing | Pro: Consistent Con: Predictable | User ID % 100 \< 50\. |
| Time-Based | Temporal allocation | Pro: Simple Con: Time confounds | Day-of-week randomization. |
| Geo-Based | Geographic clustering | Pro: Market-level Con: Spillover effects | Test in specific states. |

3.2 Implementation Frameworks

| Framework | Examples | Use Case | Affirm Example |
| :---- | :---- | :---- | :---- |
| Feature Flags | • LaunchDarkly • Optimizely • Split.io | Real-time control | Toggle checkout flow variants. |
| Server-Side Testing | • Backend randomization • API-driven | Sensitive features | Payment terms calculation. |
| Client-Side Testing | • JavaScript-based • Google Optimize • VWO | UI/UX changes | Button color testing. |
| Edge Computing | • CDN-level • Cloudflare Workers | Low latency | Personalized landing pages. |
| Mobile SDKs | • Firebase A/B • Apptimize | App experiments | Mobile app checkout flow. |
| Full-Stack Platforms | • Amplitude Experiment • Statsig | End-to-end solution | Integrated testing platform. |

4\. Monitoring & Quality Assurance

4.1 Pre-Launch Checks

| Check Type | Methods | Critical Metrics | Affirm Example |
| :---- | :---- | :---- | :---- |
| AA Testing | Run control vs control | • Type I error rate • Randomization balance | 5% false positive rate confirmed. |
| Sample Ratio Mismatch | Chi-square test on assignment | • Expected vs actual ratio • P-value \< 0.001 flags issue | 50.1% vs 49.9% (acceptable). |
| Covariate Balance | • T-tests on features • Standardized differences | • Age, income, credit score • \<0.1 std dev difference | All user attributes balanced. |
| Technical Validation | • Logging verification • Event tracking | • 100% event capture • No data loss | All checkout events tracked. |
| Canary Deployment | Gradual rollout | • Error rates • Performance metrics | 1% → 5% → 25% → 50%. |

4.2 Runtime Monitoring

| Type | Tools/Methods | Alert Thresholds | Response Plan |
| :---- | :---- | :---- | :---- |
| Statistical Significance | • Sequential testing • P-value tracking | • Alpha spending • Adjusted p-values | Daily significance checks. |
| Practical Significance | • Effect size monitoring • Business impact | • Minimum meaningful difference • ROI thresholds | Alert if effect \< 1%. |
| Data Quality | • Missing data rates • Outlier detection | • \>5% missing data • Impossible values | Automated data quality reports. |
| System Health | • Latency monitoring • Error rates | • P95 latency \>2s • Error rate \>0.1% | PagerDuty alerts. |
| Sample Size Tracking | • Daily accumulation • Projection models | • Behind schedule • Imbalanced exposure | Traffic allocation adjustment. |

5\. Analysis Methods & Techniques

5.1 Primary Analysis Approaches

| Method | Statistical Technique | Implementation | Affirm Example |
| :---- | :---- | :---- | :---- |
| Frequentist Analysis | • Hypothesis testing • P-values | • Python statsmodels • R stats package | t-test on conversion rates. |
| Bayesian Analysis | • Posterior distributions • Credible intervals | • PyMC3 • Stan | P(variant \> control) \= 0.97. |
| Regression Adjustment | • ANCOVA • Linear models | • Include covariates • Reduce variance | Adjust for user credit score. |
| Machine Learning | • Causal forests • Double ML | • CausalML • EconML | Heterogeneous treatment effects. |
| Time Series | • Interrupted time series • ARIMA models | • Seasonal adjustment • Trend analysis | Account for holiday effects. |
| Survival Analysis | • Kaplan-Meier • Cox regression | • Time to event • Censoring | Time to first purchase. |

5.2 Advanced Techniques

| Technique | Description | Complexity | Use Case |
| :---- | :---- | :---- | :---- |
| CUPED | Variance reduction using pre-data | Medium | 30-50% variance reduction possible. |
| Difference in Differences | Control for time trends | Medium | Rollout experiments. |
| Instrumental Variables | Handle non-compliance | High | Users don't see assigned variant. |
| Synthetic Control Method | Create counterfactual | High | Single unit treatment (new market). |
| Regression Discontinuity | Exploit thresholds | High | Credit score cutoffs. |
| Quantile Treatment Effects | Analyze distribution impacts | Medium | Effect varies by user segment. |
| Meta-Analysis | Combine multiple experiments | Medium | Synthesize learning across tests. |
| Heterogeneous Effects | Subgroup analysis, interaction terms | High | Personalization opportunities. |

6\. Results Interpretation & Decision Making

6.1 Statistical Interpretation Framework

| Aspect | Considerations | Best Practices | Common Pitfalls |
| :---- | :---- | :---- | :---- |
| Effect Size | • Practical vs statistical significance • Confidence intervals | Report both absolute and relative | Focusing only on p-values. |
| Multiple Testing | • Bonferroni correction • FDR control | Pre-specify primary metric | P-hacking with many metrics. |
| Segment Analysis | • Pre-specified vs exploratory • Interaction tests | Register segments beforehand | HARKing (post-hoc storytelling). |
| Long-term Effects | • Novelty effects • Learning curves • Seasonality | Run for a full business cycle | Stopping too early. |
| External Validity | • Generalizability • Population differences | Document assumptions | Over-generalizing results. |

6.2 Decision Frameworks

| Framework | Approach | Key Consideration | Example Decision Rule |
| :---- | :---- | :---- | :---- |
| Hypothesis Testing | Reject if p \< α | Type I/II errors | Ship if p \< 0.05. |
| Bayesian Decision | Maximize expected utility | Loss function | Ship if P(lift\>0) \> 0.95. |
| Risk-Adjusted | Consider downside | Worst-case scenario | Ship if worst case \> \-0.5%. |
| Portfolio Approach | Optimize across tests | Resource allocation | Fund top 20% of ideas. |
| Sequential Decision | Continue/stop rules | Opportunity cost | Stop if futility boundary crossed. |
| Multi-Stakeholder | Weighted objectives | Stakeholder alignment | Product \+ Risk \+ Legal approval. |

7\. Post-Experiment Actions

7.1 Implementation Strategies

| Strategy | Approach | Risk Mitigation | Timeline |
| :---- | :---- | :---- | :---- |
| Full Rollout | 100% immediate | Monitor closely | 1 day. |
| Gradual Rollout | 50% → 75% → 100% | Staged validation | 2 weeks. |
| Holdout Groups | Keep 5-10% control | Long-term measurement | Ongoing. |
| Regional Rollout | Geography-based | Market differences | 1 month. |
| Segment-Based | High-value users first | Protect core base | 3 weeks. |
| Feature Flags | Instant rollback capability | Quick reversion | Immediate. |

7.2 Knowledge Management

| Component | Methods | Tools | Deliverables |
| :---- | :---- | :---- | :---- |
| Documentation | • Experiment briefs • Analysis notebooks | • Confluence • GitHub • Notion | Experiment report template. |
| Knowledge Sharing | • Review meetings • Wiki updates | • Slack channels • Email digests | Weekly experiment review. |
| Meta-Learning | • Cross-experiment analysis • Pattern recognition | • DataBricks • Tableau • Python | Quarterly insights report. |
| Process Improvement | • Retrospectives • Efficiency metrics | • JIRA • Asana • Linear | Monthly process review. |

8\. Advanced Topics & Considerations

8.1 Network & Other Effects

| Effect Type | Challenges | Mitigation Strategies | Example |
| :---- | :---- | :---- | :---- |
| Direct Network Effects | • Cluster randomization • SUTVA violations | • Market-level randomization • Synthetic control | Merchant referral programs. |
| Indirect Effects | • Spillover analysis • Spatial models | • Buffer zones • Cluster designs | User word-of-mouth. |
| Competitive Effects | • Game theory models • Market share analysis | • Simultaneous moves • Strategic timing | Competitor response to pricing. |
| Platform Effects | • Two-sided markets • Feedback loops | • Careful measurement • Dynamic models | Merchant-consumer interactions. |

8.2 Ethical Considerations

| Aspect | Guidelines | Implementation | Example |
| :---- | :---- | :---- | :---- |
| Fairness | • Equal treatment • No discrimination | • Bias testing • Fairness metrics | Equal approval rates across demographics. |
| Transparency | • User notification • Opt-out options | • Privacy policy • Clear communication | "You're seeing a new checkout experience". |
| Risk Management | • Minimize harm • Protect vulnerable users | • Guardrail metrics • Safety protocols | Don't test on high-risk loan applicants. |
| Data Privacy | • GDPR compliance • Data minimization | • Anonymization • Retention policies | Hash PII, delete after analysis. |

9\. Tools & Technology Stack

9.1 Experimentation Platforms

| Platform Type | Examples | Key Features | Best For |
| :---- | :---- | :---- | :---- |
| Commercial | • Optimizely • Adobe Target • VWO | • Visual editors • Built-in stats | Marketing teams, quick starts. |
| Developer-Focused | • LaunchDarkly • Split.io • Statsig | • Feature flags • SDKs • API-first | Engineering-led experimentation. |
| Analytics-Integrated | • Amplitude Experiment • Mixpanel | • Unified data • User journey | Product analytics teams. |
| Open Source | • GrowthBook • Wasabi • PlanOut | • Customizable • Self-hosted | Teams with engineering resources. |
| Custom Built | • Internal platforms • Microservices | • Full control • Tailored needs | Large organizations. |

9.2 Analysis Tools

| Tool Category | Options | Use Case | Integration |
| :---- | :---- | :---- | :---- |
| Statistical Software | • R \+ tidyverse • Python (scipy) | Complex analysis | Data pipelines. |
| Notebooks | • Jupyter • RStudio • Databricks | Exploratory analysis | Version control. |
| BI Tools | • Tableau • Looker • PowerBI | Dashboards | Real-time monitoring. |
| Data Processing | • Spark • Presto • BigQuery | Large-scale processing | ETL pipelines. |
| Workflow Management | • Airflow • Prefect • Dagster | Automation | Scheduled analysis. |

10\. Example End-to-End Experiment: Affirm Checkout Optimization

Stage 1: Planning

• Hypothesis: Reducing checkout steps from 5 to 3 will increase conversion by 25%.

• Metrics: Primary: Conversion rate, Secondary: Time to complete, Guardrail: Error rate.

• Sample Size: 50,000 users per variant (α=0.05, β=0.20, MDE=2%).

Stage 2: Design

• Randomization: Hash-based on user ID.

• Duration: 3 weeks (full purchase cycle).

Stage 3: Implementation

• Platform: Internal feature flag system.

• Monitoring: Real-time dashboard in Looker.

• Quality Checks: AA test passed, SRM check daily.

Stage 4: Analysis

• Method: Two-proportion z-test with CUPED.

• Results: 23% lift (95% CI: 18%-28%), p \< 0.001.

• Segments: Larger effect for mobile users (28% vs 19%).

Stage 5: Decision

• Recommendation: Ship to 100% with a 1-week staged rollout.

• Holdout: 5% control for long-term monitoring.

• Next Steps: Explore further optimization for the desktop experience.

Stage 6: Learning

• Insight: Form simplification has diminishing returns after 3 fields.

• Future Tests: Focus on mobile-first design.

• Process Improvement: Implement automatic SRM alerts.

---

---

### Block 14

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > All-in-one cheat sheet to ace interviews

**Mapping:** score=0.61 reason=keyword:overview|head='All-in-one cheat sheet to ace interviews'

Questions on A/B testing are being increasingly asked in interviews but reliable resources to prepare for these are still far and few. Let’s say you completed a [great course on A/B testing](https://www.udemy.com/course/product-experimentation-ab-testing-in-r-with-real-examples/learn/practice/1238666?referralCode=C0EC84F644B6BCB10FD0#overview) sometime back and felt confident in your understanding of A/B testing statistics. It’s been a while now, you have an interview coming up and for the love of god, you can’t seem to remember what statistical power means or what SUTVA stands for. OR you have been using experimentation in your current role and have automated most processes. Without the need for manual steps, you have become rusty and need a quick cheat sheet to recall important concepts and intuition behind them so that you can ace an upcoming interview.

Use this post as a quick resource for the most important concepts in A/B testing you need to know before interviews. You will find a summary of the most important concepts along with examples to build your intuition.

---

### Block 15

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Overview**

**Mapping:** score=0.61 reason=keyword:overview|head='**Overview**'

This book is a technical and practical guide to running online controlled experiments (OCEs)—commonly known as A/B tests—at scale. Written by three experts from Microsoft, Google, and LinkedIn, it draws on decades of experience running tens of thousands of experiments across some of the world’s largest tech platforms.

The book is structured to balance **theory**, **statistical rigor**, **technical execution**, and **organizational adoption**, making it relevant for data scientists, engineers, product managers, and leaders aiming to drive experimentation-led growth.

---

### Block 16

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Key Sections in Detail** > **2\. Causality and Randomization**

**Mapping:** score=0.61 reason=keyword:causality|head='**2\. Causality and Randomization**'

Causality lies at the heart of experimentation. To isolate the effect of a feature or change, users must be **randomly assigned** to control and treatment groups using **stable identifiers** (e.g., user ID, device ID). This randomization ensures that both known and unknown confounders are equally distributed.

The authors caution against poor randomization, such as assigning by session ID or by IP address, which can introduce serious bias and destroy the validity of results.

---

### Block 17

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > Overview of the Book

**Mapping:** score=0.61 reason=keyword:overview|head='Overview of the Book'

This book serves as a practical guide to understanding and performing various types of hypothesis tests to determine statistical significance. It is designed to be direct and easy to follow, providing worked examples that can be solved both by hand using equations and with functions in Microsoft Excel. The book covers several key statistical tests, including the Z-Test and various T-Tests (1-Sample, Paired, 2-Sample with Equal Variance, and 2-Sample with Unequal Variance). As a bonus, it offers readers a free downloadable "Hypothesis Testing cheat sheet" that summarizes the five main test types, their equations, and corresponding Excel functions.

---

### Block 18

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > Core Concepts of Hypothesis Testing > **What is Statistical Significance?**

**Mapping:** score=0.61 reason=keyword:what is|head='**What is Statistical Significance?**'

The fundamental question of statistical significance is: **"How unlikely would this outcome have been if it just happened by random chance?"**. The goal is to determine if an observed effect is likely due to a specific cause or simply random variation.

To illustrate this, the source uses an example of a farmer testing a new pig food. If the pigs eating the new food gain more weight, statistical significance helps determine if the food was the cause, or if those specific pigs were just naturally inclined to gain more weight anyway.

Two factors are crucial in this calculation:

1. **The distance of the measured average from the comparison value**: A larger difference is more likely to be significant.  
2. **The standard deviation of the measurements**: This measures how spread out the data is. A low standard deviation (like the weights of 10 identical coins) means the data is clustered together, while a high standard deviation (like the weights of 10 different rocks) means the data is widely varied.

A typical normal curve shows that **68%** of data falls within 1 standard deviation of the mean, **95%** within 2 standard deviations, and **99.7%** within 3 standard deviations. Hypothesis testing essentially reverses this by asking how many standard deviations a reference value is from our measured data's mean.

---

### Block 19

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **Example 1: Z-Test**

**Mapping:** score=0.61 reason=keyword:when to use|head='**Example 1: Z-Test**'

* **When to Use**: A Z-Test is appropriate when you are comparing a sample mean to a known population mean, and **the population standard deviation (σ) is also known**. Some sources also state a Z-test can be used with a large sample size (e.g., \>30), as the T-test converges on the Z-test.  
* **Scenario**: Determining if the average birth weight of 30 male babies at a hospital (sample mean \= 7.83 lbs) is significantly greater than the national average (population mean \= 7.5 lbs, population SD \= 1.25 lbs).  
* **Instructions**:  
  1. **Calculate the Z-Statistic**: Use the formula `Z = (x̄ - u₀) / (σ / √n)`. For the example, Z \= (7.8333 \- 7.5) / (1.25 / √30) \= **1.461**.  
  2. **Choose 1-Tailed or 2-Tailed Test**: Since the question asks if the weight is *greater than* the average, a **1-tailed test** is used. A 2-tailed test would be used to see if the weight was simply *different* (either greater or lesser).  
  3. **Find the p-value**: Look up the Z-statistic (1.46) in a Z-Table. This corresponds to a cumulative probability of 0.9279, which means there is a `1 - 0.9279 = 0.0721` or **7.21%** chance of observing this result randomly. Since this p-value is greater than the 0.05 required for 95% confidence, we cannot conclude the babies are significantly heavier.  
* **Excel Functions**:  
  * `=NORM.S.DIST(z, TRUE)`: To find the cumulative probability from a Z-statistic.  
  * `=Z.TEST(array, x, [sigma])`: To calculate the p-value directly from the data.

A summary table for this example is provided: | Example 1 Summary Table | | | :--- | :--- | | **Problem** | Is the average baby weight \> 7.5 lbs with 95% confidence? | | **Data** | Sample Mean: 7.8333 lbs, n=30, Pop. Mean: 7.5 lbs, Pop. SD: 1.25 lbs | | **Z Statistic** | 1.461 | | **P-value (1 tailed)** | 0.0721 | | **Conclusion** | Cannot conclude with 95% confidence. |

---

### Block 20

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **Example 2: 1-Sample T-Test**

**Mapping:** score=0.61 reason=keyword:when to use|head='**Example 2: 1-Sample T-Test**'

* **When to Use**: When comparing a single sample's mean against a known population mean, but the population standard deviation is unknown.  
* **Scenario**: Measuring the height of 15 college students to see if it is statistically different from the national average of 5.5 feet.  
* **Instructions**:  
  1. **Calculate the T-Statistic**: The formula is `t = (x̄ - u₀) / (s / √n)`, where `s` is the *sample* standard deviation. For the example, the sample mean (`x̄`) is 5.673 ft, sample SD (`s`) is 0.3105, and n is 15\. The T-statistic is **2.16**.  
  2. **Calculate Degrees of Freedom (df)**: For a 1-sample T-test, `df = n - 1`. Here, df \= 15 \- 1 \= **14**.  
  3. **Choose 1-Tailed or 2-Tailed**: The question asks if the height is *different*, so a **2-tailed test** is used.  
  4. **Find the p-value**: Using a T-Table with df=14, a T-value of 2.16 is close to the column for a p-value of 0.05 (for a 2-tailed test). Using Excel (`=T.DIST.2T(2.16, 14)`), the precise p-value is **0.0484**, which is less than 0.05. We can conclude with 95% confidence that the height is different.

---

### Block 21

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **Example 3: Paired T-Test**

**Mapping:** score=0.61 reason=keyword:when to use|head='**Example 3: Paired T-Test**'

* **When to Use**: When you measure the *same subject* multiple times, typically in a "before and after" scenario.  
* **Scenario**: Weighing 20 people before and after a diet to see if they lost weight with 99% confidence.  
* **Instructions**:  
  1. **Calculate the Differences**: For each pair, calculate the difference (e.g., After Weight \- Before Weight).  
  2. **Calculate the T-Statistic**: The formula is `t = d̄ / (s_d / √n)`, where `d̄` is the average of the differences and `s_d` is the standard deviation of the differences. For the example, `d̄` \= \-5.35 lbs, `s_d` \= 5.6127, and n=20. The T-statistic is **\-4.2628**.  
  3. **Calculate df**: `df = n - 1` (where n is the number of pairs). Here, df \= 20 \- 1 \= **19**.  
  4. **Find the p-value**: Using Excel's `=T.DIST.RT()` function for a 1-tailed test gives a p-value of **0.0002**. This is much less than the 0.01 required for 99% confidence, so we can conclude the diet was effective.  
* **Excel Function**: `=TTEST(array1, array2, tails, type=1)`.

---

### Block 22

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **Example 4: Two-Sample T-Test with Equal Variance**

**Mapping:** score=0.61 reason=keyword:when to use|head='**Example 4: Two-Sample T-Test with Equal Variance**'

* **When to Use**: When comparing the means of two **independent groups** and you can assume the variance (spread) of the two groups is roughly the same.  
* **Scenario**: Comparing the amount of food eaten by two different groups of cats given two different food types.  
* **Instructions**: The formula is more complex, using a "pooled" or weighted average of the two sample variances to calculate the T-statistic. The degrees of freedom are calculated as `df = n₁ + n₂ - 2`. The results for the example showed a 2-tailed p-value of 0.0958, so you cannot conclude with 95% confidence that the cats ate a different amount.  
* **Excel Function**: `=TTEST(array1, array2, tails, type=2)`.

---

### Block 23

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **Example 5: Two-Sample T-Test with Unequal Variance**

**Mapping:** score=0.61 reason=keyword:when to use|head='**Example 5: Two-Sample T-Test with Unequal Variance**'

* **When to Use**: When comparing two independent groups where the variances are expected to be different. This often occurs when a treatment, like training, might reduce the variability in one group.  
* **Scenario**: Comparing the time it takes to assemble a part for a group of employees with no training versus a group with training.  
* **Instructions**: This test uses a different T-statistic formula and a much more complex formula for calculating degrees of freedom. For the example, the training was found to have reduced the assembly time with 90% confidence (p-value \= 0.0934).  
* **Excel Function**: `=TTEST(array1, array2, tails, type=3)`.

Finally, the source notes that while there are two different two-sample tests, the practical difference in their results is often not very large. If unsure, one can run the analysis both ways.

---

---

### Block 24

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Next-Level A/B Testing: Repeatable, Rapid, and Flexible Product Experimentation

**Mapping:** score=0.61 reason=keyword:overview|head='Next-Level A/B Testing: Repeatable, Rapid, and Flexible Product Experimentation'

Overview of the Book

This book is designed for professionals who are already familiar with the fundamentals of A/B testing and are looking to advance their practices. The intended audience includes product managers, software engineers, business analysts, and others involved in product experimentation. The book aims to simplify advanced concepts into actionable terms, using relatable metaphors and a continuous case study of a fictitious e-commerce company, MarketMax, to provide practical, hands-on examples.

The central theme is to elevate A/B testing by focusing on three critical areas: improving the experimentation rate, quality, and cost. The book provides a comprehensive toolkit of strategies that go beyond basic A/B tests to address the challenges that arise as a company's experimentation culture matures and scales.

---

### Block 25

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Ace A/B Testing Interview Question: A Data-driven Approach for Data Scientists > Top A/B Testing Interview Questions

**Mapping:** score=0.61 reason=keyword:what is|head='Top A/B Testing Interview Questions'

Now let's dive in. Here's a diagram showing the distribution of top AB testing interview questions. I created this diagram after analyzing over 350 interview questions from 46 companies. Let's look at top five AB testing interview questions. The design question is the top AB testing interview question. It accounts for over 30% of interview questions. It means one out of three questions is the design question. So what is the design question?

The design question is a broad question. It asks you to design a test to evaluate the effectiveness of a new feature or the success of a new product, et cetera. For example, how do you design a test to evaluate the effectiveness of a referral program? Next up is sample size and test duration. This type of question is straightforward. It asks you to calculate the sample size and the duration of a test. The third common question is causal inference. Causal inference questions can also appear in the interview because it's a method that can be considered when AB testing is not feasible. This type of question is more common when you interview with a company that employs a two-sided marketplace or three sided marketplace business model such as Uber, Lyft, and DoorDash.

The next type of question is multiple testing. Multiple testing problems occur frequently in reality. It occurs when we run multiple tests in parallel or when we test multiple metrics in one AB test. Another AB testing interview question is launch decision. What does this mean? It means that once we finish running the test and we have gathered the data, we need to make the launch decision to determine if we want to launch this feature or the product or not. One example could be based on the data. From this test, what is your suggestion to launch this feature or not?

Now you know the top five AB testing interview questions and in this video we are going to focus on the top AB testing

---

### Block 26

**Source:** `md`  
**Original headings:** A guide to passing the A/B test interview question in tech companies

**Mapping:** score=0.61 reason=keyword:what is|head='A guide to passing the A/B test interview question in tech companies'

[Discussion](https://www.reddit.com/r/datascience/?f=flair_name%3A%22Discussion%22)

Hey all,

I'm a Sr. Analytics Data Scientist at a large tech firm (not FAANG) and I conduct about \~3 interviews per week. I wanted to share my advice on how to pass A/B test interview questions as this is an area I commonly see candidates get dinged. Hope it helps.

Product analytics and data scientist interviews at tech companies often include an A/B testing component. Here is my framework on how to answer A/B testing interview questions. Please note that this is not necessarily a guide to design a good A/B test. Rather, it is a guide to help you convince an interviewer that you know how to design A/B tests.

A/B Test Interview Framework

Imagine during the interview that you get asked “Walk me through how you would A/B test this new feature?”. This framework will help you pass these types of questions.

Phase 1: Set the context for the experiment. Why do we want to AB test, what is our goal, what do we want to measure?

1. The first step is to clarify the purpose and value of the experiment with the interviewer. Is it even worth running an A/B test? Interviewers want to know that the candidate can tie experiments to business goals.

2. Specify what exactly is the treatment, and what hypothesis are we testing? Too often I see candidates fail to specify what the treatment is, and what is the hypothesis that they want to test. It’s important to spell this out for your interviewer. 

3. After specifying the treatment and the hypothesis, you need to define the metrics that you will track and measure.

   * Success metrics: Identify at least 2-3 candidate success metrics. Then narrow it down to one and propose it to the interviewer to get their thoughts.

   * Guardrail metrics: Guardrail metrics are metrics that you do not want to harm. You don’t necessarily want to improve them, but you definitely don’t want to harm them. Come up with 2-4 of these.

   * Tracking metrics: Tracking metrics help explain the movement in the success metrics. Come up with 1-4 of these.

Phase 2: How do we design the experiment to measure what we want to measure?

1. Now that you have your treatment, hypothesis, and metrics, the next step is to determine the unit of randomization for the experiment, and when each unit will enter the experiment. You should pick a unit of randomization such that you can measure success your metrics, avoid interference and network effects, and consider user experience.

   * As a simple example, let’s say you want to test a treatment that changes the color of the checkout button on an ecommerce website from blue to green. How would you randomize this? You could randomize at the user level and say that every person that visits your website will be randomized into the treatment or control group. Another way would be to randomize at the session level, or even at the checkout page level. 

   * When each unit will enter the experiment is also important. Using the example above, you could have a person enter the experiment as soon as they visit the website. However, many users will not get all the way to the checkout page so you will end up with a lot of users who never even got a chance to see your treatment, which will dilute your experiment. In this case, it might make sense to have a person enter the experiment once they reach the checkout page. You want to choose your unit of randomization and when they will enter the experiment such that you have minimal dilution. In a perfect world, every unit would have the chance to be exposed to your treatment.

2. Next, you need to determine which statistical test(s) you will use to analyze the results. Is a simple t-test sufficient, or do you need quasi-experimental techniques like difference in differences? Do you require heteroskedastic robust standard errors or clustered standard errors?

   * The t-test and z-test of proportions are two of the most common tests.

3. The next step is to conduct a power analysis to determine the number of observations required and how long to run the experiment. You can either state that you would conduct a power analysis using an alpha of 0.05 and power of 80%, or ask the interviewer if the company has standards you should use.

   * I’m not going to go into how to calculate power here, but know that in any AB  test interview question, you will have to mention power. For some companies, and in junior roles, just mentioning this will be good enough. Other companies, especially for more senior roles, might ask you more specifics about how to calculate power. 

4. Final considerations for the experiment design: 

   * Are you testing multiple metrics? If so, account for that in your analysis. A really common academic answer is the Bonferonni correction. I've never seen anyone use it in real life though, because it is too conservative. A more common way is to control the False Discovery Rate. You can google this. Alternatively, the book [Trustworthy Online Controlled Experiments](https://amzn.to/4dzXyZP) by Ron Kohavi discusses how to do this (note: this is an affiliate link). 

   * Do any stakeholders need to be informed about the experiment? 

   * Are there any novelty effects or change aversion that could impact interpretation?

5. If your unit of randomization is larger than your analysis unit, you may need to adjust how you calculate your standard errors.

6. You might be thinking “why would I need to use difference-in-difference in an AB test”? In my experience, this is common when doing a geography based randomization on a relatively small sample size. Let’s say that you want to randomize by city in the state of California. It’s likely that even though you are randomizing which cities are in the treatment and control groups, that your two groups will have pre-existing biases. A common solution is to use difference-in-difference. I’m not saying this is right or wrong, but it’s a common solution that I have seen in tech companies.

Phase 3: The experiment is over. Now what?

1. After you “run” the A/B test, you now have some data. Consider what recommendations you can make from them. What insights can you derive to take actionable steps for the business? Speaking to this will earn you brownie points with the interviewer.

   * For example, can you think of some useful ways to segment your experiment data to determine whether there were heterogeneous treatment effects?

Common follow-up questions, or “gotchas”

These are common questions that interviewers will ask to see if you really understand A/B testing.

* Let’s say that you are mid-way through running your A/B test and the performance starts to get worse. It had a strong start but now your success metric is degrading. Why do you think this could be?

  * A common answer is novelty effect

* Let’s say that your AB test is concluded and your chosen p-value cutoff is 0.05. However, your success metric has a p-value of 0.06. What do you do?

  * Some options are: Extend the experiment. Run the experiment again.

  * You can also say that you would discuss the risk of a false positive with your business stakeholders. It may be that the treatment doesn’t have much downside, so the company is OK with rolling out the feature, even if there is no true improvement. However, this is a discussion that needs to be had with all relevant stakeholders and as a data scientist or product analyst, you need to help quantify the risk of rolling out a false positive treatment.

* Your success metric was stat sig positive, but one of your guardrail metrics was harmed. What do you do?

  * Investigate the cause of the guardrail metric dropping. Once the cause is identified, work with the product manager or business stakeholders to update the treatment such that hopefully the guardrail will not be harmed, and run the experiment again.

  * Alternatively, see if there is a segment of the population where the guardrail metric was not harmed. Release the treatment to only this population segment.

* Your success metric ended up being stat sig negative. How would you diagnose this? 

I know this is really long but honestly, most of the steps I listed could be an entire blog post by itself. If you don't understand anything, I encourage you to do some more research about it, or get the book that I linked above (I've read it 3 times through myself). Lastly, don't feel like you need to be an A/B test expert to pass the interview. We hire folks who have no A/B testing experience but can demonstrate framework of designing AB tests such as the one I have just laid out. Good luck\!

---

CHAPTER 1The power of small improvements

Speaker 100:01

I'm very clear that I'm a big fan of test everything, which is any code change that you make any feature that you introduce has to be in some experiment. Because again, I've observed this sort of surprising result that even small bug fixes, even small changes can sometimes have surprising unexpected impact.

And so I don't think it's possible to experiment too much. You have to allocate sometimes to these high risk, high reward ideas. We're gonna try something that's most likely to fail. But if it does win, it's gonna be a home run and you have to be ready to understand and agree that most will fail.

And I've, it's amazing how many times I've seen people come up with new designs or a radical new idea and they believe in it and that's OK. I'm just cautioning them all the Time to say if you go for something big, try it out but be ready to fail. 80% of the Time.

Speaker 201:05

Welcome to Lenny's podcast where I interview world class product leaders and growth experts to learn from their hard one experiences building and growing today's most successful products. Today. My guest is Ronnie Koha Ronnie is seen by many as the world expert on A B testing and experimentation. Most recently US VP and technical fellow of relevance at Airbnb where he led their search experience team.

Prior to that, he was corporate vice president at Microsoft, where he led Microsoft's Experimentation Platform team. Before that, he was director of Data Mining And Personalization at Amazon. He's currently a full Time advisor and instructor. He's also the author of the go to book on experimentation called Trustworthy Online Controlled Experiments.

And in our show notes, you'll find a code to get a discount on taking his live cohort based course on Maven. In our conversation, we get super tactical about A B testing. Ronnie shares his advice for when you should start considering running experiments at your company, how to change your company's culture to be more experiment driven.

What are signs your experiments are potentially invalid? Why trust is the most important element of a successful experiment culture and platform, how to get started. If you want to start running experiments at your company, he explains what actually is a P value and something called Twin's Law plus some hot takes about Airbnb and experiments in general.

This episode is for anyone who is interested in either creating an experiment driven culture at their company or just fine tuning one that already exists. Enjoy this episode with Coy after a short word from our sponsors, this episode is brought to you by mix panel, get deep insights into what your users are doing at every stage of the funnel at a fair price that scales as you grow.

Mix panel gives you quick answers about your users from awareness to acquisition through attention and by capturing website activity, add data and multi touch attribution, right. In mix panel, you can improve every aspect of the full user fun powered by first party behavioral data.

Instead of third party cookies, mix panel is built to be more powerful and easier to use than Google analytics. Explore plans for teams of every size and see what mix panel can do for you at mix panel dot com slash friends slash Lenny. And while you're at it, they're also hiring. So check it out at mix panel dot com slash friends slash Lenny.

This episode is brought to you by round. Round is the private network built by tech leaders for tech leaders. Round combines the best of coaching, learning and authentic relationships to help you identify where you want to go and accelerate your path to get there, which is why their wait list tops thousands of tech execs.

Round is on a mission to shape the future of technology and its impact on society leading in tech is uniquely challenging and doing it well is easiest when surrounded by leaders who understand your data day experiences.

When we're meeting and building relationships with the right people, we're more likely to learn, find new opportunities be dynamic in our thinking and achieve our goals, building and managing your network doesn't have to feel like networking.

Join round to surround yourself with leaders from tech's most innovative companies build relationships, be inspired, take action, visit round dot tech slash apply and use promo code Lenny to skip the waitlist. That's round dot tech slash apply.

Ronnie. Welcome to the podcast. Thank you for having me. So you're known by many as maybe the leading expert on A B testing and experimentation, which I think is something every product company eventually ends up trying to do often badly. And so I'm excited to dig quite deep into the world of experimentation and A B testing to help people run better experiments. So thank you again for being here. Thank you.

Let me start with kind of a fun question. What is maybe the most unexpected A B test you've run or maybe the most surprising result from an A B test that you run? Yeah.

Speaker 105:06

So I think the the opening example that I use in my book and in my class is the most surprising public example we can talk about. And this is this was kind of an interesting experiment. Somebody proposed to change the way that ads were displayed on Bing the search engine. And he basically said, let's take the second line and move it, promote it to the first line so that the title line becomes larger.

And when you think about that. And there's, you know, if you're gonna look in my book or in the class, there's a, an actual diagram of what happened the screenshots. But if you think about it, it just realistically, it looks like a mad idea. Like why would this be such a reasonable, interesting thing to do?

And indeed, when we went back to the backlog, it was on the backlog for months and language there and many things were rated higher. But the point about this is it's trivial to implement. So if you think about return on investment, we could get the data by having some engineers spend a couple of hours implementing it.

And that's exactly what happened. Somebody Ed Bing who kept seeing this in the backlog and said, my God, we're spending too much Time discussing it. I could just implement that he did. He spent a couple of days implementing it. And as is, you know, the common thing at Bing, he launched the experiment.

And a funny thing happened, we had an alarm, big escalation. Something is wrong with the revenue metric.

Now, this alarm fired several times in the past when there were real mistakes where somebody would log revenue twice or you know, there's some data problem. But in this case, there was no bug we that simple idea, increased revenue by about 12%. And this is something that just doesn't happen. We can talk later about twin's Law. But that was the first reaction, which is, this is too good to be true. Let's find the bug.

And we did and we looked for several times and we replicated the experiment several times and there was nothing wrong with it. This thing was worth $100 million at the Time when Bing was a lot smaller. And the key thing is it didn't hurt the user metrics. So it's very easy to increase revenue by doing theatrics that, you know, displaying more ads is a trivial way to raise revenue, but it hurts the user experience.

And we've done the experiments to show that in this case, this was just a home run that improved revenue didn't significantly hurt the the guardrail metrics. And so I was, we were like in awe of, you know, what a trivial change. That was the biggest revenue impact of being in all its history.

Speaker 207:57

And that was basically shifting in two lines, right? Switching two lines in the search results, right?

Speaker 108:02

And this was just moving the second line to the first line. Now you then go and run a lot of experiments to understand what happened here. Is it the fact that the title line has a bigger fond sometimes different color. So we ran a whole bunch of experiments and this is what usually happens. We have a breakthrough.

You start to understand more about what can we do. And there was suddenly a shift towards OK. What are other things we could do that would allow us to improve revenue? And we came up with a lot of follow on ideas that helped a lot. But to me, this was an example of a tiny change.

That was the best revenue generating idea in Bing's history and we didn't rate it properly, right. Nobody gave this the the priority that in hindsight, it deserves. And that that's something that happens often. I mean, we are often humbled by how bad we are at predicting the outcome of experiments.

Speaker 209:01

This reminds me of a classic experiment at Airbnb while I was there and we'll talk about Airbnb in a bit. The search team just ran a small experiment of what if we were to open a new tab every Time someone clicked on a search result instead of just going straight to that listing. And that was one of the biggest wins in search. Yeah. And by the way.

Speaker 109:19

I, I don't know if you know the history of this, but I tell about this in class. We did this experiment way back around 2008 I think. And so this predates Airbnb. And I, I remember it was heavily debated, like why would you open something in a new tab? The users didn't ask for it.

It was a lot of pushback from the designers and we ran that experiment. And again, it was one of these highly surprising results that made it that we learned so much from it. So we, we first did this, it was done in the UK for opening Hotmail and then we moved it to MS N.

So it would open search in Utah and all the set of experiments were highly, highly beneficial. We published this. And I have to tell you when I came to Air B NBI talked to our joint friend Ricardo about this and it was sort of done. It was very beneficial and then it was semi forgotten, which is one of the things you learn about institutional memories when you have winners, make sure to address them and remember them.

So it was an Air BNB done for a long Time before I joined that listings open in a new tab. But other things that were designed in the future were not done. And I reintroduced this to the team and we saw big improvements.

Speaker 210:35

Shout out to Ricardo, our mutual friend who helped make this conversation happen. There's this like holy grail of experiments that I think people are always looking for of like one, you know, hour of work and it creates this massive result. I imagine this is very rare and I don't expect this to happen, I guess in your experience, how often do you find kind of one of these gold nuggets just lying around? Yeah.

Speaker 110:57

So again, this is a topic that's near and dear to my heart. Everybody wants these amazing results and you know, I show them in chapter one in my book, multiple of these, you know, small efforts, huge gain.

But as you said, they're very rare. I think most of the Time the winnings are made sort of this inch by inch. And there's a graph that I show in my book, a real graph of how Bing ads has managed to improve the revenue per 1000 searches over Time.

And every month you can see a small improvement and a small improvement, sometimes a degradation because of legal reasons or other things. We, you know, there was some concern that we were not marking the ads properly. So you have to suddenly do something that you know, is gonna hurt revenue.

But yes, I think most results are inch by inch, you improve small amounts, lots of them. I think that the best example that I can say is a couple of them that I can speak about. One is that Bing the relevance team, hundreds of people all working to improve being relevant.

They have a, a metric we'll talk about, oh, we see the overall e criterion but they have a metric that their goal is to improve it by 2% every year. It's a small amount and that 2% you can see here's a 0.1 here's a 0.15 here's a 0.2 and then they add up to around 2% every year, which is amazing.

Another example that I am allowed to speak about from Air BNB is the fact that we ran some 250 experiments in my tenure there in search relevance. And again, small improvements added up. So this became overall a 6% improvement to revenue, you know, so when you think about 6% it's a big number, but it deca it came out not of one idea, but many, many smaller ideas that each gave you a small gain.

And in fact, I again, there's another number I'm allowed to say of these experiments, 92% failed to improve the metric that we were trying to move. So only 8% of our ideas actually were successful at moving the key metrics.

Speaker 213:17

There's so many threads I want to follow here. But let me follow this one right here. You just mentioned of 92% of experiments failed. Is that typical in your experience running seeing experiments run a lot of companies like what should people expect when they're running experiments, what percentage should they expect to fail?

Speaker 113:32

Well, first of all, I published three different numbers for my career. So overall at Microsoft, about 66% 2 3rd of ideas fail, right? And don't think the 66 is accurate, like, you know, it's about two thirds and Bing which is a much more optimized domain after we've been optimizing it for a while, the failure rate was around 85%.

So it's harder to improve something that you've been optimizing for a while. And then at Air BNB, this 92% number is, you know, the highest failure rate that I've observed. Now, I've quoted other sources that, you know, it's not that I worked at groups that were particularly bad booking Google ads. Other companies published numbers, there are around 80 to 90% failure rate of ideas.

This is where it's important of experiments. It is important to realize that when you have a platform, it's easy to get this number. You look at how many experiments were run and how many of them launched. Not every experiment maps to an idea. So it's possible that when you have an idea, your first implementation, you start an experiment boom, it's egregiously bad because you have a bug.

In fact, 10% of experiments tend to be aborted on the first date. Those are usually not that the idea is bad but that there is an implementation issue or something we haven't thought about that forces on a board, you may iterate and pivot again.

And ultimately, if you do two or three or four pivots or bug fixes, you may get to a successful launch. But those numbers of 80 to 92% failure are of experiments very humbling. I know that every group that starts to run experiments, they always start off by thinking that somehow they're different. And their successor is gonna be much, much higher and they're all humbled.

Speaker 215:29

You mentioned that you have this pattern of clicking a link and opening a new tab is a thing that just worked at a lot of different places. Yeah. Are there other versions of this? You, do you collect kind of a list of like here's things that often work when we wanna move. Yeah, there's some, some you could share. I don't know if you have a list in your head, like you give you two resources.

Speaker 115:49

One of them was a paper that we wrote called Rules of Thumb. And what we tried to do at that Time at Microsoft was to just look at thousands of experiments that run and extract some patterns.

And so that's, that's one paper that we can then put in the notes. Perfect. But there's another more, more accurate, I would say resource that's useful that I recommend to people. And it's a site called good U I dot org and Good you I dot org is exactly the site that tries to do what you're saying at scale. So guy, the name is Jacob Leovy.

He asks people to send them results of experiments and he derives, he puts them into patterns. There's probably like 100 and 40 patterns I think at this point. And then for each pattern, he says, well, who hasn't helped how many times and by how much So you have an idea of, you know, this worked three out of five times and it was a huge win. In fact, you can find that open a new window in there.

Speaker 216:55

I feel like you feed that into chat GP T and you have basically a product manager creating a road map tool in general.

Speaker 117:02

By the way, this is all about a lot of that is institutional memory, right? Which is, can you document things well enough so that the organization remembers the successes and failures and learns from them. I think one of the mistakes that some company makes is they launch a lot of experiments and never go back and summarize the learning.

So I've actually put a lot of effort in this idea of institutional learning of doing the quarterly meeting of the most surprising experiments. By the way, surprising is a is another question that people often are not clear about what is a surprising experiment.

To me. A surprising experiment is one where the estimated result beforehand and the actual result differ by a lot. So that absolute value of the difference is large. Now, you can expect something to be great and it's flat. Well, you learn something but if you expect something to be small and it turns out to be great like that a title promotion, then you've learned a lot.

Or conversely, if you expect that something will be small and it's very negative you can learn a lot by understanding why this was so negative. And that's interesting. So we focus not just on the winners but also surprising losers, things that people thought would be a no brainer to run.

And then for some reason, it was very negative and sometimes it's that negative that gives you into, I actually, you know, I'm just coming up with one example of that, that I should mention we were running this experiment at Microsoft to improve the Windows indexer.

And the team was able to show on offline test that it does much better in indexing. And you know, they showed some relevance is higher and all these good things and then they ran it as an experiment and you know what happened?

Surprising result, indexing the relevance was actually high but it killed the battery life.

So here's something that comes from left field that you didn't expect it was consuming a lot more CPU on laptops, it was killing the laptops and therefore OK, we learned something, let's document it, let's remember this so that, you know, we now take this other factor into account as we design the next iteration.

Speaker 219:23

What advice do you have for people to actually remember these surprises? You said that a lot of it is institutional. What do you recommend people do so that they can actually remember this when people leave, say three years later.

Speaker 119:34

Document it, you know, right. You know, we had a large deck internally of these successes and failures. And we encourage people to look at the other thing that's very beneficial is just to have your whole history of experiments and do some ability to search by keywords, right?

So I'm I have an idea, type a few keywords and see if from the thousands of experiments that ran. And by the way, these are very reasonable numbers at Microsoft. Just to let you know when I left in 2019, we were on a rate of about 20 to 25,000 experiments every year.

So every working day we were starting something like 100 new treatments, big numbers. So when you're running in a group like Bing, which is running thousands and thousands of experiments, you wanna be able to ask as anybody did an experiment on this or this or this.

And so that searching capability is in the platform. But more than that, I think just doing the quarterly meeting of the most successful, most interesting, sorry, not just successful. Most interesting experiments is very key and that also helps the flywheel of experimentation.

CHAPTER 2Experimentation culture at companies

Speaker 220:45

It's a good segue to something I wanted to touch on, which is there's often a, I guess the weariness of running too many experiments and being too data driven and the sense that experimentation just leads you to these micro optimizations and you don't really innovate and do big, do big things. What's your perspective on that? And then just can you be too experiment driven in your experience?

Speaker 121:08

I'm very clear that I'm a big fan of test everything, which is any code change that you make any feature that you introduce has to be in some experiment. Because again, I've observed this sort of surprising result that even small bug fixes, even small changes can sometimes have surprising unexpected impact.

And so I don't think it's possible to experiment too much.

I think it is possible to focus on incremental changes because some people say, well, you know, if we only tested 17 things around this and you have to think about, it's not just, it's like in stock, you need a portfolio, you need some experiments that are incremental, that move you in the direction that you know, you're gonna be successful over Time if you just try enough.

But some experiments have, you have to allocate sometimes to these high risk high reward ideas. We're gonna try something that's most likely to fail. But if it does win, it's gonna be a home run.

And so you have to allocate some efforts to that and you have to be ready to understand and agree that most will fail most of these high. And i it's amazing how many times I've seen people come up with new designs or a radical new idea and they believe in it.

And that's OK. I'm just cautioning them all the Time to say if you go for something big try it out but be ready to fail. 80% of the Time, right?

And one true example that again, I'm, I'm able to talk about because we put it in my book is we were at bank trying to change the landscape of search. And one of the ideas, the big ideas was we're going to integrate with social.

So we hooked into the Twitter Firehose feed and we hooked into Facebook and we spent 100 person years on this idea and it failed.

You don't see it anymore. It existed for about a year and a half. And all the experiments were just negative to flat and, you know, it was an attempt, it was fair to try it. I think it took us a little long to fail to, to decide that this is a failure. But at least we had the data, we had hundreds of experiments that we tried. None of them were a breakthrough.

And I remember sort of mailing with some statistics showing that, you know, it's Time to abort, it's Time to fail on this. And, you know, he decided to continue more and it's a million dollar question, you know, do you continue? And then maybe the breakthrough will come next month or do you abort? And a few, a few months later, we, we aborted.

Speaker 224:07

That reminds me of at Netflix, they tried a social component that also failed Airbnb early on. There was a big social attempt to make like here's your friends have stayed at these airbnbs completely not had no impact. So maybe that's one of these learnings that we should talk about.

Speaker 124:22

This is hard, this is hard. And but that's again, that's the value of experiments which are this oracle that gives you the data. You may be excited about things, you may believe it's a good idea. But ultimately, the arbiter, the oracle is the controlled experiment. It tells you whether users are actually benefiting from it, whether you and the users, the company and the users.

Speaker 224:48

There's obviously a bit of overhead and downsides running an experiment, setting it all up and making sure, you know, analyzing the results. Is there anything that you ever don't think is worth A B testing?

Speaker 124:59

First of all, there are some necessary ingredients to A B testing and I'll just say, all right, not every domain is a minimal to be testing, right? You can't A B test, mergers and acquisitions, right? It's something that happens once you either acquire, you don't acquire. And so you do have to have some necessary ingredient.

You need to have enough units, mostly users in order to for the statistics to work out. So yeah, if you're too small, it may be too early to A B test. But what I find is that in software, it is so easy to run A B testing and it is so easy to build A platform, I don't say it's easy to build a platform. But once you build the platform, the incremental cost of running an experiment should approach zero.

And we got to that at Microsoft where after a while the cost of running experiments was so low that nobody was questioning the idea that everything should be experimented with. Now, I don't think we were there at Air BNB. For example, the platform at Airbnb was much less mature and required a lot more analysts in order to interpret the results and to find issues with it.

So I do think there's this tradeoff, you're willing to invest in the platform. It is possible to get the marginal cost to be close to zero. But when you're not there, it's still expensive. And there are, there may be reasons why not to run A B.

Speaker 226:27

Tufts, you talked about how you may be too small to run A B tests. And this is a constant question for startups is when should we start running A B tests? Do you have kind of a heuristic or rule thumb of just like here's a Time you should really start thinking about running an a.

Speaker 126:43

Million dollar question that everybody asks. So I actually, we'll put this in the notes but I gave a talk last year, what I call it is practical defaults. And one of the things I show there is that unless you have at least tens of thousands of users the math, the statistics just don't work out for most of the metrics that you're interested in.

In fact, you know, I gave an actual practical number of a retail site with some conversion rate trying to detect changes that are at least, you know, 5% beneficial, which is something that startups should focus on. They shouldn't focus on the 1% they should focus on the five and 10%.

Then you need something like 200,000 users, right? So start experimenting when you're in the tens of thousands of users, you'll be only be able to detect large effects. And then once you get to 200,000 users, then the magic starts happening, then you can start testing a lot more.

Then you have the ability to test everything and make sure that you're not degrading and getting value of presentation. So you ask for rule of thumb, 200,000 users, you're magical below that, start building the culture, start building the platform, start integrating. So that as you scale, you, you start to see the value, love it.

Speaker 228:01

Coming back to this kind of concern people have of experimentation keeps you from innovating and taking big bets. I know you have this framework overall evaluation criterion. And I think that helps with this. Can you talk a bit about that?

Speaker 128:14

The OEC or the overall evaluation criterion is something that I think many people that start to dabble in A B testing miss.

And the question is, what are you optimizing for?

And it's a much harder question that people think because it's very easy to say we're gonna optimize for money revenue.

But that's the wrong question because you can do a lot of bad things that will improve revenue.

So there has to be some countervailing metric that tells you how do I improve revenue without hurting the user experience? Ok. So let's take a good example. With search, you can put more ads on the page and you will make more money. There's no doubt about it. You will make more money in the short term.

The question is what happens to the user experience and how is that gonna impact you in the long term? So we've run those experiments and we were able to map out, you know, this number of ads causes this much increase to churn. This number of ads causes this much increase to the Time that users take to find a successful result.

And we came up with an OEC that is based on all these metrics that allows you to say, OK, I'm willing to take this additional money if I'm not hurting the user experience by more than this much, right? So there's a tradeoff there. One of the nice ways to phrase this as a constraint optimization problem. I want you to increase revenue, but I'm gonna give you a fixed amount of average real estate that you can use, right?

So you can, for one query, you can have zero ads for another query. You can have three ads for a third query. You can have wider, bigger ads. I'm just gonna count the pixels that you take the vertical pixels and I will give you some budget and if you can under the same budget, make more money, you're good to go.

Right. So that to me turns the problem from a badly defined, let's just make more money, right? Any page can start plastering more ads and make more money short term. But that's not the goal. The goal is long term growth and revenue, then you need to insert these other criteria. And what am I doing to the user experience?

One way around? It is to put this constraint. Another one is just to have these other metrics again, something that we did to look at the user experience. How long does it take the user to reach a successful click? What percentage of sessions are successful? These are key metrics that were part of the overall evaluation criterion that we've used.

I can give you another example by the way from, you know, the hotel industry or Airbnb that we both worked at.

CHAPTER 3Balancing user experience and metrics

Speaker 131:03

You can say I want to improve conversion rate, but you can be smarter about it and say it's not just enough to convert a user to buy or to pay for a listing. I want them to be happy with it several months down the road when they actually stay there. Right.

So that could be part of your OEC to say, what is the rating that they will give to that listing when they actually stay there? And that's a, that causes an interesting problem because you don't have this data. Now, you're gonna have it three months from now when they actually stay.

So you have to build the training set that allows you to make a prediction about whether this user, whether Lenny is gonna be happy at this cheap place or whether no, I should offer him something more expensive because Lenny likes to stay at nicer places where the water actually is hot and comes out of the faucet.

Speaker 231:53

And it's true. Ok. So it sounds like the core of this approach is basically have a kind of a drag metric that makes sure you're not hurting something that's really important to the business. And then being very clear on what's the long term metric we care most about to me that.

Speaker 132:06

The key here, the keyword is lifetime value, which is you have to define the OEC such that it is causally predictive of the lifetime value of the user, right? And that that's what causes you to think about things properly, which is, am I doing something that just helps me short term or am I doing something that will help me in the long term?

Once you put that model of lifetime value, people say, OK, what about retention rates? We can measure that. What about the Time to achieve a task? We can measure that. And those are these countervailing metrics that make it make the OEC useful.

Speaker 232:43

And to understand these longer term metrics, what I'm hearing is use kind of models and forecasts and predictions or would you suggest sometimes use like a long term holdout or some other approach? Like what do you find is the best way to think, see these?

Speaker 132:57

So there, there's two ways that I like to think about it. One is you can run long term experiments for the goal of learning something. So I mentioned that at B we did run these experiments where we increased the odds and decreased the odds so that we will understand what happens to the key metrics.

The other thing is you could just build models that use some of our background knowledge or use some, you know, they decide to look at historical. I'll give you another good example of this. When I came to Amazon, one of the teams that reported to me was the email team that it was not the transactional emails.

When you buy something, you get an email, but it was the team that sent these recommendations. You know, here's a book by an author that you bought. Here's a product that we recommend. And the question is, how do we give credit to that team. And the initial version was, well, whenever a user comes from the email and purchases something on Amazon, we're gonna give that email credit.

Well, it turned out this had no countervailing metric, the more emails you send, the more money you're gonna credit the team. And so that led to spam literally a really interesting problem. The team just ramped up the number of emails that they were sending out and claimed to make more money and their fitness function improved.

And, and then so then we backed up and then we said, ok, there, we can either phrase this as a constraint satisfaction problem. You're allowed to send user an email every days or which is what we ended up doing is let's model the cost of spamming the users. Ok. What's that cost? Well, when they unsubscribe, we can't mail them.

Ok. So we did some data science study on the side and we said, what is the value that we're losing from an unsubscribed? Right? And we came up with a number of a few dollars. But the point was now we have this countervail metric.

We say here's the money that we generate from the emails. Here's the money that we're losing a long term value. What's the tradeoff? And then when we started to incorporate those formula, more than half the campaigns that were being sent were negative.

Ok. So it was a huge insight at Amazon about how to send the right campaigns. And this led. And this is what I like about these discoveries. This fact that we integrated the unsubscribed led us to a new feature to say, well, let's not lose their future lifetime value through email.

When they unsubscribe, let's offer them by default to unsubscribe from this campaign. So when you get an email, you know, there's a new book by the author, the default to unsubscribe would be unsubscribe me from author emails.

And so now the the negative, the countervailing metric is much smaller. And so again, this was a breakthrough in our ability to send more emails and understand based on what users were unsubscribing from which ones are really beneficial.

Speaker 236:06

I love the surprising results.

Speaker 136:08

We all love them. Lots of, I mean, this is, this is the humbling reality and you know, people talk about the fact that A B testing sometimes leads you to incremental. I actually think that many of these small insights lead to fundamental insights about, you know, which areas to go, some strategies we should take some things we should develop, helps a lot.

Speaker 236:31

This makes me think about how every Time I've done a full redesign of a product, I don't think ever, has it ever been a positive result? And then the team always ends up having to claw back what they just hurt and try to figure out what they messed up is that your experience too Absolutely.

Speaker 136:49

Yeah. In fact, I, I've published some of these in, in linkedin Post showing a large set of, you know, big launches that redesigns that dramatically failed.

And it happens very often. So the right way to do this is to say yes, we want to do a redesign, but let's do it in steps and test on the way and adjust. So you don't need to take 17 new changes that many of them are going to fail, start to move incrementally in a direction that you believe is beneficial, adjust on the weight.

Speaker 237:25

The worst part of that, those experiences I find is it took like, I don't know, 36 months, 3 to 6 months to build it. And by the Time it's launched, it's just like we're not gonna unlatch this, everyone's been working in this direction. All the new features are assuming this is gonna work and you're basically stuck, right?

Speaker 137:41

I mean, this is the sun cost fallacy, right? We invested so many years in it. Let's launch this even though it's bad for the user. No, that's terrible. Yeah. Yeah. So this is this is the other advantage of recognizing this humble reality that most ideas fail, right?

If, if you believe in that statistics that I published, then doing 17 changes together is more likely to be negative. Do them in smaller increments, learn from it's called o fat one factor at a Time. Do one factor, learn from it and adjust of the 17, maybe you have four good ideas.

CHAPTER 4Embracing failure and learning

Speaker 138:18

Those are the ones that will launch and be positive.

Speaker 238:22

I generally agree with that and always try to avoid a big redesign, but it's hard to avoid them completely. There's often team members that are really passionate and like we just need to rethink this whole experience, we're not going to incrementally get there. Have you found anything effective in helping people either see this perspective or just making a larger bet more successful?

Speaker 138:42

By the way, I, I'm not opposed to large redesigns. I try to give the team the data to say, look, here are lots of examples where big redesigns fail, try to decompose your redesign if you can't decompose it to one factor at Time to a small set of factors at a Time and learn from these smaller changes, what works and what doesn't. Now it's also possible to do a complete redesign.

I'm just, as you said yourself, they'd be ready to fail, right? I mean, do you, do you really want to work on something for six months or a year and then run the A B test and realize that you've hurt revenues or other key metrics by several percentage points and a data driven organization will not allow you to launch, what are you gonna write in your annual review?

Speaker 239:33

Yeah, but nobody ever thinks it's gonna fail. I think. No, we got this. We talked to so many.

Speaker 139:37

People, but I think they start to run experiments are humbled early on from the smaller changes, right? You're right. Nobody, I'll tell you a funny story. When I came from Amazon to Microsoft, I joined the group and for one reason or another, that group disbanded a month after I joined.

And so people came to me and said, look, you just joined the company, you're at partner level, you figure out well, how you can help Microsoft. And I said I'm gonna build an Experimentation Platform because nobody at Microsoft is running experiments and 50% more than 50% of ideas in Amazon that we tried failed.

And the classical response was we have better P MS here, right? There was this complete denial that it's possible that 50% of ideas that Microsoft is implementing in a three year development cycle. By the way, this is how long it took office to release. It was a classical every three years we release and the the data came about showing that.

Yeah, you know, Bing was the first to truly implement experimentation at scale and we shared with the rest of the companies, the surprising results. And so when office was and this was, you know, credit to and Satya Nadella, they were ones that says, Ronnie, you know, you try to get office to run experiments, we'll give you the Air support.

And it was hard, but we didn't, you know, it was, it took a while but office started to run experiments and they realized that many of their ideas were failing.

Speaker 241:20

He said that there's a site of it failed redesigns. Was that, is that in your book or is that a site that you can point people to, to kind of help build this case?

Speaker 141:29

It's so I teach this in my class, but I, I've, I think I've posted this on linkedin and answered some questions. I'm happy to put that in the notes. Ok.

Speaker 241:37

Cool. We'll put that in the show notes because I think that's the kind of data that often helps convince a team. Maybe we shouldn't rethink this entire onboarding flow from scratch. Maybe we should kind of iterate towards and learn as we go.

This episode is brought to you by EOEO is a next generation A B testing platform built by Airbnb alums from modern growth teams. Companies like draftkings, Zai click up, Twitch and cameo, rely on eo to power their experiments wherever you work, running experiments is increasingly essential, but there are no commercial tools that integrate with a modern growth team stack.

This leads to waste of Time, internal tools or trying to run your own experiments through a clunky marketing tool.

When I was at Airbnb, one of the things that I loved most about working there was our Experimentation Platform where I was able to slice and dice data by device types, country user stage EPO does all that and more delivering results quickly avoiding annoying prolonged analytic cycles and helping you easily get to the root cause of any. You discover.

Eo lets you go beyond basic click through metrics and instead use your North Star metrics like activation retention, subscription and payments. Eo supports test on the front end, on the back end, email marketing, even machine learning clients check out eo at get eppo dot com. That's get eo dot com and 10 year experiment velocity.

Is it ever worth just going? Let's just rethink this whole thing and just give it a shot to break out of a lo a local minimum or local maxima essentially.

Speaker 143:04

So I, I think what you said is fair. I mean, I I do want to allocate some percentage of resources to big bets. As you said, we've been optimizing this thing to hell. Could we completely redesign it? It's a very valid idea. You may be able to break out of a local minimum.

What I'm telling you is 80% of the Time you will fail. So be ready for that, right? What, what people usually expect is my redesign is going to work. No, you're most likely going to fail. But if you do succeed, it's a breakthrough.

Speaker 243:35

I like this 80% rule of thumb is that just like a simple way of thinking about it, 80%.

Speaker 143:40

Rule of thumb. And you know, you had you know, I've heard people say it's 70% or, or 80%. But it's in that area where I think, you know, when you talk about how much to invest in the known versus the high risk, high reward, that's usually the right percentage that most organizations end up doing this allocation.

But you interviewed Treas, I think he mentioned that you know, that at Google is like 70% you know, the search and ads and it's the 20% for some of the apps and new stuff and then it's the 10% for infrastructure.

Speaker 244:16

Yeah. And I think the, the most important point there is if you're not running an experiment, 70% of stuff you're shipping is hurting your business.

Speaker 144:23

Well, it's not hurting. It may, it's flat, too negative. Some of them are flat. And by the way flat to me, if something is not that big, that's a no ship because you've just introduced war code, there is a maintenance overhead to shipping your stuff. I've heard people say, look, we already spent all this Time. The team will be demotivated if we don't ship it.

And I'm no, that's wrong guys, right. You know, let's make sure that we understand that shipping, this project has no value is complicating. The code base maintenance costs will go up. You don't ship on flat unless it's a sort of a legal requirement, right? When legal comes along and says you have to do X or Y you have to ship on flat or even negative and that's understandable.

But again, I think that's something that a lot of people make the mistake of saying legal told us we have to do this. Therefore, we're gonna take the hits. No legal gave you a framework that you have to work under. Try three different things and ship. The one that hurts the least.

Speaker 245:25

I love. That reminds me when Airbnb launched the rebrand, even that they ran as an experiment with the entire home page redesign, the new logo and all that. And I think there was a long term holdout even. And I think it was positive in the end from what I remember.

Speaking of Airbnb, I want to chat about Airbnb briefly, I know there's and you're limited in what you can share. But it's interesting that Air BNB seems to be moving in this other direction where it's becoming a lot more top down Brian vision oriented. And Brian's even talked about how he's less motivated to run experiments.

He doesn't want to run as many experiments as they used to. Things are going well. And so, you know, it's hard to argue with the success. Potentially, you worked there for many years, you ran the search team essentially, I guess just what was your experience like there? And then roughly what's your sense of how things are going, where it's going.

CHAPTER 5Data-driven decision making in uncertain times

Speaker 146:15

So as you, as you know, and I'm I'm restricted from talking about Air. Air B NBI will say a few things that I am allowed to say one is in my team in search relevance, everything was A B tested.

So while Brian can focus on some of the design aspects that people who are actually doing, you know, the neural networks and the search, everything was A B tested to help. So nothing was launching without an A B test. We have targets around improving cer certain metrics and everything. Was that A B test? Now other teams, some did, some did not.

I I will say that, you know, when you say things are going well, I think we don't know the counterfactual I believe that had Air BNB kept people like Greg Greeley, which was pushing for a lot more data driven and had Air BNB run more experiments. It would have been in a better state than today, but it's the counterfactual. We don't know.

Speaker 247:14

It's a really interesting perspective. Yeah, Airbnb is such an interesting natural experiment of a way of doing things differently. There's like deemphasizing experiments and also they turned off paid ads during COVID.

And I think, I don't know where it is now, but it feels like it's become a much smaller part of the growth strategy. Who knows if they've ramped it up to back to where it is today. But I think it's gonna be a really interesting case study. Looking back, I don't know, 5, 10 years from now.

Speaker 147:38

It's a one-off experiment where it's hard to assign value to some of the things that Air BNB is doing. I personally believe it could have been a lot bigger and a lot more successful if it had run more controlled experiments. But I can't speak about some of those that I ran and that showed us that some of the things that were initially untested were actually negative and could be better.

Speaker 248:04

All right, mysterious.

One more question, Airbnb, you were there during COVID, which was quite a wild Time for Airbnb. We had sun on the podcast talking about all the craziness that went on when travel basically stopped and there was a sense that Airbnb was done and travel is not gonna happen for years and years.

What's your take on experimentation in that world where you have to really move fast, make crazy decisions and make big decisions. What did you, what was like during that Time?

So II I.

Speaker 148:35

Think actually in a state like that it's even more important to run A B tests, right? Because what you want to be able to see is if we're making this change, is it actually helping in the current environment? You know, there's this idea of external generalize, is it gonna work out now during COVID? Is it gonna generalize later on?

These are things that you can really answer with the controlled experiments? And sometimes it means that you might have to replicate them six months down when COVID say is not as impactful as it is. Saying that you have to make decisions quickly. To me, I'll point you to the success rate. Like if, if in peace Time, you're wrong two thirds to 80% of the Time, why would you be suddenly right in war Time?

Right, in COVID Time. So, I, I don't believe in the idea that because bookings went down materially, the company should certainly, you know, not be data driven and do things differently. I think if Air BNB stayed the course, did nothing, the revenue would have gone up in the same way.

In fact, if you look at one investment, one big investment that was done at the Time was online experiences and the initial data wasn't very promising. And I think today it's a footnote.

Speaker 250:01

Yeah, what a another case study for the history books, Airbnb Experiences. I want to shift a little bit and talk about your book, which you mentioned a couple of times. It's called Trustworthy Online Controlled Experiments. And I think it's basically the book on A B testing.

Let me ask you just what surprised you most about writing this book and putting it out in, in the reaction to it?

Speaker 150:24

I was pleasantly surprised that it sold more than what we thought and more came more than what Cambridge predicted. So when, when first we were approached by Cambridge after a tutorial that we did to write a book, I was like, I don't know, this is too small of a niche area.

And I, you know, they were saying, so you'll be able to sell a few 1000 copies and help the world. And I found, you know, my coauthors, which are great and, you know, we wrote a book that we thought is not statistically oriented, has fewer formulas than you normally see and focuses on the practical aspects and on trust, which is the key the book, as I said, you know, was more successful.

It sold over 20,000 copies in English. It was translated to Chinese Korean, Japanese and Russian. And so it's, it's great to see that we help the world become more data driven with experimentation. And I'm happy because of that.

I was pleasantly surprised by the way, all proceeds from the book are donated to charity. So I'm, if I'm pitching the book here, I there is no financial gain for me from having more copies sold. I think we made that decision, which was a good decision. All proceeds go with the charity.

Speaker 251:47

Amazing. I didn't know that we'll link to the book in the show. That's you talked about how trust like it's trust is in the title. You just mentioned how important trust is to experimentation. A lot of people talk about how do I run experiments faster? You focus a lot on trust. Why is trust so important in running experiments?

Speaker 152:04

So to me, the Experimentation Platform is the safety net and it's an oracle. So it serves really two purposes. The safety net means that if you launch something bad, you should be able to abort quickly, right, safe deployments, safe velocity.

There are some names for this, but this is one key value that the platform can give you the other one, which is the more standard one is at the end of the two week experiment, we will tell you what happened to your key metric and do many of the other surrogate and debugging and guard rail metrics trust builds up, it's easy to lose.

And so to me, it is very important that when you present this and say this is science, this is a controlled experiment. This is the resolve you better believe that this is trustworthy. And so I focused on that a lot. I think it allowed us to gain the organizational trust that this is really.

And the nice thing is when we, we built all these checks to make sure that the experiment is correct. If there was something wrong with it, we would stop and say, hey, something is wrong with the experiment. And I think that's something that some of the early implementations in other places did not do. And it was a big mistake.

I've mentioned this in my book. So I can mention this here optimized in its early days, we're very statistically naive. They sort of said, hey, we're real Time, we can compute your P values in real Time. And then you can stop an experiment when the P value is statistically significant.

That is a big mistake that inflates your what's called type one error or the false positive rate materially. So if you think you've got a 5% type one error or you aim for that P value less than 0.05 using real Time sort of P value monitoring to optimize the offered, you would probably have a 30% error rate.

So what this learnt is that people that started using optimize, thought that the platform was telling them they're very successful. But when they actually started to see, well, it told us this is positive revenue, but I don't see this over Time. Like by now, we should have made double their money. So their questions started to come up around the trust in the platform.

There's a very famous post that somebody wrote about how optimized he almost got me fired by a person who basically said, look, I came to the organ, I said, we have all these successes. But then I said something is wrong and he tells us how he ran an A, a test when there is no difference between the A and the B and optimized.

They told them that it was statistically significant too many times optimized. He learned optimized. The, you know, several people pointed, I pointed this out in my Amazon review of the book that the, the author wrote early on, I said, hey, you are not doing the statistics correctly.

Other, you know, Ramesh Jo at Stanford pointed this out, became a consultant to the company and then they fixed it. But to me, that's a very good example of how to lose trust. They lost a lot of trust in the market, they lost all this trust because they built something that had very much inflated heroic.

Speaker 255:26

That is a pretty scary to think about. You've been running all these experiments and they weren't actually telling you accurate results. What are signs that what you're doing may not be valid if you're starting to run experiments and then just how do you avoid having that situation? What kind of tips can you share for people trying to run experiments?

Speaker 155:47

You know, there's a whole chapter of that in my book. But I'll say maybe one of the things that is the most common occurrence by far, which is a sample ratio mismatch. Now, what is a sample ratio mismatch if you design the experiment to send 50% of users to control and 50% of users to treatment it supposed to be a random number or you know hash function.

If you get something off from 50% it's a red flag. So let's take a real example, let's say you're running an experiment and it's large, it's got a million users and you got 50.2.

So people say, well, I don't know, it's not gonna be exactly the same as 50.2 reasonable or not. Well, there's a formula that you can plug in. I have a spreadsheet available for those that are interested and you can tell here's how many users are in control. Here's how many users have in treatment.

My design was 50 50 it tells you the probability that this could have happened by chance. Now, in a case like this, you plug in the numbers, it might tell you that this should happen one in half a million experiments or unless you run a half a million experiment, very unlikely that you would get a 50.2 versus 49.8 split.

And therefore something is wrong with the experiment right now. People, I, I remember when we first implemented this check, we were surprised to see how many experiments suffered from this, right?

And there's a paper that was published in 2018 and where we share that at Microsoft, even though we'd be running experiments for a while, is around 8% of experiments that suffered from the sample regime mismatch. And it's a big number. But think about this, you're running 20,000 experiments a year. So many of them, 8% of them are invalid.

And we, somebody has to go down and understand what happened here. We know that we can't trust the results but why? So over Time you begin to understand there's something wrong with the pipe data pipeline. There's something that happens with bots, bots are a very common factor for causing a sample ratio mismatch.

So there's a whole that paper that was published by my team talks about how to diagnose sample ratio mismatches in the last probably year and a half.

It was amazing to see all these third party companies implement sample ratio mismatches and all of them were reporting oh my God, you know, 6% 8% 10%. So yeah, they were, it's, it's sometimes fun to go back and say how many of your results were in the past were invalid before you had this sample ratio mismatch test.

Speaker 258:32

And it's frightening is the most common reason this happens is you're signing users in, in kind of the wrong place in your, in your code.

Speaker 158:40

So when you say most common, I think the most common is bots somehow they hit the control or the treatment in different proportions because you change the website. The bot may fail to parse the page and try to hit it more often. That's a a classical example. Another one is just the data pipeline.

We've had cases where we were trying to remove bad traffic under certain conditions and it was skewed because of the control and treatment. I've seen people that start an experiment in the middle of this site on some page, but they don't realize that some campaign is pushing people from the side.

So there's multiple reasons. It is surprising how often this happens. And I'll tell you a funny story, which is when we first added this test to the platform, we just put a banner saying you have a sample ratio, mismatch do not trust these results.

And we noticed that people ignored it. They were starting to present results that had this banner. And so we blanked out the scorecard. We put a big you know red can't see this result. You have a sample ratio, mismatch click OK?

To expose the result and why we do we need that, OK? We need that OK button because you want to be able to debug the reasons and sometimes the metrics help you understand why you have a sample ratio mismatch.

So we blanked out the scorecard, we had this button and then we started to see that people press the button and still presented the results of experiments with the sample ratio mismatch. So we ended up with an amazing compromise, which is every number in the scorecard was highlighted with a red line.

So that if you took a screenshot other people could tell you how the sample ratio is less.

Speaker 201:00:24

Freaking product managers. This is this is intuition.

Speaker 101:00:29

People just say, well my srm was small. Therefore, I can still present the results, people wanna see success. I mean, this is a natural bias and then we have to be very conscientious and fight that bias and say when something looks too good to be true, investigate.

Speaker 201:00:46

Which is a great segue to something you mentioned briefly. Something called Tomans Law, you talk about that.

Speaker 101:00:52

Yes, Soloman Law, you know, the, the general statement is if any figure that looks interesting or different is usually wrong. It was first said by this person in the UK who worked on radio media, but I'm a big fan of it. And you know, my main claim to people is if the result looks too good to be true.

If you suddenly moved your, you know, your normal movement of an experiment is under 1% and you suddenly have a 10% movement, hold a celebratory dinner like it was just your first reaction, right? Let's take everybody to a Fancy dinner because we just improved revenue by millions of dollars. Hold that dinner. Investigate c because there's a large probability that something is wrong with the result.

And I will say that nine out of 10 when we call out Time's Law, it is the case that we find some flaw in the experiment. Now, there are obviously outliers, right? That first experiment that I showed where we promoted that made long ad titles that was successful, but that was replicated multiple times and double and triple checked and everything was good about it. Many other results that were so big turned out to be false.

CHAPTER 6Understanding p-values and experiment validity

Speaker 101:02:05

So I'm a big, I'm a big, big fan of Tomas Law. There's a deck. I can also give this in a note where I shared some real examples of t to Law.

Speaker 201:02:14

Amazing. I wanna talk about rolling this out at companies and things that run, you run into that fail. But before I get to that, I'd love for you to explain just P value. I know that people kind of misunderstand it. And this might be a good Time just to help people understand. What is it actually telling you that P value is 8.05. I, I don't know if this.

Speaker 101:02:30

Is the, the right forum for explaining P values because the definition of A P value is simple. What it hides is very complicated. So I'll say one thing which is many people assign one minus P value as the probability that your treatment is better than control. So you ran an experiment, you got a P value of 0.02. They think there's a 98% probability that the treatment is better than the control that is wrong.

Ok. So rather than defining P values, I wanna cautious, caution everybody that the most common interpretation is incorrect. P value assumes it's a conditional probability or an ass or assume probability, it assumes that the null hypothesis is true.

And we're computing the probability that the data we're seeing, it matches the hypothesis. It's no hypothesis. In order to get the probability that most people want, we need to apply base rule and invert the probability from the probability of the data.

Given the hypothesis to the probability, the hypothesis, given the data for that, we need an additional number, which is the probability, the prior probability that the hypothesis that you're testing is successful or not, that's an unknown. What we do is we can take historical data and say, look, people fail two thirds of the Time or 80% of the Time.

And we can apply that number and compute that. We've done that in a paper that I will give it the notes so that you can assess the number that you really want that what's called the false positive risk. So I think that's something for people to internalize that.

What you really want to look at is this false positive risk, which tends to be much, much higher than the 5% that people think. Right. So if you're, I think the classical example in the Air BNB where the failure rate was very, very high is that when you get a statistically significant resolve, let me actually pull the note so that I know how to have the actual number.

If you're at Airbnb with the success rate of or Airbnb search where the success rate is only 8%. If you get a statistically significant result with a P value less than 0.05 there is a 26% chance that this is a false positive result, right?

It's not 5% it's 26%. So that's the number that you, that you have in your mind. And that's why when I worked in Air BNB, one of the things we did is we said, OK, if you're less than 0.05 but above 0.01 rerun replicate, when you replicate, you can combine the two experiments and get a combined P value using something called Fisher's method or Staffer's method.

And that gives you the joint probability and that's usually much, much lower. So if you get 2.05 or something like that, then the joint, the probability that you've got them is much, much lower.

Speaker 201:05:26

Wow. I have never heard it described that way. It makes me think about how like even data scientists and our teams are always just like this isn't perfect. Like we're not 100% sure this experiment is positive, but on balance, if we're launching positive experiments, we're probably doing good things. It's OK if sometimes we're wrong, but it's.

Speaker 101:05:43

True on balance, you're probably better than 50 50\. But people don't appreciate how much that 26% that I mentioned is high. And the reason that I want to be sure is that I think it leads to this idea of the learning, the institutional knowledge, what you wanna be able to say is share with the organ success.

And so you wanna be really sure that you're successful. So by lowering the P value, by forcing teams to work with the P value, maybe below 0.01 and do replication on hires, then you can be much more successful and, and the false positive rate will be much, much lower.

Speaker 201:06:20

Fascinating and also shows the value of keeping track of just what percent of your experiments are failing historically at the company or within that specific product.

Say someone listening, wants to start running experiments. They say they have tens of thousands of users at this point. What would be the first couple of steps you'd recommend?

Speaker 101:06:38

Well, see if they have somebody in the org that has previously been involved experiment. That's a good way to consult internally. I think that the key decision is whether you want to build or buy.

There's a whole series of eight sessions that I posted on linkedin where I invited guest speakers to talk about those problems. So if people are interested, they can look at how, what the vendor say and what a agency said about build versus buy question. And it's usually not a 01\.

It's usually a both. You build some and you buy some and it's a question of, do you build 10% or do you build a 90%. I think for people starting the third party products that are available today are pretty good. This wasn't the case when I started working.

So when I started building or running experiments at Amazon, we were building the platform because nothing existed. Same at Microsoft. I think today there's enough vendors that provide good experimentation platforms that are trustworthy that I would say not a good way to consider. Using one of those.

Speaker 201:07:45

Say you're at a company where there's resistance to experimentation and A B testing, whether it's a startup or a bigger company, what have you found works in helping shift that culture? And how long does that usually take? Especially at a larger company.

Speaker 101:07:58

My general experiences with Microsoft where, you know, we, we went with this beach head of Bing, we were running a few experiments and then we were asked to focus on Bing and we scaled experimentation and build a platform at scale at Bing once Bing was successful and we were able to share all these surprising results.

I think that many, many more people in the company were amenable and it's all, it was also the case that helped a lot that, you know, there's the usual cross pollination people from being moved out to other groups. And that helped these other groups say, hey, there's a better way to build software.

So I think if you're starting out, find a place, find a team where experimentation is easy to run. And by that, I mean, they're launching often, right? Don't go with the team that launches every six months or, you know, office used to launch every three years.

Go with the team that launches frequently. You know, they're running on sprints, they launch every week or two, sometimes they launch, I mean, being used to launch multiple times a day and then make sure that you understand the question of the OEC. Is it clear what they're optimizing for?

Right?

There are some groups where you can come up with a good OEC, some groups are harder, you know, I remember one funny example was the Microsoft dot com website which this is not MS N, this is Microsoft dot com has like multiple different constituencies that are trying to determine this is a support site and this is some the ability to sell software through this site and it's, and, and warn you about, you know, safety and updates.

It has so many goals. I remember when the team said we want our own experiments and I and I brought the group in and some of the managers and I said, do you know what you're optimizing for? It was very funny because the they, they surprised me. They said, hey, Ronnie, we read some of your papers. We know there's this term called OEC.

We decided the Time on site is ro is it?

And I said, wait a minute, some of your main goals is support site, is people more spending more Time on a support site, a good thing or a bad thing. And then half the room thought that more Time is better and half the room thought that more Time is worse. So, and nobody sees bad if directionally, you can't agree on it.

Speaker 201:10:18

That's a great tip along the same lines. I know you're a big fan of platforms and building a platform to run experiments versus just one off experiments. Can you just talk briefly about that to give people a sense of where they probably should be going with their experimentation approach?

Speaker 101:10:32

Yeah, I mean, so I think the motivation is to bring the marginal cost of experiments down to zero. So the more you self-service, right, go to a website, set up your experiment, define your targets, define the metrics that you want, right? People don't appreciate that the number of metrics starts to grow really fast if you're doing things right?

And being you could define 10,000 metrics that you wanted to be in your scorecard, big numbers. So it was so big and people said it's computationally inefficient, we broke them into templates so that if you were launching a U I experiment, you would get this set of 2000\.

If you're doing a revenue experiment, you would get this set of 2000 if you're doing. So the point was build a platform that can quickly allow you to set up and run an experiment and then analyze it. I think, you know, one of the things that I will say at Air BNB is the analysis was relatively weak.

And so lots of data scientists were hired to be able to compensate for the fact that the platform didn't do enough. And so and this happens in other organizations too where there's this tradeoff, like if you're building a good platform, invest in it so that more and more automation will allow people to look at the analysis. Without the need to involve a data scientist.

CHAPTER 7Building trust and speed in experimentation

Speaker 101:11:54

We published a paper again, I'll give it in the notes with this, you know, sort of a nice matrix of six axes and how you move from crawl to walk, to run, to fly and what you need to build on those six axes.

So if you know one of the things that I do sometimes when I can solve is I go into the organ and say, where do you think you are on these six axis? And that should be the guidance for what are the things you need to do next?

Speaker 201:12:21

This is gonna be the most epic show notes episode we've had yet. Maybe a last question we talked about how important trust is to running experiments and how even though people talk about speed trust ends up being most important, still I want to ask you about speed. Is there anything you recommend for helping people run experiments faster and get results more quickly that they can implement.

Speaker 101:12:41

So I'll say a couple of things, one is if your platform is good, then when the experiment finishes, you should have a scorecard soon after. I mean, it takes a day, but it shouldn't be that you have to wait a week for the data scientist. To me, this is the number one way to speed up things.

Now, in terms of using the data efficiently, there are mechanisms out there under the title of variance reduction that help you reduce the variance of metrics so that you need less users so that you can get results faster. Some examples that you might think about are capping metrics. So if your revenue metric is very skewed, maybe you say, well, if somebody purchased over $1000 let's make that $1000 at Air BNB.

One of the key metrics, for example, is Knights Booked. Well, it turns out that some people book tens of nights, they're like an agency or something. Hundreds of nights. You may say, OK, let's just cap this. It's unlikely that, you know, people book more than 30 days in a given month. So that various reduction technique will allow you to get statistically significant results faster.

And a third technique is called cupid, which is an article that we published again. I can give it in the notes which uses the pre experiment data to adjust the result and we can show that you get the result as unbiased but with lower variants and help it. Hence, it requires fewer users.

Speaker 201:14:11

Ronnie. Is there anything else you want to share before we get to our very exciting Lightning Round?

Speaker 101:14:15

No, I think we've asked a lot of good questions.

Hope people enjoy this.

Speaker 201:14:21

I know they will. Lightning Round Lightning Round. Here we go. I'm just gonna roll right into it. What are two or three books that you recommended most to other people?

Speaker 101:14:29

There's a fun book called Calling Bullshit, which is despite the sort of name, which is a little extreme, I think for title, it actually has a lot of amazing insights that I love and, and it sort of embodies in my opinion, a lot of the twin's Law of showing that things that are too extreme, your bullshit meter should go up and say, hey, I don't believe that. So that was, that's my number one recommendation.

There's a slightly older book that I love called Hard Facts, Dangerous Half Truths and Total Nonsense by the Stanford professors from the graduate school of business. Very interesting to see many of the things that we grew up with as sort of well understood, turn out to have no justification. And then so with Stranger book, which I love sort of on the verge of psychology is called mistakes were made, but not by me.

About all the fallacies and, and that, that we fall into, and the humbling results from that.

Speaker 201:15:38

The titles of these are hilarious and there's a common theme across all these books.

Next question, what is a favorite recent movie or TV show?

Speaker 101:15:47

So I recently saw a short series called Chernobyl On The Disaster. It, I, I thought it was amazingly well done, highly recommended, you know, based on true events.

You know, as usual, there's some freedom for the artistic movie. They, that it was kind of interesting at the end. They say this woman in the movie wasn't really a woman. It was a bunch of 30 data scientists, not data scientists, 30 scientists that in real life presented all the data to the leadership of what to do.

Speaker 201:16:22

I remember that. Fun fact. I was born in Odessa Ukraine, which was not so far from Chernobyl. And I remember my dad told me he had to go to work. They called him into work that day to clean some stuff off the trees. I think ash from the explosion or something.

It was like far away where I don't think we were exposed. But but yeah, we were in the vicinity. That's pretty scary. My wife thinks I've every, every Time something's wrong with me, she's like, oh, that must be a Chernobyl Chernobyl thing.

Ok. Next question, favorite interview question you like to ask people when you're interviewing them.

Speaker 101:16:56

So it depends on an interview, but I'll I'll give you when I do a technical interview, which I do less of. But one question that I love that, that is amazing how many people it throws away for languages like C++ is, tell me what the static qualifier does. And for, for multiple, you know, you can do it for a variable, you can do it for a function.

And it is just amazing that I would say more than 50% of people that interview for engineering job cannot get this and get it awfully wrong.

Speaker 201:17:32

Definitely the most technical answer to this question.

Ok. What's the favorite recent product you've discovered that you love blink cameras?

Speaker 101:17:42

So a blink camera is this small camera, you stick in two AA batteries and it lasts for about six months. They claim up to two years.

My experience is usually about six months, but it was just amazing to me how you could throw these things around in the yard and see things that you would never know otherwise, you know, some animals that go by, we had a skunk that we couldn't figure out how it was entering. So I threw five cameras out and I saw where he came in.

Where did it come in? He came in under a hole in the fence that was about this high. I I cannot, I have a video of this thing just squishing underneath. We never would have assumed that it came from there, from the neighbor.

But yeah, it's, these things have just changed and when you're away on a trip, it's always nice to be able to say, you know, I can see my house, everything's ok. You know, at one point we had a false alarm and the cops came in and had this amazing video of how they're entering the house and pulling the guns down.

Speaker 201:18:57

You gotta share that on TikTok. That's good content.

Oh Wow. Ok. But cameras, we set those up in my house as a Yes.

What is something relatively minor you've changed in the way your teams develop product that has had a big impact on their ability to execute.

Speaker 101:19:13

I think this is something that I learned at Amazon, which is a structured narrative.

So Amazon has some variants of this which sometimes, but then they go by the name of a six page or something. But when I was at Amazon, I still remember that email from Jeff which is no more Power Point. I'm gonna force you to write a narrative.

I took that to heart and many of the features that the team presented instead of a Power Point, you start off with a structured document that tells you what you need, the questions you need to answer for your idea.

CHAPTER 8Importance of evidence and structured narratives

Speaker 101:19:48

And then we review them as a team and Amazon, these were like paper based now it's all, you know, based on Word Or Google Docs where people comment and I think the impact of that was amazing. I think it the, the ability to give people honest feedback and have them appreciate and have it stay after the meeting was, you know, in these notes on the document.

Speaker 201:20:12

Just amazing final question. Have you ever run an A B test on your life? Either your dating life, your family, your kids. And if so, what did you try?

Speaker 101:20:21

So there aren't enough units. Remember? I said you need 10,000 or something to run through A B tests. I do. I will say a couple of things. One is I, I try to emphasize to my family and friends and everybody, this idea called the hierarchy of evidence. When you read something, there's a hierarchy of trust levels.

If something is anecdotal, don't trust it. If there was an experiment, it was observational. Give it some bit of trust as you get more up and up to a natural experiment and controlled experiments and multiple control experiments, your trust levels should go up.

So I think that that's a very important thing that a lot of people miss when they see something in the news is where does it come from? I have a, a talk that I, I've shared of all these observational studies that people made that were published and then somehow a control experiment was run later on and proved that it was directionally incorrect.

So I, I think there's a lot to learn about this idea of the hierarchy of evidence and share it with our family and kids and, and friends and there's a, now, I think there's a book that's based on this. It is like how to read a book.

Speaker 201:21:34

Well, Ronnie, the experiment of us recording a podcast I think is 100% positive P value 0.0. Thank you so much for being here.

Speaker 101:21:44

Thank you so much for inviting me and for great questions.

Speaker 201:21:48

Amazing. I appreciate that. Two final questions. Where can folks find you online if they want to reach out? And is there anything that listeners can do for you finding me.

Speaker 101:21:56

Online is easy. It's linkedin. And what can people do for me, you know, understand the idea of control experiments as a mechanism to make the right data driven decisions, use science, you know, learn more by reading my book.

If you want again, all proceeds go to charity. And if you want to learn more, there's a class that I teach every quarter on Maven, we'll put in the notes how to find it. And some discount for people who manage to stay all the way to the end of this podcast.

Speaker 201:22:31

Yeah, that's awesome. We'll include that at the top. So people don't miss it. So there's gonna be a code to get a discount on your course, Ronnie. Thank you again so much for being here. This was amazing. Thank you so much. Bye everyone.

Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple podcasts, Spotify or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lenny's podcast dot com. See you in the next episode.

---

---

### Block 27

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter.

**Mapping:** score=0.61 reason=keyword:what is|head='What is product experimentation? How to build, test, and scale smarter.'

[A/B testing](https://mixpanel.com/blog/tag/a-b-testing)

[feature flags](https://mixpanel.com/blog/tag/feature-flags)

[product experimentation](https://mixpanel.com/blog/tag/product-experimentation)

[user research](https://mixpanel.com/blog/tag/user-research)

* 

Product experimentation is the structured process of testing new ideas, features, or changes in a controlled way to measure their impact on user behavior and key metrics. It’s how product managers, growth marketers, and engineers validate decisions with data before committing to a full rollout. Product experimentation techniques include A/B tests, multivariate tests, feature flags, phased rollouts, and even pricing tests.

When was the last time you had a product idea that felt right, but left you wondering whether it would actually move the needle?

That’s where product experimentation comes in. It’s how today’s most successful product teams test ideas, learn fast, and build smarter. From [A/B tests](https://mixpanel.com/blog/what-is-ab-testing/) to feature flag rollouts, experimentation helps you minimize risk while maximizing insight.

But to get the most from your product experiments, you need more than just a hunch and a toggle switch. You need a repeatable process, the right tools, and clear ways to measure success (or failure).

Today, we’ll walk through what product experimentation means, how to run better tests, and tools that will help you close the loop faster.

---

### Block 28

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > What is product experimentation?

**Mapping:** score=0.61 reason=keyword:what is|head='What is product experimentation?'

Product experimentation is the structured process of testing new ideas, features, or changes in a controlled way to measure their impact on user behavior and key metrics. It’s how product managers, growth marketers, and engineers validate decisions with data before committing to a full rollout.

Typically, product experimentation is:

* Hypothesis-driven: You start with an idea you want to prove or disprove

* Data-informed: You collect data before, during, and after to measure success

* Iterative: You learn and adapt, even when experiments “fail”

---


