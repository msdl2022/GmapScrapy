import requests
from bs4 import BeautifulSoup

# Function to scrape company information
def scrape_company_info(country):
    # Define the Google Maps URL with the country as a query parameter
    url = f"https://www.google.com/maps/search/{country}+companies"
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the company listings on the page
        company_listings = soup.find_all('div', class_='section-result-content')
        
        # Iterate through each listing and extract information
        for listing in company_listings:
            # Extract company name
            company_name = listing.find('h3', class_='section-result-title').text.strip()
            
            # Extract address
            address = listing.find('span', class_='section-result-location').text.strip()
            
            # Extract postal code
            postal_code = None  # You may need to modify this to extract postal code from the address
            
            # Extract website if available
            website = None
            website_elem = listing.find('div', class_='section-result-hours-phone-web')
            if website_elem:
                website = website_elem.find('div', class_='section-result-website-link')
                if website:
                    website = website.a['href']
            
            # Print or store the information as per your requirement
            print(f"Company Name: {company_name}")
            print(f"Address: {address}")
            print(f"Postal Code: {postal_code}")
            print(f"Website: {website}")
            print()
    else:
        print("Failed to fetch data from Google Maps.")

# Get user input for the country
country = input("Enter a country to search for companies: ")

# Call the function to scrape company information
scrape_company_info(country)
