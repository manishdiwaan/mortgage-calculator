import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://urmortgage.online',
  trailingSlash: 'always',
  integrations: [
    mdx(),
    sitemap({
      customPages: [
        'https://urmortgage.online/calculator/',
        'https://urmortgage.online/privacy/',
        'https://urmortgage.online/terms/',
      ],
    }),
    tailwind(),
  ],
});
