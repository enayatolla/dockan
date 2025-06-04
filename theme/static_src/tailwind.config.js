/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
/** @type {import('tailwindcss').Config} */

module.exports = {
   content: [
      /**
       * HTML. Paths to Django template files that will contain Tailwind CSS classes.
       */

      /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
      "../templates/**/*.html",

      /*
       * Main templates directory of the project (BASE_DIR/templates).
       * Adjust the following line to match your project structure.
       */
      "../../templates/**/*.html",

      /*
       * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
       * Adjust the following line to match your project structure.
       */
      "../../**/templates/**/*.html",

      /**
       * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
       * patterns match your project structure.
       */
      /* JS 1: Ignore any JavaScript in node_modules folder. */
      // '!../../**/node_modules',
      /* JS 2: Process all JavaScript files in the project. */
      // '../../**/*.js',

      /**
       * Python: If you use Tailwind CSS classes in Python, uncomment the following line
       * and make sure the pattern below matches your project structure.
       */
      // '../../**/*.py'
   ],
   plugins: [
      /**
       * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
       * for forms. If you don't like it or have own styling for forms,
       * comment the line below to disable '@tailwindcss/forms'.
       */
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography"),
      require("@tailwindcss/aspect-ratio"),
   ],
   darkMode: "class",
   theme: {
      screens: {
         xs: "480px",
         sm: "640px",
         md: "768px",
         lg: "1024px",
         xl: "1380px",
      },

      extend: {
         spacing: {
            25: "6.25rem",
            50: "12.5rem",
         },
         boxShadow: {
            base: "0px 1px 10px rgba(0, 0, 0, 0.05)",
         },
         borderRadius: {
            "4xl": "2rem",
         },
         container: {
            center: true,
            padding: {
               DEFAULT: "1rem",
               lg: "0.625rem",
            },
         },
         animation: {
            "border-width": "border-width 500ms forwards",
            "border-width-reverse": "border-width-reverse 500ms forwards",
         },
         keyframes: {
            "border-width": {
               from: {
                  width: "0",
                  opacity: "0",
               },
               to: {
                  width: "100%",
                  opacity: "1",
               },
            },
            "border-width-reverse": {
               from: {
                  width: "100%",
                  opacity: "1",
               },
               to: {
                  width: "0",
                  opacity: "0",
               },
            },
         },
         colors: {
            white: "#FEFEFF",
            black: "#0D0D0D",
         },
         borderRadius: {
            base: "13px",
         },
         fontFamily: {
            iranyekan: "IRANYekan",
         },
      },
   },
};
