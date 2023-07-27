from flask import Flask, request, jsonify, render_template
from flask_restx import Api, Resource, fields, reqparse
from werkzeug.datastructures import FileStorage
from analyze_image import analyze, image_to_array

app = Flask(__name__)

api = Api(app, version="1.0", title="API 문서", description="Swagger 문서", doc="/api-docs")


analyze_image_api = api.namespace("", description="이미지 분석 API")

# 요청 매개변수를 정의하는 RequestParser 객체 생성
parser = reqparse.RequestParser()
parser.add_argument("image", type=FileStorage, location="files", required=True)


@app.route("/test")
def test():
    return jsonify("/test에 대한 요청이 성공하였습니다!!!!!!!")


@app.route("/video")
def home():
    return render_template("video.html")  # 여기서 index.html은 당신의 홈페이지 템플릿 파일입니다.


@analyze_image_api.route("/analyze", methods=["POST"])
class AnalyzeImageResource(Resource):
    @analyze_image_api.expect(parser, validate=True)
    def post(self):
        # POST 요청에서 이미지 데이터를 가져옴.
        image = request.files["image"]

        # 이미지를 numpy 배열로 변환
        image = image_to_array(image)

        # 이미지를 분석하여 결과를 반환
        result = analyze(image)

        if result.get("message") == "failed":
            return result
        elif result.get("message") == "success":
            if result.get("emotion") == "Happy" and result.get("stopVideo"):
                print("웃었네요. 종료합니다.ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                result["stopVideo"] = True
                return jsonify(result)
            else:
                return jsonify(result)


analyze_image_api.add_resource(AnalyzeImageResource, "/analyze")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
