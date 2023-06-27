from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Please see the docs at /docs"}

@app.get("/roll/{dice}")
async def roll(dice: str):
    try:

        results = {}
        results['rolls'] = []
        results['modifier'] = 0
        results['total'] = 0
        dice = dice.lower()

        # split off a + or - modifier if it exists

        if "+" in dice:
            dice, modifier = dice.split("+")
            results['modifier'] = int(modifier)
        elif "-" in dice:
            dice, modifier = dice.split("-")
            results['modifier'] = -int(modifier)

        # split off the number of dice and the number of sides
        num_dice, num_sides = dice.split("d")
        if len(num_dice) == 0:
            num_dice = 1

        num_dice = int(num_dice)

        if num_dice > 100:
            return {"error": "Too many dice!"}

        if num_dice < 1:
            return {"error": "Too few dice!"}

        num_sides = int(num_sides)

        # roll each die, add the roll to the rolls array
        for _ in range(num_dice):
            roll = random.randint(1, num_sides)
            results['rolls'].append(roll)
            results['total'] += roll

        # add the modifier
        results['total'] += results['modifier']

        return results

    except Exception as e:
        return {"error": "Something went wrong!"}





