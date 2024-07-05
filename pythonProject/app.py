from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Technical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    desc = db.Column(db.String(200))
    price = db.Column(db.String(200))

    def __repr__(self):
        return f'<Technical{self.id}'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        price = request.form['price']
        if title.strip() != '' and desc.strip() != '' and price.strip() != '':
            new_item = Technical(title=title, desc=desc, price=price)
            db.session.add(new_item)
            db.session.commit()
        return redirect('/')
    else:
        items = Technical.query.all()
        return render_template('index.html', items=items)


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    edits = Technical.query.get_or_404(item_id)
    if request.method == 'POST':
        edits.title = request.form['title']
        edits.desc = request.form['desc']
        edits.price = request.form['price']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', edits=edits)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = Technical.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
