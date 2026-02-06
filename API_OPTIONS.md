# 🔄 다른 API로 변경하기 가이드

이 문서는 `main.py`를 수정하여 다른 API를 사용하는 방법을 안내합니다.

## 📋 추천 API 목록 (open-apis-korea 기준)

### 1. 🐕 강아지 사진 API (RandomDog)
- **URL**: `https://random.dog/woof.json`
- **API Key**: 불필요
- **설명**: 무작위 강아지 사진

**코드 예시:**
```python
def get_random_dog_image():
    url = "https://random.dog/woof.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("url", "")
```

---

### 2. 🦊 여우 사진 API (RandomFox)
- **URL**: `https://randomfox.ca/floof/`
- **API Key**: 불필요
- **설명**: 무작위 여우 사진

**코드 예시:**
```python
def get_random_fox_image():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("image", "")
```

---

### 3. 💬 명언 API (Advice Slip)
- **URL**: `https://api.adviceslip.com/advice`
- **API Key**: 불필요
- **설명**: 무작위 조언/명언

**코드 예시:**
```python
def get_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("slip", {}).get("advice", "")
```

**README 업데이트 함수 수정:**
```python
def update_readme(advice_text):
    # ... (기존 코드)
    new_content = f"""
> {advice_text}

**업데이트 시간:** {today}
"""
    # ... (나머지 코드)
```

---

### 4. 💰 코인 시세 API (CoinGecko)
- **URL**: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=krw`
- **API Key**: 불필요
- **설명**: 비트코인 가격 (원화)

**코드 예시:**
```python
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "krw"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    price = data.get("bitcoin", {}).get("krw", 0)
    return f"{price:,.0f}원"
```

---

### 5. 🌤️ 날씨 API (OpenWeatherMap)
- **URL**: `https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&lang=kr`
- **API Key**: 필요 (무료 발급 가능)
- **설명**: 서울 날씨 정보

**코드 예시:**
```python
import os

def get_weather():
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("WEATHER_API_KEY 환경변수가 설정되지 않았습니다.")
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Seoul",
        "appid": api_key,
        "lang": "kr",
        "units": "metric"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"서울: {temp}°C, {desc}"
```

**GitHub Secrets 설정 필요:**
- 저장소 Settings → Secrets → New repository secret
- Name: `WEATHER_API_KEY`
- Value: 발급받은 API Key

---

### 6. 📰 뉴스 헤드라인 API (NewsAPI)
- **URL**: `https://newsapi.org/v2/top-headlines?country=kr&apiKey={API_KEY}`
- **API Key**: 필요 (무료 발급 가능)
- **설명**: 한국 뉴스 헤드라인

**코드 예시:**
```python
import os

def get_news_headline():
    api_key = os.environ.get("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY 환경변수가 설정되지 않았습니다.")
    
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "kr",
        "apiKey": api_key
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    if data.get("articles"):
        article = data["articles"][0]
        title = article.get("title", "")
        return title
    return "뉴스를 가져올 수 없습니다."
```

---

### 7. 🎭 농담 API (JokeAPI)
- **URL**: `https://v2.jokeapi.dev/joke/Any?lang=ko&type=single`
- **API Key**: 불필요
- **설명**: 한국어 농담

**코드 예시:**
```python
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "lang": "ko",
        "type": "single"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("joke", "")
```

---

## 🔧 변경 방법

1. **`main.py` 파일 열기**
2. **`get_random_cat_image()` 함수를 원하는 API 함수로 교체**
3. **`update_readme()` 함수의 `new_content` 부분을 원하는 형식으로 수정**
4. **API Key가 필요한 경우 GitHub Secrets에 등록**

## 📝 예시: 강아지 사진으로 변경하기

### 1. `main.py` 수정

```python
# 함수 이름 변경
def get_random_dog_image():  # get_random_cat_image() → get_random_dog_image()
    url = "https://random.dog/woof.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("url", "")

# main() 함수 수정
def main():
    print("🐕 오늘의 강아지 사진을 가져오는 중...")
    dog_image_url = get_random_dog_image()  # 함수 호출 변경
    update_readme(dog_image_url)  # update_readme 함수도 수정 필요
```

### 2. `update_readme()` 함수 수정

```python
def update_readme(dog_image_url):
    # ... (기존 코드)
    new_content = f"""
![오늘의 강아지 🐕]({dog_image_url})

**업데이트 시간:** {today}
"""
    # ... (나머지 코드)
```

### 3. `README.md` 마커 수정

```markdown
<!-- DOG_START -->
<!-- DOG_END -->
```

### 4. `main.py`의 패턴도 수정

```python
pattern = r'(<!--\s*DOG_START\s-->)(.*?)(<!--\s*DOG_END\s-->)'
```

---

## 💡 팁

- **API Key가 필요한 경우**: GitHub Actions에서 환경변수로 설정해야 합니다.
- **에러 처리**: API가 실패할 경우를 대비해 try-except를 사용하세요.
- **타임아웃 설정**: `timeout=10`으로 설정하여 무한 대기를 방지하세요.

---

더 많은 API는 [open-apis-korea](https://github.com/dl0312/open-apis-korea)를 참고하세요!
