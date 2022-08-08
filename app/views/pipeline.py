from sklearn import metrics
from flask import jsonify,request
from ..models.pipeline import Pipeline,Data

import pandas as pd


def predict_all():
    '''
    Predict all data
    :param request:
    :return:
    '''

    pipe = Pipeline()
    model = pipe.get_pipeline()

    data = Data()
    X_train, y_train, X_test, y_test = data.get_all_data()

    y_teste_pred = model.predict(X_test)

    roc = metrics.roc_auc_score(y_test, y_teste_pred)
    auc = metrics.roc_auc_score(y_test, y_teste_pred)
    f1 = metrics.f1_score(y_test, y_teste_pred)
    df = pd.DataFrame({'y_test': y_test, 'y_test_pred': y_teste_pred})
    return jsonify({ 'roc': roc, 'auc': auc, 'f1': f1,'y_pred':df.to_dict()},200)

