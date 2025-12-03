"""
환경 설정 모듈
-------------
프로젝트 전체에서 사용하는 경로(Path), 감정 리스트, 
상수 값들을 한곳에서 관리하는 파일입니다.
"""
import csv
import os

# 1. 파일들이 있는 현재 경로 확인
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. 합칠 CSV 파일들의 이름 리스트 (화면에 보이는 파일명 기준)
csv_files = [
    'data_anger.csv', 
    'data_fear.csv', 
    'data_peace.csv', 
    'data_sad.csv', 
    'data_tired.csv',
    # 나머지 하나 파일명도 여기에 추가해주세요 (예: 'data_joy.csv')
]

# 3. 모든 데이터를 담을 리스트 변수 선언
ALL_EMOTIONS = []

# 4. 파일들을 하나씩 읽어서 합치기
for filename in csv_files:
    file_path = os.path.join(BASE_DIR, filename)
    
    # 파일이 실제로 존재하는지 확인
    if os.path.exists(file_path):
        # 'utf-8-sig'는 엑셀/CSV 한글 깨짐을 방지하기 위함
        with open(file_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 각 행(row)을 리스트에 추가
                ALL_EMOTIONS.append(row)
    else:
        print(f"경고: {filename} 파일을 찾을 수 없습니다.")

# 확인용: 데이터가 잘 들어갔는지 개수 출력 (실행 시 확인 가능)
if __name__ == "__main__":
    print(f"총 {len(ALL_EMOTIONS)}개의 감정 데이터가 로드되었습니다.")
    # 예시 데이터 1개 출력
    if ALL_EMOTIONS:
        print("예시 데이터:", ALL_EMOTIONS[0])