from flask import Flask, jsonify, render_template
import psutil
import time
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from simulate_before import simulate_before
from simulate_after import simulate_after

app = Flask(__name__)

class MemoryMonitor:
    def __init__(self):
        self.memory_history = []
        self.cache_history = []
        self.timestamps = []
        self.optimization_history = {
            'memory': {'before': None, 'after': None},
            'cache': {'before': None, 'after': None}
        }
        self.performance_metrics = {
            'response_times': [],
            'throughput': [],
            'page_faults': [],
            'swap_usage': []
        }

    def get_memory_stats(self):
        vm = psutil.virtual_memory()
        swap = psutil.swap_memory()
        return {
            'total': vm.total,
            'available': vm.available,
            'used': vm.used,
            'free': vm.free,
            'percent': vm.percent,
            'swap_total': swap.total,
            'swap_used': swap.used,
            'swap_free': swap.free,
            'swap_percent': swap.percent
        }

    def get_cache_stats(self):
        # Simulated cache statistics
        return {
            'hits': np.random.randint(80, 95),
            'misses': np.random.randint(5, 20),
            'hit_ratio': np.random.uniform(0.8, 0.95),
            'access_time': np.random.uniform(0.1, 0.5),
            'eviction_rate': np.random.uniform(0.1, 0.3),
            'write_back_rate': np.random.uniform(0.2, 0.4)
        }

    def get_performance_metrics(self):
        # Simulated performance metrics
        return {
            'response_time': np.random.uniform(0.1, 2.0),
            'throughput': np.random.uniform(1000, 5000),
            'page_faults': np.random.randint(10, 100),
            'swap_rate': np.random.uniform(0.1, 1.0)
        }

    def record_stats(self):
        self.memory_history.append(self.get_memory_stats())
        self.cache_history.append(self.get_cache_stats())
        metrics = self.get_performance_metrics()
        self.performance_metrics['response_times'].append(metrics['response_time'])
        self.performance_metrics['throughput'].append(metrics['throughput'])
        self.performance_metrics['page_faults'].append(metrics['page_faults'])
        self.performance_metrics['swap_usage'].append(metrics['swap_rate'])
        self.timestamps.append(datetime.now())

monitor = MemoryMonitor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/real-time-stats')
def get_real_time_stats():
    monitor.record_stats()
    return jsonify({
        'memory': monitor.memory_history[-1],
        'cache': monitor.cache_history[-1],
        'timestamp': monitor.timestamps[-1].strftime('%H:%M:%S')
    })

@app.route('/api/optimize-memory')
def optimize_memory():
    before_stats = monitor.get_memory_stats()
    monitor.optimization_history['memory']['before'] = before_stats
    
    # Simulate memory optimization
    time.sleep(2)
    
    # Simulate improved memory stats
    after_stats = {
        'total': before_stats['total'],
        'available': before_stats['available'] * 1.2,  # 20% improvement
        'used': before_stats['used'] * 0.8,  # 20% reduction
        'free': before_stats['free'] * 1.2,  # 20% improvement
        'percent': before_stats['percent'] * 0.8  # 20% reduction
    }
    
    monitor.optimization_history['memory']['after'] = after_stats
    
    return jsonify({
        'before': before_stats,
        'after': after_stats,
        'improvement': compare_performance(
            before_stats['percent'],
            after_stats['percent']
        )
    })

@app.route('/api/optimize-cache')
def optimize_cache():
    before_stats = monitor.get_cache_stats()
    monitor.optimization_history['cache']['before'] = before_stats
    
    # Simulate cache optimization
    time.sleep(2)
    
    # Simulate improved cache stats
    after_stats = {
        'hits': min(99, before_stats['hits'] * 1.15),  # 15% improvement
        'misses': max(1, before_stats['misses'] * 0.7),  # 30% reduction
        'hit_ratio': min(0.99, before_stats['hit_ratio'] * 1.15),  # 15% improvement
        'access_time': before_stats['access_time'] * 0.7  # 30% faster
    }
    
    monitor.optimization_history['cache']['after'] = after_stats
    
    return jsonify({
        'before': before_stats,
        'after': after_stats,
        'improvement': compare_performance(
            before_stats['hit_ratio'],
            after_stats['hit_ratio']
        )
    })

@app.route('/api/visualization')
def get_visualization():
    # Create visualization using plotly with more charts
    fig = make_subplots(
        rows=4, cols=2,
        subplot_titles=(
            'Memory Usage Over Time',
            'Cache Performance Over Time',
            'Memory Usage Comparison',
            'Cache Hit/Miss Ratio',
            'Memory Optimization Impact',
            'Cache Performance Metrics',
            'System Performance Metrics',
            'Memory Allocation Distribution'
        ),
        vertical_spacing=0.08,
        horizontal_spacing=0.1,
        specs=[
            [{"type": "scatter"}, {"type": "scatter"}],
            [{"type": "bar"}, {"type": "pie"}],
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "scatter"}, {"type": "sunburst"}]
        ]
    )
    
    # 1. Memory usage over time
    memory_usage = [m['percent'] for m in monitor.memory_history]
    timestamps = [t.strftime('%H:%M:%S') for t in monitor.timestamps]
    
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=memory_usage,
            name='Memory Usage',
            line=dict(color='#4a90e2', width=2)
        ),
        row=1, col=1
    )
    
    # 2. Cache performance over time
    cache_hits = [c['hits'] for c in monitor.cache_history]
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=cache_hits,
            name='Cache Hits',
            line=dict(color='#2ecc71', width=2)
        ),
        row=1, col=2
    )
    
    # 3. Memory usage comparison (if optimization was performed)
    if monitor.optimization_history['memory']['before'] and monitor.optimization_history['memory']['after']:
        memory_comparison = {
            'Before': monitor.optimization_history['memory']['before']['percent'],
            'After': monitor.optimization_history['memory']['after']['percent']
        }
        fig.add_trace(
            go.Bar(
                x=list(memory_comparison.keys()),
                y=list(memory_comparison.values()),
                name='Memory Usage',
                marker_color=['#ff7675', '#55efc4']
            ),
            row=2, col=1
        )
    
    # 4. Cache hit/miss ratio (current)
    latest_cache = monitor.cache_history[-1] if monitor.cache_history else monitor.get_cache_stats()
    fig.add_trace(
        go.Pie(
            labels=['Hits', 'Misses'],
            values=[latest_cache['hits'], latest_cache['misses']],
            name='Cache Hit/Miss',
            marker=dict(colors=['#00b894', '#ff7675'])
        ),
        row=2, col=2
    )
    
    # 5. Memory optimization impact (if performed)
    if monitor.optimization_history['memory']['before'] and monitor.optimization_history['memory']['after']:
        memory_metrics = {
            'Used': [
                monitor.optimization_history['memory']['before']['used'] / (1024**3),
                monitor.optimization_history['memory']['after']['used'] / (1024**3)
            ],
            'Free': [
                monitor.optimization_history['memory']['before']['free'] / (1024**3),
                monitor.optimization_history['memory']['after']['free'] / (1024**3)
            ]
        }
        
        fig.add_trace(
            go.Bar(
                name='Before',
                x=list(memory_metrics.keys()),
                y=[memory_metrics[k][0] for k in memory_metrics.keys()],
                marker_color='#ff7675'
            ),
            row=3, col=1
        )
        
        fig.add_trace(
            go.Bar(
                name='After',
                x=list(memory_metrics.keys()),
                y=[memory_metrics[k][1] for k in memory_metrics.keys()],
                marker_color='#55efc4'
            ),
            row=3, col=1
        )
    
    # 6. Cache performance metrics (if optimization was performed)
    if monitor.optimization_history['cache']['before'] and monitor.optimization_history['cache']['after']:
        cache_metrics = {
            'Hit Ratio': [
                monitor.optimization_history['cache']['before']['hit_ratio'] * 100,
                monitor.optimization_history['cache']['after']['hit_ratio'] * 100
            ],
            'Access Time': [
                monitor.optimization_history['cache']['before']['access_time'],
                monitor.optimization_history['cache']['after']['access_time']
            ]
        }
        
        fig.add_trace(
            go.Bar(
                name='Before',
                x=list(cache_metrics.keys()),
                y=[cache_metrics[k][0] for k in cache_metrics.keys()],
                marker_color='#ff7675'
            ),
            row=3, col=2
        )
        
        fig.add_trace(
            go.Bar(
                name='After',
                x=list(cache_metrics.keys()),
                y=[cache_metrics[k][1] for k in cache_metrics.keys()],
                marker_color='#55efc4'
            ),
            row=3, col=2
        )

    # 7. System Performance Metrics
    metrics = monitor.performance_metrics
    
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=metrics['response_times'],
            name='Response Time',
            line=dict(color='#6c5ce7', width=2)
        ),
        row=4, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=metrics['throughput'],
            name='Throughput',
            line=dict(color='#00b894', width=2),
            yaxis='y2'
        ),
        row=4, col=1
    )

    # 8. Memory Allocation Sunburst
    if monitor.memory_history:
        latest_memory = monitor.memory_history[-1]
        total_gb = latest_memory['total'] / (1024**3)
        used_gb = latest_memory['used'] / (1024**3)
        cached_gb = (latest_memory['total'] - latest_memory['available'] - latest_memory['used']) / (1024**3)
        free_gb = latest_memory['free'] / (1024**3)
        
        fig.add_trace(
            go.Sunburst(
                labels=['Total', 'Used', 'Cached', 'Free', 'Active', 'Inactive'],
                parents=['', 'Total', 'Total', 'Total', 'Used', 'Used'],
                values=[total_gb, used_gb, cached_gb, free_gb, used_gb * 0.7, used_gb * 0.3],
                branchvalues='total',
                marker=dict(
                    colors=['#2ecc71', '#e74c3c', '#3498db', '#95a5a6', '#e67e22', '#9b59b6']
                ),
                name='Memory Distribution'
            ),
            row=4, col=2
        )

    # Update layout for better visualization
    fig.update_layout(
        height=1400,  # Increased height for more charts
        showlegend=True,
        template='plotly_white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='Segoe UI, sans-serif',
            size=12
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # Add second y-axis for throughput
    fig.update_layout(
        yaxis7=dict(title="Response Time (ms)"),
        yaxis8=dict(title="Throughput (req/s)", overlaying="y7", side="right")
    )

    # Update axes labels for all charts
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_xaxes(title_text="Time", row=1, col=2)
    fig.update_yaxes(title_text="Memory Usage (%)", row=1, col=1)
    fig.update_yaxes(title_text="Cache Hits", row=1, col=2)
    fig.update_yaxes(title_text="Memory Usage (%)", row=2, col=1)
    fig.update_yaxes(title_text="GB", row=3, col=1)
    fig.update_yaxes(title_text="Value", row=3, col=2)

    return jsonify(fig.to_dict())

def compare_performance(before, after):
    return {
        "before_ratio": before,
        "after_ratio": after,
        "improvement": round(((after - before) / before) * 100, 2)
    }

if __name__ == '__main__':
    app.run(debug=True)
