/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './mainsite/templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#E879F9',
        // primaryDark: '#FBCFE8',
        secondary: '#F472B6',
        white: '#FAFAF9',
        black: '#1C1917',
        success: '#A7F3D0',
        error: '#F87171',
        warning: '#FED7AA',
      },
    },
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '1rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
  },
  plugins: [],
}

