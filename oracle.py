import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def article(n):
    s = str(abs(int(n)))
    return "An" if s.startswith("8") or s.startswith("11") or s.startswith("18") else "A"

def potty_truth(age):
    if age <= 0:
        raise ValueError("the age must be above zero")
    hours = min(age + 1, 8)
    return f"{article(age)} {age}-month-old puppy asks a break about every {hours} hours honestly."

def meals_truth(age):
    if age <= 0:
        raise ValueError("the age must be above zero")
    if age < 3:
        meals = 4
    elif age < 6:
        meals = 3
    else:
        meals = 2
    return f"{article(age)} {age}-month-old puppy eats {meals} meals a day honestly."

def food_truth(lb, meals):
    if lb <= 0:
        raise ValueError("the adult weight must be above zero")
    if meals <= 0:
        raise ValueError("the meal count must be above zero")
    total = tenths(lb / 10)
    per_meal = tenths(total / meals)
    meal_word = "meal" if meals == 1 else "meals"
    return (f"A puppy growing toward about {fixed1(lb)} pounds asks {fixed1(total)} cups a day, "
            f"{fixed1(per_meal)} cups a meal across {meals} {meal_word} honestly.")

cases = []

def add(fn_name, args):
    try:
        fn = {"pottyTruth": potty_truth, "mealsTruth": meals_truth, "foodTruth": food_truth}[fn_name]
        cases.append({"fn": fn_name, "args": args, "result": fn(*args)})
    except ValueError as e:
        cases.append({"fn": fn_name, "args": args, "error": str(e)})

# pottyTruth
add("pottyTruth", [1])      # 2 hours
add("pottyTruth", [3])      # 4 hours
add("pottyTruth", [6])      # 7 hours
add("pottyTruth", [8])      # An 8-month-old, capped at 8
add("pottyTruth", [11])     # An 11-month-old, capped at 8
add("pottyTruth", [0])      # error
# mealsTruth
add("mealsTruth", [2])      # 4 meals
add("mealsTruth", [3])      # 3 meals, edge
add("mealsTruth", [5])      # 3 meals
add("mealsTruth", [6])      # 2 meals, edge
add("mealsTruth", [8])      # An 8-month-old, 2 meals
add("mealsTruth", [0])      # error
# foodTruth
add("foodTruth", [40, 3])   # 4.0 a day, 1.3 a meal
add("foodTruth", [10, 4])   # 1.0 a day, 0.3 a meal
add("foodTruth", [80, 2])   # 8.0 a day, 4.0 a meal
add("foodTruth", [5, 3])    # 0.5 a day, 0.2 a meal
add("foodTruth", [25, 1])   # 2.5 a day, 2.5 across 1 meal (singular)
add("foodTruth", [0, 3])    # error
add("foodTruth", [40, 0])   # error

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
    f.write("\n")
print(f"{len(cases)} cases written")
for c in cases:
    print(c["fn"], c["args"], "->", c["result"] if "result" in c else "ERR: " + c["error"])
