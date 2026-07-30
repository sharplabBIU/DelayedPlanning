"""
Fast drop-in replacement for the per-subject pandas DataFrame used by the ported
`f(samples, data, rng_samples)` likelihoods. The likelihoods access data only via a
small, fixed set of operations:

    np.sort(data['trial_num'].unique())
    df_temp = data[data['trial_num'] == trial].reset_index(drop=True)
    df_temp['col'].values            df_temp['col'].values[0]
    df_temp['col'][0:]  / [:]        (df_temp['col'] == 2).sum()
    len(data)

Pandas boolean-masking + frame construction 60x per evaluation dominates runtime
(~29 ms/eval). Precomputing the per-trial numpy columns once and serving them
through these same operations makes an evaluation ~1 ms, with identical results.
"""
import numpy as np


class _Col:
    """A single column of one trial (thin ndarray wrapper exposing `.values`)."""
    __slots__ = ('a',)

    def __init__(self, a):
        self.a = a

    @property
    def values(self):
        return self.a

    def __getitem__(self, k):
        return self.a[k]           # slice -> ndarray (supports ==, .sum()); int -> scalar

    def __eq__(self, v):
        return self.a == v

    def __len__(self):
        return len(self.a)


class _TrialFrame:
    __slots__ = ('cols',)

    def __init__(self, cols):
        self.cols = cols           # {name: ndarray}

    def reset_index(self, drop=True):
        return self

    def __getitem__(self, name):
        return _Col(self.cols[name])


class _TrialCol:
    """The full-data 'trial_num' column: `.unique()` and `== trial` -> selector."""
    __slots__ = ('vals',)

    def __init__(self, vals):
        self.vals = vals

    def unique(self):
        return np.unique(self.vals)

    @property
    def values(self):
        return self.vals

    def __eq__(self, trial):
        return _Sel(trial)


class _Sel:
    __slots__ = ('trial',)

    def __init__(self, trial):
        self.trial = trial


class FastData:
    """Drop-in for a per-subject DataFrame, backed by precomputed per-trial columns."""

    def __init__(self, df):
        self._n = len(df)
        cols = {c: df[c].to_numpy() for c in df.columns}
        self._trial_vals = cols['trial_num']
        trials = np.unique(self._trial_vals)
        # precompute per-trial column dict (ordered by decision as in the frame)
        self._by_trial = {}
        for t in trials:
            mask = self._trial_vals == t
            self._by_trial[t] = _TrialFrame({c: v[mask] for c, v in cols.items()})

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        if isinstance(key, _Sel):
            return self._by_trial[key.trial]
        if key == 'trial_num':
            return _TrialCol(self._trial_vals)
        # generic full-column access (rarely used); return ndarray-like
        raise KeyError(key)
