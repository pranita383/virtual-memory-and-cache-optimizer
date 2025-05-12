import random
import time

# Function to simulate memory access with optimized cache strategy (e.g., LRU or Optimal)
def simulate_memory_access_optimized(memory_size, access_pattern, cache_size=5):
    memory = list(range(memory_size))  # Simulated memory pages
    cache = []
    page_faults = 0

    for page in access_pattern:
        if page not in cache:
            if len(cache) < cache_size:
                cache.append(page)
            else:
                # LRU Cache Eviction
                cache.pop(0)
                cache.append(page)
            page_faults += 1
        else:
            cache.remove(page)
            cache.append(page)  # Mark the page as recently used
    
    return page_faults

# Generate random memory access pattern
def generate_access_pattern(memory_size, num_accesses):
    return [random.randint(0, memory_size - 1) for _ in range(num_accesses)]

# Simulate after optimization
def simulate_after():
    memory_size = 100  # Size of the simulated memory
    access_pattern = generate_access_pattern(memory_size, 100)  # Generate random access pattern
    cache_size = 5  # Cache size
    
    page_faults = simulate_memory_access_optimized(memory_size, access_pattern, cache_size)
    
    return page_faults

if __name__ == "__main__":
    page_faults_after = simulate_after()
    print(f"Page faults after optimization: {page_faults_after}")
