import os 

# 폴더에 있는 파일 명들을 불러오는 함수
def get_file_list(dir_name):
    return os.listdir(dir_name)

def get_contents(file_list):
    y_class = []
    x_text = []
    class_dict = {
        1:'0', 2:'0', 3:'0', 4:'0', 5:'1', 6:'1', 7:'1', 8:'1'
    }
    for fiie_name in file_list:
        try:
            # 읽기모드로 파일 열기 cp949로 인코딩 해줘야 윈도우에서 열린다.
            f = open(file_name, 'r', encoding="cp949")
            # os.sep 은 각 os 에서 파일 디렉토리를 나누는 기호
            # 카테고리에는 파일명 가장 앞의 숫자가 들어간다.
            category = int(file_name.split(os.sep)[1].split(("_")[0]))
            # 사전 클래스의 value 값을 담아 축구와 야구에 관련성을 숫자 0, 1 로 나타낸다.
            y_class.append(class_dict[category])
            # 각 파일에 들어있는 텍스트를 담는다.
            x_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
        return x_text, y_class
            
def get_cleaned_text(text):
    import re
    # 첫번째 매개변수에 입력되어 있는 단어들은 두번째 매개변수로 대체한다.
    text = re.sub('/\+', '', text.lower())
    return text

def get_corpus_dict(text):
    # 각 파일에 입력되어 있는 문장의 단어들로 이뤄진 2차원 리스트가 생성된다.
    text = [sentence.split() for sentence in text]
    # 전 처리 과정
    cleand_words = [get_cleaned_text(word) for words in text for word in words]
    
    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleand_words)):
        corpus_dict[v] = i
    return corpus_dict

def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    # 각 단어에 id 와 같이 고유한 숫자가 정해져 있고, 문장안에 단어가 몇 개들어 있는지
    # 2차 배열을 만들어 반환한다.
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]
    x_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]
    
    for i, text in enumerate(word_number_list):
        for word_number in text:
            x_vector[i][word_number] += 1
    return x_vector

import math
def get_cosine_similarity(v1, v2):
    # 내적을 이용하여 두 벡터의 코사인 값을 반환
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumxy += x*y
        sumyy += y*y
    return sumxy/math.sqrt(sumxx*xumyy)

def get_similarity_score(x_vector, source):
    # x_vector 내에서 다른 문장의 x_vector와 코사인 유사도 검사
    source_vector = x_vector[source]
    similarity_list = []
    for target_vector in x_vector:
        similarity_lis.append(
            get_cosine_similarity(source_vector,target_vector)
        )
    return similarity_list

def get_top_n_similarity_news(similarity_score, n):
    # 유사도가 높은 것부터 10가지 출력
    import operator
    x = {i:v for i, v in enumberate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    return list(reversed(sorted_x))[1:n+1]

def get_accuracy(similarity_lis, y_class, source_news):
    # 유사도 계산
    source_class = y_class[source_news]
    
    return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)


if __name__ == "__main__":
    # 파일들의 상대 경로를 저장
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    
    x_text, y_class = get_contents(file_list)
    
    corpus = get_corpus_dict(x_text)
    print("Number of words : {0}".format(len(corpus)))
    x_vector = get_count_vector(x_text, corpus)
    source_number = 10
    
    result = []
    for i in range(80):
        source_number = i
        
        similarity_score = get_similarity_score(x_vector, source_number)
        similarity_news = get_top_n_similarity_news(similarity_score, 10)
        accuracy_score = get_accuracy(similarity_news, y_class, source_number)
        result.append(accuracy_score)
    print(sum(result) / 80)