import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar/Navbar";
import { useNavigate } from "react-router-dom";

export default function FinancialOnboarding() {
  const navigate = useNavigate();
  const [step, setStep] = useState(1);
  const totalSteps = 6;

  // Form State
  const [formData, setFormData] = useState({
    // Step 1: Basic Information & Household
    name: "",
    age: "",
    city: "",
    employmentType: "",
    dependents: "0",

    // Step 2: Monthly Income & Expense Allocation
    monthlyIncome: "",
    monthlyExpenses: "",
    expenseCategories: [],

    // Step 3: Banking & Current Liquidity
    primaryBank: "",
    activeCards: [],
    liquidSavings: "",
    emergencyFund: "",

    // Step 4: Loans & Liabilities
    hasDebt: null, // "yes" or "no"
    loans: [
      { type: "Home Loan", bank: "", amount: "", interestRate: "", tenureYears: "" }
    ],

    // Step 5: Risk Tolerance Assessment
    riskAnswers: {},

    // Step 6: Financial Objectives & Horizons
    goals: [],
    targetTimeline: "",
  });

  // Analysis Loading State
  const [analysisProgress, setAnalysisProgress] = useState(0);
  const [completedCheckmarks, setCompletedCheckmarks] = useState([]);

  // Risk Score Calculation
  const calculateRiskProfile = () => {
    const scores = Object.values(formData.riskAnswers);
    if (scores.length === 0) return { label: "MODERATE", score: 50 };
    const avgScore = scores.reduce((a, b) => a + b, 0) / scores.length;
    if (avgScore <= 30) return { label: "CONSERVATIVE", score: 30 };
    if (avgScore <= 65) return { label: "BALANCED", score: 65 };
    return { label: "AGGRESSIVE GROWTH", score: 90 };
  };

  // Step 7 Timer Animation
  useEffect(() => {
    if (step === 7) {
      const interval = setInterval(() => {
        setAnalysisProgress((prev) => {
          if (prev >= 100) {
            clearInterval(interval);
            return 100;
          }
          return prev + 2;
        });
      }, 45);

      return () => clearInterval(interval);
    }
  }, [step]);

  useEffect(() => {
    if (step === 7) {
      const checkTimers = [
        setTimeout(() => setCompletedCheckmarks((prev) => [...prev, 1]), 500),
        setTimeout(() => setCompletedCheckmarks((prev) => [...prev, 2]), 1100),
        setTimeout(() => setCompletedCheckmarks((prev) => [...prev, 3]), 1700),
        setTimeout(() => setCompletedCheckmarks((prev) => [...prev, 4]), 2200),
        setTimeout(() => setCompletedCheckmarks((prev) => [...prev, 5]), 2700),
      ];
      return () => checkTimers.forEach(clearTimeout);
    }
  }, [step]);

  const handleNext = () => setStep((prev) => Math.min(prev + 1, 7));
  const handlePrev = () => setStep((prev) => Math.max(prev - 1, 1));

  const toggleArrayItem = (key, item) => {
    setFormData((prev) => {
      const list = prev[key];
      return {
        ...prev,
        [key]: list.includes(item)
          ? list.filter((i) => i !== item)
          : [...list, item],
      };
    });
  };

  // Loan Dynamic Input Handler
  const addLoanRow = () => {
    setFormData((prev) => ({
      ...prev,
      loans: [...prev.loans, { type: "Personal Loan", bank: "", amount: "", interestRate: "", tenureYears: "" }],
    }));
  };

  const updateLoanField = (index, field, value) => {
    setFormData((prev) => {
      const updatedLoans = [...prev.loans];
      updatedLoans[index][field] = value;
      return { ...prev, loans: updatedLoans };
    });
  };

  const removeLoanRow = (index) => {
    setFormData((prev) => ({
      ...prev,
      loans: prev.loans.filter((_, i) => i !== index),
    }));
  };

  // Static Data Lists
  const expenseOptions = [
    { id: "EMI", label: "Loan EMI / Debt Paydown" },
    { id: "OTHERS", label: "Lifestyle & Discretionary" },
  ];

  const cardOptions = [];

  const goalOptions = [
    { id: "house", label: "Real Estate Acquisition" },
    { id: "vehicle", label: "Vehicle Purchase" },
    { id: "education", label: "Higher Education" },
    { id: "travel", label: "International Travel" },
    { id: "emergency", label: "Emergency Reserve" },
    { id: "retirement", label: "Early Retirement" },
    { id: "wealth", label: "Wealth Accumulation" },
  ];

  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100 flex flex-col justify-between selection:bg-lime-400 selection:text-black relative overflow-x-hidden">

      {/* Integrated Navigation Bar */}
      <Navbar />

      {/* Background Radial Glow */}
      <div className="absolute top-20 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-neutral-900/40 rounded-full blur-[140px] pointer-events-none" />

      <main className="flex-1 flex flex-col justify-center py-8 px-4 sm:px-6 lg:px-8 z-10 max-w-3xl mx-auto w-full">

        {/* Progress Header */}
        {step <= 6 && (
          <div className="w-full mb-8">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-mono tracking-widest text-lime-400 uppercase">
                Financial Onboarding
              </span>
              <span className="text-xs font-mono tracking-widest text-neutral-400 uppercase bg-neutral-900 border border-neutral-800 px-3 py-1 rounded-md">
                0{step} / 0{totalSteps}
              </span>
            </div>

            <div className="w-full bg-neutral-900 h-1.5 rounded-full overflow-hidden border border-neutral-800/50">
              <div
                className="bg-lime-400 h-full transition-all duration-300 ease-out shadow-[0_0_8px_rgba(163,230,53,0.6)]"
                style={{ width: `${(step / totalSteps) * 100}%` }}
              />
            </div>
          </div>
        )}

        {/* STEP 1: Basic Information & Household */}
        {step === 1 && (
          <div className="space-y-6">
            <div>
              <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                Personal Profile & Household
              </h1>
              <p className="mt-1 text-neutral-400 text-sm">
                Provide essential demographic context to help us calculate tax brackets and asset distribution models.
              </p>
            </div>

            <div className="space-y-4">
              <div>
                <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                  Full Name
                </label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  placeholder="e.g. Rahul Sharma"
                  className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-3 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 transition-colors"
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                    Age
                  </label>
                  <input
                    type="number"
                    value={formData.age}
                    onChange={(e) => setFormData({ ...formData, age: e.target.value })}
                    placeholder="e.g. 32"
                    className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-3 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 transition-colors"
                  />
                </div>

                <div>
                  <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                    City of Residence
                  </label>
                  <input
                    type="text"
                    value={formData.city}
                    onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                    placeholder="e.g. Bengaluru"
                    className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-3 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 transition-colors"
                  />
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
                <div>
                  <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                    Employment Sector
                  </label>
                  <select
                    value={formData.employmentType}
                    onChange={(e) => setFormData({ ...formData, employmentType: e.target.value })}
                    className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-lime-400 transition-colors"
                  >
                    <option value="">Select Employment Type</option>
                    <option value="Salaried Corporate">Salaried Corporate</option>
                    <option value="Government / PSU">Government / PSU</option>
                    <option value="Business Owner / Founder">Business Owner / Founder</option>
                    <option value="Freelancer / Consultant">Freelancer / Consultant</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                    Family Dependents
                  </label>
                  <select
                    value={formData.dependents}
                    onChange={(e) => setFormData({ ...formData, dependents: e.target.value })}
                    className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-lime-400 transition-colors"
                  >
                    <option value="0">None (0)</option>
                    <option value="1">1 Dependent</option>
                    <option value="2">2 Dependents</option>
                    <option value="3">3 Dependents</option>
                    <option value="4+">4+ Dependents</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* STEP 2: Monthly Income & Expense Allocation */}
        {step === 2 && (
          <div className="space-y-6">
            <div>
              <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                Income & Expense Distribution
              </h1>
              <p className="mt-1 text-neutral-400 text-sm">
                Define your monthly cash inflow and break down major expenditure outflow channels.
              </p>
            </div>

            <div className="space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="bg-neutral-900 border border-neutral-800 p-5 rounded-2xl">
                  <label className="block text-xs font-medium text-neutral-400 uppercase tracking-wider mb-2">
                    Net Monthly Income
                  </label>
                  <div className="flex items-center gap-2">
                    <span className="text-xl font-medium text-lime-400">₹</span>
                    <input
                      type="number"
                      value={formData.monthlyIncome}
                      onChange={(e) => setFormData({ ...formData, monthlyIncome: e.target.value })}
                      placeholder="1,80,000"
                      className="w-full bg-transparent text-xl font-semibold text-white placeholder-neutral-700 focus:outline-none"
                    />
                  </div>
                </div>

                <div className="bg-neutral-900 border border-neutral-800 p-5 rounded-2xl">
                  <label className="block text-xs font-medium text-neutral-400 uppercase tracking-wider mb-2">
                    Total Monthly Outflow
                  </label>
                  <div className="flex items-center gap-2">
                    <span className="text-xl font-medium text-neutral-500">₹</span>
                    <input
                      type="number"
                      value={formData.monthlyExpenses}
                      onChange={(e) => setFormData({ ...formData, monthlyExpenses: e.target.value })}
                      placeholder="75,000"
                      className="w-full bg-transparent text-xl font-semibold text-white placeholder-neutral-700 focus:outline-none"
                    />
                  </div>
                </div>
              </div>

              <div className="pt-2">
                <label className="block text-xs font-medium text-neutral-400 mb-2 uppercase tracking-wider">
                  Where does the majority of your monthly expenditure go?
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {expenseOptions.map((item) => {
                    const isChecked = formData.expenseCategories.includes(item.id);
                    return (
                      <button
                        key={item.id}
                        type="button"
                        onClick={() => toggleArrayItem("expenseCategories", item.id)}
                        className={`p-3.5 rounded-xl border text-left text-xs font-medium transition-all flex items-center justify-between ${isChecked
                          ? "bg-neutral-800 border-lime-400 text-white"
                          : "bg-neutral-900/60 border-neutral-800 text-neutral-400 hover:border-neutral-700"
                          }`}
                      >
                        <span>{item.label}</span>
                        <div className={`w-4 h-4 rounded border flex items-center justify-center transition-colors ${isChecked ? "bg-lime-400 border-lime-400 text-black" : "border-neutral-700 bg-neutral-950"
                          }`}>
                          {isChecked && <span className="text-[10px] font-bold">✓</span>}
                        </div>
                      </button>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* STEP 3: Banking & Current Liquidity */}
        {step === 3 && (
          <div className="space-y-6">
            <div>
              <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                Banking & Liquid Assets
              </h1>
              <p className="mt-1 text-neutral-400 text-sm">
                Map your current operating accounts and existing uninvested capital reserves.
              </p>
            </div>

            <div className="space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                    Primary Operating Bank
                  </label>
                  <input
                    type="text"
                    value={formData.primaryBank}
                    onChange={(e) => setFormData({ ...formData, primaryBank: e.target.value })}
                    placeholder="e.g. HDFC Bank / ICICI Bank"
                    className="w-full bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-3 text-sm text-white placeholder-neutral-600 focus:outline-none focus:border-lime-400 transition-colors"
                  />
                </div>

                <div>
                  <label className="block text-xs font-medium text-neutral-400 mb-1.5 uppercase tracking-wider">
                    Liquid Savings Balance
                  </label>
                  <div className="bg-neutral-900 border border-neutral-800 rounded-xl px-4 py-2.5 flex items-center gap-2">
                    <span className="text-lime-400 text-sm font-semibold">₹</span>
                    <input
                      type="number"
                      value={formData.liquidSavings}
                      onChange={(e) => setFormData({ ...formData, liquidSavings: e.target.value })}
                      placeholder="e.g. 2,50,000"
                      className="w-full bg-transparent text-sm text-white placeholder-neutral-600 focus:outline-none"
                    />
                  </div>
                </div>
              </div>


            </div>
          </div>
        )}

        {/* STEP 4: Loans & Liabilities */}
        {step === 4 && (
          <div className="space-y-6">
            <div>
              <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                Existing Liabilities & Debt Structure
              </h1>
              <p className="mt-1 text-neutral-400 text-sm">
                Accurate debt tracking allows Finova to optimize high-interest paydown schedules.
              </p>
            </div>

            <div className="space-y-4">
              <label className="block text-xs font-medium text-neutral-400 uppercase tracking-wider">
                Do you currently have active loans or unpaid debt balances?
              </label>

              <div className="grid grid-cols-2 gap-3">
                <button
                  type="button"
                  onClick={() => setFormData({ ...formData, hasDebt: "no" })}
                  className={`p-4 rounded-xl border text-center font-medium text-sm transition-all ${formData.hasDebt === "no"
                    ? "bg-neutral-800 border-lime-400 text-white"
                    : "bg-neutral-900 border-neutral-800 text-neutral-400 hover:border-neutral-700"
                    }`}
                >
                  No Active Liabilities
                </button>
                <button
                  type="button"
                  onClick={() => setFormData({ ...formData, hasDebt: "yes" })}
                  className={`p-4 rounded-xl border text-center font-medium text-sm transition-all ${formData.hasDebt === "yes"
                    ? "bg-neutral-800 border-lime-400 text-white"
                    : "bg-neutral-900 border-neutral-800 text-neutral-400 hover:border-neutral-700"
                    }`}
                >
                  Yes, Active Liabilities
                </button>
              </div>

              {formData.hasDebt === "yes" && (
                <div className="space-y-4 pt-2">
                  {formData.loans.map((loan, idx) => (
                    <div key={idx} className="bg-neutral-900/90 border border-neutral-800 p-4 rounded-xl space-y-3 relative">
                      <div className="flex justify-between items-center border-b border-neutral-800 pb-2">
                        <span className="text-xs font-semibold text-lime-400 uppercase tracking-wider">
                          Liability #{idx + 1}
                        </span>
                        {formData.loans.length > 1 && (
                          <button
                            type="button"
                            onClick={() => removeLoanRow(idx)}
                            className="text-xs text-neutral-500 hover:text-red-400"
                          >
                            Remove
                          </button>
                        )}
                      </div>

                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                          <label className="block text-[11px] text-neutral-400 mb-1">Loan Category</label>
                          <select
                            value={loan.type}
                            onChange={(e) => updateLoanField(idx, "type", e.target.value)}
                            className="w-full bg-neutral-950 border border-neutral-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-lime-400"
                          >
                            <option value="Home Loan">Home Loan</option>
                            <option value="Education Loan">Education Loan</option>
                            <option value="Personal Loan">Personal Loan</option>
                            <option value="Vehicle Loan">Vehicle Loan</option>
                            <option value="Credit Card Outstanding">Credit Card Outstanding</option>
                          </select>
                        </div>

                        <div>
                          <label className="block text-[11px] text-neutral-400 mb-1">Lending Bank / Institution</label>
                          <input
                            type="text"
                            placeholder="e.g. SBI / HDFC"
                            value={loan.bank}
                            onChange={(e) => updateLoanField(idx, "bank", e.target.value)}
                            className="w-full bg-neutral-950 border border-neutral-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-lime-400"
                          />
                        </div>

                        <div>
                          <label className="block text-[11px] text-neutral-400 mb-1">Remaining Principal Amount (₹)</label>
                          <input
                            type="number"
                            placeholder="e.g. 15,00,000"
                            value={loan.amount}
                            onChange={(e) => updateLoanField(idx, "amount", e.target.value)}
                            className="w-full bg-neutral-950 border border-neutral-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-lime-400"
                          />
                        </div>

                        <div className="grid grid-cols-2 gap-2">
                          <div>
                            <label className="block text-[11px] text-neutral-400 mb-1">Interest Rate (%)</label>
                            <input
                              type="number"
                              step="0.1"
                              placeholder="e.g. 8.5"
                              value={loan.interestRate}
                              onChange={(e) => updateLoanField(idx, "interestRate", e.target.value)}
                              className="w-full bg-neutral-950 border border-neutral-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-lime-400"
                            />
                          </div>
                          <div>
                            <label className="block text-[11px] text-neutral-400 mb-1">Term Left (Years)</label>
                            <input
                              type="number"
                              placeholder="e.g. 10"
                              value={loan.tenureYears}
                              onChange={(e) => updateLoanField(idx, "tenureYears", e.target.value)}
                              className="w-full bg-neutral-950 border border-neutral-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-lime-400"
                            />
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}

                  <button
                    type="button"
                    onClick={addLoanRow}
                    className="text-xs font-semibold text-lime-400 border border-dashed border-neutral-800 hover:border-lime-400/50 w-full py-2.5 rounded-xl transition-colors"
                  >
                    + Add Another Loan Facility
                  </button>
                </div>
              )}
            </div>
          </div>
        )}

        {/* STEP 5: Risk Profile Assessment */}
        {step === 5 && (
          <div className="space-y-6">
            <div>
              <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                Risk Tolerance Assessment
              </h1>
              <p className="mt-1 text-neutral-400 text-sm">
                Determine your psychological comfort level with temporary market drawdowns.
              </p>
            </div>

            <div className="space-y-5">
              <div className="space-y-3">
                <p className="text-xs font-semibold text-neutral-400 uppercase tracking-wider">
                  What is your risk taking capacity?
                </p>

                <div className="space-y-2">
                  {[
                    { label: "High", val: 100 },
                    { label: "Moderate", val: 50 },
                    { label: "Low", val: 10 },
                  ].map((opt, i) => (
                    <button
                      key={i}
                      type="button"
                      onClick={() => setFormData({ ...formData, riskAnswers: { ...formData.riskAnswers, q1: opt.val } })}
                      className={`w-full p-3.5 rounded-xl border text-left text-xs font-medium transition-all ${formData.riskAnswers.q1 === opt.val
                        ? "bg-neutral-800 border-lime-400 text-white"
                        : "bg-neutral-900/60 border-neutral-800 text-neutral-400 hover:border-neutral-700"
                        }`}
                    >
                      {opt.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* STEP 6: Financial Objectives */}
        {/* STEP 6: Financial Objectives */}
        {/* STEP 6: Financial Objectives */}
        {step === 6 && (
          <div className="space-y-6">

            {/* Heading */}
            <div>
              <h1 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
                Financial Goals
              </h1>

              <p className="mt-1 text-neutral-400 text-sm">
                Tell us what you are saving and investing for, and set a target for your future.
              </p>
            </div>


            <div className="space-y-6">

              {/* ================= FINANCIAL GOALS ================= */}
              <div>

                <label className="block text-xs font-medium text-neutral-400 mb-2 uppercase tracking-wider">
                  What are you investing and saving for?
                </label>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">

                  {goalOptions.map((goal) => {

                    const isSelected = formData.goals.includes(goal.id);

                    return (
                      <button
                        key={goal.id}
                        type="button"
                        onClick={() =>
                          toggleArrayItem("goals", goal.id)
                        }
                        className={`p-3.5 rounded-xl border text-left text-xs font-medium transition-all flex items-center justify-between ${isSelected
                            ? "bg-neutral-800 border-lime-400 text-white"
                            : "bg-neutral-900/60 border-neutral-800 text-neutral-400 hover:border-neutral-700"
                          }`}
                      >

                        <span>{goal.label}</span>

                        <div
                          className={`w-4 h-4 rounded border flex items-center justify-center transition-colors ${isSelected
                              ? "bg-lime-400 border-lime-400 text-black"
                              : "border-neutral-700 bg-neutral-950"
                            }`}
                        >
                          {isSelected && (
                            <span className="text-[10px] font-bold">
                              ✓
                            </span>
                          )}
                        </div>

                      </button>
                    );

                  })}

                </div>

              </div>


              {/* ================= FINANCIAL TARGET ================= */}
              <div className="pt-5 border-t border-neutral-900">

                <div className="mb-4">

                  <h2 className="text-sm font-semibold text-white">
                    Your Financial Target
                  </h2>

                  <p className="text-xs text-neutral-500 mt-1">
                    Set the amount you want to accumulate and when you want to achieve it.
                  </p>

                </div>


                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">


                  {/* TARGET AMOUNT */}
                  <div className="bg-neutral-900 border border-neutral-800 p-5 rounded-2xl">

                    <label className="block text-xs font-medium text-neutral-400 uppercase tracking-wider mb-2">
                      Target Amount
                    </label>

                    <div className="flex items-center gap-2">

                      <span className="text-xl font-medium text-lime-400">
                        ₹
                      </span>

                      <input
                        type="number"
                        value={formData.targetAmount}
                        onChange={(e) =>
                          setFormData({
                            ...formData,
                            targetAmount: e.target.value
                          })
                        }
                        placeholder="50,00,000"
                        className="w-full bg-transparent text-xl font-semibold text-white placeholder-neutral-700 focus:outline-none"
                      />

                    </div>

                    <p className="text-[11px] text-neutral-500 mt-2">
                      How much money do you want to accumulate?
                    </p>

                  </div>


                  {/* TARGET TIMELINE */}
                  <div className="bg-neutral-900 border border-neutral-800 p-5 rounded-2xl">

                    <label className="block text-xs font-medium text-neutral-400 uppercase tracking-wider mb-2">
                      Target Timeline
                    </label>

                    <div className="flex items-center gap-2">

                      <input
                        type="number"
                        min="1"
                        value={formData.targetYears}
                        onChange={(e) =>
                          setFormData({
                            ...formData,
                            targetYears: e.target.value
                          })
                        }
                        placeholder="10"
                        className="w-full bg-transparent text-xl font-semibold text-white placeholder-neutral-700 focus:outline-none"
                      />

                      <span className="text-neutral-400 text-sm font-medium">
                        Years
                      </span>

                    </div>

                    <p className="text-[11px] text-neutral-500 mt-2">
                      When do you want to reach this target?
                    </p>

                  </div>

                </div>


                {/* GOAL SUMMARY */}
                {(formData.targetAmount || formData.targetYears) && (
                  <div className="mt-4 p-4 rounded-xl bg-lime-400/5 border border-lime-400/10">

                    <p className="text-xs text-neutral-400">
                      Your goal
                    </p>

                    <p className="text-sm font-medium text-white mt-1">

                      {formData.targetAmount
                        ? `Accumulate ₹${Number(formData.targetAmount).toLocaleString("en-IN")}`
                        : "Set your target amount"}

                      {formData.targetYears
                        ? ` within ${formData.targetYears} ${Number(formData.targetYears) === 1
                          ? "year"
                          : "years"
                        }.`
                        : "."}

                    </p>

                  </div>
                )}

              </div>

            </div>

          </div>
        )}
        {/* STEP 7: Final Analysis Screen */}
        {step === 7 && (
          <div className="py-6 space-y-6 text-center">
            <div>
              <span className="text-[11px] font-mono tracking-widest text-lime-400 uppercase">
                MoneyBuddy Analytical Core
              </span>
              <h2 className="text-2xl sm:text-3xl font-semibold text-white mt-1">
                Synthesizing Financial Framework
              </h2>
            </div>

            {/* Progress Radial Bar */}
            <div className="w-full bg-neutral-900 h-2 rounded-full overflow-hidden border border-neutral-800 my-4">
              <div
                className="bg-lime-400 h-full transition-all duration-100 ease-out"
                style={{ width: `${analysisProgress}%` }}
              />
            </div>

            {/* Step Verification Checkmarks */}
            <div className="bg-neutral-900 border border-neutral-800 p-5 rounded-2xl max-w-md mx-auto text-left space-y-2.5 font-mono text-xs">
              {[
                "Demographic Profile Verified",
                "Cashflow Net Margin Computed",
                "Liability Structure Analyzed",
                "Risk Metric Weighted",
                "Horizon Strategy Formulated",
              ].map((label, idx) => {
                const isDone = completedCheckmarks.includes(idx + 1);
                return (
                  <div key={label} className="flex items-center justify-between">
                    <span className={isDone ? "text-neutral-200" : "text-neutral-600"}>
                      {label}
                    </span>
                    <span className={isDone ? "text-lime-400 font-bold" : "text-neutral-700"}>
                      {isDone ? "✓ DONE" : "PENDING..."}
                    </span>
                  </div>
                );
              })}
            </div>

            {/* Action Button once completed */}
            {analysisProgress === 100 && (
              <button
                onClick={() => navigate("/portfolio")}
                className="w-full max-w-md mx-auto bg-lime-400 text-black font-extrabold py-3.5 px-6 rounded-xl text-sm hover:bg-lime-300 shadow-lg shadow-lime-400/20 transition-all cursor-pointer animate-fadeIn"
              >
                Launch MoneyBuddy Decision Center →
              </button>
            )}
          </div>
        )}

        {/* Step Navigation Controls */}
        {step <= 6 && (
          <div className="flex items-center justify-between pt-8 border-t border-neutral-900 mt-8">
            <button
              type="button"
              onClick={handlePrev}
              disabled={step === 1}
              className={`px-5 py-2.5 rounded-xl text-xs font-semibold border border-neutral-800 transition-all ${step === 1
                ? "opacity-30 cursor-not-allowed text-neutral-600 border-transparent"
                : "text-neutral-300 hover:text-white hover:bg-neutral-900 cursor-pointer"
                }`}
            >
              ← Back
            </button>

            <button
              type="button"
              onClick={handleNext}
              className="bg-lime-400 text-black font-extrabold px-6 py-2.5 rounded-xl text-xs hover:bg-lime-300 shadow-md shadow-lime-400/10 active:scale-95 transition-all cursor-pointer"
            >
              {step === totalSteps ? "Generate Analysis →" : "Continue →"}
            </button>
          </div>
        )}

      </main>
    </div>
  );
}