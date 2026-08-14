
import React, { useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import logo from "../../assets/MoneyBuddy_Logo.png";


function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const navLinks = [
    { name: "Portfolio", path: "/portfolio" },
    { name: "Dashboard", path: "/dashboard" },
    { name: "Finance", path: "/finances" },
    { name: "Markets", path: "/markets" },
  ];

  const handleLoginClick = () => {
    setMobileMenuOpen(false);
    navigate("/login");
  };

  const handleGetStartedClick = () => {
    setMobileMenuOpen(false);
    navigate("/finances");
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b border-neutral-800/80 bg-black/80 backdrop-blur-xl transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <div className="flex items-center justify-between h-20">

          {/* ================= BRAND ================= */}
          <Link
            to="/"
            className="flex items-center gap-2 group focus:outline-none focus:ring-2 focus:ring-lime-400 rounded-lg p-1"
          >

            {/* Logo Image */}
            <div className="w-12 h-12 overflow-hidden flex items-center justify-center">
              <img
                src={logo}
                alt="Finova logo"
                className="w-15 h-15 max-w-none object-contain transition-transform duration-300 group-hover:scale-110"
              />
            </div>

            {/* Brand Name */}
            <span className="text-xl font-extrabold tracking-tight text-white">
              MoneyBuddy
            </span>

          </Link>


          {/* ================= DESKTOP NAVIGATION ================= */}
          <nav className="hidden md:flex items-center gap-1 bg-neutral-900/60 border border-neutral-800/60 p-1.5 rounded-full">

            {navLinks.map((link) => {
              const isActive = location.pathname === link.path;

              return (
                <Link
                  key={link.name}
                  to={link.path}
                  className={`px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 ${
                    isActive
                      ? "bg-neutral-800 text-lime-400 font-semibold shadow-sm"
                      : "text-neutral-400 hover:text-white hover:bg-neutral-800/80"
                  }`}
                >
                  {link.name}
                </Link>
              );
            })}

          </nav>


          {/* ================= DESKTOP CTA ================= */}
          <div className="hidden md:flex items-center gap-3">

            <button
              onClick={handleLoginClick}
              className="text-sm font-medium text-neutral-300 hover:text-white px-4 py-2.5 rounded-full hover:bg-neutral-900 transition-all cursor-pointer"
            >
              Log in
            </button>

            <button
              onClick={handleGetStartedClick}
              className="relative group inline-flex items-center justify-center bg-lime-400 text-black px-5 py-2.5 rounded-full text-sm font-semibold hover:bg-lime-300 shadow-lg shadow-lime-400/20 hover:shadow-lime-400/35 hover:scale-[1.02] active:scale-[0.98] transition-all duration-200 cursor-pointer"
            >
              <span>Get Started</span>

              <svg
                className="w-4 h-4 ml-1.5 transition-transform duration-200 group-hover:translate-x-0.5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2.5}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
                />
              </svg>

            </button>

          </div>


          {/* ================= MOBILE MENU BUTTON ================= */}
          <div className="flex md:hidden">

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2.5 rounded-xl text-neutral-400 hover:text-white hover:bg-neutral-900 focus:outline-none"
              aria-label="Toggle Menu"
              aria-expanded={mobileMenuOpen}
            >

              {mobileMenuOpen ? (
                <svg
                  className="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M6 18L18 6M6 6l12 12"
                  />
                </svg>
              ) : (
                <svg
                  className="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              )}

            </button>

          </div>

        </div>
      </div>


      {/* ================= MOBILE DRAWER ================= */}
      {mobileMenuOpen && (

        <div className="md:hidden border-b border-neutral-800 bg-neutral-950/95 backdrop-blur-2xl px-4 pt-3 pb-6 space-y-3">

          {/* Mobile Brand */}
          <div className="flex items-center gap-2 px-2 pb-3">

            <div className="w-11 h-11 overflow-hidden flex items-center justify-center">
              <img
                src={logo}
                alt="Finova logo"
                className="w-18 h-18 max-w-none object-contain"
              />
            </div>

            <span className="text-lg font-extrabold text-white">
              Finova<span className="text-lime-400">.</span>
            </span>

          </div>


          {/* Mobile Navigation */}
          <nav className="flex flex-col space-y-1">

            {navLinks.map((link) => {

              const isActive = location.pathname === link.path;

              return (
                <Link
                  key={link.name}
                  to={link.path}
                  className={`px-4 py-3 rounded-xl text-base font-medium transition-colors ${
                    isActive
                      ? "bg-neutral-900 text-lime-400 font-semibold"
                      : "text-neutral-300 hover:text-lime-400 hover:bg-neutral-900/80"
                  }`}
                  onClick={() => setMobileMenuOpen(false)}
                >
                  {link.name}
                </Link>
              );

            })}

          </nav>


          {/* Mobile Buttons */}
          <div className="pt-4 border-t border-neutral-800 flex flex-col gap-2.5">

            <button
              onClick={handleLoginClick}
              className="w-full text-center text-neutral-300 hover:text-white py-3 rounded-xl text-sm font-medium border border-neutral-800 hover:bg-neutral-900 transition-colors"
            >
              Log in
            </button>

            <button
              onClick={handleGetStartedClick}
              className="w-full bg-lime-400 text-black py-3 rounded-xl text-sm font-semibold hover:bg-lime-300 transition-colors shadow-md shadow-lime-400/20"
            >
              Get Started →
            </button>

          </div>

        </div>

      )}

    </header>
  );
}

export default Navbar;

