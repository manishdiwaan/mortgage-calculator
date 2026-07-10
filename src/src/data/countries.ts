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

export const ALL_COUNTRIES: CountryMeta[] = [
  // Pilot countries
  { name: 'Australia', code: 'australia', iso: 'AU', currency: 'AUD', currencySymbol: '$', flag: '🇦🇺', language: 'en', region: 'Asia-Pacific', centralBank: 'Reserve Bank of Australia', slug: 'australia' },
  { name: 'India', code: 'india', iso: 'IN', currency: 'INR', currencySymbol: '₹', flag: '🇮🇳', language: 'en', region: 'Asia-Pacific', centralBank: 'Reserve Bank of India', slug: 'india' },
  { name: 'United States', code: 'united-states', iso: 'US', currency: 'USD', currencySymbol: '$', flag: '🇺🇸', language: 'en', region: 'North America', centralBank: 'Federal Reserve', slug: 'united-states' },
  { name: 'United Kingdom', code: 'united-kingdom', iso: 'GB', currency: 'GBP', currencySymbol: '£', flag: '🇬🇧', language: 'en', region: 'Europe', centralBank: 'Bank of England', slug: 'united-kingdom' },
  { name: 'UAE', code: 'uae', iso: 'AE', currency: 'AED', currencySymbol: 'د.إ', flag: '🇦🇪', language: 'en', region: 'Middle East', centralBank: 'Central Bank of the UAE', slug: 'uae' },
  { name: 'Singapore', code: 'singapore', iso: 'SG', currency: 'SGD', currencySymbol: '$', flag: '🇸🇬', language: 'en', region: 'Asia-Pacific', centralBank: 'Monetary Authority of Singapore', slug: 'singapore' },
  // Remaining 17
  { name: 'Canada', code: 'canada', iso: 'CA', currency: 'CAD', currencySymbol: '$', flag: '🇨🇦', language: 'en', region: 'North America', centralBank: 'Bank of Canada', slug: 'canada' },
  { name: 'New Zealand', code: 'new-zealand', iso: 'NZ', currency: 'NZD', currencySymbol: '$', flag: '🇳🇿', language: 'en', region: 'Asia-Pacific', centralBank: 'Reserve Bank of New Zealand', slug: 'new-zealand' },
  { name: 'Germany', code: 'germany', iso: 'DE', currency: 'EUR', currencySymbol: '€', flag: '🇩🇪', language: 'en', region: 'Europe', centralBank: 'European Central Bank', slug: 'germany' },
  { name: 'France', code: 'france', iso: 'FR', currency: 'EUR', currencySymbol: '€', flag: '🇫🇷', language: 'en', region: 'Europe', centralBank: 'European Central Bank', slug: 'france' },
  { name: 'Spain', code: 'spain', iso: 'ES', currency: 'EUR', currencySymbol: '€', flag: '🇪🇸', language: 'en', region: 'Europe', centralBank: 'European Central Bank', slug: 'spain' },
  { name: 'Italy', code: 'italy', iso: 'IT', currency: 'EUR', currencySymbol: '€', flag: '🇮🇹', language: 'en', region: 'Europe', centralBank: 'European Central Bank', slug: 'italy' },
  { name: 'Netherlands', code: 'netherlands', iso: 'NL', currency: 'EUR', currencySymbol: '€', flag: '🇳🇱', language: 'en', region: 'Europe', centralBank: 'European Central Bank', slug: 'netherlands' },
  { name: 'Ireland', code: 'ireland', iso: 'IE', currency: 'EUR', currencySymbol: '€', flag: '🇮🇪', language: 'en', region: 'Europe', centralBank: 'European Central Bank', slug: 'ireland' },
  { name: 'Japan', code: 'japan', iso: 'JP', currency: 'JPY', currencySymbol: '¥', flag: '🇯🇵', language: 'en', region: 'Asia-Pacific', centralBank: 'Bank of Japan', slug: 'japan' },
  { name: 'South Korea', code: 'south-korea', iso: 'KR', currency: 'KRW', currencySymbol: '₩', flag: '🇰🇷', language: 'en', region: 'Asia-Pacific', centralBank: 'Bank of Korea', slug: 'south-korea' },
  { name: 'Hong Kong', code: 'hong-kong', iso: 'HK', currency: 'HKD', currencySymbol: '$', flag: '🇭🇰', language: 'en', region: 'Asia-Pacific', centralBank: 'Hong Kong Monetary Authority', slug: 'hong-kong' },
  { name: 'Malaysia', code: 'malaysia', iso: 'MY', currency: 'MYR', currencySymbol: 'RM', flag: '🇲🇾', language: 'en', region: 'Asia-Pacific', centralBank: 'Bank Negara Malaysia', slug: 'malaysia' },
  { name: 'Thailand', code: 'thailand', iso: 'TH', currency: 'THB', currencySymbol: '฿', flag: '🇹🇭', language: 'en', region: 'Asia-Pacific', centralBank: 'Bank of Thailand', slug: 'thailand' },
  { name: 'South Africa', code: 'south-africa', iso: 'ZA', currency: 'ZAR', currencySymbol: 'R', flag: '🇿🇦', language: 'en', region: 'Africa', centralBank: 'South African Reserve Bank', slug: 'south-africa' },
  { name: 'Brazil', code: 'brazil', iso: 'BR', currency: 'BRL', currencySymbol: 'R$', flag: '🇧🇷', language: 'en', region: 'South America', centralBank: 'Central Bank of Brazil', slug: 'brazil' },
  { name: 'Mexico', code: 'mexico', iso: 'MX', currency: 'MXN', currencySymbol: '$', flag: '🇲🇽', language: 'en', region: 'North America', centralBank: 'Bank of Mexico', slug: 'mexico' },
  { name: 'Saudi Arabia', code: 'saudi-arabia', iso: 'SA', currency: 'SAR', currencySymbol: 'ر.س', flag: '🇸🇦', language: 'en', region: 'Middle East', centralBank: 'Saudi Central Bank', slug: 'saudi-arabia' },
];

// Keep backward compatibility
export const PILOT_COUNTRIES = ALL_COUNTRIES;

export function getCountryByCode(code: string): CountryMeta | undefined {
  return ALL_COUNTRIES.find((c) => c.code === code);
}

export function getAllCountryCodes(): string[] {
  return ALL_COUNTRIES.map((c) => c.code);
}
