import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocesamiento(df):
    #eliminamos las columnas que no usamos
    df = df.drop(["Movie", "Year", "Likes", "Dislikes", "Comments"], axis=1)

    #assignamos variables categoricas y numericas
    categorical_columns = ["Genre"]
    numerical_columns = [c for c in df.columns if c not in categorical_columns]

    #convertimos las variables categoricas
    for column in categorical_columns:
        one_hot = pd.get_dummies(df[column], prefix=column)
        df = df.merge(one_hot,left_index=True,right_index=True)
        df = df.drop(columns=column)

    #escalamos variables
    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    #procesamiento de missing values
    df.fillna(df.mean(), inplace=True)

    return df


def preprocesado_from_file(fichero='./CSM_dataset.xlsx'):
    # Importamos los datos:
    data = pd.read_excel(fichero)
    df = pd.DataFrame(data)

    df = preprocesamiento(df)

    X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["Gross"]), df["Gross"], test_size=0.2, random_state=42)
    
    return X_train, y_train, X_test, y_test