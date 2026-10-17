// Puppy Math engine - the food bag does the prescribing, this page only does the dividing.
// The potty line is a rough heuristic people repeat, not a schedule.
// Your puppy, your label and your vet win every tie; the app never gives a care or health verdict.

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

function money(x) {
  return "$" + x.toFixed(2);
}

function article(n) {
  return (n === 8 || n === 11 || n === 18 || (n >= 80 && n <= 89)) ? "an" : "a";
}

function articleMoney(price) {
  const n = Math.floor(price);
  return (n === 8 || n === 11 || n === 18 || (n >= 80 && n <= 89)) ? "An" : "A";
}

function cupWord(x) {
  return x === 1 ? "cup" : "cups";
}

// The potty heuristic: age in months plus one hours, capped at 8.
// A rough heuristic some trainers repeat - a cited ceiling, never a schedule.
function pottyTruth(ageMonths) {
  assertPositive(ageMonths, "the age");
  const hours = Math.min(ageMonths + 1, 8);
  const hourWord = hours === 1 ? "hour" : "hours";
  return "A rough heuristic some trainers repeat says age in months plus one hours between " +
    "breaks, capped at 8 - for " + article(ageMonths) + " " + ageMonths + "-month-old that reads " +
    hours + " " + hourWord + ". It is a ceiling people cite, not a schedule; your puppy's signals " +
    "and your vet set the real one.";
}

// The meal split: the label's daily amount divided by the meals you chose.
function mealTruth(dailyCups, mealsPerDay) {
  assertPositive(dailyCups, "the daily amount");
  assertPositive(mealsPerDay, "the meals");
  const per = tenths(dailyCups / mealsPerDay);
  const mealWord = mealsPerDay === 1 ? "meal" : "meals";
  return "Your label's " + fixed1(dailyCups) + " " + cupWord(dailyCups) + " a day split across " +
    mealsPerDay + " " + mealWord + " is " + fixed1(per) + " " + cupWord(per) +
    " a meal - the label does the prescribing, this page only does the dividing.";
}

// The bag truth: cups you counted against the daily amount.
function bagTruth(dailyCups, bagCups) {
  assertPositive(dailyCups, "the daily amount");
  assertPositive(bagCups, "the bag");
  const days = tenths(bagCups / dailyCups);
  const dayWord = days === 1 ? "day" : "days";
  return "At " + fixed1(dailyCups) + " " + cupWord(dailyCups) + " a day, a bag that measures " +
    fixed1(bagCups) + " " + cupWord(bagCups) + " covers " + fixed1(days) + " " + dayWord +
    " - count the cups once and the bag stops surprising you.";
}

// The cost truth: bag price down to the day and the month.
function costTruth(bagPrice, bagCups, dailyCups) {
  assertPositive(bagPrice, "the bag price");
  assertPositive(bagCups, "the bag");
  assertPositive(dailyCups, "the daily amount");
  const perDay = (bagPrice / bagCups) * dailyCups;
  const per30 = perDay * 30;
  return articleMoney(bagPrice) + " " + money(bagPrice) + " bag at " + fixed1(dailyCups) + " " +
    cupWord(dailyCups) + " a day runs " + money(perDay) + " a day, about " + money(per30) +
    " a month - the bag size on the shelf is the marketing, this is the number.";
}

if (typeof module !== "undefined") {
  module.exports = { pottyTruth, mealTruth, bagTruth, costTruth, tenths, fixed1 };
}
