# DHLC Phase 1-2 Reproducibility Record

## Scope

This record summarizes the work completed for DHLC Phase 1 (Understand the
data) and Phase 2 (Dataset).

## Phase 1 Deliverables

- Added a one-day activity visualization for fictional participant `10001`.
- Added a five-line preprocessing summary covering the chronological activity
  grid, invalid-minute masking, Choi-style non-wear parameters, epoch
  aggregation, attention coverage, covariates, mortality, and splitting.
- Added three-patient synthetic NHANES fixtures in the real source schema:
  `participants.csv`, `covariates.csv`, `mortality.csv`, and `activity.csv`.
- Added `scripts/analyze/plot_fake_activity_day.py` to generate the participant
  activity plot reproducibly.

The fixtures contain no real participants. They use NHANES-style uppercase
columns such as `SEQN`, `PAXDAY`, `PAXHOUR`, `PAXINTEN`, `RIDAGEYR`, and
`mortstat`, while only the added synthetic values are stored in them.

## Phase 2 Deliverables

- Added `PyHealth/pyhealth/datasets/configs/nhanes.yaml`, defining tables for
  patients, covariates, mortality, and wearable activity.
- Added `PyHealth/pyhealth/datasets/nhanes.py` with an `NHANESDataset` class
  inheriting from `BaseDataset`.
- Exported `NHANESDataset` from
  `PyHealth/pyhealth/datasets/__init__.py`.
- Added wearable preprocessing that constructs a synthetic relative timestamp
  from `PAXDAY`, `PAXHOUR`, and `PAXMINUT`.
- Added source validation for missing files, unsupported formats, and missing
  required columns.
- Added Google-style method docstrings and type hints.
- Added focused tests for fake-data loading and missing-file/column errors.

## Reproduction

Generate the one-day plot:

```bash
uv run python scripts/analyze/plot_fake_activity_day.py
```

The generated image is written to
`tests/fixtures/dhlc_phase1/participant_10001_day1.png`.

Run the focused PyHealth dataset tests:

```bash
cd PyHealth
uv run pytest -q tests/test_nhanes_dataset.py
```

## Verification Result

The focused NHANES test suite passed all 3 tests. The fake fixture produced
3 unique patients, 24 activity events for participant `10001`, and one
demographics, covariate, and mortality event for that participant.
