from tika import parser
import ast
from multiprocessing import Pool
import numpy
# cores = 8
'''
not working!!!
tika server as instance?
perhaps one instance should be fed multiple data as in parse.py
'''
def tagabasa(file_path):
    print("Process created.")
    x = 0
    file = parser.from_file(file_path)
    with open(".".join(file_path.split(".")[:-1])+".txt",'w+',encoding="utf-8") as f:
        if 'content' in file:
            out = file["content"].strip()
            print(out[:30])
            f.write(out)
        else:
            print("No content!")
        print("DONE!" + str(x))
    x+=1

def main(cores):
    print("here")
    with open("log.txt","r",encoding="utf-8") as f:
        paths = ast.literal_eval(f.read())
    pool = Pool(cores)
    pool.map_async(tagabasa,paths[0:17])
    pool.close()
    pool.join()

if __name__ == "__main__":
    cores = 8
    main(cores)
