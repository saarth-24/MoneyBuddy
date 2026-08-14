import React, { useState } from "react";
import logo from "../../assets/MoneyBuddy_Logo.png";
import { Link } from "react-router-dom";

export default function AuthPage() {
  const [isSignUp, setIsSignUp] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    password: "",
    rememberMe: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(isSignUp ? "Sign Up Submitted:" : "Login Submitted:", formData);
  };

  return (
    <div className="min-h-screen bg-black text-white flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden selection:bg-lime-400 selection:text-black">

      {/* Background Decorative Gradients */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-lime-500/10 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute bottom-0 right-10 w-[300px] h-[300px] bg-neutral-800/30 rounded-full blur-[100px] pointer-events-none" />

      {/* Header / Brand Logo */}
      {/* Header / Brand Logo */}
      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center z-10 mb-6">
        <Link
          to="/"
          className="inline-flex items-center gap-3 group focus:outline-none mb-4"
        >
          <div className="w-12 h-12 overflow-hidden flex items-center justify-center">
            <img
              src={logo}
              alt="MoneyBuddy logo"
              className="w-15 h-15 max-w-none object-contain transition-transform duration-300 group-hover:scale-110"
            />
          </div>

          {/* Brand Name */}
          <span className="text-xl font-extrabold tracking-tight text-white">
            MoneyBuddy
          </span>
        </Link>

        <h2 className="text-2xl font-bold tracking-tight text-white">
          {isSignUp ? "Create your account" : "Welcome back"}
        </h2>

        <p className="mt-2 text-sm text-neutral-400">
          {isSignUp
            ? "Start managing your crypto portfolio today"
            : "Enter your credentials to access your dashboard"}
        </p>
      </div>

      {/* Main Card Container */}
      <div className="sm:mx-auto sm:w-full sm:max-w-md z-10">
        <div className="bg-neutral-900/80 backdrop-blur-xl py-8 px-6 shadow-2xl border border-neutral-800/80 sm:rounded-3xl sm:px-10">

          {/* Auth Type Switcher Tabs */}
          <div className="flex bg-neutral-950 p-1 rounded-xl border border-neutral-800/80 mb-6">
            <button
              type="button"
              onClick={() => setIsSignUp(false)}
              className={`flex-1 py-2 text-xs font-semibold rounded-lg transition-all duration-200 ${!isSignUp
                ? "bg-neutral-800 text-white shadow-sm"
                : "text-neutral-400 hover:text-white"
                }`}
            >
              Sign In
            </button>
            <button
              type="button"
              onClick={() => setIsSignUp(true)}
              className={`flex-1 py-2 text-xs font-semibold rounded-lg transition-all duration-200 ${isSignUp
                ? "bg-lime-400 text-black shadow-sm"
                : "text-neutral-400 hover:text-white"
                }`}
            >
              Register
            </button>
          </div>

          {/* Social Auth Buttons */}
          <div className="grid grid-cols-2 gap-3 mb-6">
            <button
              type="button"
              className="flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl border border-neutral-800 bg-neutral-900 hover:bg-neutral-800/80 text-xs font-medium text-neutral-300 transition-colors"
            >
              <svg className="w-4 h-4" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                />
                <path
                  fill="currentColor"
                  d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                />
                <path
                  fill="currentColor"
                  d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"
                />
                <path
                  fill="currentColor"
                  d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"
                />
              </svg>
              Google
            </button>
            <button
              type="button"
              className="flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl border border-neutral-800 bg-neutral-900 hover:bg-neutral-800/80 text-xs font-medium text-neutral-300 transition-colors"
            >
              <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.1c.64-.78 1.08-1.85.96-2.93-.93.04-2.06.62-2.73 1.4-.59.69-1.11 1.78-.97 2.84 1.05.08 2.11-.53 2.74-1.31z" />
              </svg>
              Apple
            </button>
          </div>

          <div className="relative mb-6">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-neutral-800" />
            </div>
            <div className="relative flex justify-center text-xs uppercase">
              <span className="bg-neutral-900/90 px-3 text-neutral-500 font-medium">
                Or continue with
              </span>
            </div>
          </div>

          {/* Form */}
          <form className="space-y-4" onSubmit={handleSubmit}>
            {isSignUp && (
              <div>
                <label className="block text-xs font-medium text-neutral-300 mb-1.5">
                  Full Name
                </label>
                <input
                  type="text"
                  name="fullName"
                  required
                  value={formData.fullName}
                  onChange={handleChange}
                  placeholder="Satoshi Nakamoto"
                  className="w-full bg-neutral-950 border border-neutral-800 rounded-xl px-4 py-2.5 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 focus:ring-1 focus:ring-lime-400 transition-colors"
                />
              </div>
            )}

            <div>
              <label className="block text-xs font-medium text-neutral-300 mb-1.5">
                Email Address
              </label>
              <input
                type="email"
                name="email"
                required
                value={formData.email}
                onChange={handleChange}
                placeholder="name@company.com"
                className="w-full bg-neutral-950 border border-neutral-800 rounded-xl px-4 py-2.5 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 focus:ring-1 focus:ring-lime-400 transition-colors"
              />
            </div>

            <div>
              <label className="block text-xs font-medium text-neutral-300 mb-1.5">
                Password
              </label>
              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  name="password"
                  required
                  value={formData.password}
                  onChange={handleChange}
                  placeholder="••••••••••••"
                  className="w-full bg-neutral-950 border border-neutral-800 rounded-xl px-4 py-2.5 pr-10 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 focus:ring-1 focus:ring-lime-400 transition-colors"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-neutral-500 hover:text-neutral-300 text-xs font-medium focus:outline-none"
                >
                  {showPassword ? "Hide" : "Show"}
                </button>
              </div>
            </div>

            {/* Remember Me & Forgot Password */}
            <div className="flex items-center justify-between text-xs">
              <label className="flex items-center gap-2 cursor-pointer text-neutral-400 hover:text-neutral-300">
                <input
                  type="checkbox"
                  name="rememberMe"
                  checked={formData.rememberMe}
                  onChange={handleChange}
                  className="w-4 h-4 rounded bg-neutral-950 border-neutral-800 text-lime-400 focus:ring-0 focus:ring-offset-0 cursor-pointer accent-lime-400"
                />
                Remember for 30 days
              </label>
              {!isSignUp && (
                <a href="#" className="text-lime-400 hover:text-lime-300 font-medium">
                  Forgot password?
                </a>
              )}
            </div>

            {/* Primary Submit Button */}
            <button
              type="submit"
              className="w-full mt-2 bg-lime-400 text-black font-semibold py-3 px-4 rounded-xl hover:bg-lime-300 shadow-lg shadow-lime-400/20 active:scale-[0.99] transition-all duration-200 text-sm"
            >
              {isSignUp ? "Create Free Account" : "Sign In to Dashboard"}
            </button>
          </form>

          {/* Footer Note */}
          <p className="mt-6 text-center text-xs text-neutral-500">
            {isSignUp ? (
              <>
                By signing up, you agree to our{" "}
                <a href="#" className="underline text-neutral-400 hover:text-white">
                  Terms
                </a>{" "}
                &{" "}
                <a href="#" className="underline text-neutral-400 hover:text-white">
                  Privacy Policy
                </a>
                .
              </>
            ) : (
              <>
                Don't have an account?{" "}
                <button
                  onClick={() => setIsSignUp(true)}
                  className="text-lime-400 hover:underline font-medium"
                >
                  Sign up for free
                </button>
              </>
            )}
          </p>

        </div>
      </div>
    </div>
  );
}