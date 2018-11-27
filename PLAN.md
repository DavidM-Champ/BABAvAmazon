Task 1. Business Understanding
1.	Business Goals
The ultimate goal is to determine which e-commerce stock is the best to invest in. Given the sheer amount of available stocks, I, as a sole proprietor business, have narrowed down the industry I want to invest in to e-commerce. That being said, there are various e-commerce stocks (specifically Amazon, Alibaba, and Shopify) to pick from, and thus data mining and data analysis must be used in order to determine which is the most appropriate stock to purchase in order to maximize the return on investment on the stock market.

Ideally, since the investment strategy is focused purely on price growth (that is, we are not interested in dividends or anything of the like), the stock purchased must generate a yearly return of at least 10% over the next 5 years. The minimum expectation would be for the stock to outperform the returns given by the S&P 500 index.

2.	Situation Assessment
Resources: We have access to all quarterly and yearly reports of the stocks we will analyze, as well as access to the earnings calls and speeches given by management/CEOs about the state of their companies and future outlooks. We also have access to the stock price history since the companies have been public, and we can utilize that to compare.

Requirements, assumptions, and constraints: We are assuming that all the quarterly and yearly reports give us accurate numbers, as reporting wrongly is in violation of federal law and against the interests of both investors and the companies. The timeframe for the project will be from now until December 19th, when the project is due, however the most favorable stock will ideally be purchased the Wednesday before, thus giving a week to track its price once actual money was put in line.

Risks: The biggest two risks are macroeconomic trends (such as a trade war between the US and China affecting the world economy) and unexpected news swings (such as sudden bad PR). These will all be taken into account hopefully quickly, and be noted as disclaimers in the analysis.

Terminology: EPS(Earnings per share), PR (public relations), AMZN, BABA, SHOP (the stock tickers of the three companies to be analyzed)

Costs and benefits: The most that the project will cost is the cost of a single share of a selected company, which will be determined in the coming weeks. For companies focused on growth, such as the three aforementioned stocks, the growth of the stock price can be exponential, while the downsides are smaller and sometimes temporary, the real cost is analyzing the stock wrongly and thus missing out on better investments, however if this were an easy thing to do, everyone would be making free money.

3.	Data mining/analysis goals
The ultimate goal is to have the earnings data organized in a reasonable manner (preferably in CSV files), and a model that can report the strongest correlations within data from the earnings and the price history.
Task 2. Data Understanding
•	Gathering Data
Requirements: The necessary data will be all the data within the earning reports and cash flow statements of the aforementioned companies as well as their price histories.

Availability: All data is publicly available, as required by law for any public company.

Selection criteria: All of the quarterly earnings from the start of 2016 to the latest available will be utilized. Within the quarterly earnings we will only really utilize profit margins (ignoring revenues and costs) except for exceptional cases (such as debt).

•	Describing Data
The quarterly reports are merely a series of numbers, which must be reorganized into a single, big dataset per company in order to make it readable by the code we will utilize to analyze it. The stock price data can be downloaded in a nicely formatted CSV file from yahoo finance.

•	Exploring Data
Not particularly relevant yet. Most of the project will be exploring the data itself.

•	Verifying Quality
As stated above: We are assuming that all the quarterly and yearly reports give us accurate numbers, as reporting wrongly is in violation of federal law and against the interests of both investors and the companies.
