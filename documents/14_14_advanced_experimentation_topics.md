## 14. Advanced Experimentation Topics

### Block 1

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 14. Advanced Experimentation Topics > 14.2 Specialized Designs

**Mapping:** score=0.61 reason=keyword:switchback|head='14.2 Specialized Designs'

#### 14.2.1 Crossover Designs
#### 14.2.2 Switchback Experiments
#### 14.2.3 Time-Based Experiments
#### 14.2.4 Latin Square Designs
#### 14.2.5 Interleaving (Search/Ranking)

---

### Block 2

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 22. Tools & Technology Ecosystem > 22.1 Experimentation Platforms

**Mapping:** score=0.646 reason=heading_fuzzy|head='22.1 Experimentation Platforms'

#### 22.1.1 End-to-End Platforms
#### 22.1.2 Feature Flag Systems
#### 22.1.3 Assignment Services

---

### Block 3

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Product & Marketing Context > **1\. Product-Led Experimentation**

**Mapping:** score=0.657 reason=heading_fuzzy|head='**1\. Product-Led Experimentation**'

* **Goal:** Improve the user experience to drive long-term value.  
* **Frameworks:**  
  * **Jobs-to-be-Done (JTBD):** What "job" is a user hiring Airbnb to do? Test changes that help them do that job better.  
    * *Case: Search & Discovery.* A user's "job" is to find the perfect place to stay. You could A/B test:  
      * **Variant A:** Current search results.  
      * **Variant B:** A new ranking algorithm that prioritizes listings with high-quality photos and recent 5-star reviews.  
      * **Primary Metric:** Conversion from search to booking.  
  * **Funnel Optimization:** Identify drop-off points in the user journey and test solutions.  
    * *Case: Booking Funnel.* You see a drop-off on the payment page.  
      * **Hypothesis:** "Simplifying the payment form by removing non-essential fields will reduce friction and increase checkout completion."  
      * **Test:** A/B test the simplified form.

---

### Block 4

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Business Objectives > Common Experimentation Goals

**Mapping:** score=0.635 reason=heading_fuzzy|head='Common Experimentation Goals'

- Conversion rate improvement  
- Customer acquisition cost reduction  
- Lifetime value increase  
- Engagement metrics optimization  
- Retention improvement  
- Brand awareness enhancement

**Example:** Increase merchant checkout conversion rate from 3.2% to 3.8%

---

### Block 5

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 9\. Tools & Technology Stack > 9.1 Experimentation Platforms

**Mapping:** score=0.656 reason=heading_fuzzy|head='9.1 Experimentation Platforms'

| Platform Type | Options | Key Features | Best For |
| :---- | :---- | :---- | :---- |
| **Commercial Platforms** | • Optimizely • Adobe Target • Google Optimize • VWO | • Visual editors • Built-in stats • Integrations | Marketing teams, quick starts |
| **Developer Focused** | • LaunchDarkly • Split.io • Statsig • Eppo | • Feature flags • SDKs • API-first | Engineering-led experimentation |
| **Analytics Integrated** | • Amplitude Experiment • Mixpanel • Heap | • Unified data • User journey • Cohort analysis | Product analytics teams |
| **Open Source** | • GrowthBook • Wasabi • PlanOut • Unleash | • Customizable • Self-hosted • Cost-effective | Teams with engineering resources |
| **Custom Built** | • Internal platforms • Microservices | • Full control • Tailored needs | Large organizations |

---

### Block 6

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Experiment Target Types & Examples > Stage 2: Experiment Types & Frameworks

**Mapping:** score=0.61 reason=keyword:interrupted time|head='Stage 2: Experiment Types & Frameworks'

| Type | Description | Example at Affirm |
| :---- | :---- | :---- |
| **A/B Testing** | Two-group comparison (control vs. treatment) | Test a redesigned email to convert pre-approved users |
| **Multivariate Testing** | Tests multiple variables at once | Test CTA color \+ headline \+ loan term placement |
| **Multi-Armed Bandit** | Allocates more traffic to better-performing variants in real-time | Optimize promo banner variants on merchant sites |
| **Holdout Testing** | Hold out a random group to assess true lift | Measure long-term impact of offering Affirm at checkout |
| **Interrupted Time Series (ITS)** | Track outcomes before & after intervention | New underwriting model rollout |

---

### Block 7

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Advanced Approaches > Causal Inference Models

**Mapping:** score=0.61 reason=keyword:propensity score|head='Causal Inference Models'

- **Propensity score matching** for quasi-experiments  
- **Diff-in-diff** when rollout cannot be randomized

---

### Block 8

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 5\. Advanced Topics in Experimentation > **5.2. Causal Inference & Quasi-Experiments**

**Mapping:** score=0.61 reason=keyword:difference-in-differences|head='**5.2. Causal Inference & Quasi-Experiments**'

* Difference-in-Differences

* Propensity Score Matching

* Instrumental Variables

---

### Block 9

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Next-Level A/B Testing: Repeatable, Rapid, and Flexible Product Experimentation > In-Depth Summary of Key Topics > **Chapter 4: Improving Machine Learning Evaluation Practices**

**Mapping:** score=0.61 reason=keyword:interleaving|head='**Chapter 4: Improving Machine Learning Evaluation Practices**'

This chapter addresses the unique challenges of testing machine learning models.

• Offline Evaluations: Before running a live A/B test, models should be evaluated offline using historical data and metrics like precision, recall, and NDCG. This helps filter out underperforming model variants, reducing the number of variants needed for online testing and saving resources.

• Multi-Armed Bandits (MAB): An adaptive strategy that balances exploration (testing different variants or "arms") and exploitation (directing more users to the best-performing arm to maximize a reward). This can be more efficient than a traditional A/B test where a suboptimal variant receives traffic for the entire duration.

• Interleaving: A highly sensitive method for comparing multiple ranking algorithms. Instead of splitting users between rankers, it creates a single "blended" list of results from all rankers and presents it to users. User clicks on items from a specific ranker indicate a preference. This requires fewer users than a standard A/B/n test but is best suited for feature-level metrics.

---


