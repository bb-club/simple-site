
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: 'Index', path: '', component: () => import('pages/Index.vue') },
      { name: 'Contact', path: '/contact', component: () => import('pages/contact.vue') },
      { name: 'Partners', path: '/partners', component: () => import('pages/partners.vue') },
      { name: 'Delivery', path: '/delivery', component: () => import('pages/delivery.vue') },
      { name: 'Products', path: '/products', component: () => import('pages/products.vue') },
      { name: 'News', path: '/news', component: () => import('pages/news.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
