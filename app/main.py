from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import random
import asyncio
import json
from datetime import datetime, timedelta

stocks = {
    "TECH": 150.0,
    "ENERGY": 75.0,
    "HEALTH": 200.0,
    "FINANCE": 100.0
}

"""
Use this function to get new stock prices, it randomly changes the price of the stock by a small amount
It will return a dictionary with the timestamp and the stocks which is for 4 industries
"""
def get_new_stock_prices():
    global stocks
    # Simulate market movements
    for stock in stocks:
        change = random.uniform(-4, 4)
        stocks[stock] += change
        stocks[stock] = max(10, stocks[stock])
    
    data = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "stocks": stocks
    }
    return data


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")
@app.get("/", response_class=HTMLResponse)
async def get():
   with open("index.html") as html:
      return HTMLResponse(content=html.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # accept the websocket connection
    await websocket.accept()
    try:
    # in a loop, get the new stock prices using get_new_stock_prices()
        while True:
            stockData = get_new_stock_prices()
    # send the new stock prices to the client
            await websocket.send_text(json.dumps(stockData))
    # sleep for 1 second
            await asyncio.sleep(1)
    # repeat
    except Exception as e:
        print(f"WebSocket disconnected: {e}")
    return

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)