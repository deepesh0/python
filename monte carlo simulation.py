weights = {'AAPL': 0.5, 'MSFT': 0.3, 'TSLA': 0.2}

# Simulate portfolio value path
portfolio_sim = np.zeros((T, N))
for ticker in tickers:
    portfolio_sim += weights[ticker] * simulations[ticker]

# Plot portfolio simulations
plt.figure(figsize=(10, 5))
plt.plot(portfolio_sim.T, color='purple', alpha=0.1)
plt.title("Monte Carlo Simulation: Portfolio Value Over Time")
plt.xlabel("Days")
plt.ylabel("Portfolio Value")
plt.grid(True)
plt.show()
    