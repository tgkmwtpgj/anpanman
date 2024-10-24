import streamlit as st
import random

# カスタムCSSの定義
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Mochiy+Pop+One&display=swap');

    body {
        font-family: 'Mochiy Pop One', sans-serif;
        background: linear-gradient(135deg, #FFD1DC, #FFC0CB, #FFB6C1);
        color: #FF69B4;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .cute-box {
        background-color: rgba(255, 182, 193, 0.3);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #FF1493;
        margin: 20px 0;
    }
    .advice {
        font-style: italic;
        background-color: rgba(255, 255, 224, 0.7);
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .footer {
        font-size: 12px;
        text-align: center;
        margin-top: 30px;
        color: #808080;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF1493;
        transform: scale(1.05);
    }
    .stSlider>div>div>div>div {
        background-color: #FF69B4;
    }
</style>
""", unsafe_allow_html=True)

st.title("💖 ヤンデレ度診断 💖")

st.markdown("""
<div class='cute-box'>
    <p>あなたの愛情度をチェックしましょう！</p>
    <p>以下の質問に正直に答えてくださいね♪</p>
</div>
""", unsafe_allow_html=True)

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

scores = []
for i, question in enumerate(questions):
    score = st.slider(f"質問 {i+1}: {question}", 0, 5, 2, key=f"q{i}")
    scores.append(score)

if st.button("診断する💕", key="submit", help="あなたの愛情度を診断します"):
    total_score = sum(scores)
    max_score = len(questions) * 5
    yandere_percentage = (total_score / max_score) * 100

    st.markdown(f"<div class='result'>あなたの愛情度は: {yandere_percentage:.2f}%</div>", unsafe_allow_html=True)

    if yandere_percentage < 20:
        result = "健全な愛情です！素敵な関係を築けそうですね♪"
    elif yandere_percentage < 40:
        result = "ちょっぴり強い愛情かも。でも、まだ大丈夫そうです！"
    elif yandere_percentage < 60:
        result = "愛情が強めです。相手の気持ちも大切にしてくださいね。"
    elif yandere_percentage < 80:
        result = "かなり強い愛情をお持ちのようです。少し落ち着いてみましょう。"
    else:
        result = "とっても強い愛情ですね。でも、相手を大切にするためにも、自分自身も大切にしましょう。"

    st.markdown(f"<div class='cute-box'>{result}</div>", unsafe_allow_html=True)

    advices = [
        "相手の個性を尊重することも愛情表現の一つです💖",
        "自分の趣味や友達との時間も大切にしましょう🌟",
        "相手のことを考えすぎて疲れちゃったら、深呼吸してリラックス😌",
        "嫉妬の気持ちは自然なものです。でも、それをコントロールする方法を見つけましょう🎭",
        "二人の関係だけでなく、自分自身の成長にも目を向けてみては？🌱"
    ]
    
    st.markdown(f"<div class='advice'>💡 アドバイス: {random.choice(advices)}</div>", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
    <p>※この診断はあくまで娯楽目的です。専門家の診断ではありません。</p>
    <p>困ったことがあれば、信頼できる人や専門家に相談してくださいね。</p>
</div>
""", unsafe_allow_html=True)


