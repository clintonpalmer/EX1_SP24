
# Assumptions and Information:
#      Supplier A and Supplier B provide the same number rocks per sample.
#          This is critical for the t_stat calculation. It has been simplified
#          to reflect this assumption.
#               See Kreyszig's "Advanced Engineering Mathematics" 10th ed. section 25.4
#                   formula (11) reduces to formula (12) when population sizes are the
#                   same for each sample.
#      Specific Mean of Supplier A is the center of the acceptable range = 0.6875
#      Specific Mean of Supplier B is the center of the acceptable range = 0.4375
#      The rocks are normally distributed over +/- 3 standard deviations for each supplier.
#      The "sieving" process rejects ALL unwanted rock sizes.
#      The t_stat variable uses the "Mean of sampling means" and the "Variance
#          of sampling means", derived by Prob1_EX1.py, to perform its calculation.

from Prob1_EX1 import statistics
from hw3b import distribution
import math

num_cycles = 11
tot_per_sample = 100

def supplier_A():
    """
    :lower_bound: minimum allowable size defined by supplier
    :upper_bound: maximum allowable size defined by supplier
    :       mean: the average of the normally distributed sizes
    :    std_dev: the variability of normally distributed rock sizes with respect to the mean
    :             1 standard deviation =
    :     return: 100 rocks are sampled 11 times. The mean and variance of the
    :                 of the 11 samples are returned.
    """
    #Size range of rocks
    lower_bound = .375
    upper_bound = 1.0
    mean = (upper_bound + lower_bound) / 2
    std_dev = (upper_bound - lower_bound) / 6
    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample, lower_bound, upper_bound)
    print(f"Supplier A:\n Mean of sampling means: {mean_of_sampling_means:.6f}\n Variance of Sampling Means: {variance_of_sampling_means:.6f}")
    return mean_of_sampling_means, variance_of_sampling_means
#supplier_A() # for debugging

def supplier_B():
    #Size range of rocks
    lower_bound = 0
    upper_bound = 0.875
    mean = (upper_bound + lower_bound) / 2
    std_dev = (upper_bound - lower_bound) / 6
    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample, lower_bound, upper_bound)
    print(f"Supplier B:\n Mean of sampling means: {mean_of_sampling_means:.6f}\n Variance of Sampling Means: {variance_of_sampling_means:.6f}")
    return mean_of_sampling_means, variance_of_sampling_means
#supplier_B()  # for debugging

def stat_analysis(num_cycles):
    """
    :df: number of taking 2 samples
    :param num_cycles:
    :return:
    """
    mean_A, var_A = supplier_A()
    mean_B, var_B = supplier_B()

#   see Kreyszig's "Advanced Engineering Mathematics" 10th ed. section 25.4
#   formula (11) reduces to formula (12) when population sizes are the same for each sample
    t_stat = math.sqrt(num_cycles) * ((mean_A - mean_B) / math.sqrt(var_B + var_A))
    print (f"t_stat = {t_stat}")

#   degrees of freedom = sample size * number of samples - number of samples
    df = tot_per_sample * 2 - 2

    p_val = 1 - distribution(df, t_stat)  # to find p-value
    print(f"Probability = {p_val}")

    # Check if the null hypothesis is rejected or accepted
    alpha = 0.05
    #degrees of freedom = 198
    # critical value c or z = 1.6526
    if p_val < alpha:
        print("We reject the null hypothesis. Supplier B produces statistically significantly smaller numbers than Supplier A.")
    else:
        print("We accept the null hypothesis. Supplier B does not produce statistically significantly smaller numbers than Supplier A.")

stat_analysis(num_cycles)


