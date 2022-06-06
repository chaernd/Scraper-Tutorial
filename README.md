# Requests
Requests is a Python module that provides convenient methods for performing HTTP(S) requests. 
## Requests vs. Selenium
Headless browsers like Selenium or Playwright are extremely powerful tools, and are a fundamental part of our stack. One of their primary use-cases is the ability to select HTML elements programatically, which allows us to automate both the traversal of websites as well as harvesting data from their attributes or text. 
There is an inheret drawback with using headless browsers to scrape data, however. It's really a twofold problem:
+ Companies change the appearance of their websites quite often. Meaning, the underlying HTML is subject to change at the developer's whim; we have to take a reactive approach and perform maintenance on our retrievers when changes occur. 
+ The data is selected and parsed via the DOM. An API is supplying raw data to a JavaScript framework, and gets passed through a series of function calls that can be reminiscent of a Rube-Goldberg machine. It's often predictable where the data ends up in the DOM, but in the case of Angular pages, for example, the framework can litter the page with tags in a way that is very difficult to parse. The worst-case scenario is we resort to unconventional ways of selecting elements which can lead to the mortal sin of extracting data that is incorrect. 

The second point above is the most critical drawback of headless-browser scraping. Wouldn't it be great if we could access the data we need directly instead of relying on the browser to render it? 

What I want to show here is the formula to extract data using Requests. I'll spare you details on how REST/SOAP api's work. You can find a million hits on Google that will explain those things way better than I can. All this looked kind of intimidating to me when I first started, but it's really very straightforward. You just have to know where to look to get the info to access an API directly. 

You'll actually have an *easier* time making retrievers using Requests once you get the hang of it. The data returned to us will be far more consistent, and you'll reduce the amount of maintenance needed. Future crawl-team devs will thank you.

### Request Crawls: Step-by-step
This example is using Delta California's retriever. This crawl currently uses Selenium in production, but you can easily copy/paste this code to see how it works. 

#### Open DevTools --> Network
First, place a breakpoint before you get the login page:
```python
class DeltaCalifornia(PDFMixin, SeleniumMixin, BaseRetriever):
    def _login(self):
        # login
        app.logger.debug("Starting Chrome")
        self.start_driver("Chrome")
        app.logger.debug("Getting Login Page")
        breakpoint()
        self.driver.get("https://www1.deltadentalins.com/login.html")
```
And another breakpoint here:
```python
    def get_claims(self):
        d = self.driver
        breakpoint()
        time.sleep(5)
```
Open up your VNC and open DevTools. Click the Network tab. 

![alt-text](https://github.com/LakeEriePartners/stream/docs/crawl_docs/requests/imgs/breakpoint-login.png)

#### DevTools --> Network --> Fetch/XHR
Start stepping through the program to get the login page. Information will start to populate in the Network tab. Click on the Fetch/XHR tab to filter the activity. 

![alt-text](https://github.com/LakeEriePartners/stream/docs/crawl_docs/requests/imgs/script-xhr.png)

#### Inspect Fetch/XHR Methods
Continue the crawl until you hit the breakpoint in get_claims(). 
