const SITE = {
  name: 'URMortgage',
  url: 'https://urmortgage.online',
  logo: 'https://urmortgage.online/images/logo.png',
};

export interface ArticleSchemaData {
  title: string;
  description: string;
  url: string;
  publishDate: string;
  lastUpdated: string;
  image?: string;
}

export interface FAQItem {
  question: string;
  answer: string;
}

export interface BreadcrumbItem {
  name: string;
  url: string;
}

export function organizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: SITE.name,
    url: SITE.url,
    logo: SITE.logo,
  };
}

export function websiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: SITE.name,
    url: SITE.url,
  };
}

export function softwareApplicationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name: 'URMortgage Calculator',
    applicationCategory: 'FinanceApplication',
    operatingSystem: 'Web',
    url: `${SITE.url}/calculator`,
    offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    description: 'Free mortgage calculator supporting 29 countries, 250+ lenders, with central bank rate tracking and full amortisation scheduling.',
  };
}

export function articleSchema(data: ArticleSchemaData) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: data.title,
    description: data.description,
    datePublished: data.publishDate,
    dateModified: data.lastUpdated,
    author: { '@type': 'Organization', name: SITE.name, url: SITE.url },
    publisher: {
      '@type': 'Organization',
      name: SITE.name,
      url: SITE.url,
      logo: { '@type': 'ImageObject', url: SITE.logo },
    },
    mainEntityOfPage: { '@type': 'WebPage', '@id': data.url },
    ...(data.image && { image: { '@type': 'ImageObject', url: data.image } }),
  };
}

export function faqSchema(faqs: FAQItem[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: { '@type': 'Answer', text: faq.answer },
    })),
  };
}

export function breadcrumbSchema(items: BreadcrumbItem[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      item: item.url.startsWith('http') ? item.url : `${SITE.url}${item.url}`,
    })),
  };
}
