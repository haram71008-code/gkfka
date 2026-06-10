```python
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
        "personality": "전략적이고 독립적이며 목표 지향적입니다."
    },

    "INTP": {
        "pokemon": "메타몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
        "personality": "호기심이 많고 창의적인 아이디어를 좋아합니다."
    },

    "ENTJ": {
        "pokemon": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "personality": "리더십이 강하고 추진력이 뛰어납니다."
    },

    "ENTP": {
        "pokemon": "고라파덕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png",
        "personality": "엉뚱하지만 창의적인 생각이 많습니다."
    },

    "INFJ": {
        "pokemon": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "personality": "통찰력이 깊고 배려심이 많습니다."
    },

    "INFP": {
        "pokemon": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "personality": "상상력이 풍부하고 따뜻한 마음을 가졌습니다."
    },

    "ENFJ": {
        "pokemon": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "personality": "사람들과 잘 어울리고 긍정적인 에너지를 줍니다."
    },

    "ENFP": {
        "pokemon": "토게피",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
        "personality": "밝고 활발하며 새로운 경험을 좋아합니다."
    },

    "ISTJ": {
        "pokemon": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "personality": "성실하고 책임감이 강합니다."
    },

    "ISFJ": {
        "pokemon": "해피너스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "personality": "친절하고 남을 잘 배려합니다."
    },

    "ESTJ": {
        "pokemon": "보스로라",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/306.png",
        "personality": "체계적이고 조직력이 뛰어납니다."
    },

    "ESFJ": {
        "pokemon": "푸린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "personality": "사교적이고 다정다감합니다."
    },

    "ISTP": {
        "pokemon": "루카리오",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
        "personality": "실용적이며 문제 해결 능력이 뛰어납니다."
    },

    "ISFP": {
        "pokemon": "나인테일",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png",
        "personality": "감성이 풍부하고 예술적 감각이 뛰어납니다."
    },

    "ESTP": {
        "pokemon": "괴력몬",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
        "personality": "에너지가 넘치고 행동력이 강합니다."
    },

    "ESFP": {
        "pokemon": "파이리",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
        "personality": "열정적이고 주변을 즐겁게 만드는 매력이 있습니다."
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
        width=150
    )

    st.success(f"추천 포켓몬 : {data['pokemon']}")

    st.write("### ✨ 성격 특징")
    st.write(data["personality"])
```
