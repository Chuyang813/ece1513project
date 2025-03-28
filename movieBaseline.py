import pandas as pd


def read_file(file_path):
    ratings = pd.read_csv(
        file_path,
        sep='::',
        names=['user_id', 'movie_id', 'rating', 'timestamp'],
        engine='python'
    )
    return ratings



if __name__ == '__main__':
    
    ratings = read_file('ml-1m/ratings.dat')
    print(ratings.head())