import Vue from 'vue';
import Router from 'vue-router';
// import './stylus/main.styl'
import Home from '@/components/Home';
import Planners from '@/components/Planner/Planners'
import CreatePlanner from '@/components/Planner/CreatePlanner'
import SignIn from '@/components/User/SignIn'
import Profile from '@/components/User/Profile'
import Planner from '@/components/Planner/Planner'


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
      component: Planner,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: SignIn,
    },
  ],
  mode: 'history'
});
