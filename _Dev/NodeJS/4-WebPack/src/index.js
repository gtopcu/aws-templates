
/*
https://www.youtube.com/watch?v=5IG4UmULyoA
Also checkout: Snowpack

!!Initialize npm on the project root dir, not in /src!
npm init -y
npm i lodash
npm i path
npm i webpack
npm install -D webpack-cli

package.json:
"scripts": {
    "start": "nodemon ./dist/main.js",
    "build": "webpack",
    "test": "npm run tests.js"
  },
  
  Console:
  npm run build
*/

import { camelCase } from "lodash";
console.log(camelCase("Hello World! how was your day?"));
