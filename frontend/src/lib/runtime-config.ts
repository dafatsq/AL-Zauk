const LOCAL_API_FALLBACK = 'http://localhost:8082/api/v1';
const PRODUCTION_API_FALLBACK = 'https://alzauk.165-245-184-75.nip.io/api/v1';

function normalizeApiBaseUrl(input: string): string {
  let url = input.trim();

  if (!url) {
    return LOCAL_API_FALLBACK;
  }

  if (url.includes('165.245.184.75:8082')) {
    url = url.replace('165.245.184.75:8082', 'alzauk.165-245-184-75.nip.io');
  }

  if (typeof window !== 'undefined' && window.location.protocol === 'https:' && url.startsWith('http://')) {
    url = `https://${url.slice('http://'.length)}`;
  }

  return url.replace(/\/+$/, '');
}

export function getApiBaseUrl(): string {
  const rawUrl = process.env.NEXT_PUBLIC_API_URL || (process.env.NODE_ENV === 'production' ? PRODUCTION_API_FALLBACK : LOCAL_API_FALLBACK);
  return normalizeApiBaseUrl(rawUrl);
}

export function getBackendBaseUrl(): string {
  return getApiBaseUrl().replace(/\/api\/v1\/?$/, '');
}
