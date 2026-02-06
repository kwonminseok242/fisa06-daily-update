"""
매일 자동으로 고양이 사진을 가져와서 README.md를 업데이트하는 스크립트

사용 API: RandomCat API (https://aws.random.cat/meow)
- API Key 불필요
- 무료 사용 가능
- HTTPS 지원
"""

import os
import re
import requests
from datetime import datetime


def get_random_cat_image():
    """
    RandomCat API에서 무작위 고양이 사진 URL을 가져옵니다.
    
    Returns:
        str: 고양이 사진의 URL
    """
    try:
        # RandomCat API 엔드포인트 (API Key 불필요)
        url = "https://aws.random.cat/meow"
        
        # API 요청
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # HTTP 에러가 있으면 예외 발생
        
        # JSON 응답 파싱
        data = response.json()
        cat_image_url = data.get("file", "")
        
        if not cat_image_url:
            raise ValueError("이미지 URL을 찾을 수 없습니다.")
        
        return cat_image_url
    
    except requests.exceptions.RequestException as e:
        print(f"❌ API 요청 중 오류 발생: {e}")
        raise
    except Exception as e:
        print(f"❌ 이미지 URL 추출 중 오류 발생: {e}")
        raise


def update_readme(cat_image_url):
    """
    README.md 파일의 마커 사이 내용을 새로운 고양이 사진으로 교체합니다.
    
    Args:
        cat_image_url (str): 고양이 사진 URL
    """
    readme_path = "README.md"
    
    # README.md 파일 읽기
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ {readme_path} 파일을 찾을 수 없습니다.")
        raise
    
    # 마커 사이의 내용을 찾아서 교체
    # <!-- CAT_START --> 와 <!-- CAT_END --> 사이의 내용을 교체
    pattern = r'(<!--\s*CAT_START\s-->)(.*?)(<!--\s*CAT_END\s-->)'
    
    # 오늘 날짜 정보
    today = datetime.now().strftime("%Y년 %m월 %d일")
    
    # 새로운 내용 생성 (마크다운 이미지 형식)
    new_content = f"""
![오늘의 고양이 🐱]({cat_image_url})

**업데이트 시간:** {today}
"""
    
    # 패턴이 존재하는지 확인
    if not re.search(pattern, content, re.DOTALL):
        print("⚠️  README.md에 마커(<!-- CAT_START -->, <!-- CAT_END -->)를 찾을 수 없습니다.")
        print("   README.md 파일에 다음 마커를 추가해주세요:")
        print("   <!-- CAT_START -->")
        print("   <!-- CAT_END -->")
        raise ValueError("마커를 찾을 수 없습니다.")
    
    # 내용 교체
    updated_content = re.sub(
        pattern,
        r'\1' + new_content + r'\3',
        content,
        flags=re.DOTALL
    )
    
    # 파일에 쓰기
    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"✅ README.md가 성공적으로 업데이트되었습니다!")
        print(f"   이미지 URL: {cat_image_url}")
    except Exception as e:
        print(f"❌ 파일 쓰기 중 오류 발생: {e}")
        raise


def main():
    """
    메인 함수: 고양이 사진을 가져와서 README.md를 업데이트합니다.
    """
    print("🐱 오늘의 고양이 사진을 가져오는 중...")
    
    try:
        # 고양이 사진 URL 가져오기
        cat_image_url = get_random_cat_image()
        print(f"✅ 고양이 사진 URL 획득: {cat_image_url}")
        
        # README.md 업데이트
        update_readme(cat_image_url)
        
        print("🎉 작업이 완료되었습니다!")
        
    except Exception as e:
        print(f"❌ 작업 실패: {e}")
        exit(1)


if __name__ == "__main__":
    main()
