import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const countries = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/countries' }),
  schema: z.object({
    name: z.string(),
    code: z.string(),
    iso: z.string(),
    currency: z.string(),
    currencySymbol: z.string(),
    flag: z.string(),
    language: z.string().default('en'),
    region: z.string(),
    metaTitle: z.string(),
    metaDescription: z.string(),
    centralBank: z.string(),
    published: z.boolean().default(false),
  }),
});

const pillarGuides = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/pillar-guides',
    generateId: ({ entry }) => entry.replace(/\.mdx?$/, ''),
  }),
  schema: z.object({
    title: z.string(),
    country: z.string(),
    slug: z.string(),
    type: z.enum(['property-buying', 'mortgage']),
    metaTitle: z.string(),
    metaDescription: z.string(),
    primaryKeyword: z.string(),
    secondaryKeywords: z.array(z.string()).default([]),
    publishDate: z.coerce.date(),
    lastUpdated: z.coerce.date(),
    wordCount: z.number().optional(),
    faqs: z.array(z.object({
      question: z.string(),
      answer: z.string(),
    })).default([]),
    relatedBlogs: z.array(z.string()).default([]),
    published: z.boolean().default(false),
  }),
});

const blogs = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/blogs',
    generateId: ({ entry }) => entry.replace(/\.mdx?$/, ''),
  }),
  schema: z.object({
    title: z.string(),
    country: z.string(),
    slug: z.string(),
    category: z.enum([
      'first-home', 'costs', 'taxes', 'grants',
      'inspections', 'loan-types', 'rent-vs-buy',
      'investment', 'refinancing', 'mistakes',
    ]),
    metaTitle: z.string(),
    metaDescription: z.string(),
    primaryKeyword: z.string(),
    secondaryKeywords: z.array(z.string()).default([]),
    publishDate: z.coerce.date(),
    lastUpdated: z.coerce.date(),
    wordCount: z.number().optional(),
    heroImage: z.string().optional(),
    imageAlt: z.string().optional(),
    relatedPosts: z.array(z.string()).default([]),
    published: z.boolean().default(false),
  }),
});

const faqs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/faqs' }),
  schema: z.object({
    country: z.string(),
    metaTitle: z.string().optional(),
    metaDescription: z.string().optional(),
    faqs: z.array(z.object({
      question: z.string(),
      answer: z.string(),
      category: z.enum([
        'buying-process', 'financing', 'costs',
        'legal', 'investment', 'general',
      ]),
    })),
    published: z.boolean().default(false),
  }),
});

export const collections = {
  countries,
  'pillar-guides': pillarGuides,
  blogs,
  faqs,
};
