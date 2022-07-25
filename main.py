from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

romInt = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

intRom = dict((v, k) for k, v in romInt.items())

@app.route('/', methods=['GET'])
def url():
    return "V31COM3"

@app.route('/romanToInt/<romNum>', methods=['GET'])
def romanToInt(romNum):
    total = 0
    for char in romNum:
        try:
            previousVal = int(romInt.get(prev_char))
        except UnboundLocalError:
            previousVal = int(romInt.get(char))
        currentVal = int(romInt.get(char))
        total += romInt.get(char)
        if currentVal > previousVal:
            total -= 2 * (romInt.get(prev_char))
        prev_char = char

    return str(total)

@app.route('/intToRoman/<integer>', methods=['GET'])
def intToRoman(integer):
    integer = int(integer)
    base = 1
    if integer == 0:
        return ""
    if integer in intRom:
        result = intRom.get(integer)
        return result
    length = len(str(integer))
    potentialMax = base * 10 ** length
    subtractive = base * 10 ** (length - 1)
    maxConversion = romInt.get(list(romInt)[-1])

    if potentialMax > maxConversion:
        result = ""
        repeat = integer // maxConversion
        for _ in range(repeat):
            result += intRom.get(maxConversion)
    elif str(integer)[0] == str(potentialMax - subtractive)[0]:
        result = intRom.get(subtractive) + intRom.get(potentialMax)
    elif potentialMax / 2 < integer < potentialMax:
        result = intRom.get(potentialMax / 2)
    else:
        if str(integer)[0] == str(potentialMax / 2 - subtractive)[0]:
            result = intRom.get(subtractive) + intRom.get(potentialMax / 2)
        else:
            result = intRom.get(subtractive)
    remainder = (integer - int(romanToInt(result)))
    return result + intToRoman(remainder)


# start flask app
app.run(host="0.0.0.0", port=5000)
