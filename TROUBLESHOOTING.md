# 🔧 문제 해결 가이드

GitHub에서 고양이 사진이 표시되지 않는 문제를 해결하는 방법입니다.

## 🔍 문제 진단

### 1. 이미지가 GitHub에서 안 보이는 경우

#### 원인 1: 이미지 URL이 유효하지 않음

**확인 방법:**
1. README.md 파일을 열어서 이미지 URL 확인
2. 브라우저에서 이미지 URL을 직접 열어보기
3. URL이 `https://`로 시작하는지 확인

**해결 방법:**
- 이미지 URL을 브라우저에서 열어서 확인
- URL이 작동하지 않으면 API가 변경되었을 수 있음
- `main.py`의 API 엔드포인트 확인

#### 원인 2: GitHub Actions가 실행되지 않음

**확인 방법:**
1. GitHub 저장소의 **Actions** 탭 확인
2. 워크플로우가 실행되었는지 확인
3. 실행 로그에서 에러 메시지 확인

**해결 방법:**
- Actions 탭에서 "Run workflow" 버튼으로 수동 실행
- 실행 로그에서 에러 확인
- `permissions: contents: write` 설정 확인

#### 원인 3: 마커가 잘못됨

**확인 방법:**
README.md 파일에 다음 마커가 정확히 있는지 확인:

```markdown
<!-- CAT_START -->
<!-- CAT_END -->
```

**해결 방법:**
- 마커가 정확한지 확인 (대소문자, 공백)
- 마커 사이에 다른 내용이 없는지 확인

#### 원인 4: 이미지가 너무 큼

**확인 방법:**
- 이미지 URL을 직접 열어서 크기 확인
- GitHub의 마크다운 렌더링 제한 확인

**해결 방법:**
- 이미지 크기를 제한하는 코드 추가 (추후 개선 예정)

---

## 🛠️ 해결 단계

### 단계 1: 로컬에서 테스트

```bash
cd fisa06-daily-update
python3 main.py
```

**예상 결과:**
```
🐱 오늘의 고양이 사진을 가져오는 중...
   시도 중: The Cat API...
   ✅ The Cat API에서 이미지 획득 성공!
✅ 고양이 사진 URL 획득: https://...
✅ README.md가 성공적으로 업데이트되었습니다!
🎉 작업이 완료되었습니다!
```

**문제가 있으면:**
- 네트워크 연결 확인
- Python 버전 확인 (3.11+)
- `requests` 라이브러리 설치 확인

### 단계 2: README.md 확인

로컬에서 업데이트된 README.md 파일 확인:

```bash
cat README.md | grep -A 5 "CAT_START"
```

**예상 결과:**
```markdown
<!-- CAT_START -->
![오늘의 고양이 🐱](https://cdn2.thecatapi.com/images/xxx.jpg)

**업데이트 시간:** 2026년 02월 06일
<!-- CAT_END -->
```

### 단계 3: GitHub에 푸시

```bash
git add README.md main.py .github/workflows/daily_update.yml
git commit -m "Fix: 이미지 표시 문제 해결"
git push
```

### 단계 4: GitHub Actions 수동 실행

1. GitHub 저장소의 **Actions** 탭 클릭
2. **"Daily Cat Image Update"** 워크플로우 선택
3. **"Run workflow"** 버튼 클릭
4. 약 1-2분 후 결과 확인

### 단계 5: 결과 확인

1. 저장소 메인 페이지에서 README.md 확인
2. **"오늘의 고양이"** 섹션에 이미지가 표시되는지 확인
3. 이미지가 안 보이면 이미지 URL을 직접 클릭해서 확인

---

## 🐛 일반적인 오류 및 해결 방법

### 오류 1: "마커를 찾을 수 없습니다"

**원인:** README.md에 마커가 없거나 잘못됨

**해결:**
```markdown
<!-- CAT_START -->
<!-- CAT_END -->
```
마커를 정확히 추가하세요.

---

### 오류 2: "모든 고양이 API에서 이미지를 가져올 수 없습니다"

**원인:** 네트워크 문제 또는 API 엔드포인트 변경

**해결:**
1. 네트워크 연결 확인
2. API 엔드포인트가 변경되었는지 확인
3. `main.py`의 API 목록 확인 및 업데이트

---

### 오류 3: GitHub Actions가 실패함

**원인:** 권한 문제 또는 스크립트 오류

**해결:**
1. Actions 로그 확인
2. `permissions: contents: write` 설정 확인
3. Python 버전 확인 (3.11)

---

### 오류 4: 이미지가 GitHub에서 깨짐

**원인:** 이미지 URL이 유효하지 않거나 접근 불가

**해결:**
1. 이미지 URL을 브라우저에서 직접 열어보기
2. URL이 `https://`로 시작하는지 확인
3. CORS 문제일 수 있음 (일부 이미지 서버는 GitHub에서 직접 접근 불가)

---

## 🔄 이미지가 여전히 안 보이는 경우

### 대안 1: 이미지 URL 직접 확인

README.md에 있는 이미지 URL을 복사해서 브라우저에서 직접 열어보세요.

### 대안 2: 다른 이미지 형식 사용

일부 이미지 서버는 GitHub에서 직접 접근이 제한될 수 있습니다. 
이 경우 다른 API를 사용하도록 변경하세요.

### 대안 3: GitHub Actions 로그 확인

1. **Actions** 탭 → 실패한 워크플로우 클릭
2. 로그에서 에러 메시지 확인
3. 에러 메시지를 기반으로 문제 해결

---

## 📞 추가 도움

문제가 계속되면:

1. GitHub Actions 로그를 확인하세요
2. 로컬에서 `python3 main.py` 실행 결과를 확인하세요
3. 이미지 URL을 브라우저에서 직접 열어보세요
4. GitHub 저장소의 Issues 탭에서 질문하세요

---

**마지막 업데이트**: 2026년 02월 06일
