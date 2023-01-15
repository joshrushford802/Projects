import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    list_transactions = db.execute(
        "SELECT symbol, SUM(shares) AS shares, price FROM user_transactions WHERE id = ? GROUP BY symbol;", user_id)
    money = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)
    monies = money[0]["cash"]

    return render_template("index.html", datab=list_transactions, monies=monies)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        stock_symbol = request.form.get("symbol")
        stock_shares = int(request.form.get("shares"))

        if not stock_symbol:
            return apology("Please enter stock-symbol")

        stock_name = lookup(stock_symbol.upper())

        if stock_name == None:
            return apology("Stock-symbol invalid.")

        if stock_shares < 0:
            return apology("Not enough shares.")

        transaction_price = stock_shares * stock_name['price']

        user_id = session["user_id"]
        user_money = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)
        user_dollars = user_money[0]["cash"]

        if user_dollars < transaction_price:
            return apology("Insuficient funds.")

        update_cash = user_dollars - transaction_price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)
        current_date = datetime.datetime.now()
        db.execute("INSERT INTO user_transactions (user_id, symbol, shares, price, calendar_date) VALUES (?, ?, ?, ?, ?)",
                   user_id, stock_name["symbol"], stock_shares, stock_name["price"], current_date)

        flash("Transaction complete.")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please enter stock-symbol")

        stock_name = lookup(symbol.upper())

        if stock_name == None:
            return apology("Stock-symbol invalid.")

        return render_template("returned_quote.html", name=stock_name["name"], price=stock_name["price"], symbol=stock_name["symbol"])

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not password:
            return apology("Must enter a password")

        if not username:
            return apology("Must enter a username")

        if password != confirmation:
            return apology("Password doesn't match")

        if not confirmation:
            return apology("Enter confirmation")

        hash = generate_password_hash(password)

        try:
            registered_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username taken, please choose a different username")

        session["user_id"] = registered_user

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        stock_symbol = request.form.get("symbol")
        stock_shares = int(request.form.get("shares"))

        if not stock_symbol:
            return apology("Please enter stock-symbol")

        stock_name = lookup(stock_symbol.upper())

        if stock_name == None:
            return apology("Stock-symbol invalid.")

        if stock_shares < 0:
            return apology("Not enough shares.")

        transaction_price = stock_shares * stock_name['price']

        user_id = session["user_id"]
        user_money = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)
        user_dollars = user_money[0]["cash"]

        owned_shares = db.execute("SELECT SUM(shares) AS shares FROM user_transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol;", user_id, stock_symbol)
        num_owned_shares = owned_shares[0]["shares"]
        if stock_shares > num_owned_shares:
            return apology("Not determinate amount of shares.")

        update_cash = user_dollars + transaction_price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)
        current_date = datetime.datetime.now()
        db.execute("INSERT INTO user_transactions (user_id, symbol, shares, price, calendar_date) VALUES (?, ?, ?, ?, ?)",
                   user_id, stock_name["symbol"], stock_shares, stock_name["price"], current_date)

        flash("Transaction complete.")
        return redirect("/")

    else:
        user = session["user_id"]
        user_symbols = db.execute(
            "SELECT symbol FROM user_transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0;", user)

        return render_template("sell.html", symbols=[i["symbol"] for i in user_symbols])