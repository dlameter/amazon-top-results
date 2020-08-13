# Amazon Top Results
Finds and displays the top results for a given search phrase. Displays product name and current price.

## Goals
Project goal is to practice web scraping. There is an Amazon product API, however, using that would go against the project goals. Thusly, only use this project as a POC or for small and infrequent requests, their API is more suited to large and frequent queries.

## Config.json
A config.json file must be placed in the same directory as the python code when running. It is structured as follows:

```
{
    "address" : string,
    "driver" : string
}
```

The value of address points to the search URL of amazon, and the value of driver points to the webdriver for chrome on your local drive.

## Libraries
This project uses the python selenium library to perform web requests and to navigate the dynamically generated website.
