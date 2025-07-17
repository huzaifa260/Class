const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
// vue.config.js
module.exports = {
  devServer: {
    port: 8081, // You can change this to any free port
  }
};

// module.exports = {
//   devServer: {
//     client: {
//       webSocketURL: {
//         protocol: 'wss', // Use secure WebSocket (wss://)
//         hostname: 'ec30-103-51-138-174.ngrok-free.app', // Your ngrok URL
//         port: 443, // HTTPS port
//       },
//     },
//     allowedHosts: 'all', // Allow all hosts
//   },
// };






