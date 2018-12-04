import Vue from 'vue';
import Router from 'vue-router';
// import './stylus/main.styl'
import Home from '@/components/Home';
import Planners from '@/components/Planner/Planners';
import CreatePlanner from '@/components/Planner/CreatePlanner';
import SignIn from '@/components/User/SignIn';
import Planner from '@/components/Planner/Planner';


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/planners',
      name: 'Planners',
      component: Planners,
    },
    {
      path: '/planner/new',
      name: 'CreatePlanner',
      component: CreatePlanner,
    },
    {
      path: '/planners/:id',
      name: 'Planner',
      props: true,
      component: Planner,
    },
    {
      path: '/account',
      name: 'SignIn',
      component: SignIn,
    },

  ],

  mode: 'hash',

});
