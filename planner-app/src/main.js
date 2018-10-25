import Vue from 'vue';
import App from './App';
import router from './router/index';
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
} from 'vuetify';

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

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
});
