from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

#hi


@app.route('/',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('form.html',pred=results)

@app.route('/info')
def info_page():
    if request.method == 'POST':
        return render_template('info.html', shortcode=request.form['shortcode'])
    elif request.method == 'GET':
        return redirect(url_for('/'))
    else:
        return 'Not a valid request method for this route'

    return render_template('info.html')








if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)