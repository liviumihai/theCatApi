from flask import Flask, render_template, request, url_for, redirect
import urllib.parse
import requests
import json


app = Flask(__name__)


@app.route("/")
def homepage():

    img_url = url = 'https://api.thecatapi.com/v1/images/search?api_key=69e306c2-8b8d-4787-bfaf-ecab686a5b30'
    json_data = requests.get(url).json()
    img = json_data[0]['url']

    return render_template("home.html", img = img)


@app.route("/beng")
def beng():

    main_api = 'https://api.thecatapi.com/v1/images/search?'
    api_key = '69e306c2-8b8d-4787-bfaf-ecab686a5b30'
    breed_id = 'beng'

    url = main_api + urllib.parse.urlencode({'breed_ids': breed_id}) + "&" + urllib.parse.urlencode({'api_key': api_key})
    json_data = requests.get(url).json()

    cat_description = json_data[0]['breeds'][0]['description']
    cat_name = json_data[0]['breeds'][0]['name']
    cat_wiki = json_data[0]['breeds'][0]['wikipedia_url']
    cat_img = json_data[0]['url']

    return render_template("breed.html", cat_image = cat_img, cat_name = cat_name, cat_description = cat_description, cat_wiki= cat_wiki)


@app.route("/aege")
def aege():

    main_api = 'https://api.thecatapi.com/v1/images/search?'
    api_key = '69e306c2-8b8d-4787-bfaf-ecab686a5b30'
    breed_id = 'aege'

    url = main_api + urllib.parse.urlencode({'breed_ids': breed_id}) + "&" + urllib.parse.urlencode({'api_key': api_key})
    json_data = requests.get(url).json()

    cat_description = json_data[0]['breeds'][0]['description']
    cat_name = json_data[0]['breeds'][0]['name']
    cat_wiki = json_data[0]['breeds'][0]['wikipedia_url']
    cat_img = json_data[0]['url']

    return render_template("breed.html", cat_image = cat_img, cat_name = cat_name, cat_description = cat_description, cat_wiki= cat_wiki)


@app.route("/abys")
def abys():

    main_api = 'https://api.thecatapi.com/v1/images/search?'
    api_key = '69e306c2-8b8d-4787-bfaf-ecab686a5b30'
    breed_id = 'abys'

    url = main_api + urllib.parse.urlencode({'breed_ids': breed_id}) + "&" + urllib.parse.urlencode({'api_key': api_key})
    json_data = requests.get(url).json()

    cat_description = json_data[0]['breeds'][0]['description']
    cat_name = json_data[0]['breeds'][0]['name']
    cat_wiki = json_data[0]['breeds'][0]['wikipedia_url']
    cat_img = json_data[0]['url']

    return render_template("breed.html", cat_image = cat_img, cat_name = cat_name, cat_description = cat_description, cat_wiki= cat_wiki)


@app.route("/acur")
def acur():

    main_api = 'https://api.thecatapi.com/v1/images/search?'
    api_key = '69e306c2-8b8d-4787-bfaf-ecab686a5b30'
    breed_id = 'acur'

    url = main_api + urllib.parse.urlencode({'breed_ids': breed_id}) + "&" + urllib.parse.urlencode({'api_key': api_key})
    json_data = requests.get(url).json()

    cat_description = json_data[0]['breeds'][0]['description']
    cat_name = json_data[0]['breeds'][0]['name']
    cat_wiki = json_data[0]['breeds'][0]['wikipedia_url']
    cat_img = json_data[0]['url']

    return render_template("breed.html", cat_image = cat_img, cat_name = cat_name, cat_description = cat_description, cat_wiki= cat_wiki)


if __name__ == '__main__':
    app.run(debug=True)



