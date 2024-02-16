from Prob1_EX1 import statistics

#Supplier A
def supplier_A():
    num_cycles = 11
    tot_per_sample = 100
    mean = (1 + 0.375) / 2
    std_dev = (1 - 0.375) / 6
    # Size range of rocks
    lower_bound = 0.375
    upper_bound = 1
    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample, lower_bound, upper_bound)
    print(f"Supplier A:\n Mean of sampling means: {mean_of_sampling_means}\n Variance of Sampling Means: {variance_of_sampling_means}")
    return mean_of_sampling_means, variance_of_sampling_means

supplier_A()

def supplier_B():
    num_cycles = 11
    tot_per_sample = 100
    lower_bound = 0
    upper_bound = 0.875
    mean = (upper_bound + lower_bound) / 2
    std_dev = (upper_bound - lower_bound) / 6

    results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample, lower_bound, upper_bound)
    print(f"Supplier B:\n Mean of sampling means: {mean_of_sampling_means}\n Variance of Sampling Means: {variance_of_sampling_means}")
    return mean_of_sampling_means, variance_of_sampling_means

supplier_B()