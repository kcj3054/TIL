from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework
# dbhomework를 못찾았넹...

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_give = request.form['name']
    count_give = request.form['cnt']
    address_give = request.form['address']
    call_give = request.form['call']

    doc = {
        'name_give' : name_give,
        'count_give' : count_give,
        'address_give' : address_give,
        'call_give' : call_give
    }
    db.shop.insert_one(doc);
    return jsonify({'msg': '저장완료'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.shop.find({}, {'_id' : False}))
    return jsonify({'msg': '이 요청은 GET!', 'orders' : orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)