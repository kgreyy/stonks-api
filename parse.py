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
        if 'content' in file:
            print(file["content"].strip()[:300])
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
