module.exports = {
    root: true,
    env: {
      node: true,
    },
    'extends': [
      'plugin:vue/strongly-recommended'
    ],
    rules: {
      'no-tabs': 'off',
      'indent': 'off',
    },
    'overrides': [
      {
        'files': ['*.vue'],
        'rules': {
          'indent': 'off'
        }
      }
    ]
  };