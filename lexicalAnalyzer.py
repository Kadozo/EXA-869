import os

class LexicalAnalyzer:
    def __init__(self) -> None:
        self.__inputdir = "./Files/"
        self.__tokens_table = []
        self.__input_files_name = []
        self.__line_counter = 1
        self.__special_characters = ['+', '-', '*', '/', '!', '=', '<', '>', '&', '|', ';', ',', '.', '(', ')', '[', ']', '{', '}','"']
        self.__ascii_symbols = ['#', '$', '%', "'", ':', '?', '@', '^', '`', '~']
        self.__characters = []
        self.__header = 0
        self.__lexeme = ''



    def readFiles(self):
        filesname = list(os.listdir(self.__inputdir))
        for filename in filesname:
            x = filename.find("-saída.txt")
            if x == -1:
                self.__input_files_name.append(filename)
        print(self.__input_files_name)


    def getText(self, filename):
        with open(self.__inputdir + filename,"r") as currentFile:
            content = currentFile.read()
        self.__characters = list(content)


    def getCharacter(self) -> str:
        self.forwardHeader()
        if self.__header <= len(self.__characters):
            return self.__characters[self.__header-1]
        else:
            return '\n'

    def forwardHeader(self):
        self.__header = self.__header + 1

    def startTokenizer(self):
        self.readFiles()
        for filename in self.__input_files_name:
            self.getText(filename)
            self.q0()
            print(filename)
            with open(self.__inputdir+filename[:-4]+"-saída.txt", 'w') as file_writer:
                for element in self.__tokens_table:
                    file_writer.write(element)
                    file_writer.write('\n')
                file_writer.close()
            self.__header = 0
            self.__line_counter = 1
            self.__tokens_table = []
    


    def q0(self):
        self.__lexeme = ''
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'v':
            self.q8()
        elif verify == 'c':
            self.q17()
        elif verify == 'm':
            self.q4()
        elif verify == 'o':
            self.q32()
        elif verify == 'r':
            self.q39()
        elif verify == 'i':
            self.q1()
        elif verify == 'e':
            self.q46()
        elif verify == 't':
            self.q50()
        elif verify == 'f':
            self.q54()
        elif verify == 'p':
            self.q59()
        elif verify == 'b':
            self.q68()
        elif verify == 's':
            self.q75()
        elif verify == '+':
            self.q88()
        elif verify == '-':
            self.q89()
        elif verify == '*':
            self.q90()
        elif verify == '/':
            self.q91()
        elif verify == '!':
            self.q94()
        elif verify == '=':
            self.q100()
        elif verify == '<':
            self.q101()
        elif verify == '>':
            self.q102()
        elif verify == '&':
            self.q95()
        elif verify == '|':
            self.q96()
        elif verify == ';':
            self.q106()
        elif verify == ',':
            self.q107()
        elif verify == '.':
            self.q108()
        elif verify == '(':
            self.q109()
        elif verify == ')':
            self.q110()
        elif verify == '[':
            self.q111()
        elif verify == ']':
            self.q112()
        elif verify == '{':
            self.q113()
        elif verify == '}':
            self.q114()
        elif verify.isalpha():
            self.q116()
        elif verify.isdecimal():
            self.q117()
        elif verify == '"':
            self.q119()
        ##
        ##
        ##
        elif verify == '\n':
            if self.__header > len(self.__characters):
                print('final do arquivo')
            else:
                if verify == '\n':
                    self.__line_counter += 1
                self.q0()
        else:
            self.q0()

    def q1(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q2()
        elif verify == 'f':
            self.q45()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q2(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q3()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q3(self): #PRE int
        verify = self.getCharacter()
        self.__lexeme += verify
        
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1 
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q4(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'a':
            self.q5()
        elif verify == 'e':
            self.q26()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q5(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'i':
            self.q6()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q6(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q7()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q7(self): #PRE main
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1    
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q8(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'a':
            self.q9()
        elif verify == 'o':
            self.q64()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q9(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'r':
            self.q10()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q10(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'i':
            self.q11()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q11(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'a':
            self.q12()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q12(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'b':
            self.q13()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q13(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'l':
            self.q14()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q14(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q15()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q15(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q16()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q16(self): #PRE variables
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q17(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'o':
            self.q18()
        elif verify == 'l':
            self.q22()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q18(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q19()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q19(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q20()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q20(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q21()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q21(self): #PRE const
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()

    def q22(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'a':
            self.q23()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q23(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q24()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q24(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q25()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q25(self): #PRE class
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q26(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q27()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q27(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'h':
            self.q28()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q28(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'o':
            self.q29()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q29(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'd':
            self.q30()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q30(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q31()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q31(self): #PRE methods
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q32(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'b':
            self.q33()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q33(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'j':
            self.q34()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q34(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q35()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q35(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'c':
            self.q36()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q36(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q37()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q37(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q38()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q38(self): #PRE objects
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q39(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q40()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q40(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q41()
        elif verify == 'a':
            self.q57()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q41(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'u':
            self.q42()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q42(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'r':
            self.q43()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q43(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q44()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q44(self): #PRE return
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q45(self): #PRE if
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()

    def q46(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'l':
            self.q47()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q47(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q48()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q48(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q49()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q49(self): #PRE else
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()

    def q50(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'h':
            self.q51()
        elif verify == 'r':
            self.q81()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q51(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q52()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q52(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q53()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q53(self): #PRE then
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q54(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'o':
            self.q55()
        elif verify == 'a':
            self.q84()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q55(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'r':
            self.q56()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q56(self): #PRE for
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q57(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'd':
            self.q58()
        elif verify == 'l':
            self.q67()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q58(self): #PRE read
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q59(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'r':
            self.q60()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q60(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'i':
            self.q61()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q61(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q62()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q62(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q63()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q63(self): #PRE print 
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q64(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'i':
            self.q65()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q65(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'd':
            self.q66()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q66(self): #PRE void
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q67(self): #PRE real
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q68(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'o':
            self.q69()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q69(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'o':
            self.q70()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q70(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'l':
            self.q71()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q71(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q72()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q72(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'a':
            self.q73()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q73(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q74()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q74(self): #PRE boolean
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q75(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 't':
            self.q76()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q76(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'r':
            self.q77()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q77(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'i':
            self.q78()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q78(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'n':
            self.q79()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q79(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'g':
            self.q80()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q80(self): #PRE string
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q81(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'u':
            self.q82()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q82(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q83()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q83(self): #PRE true
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q84(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'l':
            self.q85()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q85(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 's':
            self.q86()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q86(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == 'e':
            self.q87()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q87(self): #PRE false
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<PRE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
    
    def q88(self): #ART +
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '+':
            self.q92()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q89(self): #ART -
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '-':
            self.q93()
        elif verify == '>':
            self.q115()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q90(self): #ART *
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q91(self): #ART /
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '/':
            self.q120()
        elif verify == '*':
            self.q121()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q92(self): #ART ++
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q93(self): #ART --
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<ART, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q94(self): #LOG !
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '=':
            self.q99()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q95(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == '&':
            self.q97()
    
    def q96(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == '|':
            self.q97()
    
    def q97(self): #LOG &&
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q98(self): #LOG ||
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<LOG, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q99(self): #REL !=
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q100(self): #REL =
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '=':
            self.q103()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q101(self): #REL <
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '=':
            self.q104()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q102(self): #REL >
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify == '=':
            self.q105()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q103(self): #REL ==
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q104(self): #REL <=
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q105(self): #REL >=
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q106(self): #DEL ;
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q107(self): #DEL ,
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q108(self): #DEL .
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q109(self): #DEL (
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q110(self): #DEL )
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q111(self): #DEL [
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q112(self): #DEL ]
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q113(self): #DEL {
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q114(self): #DEL }
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q115(self): #DEL ->
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<DEL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
        elif verify.isdecimal() or verify.isalpha():
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<REL, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()

    def q116(self): #IDE
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify.isalpha() or verify.isdecimal() or verify == '_':
            self.q116()
        elif verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<IDE, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q117(self):
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify.isdecimal() or verify == '.':
            self.q118()
        elif verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<NRO, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<NRO, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q118(self): #NRO
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify.isdecimal():
            self.q118()
        elif verify == ' ' or verify == '\n':
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<NRO, " + self.__lexeme + ">")
            if verify == '\n':
                self.__line_counter += 1
            self.q0()
        elif verify in self.__special_characters:
            self.__lexeme = self.__lexeme[:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<NRO, " + self.__lexeme + ">")
            self.__header = self.__header - 1
            self.q0()
    
    def q119(self): #CAC
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == '"':
            self.__lexeme = self.__lexeme[1:-1]
            self.__tokens_table.append(str(self.__line_counter) + ": " + "<CAC, " + self.__lexeme + ">")
            self.q0()        
        elif verify.isdecimal() or verify.isalpha() or verify in self.__ascii_symbols or verify in self.__special_characters or verify == " ":
            self.q119()

    def q120(self): #Comentário de Linha
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify != '\n':
            self.q120() 
        else:
            self.__line_counter +=1
            self.q0()
    
    def q121(self): #Comentário de bloco
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == '*':
            self.q122() 
        elif verify == '\n':
            self.__line_counter +=1
            self.q121()
        else:
            self.q121()

    def q122(self): #Comentário de bloco
        verify = self.getCharacter()
        self.__lexeme += verify
        if verify == '/':
            self.q0()
        elif verify == '\n':
            self.__line_counter += 1
            self.q121()
        else:
            self.__line_counter += 1
            self.q121()


LexicalAnalyzer().startTokenizer()