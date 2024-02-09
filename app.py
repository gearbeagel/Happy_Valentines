from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/', methods=['GET', 'POST'])
def page():
    no_count = int(request.form.get('no_count', 0))
    yes_pressed = request.form.get('yes_pressed', False, type=bool)

    phrases = [
        "Ні",
        "Ти впевнений?",
        "Прям дуже впевнений?",
        "Киць, подумай ще раз",
        "Точно?",
        "Ти мене дразниш, так?(",
        "Запевнився?",
        "Чому ти не передумаєш?",
        "Це твоя остаточна відповідь?",
        "Все, мені сумно :("
    ]

    no_button_text = phrases[no_count % len(phrases)]
    disable_no_button = no_count == len(phrases) - 1

    if request.method == 'POST':
        if 'yes_button' in request.form:
            return render_template('page.html', yes_pressed=True)
        elif 'no_button' in request.form:
            no_count = int(request.form['no_count']) + 1
            no_button_text = phrases[no_count % len(phrases)]
            disable_no_button = no_count == len(phrases) - 1
            return render_template('page.html', no_count=no_count, no_button_text=no_button_text, disable_no_button=disable_no_button)

    return render_template('page.html', no_count=no_count, yes_pressed=yes_pressed,
                           no_button_text=no_button_text, phrases=phrases)


if __name__ == '__main__':
    app.run(debug=True)
