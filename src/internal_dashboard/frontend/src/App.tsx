import React, { useEffect, useMemo, useState } from 'react';
import { api, Property, PropertyStatus, Unit } from './lib/api';

function useAsync<T>(fn: () => Promise<T>, deps: any[]) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    let mounted = true;
    setLoading(true);
    setError(null);
    fn()
      .then((d) => mounted && setData(d))
      .catch((e) => mounted && setError(e?.message || 'Error'))
      .finally(() => mounted && setLoading(false));
    return () => {
      mounted = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
  return { data, loading, error, reload: () => fn().then(setData).catch((e) => setError(e?.message || 'Error')) };
}

function StatusBadge({ status }: { status: PropertyStatus }) {
  const color = status === 'Operational' ? '#16a34a' : '#a1a1aa';
  return <span style={{ padding: '2px 8px', borderRadius: 12, background: color, color: 'white', fontSize: 12 }}>{status}</span>;
}

function DeleteConfirm({ label, onConfirm }: { label: string; onConfirm: () => void }) {
  const [open, setOpen] = useState(false);
  const [text, setText] = useState('');
  return (
    <span style={{ display: 'inline-block' }}>
      {!open ? (
        <button data-testid={`open-delete-${label}`} onClick={() => setOpen(true)} style={{ color: '#dc2626' }}>Delete</button>
      ) : (
        <span>
          <input
            data-testid={`confirm-input-${label}`}
            placeholder="type delete"
            value={text}
            onChange={(e) => setText(e.target.value)}
            style={{ marginRight: 8 }}
          />
          <button
            data-testid={`confirm-delete-${label}`}
            onClick={() => { if (text.toLowerCase() === 'delete') { onConfirm(); setOpen(false); setText(''); } }}
            disabled={text.toLowerCase() !== 'delete'}
            style={{ color: 'white', background: '#dc2626', padding: '4px 10px', borderRadius: 6 }}
          >Confirm</button>
          <button onClick={() => { setOpen(false); setText(''); }} style={{ marginLeft: 6 }}>Cancel</button>
        </span>
      )}
    </span>
  );
}

function UnitsManager({ property }: { property: Property }) {
  const [units, setUnits] = useState<Unit[]>([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [form, setForm] = useState({ unit_number: '' });

  const refresh = async () => {
    setLoading(true);
    setErr(null);
    try {
      const data = await api.listUnits(property.id);
      setUnits(data);
    } catch (e: any) {
      setErr(e?.message || 'Error');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { refresh(); }, [property.id]);

  const locked = property.status !== 'Operational';

  return (
    <div style={{ borderTop: '1px solid #e5e7eb', marginTop: 10, paddingTop: 10 }}>
      <h4>Units</h4>
      {err && <div style={{ color: '#dc2626' }}>{err}</div>}
      <div style={{ display: 'flex', gap: 8, marginBottom: 8 }}>
        <input
          placeholder="Unit Number"
          value={form.unit_number}
          onChange={(e) => setForm({ ...form, unit_number: e.target.value })}
          disabled={locked}
        />
        <button
          data-testid={`add-unit-${property.id}`}
          onClick={async () => {
            if (!form.unit_number) return;
            await api.createUnit(property.id, { unit_number: form.unit_number });
            setForm({ unit_number: '' });
            refresh();
          }}
          disabled={locked}
        >Add Unit</button>
      </div>

      {loading ? (
        <div>Loading units…</div>
      ) : (
        <table width="100%" cellPadding={6} style={{ borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ background: '#f3f4f6' }}>
              <th align="left">Unit</th>
              
              <th align="left">Status</th>
              <th align="left">Actions</th>
            </tr>
          </thead>
          <tbody>
            {units.map((u) => (
              <tr key={u.id} style={{ borderTop: '1px solid #e5e7eb' }}>
                <td>{u.unit_number}</td>
                <td><StatusBadge status={u.status as PropertyStatus} /></td>
                <td>
                  <button
                    data-testid={`toggle-unit-${u.id}`}
                    onClick={async () => {
                      const next = u.status === 'Operational' ? 'Non Operational' : 'Operational';
                      await api.patchUnit(property.id, u.id, { status: next });
                      refresh();
                    }}
                    disabled={locked}
                  >{u.status === 'Operational' ? 'Set Non‑Operational' : 'Set Operational'}</button>
                  &nbsp;
                  <DeleteConfirm
                    label={`unit-${u.id}`}
                    onConfirm={async () => { await api.deleteUnit(property.id, u.id); refresh(); }}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default function App() {
  const { data, loading, error, reload } = useAsync<Property[]>(api.listProperties, []);
  const [form, setForm] = useState({
    property_name: '',
    pincode: '',
    state: '',
    city: '',
    locality: '',
    line1: '',
  });
  const [localities, setLocalities] = useState<string[]>([]);
  const [pinErr, setPinErr] = useState<string | null>(null);
  const [expanded, setExpanded] = useState<string | null>(null);
  const propsData = useMemo(() => data || [], [data]);

  return (
    <div style={{ maxWidth: 960, margin: '0 auto', padding: 16 }}>
      <h2>Properties</h2>
      {error && <div style={{ color: '#dc2626', marginBottom: 8 }}>{error}</div>}

      <div style={{ border: '1px solid #e5e7eb', borderRadius: 8, padding: 12, marginBottom: 16 }}>
        <h3>Add Property</h3>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
          <input placeholder="Property Name" value={form.property_name} onChange={(e) => setForm({ ...form, property_name: e.target.value })} />
          <div>
            <div style={{ display: 'flex', gap: 8 }}>
              <input placeholder="Pincode" value={form.pincode} onChange={(e) => setForm({ ...form, pincode: e.target.value })} maxLength={6} />
              <button onClick={async () => {
                setPinErr(null);
                setLocalities([]);
                const pin = form.pincode.trim();
                if (!/^\d{6}$/.test(pin)) { setPinErr('Enter a valid 6-digit PIN code'); return; }
                try {
                  const res = await fetch(`https://api.postalpincode.in/pincode/${pin}`);
                  const json = await res.json();
                  const first = json?.[0];
                  if (first?.Status !== 'Success') { setPinErr('PIN lookup failed'); return; }
                  const offices = (first?.PostOffice || []) as any[];
                  const cities = new Set(offices.map((o) => o.District).filter(Boolean));
                  const states = new Set(offices.map((o) => o.State).filter(Boolean));
                  const locs = Array.from(new Set(offices.map((o) => o.Name).filter(Boolean)));
                  setForm((f) => ({ ...f, city: Array.from(cities)[0] || f.city, state: Array.from(states)[0] || f.state }));
                  setLocalities(locs as string[]);
                } catch (e) {
                  setPinErr('PIN lookup failed');
                }
              }}>Autofill</button>
            </div>
            {pinErr && <div style={{ color: '#dc2626', fontSize: 12 }}>{pinErr}</div>}
          </div>
          <input placeholder="State" value={form.state} onChange={(e) => setForm({ ...form, state: e.target.value })} />
          <input placeholder="City" value={form.city} onChange={(e) => setForm({ ...form, city: e.target.value })} />
          {localities.length > 0 ? (
            <select value={form.locality} onChange={(e) => setForm({ ...form, locality: e.target.value })}>
              <option value="">Select Locality</option>
              {localities.map((l) => <option key={l} value={l}>{l}</option>)}
            </select>
          ) : (
            <input placeholder="Locality (optional)" value={form.locality} onChange={(e) => setForm({ ...form, locality: e.target.value })} />
          )}
          <input placeholder="Address Line 1" value={form.line1} onChange={(e) => setForm({ ...form, line1: e.target.value })} />
        </div>
        <div style={{ marginTop: 8 }}>
          <button
            data-testid="add-property"
            onClick={async () => {
              if (!form.property_name || !form.line1 || !form.city || !form.state || !/^\d{6}$/.test(form.pincode)) return;
              await api.createProperty({
                property_name: form.property_name,
                address: { line1: form.line1, locality: form.locality || undefined, city: form.city, state: form.state, pincode: form.pincode },
              });
              setForm({ property_name: '', pincode: '', state: '', city: '', locality: '', line1: '' });
              setLocalities([]);
              reload();
            }}
          >Add</button>
        </div>
      </div>

      {loading ? (
        <div>Loading…</div>
      ) : (
        <table width="100%" cellPadding={8} style={{ borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ background: '#f3f4f6' }}>
              <th align="left">Property</th>
              <th align="left">Address</th>
              <th align="left">Status</th>
              <th align="left">Actions</th>
            </tr>
          </thead>
          <tbody>
            {propsData.map((p) => (
              <React.Fragment key={p.id}>
                <tr style={{ borderTop: '1px solid #e5e7eb' }} data-testid={`property-row-${p.id}`}>
                  <td>{p.property_name}</td>
                  <td>{p.address?.line1}, {p.address?.city}</td>
                  <td><StatusBadge status={p.status} /></td>
                  <td>
                    <button
                      data-testid={`toggle-status-${p.id}`}
                      onClick={async () => {
                        const next = p.status === 'Operational' ? 'Non Operational' : 'Operational';
                        await api.patchProperty(p.id, { status: next });
                        reload();
                      }}
                    >{p.status === 'Operational' ? 'Set Non‑Operational' : 'Set Operational'}</button>
                    &nbsp;
                    <button onClick={() => setExpanded(expanded === p.id ? null : p.id)}>
                      {expanded === p.id ? 'Hide Units' : 'Show Units'}
                    </button>
                    &nbsp;
                    <DeleteConfirm label={`property-${p.id}`} onConfirm={async () => { await api.deleteProperty(p.id); if (expanded === p.id) setExpanded(null); reload(); }} />
                  </td>
                </tr>
                {expanded === p.id && (
                  <tr>
                    <td colSpan={4}>
                      <UnitsManager property={p} />
                    </td>
                  </tr>
                )}
              </React.Fragment>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
