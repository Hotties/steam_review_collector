# chart_generator.py

import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def plot_top_n_nouns(nouns: list[str], top_n: int = 10):
    """
    명사 리스트에서 상위 N개를 막대그래프로 시각화
    :param nouns: 전체 명사 리스트
    :param top_n: 시각화할 상위 명사 개수
    """
    counter = Counter(nouns)
    most_common = counter.most_common(top_n)

    if not most_common:
        print("⚠️ 명사가 충분하지 않습니다.")
        return

    labels, counts = zip(*most_common)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(counts), y=list(labels), palette="Reds_r")
    plt.xlabel("빈도수")
    plt.ylabel("단어")
    plt.title(f"자주 등장한 명사 TOP {top_n}")
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
