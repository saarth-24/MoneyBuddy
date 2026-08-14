import React, { useState } from "react";
import Navbar from "../../components/Navbar/Navbar";

export default function PortfolioPage() {
  // State for AI Decision Tab Selector
  const [activeRecommendation, setActiveRecommendation] = useState("save");

  // State for Interactive Holdings Filter
  const [selectedAssetFilter, setSelectedAssetFilter] = useState("All");

  // Holdings Data
  const holdings = [
    { name: "NIFTY 50 ETF", category: "Stocks", value: 72400, returnRate: "+16.7%", positive: true },
    { name: "HDFC Flexi Cap Fund", category: "Mutual Funds", value: 82400, returnRate: "+14.2%", positive: true },
    { name: "Reliance Industries", category: "Stocks", value: 54200, returnRate: "+8.2%", positive: true },
    { name: "Sovereign Gold Bond", category: "Gold", value: 43000, returnRate: "+9.4%", positive: true },
    { name: "ICICI Prudential Liquid Fund", category: "Debt/Liquid", value: 65000, returnRate: "+6.8%", positive: true },
  ];

  // Loan data
  // Replace this with the loan data coming from your earlier user form
  const loans = [
    {
      name: "Personal Loan",
      type: "Personal",
      balance: 120000,
      interestRate: 12.5,
      tenure: "24 months",
    },

    // Example of more loans:
    // {
    //   name: "Education Loan",
    //   type: "Education",
    //   balance: 250000,
    //   interestRate: 8.5,
    //   tenure: "48 months",
    // },
    // {
    //   name: "Car Loan",
    //   type: "Vehicle",
    //   balance: 180000,
    //   interestRate: 9.2,
    //   tenure: "36 months",
    // },
  ];

  // Highest interest rate = highest priority
  const prioritizedLoans = [...loans].sort(
    (a, b) => b.interestRate - a.interestRate
  );

  const topPriorityLoan = prioritizedLoans[0];

  const filteredHoldings = selectedAssetFilter === "All"
    ? holdings
    : holdings.filter(h => h.category === selectedAssetFilter);



  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100 flex flex-col selection:bg-lime-400 selection:text-black">

      {/* Integrated Navbar */}
      <Navbar />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">

        {/* PAGE TITLE & ACTION BAR */}
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-neutral-900 pb-6">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-lime-400 mb-1">
              <span className="w-2 h-2 rounded-full bg-lime-400 animate-pulse" />
              Decision Center
            </div>
            <h1 className="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
              Financial Portfolio
            </h1>
            <p className="text-neutral-400 text-xs sm:text-sm mt-1">
              Real-time wealth tracking, cashflow diagnostics, and AI decision intelligence.
            </p>
          </div>

        </div>

        {/* 1. TOP — FINANCIAL SNAPSHOT METRICS */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-neutral-900/80 border border-neutral-800/80 hover:border-neutral-700 p-5 rounded-2xl transition-all">
            <span className="text-[11px] font-mono text-neutral-400 uppercase tracking-wider">Net Worth</span>
            <div className="text-2xl font-bold text-white mt-1">₹8,42,000</div>
            <div className="text-xs font-medium text-lime-400 mt-2 flex items-center gap-1">
              <span>↑ 8.4%</span>
              <span className="text-neutral-500 font-normal">vs last month</span>
            </div>
          </div>

          <div className="bg-neutral-900/80 border border-neutral-800/80 hover:border-neutral-700 p-5 rounded-2xl transition-all">
            <span className="text-[11px] font-mono text-neutral-400 uppercase tracking-wider">Invested Assets</span>
            <div className="text-2xl font-bold text-white mt-1">₹5,24,000</div>
            <div className="text-xs font-medium text-lime-400 mt-2 flex items-center gap-1">
              <span>↑ 12.2%</span>
              <span className="text-neutral-500 font-normal">unrealized gain</span>
            </div>
          </div>

          <div className="bg-neutral-900/80 border border-neutral-800/80 hover:border-neutral-700 p-5 rounded-2xl transition-all">
            <span className="text-[11px] font-mono text-neutral-400 uppercase tracking-wider">Liquid Savings</span>
            <div className="text-2xl font-bold text-white mt-1">₹1,86,000</div>
            <div className="text-xs font-medium text-neutral-400 mt-2">
              <span className="text-white font-semibold">23%</span> of income
            </div>
          </div>

          <div className="bg-neutral-900/80 border border-neutral-800/80 hover:border-neutral-700 p-5 rounded-2xl transition-all">
            <span className="text-[11px] font-mono text-neutral-400 uppercase tracking-wider">Active Liabilities</span>
            <div className="text-2xl font-bold text-white mt-1">₹2,40,000</div>
            <div className="text-xs font-medium text-neutral-400 mt-2">
              <span className="text-neutral-300 font-semibold">-₹8,000</span>/month commitment
            </div>
          </div>
        </div>

        {/* 2. CASHFLOW & WEALTH ALLOCATION CHARTS */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

          {/* Income Flow Ring */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl flex flex-col justify-between">
            <div className="flex justify-between items-start mb-4">
              <div>
                <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                  Monthly Cashflow Allocation
                </h2>
                <span className="text-xs font-mono text-neutral-500">Inflow: ₹75,000 / month</span>
              </div>
              <span className="text-[10px] font-mono bg-neutral-800 text-neutral-300 px-2.5 py-1 rounded-full border border-neutral-700">
                Insight
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 items-center my-auto">
              <div className="relative w-36 h-36 mx-auto">
                <svg className="w-full h-full -rotate-90" viewBox="0 0 36 36">
                  <path className="text-neutral-800" strokeWidth="3.8" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                  <path className="text-neutral-500" strokeDasharray="20, 100" strokeWidth="3.8" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                  <path className="text-lime-400" strokeDasharray="25, 100" strokeDashoffset="-20" strokeWidth="3.8" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                  <path className="text-emerald-500" strokeDasharray="20, 100" strokeDashoffset="-45" strokeWidth="3.8" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                  <path className="text-neutral-600" strokeDasharray="15, 100" strokeDashoffset="-65" strokeWidth="3.8" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                </svg>
                <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
                  <span className="text-[10px] font-mono text-neutral-500 uppercase">Allocated</span>
                  <span className="text-sm font-extrabold text-white">100%</span>
                </div>
              </div>

              <div className="space-y-2 text-xs">
                <div className="flex justify-between items-center"><span className="text-neutral-400">Investments</span><span className="text-lime-400 font-mono font-semibold">25% (₹18.7K)</span></div>
                <div className="flex justify-between items-center"><span className="text-neutral-400">Savings</span><span className="text-emerald-400 font-mono font-semibold">20% (₹15.0K)</span></div>
                <div className="flex justify-between items-center"><span className="text-neutral-400">Rent</span><span className="text-neutral-300 font-mono">20% (₹15.0K)</span></div>
                <div className="flex justify-between items-center"><span className="text-neutral-400">Household</span><span className="text-neutral-300 font-mono">15% (₹11.2K)</span></div>
                <div className="flex justify-between items-center"><span className="text-neutral-400">EMI & Obligations</span><span className="text-neutral-300 font-mono">20% (₹15.0K)</span></div>
              </div>
            </div>
          </div>

          {/* Current Asset Breakdown */}
          <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl flex flex-col justify-between">
            <div className="flex justify-between items-start mb-4">
              <div>
                <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                  Asset Distribution
                </h2>
                <span className="text-xs font-mono text-neutral-500">Current Portfolio Split</span>
              </div>
              <span className="text-[10px] font-mono bg-neutral-800 text-neutral-300 px-2.5 py-1 rounded-full border border-neutral-700">
                Insight
              </span>
            </div>

            <div className="space-y-2.5 my-auto">
              {[
                { name: "Equity & Stocks", pct: 35, val: "₹2,94,700", color: "bg-lime-400" },
                { name: "Mutual Funds", pct: 25, val: "₹2,10,500", color: "bg-emerald-400" },
                { name: "Bank Savings", pct: 18, val: "₹1,51,560", color: "bg-teal-400" },
                { name: "Fixed Deposits", pct: 12, val: "₹1,01,040", color: "bg-neutral-400" },
                { name: "Gold & Precious Metals", pct: 6, val: "₹50,520", color: "bg-amber-400" },
                { name: "Cash Liquidity", pct: 4, val: "₹33,680", color: "bg-neutral-600" },
              ].map((asset) => (
                <div key={asset.name} className="space-y-1">
                  <div className="flex justify-between text-xs">
                    <span className="text-neutral-300 font-medium">{asset.name}</span>
                    <span className="font-mono text-neutral-400 text-[11px]">{asset.val} ({asset.pct}%)</span>
                  </div>
                  <div className="w-full bg-neutral-950 h-1.5 rounded-full overflow-hidden">
                    <div className={`${asset.color} h-full rounded-full`} style={{ width: `${asset.pct}%` }} />
                  </div>
                </div>
              ))}
            </div>
          </div>

        </div>

        {/* 3. INTERACTIVE INVESTMENT HOLDINGS */}
        <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-6">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 border-b border-neutral-800/80 pb-4">
            <div>
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Investment Holdings
              </h2>
              <span className="text-xs font-mono text-neutral-500">Overall Yield: +₹62,680 (+13.06%)</span>
            </div>

            {/* Asset Category Filter Chips */}
            <div className="flex flex-wrap gap-1.5">
              {["All", "Stocks", "Mutual Funds", "Gold", "Debt/Liquid"].map((cat) => (
                <button
                  key={cat}
                  onClick={() => setSelectedAssetFilter(cat)}
                  className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${selectedAssetFilter === cat
                    ? "bg-lime-400 text-black font-semibold"
                    : "bg-neutral-950 border border-neutral-800 text-neutral-400 hover:text-white"
                    }`}
                >
                  {cat}
                </button>
              ))}
            </div>
          </div>

          {/* Holdings Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {filteredHoldings.map((inv) => (
              <div key={inv.name} className="bg-neutral-950 border border-neutral-800/80 p-4 rounded-xl flex items-center justify-between hover:border-neutral-700 transition-colors">
                <div>
                  <span className="text-xs font-semibold text-white block">{inv.name}</span>
                  <span className="text-[10px] font-mono text-neutral-500 uppercase">{inv.category}</span>
                  <span className="text-sm font-mono text-neutral-300 font-bold block mt-1">₹{inv.value.toLocaleString()}</span>
                </div>
                <span className="text-xs font-mono font-bold text-lime-400 bg-lime-400/10 px-2.5 py-1 rounded-lg border border-lime-400/20">
                  {inv.returnRate}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* 4. 🔥 FINOVA AI DECISION ENGINE */}
        <div className="bg-neutral-900/90 border border-lime-400/30 p-6 sm:p-8 rounded-3xl space-y-6 relative overflow-hidden shadow-2xl">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-neutral-800/80 pb-4">
            <div>
              <span className="text-lime-400 font-mono text-xs font-extrabold uppercase tracking-widest">
                ✦ Finova AI Decision Engine
              </span>
              <p className="text-neutral-300 text-xs sm:text-sm mt-1">
                4 personalized financial optimizations identified based on your current cashflow.
              </p>
            </div>
            <span className="text-[10px] font-mono uppercase bg-lime-400/10 text-lime-400 border border-lime-400/30 px-3 py-1 rounded-full">
              Educational Model
            </span>
          </div>

          {/* Dynamic Action Tabs */}
          <div className="flex flex-wrap gap-2">
            {[
              { id: "save", label: "1. Emergency Reserve", badge: "Recommendation" },
              { id: "invest", label: "2. Surplus Deployment", badge: "Recommendation" },
              { id: "card", label: "3. Card Reward Match", badge: "Insight" },
              { id: "debt", label: "4. Debt Paydown Strategy", badge: "Recommendation" },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveRecommendation(tab.id)}
                className={`px-4 py-2.5 rounded-xl text-xs font-medium transition-all ${activeRecommendation === tab.id
                  ? "bg-lime-400 text-black font-semibold shadow-md shadow-lime-400/20"
                  : "bg-neutral-950 border border-neutral-800 text-neutral-400 hover:text-white"
                  }`}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* TAB CONTENT CARDS */}
          {activeRecommendation === "save" && (
            <div className="bg-neutral-950 border border-neutral-800/80 p-5 rounded-2xl space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-[11px] font-mono text-lime-400 uppercase tracking-wider">Recommendation · Capital Protection</span>
                <span className="text-xs text-neutral-500 font-mono">Target: 6 Months Buffer</span>
              </div>
              <h3 className="text-base font-bold text-white">Emergency Reserve Target</h3>
              <p className="text-xs text-neutral-400 leading-relaxed">
                Based on your monthly fixed expenses of ₹32,000, we recommend securing a 6-month liquidity buffer of ₹1.92L before increasing equity exposure.
              </p>

              <div className="bg-neutral-900/80 p-4 rounded-xl space-y-2 border border-neutral-800/60">
                <div className="flex justify-between text-xs font-mono">
                  <span className="text-neutral-400">Current Progress (₹1,20,000 / ₹1,92,000)</span>
                  <span className="text-lime-400 font-bold">62%</span>
                </div>
                <div className="w-full bg-neutral-950 h-2 rounded-full overflow-hidden">
                  <div className="bg-lime-400 h-full rounded-full" style={{ width: "62%" }} />
                </div>
                <div className="flex justify-between text-[11px] text-neutral-500 pt-1 font-mono">
                  <span>Remaining: ₹72,000</span>
                  <span>Suggested Allocation: ₹6,000 / month</span>
                </div>
              </div>
            </div>
          )}

          {activeRecommendation === "invest" && (
            <div className="bg-neutral-950 border border-neutral-800/80 p-5 rounded-2xl space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-[11px] font-mono text-lime-400 uppercase tracking-wider">Recommendation · Wealth Accumulation</span>
                <span className="text-xs text-neutral-500 font-mono">Moderate Risk Profile</span>
              </div>
              <h3 className="text-base font-bold text-white">Surplus Cash Allocation</h3>
              <p className="text-xs text-neutral-400 leading-relaxed">
                After accounting for essential expenses and savings commitments, you have ~₹11,000 in monthly disposable capacity.
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
                <div className="bg-neutral-900/80 p-4 rounded-xl border border-neutral-800/60">
                  <span className="text-[11px] text-neutral-400 block">Suggested Monthly Investment</span>
                  <span className="text-lg font-bold text-lime-400 block mt-1 font-mono">₹7,000 / month</span>
                </div>
                <div className="bg-neutral-900/80 p-4 rounded-xl border border-neutral-800/60 space-y-1">
                  <span className="text-[11px] text-neutral-400 block">Recommended Asset Split</span>
                  <div className="text-xs font-mono space-y-0.5">
                    <div className="flex justify-between"><span className="text-neutral-300">Equity Index Funds</span><span className="text-lime-400">70%</span></div>
                    <div className="flex justify-between"><span className="text-neutral-300">Fixed Income / Debt</span><span className="text-neutral-400">30%</span></div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeRecommendation === "card" && (
            <div className="bg-neutral-950 border border-neutral-800/80 p-5 rounded-2xl space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-[11px] font-mono text-lime-400 uppercase tracking-wider">Insight · Reward Maximization</span>
                <span className="text-xs text-neutral-500 font-mono">Sample Spend: ₹8,000</span>
              </div>
              <h3 className="text-base font-bold text-white">Optimal Credit Card Selector</h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div className="bg-neutral-900/80 border border-neutral-800/60 p-4 rounded-xl">
                  <span className="text-[11px] text-neutral-500 font-mono">Card A · Standard Card</span>
                  <div className="text-sm font-bold text-white mt-1">1% Cashback</div>
                  <div className="text-xs text-neutral-500 font-mono">Yield: ₹80</div>
                </div>
                <div className="bg-neutral-900/80 border border-lime-400/50 p-4 rounded-xl">
                  <span className="text-[11px] text-lime-400 font-mono font-bold">Card B · Recommended Option</span>
                  <div className="text-sm font-bold text-white mt-1">5% Category Reward</div>
                  <div className="text-xs text-lime-400 font-mono font-bold">Yield: ₹400</div>
                </div>
              </div>
              <p className="text-xs text-neutral-300 font-mono bg-neutral-900/80 p-3 rounded-xl border border-neutral-800">
                ✦ Outcome: Card B yields an extra <span className="text-lime-400 font-bold">₹320 value</span> on this category purchase.
              </p>
            </div>
          )}

          {activeRecommendation === "debt" && (
            <div className="bg-neutral-950 border border-neutral-800/80 p-5 rounded-2xl space-y-5">

              {/* Header */}
              <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-3">
                <div>
                  <span className="text-[11px] font-mono text-lime-400 uppercase tracking-wider">
                    Recommendation · Interest Optimization
                  </span>

                  <h3 className="text-base font-bold text-white mt-1">
                    Pay Your Highest-Interest Loan First
                  </h3>

                  <p className="text-xs text-neutral-500 mt-1">
                    Your loans are ranked automatically by interest rate.
                  </p>
                </div>

                <span className="text-[10px] font-mono uppercase bg-lime-400/10 text-lime-400 border border-lime-400/30 px-3 py-1.5 rounded-full w-fit">
                  Debt Avalanche
                </span>
              </div>


              {/* TOP PRIORITY LOAN */}
              {topPriorityLoan && (
                <div className="relative overflow-hidden bg-gradient-to-br from-lime-400/10 via-neutral-900 to-neutral-900 border border-lime-400/30 rounded-2xl p-5">

                  <div className="absolute top-0 right-0 w-32 h-32 bg-lime-400/5 rounded-full blur-3xl" />

                  <div className="relative">

                    {/* Loan heading */}
                    <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">

                      <div className="flex items-center gap-3">

                        {/* Number */}
                        <div className="w-11 h-11 rounded-xl bg-lime-400 text-black flex items-center justify-center font-black text-lg shadow-lg shadow-lime-400/20">
                          #1
                        </div>

                        <div>
                          <span className="text-[10px] text-lime-400 font-mono uppercase tracking-wider font-bold">
                            Pay This Loan First
                          </span>

                          <div className="text-lg font-bold text-white">
                            {topPriorityLoan.name}
                          </div>

                          <div className="text-[11px] text-neutral-500 font-mono">
                            {topPriorityLoan.type} Loan
                          </div>
                        </div>

                      </div>


                      {/* Interest rate */}
                      <div className="text-left sm:text-right">

                        <div className="text-[10px] text-neutral-500 uppercase tracking-wider">
                          Interest Rate
                        </div>

                        <div className="text-3xl font-black text-lime-400 font-mono">
                          {topPriorityLoan.interestRate}%
                        </div>

                        <div className="text-[10px] text-neutral-500">
                          per annum
                        </div>

                      </div>

                    </div>


                    {/* Loan details */}
                    <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 mt-5 pt-4 border-t border-neutral-800/80">

                      <div>
                        <span className="text-[10px] text-neutral-500 uppercase tracking-wider">
                          Outstanding
                        </span>

                        <div className="text-sm font-bold text-white font-mono mt-1">
                          ₹{topPriorityLoan.balance.toLocaleString()}
                        </div>
                      </div>


                      <div>
                        <span className="text-[10px] text-neutral-500 uppercase tracking-wider">
                          Remaining Tenure
                        </span>

                        <div className="text-sm font-bold text-white font-mono mt-1">
                          {topPriorityLoan.tenure}
                        </div>
                      </div>


                      <div>
                        <span className="text-[10px] text-neutral-500 uppercase tracking-wider">
                          Priority
                        </span>

                        <div className="text-sm font-bold text-lime-400 font-mono mt-1">
                          Highest
                        </div>
                      </div>

                    </div>

                  </div>
                </div>
              )}


              {/* WHY THIS LOAN? */}
              {topPriorityLoan && (
                <div className="bg-lime-400/5 border border-lime-400/20 rounded-xl p-4">

                  <div className="flex items-start gap-3">

                    <div className="w-8 h-8 rounded-lg bg-lime-400/10 border border-lime-400/20 flex items-center justify-center text-lime-400">
                      ✦
                    </div>

                    <div>
                      <h4 className="text-xs font-bold text-white">
                        Why should you pay this first?
                      </h4>

                      <p className="text-xs text-neutral-400 leading-relaxed mt-1">
                        {topPriorityLoan.name} has the highest interest rate
                        at{" "}
                        <span className="text-lime-400 font-bold">
                          {topPriorityLoan.interestRate}%
                        </span>
                        . Paying it down first can reduce the amount of
                        interest you pay over time.
                      </p>
                    </div>

                  </div>

                </div>
              )}


              {/* PRIORITY RANKING */}
              <div>

                <div className="flex justify-between items-center mb-3">

                  <div>
                    <span className="text-[11px] font-semibold text-neutral-300 uppercase tracking-wider">
                      Paydown Priority
                    </span>

                    <p className="text-[10px] text-neutral-500 mt-0.5">
                      Highest interest → lowest interest
                    </p>
                  </div>

                  <span className="text-[10px] font-mono text-neutral-500">
                    {prioritizedLoans.length}{" "}
                    {prioritizedLoans.length === 1 ? "loan" : "loans"}
                  </span>

                </div>


                <div className="space-y-2">

                  {prioritizedLoans.map((loan, index) => (

                    <div
                      key={loan.name}
                      className={`flex items-center gap-3 p-3 rounded-xl border transition-all ${index === 0
                        ? "bg-lime-400/5 border-lime-400/30"
                        : "bg-neutral-900/70 border-neutral-800/70"
                        }`}
                    >

                      {/* Ranking number */}
                      <div
                        className={`w-8 h-8 rounded-lg flex items-center justify-center text-[11px] font-bold font-mono ${index === 0
                          ? "bg-lime-400 text-black"
                          : "bg-neutral-800 text-neutral-400"
                          }`}
                      >
                        {index + 1}
                      </div>


                      {/* Loan information */}
                      <div className="flex-1 min-w-0">

                        <div className="flex items-center gap-2">

                          <span className="text-xs font-semibold text-white truncate">
                            {loan.name}
                          </span>

                          {index === 0 && (
                            <span className="text-[8px] uppercase font-bold text-lime-400 bg-lime-400/10 border border-lime-400/20 px-1.5 py-0.5 rounded">
                              Start Here
                            </span>
                          )}

                        </div>

                        <div className="text-[10px] text-neutral-500 font-mono mt-0.5">
                          ₹{loan.balance.toLocaleString()} outstanding
                        </div>

                      </div>


                      {/* Interest rate */}
                      <div className="text-right">

                        <div
                          className={`text-sm font-bold font-mono ${index === 0
                            ? "text-lime-400"
                            : "text-neutral-300"
                            }`}
                        >
                          {loan.interestRate}%
                        </div>

                        <div className="text-[9px] text-neutral-600 uppercase">
                          APR
                        </div>

                      </div>

                    </div>

                  ))}

                </div>

              </div>


              {/* STRATEGY EXPLANATION */}
              <div className="bg-neutral-900/80 p-4 rounded-xl border border-neutral-800/60">

                <div className="flex items-center gap-2 mb-2">

                  <div className="w-2 h-2 rounded-full bg-lime-400" />

                  <span className="text-[11px] font-bold text-neutral-300 uppercase tracking-wider">
                    Recommended Strategy
                  </span>

                </div>

                <p className="text-xs text-neutral-400 leading-relaxed">
                  Continue making the minimum payments on all loans, but direct
                  any extra repayment amount toward the loan with the highest
                  interest rate. Once that loan is cleared, move to the next
                  highest-rate loan.
                </p>

              </div>

            </div>
          )}

          <p className="text-[10px] text-neutral-600 font-mono text-center pt-2">
            * Finova AI provides educational decision insights based on user input. These models do not constitute regulated financial advice.
          </p>
        </div>


        {/* 5. FINANCIAL PRIORITY SECTION */}
        {/* 5. FINANCIAL PRIORITY GRAPH */}
        <div className="bg-neutral-900/80 border border-neutral-800/80 p-6 rounded-3xl space-y-6">

          {/* Header */}
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 border-b border-neutral-800/80 pb-4">

            <div>
              <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                Financial Priority
              </h2>

              <p className="text-xs font-mono text-neutral-500 mt-1">
                Recommended priority for your financial decisions
              </p>
            </div>

            <span className="text-xs font-mono bg-lime-400/10 text-lime-400 border border-lime-400/20 px-3 py-1 rounded-full">
              Priority Guide
            </span>

          </div>


          {/* Graph */}
          <div className="bg-neutral-950 border border-neutral-800/80 rounded-2xl p-5">

            <div className="flex items-center justify-between mb-6">

              <div>
                <h3 className="text-sm font-semibold text-white">
                  Priority Ranking
                </h3>

                <p className="text-[11px] text-neutral-500 mt-1">
                  Higher the bar, higher the priority
                </p>
              </div>

              <span className="text-[10px] font-mono text-neutral-600">
                DUMMY DATA
              </span>

            </div>


            {/* Vertical Bar Graph */}
            <div className="h-72 flex items-end justify-around gap-3 sm:gap-6 border-b border-neutral-800 pb-0">

              {/* Emergency Fund */}
              <div className="h-full flex flex-col justify-end items-center flex-1">

                <span className="text-xs font-mono font-bold text-lime-400 mb-2">
                  95%
                </span>

                <div className="w-full max-w-[65px] h-[95%] bg-lime-400 rounded-t-xl hover:bg-lime-300 transition-all duration-300 shadow-lg shadow-lime-400/10" />

                <div className="mt-3 text-center">
                  <p className="text-[10px] sm:text-xs font-semibold text-white">
                    Emergency
                  </p>

                  <p className="text-[9px] sm:text-[10px] text-neutral-500">
                    Fund
                  </p>
                </div>

              </div>


              {/* Debt */}
              <div className="h-full flex flex-col justify-end items-center flex-1">

                <span className="text-xs font-mono font-bold text-orange-400 mb-2">
                  85%
                </span>

                <div className="w-full max-w-[65px] h-[85%] bg-orange-400 rounded-t-xl hover:bg-orange-300 transition-all duration-300" />

                <div className="mt-3 text-center">
                  <p className="text-[10px] sm:text-xs font-semibold text-white">
                    High-Interest
                  </p>

                  <p className="text-[9px] sm:text-[10px] text-neutral-500">
                    Debt
                  </p>
                </div>

              </div>


              {/* Insurance */}
              <div className="h-full flex flex-col justify-end items-center flex-1">

                <span className="text-xs font-mono font-bold text-blue-400 mb-2">
                  70%
                </span>

                <div className="w-full max-w-[65px] h-[70%] bg-blue-400 rounded-t-xl hover:bg-blue-300 transition-all duration-300" />

                <div className="mt-3 text-center">
                  <p className="text-[10px] sm:text-xs font-semibold text-white">
                    Insurance
                  </p>

                  <p className="text-[9px] sm:text-[10px] text-neutral-500">
                    Protection
                  </p>
                </div>

              </div>


              {/* Investing */}
              <div className="h-full flex flex-col justify-end items-center flex-1">

                <span className="text-xs font-mono font-bold text-emerald-400 mb-2">
                  55%
                </span>

                <div className="w-full max-w-[65px] h-[55%] bg-emerald-400 rounded-t-xl hover:bg-emerald-300 transition-all duration-300" />

                <div className="mt-3 text-center">
                  <p className="text-[10px] sm:text-xs font-semibold text-white">
                    Long-Term
                  </p>

                  <p className="text-[9px] sm:text-[10px] text-neutral-500">
                    Investing
                  </p>
                </div>

              </div>

            </div>


            {/* Priority Scale */}
            <div className="flex justify-between text-[9px] text-neutral-600 font-mono mt-3 px-1">
              <span>0</span>
              <span>25</span>
              <span>50</span>
              <span>75</span>
              <span>100</span>
            </div>

          </div>


          {/* Insight */}
          <div className="flex items-start gap-3 bg-lime-400/5 border border-lime-400/10 p-4 rounded-2xl">

            <span className="text-lime-400 text-lg">
              ✦
            </span>

            <div>

              <p className="text-xs font-semibold text-white">
                Priority Insight
              </p>

              <p className="text-[11px] text-neutral-500 mt-1 leading-relaxed">
                Your financial foundation should come first. Build an emergency
                fund, manage high-interest debt, protect yourself with insurance,
                and then focus on long-term investing.
              </p>

            </div>

          </div>

          {/* 6. FUTURE FINANCIAL HEALTH */}
          {/* 6. FUTURE FINANCIAL HEALTH */}
          <div className="bg-neutral-900/80 border border-neutral-800 p-6 rounded-3xl space-y-6">

            {/* Header */}
            <div className="flex flex-col sm:flex-row justify-between sm:items-center gap-3 border-b border-neutral-800/80 pb-4">
              <div>
                <div className="flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-400" />

                  <h2 className="text-xs font-bold uppercase tracking-wider text-neutral-300">
                    Future Financial Health
                  </h2>
                </div>

                <p className="text-xs text-neutral-500 mt-1">
                  See how positive financial changes could improve your future.
                </p>
              </div>

              <span className="text-[10px] font-mono bg-emerald-400/10 text-emerald-400 border border-emerald-400/20 px-3 py-1.5 rounded-full">
                FUTURE SCENARIO
              </span>
            </div>


            {/* Main Scenario */}
            <div className="bg-neutral-950 border border-neutral-800 rounded-2xl p-5">

              {/* Scenario Title */}
              <div className="flex flex-col sm:flex-row justify-between sm:items-end gap-4">

                <div>
                  <span className="text-[10px] font-mono uppercase tracking-widest text-emerald-400">
                    Possible Best Scenario
                  </span>

                  <h3 className="text-lg sm:text-xl font-bold text-white mt-1">
                    What if your salary increases by ₹20,000?
                  </h3>

                  <p className="text-xs text-neutral-500 mt-1 max-w-xl">
                    If your income increases from ₹75,000 to ₹95,000, you could use
                    the additional income to strengthen your financial foundation
                    instead of increasing unnecessary spending.
                  </p>
                </div>


                {/* Future Salary */}
                <div className="sm:text-right shrink-0">
                  <p className="text-[10px] text-neutral-500 uppercase tracking-wider">
                    Future Monthly Income
                  </p>

                  <p className="text-2xl font-black text-emerald-400 font-mono mt-1">
                    ₹95,000
                  </p>

                  <p className="text-[10px] text-emerald-400 font-mono">
                    +₹20,000 / month
                  </p>
                </div>

              </div>


              {/* Current → Future */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-6">

                <div className="bg-neutral-900 border border-neutral-800 rounded-xl p-4">
                  <p className="text-[10px] text-neutral-500 uppercase tracking-wider">
                    Current Situation
                  </p>

                  <div className="flex items-end gap-2 mt-2">
                    <span className="text-xl font-bold text-white font-mono">
                      ₹75K
                    </span>

                    <span className="text-[10px] text-neutral-500 mb-1">
                      monthly income
                    </span>
                  </div>
                </div>


                <div className="bg-emerald-400/5 border border-emerald-400/20 rounded-xl p-4">
                  <p className="text-[10px] text-emerald-400 uppercase tracking-wider">
                    Possible Future
                  </p>

                  <div className="flex items-end gap-2 mt-2">
                    <span className="text-xl font-bold text-emerald-400 font-mono">
                      ₹95K
                    </span>

                    <span className="text-[10px] text-neutral-500 mb-1">
                      monthly income
                    </span>
                  </div>
                </div>

              </div>


              {/* Allocation Graph */}
              <div className="mt-7">

                <div className="flex justify-between items-center mb-3">
                  <div>
                    <h4 className="text-xs font-bold text-white">
                      Recommended Use of Extra ₹20,000
                    </h4>

                    <p className="text-[10px] text-neutral-500 mt-1">
                      A healthier way to use the additional income
                    </p>
                  </div>

                  <span className="text-xs font-mono font-bold text-emerald-400">
                    ₹20K
                  </span>
                </div>


                {/* Graph */}
                <div className="w-full h-6 bg-neutral-800 rounded-lg overflow-hidden flex">

                  {/* Emergency Fund — 35% */}
                  <div
                    className="bg-emerald-400 h-full hover:bg-emerald-300 transition-all"
                    style={{ width: "35%" }}
                  />

                  {/* Debt — 30% */}
                  <div
                    className="bg-orange-400 h-full hover:bg-orange-300 transition-all"
                    style={{ width: "30%" }}
                  />

                  {/* Investments — 25% */}
                  <div
                    className="bg-lime-400 h-full hover:bg-lime-300 transition-all"
                    style={{ width: "25%" }}
                  />

                  {/* Lifestyle — 10% */}
                  <div
                    className="bg-neutral-500 h-full hover:bg-neutral-400 transition-all"
                    style={{ width: "10%" }}
                  />

                </div>


                {/* Graph Labels */}
                <div className="grid grid-cols-4 mt-3">

                  {/* Emergency */}
                  <div className="text-left pr-2">
                    <div className="flex items-center gap-1.5">
                      <span className="w-2 h-2 rounded-full bg-emerald-400 shrink-0" />

                      <span className="text-[10px] text-neutral-400 truncate">
                        Emergency Fund
                      </span>
                    </div>

                    <p className="text-sm font-bold text-emerald-400 font-mono mt-1">
                      ₹7,000
                    </p>

                    <p className="text-[9px] text-neutral-600">
                      35%
                    </p>
                  </div>


                  {/* Debt */}
                  <div className="text-center px-1">
                    <div className="flex items-center justify-center gap-1.5">
                      <span className="w-2 h-2 rounded-full bg-orange-400 shrink-0" />

                      <span className="text-[10px] text-neutral-400 truncate">
                        Debt Payment
                      </span>
                    </div>

                    <p className="text-sm font-bold text-orange-400 font-mono mt-1">
                      ₹6,000
                    </p>

                    <p className="text-[9px] text-neutral-600">
                      30%
                    </p>
                  </div>


                  {/* Investments */}
                  <div className="text-center px-1">
                    <div className="flex items-center justify-center gap-1.5">
                      <span className="w-2 h-2 rounded-full bg-lime-400 shrink-0" />

                      <span className="text-[10px] text-neutral-400 truncate">
                        Investments
                      </span>
                    </div>

                    <p className="text-sm font-bold text-lime-400 font-mono mt-1">
                      ₹5,000
                    </p>

                    <p className="text-[9px] text-neutral-600">
                      25%
                    </p>
                  </div>


                  {/* Lifestyle */}
                  <div className="text-right pl-2">
                    <div className="flex items-center justify-end gap-1.5">
                      <span className="w-2 h-2 rounded-full bg-neutral-500 shrink-0" />

                      <span className="text-[10px] text-neutral-400 truncate">
                        Lifestyle
                      </span>
                    </div>

                    <p className="text-sm font-bold text-neutral-300 font-mono mt-1">
                      ₹2,000
                    </p>

                    <p className="text-[9px] text-neutral-600">
                      10%
                    </p>
                  </div>

                </div>

              </div>


              {/* What Changes */}
              <div className="mt-7 pt-5 border-t border-neutral-800">

                <h4 className="text-xs font-bold text-white mb-3">
                  How could your financial life change?
                </h4>

                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">

                  {/* Security */}
                  <div className="bg-neutral-900 rounded-xl p-4">
                    <p className="text-[10px] text-emerald-400 uppercase tracking-wider">
                      Financial Security
                    </p>

                    <p className="text-xs text-neutral-300 mt-2 leading-relaxed">
                      Your emergency fund reaches its target faster, giving you a
                      stronger safety net.
                    </p>
                  </div>


                  {/* Debt */}
                  <div className="bg-neutral-900 rounded-xl p-4">
                    <p className="text-[10px] text-orange-400 uppercase tracking-wider">
                      Debt Freedom
                    </p>

                    <p className="text-xs text-neutral-300 mt-2 leading-relaxed">
                      Extra payments can reduce your high-interest debt sooner and
                      lower future interest costs.
                    </p>
                  </div>


                  {/* Wealth */}
                  <div className="bg-neutral-900 rounded-xl p-4">
                    <p className="text-[10px] text-lime-400 uppercase tracking-wider">
                      Long-Term Wealth
                    </p>

                    <p className="text-xs text-neutral-300 mt-2 leading-relaxed">
                      Higher investment contributions give your money more opportunity
                      to compound over time.
                    </p>
                  </div>

                </div>

              </div>


              {/* Final Insight */}
              <div className="mt-5 bg-emerald-400/5 border border-emerald-400/10 rounded-xl p-4">

                <p className="text-xs text-neutral-300 leading-relaxed">
                  <span className="text-emerald-400 font-bold">
                    ✦ Best-case direction:
                  </span>{" "}
                  Instead of letting the entire ₹20,000 increase your expenses,
                  redirecting most of it toward savings, debt and investments could
                  help you become financially healthier while still giving you a
                  little extra lifestyle flexibility.
                </p>

              </div>

            </div>


            {/* Disclaimer */}
            <p className="text-[10px] text-neutral-600 font-mono text-center">
              * Illustrative scenario based on dummy data. Actual outcomes will depend
              on income, expenses, debt and financial goals.
            </p>

          </div>
        </div>


      </main>
    </div>
  );
}