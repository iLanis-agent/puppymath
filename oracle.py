import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def money(x):
    return f"${x:.2f}"

def article(n):
    return "an" if (n == 8 or n == 11 or n == 18 or 80 <= n <= 89) else "a"

def article_money(p):
    return "An" if (math.floor(p) in (8, 11, 18) or 80 <= math.floor(p) <= 89) else "A"

def cup_word(x):
    return "cup" if x == 1 else "cups"

def potty_truth(age):
    hours = min(age + 1, 8)
    word = "hour" if hours == 1 else "hours"
    return (f"A rough heuristic some trainers repeat says age in months plus one hours between "
            f"breaks, capped at 8 - for {article(age)} {age}-month-old that reads {hours} {word}. "
            f"It is a ceiling people cite, not a schedule; your puppy's signals and your vet set "
            f"the real one.")

def meal_truth(daily, meals):
    per = tenths(daily / meals)
    word = "meal" if meals == 1 else "meals"
    return (f"Your label's {fixed1(daily)} {cup_word(daily)} a day split across {meals} {word} "
            f"is {fixed1(per)} {cup_word(per)} a meal - the label does the prescribing, this page "
            f"only does the dividing.")

def bag_truth(daily, bag):
    days = tenths(bag / daily)
    word = "day" if days == 1 else "days"
    return (f"At {fixed1(daily)} {cup_word(daily)} a day, a bag that measures {fixed1(bag)} "
            f"{cup_word(bag)} covers {fixed1(days)} {word} - count the cups once and the bag "
            f"stops surprising you.")

def cost_truth(price, bag, daily):
    per_day = price / bag * daily
    per30 = per_day * 30
    return (f"{article_money(price)} {money(price)} bag at {fixed1(daily)} {cup_word(daily)} "
            f"a day runs {money(per_day)} a day, about {money(per30)} a month - the bag size on "
            f"the shelf is the marketing, this is the number.")

cases = []
for a in [3, 8, 1, 11, 6]:
    cases.append({"fn": "pottyTruth", "args": [a], "expected": potty_truth(a)})
for d, m in [(3, 3), (4, 2), (2.5, 2), (1, 1), (2, 4)]:
    cases.append({"fn": "mealTruth", "args": [d, m], "expected": meal_truth(d, m)})
for d, b in [(3, 100), (2.5, 80), (4, 60), (1, 30)]:
    cases.append({"fn": "bagTruth", "args": [d, b], "expected": bag_truth(d, b)})
for p, b, d in [(58, 100, 3), (8, 40, 2), (72, 150, 4), (45, 80, 2.5)]:
    cases.append({"fn": "costTruth", "args": [p, b, d], "expected": cost_truth(p, b, d)})

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
    f.write("\n")
print(len(cases), "cases written")
