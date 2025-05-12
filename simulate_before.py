import random
import time

# Function to simulate memory access
def simulate_memory_access(memory_size, access_pattern, cache_size=5):
    memory = list(range(memory_size))  # Simulated memory pages
    cache = []
    page_faults = 0

    for page in access_pattern:
        if page not in cache:
            if len(cache) < cache_size:
                cache.append(page)
            else:
                cache.pop(0)
                cache.append(page)
            page_faults += 1
    return page_faults

# Generate random memory access pattern
def generate_access_pattern(memory_size, num_accesses):
    return [random.randint(0, memory_size - 1) for _ in range(num_accesses)]

# Simulate before optimization
def simulate_before():
    memory_size = 100  # Size of the simulated memory
    access_pattern = generate_access_pattern(memory_size, 100)  # Generate random access pattern
    cache_size = 5  # Cache size
    
    page_faults = simulate_memory_access(memory_size, access_pattern, cache_size)
    
    return page_faults

if __name__ == "__main__":
    page_faults_before = simulate_before()
    print(f"Page faults before optimization: {page_faults_before}")
