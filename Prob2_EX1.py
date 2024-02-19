#
# When Problem 1 rock population is set to 5 million, the code runs for about 3 minutes.
# Assumptions:
#      Supplier A and Supplier B provide the same number rocks per sample.
#          This is critical for the t_stat calculation. It has been simplified
#          to reflect this assumption.
#               See Kreyszig's "Advanced Engineering Mathematics" 10th ed. section 25.4
#                   formula (11) simplifies to formula (12) when population size is the
#                   same for each sample.
#      Specific Mean of Supplier A is the center of the acceptable range = 0.6875
#      Specific Mean of Supplier B is the center of the acceptable range = 0.4375
#      The rocks are normally distributed over +/- 3 standard deviations for each supplier.
# Information:
#      The t_stat variable uses the "Mean of sampling means" and the "Variance
#          of sampling means", derived by Prob1_EX1.py, to perform its calculation.

from Prob1_EX1 import statistics
from hw3b import distribution
import math

num_cycles = 11
tot_per_sample = 100

def supplier_A():
    """
    This function sets the initial conditions of the samples to be taken, then calls the statistics function
    from Prob1_EX1.py to generate data for the t_test calculation
    :       mean: the average of the normally distributed sizes
    :    std_dev: the variability of normally distributed rock sizes with respect to the mean
    :     return: the data that returns from the statistics function is then delivered to the variables mean_A, var_A
    :             in the stat_analysis function.
    Gemini assisted with the development of this function
    """
    mean = (1 + 0.375) / 2
    std_dev = (1 - 0.375) / 6
    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample)
    print(f"Supplier A:\n   Mean of sampling means: {mean_of_sampling_means:.6f}\n   Variance of Sampling Means: {variance_of_sampling_means:.6f}")
    return mean_of_sampling_means, variance_of_sampling_means
#supplier_A() # for debugging

def supplier_B():
    """
    This function sets the initial conditions of the samples to be taken, then calls the statistics function
    from Prob1_EX1.py to generate data for the t_test calculation
    :       mean: the average of the normal distribution.
    :    std_dev: the variability of normally distributed rock sizes with respect to the mean
    :     return: the data that returns from the statistics function is then delivered to the variables mean_B, var_B
    :             in the stat_analysis function
    Gemini assisted with the development of this function
    """
    mean = 0.875 / 2
    std_dev = 0.875 / 6
    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample)
    print(f"Supplier B:\n   Mean of sampling means: {mean_of_sampling_means:.6f}\n   Variance of Sampling Means: {variance_of_sampling_means:.6f}")
    return mean_of_sampling_means, variance_of_sampling_means
#supplier_B()  # for debugging

def stat_analysis(num_cycles):
    """
    This function retrieves the mean of sampling means and variation of sampling means for Supplier A and
    Supplier B.  These values are then used to calculate t statistic value (similar to z-score). This value
    is then paired with the degrees of freedom, sent to the distribution function to calculate the probability.
    If the distribution function returns a probability > the claimed significance level (alpha), the result
    will be to accept the null hypothesis and reject the claim.  If prob < alpha, the null hypothesis is rejected,
    and the claim is now supported with data.
    :p_val:  is the probability the claim is true
    :t_stat:  see Kreyszig's "Advanced Engineering Mathematics" 10th ed. section 25.4 formula (11) simplifies to
               formula (12) when population sizes are the same for each sample
    :df:  sample size * number of samples - number of samples
    :num_cycles: is number of rocks per sample, used by the t_stat calculation.
    :return:  prints the results of the statistical analysis. If the probability is less than or greater than alpha,
              the corresponding print statement is sent to the CLI.
    Gemini assisted with the development of this function
    """
    mean_A, var_A = supplier_A()
    mean_B, var_B = supplier_B()

#   see Kreyszig's "Advanced Engineering Mathematics" 10th ed. section 25.4
#   formula (11) reduces to formula (12) when population sizes are the same for each sample
    t_stat = math.sqrt(num_cycles) * ((mean_A - mean_B) / math.sqrt(var_B + var_A))
    print (f"t_stat = {t_stat}")

#   degrees of freedom = sample size * number of samples - number of samples
    df = tot_per_sample * 2 - 2

    p_val = 1 - distribution(df, t_stat)
    print(f"Probability = {p_val}")

    alpha = 0.05
    # degrees of freedom = 198
    # critical value = 1.65
    if p_val < alpha:
        print("We reject the null hypothesis. Supplier B produces statistically significantly smaller numbers than Supplier A.")
    else:
        print("We accept the null hypothesis. Supplier B does not produce statistically significantly smaller numbers than Supplier A.")

stat_analysis(num_cycles)


