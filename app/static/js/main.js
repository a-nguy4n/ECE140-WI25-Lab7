// Constants and configuration
const maxDataPoints = 50;

// Initialize chart
const ctx = document.getElementById('stockChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            {
                label: 'TECH',
                data: [],
                borderColor: '#2196f3',
                tension: 0.4
            },
            {
                label: 'ENERGY',
                data: [],
                borderColor: '#f44336',
                tension: 0.4
            },
            {
                label: 'HEALTH',
                data: [],
                borderColor: '#4caf50',
                tension: 0.4
            },
            {
                label: 'FINANCE',
                data: [],
                borderColor: '#ff9800',
                tension: 0.4
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
            intersect: false,
            mode: 'index'
        },
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Stock Prices Over Time'
            }
        },
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});

// Display the stock card
function displayStockCard(stock, price, change) {
    const stockPricesDiv = document.getElementById('stockPrices');
    const card = document.createElement('div');
    card.className = 'stock-card';
    card.innerHTML = `
        <div class="stock-name">${stock}</div>
        <div class="stock-price">$${price.toFixed(2)}</div>
        <div class="stock-change ${change >= 0 ? 'positive' : 'negative'}">
            ${change >= 0 ? '▲' : '▼'} ${Math.abs(change)}%
        </div>
    `;
    stockPricesDiv.appendChild(card);
}