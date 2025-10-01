// Inline SVG components for decoration
function FloralDivider() {
  return (
    <svg viewBox="0 0 600 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" className="w-full h-10">
      <g fill="none" stroke="#cfa15b" strokeWidth="1.5">
        <path d="M10 30 Q100 5 190 30 T370 30 T550 30" opacity=".5" />
        <path d="M10 35 Q100 10 190 35 T370 35 T550 35" opacity=".25" />
      </g>
      <g fill="#cfa15b">
        <circle cx="300" cy="30" r="3" />
        <circle cx="220" cy="30" r="2" />
        <circle cx="380" cy="30" r="2" />
      </g>
    </svg>
  )
}

function Rings() {
  return (
    <svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" className="w-28 h-28">
      <defs>
        <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#cfa15b" />
          <stop offset="50%" stopColor="#f6d17a" />
          <stop offset="100%" stopColor="#cfa15b" />
        </linearGradient>
      </defs>
      <g fill="none" stroke="url(#gold)" strokeWidth="6">
        <circle cx="55" cy="65" r="28" />
        <circle cx="75" cy="55" r="28" />
      </g>
      <polygon points="60,12 68,26 52,26" fill="#f6d17a" stroke="#cfa15b" strokeWidth="2" />
    </svg>
  )
}
import { useDispatch, useSelector } from 'react-redux'
import { nextStep } from './store/uiSlice'

function App() {
  const dispatch = useDispatch()
  const step = useSelector((state) => state.ui.step)

  return (
    <div className="min-h-full bg-rose-50 bg-rose-gradient text-slate-800">
      {/* Header */}
      <header className="relative">
        <div className="absolute inset-0 pointer-events-none">
          <FloralDivider />
        </div>
        <div className="mx-auto max-w-7xl px-6 py-6 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="shrink-0">{Rings}</div>
            <span className="font-display text-2xl tracking-wide text-gradient-gold">WeddingBazaar</span>
          </div>
          <nav className="hidden sm:flex items-center gap-6 text-sm">
            <a className="hover:text-rose-600" href="#stories">Stories</a>
            <a className="hover:text-rose-600" href="#vendors">Vendors</a>
            <a className="hover:text-rose-600" href="#planning">Planning</a>
          </nav>
          <a href="#get-started" className="inline-flex items-center rounded-full bg-rose-500 text-white px-5 py-2 text-sm shadow hover:bg-rose-600 transition">Get Started</a>
        </div>
      </header>

      {/* Hero */}
      <main className="relative overflow-hidden">
        <div className="absolute -top-24 -left-24 w-96 h-96 rounded-full bg-rose-200/40 blur-3xl" />
        <div className="absolute -bottom-24 -right-24 w-96 h-96 rounded-full bg-pink-100/40 blur-3xl" />

        <section className="mx-auto max-w-7xl px-6 pt-16 pb-10 text-center">
          <h1 className="font-display text-4xl sm:text-6xl leading-tight text-slate-900">
            Celebrate Your Love Story
          </h1>
          <p className="mt-4 text-slate-600 max-w-2xl mx-auto">
            Discover curated vendors, dreamy inspirations, and a seamless planning experience — all in one place.
          </p>
          <div className="mt-8 flex items-center justify-center gap-4">
            <button onClick={() => dispatch(nextStep())} className="rounded-full bg-slate-900 text-white px-6 py-3 text-sm shadow hover:bg-slate-800 transition">Explore Venues</button>
            <button onClick={() => dispatch(nextStep())} className="rounded-full border border-rose-300 text-rose-700 px-6 py-3 text-sm hover:bg-rose-50 transition">Get Inspired</button>
          </div>

          <div className="mt-12 flex items-center justify-center">
            <Rings />
          </div>

          <div className="mt-10">
            <FloralDivider />
          </div>
        </section>

        {/* Features */}
        <section className="mx-auto max-w-7xl px-6 py-12 grid sm:grid-cols-3 gap-6">
          <div className="rounded-2xl bg-white/70 backdrop-blur border border-rose-100 p-6 text-left">
            <div className="mb-3">
              <svg viewBox="0 0 24 24" className="w-8 h-8" fill="none" stroke="#cfa15b" strokeWidth="1.5" aria-hidden="true">
                <path d="M12 3l2.5 5 5 .7-3.7 3.6.9 5.2L12 15l-4.7 2.5.9-5.2L4.5 8.7l5-.7L12 3z" />
              </svg>
            </div>
            <h3 className="font-display text-xl text-slate-900">Handpicked Vendors</h3>
            <p className="mt-2 text-slate-600 text-sm">Discover trusted professionals for venues, decor, photography, and more.</p>
          </div>
          <div className="rounded-2xl bg-white/70 backdrop-blur border border-rose-100 p-6 text-left">
            <div className="mb-3">
              <svg viewBox="0 0 24 24" className="w-8 h-8" fill="none" stroke="#cfa15b" strokeWidth="1.5" aria-hidden="true">
                <circle cx="12" cy="8" r="4" />
                <path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8" />
              </svg>
            </div>
            <h3 className="font-display text-xl text-slate-900">Personalized Planning</h3>
            <p className="mt-2 text-slate-600 text-sm">Tailor your checklist and budget to match your style and timeline.</p>
          </div>
          <div className="rounded-2xl bg-white/70 backdrop-blur border border-rose-100 p-6 text-left">
            <div className="mb-3">
              <svg viewBox="0 0 24 24" className="w-8 h-8" fill="none" stroke="#cfa15b" strokeWidth="1.5" aria-hidden="true">
                <path d="M4 7h16M4 12h16M4 17h10" />
              </svg>
            </div>
            <h3 className="font-display text-xl text-slate-900">Inspiration Library</h3>
            <p className="mt-2 text-slate-600 text-sm">Browse color palettes, themes, and real wedding stories.</p>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="mx-auto max-w-7xl px-6 py-10 text-center text-sm text-slate-500">
        <p className="mb-1">Onboarding step: <span className="font-semibold text-slate-700">{step}</span></p>
        <p>&copy; {new Date().getFullYear()} WeddingBazaar. Crafted with love.</p>
      </footer>
    </div>
  )
}

export default App
