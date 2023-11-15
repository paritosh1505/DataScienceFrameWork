import sys


def exception_error(error_detail:sys,err):
    _,_,exec_tb=error_detail.exc_info()
    fileName = exec_tb.tb_frame.f_code.co_filename
    erro_message = "Error in Python Code [{0}] and line number for the error is [{1}] and error message is [{2}]".format(
    fileName,exec_tb.tb_lineno,str(err)
    )
    return erro_message


class myException(Exception):
    def __init__(self,error_message,error_desc:sys):
        super().__init__(error_message)
        self.error_message = exception_error(error_detail=error_desc,err=error_message)

    def __str__(self) -> str:
        return self.error_message