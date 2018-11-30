'use strict'
require('dotenv/config');
module.exports = {
  NODE_ENV: '"production"',
  API_KEY: JSON.stringify(process.env.VUE_APP_KEY),
  OAUTH_KEY: JSON.stringify(process.env.VUE_APP_OAUTH),
  SEARCH: '"api/search/"',
  TIME_REMAIN: '"api/time-remain/"',
  SAVE_DATA: '"api/savedata/"',
  PLACE_DURATION: '"api/place/"',
  PLAN_DATA: '"api/plan_data/"',
  USER_DATA: '"api/user_data/"',
  API_URL: '""',
}
