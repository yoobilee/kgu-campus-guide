# 🎓 KGU Campus Guide

> 경기대학교 재학생을 위한 캠퍼스 통합 정보 포털 웹 서비스

**캡스톤 디자인 심화** 과목 팀 프로젝트 (2023)

---

## 📌 프로젝트 소개

교내·교외의 흩어진 정보를 한 곳에서 확인할 수 있는 **경기대학교 캠퍼스 가이드 웹 서비스**입니다.  
재학생이 자주 필요로 하는 시설, 식당, 카페, 동아리, 학사 정보를 통합하여 제공합니다.

---

## ✨ 주요 기능

| 카테고리 | 기능 |
|---|---|
| 🍽️ **교내 시설** | 학생 식당, 카페, 편의시설 정보 조회 |
| ☕ **교외 음식점/카페** | 정문·후문 주변 식당 및 카페 안내 |
| 🎵 **동아리** | 음악, 운동, 소프트웨어 등 카테고리별 동아리 정보 |
| 📚 **강의실 안내** | 강의 시설 위치 및 정보 |
| 🎓 **학사 정보** | 복수전공/부전공 신청 안내, 편입학 정보 |
| 🔍 **검색** | 키워드 기반 통합 검색 |
| 👤 **회원 시스템** | 회원가입 / 로그인 / 로그아웃 |

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

---

## 📁 프로젝트 구조

```
Capstone_Project/
├── accounts/          # 회원가입 / 로그인
├── dbapp/             # 메인 앱 (시설, 동아리, 학사 정보)
│   ├── models.py      # Facility, Club, Multimajor, Scholarship, Post
│   ├── views.py       # 각 페이지 뷰 로직
│   ├── urls.py        # URL 라우팅
│   ├── templates/     # HTML 템플릿
│   └── static/        # CSS, JS, 이미지 리소스
├── search/            # 통합 검색 기능
├── database_project/  # Django 프로젝트 설정
└── manage.py
```

---

## 🚀 실행 방법

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 3. 서버 실행
python manage.py runserver
```

---

## 📄 주요 페이지

- `/` — 메인 홈
- `/facility` — 교내 시설 목록
- `/facility_cafeteria` — 학생 식당
- `/facility_beverage` — 카페·음료
- `/club` — 동아리 목록
- `/outside` — 교외 음식점/카페
- `/graduate` — 편입학 정보
- `/major` — 복수전공/부전공 안내

---

## 🧑‍💻 개발 정보

- **과목:** 캡스톤 디자인 심화
- **개발 기간:** 2023.01 ~ 2023.06
- **팀 구성:** 5인 팀 프로젝트