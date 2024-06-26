import InputText from "primevue/inputtext";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth'
  ],
  primevue: {
    components: {
      include: ['Button', 'Avatar', 'InputText', 'FloatLabel', 'Menubar']
    }
  },
  css: [
    'primeicons/primeicons.css',
    'primevue/resources/themes/aura-light-green/theme.css',
    'primeflex/primeflex.css',
    '~/assets/global.scss',
  ],
  auth: {
    baseURL: 'somativaandrelivraria-production.up.railway.app',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut:{ path: '/token/logout', method: 'post'},
        getSession: { path: '/token/login', method: 'get'},
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token'},
      pages: { login: '/' }
    } 
  }
})



