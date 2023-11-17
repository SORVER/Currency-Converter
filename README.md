# Currency Converter

A simple currency converter web application built with Flask, AJAX, and an external currency conversion API.
![Currency Converter Logo](/images/photo.png)

## Features

- **Currency Conversion:** Convert USD to other currencies using an external API.
- **AJAX Integration:** Utilizes AJAX for asynchronous communication between the client and server.
- **Flask Web Framework:** Server-side logic and API handling using Flask.
- **External API:** Fetches real-time currency exchange rates from an external API.

## Technologies Used

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Backend:**
  - Flask (Python web framework)
  - Requests library for handling HTTP requests

- **API:**
  - [CurrencyAPI](https://www.currencyapi.net/)

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- API Key from CurrencyAPI

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/currency-converter.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Set your CurrencyAPI key as an environment variable:   
   ```bash
   export API_KEY=your_currencyapi_key
   Replace your currency api_key with your actual API key
4. Run the Flask application:
   ```bash
   flask run
   The application should be accessible at http://127.0.0.1:5000.
### Usage
1. Open the application in your web browser.
3. Enter the target currency in the input field.
4. Click "Get Exchange Rate" to see the conversion result.

   
