import Vue from 'vue';
import Vuex from 'vuex';
import App from './App';
import router from './router/index';
import VueCookie from 'vue-cookie';
import { store } from './store';
import VueLogger from 'vuejs-logger';


import VuetifyGoogleAutocomplete from 'vuetify-google-autocomplete';
import GSignInButton from 'vue-google-signin-button';
import FBSignInButton from 'vue-facebook-signin-button';
import GAuth from 'vue-google-oauth2';

import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VToolbar,
  transitions,
  VForm,
  VTextField,
  VCard,
  VCarousel,
  VDatePicker,
  VTimePicker,
  VMenu,
  VDataTable,
  VTimeline,
  VAutocomplete,
  VDivider,
  VCombobox,
  VAlert,

} from 'vuetify';


Vue.use(GAuth, { clientId: '464916650517-c62c52q1j7jhvbuksr8a16i48d62au4t.apps.googleusercontent.com', scope: 'profile email https://www.googleapis.com/auth/plus.login' });

Vue.use(FBSignInButton);

Vue.use(GSignInButton);

Vue.use(VuetifyGoogleAutocomplete, {
  apiKey: process.env.API_KEY, // Can also be an object. E.g, for Google Maps Premium API, pass `{ client: <YOUR-CLIENT-ID> }`
});

Vue.use(Vuex);
Vue.use(VueCookie);


Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    transitions,
    VForm,
    VTextField,
    VCard,
    VCarousel,
    VDatePicker,
    VTimePicker,
    VMenu,
    VDataTable,
    VTimeline,
    VAutocomplete,
    VDivider,
    VCombobox,
    VAlert,
  },
  theme: {
    primary: '#FFAB00',
    secondary: '#424242',
    accent: '#82B1FF',
    error: '#FF5252',
    info: '#81D4FA',
    success: '#4CAF50',
    warning: '#FFC107',
  },
});

Vue.config.productionTip = false;

const isProduction = process.env.NODE_ENV === 'production';

const options = {
  isEnabled: true,
  logLevel: isProduction ? 'error' : 'debug',
  stringifyArguments: false,
  showLogLevel: true,
  showMethodName: true,
  separator: ' ',
  showConsoleColors: true
};

Vue.use(VueLogger, options);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
});
