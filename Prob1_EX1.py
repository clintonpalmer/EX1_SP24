#
# The code runs for about 1 minute when the rock population is set to 5 million.
# see line 29 to change rock population if needed.
# Unblock section at bottom to generate output
# Block section at bottom before running Problem 2
#
# Assumptions: The specific mean of the normal distribution is centered in the
#              range of acceptable size rocks.
#              The range is broken into 6 sections (standard deviations) with
#              +/- 3 standard deviations representing 99.7% of possible rock
#              sizes.

import random
num_cycles = 11
tot_per_sample = 100
mean = (1 + 0.375) / 2
std_dev = (1 - 0.375) / 6

def collect_population(mean, std_dev, tot_per_sample):
    """
    This function simulates the post sieving process that produced a normally distributed pile of rocks.
    Although a rock is unlikely to be outside the specified range, I added a filter process that inspects
    each rock to ensure it is in the suppliers expected size range.
    :rock_population: Generates a random normal distribution of rocks using specified mean and standard deviation.
    :collect_rocks: Extracts 100 random size rocks into a list
    :return:  the sizes of rocks are put into a list and returned to the variable "data" in the statistics function.
    Gemini assisted in developing this function
    """
    rock_population = [random.normalvariate(mean, std_dev) for _ in range(5000000)]
    collect_rocks = random.sample(rock_population, tot_per_sample)

#   print(collect_rocks) #for debugging
    return collect_rocks

def calculate_statistics(data):
    """
    Calculates sample mean and variance:
    :data: contains the rock population (data points).
    :sample_mean: the sum of the data points divided by the total number of points.
                    x̄ = ( Σ xi ) / n
    :sample_variance: The measure of the variability from the sample mean.
                    s² = Σ (xi - x̄)² / (n - 1)
    Returns:
        the sample mean and sample variance.
    Gemini assisted in developing this function
    """
    sample_mean = sum(data) / len(data)
    sample_variance = sum((x - sample_mean) ** 2 for x in data) / (len(data) - 1)
    return sample_mean, sample_variance

def statistics(mean, std_dev, num_cycles, tot_per_sample):
    """
    This function generates statistics on a random, normally distributed population of rocks, stores the
    data in a list as (mean, variance),..., then calculates the mean of the sampling means and variance of the
    sampling means, then outputs the results of the statistics to the CLI.
    :lower_bound: minimum allowable size defined by supplier
    :upper_bound: maximum allowable size defined by supplier
    :       mean: the average of the normally distributed sizes
    :    std_dev: the variability of normally distributed rock sizes with respect to the mean
    : num_cycles: total number of samples taken
    :tot_per_sample: number of rocks per sample
    :     return: 100 rocks are sampled 11 times. The "sample mean" and "sample variance" for
    :                 each of the 11 samples are returned, then the "Mean of sampling means" and
    :                 "Variance of sampling means" are returned
    Gemini assisted in developing this function
    """
    n = num_cycles
    sampling_means = []
    sampling_variances = []
    results = []

    for i in range(n):
        data = collect_population(mean, std_dev, tot_per_sample)
        sample_mean, sample_variance = calculate_statistics(data)
        sampling_means.append(sample_mean)
        sampling_variances.append(sample_variance)
        results.append((sample_mean, sample_variance))

    mean_of_sampling_means = sum(sampling_means) / n
    variance_of_sampling_means = sum((x - mean_of_sampling_means) ** 2 for x in sampling_means) / (num_cycles - 1)

    return results, mean_of_sampling_means, variance_of_sampling_means


results, mean_of_sampling_means, variance_of_sampling_means = statistics(mean, std_dev, num_cycles, tot_per_sample)



#  Unblock this section to generate an output for this code
#  Block this section for problem 2
##########################################################################
for i, result in enumerate(results):
    print(f"Sample {i + 1} ")
    print(f"    Mean: {result[0]:.4f}, Variance: {result[1]:.4f}")

print(f"\nMean of Sampling Means: {mean_of_sampling_means:.4f}")
print(f"Variance of Sampling Means: {variance_of_sampling_means:.8f}")
statistics(mean, std_dev, num_cycles, tot_per_sample)
##########################################################################

