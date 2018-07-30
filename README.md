# cs50-projects
All of my projects for CS50 2018


## Crypto Dashboard
React Native, Redux
A React Native mobile app that displays the names of the top 200 cryptocurrencies by market cap, their current prices relative to USD, and their change in price over the past 24 hours and 7 days. You can click on each cryptocurrency to view more price-related and technical information such as its available, total, and maximum supply.
![app screenshot](https://github.com/dpett/cs50-projects/blob/master/project/image1.jpg?raw=true)
![app gif](https://github.com/dpett/cs50-projects/blob/master/project/gif1.gif?raw=true)
<a href="http://www.youtube.com/watch?feature=player_embedded&v=3HaIw0yAygI
" target="_blank"><img src="http://img.youtube.com/vi/3HaIw0yAygI/0.jpg" 
alt="Youtube Video" width="240" height="180" border="10" /></a>



Each currency's own page also features recent trending news headlines and their source.

This app uses React Native and Redux to store each coin's information and news.

# show coinmarketcap api

I used axios to fetch coin data from Coinmarketcap's API

# show cryptopanic api

and news data from Cryptopanic's API.

# show guide

I used this guide by Indrek Lasn to help set up react-redux as a single-page app with a list of cryptocurrencies

# show app

and then I used the React Native and Redux docs to create multi-page navigation and fetch news to the redux store when a coin's page is visited.
