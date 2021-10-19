import Vue from 'vue';
import Router from 'vue-router';
import Login from './components/login.vue';
import Space_Jam from './components/space_jam/game.vue';
import Register from './components/register.vue';
import Chat from './components/chat.vue';
import Tutorial from './components/space_jam/tutorial.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Login-Default',
      component: Login,
      props: true,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      props: true,
    },
    {
      path: '/experiment',
      name: 'Space_Jam',
      component: Space_Jam,
      props: true,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
    },
    // {
    //   path: '/chat',
    //   name: "Chat",
    //   component: Chat,
    // },
    {
      path: '/tutorial',
      name: 'Tutorial',
      component: Tutorial
    },                 
  ],
});
