import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from './components/UserLogin.vue';
import DashboardBase from './components/DashboardBase.vue';
import ResetPassword from './components/ResetPassword.vue';

const routes = [
  { path: '/', component: UserLogin },
  { path: '/dashboard', component: DashboardBase, meta: { requiresAuth: true } },
  { path: '/resetpassword', component:ResetPassword}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
    console.log('Token en localStorage:', localStorage.getItem('token'));
  const isAuthenticated = !!localStorage.getItem('token'); 
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/');
  } else {
    next();
  }
});

export default router;
