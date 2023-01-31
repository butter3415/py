# pandas
# pip install pandas #
import pandas as pd

# pd.DataFrame # 행과 열의 데이터 프레임 만들어짐
'''
df = pd.DataFrame(
    {'a' = [4, 5, 6],
     'b' = [7, 8, 9],
     'c' = [10, 11, 12]},
     index = [1, 2, 3]) # 인덱스 안주면 0번으로 시작

    a   b   c
1   4   7   10
2   5   8   11
3   6   9   12
'''

# df = pd.DataFrame({"a" : [4, 5, 6],
#                    "b" : [7, 8, 9],
#                    "c" : [10, 11, 12]},
#                    index = [1, 2, 3]) # 딕셔너리 스타일

df = pd.DataFrame([[4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]],
                   index = [1, 2, 3],
                   columns=['a','b','c'])   # 2차원 리스트 형태
print(df)
# print(df.loc[: , ['a', 'c']])
print(df.loc[df['b']>8, ['a', 'c']])    # b의 수가 8 이상인 a,c열의 수 가져오기 

df1 = (pd.melt(df)
       .rename(columns={
               'variable' : 'var',
               'value' : 'val' })
       .iloc[:,[1]]
       # .iloc[1:5]
       #.query('val >= 7')
)
# pivot 은 melt 의 반대
print(df1)

print(df1.sort_values('val'))   # 오름차순 정렬
print(df1.sort_values('val',ascending=False))   # 내림차순 정렬