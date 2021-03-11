'''
Created on 23 dec. 2018

@author: Revnic
'''
from console import Console
from controller import Controller
from matrix import Matrix
def run():
    matrix=Matrix()
    controller=Controller(matrix)
    console=Console(controller)
    console.run()
run()