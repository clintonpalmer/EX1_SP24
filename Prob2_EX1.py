from Prob1_EX1 import statistics
from hw3b import distribution
import math

num_cycles = 11
tot_per_sample = 100

#Supplier A
def supplier_A():
    # Size range of rocks
    lower_bound = .375
    upper_bound = 1.0
    mean = (upper_bound + lower_bound) / 2
    std_dev = (upper_bound - lower_bound) / 6
    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample, lower_bound, upper_bound)
    print(f"Supplier A:\n Mean of sampling means: {mean_of_sampling_means:.6f}\n Variance of Sampling Means: {variance_of_sampling_means:.6f}")
    return mean_of_sampling_means, variance_of_sampling_means

#supplier_A() # for debugging

def supplier_B():
    lower_bound = 0
    upper_bound = 0.875
    mean = (upper_bound + lower_bound) / 2
    std_dev = (upper_bound - lower_bound) / 6

    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample, lower_bound, upper_bound)
    print(f"Supplier B:\n Mean of sampling means: {mean_of_sampling_means:.6f}\n Variance of Sampling Means: {variance_of_sampling_means:.6f}")
    return mean_of_sampling_means, variance_of_sampling_means

#supplier_B()  # for debugging

def stat_analysis(num_cycles):
    mean_A, var_A = supplier_A()
    mean_B, var_B = supplier_B()
    # pooled_se = pooled_std_error(var_A, var_B, num_cycles, num_cycles)

    # Calculate the t-statistic
    Sp = math.sqrt((99) * mean_A ** 2 + (99) * mean_B ** 2) / 198
    t_stat = (mean_A - mean_B)  / (Sp * math.sqrt(1 / 100 + 1 / 100))
    print (f"t_stat = {t_stat}")
    # Calculate the degrees of freedom
    df = num_cycles - 1

    # Calculate the p-value
    p_val = 1- distribution(df, (t_stat))
    print(f"Probability = {p_val}")

    # Check if the null hypothesis is rejected or accepted
    alpha = 0.05
    #degrees of freedom = 10
    # critical value c or z = 1.81
    if p_val < alpha:
        print("We reject the null hypothesis. Supplier B produces statistically significantly smaller numbers than Supplier A.")
    else:
        print("We accept the null hypothesis. Supplier B does not produce statistically significantly smaller numbers than Supplier A.")

stat_analysis(num_cycles)


