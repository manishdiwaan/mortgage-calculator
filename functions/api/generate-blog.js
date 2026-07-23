// Blog Generation API — Cloudflare Pages Function
// POST /api/generate-blog
// Requires ADMIN_SECRET header, CLAUDE_API_KEY and GITHUB_TOKEN env vars

const COUNTRIES = [
  { name: 'Australia', slug: 'australia', currency: 'AUD', currencySymbol: '$' },
  { name: 'Belgium', slug: 'belgium', currency: 'EUR', currencySymbol: '€' },
  { name: 'Brazil', slug: 'brazil', currency: 'BRL', currencySymbol: 'R$' },
  { name: 'Canada', slug: 'canada', currency: 'CAD', currencySymbol: '$' },
  { name: 'Denmark', slug: 'denmark', currency: 'DKK', currencySymbol: 'kr' },
  { name: 'France', slug: 'france', currency: 'EUR', currencySymbol: '€' },
  { name: 'Germany', slug: 'germany', currency: 'EUR', currencySymbol: '€' },
  { name: 'Hong Kong', slug: 'hong-kong', currency: 'HKD', currencySymbol: 'HK$' },
  { name: 'India', slug: 'india', currency: 'INR', currencySymbol: '₹' },
  { name: 'Ireland', slug: 'ireland', currency: 'EUR', currencySymbol: '€' },
  { name: 'Italy', slug: 'italy', currency: 'EUR', currencySymbol: '€' },
  { name: 'Japan', slug: 'japan', currency: 'JPY', currencySymbol: '¥' },
  { name: 'Malaysia', slug: 'malaysia', currency: 'MYR', currencySymbol: 'RM' },
  { name: 'Mexico', slug: 'mexico', currency: 'MXN', currencySymbol: '$' },
  { name: 'Netherlands', slug: 'netherlands', currency: 'EUR', currencySymbol: '€' },
  { name: 'New Zealand', slug: 'new-zealand', currency: 'NZD', currencySymbol: '$' },
  { name: 'Norway', slug: 'norway', currency: 'NOK', currencySymbol: 'kr' },
  { name: 'Portugal', slug: 'portugal', currency: 'EUR', currencySymbol: '€' },
  { name: 'Saudi Arabia', slug: 'saudi-arabia', currency: 'SAR', currencySymbol: '﷼' },
  { name: 'Singapore', slug: 'singapore', currency: 'SGD', currencySymbol: '$' },
  { name: 'South Africa', slug: 'south-africa', currency: 'ZAR', currencySymbol: 'R' },
  { name: 'South Korea', slug: 'south-korea', currency: 'KRW', currencySymbol: '₩' },
  { name: 'Spain', slug: 'spain', currency: 'EUR', currencySymbol: '€' },
  { name: 'Sweden', slug: 'sweden', currency: 'SEK', currencySymbol: 'kr' },
  { name: 'Switzerland', slug: 'switzerland', currency: 'CHF', currencySymbol: 'CHF' },
  { name: 'Thailand', slug: 'thailand', currency: 'THB', currencySymbol: '฿' },
  { name: 'UAE', slug: 'uae', currency: 'AED', currencySymbol: 'د.إ' },
  { name: 'United Kingdom', slug: 'united-kingdom', currency: 'GBP', currencySymbol: '£' },
  { name: 'United States', slug: 'united-states', currency: 'USD', currencySymbol: '$' },
];

const BLOG_CATEGORIES = [
  'first-home', 'costs', 'taxes', 'grants', 'inspections',
  'loan-types', 'rent-vs-buy', 'investment', 'refinancing', 'mistakes'
];

const EXISTING_SLUGS = [
  'buying-costs-explained', 'common-buying-mistakes', 'first-home-buyer-guide',
  'government-grants-schemes', 'mortgage-types-compared', 'property-inspection-checklist',
  'property-investment-guide', 'property-tax-guide', 'refinancing-guide',
  'rent-vs-buy-analysis', 'stamp-duty-explained'
];

function getCountryForWeek() {
  const now = new Date();
  const startOfYear = new Date(now.getFullYear(), 0, 1);
  const weekNumber = Math.ceil(((now - startOfYear) / 86400000 + startOfYear.getDay() + 1) / 7);
  const index = (weekNumber - 1) % COUNTRIES.length;
  return COUNTRIES[index];
}

function getNextCountries(count = 5) {
  const now = new Date();
  const startOfYear = new Date(now.getFullYear(), 0, 1);
  const weekNumber = Math.ceil(((now - startOfYear) / 86400000 + startOfYear.getDay() + 1) / 7);
  const result = [];
  for (let i = 0; i < count; i++) {
    const index = (weekNumber - 1 + i) % COUNTRIES.length;
    result.push({ week: weekNumber + i, country: COUNTRIES[index] });
  }
  return result;
}

function buildPrompt(country) {
  const today = new Date().toISOString().split('T')[0];
  const year = new Date().getFullYear();

  return `You are a senior real estate content writer for URMortgage.online, a mortgage and property knowledge platform.

Write a NEW, UNIQUE blog post about mortgages or property buying in ${country.name}. The topic must be DIFFERENT from these existing posts:
${EXISTING_SLUGS.map(s => `- ${s}`).join('\n')}

Requirements:
1. Choose a specific, useful topic relevant to ${country.name}'s current property market (e.g., "How to Negotiate Property Prices in ${country.name}", "Understanding ${country.name}'s Mortgage Pre-Approval Process", "Best Neighborhoods for First-Time Buyers in ${country.name}", etc.)
2. Write 1200-1800 words of genuinely helpful, specific content with real local details
3. Use ${country.currency} (${country.currencySymbol}) for any monetary amounts
4. Include practical tips, local regulations, current market context
5. Reference local institutions, laws, or programs by their actual names
6. Write for an educated audience making major financial decisions
7. DO NOT use generic filler content that could apply to any country

Return your response in EXACTLY this format (no extra text before or after):

---FRONTMATTER---
title: "[Your Title] ${year}"
slug: "[url-slug-no-spaces]"
category: "[pick one: ${BLOG_CATEGORIES.join(', ')}]"
metaTitle: "[50-60 char title] | URMortgage"
metaDescription: "[150-160 char description]"
primaryKeyword: "[main keyword phrase]"
secondaryKeywords: ["keyword1", "keyword2", "keyword3"]
---END_FRONTMATTER---

---CONTENT---
[Full markdown blog post content here. Use ## for H2, ### for H3. No H1.]
---END_CONTENT---`;
}

async function generateBlog(claudeKey, country) {
  const prompt = buildPrompt(country);

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': claudeKey,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-6-20250514',
      max_tokens: 4000,
      messages: [{ role: 'user', content: prompt }],
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(`Claude API error ${response.status}: ${err}`);
  }

  const data = await response.json();
  const text = data.content[0].text;

  // Parse frontmatter
  const fmMatch = text.match(/---FRONTMATTER---([\s\S]*?)---END_FRONTMATTER---/);
  const contentMatch = text.match(/---CONTENT---([\s\S]*?)---END_CONTENT---/);

  if (!fmMatch || !contentMatch) {
    throw new Error('Failed to parse Claude response — missing markers');
  }

  const fm = fmMatch[1].trim();
  const content = contentMatch[1].trim();

  // Extract fields from frontmatter
  const titleMatch = fm.match(/title:\s*"([^"]+)"/);
  const slugMatch = fm.match(/slug:\s*"([^"]+)"/);
  const categoryMatch = fm.match(/category:\s*"([^"]+)"/);
  const metaTitleMatch = fm.match(/metaTitle:\s*"([^"]+)"/);
  const metaDescMatch = fm.match(/metaDescription:\s*"([^"]+)"/);
  const primaryKwMatch = fm.match(/primaryKeyword:\s*"([^"]+)"/);
  const secondaryKwMatch = fm.match(/secondaryKeywords:\s*\[([^\]]+)\]/);

  if (!titleMatch || !slugMatch || !categoryMatch) {
    throw new Error('Failed to extract required fields from frontmatter');
  }

  const slug = slugMatch[1].toLowerCase().replace(/[^a-z0-9-]/g, '-').replace(/-+/g, '-');
  const category = BLOG_CATEGORIES.includes(categoryMatch[1]) ? categoryMatch[1] : 'investment';
  const secondaryKws = secondaryKwMatch
    ? secondaryKwMatch[1].split(',').map(k => k.trim().replace(/"/g, ''))
    : [];

  // Build the final .md file
  const today = new Date().toISOString().split('T')[0];
  const wordCount = content.split(/\s+/).length;

  const markdown = `---
title: "${titleMatch[1].replace(/"/g, '\\"')}"
country: "${country.slug}"
slug: "${slug}"
category: "${category}"
metaTitle: "${(metaTitleMatch ? metaTitleMatch[1] : titleMatch[1] + ' | URMortgage').replace(/"/g, '\\"')}"
metaDescription: "${(metaDescMatch ? metaDescMatch[1] : '').replace(/"/g, '\\"')}"
primaryKeyword: "${(primaryKwMatch ? primaryKwMatch[1] : '').replace(/"/g, '\\"')}"
secondaryKeywords:
${secondaryKws.map(k => `  - "${k}"`).join('\n')}
publishDate: ${today}
lastUpdated: ${today}
wordCount: ${wordCount}
heroImage: ""
imageAlt: ""
relatedPosts: []
published: true
---

${content}
`;

  return { markdown, slug, title: titleMatch[1], category, wordCount };
}

async function commitToGitHub(githubToken, country, slug, content) {
  const path = `src/src/content/blogs/${country.slug}/${slug}.md`;
  const message = `blog: add "${slug}" for ${country.name}`;

  // Base64 encode the content
  const encoded = btoa(unescape(encodeURIComponent(content)));

  // Check if file already exists
  const checkRes = await fetch(
    `https://api.github.com/repos/manishdiwaan/mortgage-calculator/contents/${path}`,
    {
      headers: {
        Authorization: `token ${githubToken}`,
        'User-Agent': 'URMortgage-Admin',
      },
    }
  );

  const body = {
    message,
    content: encoded,
    branch: 'main',
  };

  if (checkRes.ok) {
    const existing = await checkRes.json();
    body.sha = existing.sha; // Update existing file
  }

  const commitRes = await fetch(
    `https://api.github.com/repos/manishdiwaan/mortgage-calculator/contents/${path}`,
    {
      method: 'PUT',
      headers: {
        Authorization: `token ${githubToken}`,
        'User-Agent': 'URMortgage-Admin',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    }
  );

  if (!commitRes.ok) {
    const err = await commitRes.text();
    throw new Error(`GitHub API error ${commitRes.status}: ${err}`);
  }

  return await commitRes.json();
}

export async function onRequestPost(context) {
  const CLAUDE_KEY = context.env.CLAUDE_API_KEY;
  const GITHUB_TOKEN = context.env.GITHUB_TOKEN;
  const ADMIN_SECRET = context.env.ADMIN_SECRET;

  const corsHeaders = {
    'Access-Control-Allow-Origin': 'https://urmortgage.online',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, X-Admin-Secret',
  };

  // Verify admin secret
  const providedSecret = context.request.headers.get('X-Admin-Secret');
  if (!ADMIN_SECRET || !providedSecret || providedSecret !== ADMIN_SECRET) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json', ...corsHeaders },
    });
  }

  // Check required env vars
  if (!CLAUDE_KEY) {
    return new Response(JSON.stringify({ error: 'CLAUDE_API_KEY not configured' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders },
    });
  }
  if (!GITHUB_TOKEN) {
    return new Response(JSON.stringify({ error: 'GITHUB_TOKEN not configured' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders },
    });
  }

  try {
    // Parse request body for optional country override
    let targetCountry;
    try {
      const body = await context.request.json();
      if (body.countrySlug) {
        targetCountry = COUNTRIES.find(c => c.slug === body.countrySlug);
      }
    } catch (e) {
      // No body or invalid JSON — use rotation
    }

    if (!targetCountry) {
      targetCountry = getCountryForWeek();
    }

    // Generate blog
    const result = await generateBlog(CLAUDE_KEY, targetCountry);

    // Commit to GitHub
    const commit = await commitToGitHub(GITHUB_TOKEN, targetCountry, result.slug, result.markdown);

    return new Response(JSON.stringify({
      success: true,
      country: targetCountry.name,
      slug: result.slug,
      title: result.title,
      category: result.category,
      wordCount: result.wordCount,
      commitUrl: commit.commit?.html_url || '',
      pageUrl: `https://urmortgage.online/${targetCountry.slug}/blog/${result.slug}/`,
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', ...corsHeaders },
    });

  } catch (err) {
    console.error('Blog generation error:', err);
    return new Response(JSON.stringify({
      error: 'Generation failed',
      details: err.message,
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders },
    });
  }
}

export async function onRequestGet(context) {
  const ADMIN_SECRET = context.env.ADMIN_SECRET;
  const providedSecret = new URL(context.request.url).searchParams.get('secret');

  if (!ADMIN_SECRET || !providedSecret || providedSecret !== ADMIN_SECRET) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const schedule = getNextCountries(10);
  const current = getCountryForWeek();

  return new Response(JSON.stringify({
    currentWeekCountry: current,
    schedule: schedule.map(s => ({ week: s.week, country: s.country.name, slug: s.country.slug })),
  }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': 'https://urmortgage.online',
      'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, X-Admin-Secret',
    },
  });
}
