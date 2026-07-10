export interface CountryMeta {
  name: string;
  code: string;
  iso: string;
  currency: string;
  currencySymbol: string;
  flag: string;
  language: string;
  region: string;
  centralBank: string;
  slug: string;
}

export const PILOT_COUNTRIES: CountryMeta[] = [
  {
    name: 'Australia',
    code: 'australia',
    iso: 'AU',
    currency: 'AUD',
    currencySymbol: '$',
    flag: '🇦🇺',
    language: 'en',
    region: 'Asia-Pacific',
    centralBank: 'Reserve Bank of Australia',
    slug: 'australia',
  },
  {
    name: 'India',
    code: 'india',
    iso: 'IN',
    currency: 'INR',
    currencySymbol: '₹',
    flag: '🇮🇳',
    language: 'en',
    region: 'Asia-Pacific',
    centralBank: 'Reserve Bank of India',
    slug: 'india',
  },
  {
    name: 'United States',
    code: 'united-states',
    iso: 'US',
    currency: 'USD',
    currencySymbol: '$',
    flag: '🇺🇸',
    language: 'en',
    region: 'North America',
    centralBank: 'Federal Reserve',
    slug: 'united-states',
  },
  {
    name: 'United Kingdom',
    code: 'united-kingdom',
    iso: 'GB',
    currency: 'GBP',
    currencySymbol: '£',
    flag: '🇬🇧',
    language: 'en',
    region: 'Europe',
    centralBank: 'Bank of England',
    slug: 'united-kingdom',
  },
  {
    name: 'UAE',
    code: 'uae',
    iso: 'AE',
    currency: 'AED',
    currencySymbol: 'د.إ',
    flag: '🇦🇪',
    language: 'en',
    region: 'Middle East',
    centralBank: 'Central Bank of the UAE',
    slug: 'uae',
  },
  {
    name: 'Singapore',
    code: 'singapore',
    iso: 'SG',
    currency: 'SGD',
    currencySymbol: '$',
    flag: '🇸🇬',
    language: 'en',
    region: 'Asia-Pacific',
    centralBank: 'Monetary Authority of Singapore',
    slug: 'singapore',
  },
];

export function getCountryByCode(code: string): CountryMeta | undefined {
  return PILOT_COUNTRIES.find((c) => c.code === code);
}

export function getAllCountryCodes(): string[] {
  return PILOT_COUNTRIES.map((c) => c.code);
}
