# *_*coding:utf-8 *_*
import ast
import tkinter.messagebox
from os.path import dirname, abspath, join, expanduser
from os import listdir
import pathlib

# 获取项目根目录
ROOT = dirname(abspath(__file__))


class Helper:
    def __init__(self):
        pass

    def get_gil_ashares(self):
        gil_ashares = self._get_gil_cn_ashare_pool().append(
            self._get_gil_hk_ashare_pool())
        # gil_ashares = self._get_gil_hk_ashare_pool()
        return gil_ashares

    def get_mysql_connect(self):
        try:
            # import sqlstar  # pip install sqlstar==3.0.7

            host_office = 'rm-wz9s90lao15s6j4v2ro.mysql.rds.aliyuncs.com'
            passwd = 'G2W9iPwpAqF4R#202'
            mysql = sqlstar.Database(f'mysql://jydb:{passwd}@'
                                     f'{host_office}:3306/jydb')
            mysql.connect()
            return mysql
        except:
            pass

    def _get_gil_cn_ashare_pool(self):
        """下载A股股票池"""
        command = """
            select secucode, chinameabbr, secuabbr, chiname, listeddate,listedstate from SecuMain 
     where (SecuCategory=1) and ((SecuMarket=83) or (SecuMarket=90))
        """
        mysql = self.get_mysql_connect()
        # 81-三板市场, 83-上海证券交易所, 90-深圳证券交易所;
        df = mysql.fetch_df(command)
        df = df.dropna(subset=['secuabbr'])
        df = df.drop_duplicates()
        df['secucode'] = df['secucode'].apply(
            lambda x: self._transform_code(x))
        return df

    def _get_gil_hk_ashare_pool(self):
        """下载香港股票池"""
        command = """
                select secucode, ChiNameAbbr as chinameabbr, secuAbbr as 
                secuabbr, ChiName as chiname, ListedDate as listeddate,
                listedstate as listedstate
                 from HK_secumain
            where (SecuCategory=3 or SecuCategory=51 or SecuCategory=53)
            and secuAbbr not in ('阿里巴巴')
            -- and (TraCurrUnit=1100)
                """
        mysql = self.get_mysql_connect()
        df = mysql.fetch_df(command)
        df = df.dropna(subset=['secuabbr'])
        df = df.drop_duplicates()
        df['secucode'] = df['secucode'].apply(lambda x: str(x) + '.HK')
        return df

    @property
    def chinameabbr_code_pair(self):
        gil_ashares = self.get_gil_ashares()
        return dict(gil_ashares[[
            'chinameabbr', 'secucode'
        ]].dropna(subset=['chinameabbr']).drop_duplicates().values)

    @property
    def secuabbr_code_pair(self):
        gil_ashares = self.get_gil_ashares()
        return dict(gil_ashares[['secuabbr',
                                 'secucode']].drop_duplicates().values)

    @staticmethod
    def _transform_code(code):
        if str(code).startswith('6'):
            return str(code) + '.SH'
        elif str(code).startswith('3') or str(code).startswith('0'):
            return str(code) + '.SZ'
        else:
            return str(code)

    def update_name_code_json(self):
        gil_ashares = self.get_gil_ashares()
        chinameabbr_code_pair = dict(gil_ashares[[
            'chinameabbr', 'secucode'
        ]].dropna(subset=['chinameabbr']).drop_duplicates().values)

        secuabbr_code_pair = dict(gil_ashares[['secuabbr', 'secucode'
                                               ]].drop_duplicates().values)

        name_code_dic = {**chinameabbr_code_pair, **secuabbr_code_pair}

        with open('datasets/name_code.json', "w", encoding='utf-8') as f:
            f.write(str(name_code_dic))

    @staticmethod
    def get_name_code_dic():
        """

        :param :
        :return:
        """
        with open(join(ROOT, 'datasets', 'name_code.json'), "r", \
                encoding='utf-8') as fr:
            data = ast.literal_eval(fr.read())
        return data


if __name__ == '__main__1':
    Helper().update_name_code_json()

if __name__ == '__main__':
    helper = Helper()
    DATASETS = join(expanduser('~'), 'Downloads', 'datasets')
    RESULTS = join(expanduser('~'), 'Downloads', 'results')
    pathlib.Path(RESULTS).mkdir(exist_ok=True, parents=True)
    files = listdir(DATASETS)
    for file in files:
        sentence = open(join(DATASETS, file), 'r', encoding='utf8').read()

        name_code_dic = helper.get_name_code_dic()

        for name, code in name_code_dic.items():
            sentence = sentence.replace(name, name + '(' + code + ')')

        print(sentence)
        with open(join(RESULTS, file), 'w', encoding='utf8') as f:
            f.write(sentence)

    tkinter.Tk().withdraw()
    tkinter.messagebox.showinfo("提示", "执行完成")
