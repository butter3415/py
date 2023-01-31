import pandas as pd

df = pd.DataFrame([[4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]],
                   index = [1, 2, 3],
                   columns=['a','b','c'])

# def squares(n):
#     return n * n


print(df)
print(df.apply(lambda n : n * n))   # squares 함수랑 동일함

# print(df.apply(squares))

# print(df.median())
# print(df.describe())    # 요약본

