import collections
def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5 
            cache.append(city)
    return answer

if __name__ == "__main__":
    assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50


