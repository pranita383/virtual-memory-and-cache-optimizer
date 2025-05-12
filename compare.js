function fetchData() {
    fetch('/api/comparison')
        .then(response => response.json())
        .then(data => {
            document.getElementById("before").textContent = data.before_optimization;
            document.getElementById("after").textContent = data.after_optimization;
        })
        .catch(error => console.error("Error fetching comparison data:", error));
}
