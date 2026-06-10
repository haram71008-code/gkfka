import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 캐릭터 추천",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 MBTI 포켓몬 캐릭터 추천")
st.write("MBTI를 선택하면 나와 닮은 포켓몬 캐릭터와 성격을 알려줘요! ✨")

pokemon_data = {

    "INTJ": {
        "pokemon": "뮤츠",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png",
        "personality": "강력한 카리스마와 뛰어난 전략성을 가진 포켓몬입니다. 깊이 생각하고 목표를 끝까지 밀고 나가는 모습이 INTJ와 닮았습니다."
    },

    "INTP": {
        "pokemon": "메타몽",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/132.png",
        "personality": "창의적이고 호기심이 많습니다. 새로운 가능성을 탐구하는 INTP의 성향과 잘 어울립니다."
    },

    "ENTJ": {
        "pokemon": "리자몽",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png",
        "personality": "자신감 있고 리더십이 강합니다. 도전 정신이 뛰어난 ENTJ를 대표합니다."
    },

    "ENTP": {
        "pokemon": "고라파덕",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/054.png",
        "personality": "엉뚱하지만 기발한 아이디어가 많습니다. ENTP 특유의 창의성이 돋보입니다."
    },

    "INFJ": {
        "pokemon": "루기아",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png",
        "personality": "신비롭고 통찰력이 깊습니다. 타인을 배려하는 INFJ와 잘 어울립니다."
    },

    "INFP": {
        "pokemon": "이브이",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",
        "personality": "따뜻하고 상상력이 풍부합니다. 다양한 가능성을 가진 INFP의 모습을 보여줍니다."
    },

    "ENFJ": {
        "pokemon": "피카츄",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
        "personality": "밝고 친절하며 주변 사람들에게 긍정적인 에너지를 전합니다."
    },

    "ENFP": {
        "pokemon": "토게피",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/175.png",
        "personality": "호기심이 많고 활발합니다. 사람들에게 행복을 전하는 ENFP와 닮았습니다."
    },

    "ISTJ": {
        "pokemon": "거북왕",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png",
        "personality": "성실하고 책임감이 강합니다. 믿음직한 ISTJ를 상징합니다."
    },

    "ISFJ": {
        "pokemon": "해피너스",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/242.png",
        "personality": "배려심이 깊고 따뜻합니다. 다른 사람을 잘 챙기는 ISFJ와 닮았습니다."
    },

    "ESTJ": {
        "pokemon": "보스로라",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/306.png",
        "personality": "강한 책임감과 리더십을 가진 든든한 포켓몬입니다."
    },

    "ESFJ": {
        "pokemon": "푸린",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png",
        "personality": "사교적이고 다정합니다. 사람들과 어울리는 것을 좋아합니다."
    },

    "ISTP": {
        "pokemon": "루카리오",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/448.png",
        "personality": "냉철한 판단력과 뛰어난 문제 해결 능력을 가졌습니다."
    },

    "ISFP": {
        "pokemon": "나인테일",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/038.png",
        "personality": "우아하고 감성적이며 자신만의 개성이 뚜렷합니다."
    },

    "ESTP": {
        "pokemon": "괴력몬",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/068.png",
        "personality": "행동력이 뛰어나고 모험을 즐깁니다."
    },

    "ESFP": {
        "pokemon": "파이리",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png",
        "personality": "열정적이고 에너지가 넘칩니다. 주변을 즐겁게 만드는 매력이 있습니다."
    }
}

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    list(pokemon_data.keys())
)

if mbti:
    data = pokemon_data[mbti]

    st.markdown("---")

    st.subheader(f"🐾 {mbti}와 가장 닮은 포켓몬")

    st.image(
        data["image"],
        width=250
    )

    st.success(f"추천 포켓몬 : {data['pokemon']}")

    st.write("### ✨ 성격 특징")
    st.write(data["personality"])

    st.balloons()
