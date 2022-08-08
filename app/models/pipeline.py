#Class to load price_pipe.pkl and return self.pipeline

class Pipeline:
    def __init__(self):
        self.pipeline = None
        self.load_pipeline()



    def load_pipeline(self):
        import joblib
        import os
        basedir = os.path.dirname(os.path.realpath(__file__))

        with open(f'{basedir}/class_pipe.pkl', 'rb') as f:
            self.pipeline = joblib.load(f)

    def get_pipeline(self):
        return self.pipeline
    

class Data:
    def __init__(self,data=None):
        self.data = data
        if data is None:
            self.load_data()
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
    
    def load_data(self):
        import pandas as pd
        self.data = pd.read_csv(f'arquivos/saida.csv')
        self.process_data()
    
    def process_data(self):
        '''
        Process data to be used in the model
        :return:
        '''
        import pandas as pd
        from sklearn.preprocessing import MultiLabelBinarizer

        self.data['caracteristica'] = self.data['caracteristica'].apply(lambda x: x.replace(' ', ''))
        self.data['caracteristica'] = self.data['caracteristica'].apply(lambda x: x.split(','))
        # convert columns caracteristic and procedimentos to list

        self.data.procedimentos.replace('N/C', 'N_C', inplace=True)
        self.data['procedimentos'] = self.data['procedimentos'].apply(lambda x: x.split(','))

        self.data.efeitos_desejados.replace('N/C', 'efeitos_desejados_N_C', inplace=True)
        self.data.efeitos_desejados.fillna('Missing_efeitos_desejados', inplace=True)
        self.data['efeitos_desejados'] = self.data['efeitos_desejados'].apply(lambda x: x.replace(' ', ''))
        self.data['efeitos_desejados'] = self.data['efeitos_desejados'].apply(lambda x: x.split(','))

        mlb = MultiLabelBinarizer(sparse_output=True)

        self.data = self.data.join(
            pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(self.data.pop('caracteristica')),
                index=self.data.index,
                columns=mlb.classes_))
        mlb = MultiLabelBinarizer(sparse_output=True)

        self.data = self.data.join(
            pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(self.data.pop('efeitos_desejados')),
                index=self.data.index,
                columns=mlb.classes_))

        mlb = MultiLabelBinarizer(sparse_output=True)

        self.data = self.data.join(
            pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(self.data.pop('procedimentos')),
                index=self.data.index,
                columns=mlb.classes_))

        # create columns caracteristica 1 até 10
        for i in range(1, 11):
            try:
                if f'Característica {i}' in self.data.columns:
                    pass
                else:
                    self.data[f'Característica{i}'] = 0
            except:
                print(f'Característica {i} já existe')

        if 'N/C' not in self.data.columns:
            self.data['N/C'] = 0


    def get_all_data(self):
        '''
        Get data to be used in the model
        :return:
        '''
        from sklearn.model_selection import train_test_split

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data.drop(['target'], axis=1),  # predictive variables
            self.data['target'],  # target
            test_size=0.2,  # portion of dataset to allocate to test set
            random_state=0,  # we are setting the seed here
        )
        self.y_train.fillna(0, inplace=True)
        self.y_test.fillna(0, inplace=True)
        return self.X_train, self.y_train, self.X_test, self.y_test

    def get_X_test(self):
        return self.X_test

    def get_y_test(self):
        return self.y_test

    def get_X_train(self):
        return self.X_train

    def get_y_train(self):
        return self.y_train