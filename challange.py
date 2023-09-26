'''Latam Challange para medicion de memoria y tiempo para leer un archivo en formato JSON'''
from collections import Counter, defaultdict
from datetime import datetime, date
from typing import List, Tuple
import time
import heapq
import json
#Libreria de medicion de memoria
from memory_profiler import profile


def timeit(func):
    '''Funcion que  mide y muestra el tiempo de ejecucion en cada funcion'''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} tomo {execution_time:.4f} segundos para procesar")
        return result
    return wrapper

def read_tweets(file_path):
    '''Se lee el archivo json linea por linea y devuelve un objeto'''
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            yield tweet

@timeit
def q1_time(file_path: str) -> List[Tuple[date, str]]:
    '''La funcion devuelve  las top 10 fechas  donde ahi mas tweets optimisando tiempo'''
    date_counts = Counter()
    user_counts = defaultdict(Counter)

    for tweet in read_tweets(file_path):
        tweet_date_str = tweet['date']
        try:
            tweet_date = datetime.strptime(tweet_date_str, '%Y-%m-%dT%H:%M:%S%z').date()
            #Manejo de errores
        except ValueError:
            continue

        username = tweet['user']['username']

        date_counts[tweet_date] += 1
        user_counts[tweet_date][username] += 1

    result = []
    for tweet_date, _ in date_counts.most_common(10):
        most_common_user = user_counts[tweet_date].most_common(1)[0]
        result.append((tweet_date, most_common_user[0]))

    return result

@timeit
#@profile
def q1_memory(file_path: str) -> List[Tuple[date, str]]:
    '''La funcion devuelve  las top 10 fechas  donde ahi mas tweets optimisando memoria con la libreria heapq'''
    date_counts = Counter()
    user_counts = defaultdict(Counter)

    for tweet in read_tweets(file_path):
        tweet_date_str = tweet['date']
        try:
            tweet_date = datetime.strptime(tweet_date_str, '%Y-%m-%dT%H:%M:%S%z').date()
        except ValueError:
            # Handle invalid date format
            continue

        username = tweet['user']['username']

        date_counts[tweet_date] += 1
        user_counts[tweet_date][username] += 1

    result = []
    for tweet_date, _ in heapq.nlargest(10, date_counts.items(), key=lambda x: x[1]):
        most_common_user = max(user_counts[tweet_date].items(), key=lambda x: x[1])
        result.append((tweet_date, most_common_user[0]))

    return result

@timeit
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    '''La funcion devuelve  las top 10 emojis  mas usados optimisando tiempo '''

    emoji_counts = Counter()

    for tweet in read_tweets(file_path):
        content = tweet['content']
        emojis = [c for c in content if c in '\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001F004\U0001F0CF\U0001F170-\U0001F251\U0001F004\U0001F600-\U0001F64F\U0001F601-\U0001F64C\U0001F600-\U0001F637']
        emoji_counts.update(emojis)

    return emoji_counts.most_common(10)
@timeit
#@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    '''La funcion devuelve  las top 10 emojis  mas usados optimisando memoria con  la libreria heapq'''
    emoji_counts = Counter()

    for tweet in read_tweets(file_path):
        content = tweet['content']
        emojis = [c for c in content if c in '\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001F004\U0001F0CF\U0001F170-\U0001F251\U0001F004\U0001F600-\U0001F64F\U0001F601-\U0001F64C\U0001F600-\U0001F637']
        emoji_counts.update(emojis)

    result = heapq.nlargest(10, emoji_counts.items(), key=lambda x: x[1])
    return result

@timeit
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    '''La funcion devuelve  las top 10 usuarios mas mencionados optimizando  tiempo'''
    user_mention_counts = Counter()

    for tweet in read_tweets(file_path):
        username = tweet['user']['username']
        mentions = tweet.get('mentionedUsers')
        if mentions is not None:
            user_mention_counts[username] += len(mentions)

    return user_mention_counts.most_common(10)
@timeit
#@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    '''La funcion devuelve  las top 10 usuarios mas mencionados optimizando  memoria usando la libreria heapq'''
    user_mention_counts = Counter()

    for tweet in read_tweets(file_path):
        username = tweet['user']['username']
        mentions = tweet.get('mentionedUsers')
        if mentions is not None:
            user_mention_counts[username] += len(mentions)

    result = heapq.nlargest(10, user_mention_counts.items(), key=lambda x: x[1])
    return result


top_dates_time = q1_time("/home/a.barrera/Latam_Challenge/farmers-protest-tweets-2021-2-4.json")
print("Top 10 Dates (Time):", top_dates_time)
print("===========================================================================================")

top_dates_memory = q1_memory("/home/a.barrera/Latam_Challenge/farmers-protest-tweets-2021-2-4.json")
print("Top 10 Dates (Memory):", top_dates_memory)
print("===========================================================================================")

top_emojis_time = q2_time("/home/a.barrera/Latam_Challenge/farmers-protest-tweets-2021-2-4.json")
print("Top 10 Emojis (Time):", top_emojis_time)
print("===========================================================================================")

top_emojis_memory = q2_memory("/home/a.barrera/Latam_Challenge/farmers-protest-tweets-2021-2-4.json")
print("Top 10 Emojis (Memory):", top_emojis_memory)
print("===========================================================================================")

top_users_time = q3_time("/home/a.barrera/Latam_Challenge/farmers-protest-tweets-2021-2-4.json")
print("Top 10 Users (Time):", top_users_time)
print("===========================================================================================")

top_users_memory = q3_memory("/home/a.barrera/Latam_Challenge/farmers-protest-tweets-2021-2-4.json")
print("Top 10 Users (Memory):", top_users_memory)
