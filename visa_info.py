import requests

def fetch_visa_info(country_name):
    base_url = "https://restcountries.com/v3/name/"
    
    try:
        # Make an API call to get country information
        response = requests.get(base_url + country_name)
        data = response.json()
        
        if response.status_code == 200 and isinstance(data, list):
            country_info = data[0]
            visa_info = country_info.get("visa", {})
            
            # Check if the country has visa-free access or visa-on-arrival information
            visa_free = visa_info.get("visa_free", [])
            visa_on_arrival = visa_info.get("visa_on_arrival", [])
            
            return visa_free, visa_on_arrival
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

def main():
    country_name = input("Enter your citizenship country: ").strip().capitalize()
    
    visa_free, visa_on_arrival = fetch_visa_info(country_name)
    
    if visa_free:
        print(f"\nVisa-Free Access Countries for {country_name}:")
        print(", ".join(visa_free))
    else:
        print(f"\nNo visa-free access information available for {country_name}.")
    
    if visa_on_arrival:
        print(f"\nCountries with Visa-on-Arrival for {country_name}:")
        print(", ".join(visa_on_arrival))
    else:
        print(f"\nNo visa-on-arrival information available for {country_name}.")

if __name__ == "__main__":
    main()
