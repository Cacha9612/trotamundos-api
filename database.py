from sqlalchemy import create_engine

DATABASE_URL = "mssql+pyodbc://sa:Trota01%40@67.205.148.136/trotamundosdb?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL, echo=True)
engine = engine.execution_options(autocommit = True)