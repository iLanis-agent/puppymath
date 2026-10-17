# Puppy Math

Puppy feeding arithmetic honesty. The food bag does the prescribing; this page only does the dividing. Puppy Math splits the label's daily amount into meals, turns a counted bag into days, and prices the habit per day and per month.

## What it computes

- **The potty heuristic** - a rough heuristic some trainers repeat (age in months plus one hours, capped at 8), labeled as a cited ceiling, never a schedule. Your puppy's signals and your vet set the real one.
- **The meal split** - the daily amount from your food bag or vet, divided across the meals you chose.
- **The bag truth** - cups the bag measures against the daily amount: how many days a bag covers.
- **The cost truth** - bag price down to cost per day and per month.

## Boundary

Illustrative arithmetic only. The potty line is a rough heuristic people repeat; the feeding panels only divide the numbers on your food bag or from your vet. Your puppy, your label and your vet win every tie. Puppy Math never gives a care or health verdict.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (18 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/puppymath/
Repo: https://github.com/iLanis-agent/puppymath
