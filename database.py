from sqlalchemy import create_engine

DATABASE_URL = "mssql+pyodbc://sa:Trotamundosserver@trotamundosdb.cuvrbibw9zda.us-east-2.rds.amazonaws.com/trotamundosdb?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL, echo=True)
engine = engine.execution_options(autocommit = True)