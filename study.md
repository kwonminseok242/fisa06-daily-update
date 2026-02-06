# 📚 GitHub Actions 자동화 프로젝트 학습 가이드

> **프로젝트명**: 매일 자동으로 고양이 사진을 가져와서 README.md를 업데이트하는 프로젝트  
> **학습 목표**: GitHub Actions를 활용한 자동화 워크플로우 구축 방법 이해

---

## 📋 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [기술 스택](#2-기술-스택)
3. [프로젝트 구조](#3-프로젝트-구조)
4. [코드 상세 분석](#4-코드-상세-분석)
5. [GitHub Actions 이해하기](#5-github-actions-이해하기)
6. [전체 프로세스 요약](#6-전체-프로세스-요약)
7. [핵심 학습 포인트](#7-핵심-학습-포인트)
8. [실습 과제](#8-실습-과제)
9. [추가 학습 자료](#9-추가-학습-자료)

---

## 1. 프로젝트 개요

### 1.1 프로젝트 목표

- **자동화**: 매일 자동으로 외부 API에서 데이터를 가져와서 README.md 파일을 업데이트
- **GitHub Actions 활용**: 코드를 직접 실행하지 않아도 GitHub에서 자동으로 실행되도록 설정
- **API 연동**: 무료 오픈 API를 활용하여 데이터 가져오기

### 1.2 왜 이 프로젝트를 만들었나?

1. **GitHub Actions 학습**: CI/CD 파이프라인 이해
2. **자동화 경험**: 반복 작업을 자동화하는 방법 학습
3. **API 활용**: REST API를 통한 데이터 가져오기 실습
4. **실전 프로젝트**: 포트폴리오에 추가할 수 있는 실제 작동하는 프로젝트

---

## 2. 기술 스택

### 2.1 사용 기술

| 기술 | 버전 | 용도 |
|------|------|------|
| Python | 3.11+ | 메인 스크립트 언어 |
| requests | 2.31.0+ | HTTP 요청 라이브러리 |
| GitHub Actions | 최신 | 자동화 워크플로우 |
| Markdown | - | README.md 포맷 |

### 2.2 선택 이유

- **Python**: 간단하고 직관적인 문법, 풍부한 라이브러리
- **requests**: HTTP 요청을 쉽게 처리할 수 있는 라이브러리
- **GitHub Actions**: 무료로 사용 가능, 설정이 간단함

---

## 3. 프로젝트 구조

```
fisa06-daily-update/
├── .github/
│   └── workflows/
│       └── daily_update.yml    # GitHub Actions 워크플로우 설정
├── main.py                      # 메인 스크립트
├── requirements.txt             # Python 패키지 의존성
├── README.md                    # 프로젝트 설명 (자동 업데이트됨)
├── API_OPTIONS.md              # 다른 API로 변경하는 가이드
├── SETUP_GUIDE.md              # 설정 가이드
├── study.md                    # 이 파일 (학습 가이드)
└── .gitignore                  # Git 제외 파일 목록
```

### 3.1 각 파일의 역할

- **`.github/workflows/daily_update.yml`**: GitHub Actions가 언제, 어떻게 실행할지 정의
- **`main.py`**: 실제 작업을 수행하는 Python 스크립트
- **`requirements.txt`**: 필요한 Python 패키지 목록
- **`README.md`**: 프로젝트 설명 및 자동 업데이트되는 고양이 사진

---

## 4. 코드 상세 분석

### 4.1 main.py 전체 구조

```python
"""
매일 자동으로 고양이 사진을 가져와서 README.md를 업데이트하는 스크립트
"""

import os
import re
import requests
from datetime import datetime

# 1. API에서 데이터 가져오기 함수
def get_random_cat_image():
    ...

# 2. README.md 업데이트 함수
def update_readme(cat_image_url):
    ...

# 3. 메인 실행 함수
def main():
    ...

if __name__ == "__main__":
    main()
```

### 4.2 get_random_cat_image() 함수 분석

#### 4.2.1 Fallback 패턴 이해

```python
def get_random_cat_image():
    # 여러 API 엔드포인트 목록 (순서대로 시도)
    api_endpoints = [
        {
            "name": "The Cat API",
            "url": "https://api.thecatapi.com/v1/images/search",
            "parser": lambda data: data[0].get("url", "") if data[0] else ""
        },
        # ... 더 많은 API
    ]
    
    # 각 API를 순차적으로 시도
    for api in api_endpoints:
        try:
            # API 요청 시도
            response = requests.get(api["url"], timeout=10)
            # 성공하면 반환
            return cat_image_url
        except:
            # 실패하면 다음 API 시도
            continue
```

**학습 포인트:**
- **Fallback 패턴**: 첫 번째 API가 실패하면 자동으로 다음 API를 시도
- **에러 처리**: try-except를 사용하여 안정성 확보
- **Lambda 함수**: 간단한 데이터 파싱에 사용

#### 4.2.2 requests 라이브러리 사용법

```python
import requests

# GET 요청 보내기
response = requests.get(url, timeout=10)

# HTTP 상태 코드 확인
response.raise_for_status()  # 4xx, 5xx 에러 시 예외 발생

# JSON 응답 파싱
data = response.json()
```

**학습 포인트:**
- `timeout=10`: 10초 후 요청 중단 (무한 대기 방지)
- `raise_for_status()`: HTTP 에러를 Python 예외로 변환
- `response.json()`: JSON 응답을 Python 딕셔너리로 변환

### 4.3 update_readme() 함수 분석

#### 4.3.1 정규표현식으로 마커 찾기

```python
import re

# 마커 패턴 정의
pattern = r'(<!--\s*CAT_START\s-->)(.*?)(<!--\s*CAT_END\s-->)'

# 패턴 매칭 (DOTALL 플래그로 여러 줄 매칭)
if not re.search(pattern, content, re.DOTALL):
    raise ValueError("마커를 찾을 수 없습니다.")

# 내용 교체
updated_content = re.sub(
    pattern,
    r'\1' + new_content + r'\3',  # \1, \3은 원래 마커 유지
    content,
    flags=re.DOTALL
)
```

**정규표현식 설명:**
- `(<!--\s*CAT_START\s-->)`: 첫 번째 그룹 (시작 마커)
  - `\s*`: 0개 이상의 공백 문자
- `(.*?)`: 두 번째 그룹 (교체할 내용)
  - `.*?`: 최소 매칭 (non-greedy)
- `(<!--\s*CAT_END\s-->)`: 세 번째 그룹 (끝 마커)

**학습 포인트:**
- **정규표현식**: 텍스트 패턴 매칭 및 교체
- **그룹 캡처**: `()`로 그룹을 만들어서 재사용
- **re.DOTALL**: `.`이 줄바꿈(`\n`)도 매칭하도록 설정

#### 4.3.2 파일 읽기/쓰기

```python
# 파일 읽기 (UTF-8 인코딩)
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 파일 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
```

**학습 포인트:**
- `with` 문: 파일을 자동으로 닫아줌 (리소스 관리)
- `encoding="utf-8"`: 한글이 깨지지 않도록 설정
- `"r"`: 읽기 모드, `"w"`: 쓰기 모드

### 4.4 main() 함수 분석

```python
def main():
    print("🐱 오늘의 고양이 사진을 가져오는 중...")
    
    try:
        # 1. API에서 데이터 가져오기
        cat_image_url = get_random_cat_image()
        
        # 2. README.md 업데이트
        update_readme(cat_image_url)
        
        print("🎉 작업이 완료되었습니다!")
        
    except Exception as e:
        print(f"❌ 작업 실패: {e}")
        exit(1)  # 에러 코드 1로 종료 (GitHub Actions가 실패로 인식)
```

**학습 포인트:**
- **에러 처리**: try-except로 예외 처리
- **exit(1)**: 프로그램을 에러 상태로 종료 (GitHub Actions가 실패로 인식)

---

## 5. GitHub Actions 이해하기

### 5.1 GitHub Actions란?

GitHub Actions는 GitHub 저장소에서 자동화된 워크플로우를 실행할 수 있는 CI/CD 플랫폼입니다.

**주요 특징:**
- 무료로 사용 가능 (Public 저장소는 무제한)
- YAML 파일로 설정 (간단함)
- 다양한 트리거 지원 (스케줄, 푸시, PR 등)

### 5.2 daily_update.yml 파일 분석

```yaml
name: Daily Cat Image Update  # 워크플로우 이름

# 워크플로우 실행 조건
on:
  schedule:
    - cron: '0 23 * * *'  # UTC 기준 매일 23:00 (한국 시간 오전 8시)
  workflow_dispatch:  # 수동 실행 가능

jobs:
  update-readme:
    runs-on: ubuntu-latest  # 실행 환경
    
    permissions:
      contents: write  # 파일 수정 권한 필요
    
    steps:
      # 1. 코드 체크아웃
      - name: Checkout repository
        uses: actions/checkout@v4
      
      # 2. Python 설정
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      # 3. 의존성 설치
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
      
      # 4. 스크립트 실행
      - name: Update README with cat image
        run: python main.py
      
      # 5. 변경사항 커밋 및 푸시
      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add README.md
          git diff --quiet && git diff --staged --quiet || \
            (git commit -m "🐱 오늘의 고양이 사진 업데이트 [$(date +'%Y-%m-%d')]" && \
             git push)
```

### 5.3 Cron 표현식 이해하기

Cron은 스케줄을 정의하는 표현식입니다.

**형식:** `분 시 일 월 요일`

```yaml
cron: '0 23 * * *'
```

**분해:**
- `0`: 분 (0분)
- `23`: 시 (23시, UTC)
- `*`: 일 (매일)
- `*`: 월 (매월)
- `*`: 요일 (매요일)

**예시:**
- `'0 0 * * *'` - 매일 UTC 00:00 (한국 시간 오전 9시)
- `'0 12 * * *'` - 매일 UTC 12:00 (한국 시간 오후 9시)
- `'0 0 * * 1'` - 매주 월요일 UTC 00:00
- `'0 */6 * * *'` - 6시간마다

**UTC와 한국 시간 변환:**
- 한국 시간 = UTC + 9시간
- 한국 시간 오전 8시 = UTC 23:00 (전날)

### 5.4 Steps 이해하기

각 step은 순차적으로 실행됩니다:

1. **Checkout**: 저장소 코드를 가져옴
2. **Set up Python**: Python 환경 설정
3. **Install dependencies**: 필요한 패키지 설치
4. **Run script**: 실제 작업 수행
5. **Commit and push**: 변경사항 커밋 및 푸시

### 5.5 Git 커밋 자동화

```bash
git config --local user.email "action@github.com"
git config --local user.name "GitHub Action"
git add README.md
git diff --quiet && git diff --staged --quiet || \
  (git commit -m "메시지" && git push)
```

**설명:**
- `git config`: 커밋 작성자 설정
- `git diff --quiet`: 변경사항이 없으면 true 반환
- `||`: 앞의 명령이 실패하면 뒤의 명령 실행
- 변경사항이 있을 때만 커밋 및 푸시

---

## 6. 전체 프로세스 요약

### 6.1 프로젝트 생성 과정

```
1. 프로젝트 폴더 생성
   └─> fisa06-daily-update/

2. Python 스크립트 작성
   └─> main.py (API 호출 + 파일 업데이트)

3. GitHub Actions 설정
   └─> .github/workflows/daily_update.yml

4. 의존성 파일 작성
   └─> requirements.txt

5. README 템플릿 작성
   └─> README.md (마커 포함)

6. 로컬 테스트
   └─> python main.py

7. GitHub에 업로드
   └─> git init, commit, push

8. GitHub Actions 활성화
   └─> 자동 실행 확인
```

### 6.2 실행 흐름도

```
[스케줄 트리거]
    ↓
[GitHub Actions 시작]
    ↓
[코드 체크아웃]
    ↓
[Python 환경 설정]
    ↓
[의존성 설치]
    ↓
[main.py 실행]
    ↓
[API 호출] → [고양이 사진 URL 획득]
    ↓
[README.md 읽기]
    ↓
[마커 사이 내용 교체]
    ↓
[README.md 쓰기]
    ↓
[변경사항 커밋]
    ↓
[GitHub에 푸시]
    ↓
[완료!]
```

---

## 7. 핵심 학습 포인트

### 7.1 Python 관련

#### ✅ requests 라이브러리
- HTTP 요청을 쉽게 처리
- `get()`, `post()` 메서드 사용
- `timeout` 설정으로 무한 대기 방지
- `raise_for_status()`로 에러 처리

#### ✅ 정규표현식 (re 모듈)
- 텍스트 패턴 매칭
- `re.search()`: 패턴 찾기
- `re.sub()`: 패턴 교체
- 그룹 캡처 `()` 활용

#### ✅ 파일 처리
- `with` 문으로 리소스 관리
- `encoding="utf-8"`로 한글 처리
- 읽기(`"r"`), 쓰기(`"w"`) 모드

#### ✅ 에러 처리
- `try-except`로 예외 처리
- `exit(1)`로 프로그램 종료 상태 전달

### 7.2 GitHub Actions 관련

#### ✅ YAML 문법
- 들여쓰기 중요 (스페이스 2개)
- `name`, `on`, `jobs`, `steps` 구조

#### ✅ Cron 스케줄링
- UTC 시간 기준
- 한국 시간 = UTC + 9시간

#### ✅ 권한 설정
- `permissions: contents: write` 필수
- 파일 수정 및 커밋을 위해 필요

#### ✅ Git 자동화
- `git config`로 사용자 설정
- 변경사항이 있을 때만 커밋

### 7.3 API 연동 관련

#### ✅ Fallback 패턴
- 여러 API를 순차적으로 시도
- 첫 번째 실패 시 자동으로 다음 API 시도
- 안정성 향상

#### ✅ 에러 처리
- 네트워크 오류 대비
- 타임아웃 설정
- 명확한 에러 메시지

---

## 8. 실습 과제

### 과제 1: 다른 API로 변경하기

**목표**: 고양이 사진 대신 다른 API를 사용하도록 수정

**예시:**
- 강아지 사진 API
- 명언 API
- 날씨 API

**힌트**: `API_OPTIONS.md` 파일 참고

---

### 과제 2: 실행 시간 변경하기

**목표**: 매일 오전 8시 대신 다른 시간에 실행되도록 변경

**예시:**
- 매일 오후 2시
- 매주 월요일 오전 9시
- 6시간마다

**힌트**: Cron 표현식 수정

---

### 과제 3: 여러 데이터 표시하기

**목표**: 고양이 사진뿐만 아니라 날씨, 명언 등 여러 데이터를 함께 표시

**예시:**
```markdown
![고양이 사진]
**오늘의 날씨**: 맑음, 15°C
**오늘의 명언**: "성공은 준비된 자에게 찾아온다"
```

---

### 과제 4: 에러 알림 추가하기

**목표**: 워크플로우가 실패했을 때 알림 받기

**힌트**: GitHub Actions의 `if: failure()` 조건 사용

---

## 9. 추가 학습 자료

### 9.1 공식 문서

- **GitHub Actions**: https://docs.github.com/en/actions
- **Python requests**: https://requests.readthedocs.io/
- **정규표현식**: https://docs.python.org/3/library/re.html

### 9.2 추천 학습 순서

1. **Python 기초** (파일 처리, 에러 처리)
2. **HTTP 요청** (requests 라이브러리)
3. **정규표현식** (텍스트 패턴 매칭)
4. **Git 기초** (커밋, 푸시)
5. **GitHub Actions** (워크플로우 설정)
6. **YAML 문법** (설정 파일 작성)

### 9.3 관련 프로젝트 아이디어

1. **코인 시세 자동 업데이트**: 매일 비트코인 가격 표시
2. **날씨 정보 자동 업데이트**: 매일 현재 날씨 표시
3. **GitHub 통계 자동 업데이트**: 매일 커밋 수, 스타 수 표시
4. **뉴스 헤드라인 자동 업데이트**: 매일 주요 뉴스 표시

---

## 10. 자주 묻는 질문 (FAQ)

### Q1: GitHub Actions가 실행되지 않아요

**A**: 저장소 Settings → Actions → General에서 Actions가 활성화되어 있는지 확인하세요.

### Q2: README.md가 업데이트되지 않아요

**A**: 
1. 마커(`<!-- CAT_START -->`, `<!-- CAT_END -->`)가 정확한지 확인
2. `permissions: contents: write`가 설정되어 있는지 확인
3. Actions 로그에서 에러 메시지 확인

### Q3: API가 실패해요

**A**: 
- 네트워크 연결 확인
- API 엔드포인트가 변경되었는지 확인
- Fallback API가 작동하는지 확인

### Q4: 로컬에서는 되는데 GitHub Actions에서 안 돼요

**A**:
- 파일 경로가 상대 경로인지 확인
- 인코딩 문제 확인 (`encoding="utf-8"`)
- Actions 로그에서 상세 에러 확인

---

## 11. 마무리

이 프로젝트를 통해 배운 것:

✅ **자동화**: 반복 작업을 자동화하는 방법  
✅ **API 연동**: 외부 API를 활용하는 방법  
✅ **GitHub Actions**: CI/CD 파이프라인 구축  
✅ **에러 처리**: 안정적인 코드 작성  
✅ **실전 프로젝트**: 포트폴리오에 추가 가능한 프로젝트

**다음 단계:**
- 다른 API로 확장해보기
- 더 복잡한 자동화 프로젝트 만들기
- 다른 사람들과 프로젝트 공유하기

---

**작성일**: 2026년 02월 06일  
**버전**: 1.0  
**작성자**: 학습 가이드
