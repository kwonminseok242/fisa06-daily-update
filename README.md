# 🐱 오늘의 고양이

매일 자동으로 새로운 고양이 사진을 가져와서 README.md를 업데이트하는 프로젝트입니다.

## 📋 프로젝트 소개

이 프로젝트는 GitHub Actions를 사용하여 매일 자동으로 고양이 API에서 고양이 사진을 가져와서 README.md 파일을 업데이트합니다.

- **사용 API**: [The Cat API](https://thecatapi.com/)
- **자동화**: GitHub Actions (매일 한국 시간 오전 8시 실행)
- **언어**: Python 3.x

## 🖼️ 오늘의 고양이

<!-- CAT_START -->
<div align="center">

![오늘의 고양이 🐱](https://cdn2.thecatapi.com/images/9gg.jpg)

**업데이트 시간:** 2026년 03월 15일

</div>
<!-- CAT_END -->

## 🚀 사용 방법

### 1. 로컬에서 테스트하기

```bash
# 저장소 클론
git clone <your-repo-url>
cd fisa06-daily-update

# 의존성 설치
pip install -r requirements.txt

# 스크립트 실행
python main.py
```

### 2. GitHub Actions 설정

이 프로젝트는 GitHub Actions를 사용하므로 별도의 API Key 설정이 필요 없습니다.

1. 이 저장소를 GitHub에 푸시합니다.
2. GitHub Actions가 자동으로 활성화됩니다.
3. 매일 한국 시간 오전 8시에 자동으로 실행됩니다.

### 3. 수동 실행

GitHub 저장소의 **Actions** 탭에서 **"Daily Cat Image Update"** 워크플로우를 선택하고 **"Run workflow"** 버튼을 클릭하면 수동으로 실행할 수 있습니다.

## 📁 프로젝트 구조

```
fisa06-daily-update/
├── .github/
│   └── workflows/
│       └── daily_update.yml    # GitHub Actions 워크플로우 설정
├── main.py                      # 메인 스크립트 (고양이 사진 가져오기 및 README 업데이트)
├── requirements.txt             # Python 의존성 패키지
└── README.md                    # 이 파일 (자동 업데이트됨)
```

## 🔧 주요 기능

- ✅ **자동화**: GitHub Actions를 통한 매일 자동 업데이트
- ✅ **무료 API**: API Key 없이 사용 가능한 고양이 API
- ✅ **간단한 구조**: 초보자도 이해하기 쉬운 코드
- ✅ **에러 처리**: API 오류 시 적절한 에러 메시지 출력
- ✅ **Fallback**: 여러 API를 순차적으로 시도하여 안정성 확보

## 📝 코드 설명

### main.py

- `get_random_cat_image()`: 여러 고양이 API를 순차적으로 시도하여 고양이 사진 URL을 가져옵니다.
- `update_readme()`: README.md 파일의 마커(`<!-- CAT_START -->
<div align="center">

![오늘의 고양이 🐱](https://cdn2.thecatapi.com/images/9gg.jpg)

**업데이트 시간:** 2026년 03월 15일

</div>
<!-- CAT_END -->`) 사이 내용을 새로운 사진으로 교체합니다.

### daily_update.yml

- **스케줄**: 매일 UTC 23:00 (한국 시간 오전 8시)에 실행
- **권한**: `contents: write` 권한으로 README.md 수정 및 커밋 가능
- **단계**: 코드 체크아웃 → Python 설정 → 의존성 설치 → 스크립트 실행 → 변경사항 커밋/푸시

## 🎨 다른 API로 변경하기

이 프로젝트를 다른 API로 변경하고 싶다면 `main.py`의 `get_random_cat_image()` 함수를 수정하면 됩니다.

더 자세한 내용은 `API_OPTIONS.md` 파일을 참고하세요.

### 예시: 강아지 사진 API로 변경

```python
def get_random_dog_image():
    url = "https://random.dog/woof.json"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data.get("url", "")
```

### 예시: 명언 API로 변경

```python
def get_quote():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data.get("slip", {}).get("advice", "")
```

## 📚 참고 자료

- [The Cat API](https://thecatapi.com/)
- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [open-apis-korea](https://github.com/dl0312/open-apis-korea) - 한국어 사용자를 위한 오픈 API 모음

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

---

**마지막 업데이트**: 2026년 02월 06일
