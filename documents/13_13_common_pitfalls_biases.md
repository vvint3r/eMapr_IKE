## 13. Common Pitfalls & Biases

### Block 1

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 13. Common Pitfalls & Biases > 13.3 Temporal & Environmental Biases

**Mapping:** score=0.61 reason=keyword:novelty|head='13.3 Temporal & Environmental Biases'

#### 13.3.1 Novelty Effect
#### 13.3.2 Maturation Effects
#### 13.3.3 Carryover Effects
#### 13.3.4 Seasonality
#### 13.3.5 S-curve Dynamics

---

### Block 2

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 13. Common Pitfalls & Biases > 13.4 Assignment & Selection Biases

**Mapping:** score=0.61 reason=keyword:selection bias|head='13.4 Assignment & Selection Biases'

#### 13.4.1 Selection Bias
#### 13.4.2 Survivorship Bias
#### 13.4.3 Argument from Coincidence

---

### Block 3

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 13. Common Pitfalls & Biases > 13.5 Interference & Spillover

**Mapping:** score=0.61 reason=keyword:network effects|head='13.5 Interference & Spillover'

#### 13.5.1 Network Effects
#### 13.5.2 Spillover & Contamination
#### 13.5.3 SUTVA Violations
#### 13.5.4 Dealing with Network Effects

---

### Block 4

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 14. Advanced Experimentation Topics > 14.3 Long-Term Effect Measurement

**Mapping:** score=0.61 reason=keyword:novelty|head='14.3 Long-Term Effect Measurement'

#### 14.3.1 Novelty Effect Detection
#### 14.3.2 Long-Term Holdouts
#### 14.3.3 Cohort Analysis
#### 14.3.4 Long-Term Monitoring
#### 14.3.5 Learning Effects

---

### Block 5

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 19. Privacy, Ethics & Compliance > 19.4 Bias & Fairness

**Mapping:** score=0.61 reason=keyword:selection bias|head='19.4 Bias & Fairness'

#### 19.4.1 Selection Bias
#### 19.4.2 Algorithmic Fairness
#### 19.4.3 Inclusive Design Testing

---

### Block 6

**Source:** `md`  
**Original headings:** Marketing Experimentation > Airbnb-Specific Cases & Interview Prep > **Airbnb's Specific Testing Culture & Nuances**

**Mapping:** score=0.61 reason=keyword:network effects|head='**Airbnb's Specific Testing Culture & Nuances**'

* **Network Effects:** A change for guests can affect hosts, and vice-versa. You must always consider the other side of the marketplace.  
* **Global Heterogeneity:** An experiment that works in North America might fail in APAC. You must segment results by region, user tenure, device type, etc.  
* **Long-Term vs. Short-Term:** Some features might have a short-term negative but a long-term positive (e.g., a stricter cancellation policy might reduce initial bookings but increase host supply, improving the marketplace long-term). Airbnb uses **"Holdback" groups** (a small % of the treatment group that never gets the winning variant) to measure long-term impact.

---

### Block 7

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Common Pitfalls & Solutions

**Mapping:** score=0.727 reason=heading_fuzzy|head='Common Pitfalls & Solutions'

| Issue | Solution |
| :---- | :---- |
| **Peeking (early stopping)** | Use fixed sample or Bayesian stopping rules |
| **Metric variance too high** | Use log transformation or median |
| **Winner's curse** | Re-test before full rollout |
| **Low power** | Increase duration or sample size |
| **Overlapping experiments** | Use mutual exclusivity buckets |

---

### Block 8

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 3\. Measurement & Statistical Rigor > **3.3. Validity & Pitfalls**

**Mapping:** score=0.61 reason=keyword:p-hacking|head='**3.3. Validity & Pitfalls**'

* Sample Size Too Small → Underpowered

* Multiple Testing / P-hacking → False positives

* Selection Bias

* Seasonality / External Interference

* Winner’s Curse (first results overestimate impact)


Analogy: Statistical testing is like using a radar to detect ships in fog. If your radar is too weak (low power), you miss ships (effects). But if it's too sensitive, it sees ghosts (false positives).

---

### Block 9

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 5\. Advanced Topics in Experimentation > **5.4. Cross-Channel & Long-Term Effects**

**Mapping:** score=0.61 reason=keyword:spillover|head='**5.4. Cross-Channel & Long-Term Effects**'

* Incrementality across marketing channels.

* Halo effects, spillovers.

* Decay curves and lagged impact analysis.

Analogy: Advanced experimentation is like managing a clinical drug trial with multiple treatments, delayed reactions, and side effects — you need not just data, but disciplined modeling to know what really helped and for whom.

---

### Block 10

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Structured Learning Sequence for Marketing Experimentation \[Continued\] > 6\) Selection bias — what it is and how it bites

**Mapping:** score=0.61 reason=keyword:selection bias|head='6\) Selection bias — what it is and how it bites'

Definition: Systematic differences between treated and control not due to treatment, causing biased estimates.

Airbnb example 1 (opt-in bias):  
 If hosts opt-in to a “Super-Photography” program and you compare their bookings vs. non-opt-ins, you’ll overstate impact because opt-ins likely have higher motivation/quality. RCT or propensity score methods can mitigate.

Airbnb example 2 (retargeting bias):  
 Users who see retargeting ads are self-selected (they already showed interest), so naive “exposed vs. unexposed” comparisons inflate impact. Use randomized holdouts, ghost ads, or instrumental variables (bid shocks) to restore causal identification.

---

### Block 11

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Threats to experiment validity

**Mapping:** score=0.61 reason=keyword:novelty|head='Threats to experiment validity'

![Image by Author][image14]Image by Author

22. Novelty Effect – "Sometimes there’s a "novelty effect" at work. Any change you make to your website will cause your existing user base to pay more attention. Changing that big call-to-action button on your site from green to orange will make returning visitors more likely to see it, if only because they had tuned it out previously. This type of effect is not likely to last in the long run – but it can artificially impact your test results.

23. Primacy effect – When there’s a change in the product, people react to it differently. Some users may be used to the way a product works and are reluctant to change. This is called primacy effect. The primacy effect is nothing but the tendency to remember the first piece of information we encounter better than information presented later on. This can be thought of as an opposite phenomenon to novelty effect.

24. Seasonality – Businesses may have different user behavior say on 1st of a month and 15th of a month. For some eCommerce sites, their traffic and sales are not stable all over the year, they tend to peak on Black Friday and Cyber Mondays for example. Variability due to these factors could influence your test results.

25. Day of week effect – Similar to seasonality, a metric may have cyclicity based on day of week. For e.g. say conversion rates are much higher on Thursdays than they are on the weekends. In this case, it is important to run tests for full-week increments, so you are including every day of the week.

---

### Block 12

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Key Sections in Detail** > **6\. Timing Issues: Novelty, Seasonality, and Duration**

**Mapping:** score=0.61 reason=keyword:novelty|head='**6\. Timing Issues: Novelty, Seasonality, and Duration**'

Not all effects are immediate or stable. Key timing concerns include:

* **Novelty effects**: A new design may initially excite users, inflating short-term metrics.

* **Carryover effects**: Users exposed to one treatment may retain the impact beyond the experiment window.

* **Seasonality**: Day of week, month, or holiday patterns can skew interpretation.

The recommendation: **run long enough** to capture **steady-state behavior** (often 2-4 weeks) and monitor **lift decay** over time.

---

### Block 13

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Key Sections in Detail** > **8\. Common Pitfalls and Anti-Patterns**

**Mapping:** score=0.638 reason=heading_fuzzy|head='**8\. Common Pitfalls and Anti-Patterns**'

Examples include:

* **Changing code mid-experiment**: Invalidates results.

* **Reusing buckets**: Previous exposure to other treatments contaminates new results.

* **Stopping early**: Increases chance of Type I errors.

* **Incorrect units of analysis**: Can lead to Simpson’s paradox and misinterpretation.

A particularly dangerous error is **not accounting for triggering**—if not all users experience the tested feature, measuring everyone dilutes the effect.

---


