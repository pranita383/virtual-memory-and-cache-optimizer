class LRUCache:
    def __init__(self, size):
        self.size = size
        self.cache = {}
        self.order = []
    
    def access_page(self, page):
        if page in self.cache:
            self.order.remove(page)
            self.order.append(page)
            return True
        else:
            if len(self.cache) >= self.size:
                least_recently_used = self.order.pop(0)
                del self.cache[least_recently_used]
            self.cache[page] = True
            self.order.append(page)
            return False

class CacheSimulator:
    @staticmethod
    def simulate_cache(cache, pages):
        hits = 0
        misses = 0
        
        for page in pages:
            if cache.access_page(page):
                hits += 1
            else:
                misses += 1
        
        return hits, misses
