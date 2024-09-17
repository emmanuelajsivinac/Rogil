module.exports = {
    root: true,
    env: {
      node: true,
    },
    extends: [
      'plugin:vue/vue3-essential',
      'eslint:recommended',
    ],
    parserOptions: {
      parser: '@babel/eslint-parser',
      requireConfigFile: false, // Desactiva la advertencia sobre el archivo de configuración de Babel
    },
    rules: {
    },
  }
  