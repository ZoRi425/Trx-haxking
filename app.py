from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Number Guessing</title>
  <style>
    html, body {
      height: 100%;
      margin: 0;
      background: #000;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .container {
      width: 98vmin;
      height: 98vmin;
      background: linear-gradient(to bottom, #000000, #550000);
      color: #fff;
      text-align: center;
      padding: 10px 15px;
      box-sizing: border-box;
      border-radius: 20px;
      box-shadow: 0 0 20px #ff4444;
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;
    }
    .title {
      font-size: 38px;
      color: yellow;
      font-weight: bold;
      margin: 0 0 20px 0;
    }
    h1 {
      font-size: 36px;
      color: #ff4444;
      margin: 0 0 20px 0;
    }
    input[type=number] {
      font-size: 60px;
      padding: 20px;
      width: 160px;
      border-radius: 15px;
      border: 3px solid #ff4444;
      text-align: center;
      background-color: #000;
      color: #fff;
      margin-bottom: 20px;
    }
    .button-group {
      margin: 10px 0;
    }
    button {
      font-size: 40px;
      padding: 20px 50px;
      margin: 10px;
      border: none;
      border-radius: 15px;
      background-color: #ff4444;
      color: #fff;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    button:hover {
      background-color: #cc0000;
    }
    .result {
      font-size: 70px;
      font-weight: bold;
      margin: 20px 0 0 0;
      height: 90px;
      line-height: 90px;
    }
    .result.big {
      color: #00ff00;
      text-shadow: 0 0 20px #00ff00, 0 0 30px #00ff00;
      animation: flashBig 1s infinite;
    }
    .result.small {
      color: #ffcc00;
      text-shadow: 0 0 20px #ffcc00, 0 0 30px #ffcc00;
      animation: flashSmall 1s infinite;
    }
    @keyframes flashBig {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }
    @keyframes flashSmall {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }
    .footer {
      font-size: 22px;
      color: yellow;
      line-height: 1.4;
      margin: 0;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="title">TRX hacking 90% win rate</div>
    <h1>Guess if the next round number is BIG or SMALL</h1>
    <form method="post" id="guessForm">
      <input type="number" name="number" min="0" max="9" required>
      <div class="button-group">
        <button type="submit">Confirm</button>
        <button type="button" onclick="document.getElementsByName('number')[0].value = '';">Reset</button>
      </div>
    </form>
    {% if result %}
    <div class="result {{ 'big' if result == 'BIG' else 'small' }}">{{ result }}</div>
    {% endif %}
    <div class="footer">
      Created by MaungKaung<br>
      — Contact me @SoriNori995
    </div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            if num >= 5:
                result = "BIG"
            else:
                result = "SMALL"
        except:
            result = "Please enter a valid number"
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)