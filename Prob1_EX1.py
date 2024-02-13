import random

# Constants
N = 100  # Number of rocks in each sample
num_samples = 11  # Number of samples

def simulate_rock_sizes(mean, std_dev, num_rocks):
    """
     This function generates a list of rock sizes by drawing random samples from a
     normal distribution with a specified (assumption) mean and standard deviation.
     The number of rock sizes generated is determined by the `num_rocks` parameter.
     :param mean: The mean (average) size of the rocks. This is the center of the
                    normal distribution from which the rock sizes are drawn.
     :param std_dev: The standard deviation of the rock sizes. This is a measure
                    of how much the sizes of the rocks vary around the mean. It
                    determines the width of the normal distribution from which
                    the rock sizes are drawn.
     :param num_rocks: The number of rock sizes to generate.
     :return: A list of `num_rocks` rock sizes, each drawn from a normal distribution
                with the specified `mean` and `std_dev`.
     chatgpt assisted in developing this function
     """
    return [random.gauss(mean, std_dev) for _ in range(num_rocks)]

# mean assumption, standard deviation assumption, and amount of rock in pile of rocks
rock_sizes = simulate_rock_sizes(0.75, 0.1, int(1e6))

# Filter the rocks that are too big for a 1"x1" screen and too small for a 3/8"x3/8" screen
filtered_rock_sizes = [rock for rock in rock_sizes if 3/8 < rock < 1]

# Function to draw samples of rocks
def draw_samples(population, num_samples, sample_size):
    """
    This function generates a list of samples by drawing random subsets from a given population.
    The number of samples and the size of each sample are determined by the `num_samples` and
    `sample_size` parameters, respectively.
    :param population: The population from which to draw the samples. This should be a list or
                        other iterable containing the individual elements of the population.
    :param num_samples: The number of samples to draw from the population.
    :param sample_size: The size of each sample. This is the number of elements from the population
                        to include in each sample.
    :return: A list of `num_samples` samples, each of which is a list of `sample_size` elements drawn
            from the `population`.
    chatgpt assisted in developing this function
    """
    return [random.sample(population, sample_size) for _ in range(num_samples)]

# Draw 11 samples of 100 rocks
samples = draw_samples(filtered_rock_sizes, num_samples, N)

# Function to calculate the mean and variance of a sample
def calculate_stats(sample):
    """
    This function calculates the mean (average) and variance of a given sample. The mean
    is calculated as the sum of the sample values divided by the number of values. The
    variance is calculated as the sum of the squared differences between each sample value
    and the mean, divided by the number of values minus 1.
    :param sample: The sample for which to calculate the mean and variance.
    :return: A tuple containing the mean and variance of the sample.
    chatgpt assisted in developing this function
    """
    mean = sum(sample) / len(sample)
    variance = sum((x - mean) ** 2 for x in sample) / (len(sample) - 1)
    return mean, variance


# Calculate the sample means and variances
sample_stats = [calculate_stats(sample) for sample in samples]
sample_means, sample_variances = zip(*sample_stats)

# Calculate the mean and variance of the sampling mean
mean_of_sampling_mean, variance_of_sampling_mean = calculate_stats(sample_means)

# Print the results
for i in range(num_samples):
    print(f"Sample {i+1}: Mean = {sample_means[i]:.4f}, Variance = {sample_variances[i]:.8f}")
print(f"Mean of Sampling Mean = {mean_of_sampling_mean:.5f}, Variance of Sampling Mean = {variance_of_sampling_mean:.8f}")
