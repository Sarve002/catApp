import importlib
from flask import request, render_template
from webApp import app, api_func, routes

print(api_func.getCats())
#print(api_func.getCatFacts())


@app.route("/", methods=['GET'])
def baseIndex():

    cats = api_func.getCats()
    url = cats[0][0]["url"]
    return render_template("catJam.html", catUrl=url)


@app.route("/", methods=['GET','POST'], endpoint='getNewCat')
def getNewCat():

    #if request.method == 'GET':
    if request.form.get('Get new Cat') == 'Get new Cat':
        importlib.reload()
        newCat = api_func.getCats()
        caturl = newCat[0][0]["url"]

        return render_template("catJam.html", catUrl=caturl)
    return baseIndex()