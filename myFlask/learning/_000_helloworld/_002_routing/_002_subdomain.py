from flask import Flask

app = Flask(__name__)
app.config['SERVER_NAME'] = 'example.com:5000'
app.debug = True

""" 이 예제를 확인하기 위해선 hosts 파일에 
    각 도메인을 모두 추가해야한다.
    일반적인 hosts 경로
    C:\Windows\System32\drivers\etc

    test.example.com
    answer.example.com
    example.com
    example2.com
    super.example.com
"""
@app.route("/board", host="example.com")
@app.route("/board", host="example2.com")
def board():
    return "/board URL을 호출하였습니다."

@app.route("/board", subdomain="test") # http://test.example.com:5000/board
@app.route("/board", subdomain="answer") # http://answer.example.com:5000/board
def board_domain_test_and_answer():
    """명확히 확인하고 싶다면 /board 를 /ted, /bod 로 변경해서 확인해보자."""
    return "test, answer 도메인의 board URL을 호출하였습니다."

# http://super.example.com:5000/board
@app.route("/board", subdomain="<user_domain>")
def board_sub_domain_path_variable(user_domain):
    return "{0} 도메인의 /board URL을 호출하였습니다.".format(user_domain)

""" redirect 예제 """
@app.route("/board_now", redirect_to="/now")
def board_redirect_to_now():
    print("body 실행도 되지 않는다.")
    return "이 구문은 실행되지 않습니다."

@app.route("/now")
def board_redirect_handle_now():
    return "redirect 받고 응답합니다."



if __name__ == '__main__':
    app.run()
