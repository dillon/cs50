import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


# check if int, a function written by Triptych on stackoverflow :)
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # jinja values = stocks[[symbol, shares, price, value]], cash, totalvalue
    portfolio = db.execute(
        "SELECT * FROM portfolios WHERE userID = :sessionid", sessionid=session["user_id"])
    cashrow = db.execute(
        "SELECT cash FROM users WHERE id = :sessionid", sessionid=session["user_id"])
    if cashrow:
        cash = cashrow[0]["cash"]
    else:
        cash = 10000
    stocks = []
    totalvalue = cash
    if portfolio:
        for stock in portfolio:
            symbol = stock["symbol"]
            shares = stock["shares"]
            # lookup name and price
            myvalue = lookup(symbol)
            if not myvalue:
                return apology("API not working")
            price = myvalue["price"]
            value = int(shares) * float(price)
            stocks.append({
                "symbol": symbol,
                "shares": shares,
                "price": usd(price),
                "value": usd(value)
            })
            totalvalue += price * shares

    return render_template("index.html", stocks=stocks, cash=usd(cash), totalvalue=usd(totalvalue))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # form names = symbol, shares
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not RepresentsInt(shares):
            return apology("You must enter a valid number of shares")
        if not symbol or not shares or int(shares) <= 0:
            return apology("You must enter a valid symbol and shares")
        quote = lookup(symbol)
        if not quote:
            return apology("Not a valid symbol or API not working")
        walletrow = db.execute(
            "SELECT * FROM users WHERE id = :sessionid", sessionid=session["user_id"])
        wallet = walletrow[0]["cash"]
        price = quote["price"]
        cost = float(price) * int(shares)
        if wallet < cost:
            return apology("Not enough cash in account")
        # if you can afford it, insert into history table
        resultHistory = db.execute("INSERT INTO history (userID, shares, symbol, price) VALUES(:userID, :shares, :symbol, :price)",
                                   userID=session["user_id"], shares=int(shares), symbol=symbol, price=float(price))
        if not resultHistory:
            return apology("Problem making a purchase. Please try again later.")
        # look for in and then update portfolios
        resultPortfoliosSearch = db.execute(
            "SELECT shares FROM portfolios WHERE userID = :sessionid AND symbol = :symbol", sessionid=int(session["user_id"]), symbol=symbol)
        if resultPortfoliosSearch:
            # if you found it, update it
            resultPortfoliosUpdate = db.execute(
                "UPDATE portfolios SET shares = shares + :shares WHERE userID = :sessionid AND symbol = :symbol", sessionid=session["user_id"], symbol=symbol, shares=shares)
            if not resultPortfoliosUpdate:
                return apology("Error resultPortfoliosUpdate")
        else:
            resultPortfoliosAdd = db.execute("INSERT INTO portfolios (userID, shares, symbol) VALUES(:userID, :shares, :symbol)",
                                             userID=session["user_id"], shares=int(shares), symbol=symbol
                                             )
            if not resultPortfoliosAdd:
                return apology("Error resultPortfoliosAdd")
        # and update users table cash
        resultUsers = db.execute(
            "UPDATE users SET cash = cash - :cost WHERE id = :sessionid", cost=cost, sessionid=session["user_id"])
        if not resultUsers:
            return apology("Problem updating your wallet. Please try again later.")
        # redirect to index
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show portfolio of stocks"""
    # jinja values = transaction[{symbol, shares, price, date}]

    resultsHistory = db.execute(
        "SELECT * FROM history WHERE userID = :sessionid", sessionid=session["user_id"])
    transactions = []
    if resultsHistory:
        for transaction in resultsHistory:
            # db values = transactionID, userID, shares, symbol, price, datetime
            symbol = transaction["symbol"]
            shares = transaction["shares"]
            price = transaction["price"]
            date = transaction["datetime"]
            transactions.append({
                "symbol": symbol,
                "shares": shares,
                "price": usd(price),
                "date": date
            })

    else:
        transactions.append({
            "name": "-",
            "symbol": "-",
            "shares": "-",
            "price": "-",
            "value": "-"
        })

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        value = request.form.get("symbol")
        if not value:
            return apology("Please enter a valid ticker")
        quote = lookup(value)
        if not quote:
            return apology("Not a valid symbol")
        return render_template("display.html", ticker=quote["symbol"], price=usd(int(quote["price"])))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # clear session
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # check form is correctly entered
        if not username:
            return apology("must create a username")
        if not password:
            return apology("must create a password")
        if not confirmation:
            return apology("must enter password again to confirm")
        if not password == confirmation:
            return apology("password and password confirmation must be identical")
        # encrypt and add
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hashedpassword)",
                            username=username, hashedpassword=generate_password_hash(password))
        if not result:
            return apology("that username is already taken")
        session["user_id"] = username
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # form names = symbol, shares
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not RepresentsInt(shares):
            return apology("You must enter a valid whole number of shares")
        if not symbol or not shares or int(shares) <= 0:
            return apology("You must enter a valid symbol and shares")
        quote = lookup(symbol)
        if not quote:
            return apology("Not a valid symbol, or API not working")
        price = quote["price"]
        cost = float(price) * int(shares)

        # look for in and then update portfolios
        resultPortfoliosSearch = db.execute(
            "SELECT shares FROM portfolios WHERE userID = :sessionid AND symbol = :symbol", sessionid=int(session["user_id"]), symbol=symbol)
        if int(resultPortfoliosSearch[0]["shares"]) > int(shares):
            # if you have it and you have extra shares, update it
            resultPortfoliosUpdate = db.execute("UPDATE portfolios SET shares = shares - :shares WHERE userID = :sessionid AND symbol = :symbol",
                                                sessionid=session["user_id"], symbol=symbol, shares=int(shares))
            if not resultPortfoliosUpdate:
                return apology("You don't have enough shares of that stock")
        elif resultPortfoliosSearch and resultPortfoliosSearch[0]["shares"] == int(shares):
            # if you have it and you have exactly the same number of shares, just delete it from portfolio
            resultPortfoliosUpdate = db.execute(
                "DELETE FROM portfolios WHERE userID = :sessionid AND symbol = :symbol", sessionid=session["user_id"], symbol=symbol)
            if not resultPortfoliosUpdate:
                return apology("You don't own any shares of that stock")
        else:
            return apology("You don't have enough shares of that stock")
        # also insert it into history table
        resultHistory = db.execute("INSERT INTO history (userID, shares, symbol, price) VALUES(:userID, :shares, :symbol, :price)",
                                   userID=session["user_id"], shares=0 - int(shares), symbol=symbol, price=float(price))
        if not resultHistory:
            return apology("Problem making a purchase. Please try again later.")
        # and update users table cash
        resultUsers = db.execute(
            "UPDATE users SET cash = cash + :cost WHERE id = :sessionid", cost=cost, sessionid=session["user_id"])
        if not resultUsers:
            return apology("Problem updating your wallet. Please try again later.")
        # redirect to index
        return redirect("/")
    else:
        # get symbols
        resultSymbols = db.execute(
            "SELECT symbol FROM portfolios WHERE userID = :sessionid", sessionid=session["user_id"])
        if not resultSymbols:
            return apology("You don't have any stocks to sell")
        return render_template("sell.html", symbols=resultSymbols)


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Allow user to delete their account"""
    if request.method == "POST":
        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = :userID",
                          userID=session["user_id"])

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # delete from users
        resultAccountDeleteU = db.execute(
            "DELETE FROM users WHERE id = :sessionid", sessionid=session["user_id"])
        if not resultAccountDeleteU:
            return apology("Failed to delete account for whatever reason")
        # delete from history
        resultAccountDeleteH = db.execute(
            "DELETE FROM history WHERE userID = :sessionid", sessionid=session["user_id"])
        if not resultAccountDeleteH:
            return apology("Failed to delete account for whatever reason")
        # delete from portfolios
        resultAccountDeleteP = db.execute(
            "DELETE FROM portfolios WHERE userID = :sessionid", sessionid=session["user_id"])
        if not resultAccountDeleteP:
            return apology("Failed to delete account for whatever reason")

        session.clear()
        return redirect("/")
    else:
        return render_template("account.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
