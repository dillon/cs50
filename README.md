# My CS50 Projects
This repository contains all of my projects from CS50. Descriptions and demos of each project are below


# Crypto Dashboard
| React Native| Redux|
|--|--|

A React Native mobile app that displays market info and news on the top 200 cryptocurrencies by market cap.

Each cryptocurrency can be clicked to view more price-related and technical information such as its available, total, and maximum supply.

This app uses React Native and Redux to store each coin's information from CoinMarketCap and news from CryptoPanic.


I used [this guide](https://medium.com/react-native-training/tutorial-react-native-redux-native-mobile-app-for-tracking-cryptocurrency-bitcoin-litecoin-810850cf8acc) by Indrek Lasn to help set up react-redux as a single-page app with a list of cryptocurrencies and then added multi-page navigation and an action to fetch news to the redux store when a coin's page is visited.


![app screenshot](https://github.com/dpett/cs50-projects/blob/master/project/image1.jpg?raw=true)
![app gif](https://github.com/dpett/cs50-projects/blob/master/project/gif1.gif?raw=true)


Demo Video:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=3HaIw0yAygI
" target="_blank"><img src="http://img.youtube.com/vi/3HaIw0yAygI/0.jpg" 
alt="Youtube Video" width="480" height="360" border="10" /></a>

___

# Local News
|Flask | SQLite    | Google Maps API|
|--|--|--|

|Python| Javascript| jQuery|
|--|--|--|

A Flask app (utilizing an SQLite database) that searches for local news.

The user can pan and zoom around the map or search by zipcode, city name, or state name.
This site uses Flask with the Google Maps API and utilizes an SQLite database with city name, state, and zipcode information.

![app screenshot](https://github.com/dpett/cs50-projects/blob/master/pset8/mashup/mashup2.png?raw=true)

![app gif](https://github.com/dpett/cs50-projects/blob/master/pset8/mashup/mashup.gif?raw=true)

___

# Stock Exchange
|Flask | SQLite | Jinja
|--|--|--|

|Python| Javascript| Jinja
|--|--|--|

A Flask app (utilizing an SQLite database) that lets users register, login, get stock quotes as well as buy and sell stocks.
Users also have the option to delete their account and all associated data from the database.

![app gif](https://github.com/dpett/cs50-projects/blob/master/pset7/finance/finance.gif?raw=true)
