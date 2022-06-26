from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html',title='LK')


@app.route('/price')
def price():
    return render_template('price.html',title='Price')

@app.route('/studio')
def studio():
    return render_template('studio.html',title='Studio')

@app.route('/portfolio')
def portfolio():

    beauty_photos  = ['/portfolio/Beauty/'+photo for photo in os.listdir('./static/portfolio/Beauty')]
    fashion_photos = ['/portfolio/Fashion/'+photo for photo in os.listdir('./static/portfolio/Fashion')]
    street_photos  = ['/portfolio/Outdoor/'+photo for photo in os.listdir('./static/portfolio/Outdoor')]
    studio_photos  = ['/portfolio/Studio-Indoor/'+photo for photo in os.listdir('./static/portfolio/Studio-Indoor')]
    still_photos   = ['/portfolio/Still-Life/'+photo for photo in os.listdir('./static/portfolio/Still-Life')]
    

    return render_template('portfolio.html',title='Portfolio',
        street_photos   = street_photos, studio_photos=studio_photos,beauty_photos=beauty_photos,
        fashion_photos = fashion_photos, still_photos = still_photos)

@app.route('/portfolio/<collection>/')
def show_collection(collection):
    coll_fld = f'./static/portfolio/{collection}/'
    photos_name = os.listdir(coll_fld)
    photos_path = ['portfolio/'+collection+'/'+f'/{photo}' for photo in photos_name ]


    return render_template('show_collection.html',title=collection, data=photos_path)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)