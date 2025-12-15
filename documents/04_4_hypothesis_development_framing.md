## 4. Hypothesis Development & Framing

### Block 1

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 4. Hypothesis Development & Framing > 4.1 Problem Identification

**Mapping:** score=0.61 reason=keyword:problem framing|head='4.1 Problem Identification'

#### 4.1.1 Problem Framing
#### 4.1.2 Research & Data Analysis
#### 4.1.3 Qualitative & Quantitative Insights

---

### Block 2

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 4. Hypothesis Development & Framing > 4.2 Hypothesis Construction

**Mapping:** score=0.645 reason=heading_fuzzy|head='4.2 Hypothesis Construction'

#### 4.2.1 Hypothesis Structure (Change → Outcome)
#### 4.2.2 Testable Predictions
#### 4.2.3 SMART Goal Setting

---

### Block 3

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 4. Hypothesis Development & Framing > 4.3 Test Prioritization

**Mapping:** score=0.61 reason=keyword:backlog|head='4.3 Test Prioritization'

#### 4.3.1 PIE Framework (Potential, Importance, Ease)
#### 4.3.2 Experiment Backlog Management
#### 4.3.3 Risk Appetite Assessment
#### 4.3.4 Quick Wins vs Strategic Bets

---

### Block 4

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Statistical Foundation > 1\. Core Concepts & Formulation

**Mapping:** score=0.61 reason=keyword:hypothesis|head='1\. Core Concepts & Formulation'

* **Hypothesis:** A clear, testable statement. It should be directional.  
  * *Example:* "We hypothesize that by adding a 'Verified by Airbnb' badge on host profiles, we will increase the guest conversion rate for listings with verified hosts because it builds trust."  
* **Variants:**  
  * **Control (A):** The existing experience (e.g., no badge).  
  * **Treatment (B/n):** The new experience(s) (e.g., with a badge, or different badge designs).  
* **Unit of Diversion:** The entity you randomize. This is critical.  
  * **User-ID:** Most common. A user is assigned to a variant for the duration of the experiment.  
  * **Cookie/Session:** For logged-out experiences.  
  * **Airbnb-specific:** Could be `Listing-ID` (for host-side tests) or `Search-Query-ID` (for ranking tests).  
* **Population & Segmentation:** Who are you running the test on? (e.g., all users, only new users in the US, only users searching for "Paris").

---

### Block 5

**Source:** `md`  
**Original headings:** Marketing Experimentation > Foundational Concepts & Core Terminology

**Mapping:** score=0.61 reason=keyword:hypothesis|head='Foundational Concepts & Core Terminology'

* **A/B Testing:** The core concept of comparing two versions (A and B) of a single variable.  
* **A/B/n Testing:** Comparing more than two versions (A, B, C, ...) of a single variable.  
* **Multivariate Testing (MVT):** Testing multiple variables and their combinations simultaneously to understand interaction effects.  
* **Control:** The original, unchanged version (Version A). Also known as the "champion" or "baseline."  
* **Variation / Treatment / Challenger:** The new version(s) being tested against the control.  
* **Hypothesis:** A clear, testable statement about the expected outcome.  
  * **Null Hypothesis ($H\_0$):** The hypothesis that there is no significant difference between the control and the variation. The goal of a test is often to reject the null hypothesis.  
  * **Alternative Hypothesis ($H\_A$):** The hypothesis that there is a significant difference between the versions.  
* **Conversion:** The successful completion of a desired action by a user (e.g., purchase, sign-up, click).  
* **Conversion Rate (CR):** The percentage of users who perform a desired action. Calculated as $(Conversions / Total Visitors) \* 100$.  
* **Conversion Rate Optimization (CRO):** The systematic process of increasing the percentage of users who take a desired action.  
* **Lift / Uplift:** The percentage increase in the conversion rate of the variation over the control.  
* **Randomization:** The process of randomly assigning users to either the control or variation group to eliminate selection bias.  
* **Population:** The entire group of users you are interested in.  
* **Sample:** A subset of the population that is included in the experiment.  
* **Unit of analysis:** The entity being randomly assigned (e.g., user, session, cookie, device ID, page view).

---

### Block 6

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Relationship Between Variables > Correlation

**Mapping:** score=0.61 reason=keyword:quantitative|head='Correlation'

Correlation is a statistical method for determining whether or not two quantitative or categorical variables are related. In other words, it's a measure of how things are connected. Correlation analysis is the study of how variables are connected.

**Examples of data with high correlation:**

- Your calorie consumption and weight  
- Your eye color and the eye colors of your relatives  
- The amount of time you spend studying and your grade point average

**Examples of data with poor (or no) correlation:**

- Your gender and the cereal you eat  
- The name of a dog and the type of dog biscuit they prefer  
- The cost of car washes and the time it takes to get a Coke at the station

Correlations are useful because they allow you to predict future behavior by determining what relationship variables exist. In the social sciences, such as government and healthcare, knowing what the future holds is critical. Budgets and company plans are also based on these facts.

---

### Block 7

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Hypothesis Testing and Statistical Significance

**Mapping:** score=0.61 reason=keyword:hypothesis|head='Hypothesis Testing and Statistical Significance'

Hypothesis testing is a method in which an analyst verifies a hypothesis about population parameters. The analyst's approach is determined by the type of data and the purpose of the study. The utilization of sample data to assess the plausibility of a hypothesis is known as hypothesis testing.

---

### Block 8

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Interpretation > P-value

**Mapping:** score=0.61 reason=keyword:hypothesis|head='P-value'

The p-value in statistics is the likelihood of getting outcomes at least as extreme as the observed results of a statistical hypothesis test, given the null hypothesis is valid. The p-value, instead of rejection points, is used to determine the minimum level of significance at which the null hypothesis is rejected. A lower p-value indicates that the alternative hypothesis has more evidence supporting it.

---

### Block 9

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Interpretation > Significance Level and Rejection Region

**Mapping:** score=0.61 reason=keyword:hypothesis|head='Significance Level and Rejection Region'

The probability that an event (such as a statistical test) occurred by chance is the significance level of the occurrence. We call an occurrence significant if the level is very low, i.e., the possibility of it happening by chance is very minimal. The rejection region depends on the significance level α, indicating the Type I error probability. This significance level is a critical parameter in hypothesis testing.

---

### Block 10

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Statistical Tests > Chi-Square Test

**Mapping:** score=0.61 reason=keyword:hypothesis|head='Chi-Square Test'

It is a test that assesses how well a model matches actual data. A chi-square statistic requires data that is random, raw, mutually exclusive, and collected from independent variables. Additionally, the data must be drawn from a sufficiently large sample. The outcomes of a fair coin flip, for example, meet these conditions.

In hypothesis testing, chi-square tests are frequently utilized. The chi-square statistic examines disparities between expected and actual results given sample size and variables.

---

---

### Block 11

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 6\. Results Interpretation & Decision Making > 6.2 Decision Frameworks

**Mapping:** score=0.61 reason=keyword:hypothesis|head='6.2 Decision Frameworks'

| Framework | Decision Rule | Risk Consideration | Affirm Example |
| :---- | :---- | :---- | :---- |
| **Hypothesis Testing** | Reject if p \< α | Type I/II errors | Ship if p \< 0.05 |
| **Bayesian Decision** | Max expected utility | Loss function | Ship if P(lift\>0) \> 0.95 |
| **Risk-Adjusted** | Consider downside | Worst-case scenario | Ship if worst case \> \-0.5% |
| **Portfolio Approach** | Optimize across tests | Resource allocation | Fund top 20% of ideas |
| **Sequential Decision** | Continue/stop rules | Opportunity cost | Stop if futility boundary crossed |
| **Multi-Stakeholder** | Weighted objectives | Stakeholder alignment | Product \+ Risk \+ Legal approval |

---

### Block 12

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Detailed Experiment Design Guide > 3\. Hypothesis Structure (Using PICO)

**Mapping:** score=0.61 reason=keyword:hypothesis|head='3\. Hypothesis Structure (Using PICO)'

- **Population:** All users entering Affirm's financing funnel  
- **Intervention:** New email design for pre-qualified users  
- **Control:** Original email design  
- **Outcome:** Increase in CTR and loan completions

**Example:** "Among prequalified users (P), if we redesign the email layout (I) compared to the current template (C), we expect a 15% increase in CTR and 10% lift in loan conversion (O)."

---

### Block 13

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Post-Test Actions > Documentation

**Mapping:** score=0.61 reason=keyword:hypothesis|head='Documentation'

- Maintain a centralized experiment wiki (Notion, Confluence)  
- Include: Hypothesis, design, metrics, results, learnings

---

### Block 14

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > A/B Testing Foundations > VI. Organizational & Cultural Aspects

**Mapping:** score=0.61 reason=keyword:hypothesis|head='VI. Organizational & Cultural Aspects'

* **Building a Culture of Experimentation**  
  * Fostering a data-driven, hypothesis-led mindset.  
  * Celebrating learning from "failed" tests as much as from "winning" ones.  
* **Documentation & Knowledge Management**  
  * **Test Hypothesis Template:** Standardizing how tests are proposed.  
  * **Centralized Experiment Repository:** A shared log of all past tests, results, and learnings (e.g., in a wiki or Confluence).  
* **Process & Workflow**  
  * Defining roles and responsibilities (who ideates, who develops, who analyzes?).  
  * Creating a cadence for review meetings and decision-making.  
* **Ethics in Experimentation**  
  * **Informed Consent:** Being transparent with users about data collection and testing, where required.  
  * **Avoiding Dark Patterns:** Ensuring tests are designed to help users, not manipulate them.  
  * **Data Privacy:** Complying with GDPR, CCPA, and other regulations.

---

---

### Block 15

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 2\. Experiment Design (The Engine Room) > **2.1. Hypothesis-Driven Framework**

**Mapping:** score=0.61 reason=keyword:hypothesis|head='**2.1. Hypothesis-Driven Framework**'

* Problem Statement

* Null and Alternative Hypotheses

* Clear dependent (outcome) and independent (treatment) variables.

---

### Block 16

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Key Sections in Detail** > **9\. Organizational Adoption and Culture**

**Mapping:** score=0.61 reason=keyword:prioritization|head='**9\. Organizational Adoption and Culture**'

The biggest barrier to effective experimentation is **not technical—it’s cultural**. The authors argue for building “experimentation cultures” where:

* All teams can run experiments

* Results are shared transparently

* Leaders accept being wrong

* Tools and infrastructure are democratized

Examples from LinkedIn, Bing, and other companies show how central experimentation becomes to roadmap planning, prioritization, and strategy when fully adopted.

---

### Block 17

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **Example 3A: Paired T-Test with a Non-Zero Hypothesis**

**Mapping:** score=0.61 reason=keyword:hypothesis|head='**Example 3A: Paired T-Test with a Non-Zero Hypothesis**'

This variation tests if the change meets a specific magnitude (e.g., "was the weight loss *at least 4 pounds*?"). The formula is adjusted to `t = (d̄ - u₀) / (s_d / √n)`, where `u₀` is the hypothesized difference (-4 pounds in this case). This makes it harder to achieve statistical significance.

---

### Block 18

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > When (and when not) to do product experimentation > When not to experiment

**Mapping:** score=0.61 reason=keyword:qualitative|head='When not to experiment'

There are some situations where experimentation isn’t the best primary option. For example:

* If your user base is too small to produce statistically significant results, you risk drawing the wrong conclusions 

* In some cases, if the change is trivial or low-impact, you’re better off shipping it directly and saving your experimental bandwidth for what really matters 

* When you're in the early stages of product discovery—where qualitative feedback and intuition drive iteration—experimenting too early can slow you down

Long story short: Experimentation is a scalpel, not a hammer. Use it thoughtfully, and it becomes one of your most strategic tools. Use it indiscriminately, and it can lead to false confidence or wasted time and resources.

---

### Block 19

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Product experimentation vs. A/B testing vs. user research

**Mapping:** score=0.61 reason=keyword:research|head='Product experimentation vs. A/B testing vs. user research'

You might sometimes hear these three terms used interchangeably, but there are some key differences between them.

Product experimentation is the broad umbrella term. It includes A/B tests, multivariate tests, feature flags, phased rollouts, and even pricing tests.

A/B testing is a specific kind of experimentation that shows version A to one group and version B to another, then compares the outcomes. User research is yet another kind of experimentation that provides qualitative data—it tells you why users behave a certain way. 

When measuring real-world impact at scale, a mix of quantitative and qualitative data is vital because it gives you both the “what” and the “why.” Quantitative data from A/B tests and other product experiments shows you what’s working (or not) across your user base, while qualitative insights such as [session replays](https://mixpanel.com/blog/mixpanel-session-replay/) and user research help you understand the motivations and friction behind those behaviors.

---

### Block 20

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Product experimentation frameworks: The basics

**Mapping:** score=0.61 reason=keyword:hypothesis|head='Product experimentation frameworks: The basics'

Beyond just running tests, product experimentation succeeds when it’s supported by a repeatable, scalable system that drives learning and growth. The best teams treat experimentation like a product itself: they iterate, improve, and build processes that compound over time.

Most successful teams follow a hypothesis-driven loop. This is a framework that keeps testing aligned with user needs and business goals, and usually looks like this: 

* Identify a user or business problem

* Form a hypothesis (if we do X, Y will improve)

* Choose an experiment type

* Launch with tracking

* Measure results

* Scale what works

There are other frameworks—some emphasize speed, while others focus on statistical rigor or user research depth. Google’s HEART framework, for example, ties experiments to user-centered metrics like happiness and engagement. What matters most isn’t the specific steps you follow, but whether your experimentation system helps your team make better decisions, faster, and with greater confidence.

---

### Block 21

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Step-by-step guide to running an experiment > 2\. Craft a strong hypothesis

**Mapping:** score=0.61 reason=keyword:hypothesis|head='2\. Craft a strong hypothesis'

A well-formed hypothesis makes or breaks your experiment. A good one should be:

* Clear and testable \- Example: If we move the pricing to the homepage, then more users will start the trial because the value is visible earlier.

* Rooted in a problem, not just an idea \- Don’t just test dark mode because it’s cool. Tie it to real user feedback or drop-off data.

* Focused on one variable at a time \- Otherwise, you’ll struggle to know what caused the result.

---

### Block 22

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Step-by-step guide to running an experiment > 6\. Iterate and scale what works

**Mapping:** score=0.61 reason=keyword:backlog|head='6\. Iterate and scale what works'

Once you’ve validated a winner, roll it out to 100% via your flag tool and document the learnings in your team’s experiment backlog or internal wiki—what worked, what didn’t, and what to test next. Use the results to inform the next experiment in the loop, or test additional variations on the winning idea.

If the test failed? That’s still a win. You just saved your team from shipping something that wouldn’t have helped—and you learned something about your users in the process.

---

### Block 23

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Tools and tech stack for experimentation > Qualitative tools: Understand why users behave a certain way

**Mapping:** score=0.61 reason=keyword:qualitative|head='Qualitative tools: Understand why users behave a certain way'

Quantitative data tells you what happened. Qualitative tools help you uncover the why. There are different types of qualitative tools you can use, like surveys and interviews, and they’re crucial for forming better hypotheses and spotting friction points before or after an experiment runs.

For example, if you notice in [session replays](https://docs.mixpanel.com/docs/session-replay) that users are hesitating or dropping off during a multi-step onboarding flow, you might design an experiment to test whether streamlining the number of steps or rewording the instructions leads to higher activation rates.

---


