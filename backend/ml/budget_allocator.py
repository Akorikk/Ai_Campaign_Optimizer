import numpy as np

def allocate_budget(channel, total_budget):

    # simulated channel performance weights
    performance = {
        "LinkedIn": 0.5,
        "Indeed": 0.3,
        "Facebook": 0.2
    }

    # normalize weights
    weights = np.array(list(performance.values()))
    weights = weights / weights.sum()

    channels = list(performance.keys())

    allocation = {}

    for i, ch in enumerate(channels):
        allocation[ch] = round(total_budget * weights[i], 2)

    return allocation