## 3. Statistical Foundations

### Block 1

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 3. Statistical Foundations > 3.1 Basic Statistical Concepts

**Mapping:** score=0.643 reason=heading_fuzzy|head='3.1 Basic Statistical Concepts'

#### 3.1.1 Mean, Median, Mode
#### 3.1.2 Standard Deviation & Variance
#### 3.1.3 Standard Error (SEM)
#### 3.1.4 Distribution Types (Normal, Binomial, etc.)
#### 3.1.5 Overdispersion

---

### Block 2

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 3. Statistical Foundations > 3.2 Hypothesis Testing Framework

**Mapping:** score=0.61 reason=keyword:hypothesis testing framework|head='3.2 Hypothesis Testing Framework'

#### 3.2.1 Null & Alternative Hypotheses
#### 3.2.2 Composite vs Point Hypotheses
#### 3.2.3 One-Sided vs Two-Sided Tests
#### 3.2.4 Test of Significance vs NHST

---

### Block 3

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 3. Statistical Foundations > 3.3 Statistical Significance

**Mapping:** score=0.63 reason=heading_fuzzy|head='3.3 Statistical Significance'

#### 3.3.1 P-values & Interpretation
#### 3.3.2 Alpha (Type I Error Rate)
#### 3.3.3 Beta (Type II Error Rate)
#### 3.3.4 Confidence Intervals & Confidence Levels
#### 3.3.5 Effect Size (Cohen's d)
#### 3.3.6 Practical vs Statistical Significance

---

### Block 4

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 3. Statistical Foundations > 3.4 Statistical Power

**Mapping:** score=0.681 reason=heading_fuzzy|head='3.4 Statistical Power'

#### 3.4.1 Power Analysis Fundamentals
#### 3.4.2 Power Function
#### 3.4.3 Observed Power (Post Hoc)
#### 3.4.4 Overpowered & Underpowered Tests
#### 3.4.5 Uniformly Most Powerful Tests (UMP)

---

### Block 5

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 8. Statistical Analysis Methods > 8.2 Bayesian Inference

**Mapping:** score=0.61 reason=keyword:distribution|head='8.2 Bayesian Inference'

#### 8.2.1 Prior & Posterior Distributions
#### 8.2.2 Credible Intervals
#### 8.2.3 Posterior Predictive Distributions
#### 8.2.4 Bayes Factors
#### 8.2.5 ROPE (Region of Practical Equivalence)
#### 8.2.6 Loss Functions & Utility
#### 8.2.7 Conjugate Models (Beta-Bernoulli, Normal-Inverse-Gamma)
#### 8.2.8 Hierarchical Bayes
#### 8.2.9 Bayesian Power & Assurance

---

### Block 6

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 11. Multiple Testing & Corrections > 11.5 P-value Adjustments

**Mapping:** score=0.61 reason=keyword:distribution|head='11.5 P-value Adjustments'

#### 11.5.1 Nominal vs Adjusted P-values
#### 11.5.2 P-value Distribution

---

### Block 7

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 12. Results Interpretation & Analysis > 12.1 Reading Test Results

**Mapping:** score=0.61 reason=keyword:distribution|head='12.1 Reading Test Results'

#### 12.1.1 Effect Size Interpretation
#### 12.1.2 Lift & Confidence Intervals
#### 12.1.3 Uplift Distribution
#### 12.1.4 MDE Attainment

---

### Block 8

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 13. Common Pitfalls & Biases > 13.1 Statistical Pitfalls

**Mapping:** score=0.706 reason=heading_fuzzy|head='13.1 Statistical Pitfalls'

#### 13.1.1 Peeking Without Control
#### 13.1.2 P-Hacking & Data Fishing
#### 13.1.3 Winner's Curse
#### 13.1.4 Regression to the Mean
#### 13.1.5 Power Dilution
#### 13.1.6 Inconsistent Denominators

---

### Block 9

**Source:** `docx`  
**Original headings:** A/B Testing & Marketing Experimentation - Consolidated Table of Contents > 19. Privacy, Ethics & Compliance > 19.1 Ethical Considerations

**Mapping:** score=0.642 reason=heading_fuzzy|head='19.1 Ethical Considerations'

#### 19.1.1 Informed Consent
#### 19.1.2 Potential Harm Assessment
#### 19.1.3 Transparency Requirements
#### 19.1.4 IRB & Ethics Review

---

### Block 10

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Statistical Foundation

**Mapping:** score=0.885 reason=heading_fuzzy|head='The Statistical Foundation'

As a Data Analyst, your primary responsibility is to ensure the statistical rigor of experiments. Interviewers will probe this deeply.

---

### Block 11

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Statistical Foundation > 4\. Statistical Significance & Testing

**Mapping:** score=0.61 reason=keyword:mean|head='4\. Statistical Significance & Testing'

* **p-value:** The probability of observing your results (or more extreme) if the null hypothesis (no difference) is true.  
  * **Interpretation:** A p-value \< 0.05 means there's less than a 5% chance the observed difference is due to random noise. **It does NOT mean the result is 95% true.**  
* **Confidence Intervals:** A range of values that is likely to contain the true effect size. **Always report effect sizes with confidence intervals.** A 95% CI means if you ran the experiment 100 times, 95 of the CIs would contain the true mean.  
  * *Example:* "The badge increased conversion by \+1.5% (±0.5%, 95% CI)." This tells you the magnitude and the precision.  
* **Common Pitfalls:**  
  * **Peeking:** Repeatedly checking results before the test ends. Use **Sequential Testing** methods if this is necessary.  
  * **Multiple Testing Problem:** Running many tests on the same data increases the false positive rate. Use corrections like Bonferroni.  
  * **Novelty Effect:** Users might interact with a new feature just because it's new, not because it's better. The effect might fade over time.

---

### Block 12

**Source:** `md`  
**Original headings:** Marketing Experimentation > Statistical Concepts & Potential Pitfalls

**Mapping:** score=0.61 reason=keyword:mean|head='Statistical Concepts & Potential Pitfalls'

* **Frequentist Approach:** The classical statistics framework based on p-values and confidence intervals.  
* **Bayesian Approach:** An alternative framework that calculates the "probability to be best" or "probability to beat control," often considered more intuitive for business decisions.  
  * **Credible Interval:** The Bayesian equivalent of a confidence interval.  
  * **Posterior Probability:** The updated probability of an outcome after collecting evidence.  
* **Type I Error (False Positive, $\\alpha$):** Concluding there is an effect when there isn't one.  
* **Type II Error (False Negative, $\\beta$):** Failing to detect an effect that actually exists.  
* **Multiple Comparisons Problem:** The risk of finding a false positive increases as you test more variations or look at more metrics/segments.  
  * **Bonferroni Correction:** A method to counteract the multiple comparisons problem.  
* **Regression to the Mean:** The phenomenon where an extreme result is likely to be followed by a result closer to the average.  
* **Novelty Effect:** Users initially reacting positively to a change simply because it's new.  
* **Learning Effect:** The opposite of the novelty effect, where users take time to adapt to a new design, and performance improves over time.  
* **Simpson's Paradox:** A trend that appears in different groups of data but disappears or reverses when these groups are combined.  
* **Network Effects / Crossover Effects:** When the experience of users in one group affects the behavior of users in another group (e.g., on a social media or marketplace platform).

---

### Block 13

**Source:** `md`  
**Original headings:** Marketing Experimentation > Marketing-Specific Applications & Metrics

**Mapping:** score=0.61 reason=keyword:sem|head='Marketing-Specific Applications & Metrics'

* **Website & Landing Page Optimization:**  
  * Call-to-Action (CTA) button text, color, placement.  
  * Headline and copy testing.  
  * Form field length and design.  
  * Page layout and navigation.  
  * Imagery and video.  
  * Social proof (testimonials, reviews).  
* **Email Marketing:**  
  * Subject line testing.  
  * "From" name.  
  * Send time/day optimization.  
  * Email body content, layout, and CTAs.  
* **Paid Advertising (SEM/PPC/Social):**  
  * Ad copy and headline variations.  
  * Display ad creative testing.  
  * Landing page destination testing.  
  * Bidding strategy experiments.  
* **Marketing Funnel Stages:**  
  * **Top of Funnel (TOFU):** Testing for engagement, click-through rate.  
  * **Middle of Funnel (MOFU):** Testing for lead generation, downloads, sign-ups.  
  * **Bottom of Funnel (BOFU):** Testing for purchases, demo requests, average order value.  
* **Common Marketing Metrics for Testing:**  
  * Click-Through Rate (CTR)  
  * Cost Per Acquisition (CPA)  
  * Return on Ad Spend (ROAS)  
  * Average Order Value (AOV)  
  * Customer Lifetime Value (LTV)  
  * Unsubscribe Rate  
  * Bounce Rate  
  * Time on Page

---

### Block 14

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Philosophical Basis and Role of Statistics

**Mapping:** score=0.61 reason=keyword:mean|head='The Philosophical Basis and Role of Statistics'

Statistics is presented as a discipline distinct from mathematics, using math as a tool to express its ideas, much like physics does. The core of statistical thinking is **relativity**; that is, numbers are rarely evaluated in a vacuum but rather in the context of their distributions. The overall goal is to use data from samples to make inferences about entire populations.

The sources distinguish between two primary philosophical approaches to statistical inference:

* **Frequentist Approach**: This is the classical approach where the parameter of interest (e.g., the population mean) is considered a fixed, unknown constant. The goal is to estimate this value using an **estimator**, which is a function of the sample data. Since the estimator's value varies from sample to sample, its properties are assessed through its sampling distribution.  
* **Bayesian Approach**: In this framework, the unknown parameter is treated as a random variable that has its own probability distribution. The process begins with a **prior distribution** (or "prior"), which represents initial beliefs about the parameter before observing data. After collecting data, Bayes' Theorem is used to update these beliefs, resulting in a **posterior distribution**. This posterior distribution combines information from both the prior and the data.

---

### Block 15

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Philosophical Basis and Role of Statistics > **Core Statistical Concepts** > **Probability Theory**

**Mapping:** score=0.61 reason=keyword:mean|head='**Probability Theory**'

Probability is the foundation of statistical inference, offering a mathematical way to quantify uncertainty. Key concepts include:

* **Random Variables**: A variable that takes on different numerical values based on the outcome of a random process. They can be discrete (taking on a finite number of values) or continuous.  
* **Probability Distributions**: These are mathematical functions that describe the likelihood of different outcomes for a random variable. Important distributions mentioned include:  
  * **Normal Distribution**: Also known as the "bell curve" or Gaussian distribution, it is a symmetrical distribution where data clusters around the central mean. It is a cornerstone of statistics, and the **Central Limit Theorem** states that the sampling distribution of the mean will approximate a normal distribution for large enough sample sizes, regardless of the population's original distribution.  
  * **Binomial Distribution**: Used for discrete data where each trial has only two possible outcomes (e.g., success/failure).  
  * **Poisson Distribution**: Models the number of events occurring in a fixed interval of time or space, often used for count data.  
  * **Gamma Distribution**: A continuous distribution often used as a conjugate prior in Bayesian analysis.  
* **Conditional Probability and Bayes' Theorem**: Conditional probability is the likelihood of an event occurring given that another event has already happened. **Bayes' Theorem** provides a mathematical formula to update a probability based on new evidence, which is the engine of Bayesian inference.

---

### Block 16

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Philosophical Basis and Role of Statistics > **Core Statistical Concepts** > **Descriptive and Inferential Statistics**

**Mapping:** score=0.61 reason=keyword:mean|head='**Descriptive and Inferential Statistics**'

Statistics is broadly divided into two categories:

* **Descriptive Statistics**: This involves summarizing and describing the main features of a dataset using numerical representations and visualizations. Key measures include:  
  * **Measures of Central Tendency**: These locate the center of a distribution and include the **mean** (average), **median** (middle value), and **mode** (most frequent value).  
  * **Measures of Dispersion**: These describe the spread or variability of the data. They include the **range** (difference between maximum and minimum values), **variance** (average of the squared deviations from the mean), and **standard deviation** (the square root of the variance).  
* **Inferential Statistics**: This involves using data from a sample to make generalizations or inferences about a larger population. The two primary tools of inferential statistics are estimation and hypothesis testing.

---

### Block 17

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Philosophical Basis and Role of Statistics > **Core Statistical Concepts** > **Hypothesis Testing**

**Mapping:** score=0.61 reason=keyword:mean|head='**Hypothesis Testing**'

This is a formal procedure for assessing two mutually exclusive statements about a population to determine which statement is best supported by the sample data.

* **Null and Alternative Hypotheses**: The **null hypothesis (H₀)** is a statement of no effect or no difference, often representing the status quo. The **alternative hypothesis (H₁)** is the statement that must be true if the null is false.  
* **P-value**: The p-value is the probability of observing a test statistic as extreme as, or more extreme than, the one actually observed, *assuming the null hypothesis is true*. A low p-value (typically ≤ 0.05) indicates that the observed data is unlikely under the null hypothesis, providing evidence to reject it.  
* **Significance Level (Alpha)**: This is a predetermined threshold (commonly 0.05) that represents the probability of committing a **Type I error**—rejecting the null hypothesis when it is actually true.  
* **Statistical Significance**: A result is deemed statistically significant if the p-value is less than the chosen significance level. It is crucial to distinguish this from **practical significance**, which refers to whether the observed effect is large enough to be meaningful in a real-world context. **Effect size** measures (like Cohen's d, eta-squared, or R²) quantify the magnitude of an effect and help assess practical significance.

---

### Block 18

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Philosophical Basis and Role of Statistics > **Core Statistical Concepts** > **Estimation and Confidence Intervals**

**Mapping:** score=0.61 reason=keyword:mean|head='**Estimation and Confidence Intervals**'

Estimation involves using sample data to calculate a value for an unknown population parameter.

* **Point and Interval Estimators**: A **point estimator** provides a single value as the best guess for the parameter (e.g., the sample mean estimates the population mean). An **interval estimator**, or **confidence interval**, provides a range of values that is likely to contain the true population parameter with a certain level of confidence (e.g., 95%).  
* **Properties of Estimators**: Good estimators have desirable properties such as being **unbiased** (the expected value of the estimator equals the true parameter value) and **consistent** (the estimator converges to the true parameter value as the sample size increases).

---

### Block 19

**Source:** `md`  
**Original headings:** Marketing Experimentation > The Philosophical Basis and Role of Statistics > **Foundational Statistical Models and Techniques**

**Mapping:** score=0.61 reason=keyword:mean|head='**Foundational Statistical Models and Techniques**'

The sources discuss numerous statistical techniques that build upon these foundational concepts.

* **T-tests**: Used to compare the means of one or two groups.  
* **Analysis of Variance (ANOVA)**: An extension of the t-test used to compare the means of three or more groups by analyzing their variances. It partitions the total variation in the data into between-group and within-group components. The **F-test** is used to determine if the variation between groups is significantly larger than the variation within groups.  
* **Correlation and Regression**: **Correlation** measures the strength and direction of a linear association between two variables. **Regression analysis** is a technique used to model the relationship between a dependent variable and one or more independent variables, often for prediction. This includes simple linear regression, multiple linear regression, and logistic regression (for categorical outcomes).  
* **Chi-Square Test**: A non-parametric test used to analyze categorical data, often to test for the independence of two variables in a contingency table or for goodness-of-fit.  
* **Advanced Models**: More complex methods like **Factor Analysis**, **Cluster Analysis**, **MANOVA**, **Discriminant Analysis**, and **Structural Equation Modeling (SEM)** are presented as extensions of these fundamental concepts, often dealing with multiple variables (multivariate analysis) or unobservable latent constructs.

---

---

### Block 20

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Table of Contents

**Mapping:** score=0.61 reason=keyword:mean|head='End to End Statistics for Data Science'

- Descriptive Analytics  
- Diagnostic Analytics  
- Predictive Analytics  
- Prescriptive Analytics  
- Probability  
- Properties of Statistics  
- Complement  
- Intersection  
- Conditional Probability  
- Independent Events  
- Mutually Exclusive Events  
- Bayes' Theorem  
- Central Tendency in Statistics  
- Mean  
- Median  
- Mode  
- Skewness  
- Kurtosis  
- Variability in Statistics  
- Range  
- Percentiles, Quartiles and Interquartile Range (IQR)  
- Relationship Between Variables  
- Probability Distributions  
- Probability Distribution Functions  
- Continuous Probability Distribution  
- Hypothesis Testing and Statistical Significance in Statistics  
- Null and Alternative Hypothesis  
- Type 1 and Type 2 Error  
- Interpretation  
- Significance Level and Rejection Region  
- Frequently Asked Questions

---

### Block 21

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Importance of Statistics

**Mapping:** score=0.61 reason=keyword:distribution|head='Importance of Statistics'

Using various statistical tests helps determine the relevance of features and avoid the risk of duplicate features by finding relationships between them. Key statistical practices include:

- Putting features into the proper format  
- Data normalization and scaling, including determining the distribution and nature of data  
- Taking data for further processing and making necessary modifications  
- Determining the best mathematical approach or model after processing the data  
- Checking acquired data against various accuracy measuring scales

---

### Block 22

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Central Tendency in Statistics > Mean

**Mapping:** score=0.61 reason=keyword:mean|head='Mean'

The mean (or average) is the most generally used and well-known measure of central tendency. It can be used with both discrete and continuous data, though it's most typically used with continuous data. The mean is equal to the sum of all the values in the data set divided by the number of values in the data set.

If we have n values in a data set with values x₁, x₂, ..., xₙ, the sample mean, usually denoted by "x̄" (x bar), is:

**x̄ \= (x₁ \+ x₂ \+ ... \+ xₙ) / n**

---

### Block 23

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Central Tendency in Statistics > Median

**Mapping:** score=0.61 reason=keyword:mean|head='Median'

The median value of a dataset is the value in the middle of the dataset when it is arranged in ascending or descending order. When the dataset has an even number of values, the median value can be calculated by taking the mean of the middle two values.

---

### Block 24

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Central Tendency in Statistics > Mode

**Mapping:** score=0.61 reason=keyword:distribution|head='Mode'

The mode is the value that appears most frequently in your data set. The mode is the highest bar in a bar chart. A multimodal distribution exists when the data contains multiple values that are tied for most frequently occurring. If no value repeats, the data does not have a mode.

---

### Block 25

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Central Tendency in Statistics > Skewness

**Mapping:** score=0.61 reason=keyword:mean|head='Skewness'

Skewness is a metric for symmetry, or more specifically, the lack of it. If a distribution, or data collection, looks the same to the left and right of the center point, it is said to be symmetric.

**Types of Skewness:**

- **Positive Skew (Right Skew)**: Tail extends to the right, mean \> median \> mode  
- **Negative Skew (Left Skew)**: Tail extends to the left, mean \< median \< mode  
- **Zero Skew**: Symmetrical distribution, mean \= median \= mode

---

### Block 26

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Central Tendency in Statistics > Kurtosis

**Mapping:** score=0.61 reason=keyword:distribution|head='Kurtosis'

Kurtosis is a measure of how heavy-tailed or light-tailed the data are in comparison to a normal distribution. Data sets having high kurtosis are more likely to contain heavy tails or outliers. Light tails or a lack of outliers are common in data sets with low kurtosis.

**Types of Kurtosis:**

- **Leptokurtic**: High kurtosis, heavy tails  
- **Mesokurtic**: Normal distribution kurtosis  
- **Platykurtic**: Low kurtosis, light tails

---

### Block 27

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Variability in Statistics > Range

**Mapping:** score=0.61 reason=keyword:distribution|head='Range'

In statistics, the range is the smallest of all dispersion measures. It is the difference between the distribution's two extreme observations. In other words, the range is the difference between the distribution's maximum and minimum observations.

**Range \= Xmax − Xmin**

Where Xmax represents the largest observation and Xmin represents the smallest observation of the variable values.

---

### Block 28

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Variability in Statistics > Variance

**Mapping:** score=0.61 reason=keyword:mean|head='Variance'

The dispersion of a data collection is measured by variance. It is defined technically as the average of squared deviations from the mean.

For a sample: **s² \= Σ(xi \- x̄)² / (n-1)**

For a population: **σ² \= Σ(xi \- μ)² / N**

---

### Block 29

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Variability in Statistics > Standard Deviation

**Mapping:** score=0.61 reason=keyword:mean|head='Standard Deviation'

The standard deviation is a measure of data dispersion within a single sample selected from the study population. The square root of the variance is used to compute it. It simply indicates how distant the individual values in a sample are from the mean.

**s \= √\[Σ(xi \- x̄)² / (n-1)\]**

---

### Block 30

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Variability in Statistics > Standard Error (SE)

**Mapping:** score=0.61 reason=keyword:mean|head='Standard Error (SE)'

The standard error indicates how close the mean of any given sample from that population is to the true population mean. When the standard error rises, implying that the means are more dispersed, it becomes more likely that any given mean is an inaccurate representation of the true population mean. When the sample size is increased, the standard error decreases—as the sample size approaches the true population size, the sample means cluster more and more around the true population mean.

**SE \= s / √n**

Where s is the sample standard deviation and n is the sample size.

---

### Block 31

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Relationship Between Variables > Covariance

**Mapping:** score=0.61 reason=keyword:variance|head='Covariance'

Covariance is a measure of the relationship between two random variables in mathematics and statistics. The statistic assesses how much—and how far—the variables change in tandem. In other words, it's a measure of the variance between two variables. The metric, however, does not consider the interdependence of factors. Any positive or negative value can be used for the covariance.

**The values are interpreted as follows:**

- **Positive covariance**: When two variables move in the same direction  
- **Negative covariance**: Indicates that two variables are moving in opposite directions

---

### Block 32

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Probability Distributions > Probability Distribution Functions

**Mapping:** score=0.61 reason=keyword:distribution|head='Probability Distribution Functions'

**Probability Mass Function (PMF)**: The probability distribution of a discrete random variable is described by the PMF, which is a statistical term. The PDF and PMF are frequently misunderstood. The PDF is for continuous random variables, whereas the PMF is for discrete random variables. Example: throwing a dice (you can only choose from 1 to 6 numbers—countable).

**Probability Density Function (PDF)**: The probability distribution of a continuous random variable is described by the word PDF, which is a statistical term. The Gaussian Distribution is the most common distribution used in PDF. If the features/random variables are Gaussian distributed, then the PDF will be as well. Because a single point represents a line that does not span the area under the curve, the probability of a single outcome is always 0 on a PDF graph.

**Cumulative Density Function (CDF)**: The cumulative distribution function can be used to describe the continuous or discrete distribution of random variables. If X is the height of a person chosen at random, then F(x) is the probability of the individual being shorter than x. If F(180 cm) \= 0.8, then an individual chosen at random has an 80% chance of being shorter than 180 cm (equivalently, a 20% chance that they will be taller than 180 cm).

---

### Block 33

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Continuous Probability Distributions > Uniform Distribution

**Mapping:** score=0.61 reason=keyword:distribution|head='Uniform Distribution'

Uniform distribution is a type of probability distribution in statistics in which all events are equally likely. A deck of cards contains uniform distributions because the chances of drawing a heart, a club, a diamond, or a spade are equal. A coin has a uniform distribution because the likelihood of receiving heads or tails in a coin toss is the same.

A coin flip that returns a head or tail has a probability of p \= 0.50 and would be represented by a line from the y-axis at 0.50.

---

### Block 34

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Continuous Probability Distributions > Normal/Gaussian Distribution

**Mapping:** score=0.61 reason=keyword:mean|head='Normal/Gaussian Distribution'

The normal distribution, also known as the Gaussian distribution, is a symmetric probability distribution centered on the mean, indicating that data around the mean occur more frequently than data far from it. The normal distribution will show as a bell curve on a graph.

**Points to remember:**

- A probability bell curve is referred to as a normal distribution  
- The mean of a standard normal distribution is 0 and the standard deviation is 1  
- It has a kurtosis of 3 and zero skew  
- Although all symmetrical distributions are not necessarily normal, normal distributions are always symmetrical  
- Most pricing distributions aren't totally normal

---

### Block 35

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Continuous Probability Distributions > Exponential Distribution

**Mapping:** score=0.61 reason=keyword:sem|head='Exponential Distribution'

The exponential distribution is a continuous distribution used to estimate the time it will take for an event to occur. For example, in physics, it is frequently used to calculate radioactive decay; in engineering, it is frequently used to calculate the time required to receive a defective part on an assembly line; and in finance, it is frequently used to calculate the likelihood of a portfolio of financial assets defaulting. It can also be used to estimate the likelihood of a certain number of defaults occurring within a certain time frame.

---

### Block 36

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Continuous Probability Distributions > Chi-Square Distribution

**Mapping:** score=0.61 reason=keyword:variance|head='Chi-Square Distribution'

A continuous distribution with degrees of freedom is called a chi-square distribution. It's used to describe a sum of squared random variables' distribution. It's also used to determine whether a data distribution's goodness of fit is good, whether data series are independent, and to estimate confidence intervals around variance and standard deviation for a random variable from a normal distribution. Furthermore, the chi-square distribution is a subset of the gamma distribution.

---

### Block 37

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Discrete Probability Distributions > Bernoulli Distribution

**Mapping:** score=0.61 reason=keyword:distribution|head='Bernoulli Distribution'

A Bernoulli distribution is a discrete probability distribution for a Bernoulli trial, which is a random experiment with just two outcomes (named "Success" or "Failure" in most cases). When flipping a coin, the likelihood of getting a head (a "success") is 0.5. "Failure" has a chance of 1 − p (where p is the probability of success, which also equals 0.5 for a coin toss). For n \= 1, it is a particular case of the binomial distribution. In other words, it's a single-trial binomial distribution (e.g., a single coin toss).

---

### Block 38

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Discrete Probability Distributions > Binomial Distribution

**Mapping:** score=0.61 reason=keyword:distribution|head='Binomial Distribution'

A discrete distribution is a binomial distribution. It's a well-known probability distribution. The model is then used to depict a variety of discrete phenomena seen in business, social science, natural science, and medical research.

**For binomial distribution to be used, the following conditions must be met:**

- There are n identical trials in the experiment, with n being a finite number  
- Each trial has only two possible outcomes, i.e., each trial is a Bernoulli's trial  
- One outcome is denoted by the letter S (for success) and the other by the letter F (for failure)  
- From trial to trial, the chance of S remains the same. The chance of success is represented by p, and the likelihood of failure is represented by q (where p \+ q \= 1\)  
- Each trial is conducted independently  
- The number of successful trials in n trials is the binomial random variable x

If X reflects the number of successful trials in n trials under the preceding conditions, then x is said to follow a binomial distribution with parameters n and p.

---

### Block 39

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Discrete Probability Distributions > Poisson Distribution

**Mapping:** score=0.61 reason=keyword:mean|head='Poisson Distribution'

A Poisson distribution is a probability distribution used in statistics to show how many times an event is expected to happen over a certain amount of time. In other words, it's a count distribution. Poisson distributions are frequently used to understand independent events that occur at a constant rate during a selected timeframe.

The Poisson distribution is a discrete function, which means the variable can only take values from a (possibly endless) list of possibilities. To put it another way, the variable can't take all of the possible values in any continuous range. The variable can only take the values 0, 1, 2, 3, etc., with no fractions or decimals, in the Poisson distribution.

---

### Block 40

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Hypothesis Testing and Statistical Significance > Null and Alternative Hypothesis

**Mapping:** score=0.61 reason=keyword:mean|head='Null and Alternative Hypothesis'

**Null Hypothesis (H₀)**

A population parameter (such as the mean, standard deviation, and so on) is equal to a hypothesized value, according to the null hypothesis. The null hypothesis is a claim that is frequently made based on previous research or specialized expertise.

**Alternative Hypothesis (H₁)**

The alternative hypothesis says that a population parameter is less, more, or different than the null hypothesis's hypothesized value. The alternative hypothesis is what you believe or want to prove to be correct.

---

### Block 41

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Hypothesis Testing and Statistical Significance > Type 1 and Type 2 Errors

**Mapping:** score=0.61 reason=keyword:mean|head='Type 1 and Type 2 Errors'

**Type 1 Error (False Positive)**

A Type 1 error, often referred to as a false positive, happens when a researcher rejects a true null hypothesis incorrectly. This means you're claiming your findings are significant when they actually happened by coincidence.

Your alpha level (α), which is the p-value below which you reject the null hypothesis, represents the likelihood of making a Type I error. When rejecting the null hypothesis, a p-value of 0.05 indicates a 5% chance of being mistaken.

By setting α to a smaller value, you'll lessen your chances of making a Type I error.

**Type 2 Error (False Negative)**

A Type II error, commonly referred to as a false negative, occurs when a researcher fails to reject a null hypothesis that is actually false. In this case, the researcher concludes that there is no significant influence, when in fact there is.

Beta (β) is the probability of making a Type II error, and it's inversely related to the statistical test's power (power \= 1 − β). By ensuring that your test has enough power, you'll reduce your chances of making a Type II error.

This can be accomplished by ensuring that your sample size is sufficient to detect a practical difference when one exists.

---

### Block 42

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Interpretation > Critical Value

**Mapping:** score=0.61 reason=keyword:distribution|head='Critical Value'

It is a point on the test distribution that is compared to the test statistic to see if the null hypothesis should be rejected. Reject the null hypothesis if the absolute test statistic exceeds the critical value, indicating statistical significance.

---

### Block 43

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Statistical Tests > Z-Test

**Mapping:** score=0.61 reason=keyword:mean|head='Z-Test'

The z-test is a hypothesis test in which the z-statistic is normally distributed. The z-test is best utilized for samples with more than 30 observations because, according to the central limit theorem, samples with over 30 samples are assumed to be approximately normally distributed.

The null and alternative hypotheses, as well as the alpha and z-score, should all be reported when doing a z-test. The test statistic should next be calculated, followed by the results and conclusion. A z-statistic, also called a z-score, is a number that indicates how many standard deviations a score produced from a z-test is above or below the mean population.

---

### Block 44

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Statistical Tests > T-Test

**Mapping:** score=0.61 reason=keyword:mean|head='T-Test'

A t-test is an inferential statistic that's used to see if there's a significant difference in the means of two groups that are related in some way. It's most commonly employed when data sets, like those obtained by flipping a coin 100 times, are expected to follow a normal distribution and have unknown variances. A t-test is a hypothesis-testing technique that can be used to assess an assumption that's applicable to a population.

---

### Block 45

**Source:** `md`  
**Original headings:** End to End Statistics for Data Science > Statistical Tests > ANOVA (Analysis of Variance)

**Mapping:** score=0.61 reason=keyword:mean|head='ANOVA (Analysis of Variance)'

ANOVA is the way to find out if experimental results are significant. One-way ANOVA compares two means from two independent groups using only one independent variable. Two-way ANOVA is the extension of one-way ANOVA using two independent variables to calculate the main effect and interaction effect.

---

### Block 46

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 2\. Statistical Framework & Power Analysis > 2.1 Statistical Test Selection

**Mapping:** score=0.643 reason=heading_fuzzy|head='2.1 Statistical Test Selection'

| Test Type | Use Case | Key Assumptions | Affirm Example |
| :---- | :---- | :---- | :---- |
| **Z-Test** | • Large samples (n\>30) • Known population variance • Normal distribution | • Independence • Normality • Equal variance | Comparing conversion rates with 100k+ users |
| **T-Test (Student's)** | • Small samples • Unknown variance • Continuous outcomes | • Independence • Normality • Equal variance | Comparing average order values |
| **Welch's T-Test** | • Unequal variances • Different sample sizes | • Independence • Normality | Comparing segments with different sizes |
| **Mann-Whitney U** | • Non-parametric • Ordinal data • Non-normal distribution | • Independence • Ordinal scale | Comparing user satisfaction scores |
| **Chi-Square Test** | • Categorical outcomes • Independence testing | • Expected frequency \>5 • Independence | Testing payment method preferences |
| **Fisher's Exact Test** | • Small sample sizes • 2x2 contingency tables | • Independence | Rare event analysis (fraud rates) |
| **Kolmogorov-Smirnov** | • Distribution comparison • Continuous data | • Independence • Continuous scale | Comparing entire distributions of loan amounts |
| **Bootstrap Methods** | • No distribution assumptions • Complex statistics | • Independence | Confidence intervals for median time to repayment |
| **Bayesian Methods** | • Prior information • Sequential analysis • Posterior probabilities | • Prior specification | Updating conversion rate beliefs with new data |
| **CUPED/CUPAC** | • Variance reduction • Pre-experiment data | • Covariate stability | Using historical purchase data to reduce variance |

---

### Block 47

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 5\. Analysis Methods & Techniques > 5.1 Primary Analysis Approaches

**Mapping:** score=0.61 reason=keyword:variance|head='5.1 Primary Analysis Approaches'

| Method | Statistical Technique | Implementation | Affirm Example |
| :---- | :---- | :---- | :---- |
| **Frequentist Analysis** | • Hypothesis testing • Confidence intervals • P-values | • Python statsmodels • R stats package | t-test on conversion rates |
| **Bayesian Analysis** | • Posterior distributions • Credible intervals • Bayes factors | • PyMC3 • Stan • JAGS | P(variant \> control) \= 0.97 |
| **Regression Adjustment** | • ANCOVA • Linear models • Propensity scores | • Include covariates • Reduce variance | Adjust for user credit score |
| **Machine Learning** | • Causal forests • Double ML • Targeted learning | • CausalML • EconML | Heterogeneous treatment effects |
| **Time Series** | • Interrupted time series • ARIMA models • State space models | • Seasonal adjustment • Trend analysis | Account for holiday effects |
| **Survival Analysis** | • Kaplan-Meier • Cox regression • AFT models | • Time to event • Censoring | Time to first purchase |

---

### Block 48

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 8\. Advanced Topics & Considerations > 8.2 Ethical Considerations

**Mapping:** score=0.654 reason=heading_fuzzy|head='8.2 Ethical Considerations'

| Aspect | Guidelines | Implementation | Example |
| :---- | :---- | :---- | :---- |
| **Fairness** | • Equal treatment • No discrimination | • Bias testing • Fairness metrics | Equal approval rates across demographics |
| **Transparency** | • User notification • Opt-out options | • Privacy policy • Clear communication | "You're seeing a new checkout experience" |
| **Risk Management** | • Minimize harm • Protect vulnerable users | • Guardrail metrics • Safety protocols | Don't test on high-risk loan applicants |
| **Data Privacy** | • GDPR compliance • Data minimization | • Anonymization • Retention policies | Hash PII, delete after analysis |

---

### Block 49

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Statistical Planning > Randomization Approach

**Mapping:** score=0.61 reason=keyword:variance|head='Randomization Approach'

- **Stratified randomization** to control for high-variance features (e.g., mobile vs desktop, merchant category)  
- Example: Users from travel merchants vs. retail merchants might behave differently

---

### Block 50

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Statistical Analysis & Models > Frequentist Methods

**Mapping:** score=0.61 reason=keyword:mean|head='Frequentist Methods'

- **t-test** for means (e.g., loan size)  
- **z-test** for proportions (e.g., CTR)  
- **Chi-square test** for categorical outcomes

---

### Block 51

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Advanced Approaches > CUPED (Controlled Pre-experiment Data)

**Mapping:** score=0.61 reason=keyword:variance|head='CUPED (Controlled Pre-experiment Data)'

Reduces variance using pre-experiment behavior as a covariate

---

### Block 52

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Structured Learning Sequence for Marketing Experimentation \[Continued\] > Power, Sample Size, and MDE — how they relate (with Airbnb examples)

**Mapping:** score=0.61 reason=keyword:variance|head='Power, Sample Size, and MDE — how they relate (with Airbnb examples)'

Intuition (analogy):  
Think of detecting treatment impact like trying to hear a soft melody (true lift) in a noisy café (natural variance).

* MDE (Minimum Detectable Effect) \= the faintest melody you claim you can reliably hear.

* Power (1−β) \= the chance you’ll actually detect that melody if it’s playing.

* Sample size \= how many people you’ll ask to listen; more listeners → the melody stands out from noise.

Core relationships:

* For fixed traffic & variance, smaller MDE ⇒ larger n needed.

* For fixed MDE, higher power ⇒ larger n.

* For fixed n and power, higher baseline variance ⇒ larger MDE (harder to separate signal from noise).

Frequentist two-proportion (A/B) sample size (per group) for conversion uplift  
 Let baseline conversion be (p), target uplift (d \= p\_B \- p\_A) (absolute, in points), two-sided (\\alpha), power (1-\\beta):  
 \[  
 n \\approx \\frac{2,p(1-p),\\big(z\_{1-\\alpha/2}+z\_{1-\\beta}\\big)^2}{d^2}  
 \]  
 (Conservative approximation; exact formulas use unpooled terms.)

Airbnb example:

* Baseline booking conversion on a key landing page (p=3%) (0.03).

* You want to detect (d=0.5) percentage points (0.005) at (\\alpha=0.05), power (=0.80).

* (z\_{1-0.05/2}=1.96), (z\_{0.80}=0.84); sum (=2.80); squared (=7.84).

* (p(1-p)=0.03\\times0.97=0.0291).

* Numerator (=2\\times0.0291\\times7.84 \= 0.456288).

* Denominator (=d^2=0.005^2=0.000025).

* (n \\approx 0.456288 / 0.000025 \\approx 18{,}252) users per arm.

Talking points you can use:

* “MDE is an explicit promise about sensitivity; we set it from business value (e.g., a \+0.5pp lift justifies eng time). Then I compute power-based n. If traffic can’t support it in time, I either relax MDE, extend duration, or use variance reduction (e.g., CUPED) to keep sensitivity.”

Variance reduction (quick):  
 CUPED uses a pre-period metric (X) correlated with outcome (Y): adjust (Y' \= Y \- \\theta (X-\\bar X)) where (\\theta \= \\frac{\\mathrm{Cov}(Y,X)}{\\mathrm{Var}(X)}). If Airbnb has strong pre-period booking propensities, you can shrink variance and cut required n materially.

---

### Block 53

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Structured Learning Sequence for Marketing Experimentation \[Continued\] > 3\) ANOVA vs. multiple t-tests — when and why

**Mapping:** score=0.61 reason=keyword:mean|head='3\) ANOVA vs. multiple t-tests — when and why'

Intuition (analogy):  
 Testing many variants with separate t-tests is like tossing lots of fishing lines; each increases the chance you’ll catch a false fish. ANOVA starts with a global “is any mean different?” before you fish specifically.

Use ANOVA when:

* ≥3 groups (A/B/C/D…) for a single continuous or rate outcome (with appropriate GLM).

* You want to control Family-Wise Error Rate globally before pairwise comparisons.

* Factorial structures (e.g., 2×3 designs) where you care about main effects and interactions.

Airbnb example:  
 Testing 4 hero images on the homepage (A/B/C/D). Start with one-way ANOVA (or a logistic/Poisson GLM for conversions) to test (H\_0): all group means equal. If rejected, follow with adjusted pairwise tests (Tukey/Holm) to locate winners, controlling multiplicity.

---

### Block 54

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Structured Learning Sequence for Marketing Experimentation \[Continued\] > 4\) How randomization removes confounding — and when to stratify

**Mapping:** score=0.61 reason=keyword:variance|head='4\) How randomization removes confounding — and when to stratify'

Intuition (analogy):  
 Randomization is a shuffle machine that balances seen and unseen traits across groups on average—like shuffling cards so neither player systematically gets all the aces.

Mechanics:

* With true random assignment, treatment is independent of potential outcomes ⇒ unbiased estimate of causal effect.

* Stratified randomization (blocking) keeps key covariates balanced within strata (e.g., new vs. returning guests, mobile vs. desktop), increasing power.

Airbnb example:  
 When testing a new search filter panel, stratify by market (US/EU/APAC) and device to control known heterogeneity. This preserves randomization within each stratum and reduces variance.

---

### Block 55

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 8\) When A/B is insignificant — what to do next (a crisp playbook)

**Mapping:** score=0.61 reason=keyword:variance|head='8\) When A/B is insignificant — what to do next (a crisp playbook)'

Checklist (in order):

1. Power/MDE sanity check: Did we power for the effect we care about? If not, acknowledge inconclusive rather than “no effect.”

2. Data quality: Randomization balance checks (covariates), event logging, unit of analysis, bots, outliers.

3. Peeking / sequential bias: If monitored continuously, use alpha spending or group-sequential methods; otherwise p-value is inflated.

4. Variance reduction: Apply CUPED, covariate-adjusted regression.

5. Heterogeneous Treatment Effects: Look for pre-registered segments (device, market, new vs. returning). Avoid garden-of-forking-paths; if you explore, treat as hypothesis-generating.

6. Practical vs statistical significance: Even with p\>0.05, a tight CI centered near business threshold may justify ship → monitor.

7. Aggregate learning: Fold the result into a prior for a Bayesian or meta-analysis across similar tests (Airbnb often repeats similar UX patterns).

Airbnb example:  
 A new wishlist nudge shows (\\hat d \= \+0.2)pp (CI: −0.1 to \+0.5). Underpowered. You apply CUPED with pre-period add-to-wishlist; CI tightens to 0.0 to \+0.4. Business threshold is \+0.3pp; you decide to iterate UI and retest with better power.

---

### Block 56

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > 10\) Balancing speed vs precision when traffic is low

**Mapping:** score=0.61 reason=keyword:variance|head='10\) Balancing speed vs precision when traffic is low'

Toolbox:

* Raise MDE (be explicit with the business).

* Sequential designs (SPRT, group-sequential) to stop early for strong signals with proper error control.

* Bayesian tests with informative priors from past similar Airbnb experiments; decide on posterior probability of uplift \> threshold (e.g., (P(d\>0.3\\text{pp}\\mid \\text{data})\>0.9)).

* Pooled experiments / meta-analysis: run the same pattern across multiple markets and combine effects with partial pooling (hierarchical modeling).

* Variance reduction: CUPED, covariate regression, cluster-level blocking.

* Bandits: For short-run allocation efficiency (exploit winners faster) but remember: bandits optimize traffic; they’re not ideal for precise inference unless you use off-policy or doubly robust estimators.

Airbnb example:  
 Testing a new image gallery for low-traffic long-tail listings:

* Use hierarchical Bayesian logistic regression: listing-level random intercepts; treatment as fixed effect; pre-period CR as covariate.

* Borrow strength across listings/markets, yielding an actionable posterior on global and market-level lifts.

---

### Block 57

**Source:** `md`  
**Original headings:** Marketing Experimentation Framework > Extra depth you can flex in answers

**Mapping:** score=0.61 reason=keyword:variance|head='Extra depth you can flex in answers'

1\) Regression-adjusted A/B (GLM):  
 Fit (\\Pr(Y=1)=\\text{logit}^{-1}(\\beta\_0 \+ \\beta\_T T \+ \\beta^\\top X)). The coefficient (\\beta\_T) estimates treatment effect while reducing variance via covariates (X) (device, market, language, pre-period propensity). Use robust (HC) or cluster-robust SEs at the randomization unit.

2\) HTE responsibly:  
 Pre-register a small set of segments (e.g., new vs. returning guests, mobile vs. desktop). Consider Causal Forests / X-Learner to surface patterns, but validate in follow-ups to avoid overfitting.

3\) Guarding against p-hacking:

* Lock analysis plan; one-touch query; code review.

* If continuous monitoring is needed, use alpha spending (O’Brien-Fleming or Pocock boundaries).

4\) Multi-armed bandits in practice:

* UCB / Thompson Sampling to route more traffic to promising Airbnb variants (e.g., price-anchor copy) during exploration.

* For reporting, use inverse propensity weighting or self-normalized DR estimators to correct assignment bias and deliver an unbiased lift estimate.

---

### Block 58

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > The Very Basics

**Mapping:** score=0.61 reason=keyword:mean|head='The Very Basics'

1. Population – It is the entire group that you want to draw conclusions about. In statistics, a population is a set of similar items or events which is of interest for some question or experiment. In our example above, the true population is every future individual who will visit the web page.

2. Sample – A sample is a small portion of a population that is representative of the characteristics of the larger population. With statistical analysis, you can use data collected from samples to make estimates or test hypotheses about population. In A/B testing, a sample is the randomly selected set of visitors we display each of our page variations to – control is exposed to one sample and treatment is exposed to another.

3. Sample Mean – For a given metric, this is the mean or average based on data collected for the sample. For our A/B test example that is aiming to optimize CTR (click-through rate), this is nothing but the average CTR for users in each sample.

4. Sample Variability – Two randomly selected samples from a population may be different from each other. Whatever conclusions we are drawing about the population through a sample, because of sample variability, there is likely to be error in our estimations. Sampling variability will decrease as sample size increases. In A/B testing, the sampling variability affects the sample size we need in order to have a chance of deriving statistically significant results.

![][image7]![Image by Author][image8]Image by Author

---

### Block 59

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Sample size calculation

**Mapping:** score=0.61 reason=keyword:mean|head='Sample size calculation'

11. Confidence Level – Confidence level refers to the percentage or probability or certainty, that the confidence interval would contain the true population parameter when you draw a random sample many times. In the tech world of online A/B Testing, a 95% confidence level is chosen most often but you can choose different levels depending on the situation. A 95% confidence level means that the confidence interval around sample mean is expected to include the true mean value 95% of the time.

![][image10]

12. Margin of error – As we noted earlier, due to sampling variability, it is possible that the conclusions your draw about the population based on samples is inaccurate. A margin of error tells you how many percentage points your results will differ from the real population value. For example, a 95% confidence interval with a 4 percent margin of error means that your statistic will be within 4 percentage points of the real population value 95% of the time. The margin of error is added to and subtracted from the mean to determine the confidence interval (discussed below).

13. Confidence Interval – In statistical inference, we aim to estimate population parameters using observed sample data. A confidence interval gives an estimated range of values which is likely to include an unknown population parameter, the estimated range being calculated from a given set of sample data. The width of confidence interval depends on 3 things – the variation within the population of interest, the size of the sample and the confidence level we are seeking.

![][image11]![Image by Author][image12]Image by Author

14. Type 1 Error – A type I error occurs when we incorrectly reject the null hypothesis. In our A/B test example, a type I error would occur if we concluded that population mean of treatment is different from population mean of control when in reality they were the same. Type I error is avoided by achieving statistically significant results.

15. Type 2 Error – A type II error occurs when the null hypothesis is false, but we incorrectly fail to reject it. In our A/B test example, a type II error would occur if we concluded that the population mean of Variation B is not different than the mean of Variation A when it actually was different. These errors are avoided by running tests with a high statistical power.

![Image by Author][image13]Image by Author

16. P-value – p-value is the probability of obtaining at least as extreme results as we are seeing if the null hypothesis of the test is true. p-value basically tells you whether your evidence makes your null hypothesis look ridiculous.

17. Statistical Significance – Statistical significance is attained when the p-value is less than the significance level. The significance level (𝛂), is the threshold you want to use for the probability of making Type 1 error i.e. concluding that population mean of Control and Treatment are different when in fact they are the same. In other words, statistical significance is another way of saying that the p-value of a statistical test is small enough to reject the null hypothesis. The scientific standard is to use a p-value \< 0.05 i.e. 𝛂 \= 5%.

18. Statistical Power – Statistical Power, which as we know is the probability that a test correctly rejects the null hypothesis i.e. the percentage of time the minimal effect will be detected, if it exists.

19. Minimum Detectable Effect (MDE) – is the smallest change in conversion rate you are interested in detecting. In the example where you are optimizing for CTR, let’s say the CTR for the control is 20%. And the smallest change you would like to detect at the minimum is 5% absolute lift relative to control i.e. if the CTR for the treatment is 25% or more. In this case 5% is the MDE.

20. Practically significant – It’s possible for hypothesis tests to produce results that are statistically significant, despite having a small effect size. This usually happens due to 2 reasons – 1\) Low sampling variance and 2\) Large sample size. In both these cases, we may be able to detect even small differences between test and control with statistical significance. However, these may not be significant in the real world. Let’s take an example of an A/B test which shows a new module to users and is able to detect a difference of .05% in the CTR – however, is that cost of building that module justified for such a small lift. What is the practically significant lift that would be feasible in this case.

21. Sample size – The number of units per variation needed to reach statistical significance, given the baseline conversion, minimum detectable difference (MDE), significance level & statistical power chosen. ‘Duration’ refers to how long you need to run the test to reach adequate sample size per variation.

---

### Block 60

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > **Key Sections in Detail** > **1\. Purpose of Online Experiments**

**Mapping:** score=0.61 reason=keyword:mean|head='**1\. Purpose of Online Experiments**'

Online Controlled Experiments enable organizations to make **data-informed decisions**, not just data-inspired. The authors emphasize that even well-meaning assumptions often lead to incorrect decisions. For example, the book cites multiple real-world experiments where changes that were expected to help—such as visual redesigns—actually hurt engagement or revenue.

Online experiments are the only reliable way to estimate **causal impact** on real users at scale, making them a gold standard in modern product development.

---

### Block 61

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > Core Concepts of Hypothesis Testing > **The Most Important Concept: Standard Deviation of the Mean**

**Mapping:** score=0.61 reason=keyword:mean|head='**The Most Important Concept: Standard Deviation of the Mean**'

The book emphasizes one concept as the key to understanding statistical significance: **we do not care about the standard deviation of our individual data points, but rather the standard deviation of the *average value* of all our measurements**.

This "standard deviation of the average" decreases as you take more measurements. The source provides a detailed visual analogy using dice rolls to explain this:

* **Rolling 1 Die**: The probability of getting a 1, 2, 3, 4, 5, or 6 is equal.  
* **Rolling 2 Dice**: When you sum the values of two dice, outcomes are more concentrated in the middle. A sum of 7 is the most likely outcome, while 2 or 12 are the least likely.  
* **Rolling More Dice**: As you add more dice, the probability distribution of the *sum* (and therefore the *average*) becomes even more concentrated around the central value of 3.5.

The source includes a visual representation of this principle: **Probability Distribution of the Average Value for 1, 2, and 3 Dice** 

\*(The source describes a plot showing that as the number of dice increases, the probability of getting an average value far from the center (3.5) decreases dramatically, and the distribution becomes narrower and more peaked at the center.)\*

This narrowing of the distribution means the **standard deviation of the average decreases as the number of samples increases**. This relationship is defined by the formula:

**Standard Deviation of the Average \= σ / √n**

Where **σ (sigma)** is the population standard deviation and **n** is the number of samples. This formula is a cornerstone of nearly every statistical significance equation in the book. It also demonstrates that there are **diminishing returns** to collecting more data; early samples reduce the standard deviation of the average significantly, but it takes more and more data to achieve the same reduction later on.

---

### Block 62

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > The General Hypothesis Testing Process

**Mapping:** score=0.61 reason=keyword:standard deviation|head='The General Hypothesis Testing Process'

For every example, the book follows a consistent two-step process:

1. **Determine how many standard deviations the outcome is from the average outcome** (by calculating a test statistic like a Z-score or T-value).  
2. **Look up that value in a probability table (like a Z-Table or T-Table) to find the p-value**, which represents the probability that the outcome occurred by random chance.

---

### Block 63

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Hypothesis Testing: A Visual Introduction To Statistical Significance. > In-Depth Instructions for Each Test Type > **T-Tests: When the Population Standard Deviation is Unknown**

**Mapping:** score=0.61 reason=keyword:standard deviation|head='**T-Tests: When the Population Standard Deviation is Unknown**'

A **T-Test** is used when the population standard deviation is unknown and must be calculated from the sample data. This introduces uncertainty, so the T-test uses a distribution that accounts for the sample size through **degrees of freedom (df)**.

* With fewer samples (low df), the T-distribution is more spread out, putting more probability in the tails to account for the uncertainty.  
* As the sample size (and df) increases, the T-distribution becomes nearly identical to the standard normal (Z) distribution.

---

### Block 64

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Next-Level A/B Testing: Repeatable, Rapid, and Flexible Product Experimentation > In-Depth Summary of Key Topics > **Chapters 2 & 3: Improving Experimentation Rate and Design**

**Mapping:** score=0.61 reason=keyword:variance|head='**Chapters 2 & 3: Improving Experimentation Rate and Design**'

These chapters focus on increasing testing throughput and efficiency.

• Varying Testing Strategies:

    \- Isolated Testing: Users are in only one experiment at a time. This provides high precision but limits capacity, making it ideal for high-stakes tests like measuring ad revenue impact.

    \- Overlapping Testing: Users can be in multiple, non-interfering experiments at once. This increases the testing rate but carries the risk of interaction effects. The source describes a "layers" system (e.g., UX layer, Search layer) inspired by Google to manage which experiments can safely overlap.

    \- Sequential Testing: Allows for "peeking" at results and stopping a test early if it shows a strong positive or negative effect, freeing up resources faster.

    \- Multivariate Testing: Evaluates multiple changes and their combinations within a single experiment, useful for holistic design optimization but requires larger sample sizes.

• Designing Better Experiments:

    \- The Gold Standard: The book proposes establishing clear criteria for what constitutes a well-designed experiment, covering both technical configuration (hypothesis, power analysis, etc.) and the user-facing product experience.

    \- Sensitive Metrics: Using more sensitive feature-level metrics (e.g., click-through rate) that are proxies for high-level company metrics (e.g., retention) can provide faster insights with smaller sample sizes. This section also explains the concept of Minimal Detectable Effect (MDE).

    \- Variance Reduction: The source details techniques to increase statistical power:

        ▪ Capping Metrics: Limiting the influence of extreme outliers (e.g., capping revenue at a certain threshold) to reduce variance.

        ▪ CUPED (Controlled Experiment Using Pre-experiment Data): Using historical user data to reduce variability in metrics and increase precision.

    \- Aligning on Goals: Experiments should be categorized based on their goal—such as Test to learn, Test to derisk, or Test to measure—as this influences the optimal design and duration. The source includes a visual hierarchy of these test types.

---

### Block 65

**Source:** `md`  
**Original headings:** 25 A/B Testing Concepts You Must Know: Interview Refresher > Ace A/B Testing Interview Question: A Data-driven Approach for Data Scientists > How to Answer Design Questions

**Mapping:** score=0.61 reason=keyword:mean|head='How to Answer Design Questions'

Now, going back to our question on how to design a test to test a new change, my tip for you is to provide a summary before you dive into the details of designing the test. What do I mean by that? Well, my suggestion is you can provide a summary at the beginning before getting into the details. You can say something like designing an AB test involves multiple steps such as choosing the right metrics, selecting the right randomization unit, calculating the sample size and test duration, as well as determining the minimum detectable effect. So which component would you like me to dive into?

So the idea is that you provide a high level summary about different components that are involved. in designing a test before talking about the details of each component. So why do I recommend this approach? There are two main benefits to using this method. The first benefit is that it provides a structure for your answer. By mentioning different components or different steps involved in designing a test, you let the interviewer know that you have knowledge on designing a test. It'll not only showcase you have knowledge, but also indicate you have the confidence to dive into any component.

Another benefit is that it allows the interviewer to choose which component they want to hear about. They may be interested in choosing the right metric or determining the right randomization unit, calculating the sample size, et cetera. When you provide options for them, they can choose which part to dive into. It will be easier for them to get the strong signal about your qualification, especially when the time is limited. Essentially, you are making their job easier by providing this summary and the option at the beginning of your answer.

Now let's do a quick recap.

---

### Block 66

**Source:** `md`  
**Original headings:** What is product experimentation? How to build, test, and scale smarter. > Step-by-step guide to running an experiment > 3\. Estimate sample size and minimum detectable effect (MDE)

**Mapping:** score=0.61 reason=keyword:mean|head='3\. Estimate sample size and minimum detectable effect (MDE)'

There are few things worse than running a test and realizing afterward that you didn’t have enough traffic to detect a meaningful result.

* Calculate your sample size: Use online calculators to estimate how many users you’ll need for statistical confidence.

* Determine your MDE: What’s the smallest uplift that would be worth acting on? A 0.5% lift might not justify the dev work, but a 5% lift would.

---


