// Internal Linking Matrix
// Enforces the linking rules from architecture_rules.md

export interface InternalLinks {
  pillarGuides: { title: string; url: string }[];
  faqHub: { title: string; url: string };
  calculator: { title: string; url: string };
  relatedBlogs: { title: string; url: string }[];
  countryHub: { title: string; url: string };
  loanProducts?: { title: string; url: string };
}

export function getBlogLinks(
  countryCode: string,
  countryName: string,
  relatedSlugs: string[] = []
): InternalLinks {
  return {
    pillarGuides: [
      {
        title: `Property Buying Guide — ${countryName}`,
        url: `/${countryCode}/property-buying-guide/`,
      },
      {
        title: `Mortgage Guide — ${countryName}`,
        url: `/${countryCode}/mortgage-guide/`,
      },
    ],
    faqHub: {
      title: `${countryName} Mortgage FAQs`,
      url: `/${countryCode}/faqs/`,
    },
    calculator: {
      title: 'Mortgage Calculator',
      url: `/calculator/?country=${countryCode}`,
    },
    relatedBlogs: relatedSlugs.map((slug) => ({
      title: slug.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()),
      url: `/${countryCode}/blog/${slug}/`,
    })),
    countryHub: {
      title: `${countryName} — Mortgage Hub`,
      url: `/${countryCode}/`,
    },
  };
}

export function getPillarLinks(
  countryCode: string,
  countryName: string,
  allBlogSlugs: string[] = []
): InternalLinks {
  return {
    pillarGuides: [
      {
        title: `Property Buying Guide — ${countryName}`,
        url: `/${countryCode}/property-buying-guide/`,
      },
      {
        title: `Mortgage Guide — ${countryName}`,
        url: `/${countryCode}/mortgage-guide/`,
      },
    ],
    faqHub: {
      title: `${countryName} Mortgage FAQs`,
      url: `/${countryCode}/faqs/`,
    },
    calculator: {
      title: 'Mortgage Calculator',
      url: `/calculator/?country=${countryCode}`,
    },
    relatedBlogs: allBlogSlugs.map((slug) => ({
      title: slug.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()),
      url: `/${countryCode}/blog/${slug}/`,
    })),
    countryHub: {
      title: `${countryName} — Mortgage Hub`,
      url: `/${countryCode}/`,
    },
  };
}

export function validateLinks(links: InternalLinks): string[] {
  const errors: string[] = [];
  if (links.pillarGuides.length < 2) {
    errors.push('Must link to both pillar guides');
  }
  if (!links.faqHub.url) {
    errors.push('Missing FAQ hub link');
  }
  if (!links.calculator.url) {
    errors.push('Missing calculator link');
  }
  if (links.relatedBlogs.length < 2) {
    errors.push('Must link to at least 2 related blogs');
  }
  return errors;
}
