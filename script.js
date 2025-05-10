document.getElementById('cacheForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const pages = document.getElementById('pages').value.split(',').map(page => page.trim());
    const cacheSize = parseInt(document.getElementById('cache_size').value);
    
    fetch('/simulate-cache', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ pages, cache_size: cacheSize })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('hits').textContent = `Hits: ${data.hits}`;
        document.getElementById('misses').textContent = `Misses: ${data.misses}`;
        document.getElementById('hit_ratio').textContent = `Hit Ratio: ${data.hit_ratio.toFixed(2)}`;
    })
    .catch(error => console.error('Error:', error));
});
