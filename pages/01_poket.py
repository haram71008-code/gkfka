import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered"
)

st.title("🎮 MBTI 포켓몬 추천")
st.markdown("나의 MBTI와 가장 잘 어울리는 포켓몬은 누구일까요? 🐾")

pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png",
        "personality": "지적이고 전략적이며 독립적인 성향을 가진 강력한 포켓몬입니다.",
        "reason": "INTJ는 미래를 계획하고 논리적으로 행동하는 전략가 유형이라 뮤츠와 잘 어울립니다."
    },
    "INTP": {
        "name": "후딘",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png",
        "personality": "높은 지능과 분석력을 가진 포켓몬입니다.",
        "reason": "INTP의 탐구심과 분석 능력이 후딘의 이미지와 닮았습니다."
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png",
        "personality": "카리스마와 리더십이 뛰어난 포켓몬입니다.",
        "reason": "ENTJ의 강한 추진력과 자신감이 리자몽과 잘 맞습니다."
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/094.png",
        "personality": "창의적이고 장난기 넘치는 포켓몬입니다.",
        "reason": "ENTP 특유의 재치와 아이디어가 팬텀의 이미지와 비슷합니다."
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png",
        "personality": "신비롭고 깊은 통찰력을 가진 전설의 포켓몬입니다.",
        "reason": "INFJ의 이상주의적이고 배려심 있는 모습과 잘 어울립니다."
    },
    "INFP": {
        "name": "이브이",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",
        "personality": "순수하고 가능성이 무한한 포켓몬입니다.",
        "reason": "INFP의 따뜻함과 상상력이 이브이와 닮았습니다."
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
        "personality": "친절하고 주변을 밝게 만드는 포켓몬입니다.",
        "reason": "ENFJ의 사교성과 리더십을 대표합니다."
    },
    "ENFP": {
        "name": "토게피",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/175.png",
        "personality": "밝고 긍정적인 에너지를 가진 포켓몬입니다.",
        "reason": "ENFP의 활발함과 창의성이 토게피와 잘 맞습니다."
    },
    "ISTJ": {
        "name": "거북왕",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png",
        "personality": "책임감 있고 신뢰할 수 있는 포켓몬입니다.",
        "reason": "ISTJ의 성실함과 안정감이 잘 드러납니다."
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/242.png",
        "personality": "남을 돕고 보살피는 것을 좋아하는 포켓몬입니다.",
        "reason": "ISFJ의 헌신적이고 따뜻한 성격과 닮았습니다."
    },
    "ESTJ": {
        "name": "보스로라",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/306.png",
        "personality": "강한 책임감과 추진력을 가진 포켓몬입니다.",
        "reason": "ESTJ의 조직력과 리더십을 상징합니다."
    },
    "ESFJ": {
        "name": "푸린",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png",
        "personality": "친근하고 사람들과 함께하는 것을 좋아합니다.",
        "reason": "ESFJ의 따뜻한 사교성이 잘 드러납니다."
    },
    "ISTP": {
        "name": "루카리오",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/448.png",
        "personality": "침착하고 뛰어난 문제 해결 능력을 가진 포켓몬입니다.",
        "reason": "ISTP의 실용성과 독립성을 상징합니다."
    },
    "ISFP": {
        "name": "나인테일",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/038.png",
        "personality": "우아하고 감성적인 매력을 가진 포켓몬입니다.",
        "reason": "ISFP의 예술적 감각과 자유로운 영혼을 닮았습니다."
    },
    "ESTP": {
        "name": "괴력몬",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/068.png",
        "personality": "에너지 넘치고 행동력이 뛰어난 포켓몬입니다.",
        "reason": "ESTP의 도전 정신과 활동성을 보여줍니다."
    },
    "ESFP": {
        "name": "파이리",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png",
        "personality": "열정적이고 사람들에게 사랑받는 포켓몬입니다.",
        "reason": "ESFP의 밝고 즐거운 성격과 잘 어울립니다."
    }
}

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    list(pokemon_data.keys())
)

if mbti:
    pokemon = pokemon_data[mbti]

    st.markdown("---")
    st.subheader(f"✨ {mbti}에게 추천하는 포켓몬")

    st.image(pokemon["image"], width=300)

    st.success(f"🐾 추천 포켓몬: {pokemon['name']}")

    st.markdown(f"""
    ### 🌟 포켓몬 성격
    {pokemon['personality']}

    ### 💡 추천 이유
    {pokemon['reason']}
    """)

    st.balloons()
