# stonks-api

##todo:
1. investigate downloading mechanism for 2 or more files
2. ~~multiprocessing for pdf parsing~~ DONE!
    1. handle companies who place cover letter(WHY?!)
    2. know when table starts given types 1 and 2 formats [4-5 column vs 2-4 column]
    3. know when table ends (rank=100 or 100 entries or start of other table or EOF)
3. code to actually add connections to companies as edges
    1. edge weight = %stake * company value
    2. same entity, different name?
