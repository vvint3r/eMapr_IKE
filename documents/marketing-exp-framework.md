# Marketing Experimentation Framework

## Business Objectives

### Common Experimentation Goals
- Conversion rate improvement
- Customer acquisition cost reduction
- Lifetime value increase
- Engagement metrics optimization
- Retention improvement
- Brand awareness enhancement

**Example:** Increase merchant checkout conversion rate from 3.2% to 3.8%

### Success Metrics Framework

**Primary Metrics (North Star)**
- Key business outcome metrics
- Example: Checkout conversion rate

**Secondary Metrics**
- Supporting indicators
- Example: Average order value

**Guardrail Metrics**
- Must-not-worsen metrics
- Example: Customer complaints

**Counter Metrics**
- Potential negative impacts

**Leading Indicators**
- Early signals of success

**Lagging Indicators**
- Long-term outcome measures

---

## Hypothesis Frameworks

### If-Then-Because Format
"If we reduce the number of form fields from 8 to 4, then checkout conversion will increase by 20%, because users abandon due to friction"

### Other Formats
- **Problem-Solution-Result**: Define problem → propose solution → expected result
- **Jobs-to-be-Done**: Focus on user need fulfillment
- **Lean Hypothesis**: Rapid testing framework
- **Scientific Method**: Formal hypothesis testing

---

## 1. Experiment Type Selection

| Experiment Type | Use Cases | Complexity | Affirm Example |
|----------------|-----------|------------|----------------|
| **A/B Testing** | • Single variable change<br>• Clear binary choices<br>• Simple implementation | Low | Testing two checkout button colors |
| **A/B/n Testing** | • Multiple variants<br>• Exploring optimization curve<br>• Finding local maxima | Medium | Testing 5 different payment plan displays |
| **Multivariate Testing (MVT)** | • Multiple variables simultaneously<br>• Interaction effects<br>• Complex UX changes | High | Testing button color × copy × position |
| **Multi-Armed Bandit** | • Dynamic allocation<br>• Minimize opportunity cost<br>• Continuous optimization | High | Optimizing interest rate offers in real-time |
| **Factorial Design** | • Full factorial (all combinations)<br>• Fractional factorial<br>• Systematic interaction study | Very High | Testing all combinations of 4 factors |
| **Sequential Testing** | • Early stopping rules<br>• Adaptive designs<br>• Resource optimization | High | Stopping test early if clear winner emerges |
| **Switchback Testing** | • Time-based allocation<br>• Network effects<br>• Market-level changes | Medium | Testing new merchant onboarding flow |
| **Synthetic Control** | • No randomization possible<br>• Market-level rollouts<br>• Causal inference | Very High | Launching in new geographic market |

---

## 2. Statistical Framework & Power Analysis

### 2.1 Statistical Test Selection

| Test Type | Use Case | Key Assumptions | Affirm Example |
|-----------|----------|-----------------|----------------|
| **Z-Test** | • Large samples (n>30)<br>• Known population variance<br>• Normal distribution | • Independence<br>• Normality<br>• Equal variance | Comparing conversion rates with 100k+ users |
| **T-Test (Student's)** | • Small samples<br>• Unknown variance<br>• Continuous outcomes | • Independence<br>• Normality<br>• Equal variance | Comparing average order values |
| **Welch's T-Test** | • Unequal variances<br>• Different sample sizes | • Independence<br>• Normality | Comparing segments with different sizes |
| **Mann-Whitney U** | • Non-parametric<br>• Ordinal data<br>• Non-normal distribution | • Independence<br>• Ordinal scale | Comparing user satisfaction scores |
| **Chi-Square Test** | • Categorical outcomes<br>• Independence testing | • Expected frequency >5<br>• Independence | Testing payment method preferences |
| **Fisher's Exact Test** | • Small sample sizes<br>• 2x2 contingency tables | • Independence | Rare event analysis (fraud rates) |
| **Kolmogorov-Smirnov** | • Distribution comparison<br>• Continuous data | • Independence<br>• Continuous scale | Comparing entire distributions of loan amounts |
| **Bootstrap Methods** | • No distribution assumptions<br>• Complex statistics | • Independence | Confidence intervals for median time to repayment |
| **Bayesian Methods** | • Prior information<br>• Sequential analysis<br>• Posterior probabilities | • Prior specification | Updating conversion rate beliefs with new data |
| **CUPED/CUPAC** | • Variance reduction<br>• Pre-experiment data | • Covariate stability | Using historical purchase data to reduce variance |

### 2.2 Sample Size Calculation Methods

| Method | Formula/Approach | When to Use | Affirm Example |
|--------|------------------|-------------|----------------|
| **Classical Power Analysis** | n = 2σ²(Z_α/2 + Z_β)²/δ² | Standard A/B tests | 15,000 users per variant for 80% power |
| **Minimum Detectable Effect** | MDE = (Z_α/2 + Z_β)√(2σ²/n) | Fixed sample constraint | Can detect 0.5% lift with current traffic |
| **Sequential Analysis** | Alpha spending functions | Continuous monitoring | Check results daily with adjusted p-values |
| **Bayesian Sample Size** | Posterior probability thresholds | Prior information available | 95% probability variant is 2% better |
| **Simulation-Based** | Monte Carlo methods | Complex designs | Simulate 10,000 experiments |
| **Adaptive Designs** | Information-based stopping | Efficient resource use | Stop when confidence interval < 0.1% |

---

## 3. Experiment Design & Implementation

### 3.1 Randomization Strategies

| Strategy | Implementation | Pros/Cons | Affirm Use Case |
|----------|---------------|-----------|-----------------|
| **Simple Random** | Random number generator | Pro: Unbiased<br>Con: Imbalanced groups | Basic feature tests |
| **Block Randomization** | Randomize within blocks | Pro: Balance covariates<br>Con: Complex | Balance by merchant type |
| **Stratified Random** | Random within strata | Pro: Representative<br>Con: Need strata info | Ensure all credit tiers represented |
| **Cluster Randomization** | Randomize groups | Pro: Avoid contamination<br>Con: Less power | Randomize by merchant |
| **Matched Pairs** | Match then randomize | Pro: Increased power<br>Con: Matching complexity | Match users by purchase history |
| **Hash-Based** | Deterministic hashing | Pro: Consistent<br>Con: Predictable | User ID % 100 < 50 |
| **Time-Based** | Temporal allocation | Pro: Simple<br>Con: Time confounds | Day-of-week randomization |
| **Geo-Based** | Geographic clustering | Pro: Market-level<br>Con: Spillover effects | Test in specific states |

### 3.2 Implementation Frameworks

| Framework | Architecture | Use Case | Affirm Implementation |
|-----------|-------------|----------|----------------------|
| **Feature Flags** | • LaunchDarkly<br>• Optimizely<br>• Split.io<br>• Custom flags | Real-time control | Toggle checkout flow variants |
| **Server-Side Testing** | • Backend randomization<br>• API-driven<br>• Database flags | Sensitive features | Payment terms calculation |
| **Client-Side Testing** | • JavaScript-based<br>• Google Optimize<br>• VWO | UI/UX changes | Button color testing |
| **Edge Computing** | • CDN-level<br>• Cloudflare Workers<br>• Lambda@Edge | Low latency | Personalized landing pages |
| **Mobile SDKs** | • Firebase A/B<br>• Apptimize<br>• Custom SDKs | App experiments | Mobile app checkout flow |
| **Full-Stack Platforms** | • Amplitude Experiment<br>• Statsig<br>• Eppo | End-to-end solution | Integrated testing platform |

---

## 4. Monitoring & Quality Assurance

### 4.1 Pre-Launch Checks

| Check Type | Methods | Critical Metrics | Affirm Example |
|------------|---------|-----------------|----------------|
| **AA Testing** | Run control vs control | • Type I error rate<br>• Randomization balance | 5% false positive rate confirmed |
| **Sample Ratio Mismatch** | Chi-square test on assignment | • Expected vs actual ratio<br>• P-value < 0.001 flags issue | 50.1% vs 49.9% (acceptable) |
| **Covariate Balance** | • T-tests on features<br>• Standardized differences | • Age, income, credit score<br>• <0.1 std dev difference | All user attributes balanced |
| **Technical Validation** | • Logging verification<br>• Event tracking<br>• Edge cases | • 100% event capture<br>• No data loss | All checkout events tracked |
| **Canary Deployment** | Gradual rollout | • Error rates<br>• Performance metrics | 1% → 5% → 25% → 50% |

### 4.2 Runtime Monitoring

| Monitoring Type | Tools/Methods | Alert Thresholds | Response Plan |
|----------------|---------------|------------------|---------------|
| **Statistical Significance** | • Sequential testing<br>• P-value tracking<br>• Confidence intervals | • Alpha spending<br>• Adjusted p-values | Daily significance checks |
| **Practical Significance** | • Effect size monitoring<br>• Business impact | • Minimum meaningful difference<br>• ROI thresholds | Alert if effect < 1% |
| **Data Quality** | • Missing data rates<br>• Outlier detection<br>• Event validation | • >5% missing data<br>• Impossible values | Automated data quality reports |
| **System Health** | • Latency monitoring<br>• Error rates<br>• Resource usage | • P95 latency >2s<br>• Error rate >0.1% | PagerDuty alerts |
| **Sample Size Tracking** | • Daily accumulation<br>• Projection models | • Behind schedule<br>• Imbalanced exposure | Traffic allocation adjustment |

---

## 5. Analysis Methods & Techniques

### 5.1 Primary Analysis Approaches

| Method | Statistical Technique | Implementation | Affirm Example |
|--------|----------------------|----------------|----------------|
| **Frequentist Analysis** | • Hypothesis testing<br>• Confidence intervals<br>• P-values | • Python statsmodels<br>• R stats package | t-test on conversion rates |
| **Bayesian Analysis** | • Posterior distributions<br>• Credible intervals<br>• Bayes factors | • PyMC3<br>• Stan<br>• JAGS | P(variant > control) = 0.97 |
| **Regression Adjustment** | • ANCOVA<br>• Linear models<br>• Propensity scores | • Include covariates<br>• Reduce variance | Adjust for user credit score |
| **Machine Learning** | • Causal forests<br>• Double ML<br>• Targeted learning | • CausalML<br>• EconML | Heterogeneous treatment effects |
| **Time Series** | • Interrupted time series<br>• ARIMA models<br>• State space models | • Seasonal adjustment<br>• Trend analysis | Account for holiday effects |
| **Survival Analysis** | • Kaplan-Meier<br>• Cox regression<br>• AFT models | • Time to event<br>• Censoring | Time to first purchase |

### 5.2 Advanced Techniques

| Technique | Purpose | Complexity | When to Use |
|-----------|---------|------------|-------------|
| **CUPED** | Variance reduction using pre-data | Medium | 30-50% variance reduction possible |
| **Difference in Differences** | Control for time trends | Medium | Rollout experiments |
| **Instrumental Variables** | Handle non-compliance | High | Users don't see assigned variant |
| **Synthetic Control Method** | Create counterfactual | High | Single unit treatment (new market) |
| **Regression Discontinuity** | Exploit thresholds | High | Credit score cutoffs |
| **Quantile Treatment Effects** | Distribution impacts | Medium | Effect varies by user segment |
| **Meta-Analysis** | Combine multiple experiments | Medium | Synthesize learning across tests |
| **Heterogeneous Effects** | • Subgroup analysis<br>• Interaction terms<br>• ML methods | High | Personalization opportunities |

---

## 6. Results Interpretation & Decision Making

### 6.1 Statistical Interpretation Framework

| Aspect | Considerations | Best Practices | Common Pitfalls |
|--------|---------------|----------------|-----------------|
| **Effect Size** | • Practical vs statistical significance<br>• Confidence intervals<br>• Standardized effects | Report both absolute and relative | Focusing only on p-values |
| **Multiple Testing** | • Bonferroni correction<br>• FDR control<br>• Hierarchical testing | Pre-specify primary metric | P-hacking with many metrics |
| **Segment Analysis** | • Pre-specified vs exploratory<br>• Interaction tests<br>• Multiple comparison adjustment | Register segments before | HARKing (post-hoc storytelling) |
| **Long-term Effects** | • Novelty effects<br>• Learning curves<br>• Seasonality | Run for full business cycle | Stopping too early |
| **External Validity** | • Generalizability<br>• Population differences<br>• Context changes | Document assumptions | Over-generalizing results |

### 6.2 Decision Frameworks

| Framework | Decision Rule | Risk Consideration | Affirm Example |
|-----------|--------------|-------------------|----------------|
| **Hypothesis Testing** | Reject if p < α | Type I/II errors | Ship if p < 0.05 |
| **Bayesian Decision** | Max expected utility | Loss function | Ship if P(lift>0) > 0.95 |
| **Risk-Adjusted** | Consider downside | Worst-case scenario | Ship if worst case > -0.5% |
| **Portfolio Approach** | Optimize across tests | Resource allocation | Fund top 20% of ideas |
| **Sequential Decision** | Continue/stop rules | Opportunity cost | Stop if futility boundary crossed |
| **Multi-Stakeholder** | Weighted objectives | Stakeholder alignment | Product + Risk + Legal approval |

---

## 7. Post-Experiment Actions

### 7.1 Implementation Strategies

| Strategy | Approach | Risk Mitigation | Timeline |
|----------|---------|-----------------|----------|
| **Full Rollout** | 100% immediate | Monitor closely | 1 day |
| **Gradual Rollout** | 50% → 75% → 100% | Staged validation | 2 weeks |
| **Holdout Groups** | Keep 5-10% control | Long-term measurement | Ongoing |
| **Regional Rollout** | Geography-based | Market differences | 1 month |
| **Segment-Based** | High-value users first | Protect core base | 3 weeks |
| **Feature Flags** | Instant rollback capability | Quick reversion | Immediate |

### 7.2 Knowledge Management

| Component | Methods | Tools | Deliverables |
|-----------|---------|-------|--------------|
| **Documentation** | • Experiment briefs<br>• Analysis notebooks<br>• Decision logs | • Confluence<br>• GitHub<br>• Notion | Experiment report template |
| **Knowledge Sharing** | • Review meetings<br>• Wiki updates<br>• Lunch & learns | • Slack channels<br>• Email digests | Weekly experiment review |
| **Meta-Learning** | • Cross-experiment analysis<br>• Pattern recognition<br>• Failure analysis | • DataBricks<br>• Tableau<br>• Python notebooks | Quarterly insights report |
| **Process Improvement** | • Retrospectives<br>• Efficiency metrics<br>• Tool evaluation | • JIRA<br>• Asana<br>• Linear | Monthly process review |

---

## 8. Advanced Topics & Considerations

### 8.1 Network Effects & Interference

| Type | Detection Method | Mitigation | Affirm Example |
|------|-----------------|------------|----------------|
| **Direct Network Effects** | • Cluster randomization<br>• SUTVA violations | • Market-level randomization<br>• Synthetic control | Merchant referral programs |
| **Indirect Effects** | • Spillover analysis<br>• Spatial models | • Buffer zones<br>• Cluster designs | User word-of-mouth |
| **Competitive Effects** | • Game theory models<br>• Market share analysis | • Simultaneous moves<br>• Strategic timing | Competitor response to pricing |
| **Platform Effects** | • Two-sided markets<br>• Feedback loops | • Careful measurement<br>• Dynamic models | Merchant-consumer interactions |

### 8.2 Ethical Considerations

| Aspect | Guidelines | Implementation | Example |
|--------|-----------|----------------|---------|
| **Fairness** | • Equal treatment<br>• No discrimination | • Bias testing<br>• Fairness metrics | Equal approval rates across demographics |
| **Transparency** | • User notification<br>• Opt-out options | • Privacy policy<br>• Clear communication | "You're seeing a new checkout experience" |
| **Risk Management** | • Minimize harm<br>• Protect vulnerable users | • Guardrail metrics<br>• Safety protocols | Don't test on high-risk loan applicants |
| **Data Privacy** | • GDPR compliance<br>• Data minimization | • Anonymization<br>• Retention policies | Hash PII, delete after analysis |

---

## 9. Tools & Technology Stack

### 9.1 Experimentation Platforms

| Platform Type | Options | Key Features | Best For |
|--------------|---------|--------------|----------|
| **Commercial Platforms** | • Optimizely<br>• Adobe Target<br>• Google Optimize<br>• VWO | • Visual editors<br>• Built-in stats<br>• Integrations | Marketing teams, quick starts |
| **Developer Focused** | • LaunchDarkly<br>• Split.io<br>• Statsig<br>• Eppo | • Feature flags<br>• SDKs<br>• API-first | Engineering-led experimentation |
| **Analytics Integrated** | • Amplitude Experiment<br>• Mixpanel<br>• Heap | • Unified data<br>• User journey<br>• Cohort analysis | Product analytics teams |
| **Open Source** | • GrowthBook<br>• Wasabi<br>• PlanOut<br>• Unleash | • Customizable<br>• Self-hosted<br>• Cost-effective | Teams with engineering resources |
| **Custom Built** | • Internal platforms<br>• Microservices | • Full control<br>• Tailored needs | Large organizations |

### 9.2 Analysis Tools

| Tool Category | Options | Use Case | Integration |
|--------------|---------|----------|-------------|
| **Statistical Software** | • R + tidyverse<br>• Python (scipy, statsmodels)<br>• SAS<br>• SPSS | Complex analysis | Data pipelines |
| **Notebooks** | • Jupyter<br>• RStudio<br>• Databricks<br>• Google Colab | Exploratory analysis | Version control |
| **BI Tools** | • Tableau<br>• Looker<br>• PowerBI<br>• Sisense | Dashboards | Real-time monitoring |
| **Data Processing** | • Spark<br>• Presto<br>• BigQuery<br>• Snowflake | Large-scale processing | ETL pipelines |
| **Workflow Management** | • Airflow<br>• Prefect<br>• Dagster<br>• Luigi | Automation | Scheduled analysis |

---

## 10. Example End-to-End Experiment: Affirm Checkout Optimization

### Stage 1: Planning
**Hypothesis:** Reducing checkout steps from 5 to 3 will increase conversion by 25%

**Metrics:**
- Primary: Conversion rate
- Secondary: Time to complete
- Guardrail: Error rate

**Sample Size:** 50,000 users per variant (α=0.05, β=0.20, MDE=2%)

### Stage 2: Design
**Type:** A/B test with 50/50 split

**Randomization:** Hash-based on user ID

**Duration:** 3 weeks (full purchase cycle)

### Stage 3: Implementation
**Platform:** Internal feature flag system

**Monitoring:** Real-time dashboard in Looker

**Quality Checks:** AA test passed, SRM check daily

### Stage 4: Analysis
**Method:** Two-proportion z-test with CUPED

**Results:** 23% lift (95% CI: 18%-28%), p < 0.001

**Segments:** Larger effect for mobile users (28% vs 19%)

### Stage 5: Decision
**Recommendation:** Ship to 100% with 1-week staged rollout

**Holdout:** 5% control for long-term monitoring

**Next Steps:** Explore further optimization for desktop experience

### Stage 6: Learning
**Insight:** Form simplification has diminishing returns after 3 fields

**Future Tests:** Focus on mobile-first design

**Process Improvement:** Implement automatic SRM alerts

---

## Experiment Process Framework

### Setup & Implementation Stages

| Stage | Process Point | Stage Purpose |
|-------|--------------|---------------|
| **Stage 1** | Objective | Specific area of improvement being targeted |
| **Stage 2** | Background | Context and status quo summary |
| **Stage 3** | Hypothesis | Estimated outcome and improvements expected |
| **Stage 4** | Test Design | Provide implementation details [control/variant] |
| **Stage 5** | Metrics | Provide measurement targets [primary/secondary & guardrail] |
| **Stage 6** | Implementation Specifics | Details on targeting, samples, randomization, etc. |
| **Stage 7** | Track & Report | Measuring results for statistical significance for control/variant |

---

## Experiment Target Types & Examples

### Stage 1: Experiment Objectives

| Target Type | Experiment Sample Targeting |
|------------|----------------------------|
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
| **Fraud Prevention and Risk Modeling** | Test identity verification steps (e.g., selfie + ID match) for new users vs. relaxed flow on drop-off rate |
| **Merchant Widget Optimization** | A/B test embedded monthly installment calculator on merchant PDPs vs. static monthly pricing copy |
| **Product Feature Adoption** | Test exposure to BNPL explainer video vs. static FAQ on user education and engagement |
| **Personalization / Segmentation** | Test personalized financing term recommendations (based on user profile) vs. default offer to improve uptake |
| **Nudges & Behavioral Design** | Test adding scarcity language ("Last chance for 0% financing!") in email footers to improve click-to-apply rate |
| **App vs. Web Performance** | Test identical email-to-checkout journeys routed to mobile app vs. mobile web to measure channel conversion lift |
| **Trust Signal Placement** | Test positioning of FDIC insurance badge and data privacy seals during financing to increase user confidence |
| **Checkout Form Field Order** | Test alternative sequences of form fields (e.g., income → employment vs. employment → income) to reduce friction |
| **Incentive Testing** | Test $10 Affirm credit vs. no credit for completing onboarding to increase loan origination volume |

### Stage 2: Experiment Types & Frameworks

| Type | Description | Example at Affirm |
|------|-------------|------------------|
| **A/B Testing** | Two-group comparison (control vs. treatment) | Test a redesigned email to convert pre-approved users |
| **Multivariate Testing** | Tests multiple variables at once | Test CTA color + headline + loan term placement |
| **Multi-Armed Bandit** | Allocates more traffic to better-performing variants in real-time | Optimize promo banner variants on merchant sites |
| **Holdout Testing** | Hold out a random group to assess true lift | Measure long-term impact of offering Affirm at checkout |
| **Interrupted Time Series (ITS)** | Track outcomes before & after intervention | New underwriting model rollout |

---

## Detailed Experiment Design Guide

### 3. Hypothesis Structure (Using PICO)

- **Population:** All users entering Affirm's financing funnel
- **Intervention:** New email design for pre-qualified users
- **Control:** Original email design
- **Outcome:** Increase in CTR and loan completions

**Example:**
"Among prequalified users (P), if we redesign the email layout (I) compared to the current template (C), we expect a 15% increase in CTR and 10% lift in loan conversion (O)."

### 4. Defining Metrics

| Metric Type | Examples at Affirm |
|------------|-------------------|
| **Primary Metric** | CTR, conversion to loan approval |
| **Secondary Metric** | Loan size, NPS, time-to-completion |
| **Guardrail Metric** | Email unsubscribes, bounce rates, fraud rates |

---

## Statistical Planning

### Sample Size Calculation

Based on:
- Baseline rate (e.g., 10% CTR)
- Minimum detectable effect (MDE) (e.g., 1.5%)
- Power (commonly 80%)
- Significance level (alpha = 0.05)

**Formula for two-proportion z-test:**
n = 2 × (Z_α/2 + Z_β)² × p̄(1-p̄) / (Δ)²

### Randomization Approach
- **Stratified randomization** to control for high-variance features (e.g., mobile vs desktop, merchant category)
- Example: Users from travel merchants vs. retail merchants might behave differently

### Avoiding Biases
- Simultaneous deployment to avoid seasonality
- Bot filtering via fingerprinting or behavioral filters
- Cookie-based bucketing for web users

---

## Execution Tools

**Experimentation Platform:** WebLab or internal experimentation engine

**Event Tracking:** Segment + Redshift or Snowflake

**Statistical Libraries:** SciPy, Statsmodels, or internal ML/stat toolkits

### Example: A/B Test – Prequalification Page Redesign
- **Control:** Existing layout
- **Variant:** Cleaner layout with "instant financing" badge
- **Primary Metric:** Prequal submission rate
- **Execution Period:** 3 weeks
- **Target Users:** Logged-in users from high-traffic merchant pages

---

## Statistical Analysis & Models

### Frequentist Methods
- **t-test** for means (e.g., loan size)
- **z-test** for proportions (e.g., CTR)
- **Chi-square test** for categorical outcomes

### Bayesian Inference
- For continuous monitoring (i.e., decision-making mid-test)
- Gives a probability that variant is better, rather than p-value

### Regression Models
**Logistic regression to control for covariates:**
Conversion ~ Treatment + Device + Merchant_Category + Time_of_Day

**Uplift modeling:** Estimate individual treatment effects (ITE)

---

## Result Interpretation Example

| Metric | Control | Variant | Lift | p-value |
|--------|---------|---------|------|---------|
| CTR | 10.2% | 11.7% | +14.7% | 0.03 |
| Prequal Completion | 7.8% | 8.1% | +3.8% | 0.21 |
| Loan Approval Rate | 4.5% | 5.2% | +15.6% | 0.04 |

**Key Takeaways:**
- Statistically significant metrics (p < 0.05)
- Non-significant result still useful for directional learning

---

## Post-Test Actions

### Rollout Criteria
- Effect is statistically significant
- Lift meets or exceeds MDE
- No negative movement in guardrail metrics

### Segmented Insights
- Segment performance by device, channel, user cohort, merchant vertical
- Use for personalized future experiments

### Documentation
- Maintain a centralized experiment wiki (Notion, Confluence)
- Include: Hypothesis, design, metrics, results, learnings

---

## Common Pitfalls & Solutions

| Issue | Solution |
|-------|----------|
| **Peeking (early stopping)** | Use fixed sample or Bayesian stopping rules |
| **Metric variance too high** | Use log transformation or median |
| **Winner's curse** | Re-test before full rollout |
| **Low power** | Increase duration or sample size |
| **Overlapping experiments** | Use mutual exclusivity buckets |

---

## Advanced Approaches

### CUPED (Controlled Pre-experiment Data)
Reduces variance using pre-experiment behavior as a covariate

### Causal Inference Models
- **Propensity score matching** for quasi-experiments
- **Diff-in-diff** when rollout cannot be randomized

### Sequential Testing
Continuous monitoring with adjusted error rates (e.g., SPRT)

### Uplift Modeling
- Estimate which users respond best to the treatment
- Used in retention/upsell experiments