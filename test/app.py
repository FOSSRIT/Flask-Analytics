from flask import Flask, render_template
from flask_analytics import Analytics

app = Flask(__name__)

app.config['GAUGES_SITEID'] = 'soV5eile3aiFi9E'
app.config['GOOGLE_ANALYTICS_ID'] = 'wiengech9tiefuW'
app.config['PIWIK_BASEURL'] = 'aeniki8pheiFiad'
app.config['PIWIK_SITEID'] = 'uiP3eeKie6ohDo6'
app.config['GOSQUARED_ID'] = 'ahz1Nahqueorahw'
app.config['CHARTBEAT_UID'] = 'uiP3eeKie6ohDo6'
app.config['CHARTBEAT_DOMAIN'] = 'eeda8Otheefu5qu'

Analytics(app)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/google/')
def google():

    return render_template('google.html')

@app.route('/gauges/')
def gauges():

    return render_template('gauges.html')

@app.route('/piwik/')
def piwik():

    return render_template('piwik.html')

@app.route('/gosquared/')
def gosquared():

    return render_template('gosquared.html')

@app.route('/chartbeat/')
def chartbeat():

    return render_template('chartbeat.html')

if __name__ == '__main__':

    app.run()
