# Sample Size Formulas

This document provides clear mathematical formulas used by the **Sample Size Calculator** application. These formulas cover the four most common scenarios encountered in statistical testing and experimentation:

---

### 1. Comparing Two Means (A/B Testing)

Use this formula to calculate the required sample size when comparing two means (continuous outcomes) from two independent groups:

$$
n = \frac{2\sigma^2(Z_{\alpha/2} + Z_{\beta})^2}{\Delta^2}
$$

where:
- $n$ = required sample size per group
- $\sigma^2$ = pooled variance
- $\Delta$ = minimum detectable difference (effect size)
- $Z_{\alpha/2}$ = critical z-value for significance level (two-tailed test)
- $Z_{\beta}$ = z-value for statistical power

---

### 2. Comparing Two Proportions (A/B Testing)

Use this formula to calculate the required sample size when comparing two independent proportions:

$$
n = \frac{(Z_{\alpha/2} + Z_{\beta})^2 \left[p_1(1 - p_1) + p_2(1 - p_2)\right]}{(p_1 - p_2)^2}
$$

where:
- $n$ = required sample size per group
- $p_1$ and $p_2$ = expected proportions for each group
- $Z_{\alpha/2}$ = critical z-value for significance level (two-tailed test)
- $Z_{\beta}$ = z-value for statistical power

---

### 3. Estimating a Single Mean

Use this formula to calculate the sample size required to estimate a single mean within a desired margin of error:

$$
n = \left(\frac{Z_{\alpha/2} \, \sigma}{E}\right)^2
$$

where:
- $n$ = required sample size
- $\sigma$ = standard deviation of the population
- $E$ = margin of error (absolute value)
- $Z_{\alpha/2}$ = critical z-value for significance level (two-tailed test)

---

### 4. Estimating a Single Proportion

This formula calculates the sample size needed when estimating a single proportion within a given margin of error:

$$
n = \frac{Z_{\alpha/2}^2 \, p(1 - p)}{E^2}
$$

where:
- $n$ = required sample size
- $p$ = estimated proportion
- $E$ = margin of error (absolute value)
- $Z_{\alpha/2}$ = critical z-value for significance level (two-tailed test)

---

For further information and practical examples, please refer to the main [README.md](../README.md) of this repository.

---

🔙 [**Return to Main README.md**](../README.md)
