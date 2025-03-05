module.exports = {
    content: [
      "./website/templates/**/*.html",
      "./templates/*.html",
      "./templates/**/*.html",
    ],
    theme: {
      container: {
        center: true,
        padding: {
          DEFAULT: "1rem",
          sm: "2rem",
        },
      },
  
      extend: {
        colors: {
          primaryGreen: "#14897b",
          lightGreen: "#32bdb5",
          textDark: "#231f20",
          lightGray: "#615959",
        },
      },
  
      fontFamily: {
        norwester: ["Norwester", "sans-serif"],
        kollektif: ["Kollektif", "sans-serif"],
        gilroy: ["Gilroy", "sans-serif"],
        poppins: ["Poppins", "sans-serif"],
      },
    },
  
    daisyui: {
      themes: false,
    },
    plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography"),
      require("daisyui"),
    ],
  };
  