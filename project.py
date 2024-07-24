
from flask import Flask, request, render_template
from random import randint


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Number_Guessing', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Generate random numbers
        result_numbers = [randint(0, 9) for n in range(3)]

        #Text algorithmn Tokenization
        separators,stored_bet,validate_bet = [" ", "-"],[],""
        
        for char in user_input:
            if char in separators:
                if validate_bet:
                    stored_bet.append(validate_bet)
                    validate_bet = ""
            else:
                validate_bet += char
        if validate_bet:
            stored_bet.append(validate_bet)
        
        #convert userbet  from list to single string
        UserBet = ""
        for num in stored_bet:
            UserBet += str(num)
        
        #convert Random result from list to single string
        result = ""
        for num in result_numbers:
            result += str(num)


         #validate the user inputs 

        if len(UserBet) == 3 and UserBet.isdigit():
             msg = ("You win" if UserBet == result else "Partial win" if sorted(UserBet) == sorted(result) else "You Lose!" )
        else:
            msg = "Input 3 numbers only" if len(UserBet) > 3  else "Number only!!!"

        return render_template('result.html', UserBet=UserBet, result=result, msg=msg)

    return render_template('index.html')



@app.route("/check_palindrome",methods = ["GET","POST"])

def palendrom():
    _msg = ""
    if request.method == "POST":
       _userinput = request.form["_userinput"]
       pal_result = _userinput
       pal_check = _userinput.lower().replace(" ","")
       word_reversed = pal_check[::-1]
       if word_reversed:
        _msg = (f"{pal_result} is palindrome" if pal_check == word_reversed else f"{pal_result} is not a palindrome")
      
    return render_template("palen.html",_msg=_msg)
        

if __name__ == '__main__':
    app.run(debug=True)
