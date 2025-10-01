/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        blush: {
          50: '#fff1f3',
          100: '#ffe4e8',
          200: '#fecdd6',
          300: '#fda4af',
          400: '#fb7185',
          500: '#f43f5e',
          600: '#e11d48',
        },
        champagne: '#f7e7ce',
        gold: '#cfa15b',
      },
      fontFamily: {
        display: ['"Playfair Display"', 'serif'],
        script: ['"Great Vibes"', 'cursive'],
      },
      backgroundImage: {
        'rose-gradient': 'radial-gradient(circle at 20% 20%, rgba(255,240,245,0.9), rgba(255,240,245,0)), radial-gradient(circle at 80% 30%, rgba(253,164,175,0.25), rgba(253,164,175,0)), radial-gradient(circle at 50% 80%, rgba(250,232,255,0.3), rgba(250,232,255,0))',
      }
    },
  },
  plugins: [],
}
