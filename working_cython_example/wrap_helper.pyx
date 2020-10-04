cdef extern from "helper.cpp":
    cdef double PhredToPError(int phred);

def  pPhredToPError(int_phred):
    return PhredToPError(int_phred)