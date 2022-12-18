import yfinance as yf
from pydantic import BaseModel
import pandas as pd
from typing import Union
from sklearn.impute import SimpleImputer, IterativeImputer

#TODO: use smart methods in python for download functionality

# create base class with settings
class DynamicDailySettings(BaseModel):
    """base model to store settings for daily pull from yfinance"""
    default_start_date: str = "2017-01-01" # 5 years ago
    default_interval: str = '1d'
    after_post_market: bool = False

class Pull():
    """pull data from yfinance and store in pandas dataframe"""

    def __init__(self, start_date: Union[None, str] = None,
                 interval: Union[None, str] = None,
                 data_preprocess: Union[None, str] = None):
        """create class variables"""
        self.settings_model: DynamicDailySettings = DynamicDailySettings()
        self.start_date = start_date
        self.interval = interval
        self.data_preprocess = data_preprocess

    @staticmethod
    def _imputer_func(dataframe: pd.DataFrame, mode: str = 'mean', impute_type: str = 'iterative'):
        """remove potential nan values from dataframe with sklearn imputer functionality"""
        pass

    def _data_call(self):
        """call yfinance data from public api"""
        pass

    def _data_cleaner(self, dataframe: pd.DataFrame):
        """clean data from yfinance"""
        pass

    def facade(self):
        """visible method to call from higher layers"""
        pass