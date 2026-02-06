# 🚀 프로젝트 설정 가이드

이 가이드는 프로젝트를 GitHub에 업로드하고 자동화를 설정하는 방법을 단계별로 안내합니다.

## ✅ 1단계: 로컬 테스트 완료

이미 완료되었습니다! 스크립트가 정상적으로 작동하는 것을 확인했습니다.

```bash
python3 main.py
# ✅ 성공적으로 실행됨
```

---

## 📤 2단계: GitHub 저장소 생성 및 업로드

### 2-1. GitHub에서 새 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단의 **"+"** 버튼 클릭 → **"New repository"** 선택
3. 저장소 이름 입력 (예: `fisa06-daily-update`)
4. **Public** 또는 **Private** 선택
5. **"Create repository"** 클릭
   - ⚠️ **"Initialize this repository with a README"**는 체크하지 마세요! (이미 README.md가 있으므로)

### 2-2. 로컬에서 Git 초기화 및 업로드

터미널에서 다음 명령어를 실행하세요:

```bash
# 프로젝트 폴더로 이동
cd /Users/kwonminseok/Desktop/woori_fisa/fisa06-daily-update

# Git 초기화
git init

# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: Daily cat image updater"

# GitHub 저장소와 연결 (YOUR_USERNAME과 YOUR_REPO_NAME을 실제 값으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 브랜치 이름을 main으로 설정
git branch -M main

# GitHub에 푸시
git push -u origin main
```

**예시:**
```bash
git remote add origin https://github.com/kwonminseok/fisa06-daily-update.git
```

---

## ⚙️ 3단계: GitHub Actions 확인

### 3-1. Actions 탭 확인

1. GitHub 저장소 페이지로 이동
2. 상단 메뉴에서 **"Actions"** 탭 클릭
3. 왼쪽 사이드바에서 **"Daily Cat Image Update"** 워크플로우가 보이는지 확인

### 3-2. 수동 실행 테스트

1. **"Actions"** 탭에서 **"Daily Cat Image Update"** 클릭
2. 우측 상단의 **"Run workflow"** 버튼 클릭
3. **"Run workflow"** 드롭다운에서 **"Run workflow"** 선택
4. 약 1-2분 후 결과 확인:
   - ✅ 초록색 체크 표시 = 성공!
   - ❌ 빨간색 X 표시 = 실패 (로그 확인 필요)

### 3-3. 자동 실행 확인

- 워크플로우는 **매일 한국 시간 오전 8시 (UTC 23:00)**에 자동으로 실행됩니다
- 첫 실행은 다음 날 아침에 자동으로 실행됩니다

---

## 🔍 4단계: 결과 확인

### 4-1. README.md 확인

1. 저장소의 메인 페이지로 이동
2. **README.md** 파일을 확인
3. **"오늘의 고양이"** 섹션에 새로운 고양이 사진이 표시되는지 확인

### 4-2. 커밋 히스토리 확인

1. 저장소 메인 페이지에서 **커밋 히스토리** 확인
2. 매일 **"🐱 오늘의 고양이 사진 업데이트 [날짜]"** 형식의 커밋이 자동으로 생성됩니다

---

## 🛠️ 5단계: 문제 해결

### 문제 1: GitHub Actions가 실행되지 않음

**해결 방법:**
- 저장소 **Settings** → **Actions** → **General**에서 Actions가 활성화되어 있는지 확인
- **"Allow all actions and reusable workflows"** 선택

### 문제 2: 워크플로우가 실패함

**해결 방법:**
1. **Actions** 탭에서 실패한 워크플로우 클릭
2. 실패한 작업(job) 클릭
3. 로그를 확인하여 오류 메시지 확인
4. 일반적인 원인:
   - 네트워크 오류 (일시적 문제일 수 있음)
   - 파일 경로 오류
   - 권한 문제

### 문제 3: README.md가 업데이트되지 않음

**해결 방법:**
- `README.md` 파일에 마커(`<!-- CAT_START -->`, `<!-- CAT_END -->`)가 정확히 있는지 확인
- 마커 사이에 공백이나 오타가 없는지 확인

---

## 📝 6단계: 커스터마이징 (선택사항)

### 다른 API로 변경하기

`API_OPTIONS.md` 파일을 참고하여 다른 API로 변경할 수 있습니다.

### 실행 시간 변경하기

`.github/workflows/daily_update.yml` 파일을 열고 다음 부분을 수정:

```yaml
schedule:
  - cron: '0 23 * * *'  # UTC 기준 매일 23:00 (한국 시간 오전 8시)
```

**Cron 표현식 예시:**
- `'0 0 * * *'` - 매일 UTC 00:00 (한국 시간 오전 9시)
- `'0 12 * * *'` - 매일 UTC 12:00 (한국 시간 오후 9시)
- `'0 0 * * 1'` - 매주 월요일 UTC 00:00

---

## 🎉 완료!

이제 프로젝트가 완전히 설정되었습니다!

- ✅ 로컬 테스트 완료
- ✅ GitHub에 업로드 완료
- ✅ GitHub Actions 자동화 설정 완료
- ✅ 매일 자동으로 고양이 사진이 업데이트됩니다!

---

## 📞 추가 도움이 필요하신가요?

- GitHub Actions 문서: https://docs.github.com/en/actions
- 프로젝트 이슈: GitHub 저장소의 Issues 탭에서 질문하세요
