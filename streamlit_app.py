import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('path/to/your/image.png')  # ローカルの画像ファイルへのパスを指定

# CSSスタイルの定義
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    body {
        background-image: url('https://www.transparenttextures.com/patterns/paper.png');
        font-family: 'Pacifico', cursive;
        color: #333;
    }
    .title {
        color: #ff69b4;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .question {
        color: #ff1493;
        font-size: 1.2em;
        margin-top: 10px;
    }
    .result {
        color: #ff4500;
        font-weight: bold;
        text-align: center;
        font-size: 1.5em;
    }
    .button {
        background-color: #ff69b4;
        color: white;
        border-radius: 15px;
        padding: 10px 20px;
        font-size: 1.2em;
    }
    .button:hover {
        background-color: #ff1493;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 ヤンデレ度診断 💖")

# ヤンデレ画像のURL（例として使用します。実際の使用には著作権に注意してください）
yandere_image_url = "https://example.com/yandere_image.jpg"

# 画像を読み込んで表示
try:
    response = requests.get(yandere_image_url)
    image = Image.open(BytesIO(response.content))
    st.image(image, caption="ヤンデレのイメージ", use_column_width=True)
except Exception as e:
    st.warning("画像の読み込みに失敗しました。代わりにテキストで説明します。")
    st.write("ヤンデレとは、好意を寄せる相手に対して過剰な愛情や執着を示す人物像を指します。")

questions = [
    "💌 好きな人の連絡先をすべて知っていますか？",
    "😰 相手の予定を把握していないと不安になりますか？",
    "😡 相手が他の異性と話しているのを見るとどう感じますか？",
    "📱 相手のSNSをこまめにチェックしていますか？",
    "🚫 相手との関係を邪魔する人がいたらどうしますか？",
    "🏠 相手の持ち物や部屋に自分の物を置きたくなりますか？",
    "📸 相手の写真をたくさん撮影していますか？",
    "😒 相手が自分以外の人と仲良くしているのを見ると嫉妬しますか？",
    "🔒 相手の行動を制限したいと思うことがありますか？",
    "💪 相手のためなら何でもできると思いますか？",
    "🎨 相手の趣味や好みに合わせて自分を変えようとしますか？",
    "🌈 相手との将来を頻繁に想像しますか？",
    "⚠️ 相手との関係が終わるくらいなら、何か極端なことをしても良いと思いますか？",
    "😊 相手の幸せが自分の幸せだと感じますか？",
    "😵 相手のことを考えると、時々冷静さを失うことがありますか？"
]

st.write("以下の質問に答えて、あなたのヤンデレ度を診断しましょう。")

scores = []
for i, question in enumerate(questions):
    score = st.slider(f"質問 {i+1}: {question}", 0, 5, 2)
    scores.append(score)

if st.button("診断する", key="submit", help="診断結果を見る"):
    total_score = sum(scores)
    max_score = len(questions) * 5
    yandere_percentage = (total_score / max_score) * 100

    st.markdown(f"<div class='result'>あなたのヤンデレ度は: {yandere_percentage:.2f}%</div>", unsafe_allow_html=True)

    if yandere_percentage < 20:
        st.write("あなたはほとんどヤンデレの傾向がありません。健全な関係を築けそうです。")
    elif yandere_percentage < 40:
        st.write("あなたは少しヤンデレの傾向があります。相手を大切に思う気持ちは素晴らしいですが、適度な距離感を保つことも大切です。")
    elif yandere_percentage < 60:
        st.write("あなたはかなりヤンデレの傾向があります。相手を思う気持ちが強すぎて、時に相手を窮屈にさせてしまうかもしれません。")
    elif yandere_percentage < 80:
        st.write("あなたは高度なヤンデレの傾向があります。相手への愛情が強すぎて、健全な関係を築くのが難しいかもしれません。カウンセリングを検討してみてはいかがでしょうか。")
    else:
        st.write("あなたは極度のヤンデレの傾向があります。相手への執着が強すぎて、危険な行動につながる可能性があります。専門家に相談することをお勧めします。")

    advices = [
        "相手の個人的な空間と時間を尊重することが大切です。",
        "自分自身の趣味や友人関係を大切にしましょう。",
        "相手の行動を制限しようとする衝動を感じたら、深呼吸をして冷静になりましょう。",
        "嫉妬の感情は自然ですが、それをコントロールする方法を学びましょう。",
        "相手との関係だけでなく、自己成長にも焦点を当てることが重要です。"
    ]
    
    st.write("💡 アドバイス:", random.choice(advices))


