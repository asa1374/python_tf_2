import re
from flask import Flask, jsonify, render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc')
def calc():
    sick = request.args.get('sick','0')
    if (sick == '0'):
        print('넘어온 식이 없다.')
    else :
        print('넘어온 식 : {}'.format(sick))
        patt = '[0-9]+'
        op = re.sub(patt,'',sick)
        print('넘어온 연산자 : {}'.format(op))
        nums = sick.split(op)
        result = 0
        if op == '+':
            result = int(nums[0]) + int(nums[1])

    print(result)

    return jsonify(result = result)

if __name__ == '__main__':
    app.run()
