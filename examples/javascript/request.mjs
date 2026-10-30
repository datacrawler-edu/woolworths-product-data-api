import { readFile } from 'node:fs/promises';
import { setTimeout as sleep } from 'node:timers/promises';

const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error('Set APIFY_API_TOKEN locally.');
async function api(path, method = 'GET', body) {
  const response = await fetch(`https://api.apify.com/v2${path}`, {
    method, headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
    signal: AbortSignal.timeout(45000),
  });
  if (!response.ok) throw new Error(`Apify HTTP ${response.status}; inspect Console before retrying.`);
  return response.json();
}
const input = JSON.parse(await readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'));
let { data: run } = await api('/acts/datascraperes~woolworths-products-scraper/runs?timeout=240&maxTotalChargeUsd=0.01', 'POST', input);
console.error('Run ID:', run.id);
const deadline = Date.now() + 300000;
while (['READY', 'RUNNING', 'TIMING-OUT', 'ABORTING'].includes(run.status)) {
  if (Date.now() >= deadline) {
    await api(`/actor-runs/${encodeURIComponent(run.id)}/abort`, 'POST', {});
    throw new Error(`Deadline reached; abort requested for ${run.id}`);
  }
  await sleep(2000);
  ({ data: run } = await api(`/actor-runs/${encodeURIComponent(run.id)}`));
}
if (run.status !== 'SUCCEEDED') throw new Error(`Run ${run.id} ended ${run.status}`);
const summary = await api(`/key-value-stores/${encodeURIComponent(run.defaultKeyValueStoreId)}/records/SUMMARY`);
if (summary.status !== 'Completed') console.error('Collection needs attention:', summary);
for (let offset = 0; ; ) {
  const page = await api(`/datasets/${encodeURIComponent(run.defaultDatasetId)}/items?format=json&clean=true&offset=${offset}&limit=1000`);
  if (!page.length) break;
  for (const item of page) console.log(JSON.stringify(item));
  offset += page.length;
}
