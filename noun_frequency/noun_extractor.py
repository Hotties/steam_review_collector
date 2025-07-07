# noun_extractor.py

import re
import emoji
from soynlp.normalizer import repeat_normalize
from konlpy.tag import Okt
##from stopwords_ko import stopwords as ko_stopwords  # stopwords-ko 사용

# 추가적인 불용어가 필요한 경우 이곳에 작성
CUSTOM_STOPWORDS = set(['것', '거', '수', '좀', '정도', '다시'])  # 필요한 만큼 확장 가능

# 결합된 불용어 리스트
##ALL_STOPWORDS = set(ko_stopwords).union(CUSTOM_STOPWORDS)

def extract_nouns(text: str) -> list[str]:
    """
    주어진 텍스트에서 명사를 추출하고 불용어 및 한 글자 단어 제거
    :param text: 입력 텍스트 (str)
    :return: 명사 리스트 (불용어 제거 및 길이 1 이하 제외)
    """
    # 전처리
    text = emoji.replace_emoji(text, replace='')
    text = repeat_normalize(text, num_repeats=2)
    text = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    # 형태소 분석
    okt = Okt()
    nouns = okt.nouns(text)
    
    # 불용어 및 한 글자 제거
    clean_nouns = [word for word in nouns if len(word) > 1]

    print(clean_nouns)
    return clean_nouns



##[ERROR] Failed to insert review 194234220: No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly.
##set "LIB=C:\Program Files (x86)\Windows Kits\10\Lib\10.0.26100.0\ucrt\x64;C:\Program Files (x86)\Windows Kits\10\Lib\10.0.26100.0\um\x64"
