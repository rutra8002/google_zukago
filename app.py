from flask import Flask, render_template, request
from engine import SearchEngine
import math

app = Flask(__name__)
search_engine = SearchEngine()
RESULTS_PER_PAGE = 15  # Adjust the value as per your requirement


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        search_results = search_engine.search(query)
        num_pages = get_num_pages(search_results)
        page = request.args.get('page', 1, type=int)
        paginated_results = paginate_results(search_results, page)
        return render_template('index.html', search_results=paginated_results, query=query, options=search_engine.options, num_pages=num_pages, page=page)
    else:
        query = request.args.get('query', '')
        search_results = search_engine.search(query)
        num_pages = get_num_pages(search_results)
        page = request.args.get('page', 1, type=int)
        paginated_results = paginate_results(search_results, page)
        return render_template('index.html', search_results=paginated_results, query=query, options=search_engine.options, num_pages=num_pages, page=page)

def get_num_pages(results):
    per_page = 15
    num_pages = math.ceil(len(results) / per_page)
    return num_pages

def paginate_results(results, page):
    per_page = 15
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_results = results[start_index:end_index]
    return paginated_results


@app.route('/add_result', methods=['GET', 'POST'])
def add_result():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        success_message = search_engine.add_result(name, url)  # Update this line
        return render_template('add_result.html', success_message=success_message)
    else:
        return render_template('add_result.html')


if __name__ == '__main__':
    app.run(host='localhost', port=69420)
