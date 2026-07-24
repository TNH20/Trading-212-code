@bot.command(name="ping")
async def porfolio(ctx):
    #for authentication of the users trading account
    api_key = "" #enter your own key and secret here
    api_secret = ""

    credentials = f"{api_key}:{api_secret}"
    encoded = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded}"
    }

    baseUrl = "https://live.trading212.com/api/v0" #base Url that the code will pull from

    summary = requests.get(f"{baseUrl}/equity/account/summary", headers=headers).json() #specific url that this bit of code will pull data from
    #account summary section
    total = (summary['totalValue'])#gets some basic account info
    cash = (summary['cash']['availableToTrade'])
    summ = discord.Embed(title="===account summary===", color=discord.Color.green())#creates the embed and adds the title and colour
    summ.add_field(name="", value=f"total Value: {total}")#adds the account info to the embed
    summ.add_field(name="", value=f"cash: £{cash}")
    await ctx.send(embed=summ)#displays the embed 

    #portfolio section
    embed = discord.Embed(title="===portfolio===")
    portfolio = requests.get(f"{baseUrl}/equity/portfolio", headers=headers).json() #changing the url for different types of data
    for item in portfolio: #for the amount of stock options, collect data like current price and average price
        stat = (f"  {item['ticker']:<12} qty: {item['quantity']:<8} "
                f"avg: £{item['averagePrice']:.2f}  "
                f"now: £{item['currentPrice']:.2f}  "
                f"P&L: £{item['ppl']:.2f}"
                f"---------------------") #this is for ease of reading
        embed.add_field(name="", value=stat)#adds the data to the embed
    await ctx.send(embed=embed)