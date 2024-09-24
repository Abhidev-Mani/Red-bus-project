# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
Here’s a quick summary of the key components and their functionality:

### Key Skills
* Web Scraping: Using Selenium to collect live bus data from the Redbus website.
* Python & SQL: Handling the scraped data, storing it in an SQL database for easy management.
* Streamlit: Building an interactive web application to visualize and filter the bus data.

### Problem Overview
* Automate data extraction from Redbus for government and private buses.
* Store the scraped data (bus routes, schedules, prices, seat availability, etc.) in a SQL database.
* Provide an interactive Streamlit application for users to filter and analyze the data.

### Use Cases
* Travel Aggregators: Real-time schedules and seat availability.
* Market Analysis: Travel patterns for market research.
* Customer Service: Tailored travel options.
* Competitor Analysis: Pricing and service comparison.

### Data Scraping Process
* Routes: Extract routes and corresponding details from Redbus using Selenium.
* Buses: Extract bus-specific details (e.g., departure time, rating, price) after collecting route information.

### SQL Database Schema
The database schema covers essential fields like:
* Route name, bus type, price, and seat availability, along with an auto-incrementing primary key for efficient data management.

### Streamlit Application Features
* The web app lets users filter buses based on criteria like bus type, route, price, ratings, and seat availability.
* The webpage offer an intuitive interface with dropdowns, sliders, and radio buttons to streamline user interaction.

### Filters and SQL Queries
The application efficiently queries the SQL database using user inputs:
* Filter buses based on the state, route, price range, star ratings, AC/non-AC type, and seat type.
* The SQL queries are dynamically generated based on the selected filters to fetch relevant data.

### In Summary:
This project offers a strong mix of web scraping, database management, and interactive web applications, making it highly impactful for the transportation sector.

### Overview of the webpage
Home Page :  ![image](https://github.com/user-attachments/assets/8baffc7b-0fa9-4def-ade7-c206ea0ae722) ,  
Next Page :  ![image](https://github.com/user-attachments/assets/b4198d4f-6acd-48c6-9763-ee1ee5d19425)

