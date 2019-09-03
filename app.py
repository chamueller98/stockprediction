from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/2")
def view_template():
    print("Chau mundo!")
    return render_template("index.html")

@app.route("/3")
def view_template2():
    name = request.args.get('name')
    print (name)

    return render_template("page2.html",a_name=name)






if __name__ == "__main__":
    app.run(debug=True)