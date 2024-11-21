from flask import Flask, render_template, request

app = Flask(__name__)

# 데이터 파일 경로
DATA_FILE = "./data/content.txt"

# 웹 페이지 렌더링
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 입력값 받아오기
        user_input = request.form.get("user_input")
        if user_input:
            # data.txt에 입력값 저장 (UTF-8 인코딩)
            with open(DATA_FILE, "a", encoding="utf-8") as file:
                file.write(user_input + "\n")
    
    # data.txt 읽어서 출력 (UTF-8 인코딩)
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            contents = file.readlines()
    except FileNotFoundError:
        contents = []
    
    return render_template("index.html", contents=contents)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
