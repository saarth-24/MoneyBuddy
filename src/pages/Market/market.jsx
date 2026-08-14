import React, { useState } from "react";
import Navbar from "../../components/Navbar/Navbar"; // Adjust import path if needed
import { useNavigate } from "react-router-dom";

export default function MarketsPage() {
  const navigate = useNavigate();

  // Navigation / Filter States
  const [region, setRegion] = useState("India");
  const [selectedChartIndex, setSelectedChartIndex] = useState("NIFTY 50");
  const [chartTimeframe, setChartTimeframe] = useState("1D");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedModalStock, setSelectedModalStock] = useState(null);

  // Watchlist State
  const [watchlist, setWatchlist] = useState([
    { symbol: "RELIANCE", name: "Reliance Industries", price: "₹1,420.50", change: "+1.42%", positive: true },
    { symbol: "HDFCBANK", name: "HDFC Bank Ltd.", price: "₹1,760.10", change: "-0.32%", positive: false },
    { symbol: "TCS", name: "Tata Consultancy Services", price: "₹3,420.80", change: "+2.14%", positive: true },
    { symbol: "NIFTY50", name: "NIFTY 50 Index", price: "24,856.30", change: "+0.84%", positive: true },
  ]);

  // Regional Index Snapshots
  const indexData = {
    India: [
      { name: "NIFTY 50", val: "24,856.30", change: "+0.84%", pos: true },
      { name: "SENSEX", val: "81,450.20", change: "+0.62%", pos: true },
      { name: "BANK NIFTY", val: "55,280.15", change: "-0.21%", pos: false },
      { name: "USD / INR", val: "₹87.42", change: "+0.12%", pos: true },
    ],
    US: [
      { name: "S&P 500", val: "5,450.10", change: "+0.45%", pos: true },
      { name: "NASDAQ", val: "17,210.40", change: "+0.92%", pos: true },
      { name: "DOW JONES", val: "39,120.80", change: "-0.15%", pos: false },
      { name: "US 10Y YIELD", val: "4.22%", change: "-0.04%", pos: false },
    ],
    Global: [
      { name: "FTSE 100", val: "8,210.50", change: "+0.18%", pos: true },
      { name: "NIKKEI 225", val: "38,450.00", change: "+1.12%", pos: true },
      { name: "HANG SENG", val: "17,640.20", change: "-0.54%", pos: false },
      { name: "BRENT CRUDE", val: "$78.20", change: "-0.85%", pos: false },
    ],
  };

  // Movers Data
  const topGainers = [
    { symbol: "RELIANCE", name: "Reliance Industries", price: "₹1,420.50", change: "+4.82%" },
    { symbol: "TCS", name: "Tata Consultancy", price: "₹3,420.80", change: "+3.61%" },
    { symbol: "INFY", name: "Infosys Limited", price: "₹1,840.10", change: "+3.14%" },
    { symbol: "HDFCBANK", name: "HDFC Bank Ltd.", price: "₹1,760.10", change: "+2.87%" },
  ];

  const topLosers = [
    { symbol: "TATAMOTORS", name: "Tata Motors Ltd.", price: "₹980.40", change: "-3.42%" },
    { symbol: "ITC", name: "ITC Limited", price: "₹485.20", change: "-2.81%" },
    { symbol: "ADANIENT", name: "Adani Enterprises", price: "₹3,120.00", change: "-2.37%" },
    { symbol: "WIPRO", name: "Wipro Limited", price: "₹510.60", change: "-1.94%" },
  ];

  // News Data with "Why it matters"
  const newsItems = [
    {
      id: 1,
      title: "RBI keeps policy repo rate unchanged at 6.50%",
      time: "2 hours ago",
      source: "Economic Pulse",
      snippet: "Monetary Policy Committee maintains status quo for the seventh consecutive meeting, citing headline inflation target alignment.",
      whyItMatters: "Supports interest-sensitive banking stocks while maintaining current borrowing structures across housing and automobile loans.",
    },
    {
      id: 2,
      title: "IT sector rallies following enterprise cloud spending acceleration",
      time: "4 hours ago",
      source: "Market Desk",
      snippet: "Tier-1 IT services experience increased deal order inflows driven by enterprise AI infrastructure modernization contracts.",
      whyItMatters: "Directly positively impacts tech-heavy portfolios and index earnings projections for Q2.",
    },
    {
      id: 3,
      title: "Brent Crude falls toward $78 amid increased supply forecasts",
      time: "6 hours ago",
      source: "Global Commodities",
      snippet: "Non-OPEC output increases pressure global crude pricing despite ongoing geopolitical supply checks.",
      whyItMatters: "Reduces raw material cost inflation for domestic paints, logistics, and consumer goods manufacturing firms.",
    },
  ];

  // Sector Data
  const sectorPerformance = [
    { name: "IT Services", pct: "+2.4%", width: "85%", pos: true },
    { name: "Banking & Financials", pct: "+1.8%", width: "70%", pos: true },
    { name: "Pharma & Healthcare", pct: "+1.2%", width: "55%", pos: true },
    { name: "FMCG", pct: "+0.8%", width: "40%", pos: true },
    { name: "Automobile", pct: "+0.4%", width: "25%", pos: true },
    { name: "Energy & Oil", pct: "-0.3%", width: "20%", pos: false },
  ];

  // Stocks to Watch
  const stocksToWatch = [
    {
      symbol: "HDFCBANK",
      sector: "Banking",
      momentum: 80,
      valuation: 60,
      volatility: 40,
      reason: "Consolidating near major technical support with robust deposit growth metrics.",
    },
    {
      symbol: "TCS",
      sector: "Information Tech",
      momentum: 90,
      valuation: 70,
      volatility: 35,
      reason: "Broke above 50-day moving average following strong deal wins in North America.",
    },
    {
      symbol: "LT",
      sector: "Infrastructure",
      momentum: 75,
      valuation: 65,
      volatility: 50,
      reason: "Order pipeline expansion backed by higher government capital expenditure allocations.",
    },
  ];

  const removeFromWatchlist = (symbol) => {
    setWatchlist(watchlist.filter((item) => item.symbol !== symbol));
  };

  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100 flex flex-col selection:bg-lime-400 selection:text-black">
      {/* Integrated Navbar */}
      <Navbar />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
        
        {/* PAGE HEADER & SEARCH */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 border-b border-neutral-900 pb-6">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-lime-400 mb-1">
              <span className="w-2 h-2 rounded-full bg-lime-400 animate-pulse" />
              Market Intelligence
            </div>
            <h1 className="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
              Markets
            </h1>
            <p className="text-neutral-400 text-xs sm:text-sm mt-1">
              Real-time global market trends connected to your personal financial portfolio.
            </p>
          </div>

          <div className="relative w-full md:w-80">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search stocks, ETFs, indices..."
              className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-2.5 pl-10 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-lime-400 transition-colors"
            />
            <span className="absolute left-3.5 top-3 text-neutral-500 text-xs font-mono">
              Q
            </span>
          </div>
        </div>

        {/* 1. TOP: MARKET SNAPSHOT */}
        <div className="space-y-4">
          <div className="flex justify-between items-center">
            <span className="text-xs font-mono uppercase tracking-wider text-neutral-400">
              Benchmark Snapshot
            </span>
            <div className="flex items-center bg-neutral-900 border border-neutral-800 rounded-xl p-1 gap-1">
              {["India", "US", "Global"].map((item) => (
                <button
                  key={item}
                  onClick={() => setRegion(item)}
                  className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                    region === item
                      ? "bg-lime-400 text-black shadow-sm"
                      : "text-neutral-400 hover:text-white"
                  }`}
                >
                  {item}
                </button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {indexData[region].map((idx) => (
              <div
                key={idx.name}
                className="bg-neutral-900/80 border border-neutral-800/80 hover:border-neutral-700 p-5 rounded-2xl transition-all"
              >
                <span className="text-[11px] font-mono text-neutral-400 uppercase tracking-wider">
                  {idx.name}
                </span>
                <div className="text-2xl font-bold text-white mt-1 font-mono">
                  {idx.val}
                </div>
                <div
                  className={`text-xs font-medium mt-2 font-mono flex items-center gap-1 ${
                    idx.pos ? "text-lime-400" : "text-rose-500"
                  }`}
                >
                  <span>{idx.pos ? "▲" : "▼"}</span>
                  <span>{idx.change}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 2. MAIN MARKET CHART */}
        <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-6">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 border-b border-neutral-800/80 pb-4">
            <div>
              <div className="flex items-center gap-3">
                <h2 className="text-lg font-bold text-white">{selectedChartIndex}</h2>
                <span className="text-xs font-mono bg-lime-400/10 text-lime-400 border border-lime-400/20 px-2.5 py-0.5 rounded-md font-semibold">
                  24,856.30 (+0.84%)
                </span>
              </div>
              <span className="text-xs font-mono text-neutral-500">Real-time Trading Overview</span>
            </div>

            {/* Timeframe Selector */}
            <div className="flex gap-1 bg-neutral-950 border border-neutral-800 p-1 rounded-xl">
              {["1D", "1W", "1M", "6M", "1Y"].map((tf) => (
                <button
                  key={tf}
                  onClick={() => setChartTimeframe(tf)}
                  className={`px-3 py-1 rounded-lg text-xs font-mono font-medium transition-all ${
                    chartTimeframe === tf
                      ? "bg-neutral-800 text-white font-bold border border-neutral-700"
                      : "text-neutral-500 hover:text-neutral-300"
                  }`}
                >
                  {tf}
                </button>
              ))}
            </div>
          </div>

          {/* Index Tabs Selector */}
          <div className="flex flex-wrap gap-2">
            {["NIFTY 50", "SENSEX", "BANK NIFTY", "NIFTY IT", "NIFTY FMCG", "NIFTY PHARMA"].map((indexName) => (
              <button
                key={indexName}
                onClick={() => setSelectedChartIndex(indexName)}
                className={`px-3.5 py-1.5 rounded-xl text-xs font-medium transition-all ${
                  selectedChartIndex === indexName
                    ? "bg-lime-400 text-black font-semibold"
                    : "bg-neutral-950 border border-neutral-800/80 text-neutral-400 hover:text-white"
                }`}
              >
                {indexName}
              </button>
            ))}
          </div>

          {/* SVG Vector Chart Illustration */}
          <div className="h-64 w-full bg-neutral-950 rounded-2xl border border-neutral-800/80 p-4 flex items-end relative overflow-hidden">
            <div className="absolute inset-0 bg-gradient-to-t from-lime-400/5 to-transparent pointer-events-none" />
            <svg className="w-full h-full text-lime-400 relative z-10" viewBox="0 0 600 150" preserveAspectRatio="none">
              <path
                fill="none"
                stroke="currentColor"
                strokeWidth="2.5"
                d="M0,120 Q60,110 120,80 T240,95 T360,40 T480,55 T600,15"
              />
            </svg>
          </div>
        </div>

        {/* 3. YOUR PORTFOLIO IN TODAY'S MARKET & FINOVA MARKET INTELLIGENCE */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          {/* Your Portfolio In Today's Market */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl flex flex-col justify-between space-y-4">
            <div className="flex justify-between items-start border-b border-neutral-800/80 pb-3">
              <div>
                <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                  Your Portfolio In Today's Market
                </h2>
                <span className="text-xs font-mono text-neutral-500">Benchmark Relative Exposure</span>
              </div>
              <span className="text-xs font-mono text-lime-400 bg-lime-400/10 px-2.5 py-1 rounded-full border border-lime-400/20">
                +₹1,550 (+0.61%)
              </span>
            </div>

            <div className="grid grid-cols-2 gap-4 my-2">
              <div className="bg-neutral-950 p-4 rounded-2xl border border-neutral-800/80 font-mono">
                <span className="text-[11px] text-neutral-500 block">NIFTY 50 Benchmark</span>
                <span className="text-lg font-bold text-lime-400 block mt-1">+0.84%</span>
              </div>
              <div className="bg-neutral-950 p-4 rounded-2xl border border-neutral-800/80 font-mono">
                <span className="text-[11px] text-neutral-500 block">Your Portfolio Movement</span>
                <span className="text-lg font-bold text-white block mt-1">+0.61%</span>
              </div>
            </div>

            <div className="space-y-2">
              <span className="text-xs font-mono text-neutral-400 block">Top Contributors to Your Balance Today</span>
              <div className="space-y-1.5 text-xs font-mono">
                <div className="flex justify-between p-2 rounded-xl bg-neutral-950 border border-neutral-800/60">
                  <span className="text-neutral-300">NIFTY ETF Holding</span>
                  <span className="text-lime-400 font-bold">+₹820</span>
                </div>
                <div className="flex justify-between p-2 rounded-xl bg-neutral-950 border border-neutral-800/60">
                  <span className="text-neutral-300">Reliance Industries</span>
                  <span className="text-lime-400 font-bold">+₹540</span>
                </div>
                <div className="flex justify-between p-2 rounded-xl bg-neutral-950 border border-neutral-800/60">
                  <span className="text-neutral-300">HDFC Bank Ltd.</span>
                  <span className="text-rose-500 font-bold">-₹120</span>
                </div>
              </div>
            </div>

            <p className="text-xs text-neutral-400 font-mono bg-neutral-950 p-3 rounded-xl border border-neutral-800/80">
              Insight: Your portfolio is currently tracking closely to index performance with lower downside volatility.
            </p>
          </div>

          {/* Finova Market Intelligence */}
          <div className="bg-neutral-900/90 border border-lime-400/30 p-6 rounded-3xl flex flex-col justify-between space-y-4 shadow-xl">
            <div className="flex justify-between items-start border-b border-neutral-800/80 pb-3">
              <div>
                <span className="text-lime-400 font-mono text-xs font-extrabold uppercase tracking-widest block">
                  Finova Market Intelligence
                </span>
                <h2 className="text-base font-bold text-white mt-0.5">Custom Impact Analysis</h2>
              </div>
              <span className="text-[10px] font-mono uppercase bg-lime-400/10 text-lime-400 border border-lime-400/30 px-2.5 py-1 rounded-full">
                Personalized
              </span>
            </div>

            <div className="bg-neutral-950 p-5 rounded-2xl border border-neutral-800/80 space-y-3">
              <div className="flex items-center justify-between text-xs font-mono">
                <span className="text-neutral-400">Sector Movement Highlight</span>
                <span className="text-lime-400 font-bold">NIFTY IT (+2.1%)</span>
              </div>
              <p className="text-xs text-neutral-300 leading-relaxed">
                NIFTY IT experienced a strong rally today. Based on your onboarded records, you currently have <span className="text-white font-bold">18% allocation</span> exposed to IT equities.
              </p>
              <div className="bg-neutral-900 p-3 rounded-xl border border-neutral-800/60 flex justify-between items-center text-xs font-mono">
                <span className="text-neutral-400">Direct Portfolio Gain:</span>
                <span className="text-lime-400 font-extrabold text-sm">+₹1,240</span>
              </div>
            </div>

            <button
              onClick={() => navigate("/portfolio")}
              className="w-full bg-lime-400 text-black font-extrabold py-3 rounded-xl text-xs hover:bg-lime-300 shadow-md shadow-lime-400/10 transition-all cursor-pointer flex items-center justify-center gap-2"
            >
              <span>View My Portfolio</span>
              <span>→</span>
            </button>
          </div>

        </div>

        {/* 4. MARKET MOVERS & SECTOR PERFORMANCE */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Top Gainers */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-4">
            <div className="flex justify-between items-center border-b border-neutral-800/80 pb-3">
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Top Gainers
              </h2>
              <span className="text-[10px] font-mono text-lime-400">NIFTY 50</span>
            </div>

            <div className="space-y-2">
              {topGainers.map((stock) => (
                <div
                  key={stock.symbol}
                  onClick={() => setSelectedModalStock(stock)}
                  className="bg-neutral-950 border border-neutral-800/80 hover:border-neutral-700 p-3 rounded-2xl flex justify-between items-center cursor-pointer transition-all"
                >
                  <div>
                    <span className="text-xs font-bold text-white block">{stock.symbol}</span>
                    <span className="text-[10px] font-mono text-neutral-500 block">{stock.name}</span>
                  </div>
                  <div className="text-right font-mono">
                    <span className="text-xs font-bold text-white block">{stock.price}</span>
                    <span className="text-xs font-bold text-lime-400 block">{stock.change}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Top Losers */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-4">
            <div className="flex justify-between items-center border-b border-neutral-800/80 pb-3">
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Top Losers
              </h2>
              <span className="text-[10px] font-mono text-rose-500">NIFTY 50</span>
            </div>

            <div className="space-y-2">
              {topLosers.map((stock) => (
                <div
                  key={stock.symbol}
                  onClick={() => setSelectedModalStock(stock)}
                  className="bg-neutral-950 border border-neutral-800/80 hover:border-neutral-700 p-3 rounded-2xl flex justify-between items-center cursor-pointer transition-all"
                >
                  <div>
                    <span className="text-xs font-bold text-white block">{stock.symbol}</span>
                    <span className="text-[10px] font-mono text-neutral-500 block">{stock.name}</span>
                  </div>
                  <div className="text-right font-mono">
                    <span className="text-xs font-bold text-white block">{stock.price}</span>
                    <span className="text-xs font-bold text-rose-500 block">{stock.change}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Sector Performance */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-4">
            <div className="flex justify-between items-center border-b border-neutral-800/80 pb-3">
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Sector Performance
              </h2>
              <span className="text-[10px] font-mono text-neutral-500">Daily Heatmap</span>
            </div>

            <div className="space-y-3">
              {sectorPerformance.map((sec) => (
                <div key={sec.name} className="space-y-1">
                  <div className="flex justify-between text-xs font-mono">
                    <span className="text-neutral-300">{sec.name}</span>
                    <span className={sec.pos ? "text-lime-400 font-bold" : "text-rose-500 font-bold"}>
                      {sec.pct}
                    </span>
                  </div>
                  <div className="w-full bg-neutral-950 h-2 rounded-full overflow-hidden">
                    <div
                      className={`h-full rounded-full ${sec.pos ? "bg-lime-400" : "bg-rose-500"}`}
                      style={{ width: sec.width }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>

        </div>

        {/* 5. MARKET NEWS WITH "WHY IT MATTERS" */}
        <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-6">
          <div className="flex justify-between items-center border-b border-neutral-800/80 pb-4">
            <div>
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Market News & Context
              </h2>
              <span className="text-xs font-mono text-neutral-500">Curated intelligence with financial implications</span>
            </div>
            <span className="text-[10px] font-mono bg-neutral-950 border border-neutral-800 px-3 py-1 rounded-full text-neutral-400">
              Live Feed
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {newsItems.map((item) => (
              <div
                key={item.id}
                className="bg-neutral-950 border border-neutral-800/80 p-5 rounded-2xl flex flex-col justify-between space-y-4 hover:border-neutral-700 transition-colors"
              >
                <div className="space-y-2">
                  <div className="flex justify-between items-center text-[10px] font-mono text-neutral-500">
                    <span>{item.source}</span>
                    <span>{item.time}</span>
                  </div>
                  <h3 className="text-xs font-bold text-white leading-snug">{item.title}</h3>
                  <p className="text-[11px] text-neutral-400 leading-relaxed">{item.snippet}</p>
                </div>

                {/* "Why it matters" Callout */}
                <div className="bg-neutral-900/90 border border-neutral-800 p-3 rounded-xl space-y-1">
                  <span className="text-[10px] font-mono font-bold uppercase tracking-wider text-lime-400 block">
                    Why it matters
                  </span>
                  <p className="text-[11px] text-neutral-300 leading-normal">{item.whyItMatters}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 6. STOCKS TO WATCH & WATCHLIST */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Stocks to Watch (2 Columns) */}
          <div className="lg:col-span-2 bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-4">
            <div className="flex justify-between items-center border-b border-neutral-800/80 pb-3">
              <div>
                <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                  Stocks to Watch
                </h2>
                <span className="text-xs font-mono text-neutral-500">Algorithmic observation list (Non-advisory)</span>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              {stocksToWatch.map((s) => (
                <div key={s.symbol} className="bg-neutral-950 border border-neutral-800/80 p-4 rounded-2xl space-y-3">
                  <div>
                    <span className="text-xs font-bold text-white block">{s.symbol}</span>
                    <span className="text-[10px] font-mono text-neutral-500 uppercase">{s.sector}</span>
                  </div>

                  <div className="space-y-1.5 text-[10px] font-mono">
                    <div>
                      <div className="flex justify-between text-neutral-400 mb-0.5">
                        <span>Momentum</span>
                        <span>{s.momentum}%</span>
                      </div>
                      <div className="w-full bg-neutral-900 h-1 rounded-full">
                        <div className="bg-lime-400 h-full rounded-full" style={{ width: `${s.momentum}%` }} />
                      </div>
                    </div>
                    <div>
                      <div className="flex justify-between text-neutral-400 mb-0.5">
                        <span>Valuation</span>
                        <span>{s.valuation}%</span>
                      </div>
                      <div className="w-full bg-neutral-900 h-1 rounded-full">
                        <div className="bg-blue-400 h-full rounded-full" style={{ width: `${s.valuation}%` }} />
                      </div>
                    </div>
                  </div>

                  <p className="text-[11px] text-neutral-400 leading-snug pt-1 border-t border-neutral-900">
                    {s.reason}
                  </p>
                </div>
              ))}
            </div>
          </div>

          {/* Personal Watchlist */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-4">
            <div className="flex justify-between items-center border-b border-neutral-800/80 pb-3">
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Your Watchlist
              </h2>
              <span className="text-[10px] font-mono text-neutral-500">{watchlist.length} items</span>
            </div>

            <div className="space-y-2">
              {watchlist.map((item) => (
                <div key={item.symbol} className="bg-neutral-950 border border-neutral-800/80 p-3 rounded-2xl flex justify-between items-center">
                  <div>
                    <span className="text-xs font-bold text-white block">{item.symbol}</span>
                    <span className="text-[10px] font-mono text-neutral-500 block">{item.name}</span>
                  </div>
                  <div className="flex items-center gap-3 font-mono">
                    <div className="text-right">
                      <span className="text-xs font-bold text-white block">{item.price}</span>
                      <span className={`text-[10px] font-bold block ${item.positive ? "text-lime-400" : "text-rose-500"}`}>
                        {item.change}
                      </span>
                    </div>
                    <button
                      onClick={() => removeFromWatchlist(item.symbol)}
                      className="text-neutral-600 hover:text-rose-400 text-xs px-1"
                      title="Remove"
                    >
                      ✕
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>

        </div>

      </main>

      {/* Stock Modal Details */}
      {selectedModalStock && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-neutral-900 border border-neutral-800 p-6 rounded-3xl max-w-sm w-full space-y-4">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="text-lg font-bold text-white">{selectedModalStock.symbol}</h3>
                <span className="text-xs text-neutral-400 font-mono">{selectedModalStock.name}</span>
              </div>
              <button
                onClick={() => setSelectedModalStock(null)}
                className="text-neutral-400 hover:text-white text-sm"
              >
                ✕
              </button>
            </div>
            <div className="bg-neutral-950 p-4 rounded-2xl border border-neutral-800 flex justify-between font-mono">
              <span className="text-xs text-neutral-400">Current Price</span>
              <span className="text-sm font-bold text-white">{selectedModalStock.price}</span>
            </div>
            <button
              onClick={() => setSelectedModalStock(null)}
              className="w-full bg-lime-400 text-black font-bold py-2.5 rounded-xl text-xs hover:bg-lime-300"
            >
              Close Snapshot
            </button>
          </div>
        </div>
      )}

    </div>
  );
}