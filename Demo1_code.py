import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from tkinter import Canvas
import tkinter.messagebox
from decimal import *
import hashlib
import math
from tkinter.constants import BOTH, BOTTOM, END, LEFT, NE, NW, RIGHT, S, TOP, TRUE, X, Y
from tkinter.ttk import Separator
from typing import Counter
from PIL import Image, ImageTk
import sympy
import base64
from io import BytesIO
import time
class Block(object):  # 创建Circle类
    def __init__(self, index, timestamp,data,previousHash): # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
       self.nonce = 0;
       self.index = index;
       self.timestamp = timestamp;
       self.data = data;
       self.previousHash = previousHash;
       self.hash = self.calculateHash();
    #    self.countnum = 0
    def calculateHash(self):
        return hashlib.sha256((str(self.index) + str(self.previousHash) + str(self.timestamp) + str(self.data)+str(self.nonce)).encode('utf-8')).hexdigest()  
    def mineBlock(self,difficulty):
        # int(difficulty)
        while(str(self.hash)[0:int(difficulty)] != ''.zfill(int(difficulty))):
            self.nonce = self.nonce + 1
            self.hash = self.calculateHash()
            print(self.hash)
        

class Blockchain(object):
    def __init__(self): 
        self.chain = [self.createGenesisBlock()];
        self.difficulty = 4;
    def createGenesisBlock(self):
        # b1 = []
        # Block(0,"01/01/2021","Genesis block","0")
        # b1.append(list())
        ticks =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return Block(0,ticks,"Group 1's block","0");

    def getLatesBlock(self):
        return self.chain[len(self.chain)-1];

    def addBlock(self,newBlock):
        
        newBlock.previousHash = self.getLatesBlock().hash;
        newBlock.mineBlock(self.difficulty);
        # newBlock.hash = newBlock.calculateHash();
        self.chain.append(newBlock);

    def isChainValid(self):
        for i in range(1,len(self.chain)):
            currentBlock = self.chain[i];
            previousBlock = self.chain[i-1];
            if(currentBlock.hash != currentBlock.calculateHash()):
                return False;
            if(currentBlock.previousHash != previousBlock.hash):
                return False;
        return True;

class MainPage():
    """
    主页面
    """

    def bf_goFunction1(self):
        """
        跳转功能1
        """
        self.root.destroy()
        tbm = Function1()
        tbm.initialGUI()
    
    def __init__(self):
        self.root = tk.Tk()
        self.WIDTH = 1000
        self.HEIGHT = 100
        self.TITLE = "BlockChain"
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        x = (self.ws / 2) - (self.WIDTH / 2)
        y = (self.hs / 2) - (self.HEIGHT / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, x, y))
        self.root.title(self.TITLE)
        # L1 = tk.Label(self.root, text="Kong Fan Nap 1155152768 | LI Jialang 1155160950 | Youguang Lin 1155169171")
        # L1.pack()
        L2 = tk.Label(self.root, text="Group 1 Demo")
        L2.pack()
        L1 = tk.Label(self.root, text="Kong Fan Nap 1155152768 | LI Jialang 1155160950 | Youguang Lin 1155169171")
        L1.pack()
        B1 = tk.Button(self.root, text="Block Chain Demo", command=self.bf_goFunction1)
        B1.pack()
        self.root.mainloop()

class Function1(object):

    def __init__(self):
        self.TITLE = "Group 1 - Block Chain Demo"
        self.WIDTH = 600
        self.HEIGHT = 200
        self.parseDic = {}
        self.count = 0
        self.root = tk.Tk()
# Initial GUI

    def initialGUI(self):
        self.root.title(self.TITLE)
        circle1 = Blockchain()
        # print("index: " + str(circle1.chain[0].index)+' Time: '+str(circle1.chain[0].timestamp)+' Data: '+str(circle1.chain[0].data)+' PreHash: '+str(circle1.chain[0].previousHash)+' CurHash: '+str(circle1.chain[0].hash))
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        x = (self.ws / 2) - (self.WIDTH / 2)
        y = (self.hs / 2) - (self.HEIGHT / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, x, y))
        Frame0 = tk.Frame(self.root)
        Frame1 = tk.Frame(self.root,width=200)
        Frame1.pack_forget()
        Frame0.pack(fill=tk.Y, pady=10)
        tk.Label(Frame0,text="Add New Block").grid(row=0,column=0,sticky='W')
        tk.Label(Frame0,text="Edit Block").grid(row=2,column=0,sticky='W')
        tk.Label(Frame0,text="Index").grid(row=3,column=0,sticky='W')
        tk.Label(Frame0,text="Edit Content").grid(row=3,column=1,sticky='W',columnspan=2)
        tk.Button(Frame0,text='Check Chain Vaild',command= lambda: changeTag2()).grid(row=6,column=0)
        tk.Button(Frame0,text='View',command= lambda: changeTag3()).grid(row=1,column=2)
        tk.Label(Frame0,text="Result: ").grid(row=6,column=1,sticky='W')
        Check_result = tk.StringVar()
        index_block1 = tk.StringVar()
        index_block = tk.Entry(Frame0,textvariable=index_block1)
        index_block.grid(row=4,column=0)
        Editcontent_block1 = tk.StringVar()
        Editcontent_block = tk.Entry(Frame0,textvariable=Editcontent_block1)
        Editcontent_block.grid(row=4,column=1)
        tk.Button(Frame0,text='Sure',command= lambda: changeTag1(index_block.get(),Editcontent_block.get())).grid(row=4,column=3)
        tk.Label(Frame0,text="Check Block").grid(row=5,column=0,sticky='W')
        content_block1 = tk.StringVar()
        content_block = tk.Entry(Frame0,textvariable=content_block1)
        content_block.grid(row=1,column=0)
        tk.Button(Frame0,text='Add',command= lambda: changeTag()).grid(row=1,column=1)
        def changeTag():
            ticks =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.count = self.count + 1
            circle1.addBlock(Block(self.count,ticks,content_block.get(),' '))
            content_block1.set(" ")
            # print("index: " + str(circle1.getLatesBlock().index)+' Time: '+str(circle1.getLatesBlock().timestamp)+' Data: '+str(circle1.getLatesBlock().data)+' PreHash: '+str(circle1.getLatesBlock().previousHash)+' CurHash: '+str(circle1.getLatesBlock().hash))

        def changeTag1(index,content):
            circle1.chain[int(index)].data = content;
            circle1.chain[int(index)].hash = circle1.chain[int(index)].calculateHash();
            # print("index: " + str(circle1.chain[int(index)].index)+' Time: '+str(circle1.chain[int(index)].timestamp)+' Data: '+str(circle1.chain[int(index)].data)+' PreHash: '+str(circle1.chain[int(index)].previousHash)+' CurHash: '+str(circle1.chain[int(index)].hash))
            index_block1.set(" ")
            Editcontent_block1.set(" ")
        def changeTag2():
            circle1.isChainValid()
            Check_result.set(str(circle1.isChainValid()))
            CheckBlock = tk.Label(Frame0,textvariable=Check_result)
            CheckBlock.grid(row=6,column=2)
        def changeTag3():
            Frame0.pack_forget()
            Frame1.pack()
            t = tk.Text(Frame1,height=50, width=200)
            t.grid(row=1,column=0)
            for j in range(0,len(circle1.chain)):
                t.insert(END,"index: " + str(circle1.chain[int(j)].index)+' Time: '+str(circle1.chain[int(j)].timestamp)+' CountNum: '+str(circle1.chain[int(j)].nonce)+' Data: '+str(circle1.chain[int(j)].data)+' PreHash: '+str(circle1.chain[int(j)].previousHash)+' CurHash: '+str(circle1.chain[int(j)].hash))
                t.insert(tk.INSERT, '\n')
            re_bu = tk.Button(t,text="Return",command=lambda: changeTag4())
            t.window_create(tk.INSERT,window=re_bu)
        def changeTag4():
            Frame0.pack()
            Frame1.forget()

            # t.insert
if __name__ == "__main__":
    MainPage()