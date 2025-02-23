# ECE140-WI25-Lab7

In this lab activity, you will implement a real-time stock market dashboard using FastAPI and WebSockets. The dashboard will display stock price changes over time using a dynamic chart and price cards that update in real-time.

Previously, we've used standard HTTP requests to communicate between the client and server. Imagine if we had to just use what we've learned so far to implement a real-time stock market dashboard. We would have to continuously poll the server for new stock prices using GET requests. This approach is inefficient and not scalable! 


When it comes to real-time applications where you need data to be rapidly updated, WebSockets are a better choice. WebSockets provide a two-way communication channel between the client and server, allowing for real-time data exchange.

The lab session slides explain the concept of WebSockets in more detail, and we also encourage you to read though these resources:

- [FastAPI WebSockets Documentation](https://fastapi.tiangolo.com/advanced/websockets/)
- [WebSockets Introduction (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

---

## Setup

Similar to what we did in previous labs, do the following:

1. Build and run the container:
   ```sh
   docker-compose up --build
   ```
2. Open `http://localhost:8000` in your web browser.

Of course, the dashboard will not display any real-time data yet. You will need to implement the WebSocket connection between the client and server to achieve this.

---

## Your Tasks
This lab contains **TODOs** in `main.py` and `index.html`. Complete the following tasks to fully implement the real-time stock market visualization.

If you implemented everything successfully, you should see:

* The stock chart updating in real-time with new datapoints every second.
* The stock cards updating in real-time with new stock prices and the percentage change.

### Task 1: Implement the WebSocket Connection (JavaScript)
**File: `app/index.html`**
- Locate the `// TODO: Initialize the WebSocket connection` section.
- Create a **WebSocket object** that connects to `ws://localhost:8000/ws`.
  - We use `/ws` because that's the endpoint we defined in the FastAPI server in `main.py`.
- Handle incoming messages to update the chart and stock cards.

### Task 2: Track Previous Stock Prices (JavaScript)
**File: `app/index.html`**
- Locate the `// TODO: Track previous prices for calculating changes` section.
- Store the last received prices in a dictionary to compute percentage changes.

### Task 3: Implement the WebSocket Message Handler (JavaScript)
**File: `app/index.html`**
- Locate the `// TODO: Implement the message handler` section.
- When new stock data arrives:
  - **Update the chart** with `updateChartData(data)`.
  - **Update the stock cards** using `updatePriceCards(data, previousPrices)`.
  - **Store the new prices** in `previousPrices`.

**Hint:** The `onmessage` event handler is used to handle incoming messages from the WebSocket server. Here is a template to get you started:
```javascript
// Note that 'socket' is the WebSocket object you created in Task 1. 
// Make sure to use the same variable name!
socket.onmessage = function(event) {
    // add your code here
};
```

### Task 4: Implement Error Handling (JavaScript)
**File: `app/index.html`**
- Locate the `// TODO: Implement error handling` section.
- Log errors to the console when they occur.

**Hint:** Similar to the `onmessage` event handler, you can use the `onerror` event handler to handle WebSocket errors.

### Task 5: Handle WebSocket Connection Closure (JavaScript)
**File: `app/index.html`**
- Locate the `// TODO: Implement connection close handling` section.
- Log when the WebSocket connection is closed.

**Hint:** We just implemented `onmessage` and `onerror`. You can probably guess what the event handler for connection closure is called.

### Task 6: Implement the WebSocket Server (Python)
**File: `app/main.py`**
- Locate the websocket endpoint: `@app.websocket("/ws")`.
- Complete the code to: 
  - Accept the WebSocket connection.
  - Continuously send new stock prices every second using `get_new_stock_prices()`.
  - Note that the `get_new_stock_prices()` function is already implemented for you and returns the data as a **dictionary**. 
  - Also note that you are asked to get the code to **sleep for 1 second** between sending new stock prices. Even though you've used `time.sleep()` before, you should **not** use it here because this is an asynchronous function. Instead, you'll need to figure out how to do the equivalent using the `asyncio` library.

---

## Submission

As directed on Gradescope submission, submit your `index.html` and `main.py` files.