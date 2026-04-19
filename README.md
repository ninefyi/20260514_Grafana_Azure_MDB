# Real-Time Observability with MongoDB and Grafana: From Logs to Dashboard

Date: 14-May-2026

Event: Grafana and Friend (MongoDB x Grafana x Microsoft Azure)

Reference: https://www.meetup.com/grafana-and-friends-singapore/events/314162971

## Run the slide deck

This repository uses [Slidev](https://sli.dev/) to present the deck in `slides/deck.md`.

### Prerequisites

- Node.js 18+ (Node.js 20+ recommended)
- npm (comes with Node.js)

### Start presentation mode

From the repository root:

```bash
npx slidev slides/deck.md --open
```

What this does:

- Installs Slidev automatically (if not already installed)
- Starts a local dev server
- Opens the deck in your default browser

### If `npx` prompts for confirmation

Type `y` and press Enter.

### Optional: choose a custom port

```bash
npx slidev slides/deck.md --open --port 3030
```

### Build static slides (optional)

```bash
npx slidev build slides/deck.md
```

The built output is generated in `dist/`.

## Run on GitHub Codespaces

If you are running this repo inside GitHub Codespaces, use the steps below.

### 1) Install Node dependencies

```bash
npm install
```

### 2) Start Slidev for Codespaces

```bash
npm run dev
```

This command runs Slidev in remote mode on port `3030`, which works with Codespaces port forwarding and presenter control.

### 3) Open forwarded port 3030

- In VS Code, open the **Ports** panel
- Find port `3030`
- Open it in browser (or set visibility as needed)

### 4) Build in Codespaces (optional)

```bash
npm run build
```
