from main import pandas_descriptive_stat_mean,pandas_descriptive_stat_median,pandas_descriptive_stat_std,visualize_data
import pandas as pd

def test_pandas_descriptive_stat_mean():
    cars = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    mean_mpg = pandas_descriptive_stat_mean(cars, target_column)

    calculated_mean = cars[target_column].sum()/len(cars[target_column])
    assert mean_mpg == calculated_mean

def test_pandas_descriptive_stat_median():
    cars = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    median_mpg = pandas_descriptive_stat_median(cars, target_column)

    calculated_median = cars[target_column].median()
    assert median_mpg == calculated_median

def test_pandas_descriptive_stat_std():
    cars = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    std_mpg = pandas_descriptive_stat_std(cars, target_column)

    calculated_std = cars[target_column].std()
    assert std_mpg == calculated_std

if __name__ == "__main__":
    test_pandas_descriptive_stat_mean()
    test_pandas_descriptive_stat_median()
    test_pandas_descriptive_stat_std()
