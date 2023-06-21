from flask import Flask, render_template, request
import key_config as keys
import boto3 
import dynamoDB_create_table as dynamodb_ct

app = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb',
    #aws_access_key_id     = keys.ACCESS_KEY_ID,
    #aws_secret_access_key = keys.ACCESS_SECRET_KEY,
    region_name           = keys.REGION_NAME,
)

@app.route('/')
def index():
    # dynamodb_ct.create_table()
    # return 'Table Created'
    return render_template('index.html')

@app.route('/login')
def login():    
    return render_template('login.html')
    
@app.route('/signup', methods=['post'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    table = dynamodb.Table('users')#getting the table
    
    table.put_item(
                Item={
        'name': name,
        'email': email,
        'password': password
            }
        )
    
    msg = "Registration Complete. Please Login to your account !"
    
    return render_template('login.html', msg = msg)
    
if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')
