from main import polars_descriptive_stat_mean,polars_descriptive_stat_median,polars_descriptive_stat_std,visualize_data
import polars as pl

def test_descriptive_stat_mean():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    mean_mpg = polars_descriptive_stat_mean(cars, target_column)

    calculated_mean = cars[target_column].sum()/len(cars[target_column])
    assert mean_mpg == calculated_mean

def test_descriptive_stat_median():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    median_mpg = polars_descriptive_stat_median(cars, target_column)

    calculated_median = cars[target_column].median()
    assert median_mpg == calculated_median

def test_descriptive_stat_std():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    std_mpg = polars_descriptive_stat_std(cars, target_column)

    calculated_std = cars[target_column].std()
    assert std_mpg == calculated_std

if __name__ == "__main__":
    test_descriptive_stat_mean()
    test_descriptive_stat_median()
    test_descriptive_stat_std()
