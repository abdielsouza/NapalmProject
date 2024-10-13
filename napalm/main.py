from napalm import Napalm

app: Napalm = Napalm()

@app.route("/home/{name}")
def home(request, response, name):
    response.text = f"home section for {name}"

app.run()