#
# Assumption: The specific mean of the normal distribution is centered in the
#             range of acceptable size rocks.
# Assumption: The range is broken into 6 sections (standard deviations) with
#             + or - 3 standard deviations representing 99.7% of the possible numbers
#             in the appropriate range. I also added a check to ensure the samples only included
#             rocks in the specified range. (The sieving technology is assumed to be excellent)

import random

mean = (1 + 0.375) / 2
std_dev = (1 - 0.375) / 6

# Size range of rocks
lower_bound = 0.375
upper_bound = 1

def generate_data():
    """
    This function produces 100 rocks in the desired size range.
    :data: Generates a random normal distribution of numbers.
    :while:  Simulates the sieving process, ensuring all rocks in a sample
             are within the specified size range.
    The while loop runs when a rock size is determined to be out of range.
    The batch is checked to ensure all rocks are within the lower and upper bound; if not,
    the "while loop" conditions are true, and a normal distribution of
    100 rocks is generated, this process continues to repeat until all 100 rocks are within
    the lower and upper bound.
    """
    data = [random.normalvariate(mean, std_dev) for _ in range(100)]
    while any(x < lower_bound or x > upper_bound for x in data):
        data = [random.normalvariate(mean, std_dev) for _ in range(100)]
#    print(data) #for debugging
    return data

def calculate_statistics(data):
    """Calculates sample mean and variance:
    :data: A list of numeric values representing a sample.
    :sample_mean: The sample mean is the average of the data points.
                    x̄ = ( Σ xi ) / n
    :sample_variance: The sample variance measures how much the data points deviate from the mean.
                    s² = Σ (xi - x̄)² / (n - 1)
    Returns:
        tuple: A tuple containing the sample mean and sample variance.
    """
    sample_mean = sum(data) / len(data)
    sample_variance = sum((x - sample_mean) ** 2 for x in data) / (len(data) - 1)

        #print(f"Sample {i+1} Mean: {sample_mean:.4f}")
        #print(f"Sample {i+1} Variance: {sample_variance:.4f}")

    return sample_mean, sample_variance

num_cycles = 11 # 11 samples generated
sampling_means = []
sampling_variances = []

for i in range(num_cycles):
    data = generate_data()
    sample_mean, sample_variance = calculate_statistics(data)
    sampling_means.append(sample_mean)
    sampling_variances.append(sample_variance)
    print(f"Sample {i+1} Mean: {sample_mean:.4f}")
    print(f"Sample Variance: {sample_variance:.4f}")

mean_of_sampling_means = sum(sampling_means) / num_cycles
variance_of_sampling_means = sum((x - mean_of_sampling_means) ** 2 for x in sampling_means) / (num_cycles - 1)

print(f"Mean of Sampling Mean: {mean_of_sampling_means:.4f}")
print(f"Variance of Sampling Mean: {variance_of_sampling_means:.8f}")
