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
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "personality": "강력한 카리스마와 전략성을 가진 포켓몬입니다."
    },

    "INTP": {
        "pokemon": "메타몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
        "personality": "창의적이고 호기심이 많습니다."
    },

    "ENTJ": {
        "pokemon": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "personality": "자신감 있고 리더십이 강합니다."
    },

    "ENTP": {
        "pokemon": "고라파덕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png",
        "personality": "엉뚱하지만 창의적인 아이디어가 많습니다."
    },

    "INFJ": {
        "pokemon": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "personality": "신비롭고 통찰력이 깊습니다."
    },

    "INFP": {
        "pokemon": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "personality": "따뜻하고 상상력이 풍부합니다."
    },

    "ENFJ": {
        "pokemon": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "personality": "친절하고 밝은 에너지를 가지고 있습니다."
    },

    "ENFP": {
        "pokemon": "토게피",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
        "personality": "호기심이 많고 활발합니다."
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
        width=200
    )

    st.success(f"추천 포켓몬 : {data['pokemon']}")

    st.write("### ✨ 성격 특징")
    st.write(data["personality"])
    
