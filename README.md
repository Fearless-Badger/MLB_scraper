Project which will scrape MLB roster information and integrate with a full web app


Requirements:

    Python 3.12.6
        -Flask
        -BeautifulSoup
        -requests
    node 23.1.0
        -npm
    

How to Run:

    # docker build -t mlb-scraper .
    # docker run -p 5000:5000 mlb-scraper