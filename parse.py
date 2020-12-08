from tika import parser
import ast
from multiprocessing import Pool
import numpy
# cores = 8
def tagabasa(chunk):
    print("Process created.")
    x = 0
    for file_path in chunk:
        file = parser.from_file(file_path)
        with open(".".join(file_path.split(".")[:-1])+".txt",w+,encoding="utf-8") as f:
            if 'content' in file:
                out = file["content"].strip()
                print(out[:30])
                f.write(out)
            else:
                print("No content!")
            print("DONE!" + str(x))
        x+=1

def main(cores):
    with open("log.txt","r",encoding="utf-8") as f:
        paths = ast.literal_eval(f.read())
    pool = Pool(cores)
    chunkedList = makeChunk(paths[0:17],cores)
    pool.map(tagabasa,chunkedList)
    pool.close()

def makeChunk(list, n):
    return numpy.array_split(list,n)

if __name__ == "__main__":
    cores = 8
    main(cores)
