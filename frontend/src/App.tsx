import { useEffect, useState } from "react";
import type { Stock } from "./types";
import "./App.css";

function App() {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [subscribed, setSubscribed] = useState<Set<string>>(new Set());

  useEffect(() => {
    const source = new EventSource("http://localhost:8000/stream/prices");

    source.onmessage = (event) => {
      const data: Stock[] = JSON.parse(event.data);
      setStocks(data);
    };

    return () => source.close();
  }, []);

  function toggleSubscribed(symbol: string) {
    setSubscribed((prev) => {
      const next = new Set(prev);
      if (next.has(symbol)) {
        next.delete(symbol);
      } else {
        next.add(symbol);
      }
      return next;
    });
  }

  return (
    <div className="dashboard">
      <h1>Stock Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>Subscribe</th>
            <th>Symbol</th>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock) => (
            <tr key={stock.symbol} className={subscribed.has(stock.symbol) ? "subscribed" : ""}>
              <td>
                <input
                  type="checkbox"
                  checked={subscribed.has(stock.symbol)}
                  onChange={() => toggleSubscribed(stock.symbol)}
                />
              </td>
              <td>{stock.symbol}</td>
              <td>{stock.name}</td>
              <td>${stock.price.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
