from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test</title>
        <style>
            .section { padding: 50px; margin: 20px; background: #f0f0f0; }
            .hero { background: #333; color: white; height: 100vh; }
        </style>
    </head>
    <body>
        <div class="hero section">Hero Section</div>
        <div class="section">About Section</div>
        <div class="section">Skills Section</div>
        <div class="section">Contact Section</div>
    </body>
    </html>
    '''

@app.route('/download-resume')
def download_resume():
    resume_path = os.path.join(app.static_folder, 'resume', 'Girish_Fedram_Resume.txt')
    return send_file(resume_path, as_attachment=True, download_name='Girish_Fedram_Resume.txt')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
