from sqlalchemy import create_engine
import os
from data_clensing1 import clean_data

engine = create_engine("postgresql://admin:admin123@localhost:5432/DozzaDB")

folder_path = "/home/angelo/Downloads/dozza_PresenzeTuristi_202508" #inserire la cartella di UN SOLO mese
file_type = "PRESENZE" #inserire PRESENZE o SPOSTAMENTI in base al tipo di dati da gestire

items = os.listdir(folder_path)
clean_data(engine, items, folder_path, file_type)