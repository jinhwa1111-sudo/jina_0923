from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)

CORS(app)

# 영화 명대사 리스트 (다른 API나 DB 호출 없이 로직만으로)
movie_quotes = [
    "포스가 너와 함께하길. (May the Force be with you.) - 스타워즈",
    "이건 시작에 불과해! (This is just the beginning!) - 배트맨 비긴즈",
    "여보게, 자네는 훌륭한 사람이야. (You're a good man, Charlie Brown.) - 찰리 브라운",
    "쇼생크 탈출! (The Shawshank Redemption!) - 쇼생크 탈출",
    "죽느냐 사느냐 그것이 문제로다. (To be or not to be, that is the question.) - 햄릿 (영화화된 작품 다수)",
    "나는 터미네이터다. (I'm the Terminator.) - 터미네이터",
    "이 또한 지나가리라. (This too shall pass.) - 반지의 제왕 (원작은 아니지만 영화에서 많이 회자됨)",
    "카르페 디엠. 현재를 즐겨라. (Carpe Diem. Seize the day, boys.) - 죽은 시인의 사회",
    "세상에 완벽한 건 없어. (Nobody's perfect.) - 뜨거운 것이 좋아",
    "인생은 원래 힘든 거야. (Life's a bitch.) - 저수지의 개들",
    "내가 다시 돌아올게. (I'll be back.) - 터미네이터",
    "내일은 내일의 태양이 뜬다. (Tomorrow is another day.) - 바람과 함께 사라지다",
    "꿈을 쫓아라. (Follow your dreams.) - 여러 영화에서 등장",
    "큰 힘에는 큰 책임이 따른다. (With great power comes great responsibility.) - 스파이더맨",
    "이 나쁜 놈들아! (You dirty rats!) - 더티 해리",
    "사랑은 모든 것을 이긴다. (Love conquers all.) - 여러 영화에서 등장",
    "나는 왕이다. (I am the king.) - 라이온 킹",
    "우리는 모두 미쳤어. (We're all mad here.) - 이상한 나라의 앨리스 (영화화된 작품 다수)",
]

@app.route('/api/random')
def random_number():
    """1부터 99 사이의 랜덤한 정수를 생성하고 JSON 형태로 반환합니다."""
    number = random.randint(1, 99)
    return jsonify({'number': number})

@app.route('/api/random-quote')
def random_quote():
    """미리 정의된 영화 명대사 리스트에서 랜덤한 명대사를 선택하여 JSON 형태로 반환합니다."""
    quote = random.choice(movie_quotes)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
