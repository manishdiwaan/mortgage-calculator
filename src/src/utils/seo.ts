const SITE_URL = 'https://urmortgage.online';
const SITE_NAME = 'URMortgage';

export interface SEOMeta {
  title: string;
  description: string;
  canonical: string;
  ogImage?: string;
}

export function buildCanonical(path: string): string {
  const clean = path.startsWith('/') ? path : `/${path}`;
  const withTrailing = clean.endsWith('/') ? clean : `${clean}/`;
  return `${SITE_URL}${withTrailing}`;
}

export function buildOGMeta(meta: SEOMeta) {
  return {
    'og:type': 'website',
    'og:title': meta.title,
    'og:description': meta.description,
    'og:url': meta.canonical,
    'og:site_name': SITE_NAME,
    ...(meta.ogImage && { 'og:image': meta.ogImage }),
    'twitter:card': 'summary_large_image',
    'twitter:title': meta.title,
    'twitter:description': meta.description,
  };
}

export function buildCountryUrl(countryCode: string): string {
  return `${SITE_URL}/${countryCode}/`;
}

export function buildPillarUrl(countryCode: string, type: 'property-buying' | 'mortgage'): string {
  const slug = type === 'property-buying' ? 'property-buying-guide' : 'mortgage-guide';
  return `${SITE_URL}/${countryCode}/${slug}/`;
}

export function buildBlogUrl(countryCode: string, blogSlug: string): string {
  return `${SITE_URL}/${countryCode}/blog/${blogSlug}/`;
}

export function buildFaqUrl(countryCode: string): string {
  return `${SITE_URL}/${countryCode}/faqs/`;
}
