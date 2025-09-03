type Method = 'GET' | 'POST' | 'PATCH' | 'DELETE';

const API_BASE = (process.env.REACT_APP_API_BASE || '').replace(/\/$/, '');
const API_TOKEN = process.env.REACT_APP_API_TOKEN || '';

async function request<T>(method: Method, path: string, body?: any): Promise<T> {
  const url = `${API_BASE}${path}`;
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  };
  if (API_TOKEN) headers['Authorization'] = `Bearer ${API_TOKEN}`;

  const res = await fetch(url, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    let msg = `Request failed: ${res.status}`;
    try {
      const err = await res.json();
      if (err?.detail) {
        const d = typeof err.detail === 'string' ? { message: err.detail } : err.detail;
        msg = d.message || msg;
        if (d.code) msg += ` (code: ${d.code})`;
      }
    } catch (_) {
      // ignore
    }
    throw new Error(msg);
  }
  return (await res.json()) as T;
}

export interface Address { line1: string; locality?: string | null; city: string; state: string; pincode: string; }
export type PropertyStatus = 'Operational' | 'Non Operational';
export interface Property {
  id: string;
  property_name: string;
  address: Address;
  status: PropertyStatus;
  photo_thumb_url?: string;
  unit_types?: string[] | null;
  created_at: string;
}

export interface Unit {
  id: string;
  property_id: string;
  unit_number: string;
  status: 'Operational' | 'Non Operational';
  created_at: string;
}

export const api = {
  // Properties
  listProperties: () => request<Property[]>('GET', '/v1/properties'),
  createProperty: (p: { property_name: string; address: Address; status?: PropertyStatus; unit_types?: string[] }) =>
    request<Property>('POST', '/v1/properties', p),
  patchProperty: (id: string, patch: Partial<{ property_name: string; address: Address; status: PropertyStatus }>) =>
    request<Property>('PATCH', `/v1/properties/${id}`, patch),
  deleteProperty: (id: string) => request<{ ok: boolean }>('DELETE', `/v1/properties/${id}`),

  // Units (scoped)
  listUnits: (propertyId: string) => request<Unit[]>('GET', `/v1/properties/${propertyId}/units`),
  createUnit: (propertyId: string, u: { unit_number: string; status?: 'Operational' | 'Non Operational' }) =>
    request<Unit>('POST', `/v1/properties/${propertyId}/units`, u),
  patchUnit: (propertyId: string, unitId: string, patch: Partial<{ status: 'Operational' | 'Non Operational' }>) =>
    request<Unit>('PATCH', `/v1/properties/${propertyId}/units/${unitId}`, patch),
  deleteUnit: (propertyId: string, unitId: string) => request<{ ok: boolean }>('DELETE', `/v1/properties/${propertyId}/units/${unitId}`),
  uploadPropertyPhoto: async (propertyId: string, file: File) => {
    const url = `${API_BASE}/v1/properties/${propertyId}/photo`;
    const fd = new FormData();
    fd.append('file', file);
    const headers: Record<string, string> = {};
    if (API_TOKEN) headers['Authorization'] = `Bearer ${API_TOKEN}`;
    const res = await fetch(url, { method: 'POST', body: fd, headers });
    if (!res.ok) {
      let msg = 'Photo upload failed';
      try { const e = await res.json(); msg = e?.detail?.message || msg; } catch {}
      throw new Error(msg);
    }
    return res.json() as Promise<{ photo_thumb_url: string }>;
  },
};
