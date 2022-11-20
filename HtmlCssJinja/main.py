from flask import Flask, render_template
from LoginForm import LF


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello hello hello hello hello world'



@app.route('/')
def main():
   return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = LF()
    if form.validate_on_submit():
        if form.password_again.data != form.password.data:
            return render_template('register.html', tittle="Регистрация", form=form,
                                    message = "Пароли не совпадают!!!")

        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}')
        return render_template('register.html', message = "Регистрация прошла успешно")
    return render_template('register.html', tittle="Регистрация", form=form)



if __name__ == '__main__':
    app.run()






'''
a - режим добавления
w - режим на запись (очищает файл)
r - режим считывания
'''