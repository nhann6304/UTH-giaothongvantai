import type { ModuleConfig } from '../types';

export interface AppliedFilter {
  field: string;
  values?: any[];
  dateFrom?: string;
  dateTo?: string;
}

export interface VerifyResult {
  total: number;
  matched: number;
  mismatched: number;
  mismatchedSamples: Array<{ id: any; field: string; rowValue: any; filterValues: any }>;
}

/**
 * So từng row trả về với filter đã apply. Trả về số mismatched + sample.
 * Pattern row field mapping nằm trong module.verifyRules.rowFieldMapping.
 *   "position"  → "position"           (so trực tiếp)
 *   "roles"     → "roles[].id"         (kiểm intersection)
 *   "createdBy" → "createdBy.id"
 *   "createdAt" → "createdAt"          (so date range)
 */
export function verifyRows(
  rows: any[],
  filters: AppliedFilter[],
  module: ModuleConfig,
): VerifyResult {
  const mapping = module.verifyRules?.rowFieldMapping || {};
  const result: VerifyResult = {
    total: rows.length,
    matched: 0,
    mismatched: 0,
    mismatchedSamples: [],
  };

  for (const row of rows) {
    let rowOk = true;
    let firstBadField = '';
    let firstBadValue: any = null;
    let firstBadFilter: any = null;

    for (const f of filters) {
      const path = mapping[f.field] || f.field;
      const rowVal = readRowField(row, path);

      if (f.dateFrom || f.dateTo) {
        // Date range check
        const ts = rowVal ? new Date(rowVal).getTime() : NaN;
        if (Number.isNaN(ts)) {
          rowOk = false;
          firstBadField = f.field;
          firstBadValue = rowVal;
          firstBadFilter = { dateFrom: f.dateFrom, dateTo: f.dateTo };
          break;
        }
        if (f.dateFrom && ts < new Date(f.dateFrom).getTime()) {
          rowOk = false;
          firstBadField = f.field;
          firstBadValue = rowVal;
          firstBadFilter = { dateFrom: f.dateFrom, dateTo: f.dateTo };
          break;
        }
        if (f.dateTo && ts > new Date(f.dateTo).getTime() + 24 * 3600 * 1000 - 1) {
          rowOk = false;
          firstBadField = f.field;
          firstBadValue = rowVal;
          firstBadFilter = { dateFrom: f.dateFrom, dateTo: f.dateTo };
          break;
        }
        continue;
      }

      if (f.values && f.values.length) {
        // Multi-select check
        const rowArr = Array.isArray(rowVal) ? rowVal : [rowVal];
        const hasMatch = rowArr.some((v) =>
          f.values!.some((fv) => String(fv) === String(v)),
        );
        if (!hasMatch) {
          rowOk = false;
          firstBadField = f.field;
          firstBadValue = rowVal;
          firstBadFilter = f.values;
          break;
        }
      }
    }

    if (rowOk) {
      result.matched++;
    } else {
      result.mismatched++;
      if (result.mismatchedSamples.length < 5) {
        result.mismatchedSamples.push({
          id: row.id || row._id || row.uuid,
          field: firstBadField,
          rowValue: firstBadValue,
          filterValues: firstBadFilter,
        });
      }
    }
  }

  return result;
}

function readRowField(row: any, path: string): any {
  // hỗ trợ "a.b" và "a[].b" (lấy array b từ each item của array a)
  if (path.includes('[].')) {
    const [head, tail] = path.split('[].');
    const arr = head.split('.').reduce((acc, k) => (acc == null ? acc : acc[k]), row);
    if (!Array.isArray(arr)) return undefined;
    return arr.map((it) => tail.split('.').reduce((acc, k) => (acc == null ? acc : acc[k]), it));
  }
  return path.split('.').reduce((acc, k) => (acc == null ? acc : acc[k]), row);
}
