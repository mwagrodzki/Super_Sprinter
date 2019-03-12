from flask import Flask, render_template, redirect, request
import data_manager

app = Flask(__name__)

@app.route('/')
def index():
    stories = None
    saved_data = data_manager.import_data()
    if saved_data:
        stories = saved_data

    return render_template('index.html', stories=stories)


@app.route('/story', methods=['GET', 'POST'])
@app.route('/story/<id>', methods=['GET', 'POST'])
def story(id=None):
    saved_data = data_manager.import_data()
    if request.method == 'POST':
        if id:
            saved_data[id]['title'] = request.form['title']
            saved_data[id]['user_story'] = request.form['user_story']
            saved_data[id]['acceptance_criteria'] = request.form['acceptance_criteria']
            saved_data[id]['business_value'] = request.form['business_value']
            saved_data[id]['estimation'] = request.form['estimation']
            saved_data[id]['status'] = request.form['status']
        else:
            new_story = {'title': request.form['title'],
                         'user_story': request.form['user_story'],
                         'acceptance_criteria': request.form['acceptance_criteria'],
                         'business_value': request.form['business_value'],
                         'estimation': request.form['estimation'],
                         'status': 'In Progress'}
            saved_data[str(len(saved_data))] = new_story
        data_manager.export_data(saved_data)
        return redirect('/')
    story = None
    if id:
        story = saved_data[id]

    return render_template('story.html', Id=id, story=story)


if __name__ == '__main__':
    app.run()
