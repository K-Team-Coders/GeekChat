/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        corme: "Cormorant Garamond",
        rale: "Raleway",
        roboto: "Roboto",
        monster: "Montserrat",
        stengazeta: ["Stengazeta", "sans-serif"],
      },
      colors: {
        background: "rgba(var(--background))",
        activeText: "rgba(var(--active-text))",
        unactiveText: "rgba(var(--unactive-text))",
        frameBackground: "rgba(var(--frame-background))",
        outlineColor: "rgba(var(--outline))",
        hoverBackground: "rgba(var(--hover-background))",
        inputBorder: "rgba(var(--input-border))",
        inputBackground: "rgba(var(--input-background))",
        inputText: "rgba(var(--input-text))",
        buttonBackground: "rgba(var(--button-background))",
        buttonHover: "rgba(var(--button-hover))",
        outputBorder: "rgba(var(--output-border))",
        outputBackground: "rgba(var(--output-background))",
        contrast: "rgba(var(--contrast))",
      },

      boxShadow: {
        "3xl": "0px 5px 44px -8px rgba(255, 255, 255, 0.8)",
        "4xl": "0px 2px 10px 1px rgba(0, 0, 0, 0.27)",
        "5xl": "0px 5px 5px 1px rgba(0, 0, 0, 0.27)",
      },
    },
  },
};
