# Puppy Math

Puppy schedule honesty. The breeder said every few hours, and the bladder keeps a stricter calendar than that. Puppy Math does the potty-break, meal-count and kibble arithmetic a new puppy runs on, with every norm labeled.

## What it computes

- **The potty truth** - age in months plus one hours between breaks, capped at 8 (a labeled care norm).
- **The meal truth** - under 3 months four meals a day, 3 to 5 months three, 6 months and up two (a labeled care norm).
- **The kibble truth** - about a cup a day per 10 pounds of expected adult weight (a labeled care norm), split per meal.

## Boundary

Illustrative arithmetic only. Every norm is a labeled care norm; your vet and the feeding chart on your own food bag win every tie. Puppy Math never gives a health verdict.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (19 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/puppymath/
Repo: https://github.com/iLanis-agent/puppymath
