from utils import load_data,data_process
import os


if __name__=="__main__":
    input_dir=r"H:/Bulk2space/tutorial/data/example_data/demo1/"
    input_sc_data_path=os.path.join(input_dir,"demo1_sc_data.csv")
    input_bulk_path=os.path.join(input_dir,"demo1_bulk.csv")
    input_sc_meta_path=os.path.join(input_dir,"demo1_sc_meta.csv")
    input_st_data_path=os.path.join(input_dir,"demo1_st_data.csv")
    input_st_meta_path=os.path.join(input_dir,"demo1_st_meta.csv")
    input_data=load_data(input_bulk_path,input_sc_data_path,input_sc_meta_path,
                     input_st_data_path,input_st_meta_path)
    processed_data=data_process(input_data,500,1)