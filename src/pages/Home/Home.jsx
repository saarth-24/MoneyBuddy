import React from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="relative min-h-screen bg-zinc-950 text-white overflow-hidden selection:bg-lime-400 selection:text-black">

      {/* Background Ambient Glows */}
      <div className="fixed inset-0 -z-10 pointer-events-none">

        <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(163,230,53,0.15),rgba(255,255,255,0))]" />

        <div className="absolute top-[-100px] left-1/2 -translate-x-1/2 w-[600px] sm:w-[900px] h-[600px] sm:h-[900px] bg-lime-400/10 rounded-full blur-[140px] animate-pulse" />

        <div className="absolute bottom-[-200px] right-[-100px] w-[500px] sm:w-[700px] h-[500px] sm:h-[700px] bg-emerald-500/10 rounded-full blur-[160px]" />

      </div>


      {/* Navbar */}
      <Navbar />


      {/* Hero Container */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 sm:pt-28 pb-20">

        {/* Hero Content */}
        <div className="flex flex-col items-center text-center max-w-4xl mx-auto">

          {/* Badge */}
          <div className="inline-flex items-center gap-2.5 px-4 py-2 mb-8 rounded-full border border-lime-400/20 bg-lime-400/5 text-xs sm:text-sm text-lime-300 backdrop-blur-md">

            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-lime-400 opacity-75"></span>

              <span className="relative inline-flex rounded-full h-2 w-2 bg-lime-400"></span>
            </span>

            <span>Your finances, but smarter.</span>

            <span className="text-lime-400/50">
              →
            </span>

          </div>


          {/* Main Heading */}
          <h1 className="text-5xl sm:text-7xl lg:text-8xl font-black tracking-tight leading-[1.05] sm:leading-[0.95]">

            Make money{" "}

            <span className="relative inline-block text-transparent bg-clip-text bg-gradient-to-r from-lime-300 via-lime-400 to-emerald-400">
              Your Buddy.
            </span>

          </h1>


          {/* Description */}
          <p className="mt-8 max-w-2xl text-base sm:text-lg lg:text-xl text-zinc-400 leading-relaxed">

            Take control of your finances with one beautifully simple platform.
            Track, understand, and grow your wealth — completely automated.

          </p>


          {/* Call To Actions */}
          <div className="flex flex-col sm:flex-row items-center gap-4 mt-10 w-full sm:w-auto">

            <button
              onClick={() => navigate("/finances")}
              className="w-full sm:w-auto px-8 py-4 rounded-full bg-lime-400 text-zinc-950 font-bold text-sm tracking-wide hover:bg-lime-300 hover:shadow-[0_0_30px_rgba(163,230,53,0.4)] hover:scale-[1.02] active:scale-[0.98] transition-all duration-200 cursor-pointer"
            >
              Get Started →
            </button>


            <button
              onClick={() => navigate("/dashboard")}
              className="w-full sm:w-auto px-8 py-4 rounded-full border border-zinc-800 bg-zinc-900/50 text-zinc-200 font-semibold text-sm tracking-wide hover:bg-zinc-800 hover:text-white hover:border-zinc-700 transition-all duration-200 cursor-pointer backdrop-blur-sm"
            >
              Explore Dashboard
            </button>

          </div>

        </div>


        {/* Dashboard Preview */}
        <div className="mt-16 sm:mt-20 relative rounded-3xl border border-zinc-800/80 bg-zinc-900/40 p-2 sm:p-4 backdrop-blur-xl shadow-2xl shadow-lime-950/20">


          {/* Window Controls */}
          <div className="flex items-center px-4 py-3 border-b border-zinc-800/60 mb-4">

            <div className="flex items-center gap-2">

              <div className="w-3 h-3 rounded-full bg-red-500/80" />

              <div className="w-3 h-3 rounded-full bg-yellow-500/80" />

              <div className="w-3 h-3 rounded-full bg-green-500/80" />

            </div>

          </div>


          {/* Overview Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6 p-2 sm:p-4">


            {/* Total Balance */}
            <div
              onClick={() => navigate("/dashboard")}
              className="group relative p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 hover:border-lime-400/40 hover:bg-zinc-800/50 transition-all duration-300 overflow-hidden cursor-pointer"
            >

              <div className="absolute top-0 right-0 w-32 h-32 bg-lime-400/5 rounded-full blur-2xl group-hover:bg-lime-400/10 transition-colors" />

              <div className="flex items-center justify-between">

                <p className="text-zinc-400 text-sm font-medium">
                  Total Balance
                </p>

                <span className="p-2 rounded-lg bg-lime-400/10 text-lime-400 text-xs">
                  📈 +12.4%
                </span>

              </div>

              <h2 className="text-3xl sm:text-4xl font-bold mt-4 tracking-tight">
                ₹1,24,580
              </h2>

              <div className="w-full bg-zinc-800/80 h-1.5 rounded-full mt-5 overflow-hidden">

                <div className="bg-lime-400 h-full rounded-full w-[72%] transition-all duration-500 group-hover:w-[78%]" />

              </div>

              <p className="text-zinc-500 text-xs mt-3">
                Updated 2 mins ago
              </p>

            </div>


            {/* Investments */}
            <div
              onClick={() => navigate("/dashboard")}
              className="group relative p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 hover:border-lime-400/40 hover:bg-zinc-800/50 transition-all duration-300 overflow-hidden cursor-pointer"
            >

              <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-400/5 rounded-full blur-2xl group-hover:bg-emerald-400/10 transition-colors" />

              <div className="flex items-center justify-between">

                <p className="text-zinc-400 text-sm font-medium">
                  Investments
                </p>

                <span className="p-2 rounded-lg bg-emerald-400/10 text-emerald-400 text-xs">
                  🚀 +8.7%
                </span>

              </div>

              <h2 className="text-3xl sm:text-4xl font-bold mt-4 tracking-tight">
                ₹84,320
              </h2>

              <div className="w-full bg-zinc-800/80 h-1.5 rounded-full mt-5 overflow-hidden">

                <div className="bg-emerald-400 h-full rounded-full w-[64%] transition-all duration-500 group-hover:w-[70%]" />

              </div>

              <p className="text-zinc-500 text-xs mt-3">
                Portfolio yield performing well
              </p>

            </div>


            {/* Monthly Savings */}
            <div
              className="group relative p-6 rounded-2xl bg-zinc-900/80 border border-zinc-800/80 hover:border-lime-400/40 hover:bg-zinc-800/50 transition-all duration-300 overflow-hidden"
            >

              <div className="absolute top-0 right-0 w-32 h-32 bg-lime-400/5 rounded-full blur-2xl group-hover:bg-lime-400/10 transition-colors" />

              <div className="flex items-center justify-between">

                <p className="text-zinc-400 text-sm font-medium">
                  Monthly Savings
                </p>

                <span className="p-2 rounded-lg bg-lime-400/10 text-lime-400 text-xs">
                  ✦ On Track
                </span>

              </div>

              <h2 className="text-3xl sm:text-4xl font-bold mt-4 tracking-tight">
                ₹18,450
              </h2>

              <div className="w-full bg-zinc-800/80 h-1.5 rounded-full mt-5 overflow-hidden">

                <div className="bg-lime-400 h-full rounded-full w-[85%] transition-all duration-500 group-hover:w-[92%]" />

              </div>

              <p className="text-zinc-500 text-xs mt-3">
                85% of your ₹22,000 monthly target
              </p>

            </div>

          </div>

        </div>

      </main>

    </div>
  );
}

export default Home;