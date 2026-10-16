// Puppy Math engine - potty breaks, meals and kibble honesty.
// Every norm is a labeled care norm; the app never gives a health verdict.

function assertPositive(value, label) {
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(label + " must be above zero");
  }
}

function tenths(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function fixed1(x) {
  return tenths(x).toFixed(1);
}

function article(n) {
  const s = String(Math.abs(Math.trunc(n)));
  return (/^([8]|11|18)/.test(s)) ? "An" : "A";
}

// Labeled care norm: a puppy holds it about age in months plus one hours, capped at 8.
function pottyTruth(ageMonths) {
  assertPositive(ageMonths, "the age");
  const hours = Math.min(ageMonths + 1, 8);
  return article(ageMonths) + " " + ageMonths + "-month-old puppy asks a break about every " +
    hours + " hours honestly.";
}

// Labeled care norm: under 3 months four meals a day, 3 to 5 months three, 6 months and up two.
function mealsTruth(ageMonths) {
  assertPositive(ageMonths, "the age");
  let meals;
  if (ageMonths < 3) {
    meals = 4;
  } else if (ageMonths < 6) {
    meals = 3;
  } else {
    meals = 2;
  }
  return article(ageMonths) + " " + ageMonths + "-month-old puppy eats " + meals + " meals a day honestly.";
}

// Labeled care norm: about 1 cup of kibble a day per 10 pounds of expected adult weight.
function foodTruth(adultLb, meals) {
  assertPositive(adultLb, "the adult weight");
  assertPositive(meals, "the meal count");
  const total = tenths(adultLb / 10);
  const perMeal = tenths(total / meals);
  const mealWord = meals === 1 ? "meal" : "meals";
  return "A puppy growing toward about " + fixed1(adultLb) + " pounds asks " + fixed1(total) +
    " cups a day, " + fixed1(perMeal) + " cups a meal across " + meals + " " + mealWord + " honestly.";
}

if (typeof module !== "undefined") {
  module.exports = { pottyTruth, mealsTruth, foodTruth, tenths, fixed1 };
}
