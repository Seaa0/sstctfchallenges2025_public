from flask import Flask, request, render_template, jsonify
import random
import string

random.seed(REDACTED)

app = Flask(__name__)

@app.route('/')
def home():
    #instructions
    return '''
    <h1>Secret Spy Training agency database</h1>
    <p style="font-size:20px;">
    Welcome to the Secret Spy Training agency.<br>A mole has infiltrated the agency and leaked a list of undercover operatives. <br>You’ve been granted access to your own profile in the agent database. <br>Can you uncover the mole's identity before the damage is irreversible?
    </p>
    <a href="/profile?id=1">
        <button>view your profile</button>
    </a>
    '''

# Create a list of users
def generate_users(num_users):
    users = {}
    for i in range(1, num_users + 1):
        # Generate random username
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        desc = "innocent :)"
        # Add to users dictionary with user_id as the key
        users[str(i)] = {"name": username, "description": desc}
    #spy user id
    spy_userid = random.randint(2,num_users) #id 1 is the user
    spy_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    flag = "oops, you've caught me...\nFlag: sstctf{REDACTED}"
    users[str(spy_userid)] = {"name": spy_username, "description": flag}
    print('spy id: ' + str(spy_userid))
    #default user id (id=1)
    desc_user1 = "Recruited by the SST agency at age 13, I specialize in undercover operations and intelligence gathering. With extensive experience in high-risk missions, I blend in seamlessly and adapt quickly to complete assignments with precision, making me a trusted asset in critical situations. (hint: look outside the box)"
    users['1']["description"] = desc_user1
    print(users)

    return users

users = generate_users(40)

@app.route('/profile')
def profile():
    # Extract 'id' from the URL query string
    user_id = request.args.get('id')

    # Check if the user exists
    if user_id in users:
        user = users[user_id]
        # Render the template and pass user data
        return render_template('index.html', user=user)
    else:
        # Return an error if user is not found
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
