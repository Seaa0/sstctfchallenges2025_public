from flask import Flask, render_template_string, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <body style="background-color: #abe0d0; height: 100%; margin: 0; font-size: 35px; font-family: Arial, sans-serif; text-align: center; padding:0;">
            <div style="background-color: #abe0d0; padding: 100px;" >
                <h1>🎉🎊 birthday wishes 🎊🎉</h1>
                <p>an innocent website for birthday wishes</p>
                <p></p>
                <p>type your name below:</p>
                    <form action="/wish" method="get">
                        <div style="height: 8vh; display: flex; flex-direction: column; justify-content: space-between;">
                            <input type="text" id="name" name="name" placeholder="Your Name" style="padding: 10px; font-size: 20px;border-radius: 8px;">
                        </div>
                        <button type="submit" style="padding: 10px; font-size: 20px; background-color: #94c9bb; border: none; border-width: none ;border-radius: 8px;">Submit</button>
                    </form>
            </div>
            
            <div style="background-color: #94c9bb; padding: 10px; width: 100vw; text-align: center; position: fixed; bottom: 0;font-size: 20px;">
                <p>sorry we aren't frontend devs</p>
            </div>
        </body>
    '''

@app.route('/wish')
def wish():
    #get name from query string
    name = request.args.get("name", "user")
    #vuln ssti
    template=f'''
        <body style="margin: 0; padding:0;">
            <div style="background-color: #94c9bb; padding: 150px; margin:0;">
                <div style="background-color: #abe0d0; padding: 50px; border-radius: 20px;">
                    <h1 style="text-algin: center; justify-content: center; font-size: 80px; font-family: Arial, sans-serif;">🎉🎊 birthday wishes 🎊🎉</h1>
                    <p style="text-align: center; font-size: 50px; font-family: Arial, sans-serif;">happy birthday, {name}!</p>
                </div>
            </div>
            <p style="text-align: center;">sincerely, from sstctf :)</p>
        </body>
    '''
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)