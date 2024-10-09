import streamlit as st
import math
import sys

a_twomeans = "docs/a.two_means.png"
b_twoprop = "docs/b.two_prop.png"
c_onemean = "docs/c.one_mean.png"
d_oneprop = "docs/d.one_prop.png"

# Functions for sample size calculations
def sample_size_comparing_two_means(variance, z_alpha, z_beta, delta):
    return math.ceil((2 * variance * (z_alpha + z_beta) ** 2) / (delta ** 2))

def sample_size_comparing_two_proportions(p1, p2, z_alpha, z_beta):
    numerator = (z_alpha + z_beta) ** 2 * ((p1 * (1 - p1)) + (p2 * (1 - p2)))
    denominator = (p1 - p2) ** 2
    return math.ceil(numerator / denominator)

def sample_size_estimating_mean(variance, z_alpha, margin_of_error):
    sigma = variance ** 0.5
    return math.ceil((z_alpha * sigma / margin_of_error) ** 2)

def sample_size_estimating_proportion(p, z_alpha, margin_of_error):
    return math.ceil((z_alpha ** 2 * p * (1 - p)) / (margin_of_error ** 2))

# Streamlit app code
def main():
    st.title("Sample Size Calculator")
    
    # Dropdown menu to select the type of calculation
    option = st.selectbox(
        "Choose a sample size calculator",
        [
            "Comparing Two Means (for AB Testing)",
            "Comparing Two Proportions (for AB Testing)",
            "Sampling a Population, Estimating the Mean",
            "Sampling a Population, Estimating a Proportion"
        ]
    )

    # Display the title for the selected calculator (without "Sample Size Calculator: " prefix)
    st.header(option)

    # Sidebar: Show the sample size formula
    st.sidebar.markdown("## Sample Size Calculator")
    st.sidebar.markdown(
        """
                    * LinkedIn: [linkedin.com/in/lucasbraga461](https://linkedin.com/in/lucasbraga461/)
                    * GitHub: [github.com/lucasbraga461/sample-size-calculator](https://github.com/lucasbraga461/sample-size-calculator/)
                    * Published article: [Mastering Sample Size Calculations @Towards Data Science](https://towardsdatascience.com/mastering-sample-size-calculations-75afcddd2ff3)
        """
    )
    if option == "Comparing Two Means (for AB Testing)":
        st.sidebar.write("# Comparing Two Means (for AB Testing)")
        st.sidebar.image(a_twomeans, use_column_width=True)
    elif option == "Comparing Two Proportions (for AB Testing)":
        st.sidebar.write("# Comparing Two Proportions (for AB Testing)")
        st.sidebar.image(b_twoprop, use_column_width=True)
    elif option == "Sampling a Population, Estimating the Mean":
        st.sidebar.write("# Sampling a Population, Estimating the Mean")
        st.sidebar.image(c_onemean, use_column_width=True)
    elif option == "Sampling a Population, Estimating a Proportion":
        st.sidebar.write("# Sampling a Population, Estimating a Proportion")
        st.sidebar.image(d_oneprop, use_column_width=True)
    
    # Confidence level mapping to z-values
    z_values_dict = {
        '90%': 1.645,
        '95%': 1.960,
        '99%': 2.576
    }

    # Z beta mapping for statistical power
    z_beta_dict = {
        '80%': 0.84,
        '90%': 1.28,
        '95%': 1.645
    }

    # Sidebar conversions between standard deviation and variance
    st.sidebar.header("Conversion Tools")

    # Convert from standard deviation to variance
    std_dev_to_var = st.sidebar.number_input("Convert Standard Deviation to Variance (σ to σ²):", min_value=0.0, step=0.01, key="std_dev_to_var")
    if std_dev_to_var > 0:
        st.sidebar.write(f"Variance (σ²): {std_dev_to_var ** 2:.2f}")

    # Convert from variance to standard deviation
    var_to_std_dev = st.sidebar.number_input("Convert Variance to Standard Deviation (σ² to σ):", min_value=0.0, step=0.01, key="var_to_std_dev")
    if var_to_std_dev > 0:
        st.sidebar.write(f"Standard Deviation (σ): {var_to_std_dev ** 0.5:.2f}")

    # Add Margin of Error Conversion Tool for historical metrics
    st.sidebar.header("Margin of Error Conversion")
    historical_value = st.sidebar.number_input("Enter the historical value of the metric (e.g., fraud rate, proportion):", value=1.0, step=0.01, format="%.6f")
    margin_of_error_percentage = st.sidebar.slider("Select the Margin of Error (%)", min_value=0, max_value=100, value=5, step=1)
    
    # Compute the lower and upper bounds of the metric
    E_interval = (margin_of_error_percentage / 100)
    lower_bound = historical_value * (1 - E_interval)
    upper_bound = historical_value * (1 + E_interval)
    margin_error_abs = upper_bound - historical_value
    
    st.sidebar.write(f"Lower Bound: {lower_bound:.6f}")
    st.sidebar.write(f"Upper Bound: {upper_bound:.6f}")
    st.sidebar.write(f"Margin of Error value: {margin_error_abs:.6f}")

    # Confidence Level Input (Smaller Heading)
    z_confidence_level = st.radio(
        'Choose a Confidence Level:',
        ('90%', '95%', '99%'), index=1
    )
    z_alpha = z_values_dict[z_confidence_level]
    st.write(f"Selected z-value for confidence level: {z_alpha}")

    # Display inputs and output based on user selection
    if option == "Comparing Two Means (for AB Testing)" or option == "Comparing Two Proportions (for AB Testing)":
        # Arrange "Statistical Power" right after "Confidence Level"
        power = st.radio('Choose Statistical Power:', ('80%', '90%', '95%'), index=0)
        z_beta = z_beta_dict[power]
        st.write(f"Selected z-value for statistical power: {z_beta}")

    if option == "Comparing Two Means (for AB Testing)":
        # Input variance only
        variance = st.number_input("Enter the variance (σ²)", value=1.0, key='variance')

        delta = st.number_input("Enter the difference you want to detect (δ)", value=0.5)

        if st.button("Calculate"):
            result = sample_size_comparing_two_means(variance, z_alpha, z_beta, delta)
            total_samples = result * 2
            st.success(f"The required sample size per group is: {result:,}, so if you have two groups (control and treatment), "
                       f"you need a total of {total_samples:,} samples.")
            st.write(f"Inputs: Variance (σ²) = {variance}, Difference to detect (δ) = {delta}, "
                     f"Z-value for Confidence = {z_alpha}, Z-value for Power = {z_beta}")

    elif option == "Comparing Two Proportions (for AB Testing)":
        # Input for proportions
        p1 = st.number_input("Enter the first proportion (p1)", value=0.5, format="%.6f")
        p2 = st.number_input("Enter the second proportion (p2)", value=0.4, format="%.6f")

        if st.button("Calculate"):
            result = sample_size_comparing_two_proportions(p1, p2, z_alpha, z_beta)
            total_samples = result * 2
            st.success(f"The required sample size per group is: {result:,}, so if you have two groups (control and treatment), "
                       f"you need a total of {total_samples:,} samples.")
            st.write(f"Inputs: Proportion 1 (p1) = {p1}, Proportion 2 (p2) = {p2}, "
                     f"Z-value for Confidence = {z_alpha}, Z-value for Power = {z_beta}")

    elif option == "Sampling a Population, Estimating the Mean":
        # Input variance only
        variance = st.number_input("Enter the variance (σ²)", value=1.0, key='variance_mean')

        # Input margin of error as an absolute value
        margin_of_error_absolute = st.number_input("Enter the margin of error as an absolute value", value=0.01, format="%.6f")

        if st.button("Calculate"):
            result = sample_size_estimating_mean(variance, z_alpha, margin_of_error_absolute)
            st.success(f"The required sample size is: {result:,}")
            st.write(f"Inputs: Variance (σ²) = {variance}, Margin of Error = {margin_of_error_absolute:.6f}, "
                     f"Z-value for Confidence = {z_alpha}")

    elif option == "Sampling a Population, Estimating a Proportion":
        # Adjust input for proportion to show 6 digits after the comma
        p = st.number_input("Enter the proportion (p)", value=0.5, format="%.6f")

        # Input margin of error as an absolute value
        margin_of_error_absolute = st.number_input("Enter the margin of error as an absolute value", value=0.01, format="%.6f")

        if st.button("Calculate"):
            result = sample_size_estimating_proportion(p, z_alpha, margin_of_error_absolute)
            st.success(f"The required sample size is: {result:,}")
            st.write(f"Inputs: Proportion (p) = {p}, Margin of Error = {margin_of_error_absolute:.6f}, "
                     f"Z-value for Confidence = {z_alpha}")

if __name__ == "__main__":
    main()
