import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천기",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 MBTI 진로 추천기")
st.markdown("### 😎 내 MBTI에 어울리는 진로를 알아보자!")

mbti_data = {
    "ISTJ": {
        "nickname": "📋 청렴한 논리주의자",
        "careers": [
            {
                "job": "📊 회계사",
                "major": "회계학과, 경영학과",
                "personality": "꼼꼼하고 책임감이 강하며 계획적으로 일하는 사람"
            },
            {
                "job": "⚖️ 공무원",
                "major": "행정학과, 법학과",
                "personality": "성실하고 안정적인 환경을 선호하는 사람"
            }
        ]
    },
    "ISFJ": {
        "nickname": "💖 용감한 수호자",
        "careers": [
            {
                "job": "🏥 간호사",
                "major": "간호학과",
                "personality": "배려심이 많고 사람을 돕는 것을 좋아하는 사람"
            },
            {
                "job": "👩‍🏫 초등교사",
                "major": "초등교육과",
                "personality": "인내심이 있고 따뜻한 마음을 가진 사람"
            }
        ]
    },
    "INFJ": {
        "nickname": "🌱 선의의 옹호자",
        "careers": [
            {
                "job": "🧠 상담사",
                "major": "심리학과, 상담학과",
                "personality": "공감 능력이 뛰어나고 사람의 마음에 관심이 많은 사람"
            },
            {
                "job": "✍️ 작가",
                "major": "문예창작과, 국어국문학과",
                "personality": "상상력이 풍부하고 깊이 있는 생각을 즐기는 사람"
            }
        ]
    },
    "INTJ": {
        "nickname": "♟️ 전략가",
        "careers": [
            {
                "job": "💻 AI 개발자",
                "major": "인공지능학과, 컴퓨터공학과",
                "personality": "분석적이고 문제 해결을 즐기는 사람"
            },
            {
                "job": "📈 경영 컨설턴트",
                "major": "경영학과, 경제학과",
                "personality": "전략을 세우고 큰 그림을 보는 것을 좋아하는 사람"
            }
        ]
    },
    "ISTP": {
        "nickname": "🔧 만능 재주꾼",
        "careers": [
            {
                "job": "🛠️ 기계공학자",
                "major": "기계공학과",
                "personality": "손으로 만들고 실험하는 것을 좋아하는 사람"
            },
            {
                "job": "✈️ 항공정비사",
                "major": "항공정비학과",
                "personality": "기계에 관심이 많고 집중력이 좋은 사람"
            }
        ]
    },
    "ISFP": {
        "nickname": "🎨 호기심 많은 예술가",
        "careers": [
            {
                "job": "🎨 디자이너",
                "major": "시각디자인과, 산업디자인과",
                "personality": "창의적이고 감각적인 사람"
            },
            {
                "job": "📷 사진작가",
                "major": "사진영상학과",
                "personality": "관찰력이 좋고 예술 감각이 뛰어난 사람"
            }
        ]
    },
    "INFP": {
        "nickname": "🌈 열정적인 중재자",
        "careers": [
            {
                "job": "🎬 콘텐츠 크리에이터",
                "major": "미디어학과, 영상학과",
                "personality": "자기표현을 좋아하고 아이디어가 풍부한 사람"
            },
            {
                "job": "💗 심리상담사",
                "major": "심리학과",
                "personality": "공감 능력이 높고 사람의 성장을 돕고 싶은 사람"
            }
        ]
    },
    "INTP": {
        "nickname": "🧐 논리적인 사색가",
        "careers": [
            {
                "job": "🔬 연구원",
                "major": "물리학과, 화학과",
                "personality": "탐구심이 강하고 새로운 지식을 좋아하는 사람"
            },
            {
                "job": "💻 소프트웨어 개발자",
                "major": "컴퓨터공학과",
                "personality": "논리적으로 문제를 해결하는 것을 좋아하는 사람"
            }
        ]
    },
    "ESTP": {
        "nickname": "🏃 모험을 즐기는 사업가",
        "careers": [
            {
                "job": "📢 마케터",
                "major": "광고홍보학과, 경영학과",
                "personality": "활동적이고 사람들과 소통하는 것을 좋아하는 사람"
            },
            {
                "job": "💼 영업 전문가",
                "major": "경영학과",
                "personality": "도전 정신이 강하고 설득력이 좋은 사람"
            }
        ]
    },
    "ESFP": {
        "nickname": "🎉 자유로운 연예인",
        "careers": [
            {
                "job": "🎤 연예인",
                "major": "공연예술학과",
                "personality": "에너지가 넘치고 사람들 앞에 서는 것을 좋아하는 사람"
            },
            {
                "job": "🎪 이벤트 기획자",
                "major": "관광경영학과",
                "personality": "즐거운 분위기를 만드는 것을 좋아하는 사람"
            }
        ]
    },
    "ENFP": {
        "nickname": "🔥 재기발랄한 활동가",
        "careers": [
            {
                "job": "📺 PD",
                "major": "방송영상학과",
                "personality": "창의적인 아이디어가 많고 협업을 좋아하는 사람"
            },
            {
                "job": "🚀 창업가",
                "major": "경영학과, 창업학과",
                "personality": "새로운 도전을 즐기는 사람"
            }
        ]
    },
    "ENTP": {
        "nickname": "💡 변론가",
        "careers": [
            {
                "job": "⚖️ 변호사",
                "major": "법학과",
                "personality": "토론과 설득을 좋아하는 사람"
            },
            {
                "job": "📈 기획자",
                "major": "경영학과",
                "personality": "새로운 아이디어를 내는 것을 좋아하는 사람"
            }
        ]
    },
    "ESTJ": {
        "nickname": "👑 엄격한 관리자",
        "careers": [
            {
                "job": "🏢 기업 관리자",
                "major": "경영학과",
                "personality": "리더십이 있고 체계적인 사람"
            },
            {
                "job": "👮 경찰관",
                "major": "경찰행정학과",
                "personality": "정의감과 책임감이 강한 사람"
            }
        ]
    },
    "ESFJ": {
        "nickname": "🌷 사교적인 외교관",
        "careers": [
            {
                "job": "👩‍🏫 교사",
                "major": "교육학과",
                "personality": "친절하고 사람들과 협력하는 것을 좋아하는 사람"
            },
            {
                "job": "🏨 호텔리어",
                "major": "호텔관광학과",
                "personality": "서비스 정신이 뛰어난 사람"
            }
        ]
    },
    "ENFJ": {
        "nickname": "🌍 정의로운 사회운동가",
        "careers": [
            {
                "job": "🎓 진로상담교사",
                "major": "교육학과, 상담학과",
                "personality": "사람의 성장을 돕는 것을 좋아하는 사람"
            },
            {
                "job": "❤️ NGO 활동가",
                "major": "사회복지학과, 국제학과",
                "personality": "사회 문제 해결에 관심이 많은 사람"
            }
        ]
    },
    "ENTJ": {
        "nickname": "🎯 대담한 통솔자",
        "careers": [
            {
                "job": "🏢 CEO",
                "major": "경영학과",
                "personality": "목표 지향적이고 추진력이 강한 사람"
            },
            {
                "job": "📊 투자 분석가",
                "major": "경제학과, 금융학과",
                "personality": "분석력과 결단력이 뛰어난 사람"
            }
        ]
    }
}

selected_mbti = st.selectbox(
    "👇 MBTI를 선택해 보세요!",
    list(mbti_data.keys())
)

if st.button("✨ 진로 추천 받기"):
    data = mbti_data[selected_mbti]

    st.success(f"당신의 유형은 {selected_mbti} {data['nickname']} 입니다!")

    st.markdown("---")
    st.subheader("🚀 추천 진로")

    for career in data["careers"]:
        st.markdown(f"""
### {career['job']}

📚 **추천 학과**
- {career['major']}

😎 **이런 성격이라면 잘 맞아요!**
- {career['personality']}
""")

    st.info(
        "💡 MBTI는 참고 자료일 뿐이야! "
        "가장 중요한 건 네가 좋아하는 것과 잘하는 것을 함께 찾는 거야 😊"
    )

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
