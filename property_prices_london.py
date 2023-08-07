import requests
from bs4 import BeautifulSoup

def get_broadband_plans(postcode):
    url = f"https://example.com/broadband/plans/{postcode}"  # Replace with a valid broadband comparison website
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Write code to extract relevant information from the webpage using BeautifulSoup
        # For example, you might find specific divs, tables, or classes containing broadband plan details.

        # Sample code to extract plan names and prices (modify as per website structure)
        plan_names = [plan.text for plan in soup.select(".plan-name")]
        plan_prices = [price.text for price in soup.select(".plan-price")]

        return plan_names, plan_prices

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

def main():
    postcode = input("Enter the postcode for broadband comparison (e.g., NW1 5AL): ").strip()

    plan_names, plan_prices = get_broadband_plans(postcode)

    if plan_names and plan_prices:
        print("\nBroadband Plans in", postcode)
        for name, price in zip(plan_names, plan_prices):
            print(f"{name}: {price}")
    else:
        print(f"\nCould not fetch broadband plans for {postcode}. Please try again later.")

if __name__ == "__main__":
    main()
