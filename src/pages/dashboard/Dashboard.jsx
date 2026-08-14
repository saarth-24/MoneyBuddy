import React, { useState } from "react";
import Navbar from "../../components/Navbar/Navbar";

// Sample mock data
const TRANSACTIONS = [
  { id: 1, name: "Apple Store", category: "Electronics", date: "Today, 2:45 PM", amount: "-₹14,900", icon: "💻", type: "expense" },
  { id: 2, name: "Salary Credit", category: "Income", date: "Yesterday", amount: "+₹85,000", icon: "💰", type: "income" },
  { id: 3, name: "Starbucks Coffee", category: "Food & Drinks", date: "08 Aug 2026", amount: "-₹450", icon: "☕", type: "expense" },
  { id: 4, name: "Zerodha Mutual Fund", category: "Investment", date: "05 Aug 2026", amount: "-₹10,000", icon: "📈", type: "expense" },
  { id: 5, name: "Freelance Payment", category: "Income", date: "01 Aug 2026", amount: "+₹22,500", icon: "🚀", type: "income" },
];

const BUDGET_CATEGORIES = [
  { name: "Shopping & Retail", spent: 18400, limit: 25000, color: "bg-lime-400" },
  { name: "Food & Dining", spent: 8200, limit: 12000, color: "bg-emerald-400" },
  { name: "Bills & Utilities", spent: 14500, limit: 15000, color: "bg-yellow-400" },
  { name: "Entertainment", spent: 4800, limit: 5000, color: "bg-lime-300" },
];

function Dashboard() {
  const [timeRange, setTimeRange] = useState("1M");
  const [selectedTab, setSelectedTab] = useState("overview");

  return (
    <div className="relative min-h-screen bg-zinc-950 text-white selection:bg-lime-400 selection:text-black">
      
      {/* Background Glows */}
      <div className="fixed inset-0 -z-10 pointer-events-none">
        <div className="absolute top-[-150px] left-[-100px] w-[600px] h-[600px] bg-lime-400/10 rounded-full blur-[150px]" />
        <div className="absolute bottom-[-100px] right-[-100px] w-[500px] h-[500px] bg-emerald-500/10 rounded-full blur-[160px]" />
      </div>

      {/* Imported Navbar */}
      <Navbar />

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-16">
        
        {/* Header Section */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-3xl sm:text-4xl font-bold tracking-tight">
                Welcome back 👋
              </h1>
            </div>
            <p className="text-zinc-400 text-sm mt-1">
              Here is what's happening with your finances today.
            </p>
          </div>

          {/* Quick Controls */}
          
        </div>

        {/* Navigation Tabs */}
        <div className="flex items-center gap-2 border-b border-zinc-800/80 mb-8 overflow-x-auto pb-2 scrollbar-none">
          {[
            { id: "overview", label: "Overview" },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setSelectedTab(tab.id)}
              className={`px-4 py-2 text-sm font-medium rounded-lg whitespace-nowrap transition-all ${
                selectedTab === tab.id
                  ? "bg-zinc-900 text-lime-400 border border-lime-400/30"
                  : "text-zinc-400 hover:text-white hover:bg-zinc-900/50"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
          
          {/* Card 1 */}
          <div className="p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 backdrop-blur-xl hover:border-lime-400/40 transition-all">
            <div className="flex items-center justify-between text-zinc-400 text-xs font-medium">
              <span>TOTAL BALANCE</span>
              <span className="p-1.5 rounded-lg bg-lime-400/10 text-lime-400">💵</span>
            </div>
            <h2 className="text-3xl font-bold mt-3 tracking-tight">₹1,24,580</h2>
            <div className="flex items-center gap-1 text-xs text-lime-400 mt-2">
          
            </div>
          </div>

          {/* Card 2 */}
          <div className="p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 backdrop-blur-xl hover:border-lime-400/40 transition-all">
            <div className="flex items-center justify-between text-zinc-400 text-xs font-medium">
              <span>MONTHLY INCOME</span>
              <span className="p-1.5 rounded-lg bg-emerald-400/10 text-emerald-400">📥</span>
            </div>
            <h2 className="text-3xl font-bold mt-3 tracking-tight">₹1,07,500</h2>
            <div className="flex items-center gap-1 text-xs text-emerald-400 mt-2">
              
            </div>
          </div>

          {/* Card 3 */}
          <div className="p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 backdrop-blur-xl hover:border-lime-400/40 transition-all">
            <div className="flex items-center justify-between text-zinc-400 text-xs font-medium">
              <span>MONTHLY EXPENSES</span>
              <span className="p-1.5 rounded-lg bg-red-400/10 text-red-400">📤</span>
            </div>
            <h2 className="text-3xl font-bold mt-3 tracking-tight">₹45,900</h2>
            <div className="flex items-center gap-1 text-xs text-red-400 mt-2">
              
              
            </div>
          </div>

          {/* Card 4 */}
          <div className="p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 backdrop-blur-xl hover:border-lime-400/40 transition-all">
            <div className="flex items-center justify-between text-zinc-400 text-xs font-medium">
              <span>EMERGENCY FUND</span>
              <span className="p-1.5 rounded-lg bg-lime-400/10 text-lime-400">📈</span>
            </div>
            <h2 className="text-3xl font-bold mt-3 tracking-tight">₹84,320</h2>
            <div className="flex items-center gap-1 text-xs text-lime-400 mt-2">
              
              
            </div>
          </div>

        </div>

        {/* Main Dashboard Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Left Column (Transactions & Performance) */}
          <div className="lg:col-span-2 space-y-8">
            
            {/* Chart Container Placeholder */}
            <div className="p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 backdrop-blur-xl">
              <div className="flex items-center justify-between mb-6">
                <div>
                  <h3 className="font-semibold text-lg">Cash Flow Overview</h3>
                  <p className="text-zinc-400 text-xs">Income vs Expense trends over time</p>
                </div>
                <div className="flex items-center gap-4 text-xs font-medium">
                  <div className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-lime-400" />
                    <span>Income</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-zinc-600" />
                    <span>Expenses</span>
                  </div>
                </div>
              </div>

              {/* Simplified Visual Bars Chart */}
              <div className="h-48 flex items-end justify-between gap-2 sm:gap-4 pt-6 border-b border-zinc-800">
                {[
                  { month: "Jan", inc: 60, exp: 40 },
                  { month: "Feb", inc: 75, exp: 50 },
                  { month: "Mar", inc: 65, exp: 45 },
                  { month: "Apr", inc: 90, exp: 60 },
                  { month: "May", inc: 80, exp: 55 },
                  { month: "Jun", inc: 95, exp: 40 },
                ].map((bar, idx) => (
                  <div key={idx} className="flex-1 flex flex-col items-center gap-2 h-full justify-end group cursor-pointer">
                    <div className="w-full flex items-end justify-center gap-1 h-full">
                      <div
                        style={{ height: `${bar.inc}%` }}
                        className="w-full max-w-[16px] bg-lime-400 rounded-t-sm group-hover:bg-lime-300 transition-all"
                      />
                      <div
                        style={{ height: `${bar.exp}%` }}
                        className="w-full max-w-[16px] bg-zinc-700 rounded-t-sm group-hover:bg-zinc-600 transition-all"
                      />
                    </div>
                    <span className="text-zinc-500 text-xs">{bar.month}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Recent Transactions List */}
            

          </div>

          {/* Right Column (Budgets & Quick Actions) */}
          <div className="space-y-8">
      
            

            {/* Budget Limits & Progress */}
            <div className="p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 backdrop-blur-xl">
              <div className="flex items-center justify-between mb-6">
                <div>
                  <h3 className="font-semibold text-lg">Monthly Budgets</h3>
                  <p className="text-zinc-400 text-xs">Tracking limits per category</p>
                </div>
                <button className="text-xs text-zinc-400 hover:text-white">Edit</button>
              </div>

              <div className="space-y-5">
                {BUDGET_CATEGORIES.map((item, idx) => {
                  const percentage = Math.min(100, Math.round((item.spent / item.limit) * 100));
                  return (
                    <div key={idx} className="space-y-1.5">
                      <div className="flex justify-between text-xs">
                        <span className="font-medium text-zinc-300">{item.name}</span>
                        <span className="text-zinc-400">
                          ₹{item.spent.toLocaleString()} / <span className="text-zinc-500">₹{item.limit.toLocaleString()}</span>
                        </span>
                      </div>
                      
                      <div className="w-full h-2 bg-zinc-800 rounded-full overflow-hidden">
                        <div
                          style={{ width: `${percentage}%` }}
                          className={`h-full rounded-full transition-all duration-500 ${item.color}`}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

          </div>

        </div>

      </main>
    </div>
  );
}

export default Dashboard;