from flask import Flask, render_template, request
app = Flask(__name__)

def getReviews():
    f = open("file/file1.txt", 'r')
    lines = f.read().splitlines()
    reviews = []
    for line in lines:
        part = line.split(', ')
        review = {}
        review['film_name'] = part[0]
        review['stars'] = part[1]
        reviews.append(review)
    f.close()
    return reviews 

def filterReviews(reviews, stars):
    if stars is not None:
        filtered_reviews = []
        for review in reviews:
            print(review)
            if review['stars'] == stars:
                filtered_reviews.append(review)
        return filtered_reviews
    return reviews

@app.route('/films/list')
def get_films():
    return render_template('index.html', reviews=filterReviews(getReviews(), request.args.get('stars')))

@app.route('/films/submit')
def get_review_form():
    return render_template('form.html')

@app.route('/films/submit', methods=['POST'])
def submit_review():
    f = open("file/file1.txt", 'a')
    f.write(request.form['film_name'] + ', ' + request.form['stars'] + '\n')
    f.close()
    return render_template('index.html', reviews=getReviews())