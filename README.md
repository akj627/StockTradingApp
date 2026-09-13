# Stock Trading App

A simple mock stock-trading dashboard: a list of tickers with live-updating
prices, subscribe/watch toggles, and (coming soon) buy/sell trades with a
portfolio view.

This is a learning project built incrementally, one small piece at a time.
Prices are currently **simulated** (not real market data) and auth is
currently **username-only, no password** — both are designed to be swapped
out later without touching the rest of the app. See [Roadmap](#roadmap).

## Architecture

```
frontend/   React + TypeScript (Vite) — the dashboard UI
backend/    Python + FastAPI — serves tickers, streams prices, will handle
            auth/orders/portfolio
```

- **Live prices** are pushed from backend to frontend over **Server-Sent
  Events (SSE)** — one-directional, simpler than WebSockets, which is all
  price ticks need. The frontend connects once with the browser's built-in
  `EventSource` and receives an update every second.
- **Prices** come from a `PriceProvider` interface
  (`backend/app/price_provider.py`). `SimulatedPriceProvider` is the only
  implementation today — it seeds realistic starting prices and nudges them
  with a small random walk each tick. A future `LivePriceProvider` (real
  market data) can implement the same interface and be swapped in via
  config, with no other code changes.
- **Auth** will follow the same pattern: an `AuthProvider` interface with a
  `UsernameOnlyAuthProvider` now, and room for a `CognitoAuthProvider` later
  (see Roadmap).
- **Config** lives in `backend/.env` (see below) so swapping providers is a
  one-line change.
- **Storage** is in-memory only for now — state resets when the backend
  restarts. No database yet.

## Prerequisites

- Python 3.9+
- Node.js 18+ (developed with Node 22)

## Running locally

Two servers, run in separate terminals.

### Backend

```bash
cd backend
python3 -m venv venv        # first time only
source venv/bin/activate
pip install -r requirements.txt   # first time only
uvicorn app.main:app --port 8000 --reload
```

Verify it's up: `curl http://127.0.0.1:8000/health`

### Frontend

```bash
cd frontend
npm install     # first time only
npm run dev
```

Open http://localhost:5173

## Configuration

`backend/.env`:

```
PRICE_PROVIDER=simulated   # only option today; "live" will be added later
AUTH_PROVIDER=username     # only option today; "cognito" will be added later
```

## API (backend, current)

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Basic health check + active config |
| `/stocks` | GET | Current list of the 10 tickers with current prices |
| `/stream/prices` | GET (SSE) | Live-updating price stream, one event/second |

## Built step by step, with Claude

This project is being built incrementally using [Claude Code](https://claude.com/claude-code) —
deliberately as a series of small, fully-explained steps rather than one
generated codebase, so each concept could be understood before moving on.
Every step below was run and verified (via `curl`, a terminal script, or a
browser) before moving to the next.

| Step | What was built | Concept learned |
|---|---|---|
| 1 | Backend skeleton — a FastAPI app with one `/health` route, run via a Python virtual environment and `uvicorn` | How a Python web server actually boots: venv isolation, the FastAPI app object, and a dev server that listens on a port |
| 2 | Ticker data model + `/stocks` endpoint | Pydantic models as a data "contract"; how FastAPI auto-converts typed Python objects to JSON |
| 3 | Simulated price engine (`PriceProvider` interface + `SimulatedPriceProvider`) | Abstract base classes as a swap-in-later seam; a random-walk simulation for realistic-looking price drift |
| 4 | `/stream/prices` SSE endpoint + config-driven provider selection | Async generators (`yield` instead of `return`) for a long-lived connection; the raw SSE wire format (`data: ...\n\n`); picking an implementation from a config value |
| 5 | React + TypeScript dashboard consuming the stream | Vite project scaffolding; the browser's built-in `EventSource` API; why cross-origin requests need CORS; React state/`useEffect` re-rendering on each server push |

Next up (see [Roadmap](#roadmap)): username-only login, then buy/sell orders
and a portfolio view — each will get the same step-by-step treatment.

## Roadmap

Built so far:
- [x] Backend skeleton + config
- [x] Ticker list endpoint
- [x] Simulated price engine
- [x] Live price streaming (SSE)
- [x] Dashboard UI with live prices + local subscribe toggle

Not built yet:
- [ ] Username-only login (server-side, per-user state)
- [ ] Buy/sell orders + portfolio positions
- [ ] Swap in a real market data feed (`LivePriceProvider`)
- [ ] Swap in real auth, e.g. AWS Cognito (`CognitoAuthProvider`)
- [ ] Deploy to AWS (currently local-only)
