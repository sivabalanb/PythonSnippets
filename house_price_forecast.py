import pandas as pd
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt

# Hypothetical input values
initial_property_price = 400000
annual_rent = 15000
mortgage_interest_rate = 5 / 100
mortgage_term = 20
down_payment = 0.05 * initial_property_price
annual_property_appreciation = 3 / 100
inflation_rate = 8 / 100

# Adjusted Values
adjusted_property_price = initial_property_price * (1 + annual_property_appreciation) ** mortgage_term
adjusted_annual_rent = annual_rent * (1 + inflation_rate) ** mortgage_term

# Calculated Costs
total_rent_costs = adjusted_annual_rent * mortgage_term

monthly_interest_rate = mortgage_interest_rate / 12
total_mortgage_payments = (initial_property_price - down_payment) * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-mortgage_term * 12)))
total_buying_costs = down_payment + total_mortgage_payments + (12 * mortgage_term * 200)  # Assuming £200 monthly for taxes and maintenance

# Home Equity
home_equity = down_payment

# Hypothetical Price Data for Renting and Buying (years 0 to 20)
years = list(range(21))
rent_price_data = [adjusted_annual_rent * (1 + annual_property_appreciation) ** year for year in years]
buying_price_data = [adjusted_property_price * (1 + annual_property_appreciation) ** year for year in years]


# Comparison Data
data = {
    'Description': ['Initial Property Price', 'Annual Rent', 'Mortgage Interest Rate', 'Mortgage Term', 'Down Payment',
                    'Annual Property Price Appreciation', 'Inflation Rate', 'Adjusted Property Price', 'Adjusted Annual Rent',
                    'Total Rent Costs', 'Total Mortgage Payments', 'Total Buying Costs', 'Home Equity'],
    'Value': [initial_property_price, annual_rent, f"{mortgage_interest_rate * 100}%", mortgage_term, down_payment,
              f"{annual_property_appreciation * 100}%", f"{inflation_rate * 100}%", adjusted_property_price, adjusted_annual_rent,
              total_rent_costs, total_mortgage_payments, total_buying_costs, home_equity]
}

# Create a DataFrame from the comparison data
df = pd.DataFrame(data)

# Generate the HTML output with the comparison table
html_table = df.to_html(index=False, classes='table table-bordered table-hover')

# Create the Price Trend Chart using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(years, rent_price_data, label='Renting')
plt.plot(years, buying_price_data, label='Buying')
plt.xlabel('Years')
plt.ylabel('Property Price (£)')
plt.title('Price Trend Comparison for Renting vs. Buying in London')
plt.legend()
plt.grid(True)
plt.savefig('price_trend_chart.png')
plt.close()

# Generate the final HTML output with the table and chart
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Comparison of Renting vs. Buying in London</title>
    <style>
        /* Add your custom CSS styles here if needed */
    </style>
</head>
<body>
    <h1>Comparison of Renting vs. Buying in London</h1>
    {html_table}
    <h2>Price Trend Chart</h2>
    <div>
        <p>Years</p>
        <p>{years}</p>
    </div>
    <div>
        <p>Property Price for Renting</p>
        <p>{rent_price_data}</p>
    </div>
    <div>
        <p>Property Price for Buying</p>
        <p>{buying_price_data}</p>
    </div>
    <div>
        <img src="price_trend_chart.png" alt="Price Trend Chart">
    </div>
</body>
</html>
"""

# Output the final HTML file
with open('output.html', 'w') as file:
    file.write(html_output)

print("Comparison table and price trend chart have been saved to 'output.html' and 'price_trend_chart.png', respectively.")