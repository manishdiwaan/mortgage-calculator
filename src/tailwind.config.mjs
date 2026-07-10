/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#004ac6',
        secondary: '#006c49',
        surface: '#f8f9ff',
        'bg-dark': '#0F172A',
        border: '#c3c6d7',
      },
      fontFamily: {
        sans: ['Geist', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '16px',
        input: '12px',
        button: '10px',
      },
      maxWidth: {
        content: '720px',
        page: '1200px',
      },
    },
  },
  plugins: [],
};
