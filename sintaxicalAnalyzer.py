'''with open(self.__inputdir+filename[:-4]+"-saída.txt", 'w') as file_writer:
                for element in self.__tokens_table:
                    file_writer.write(element)
                    file_writer.write('\n')
                if(len(self.__errors_table)>0):
                        file_writer.write('\n')
                        file_writer.write('-----------------TABELA DE ERROS-----------------\n')
                        for element in self.__errors_table:
                            file_writer.write('\n')
                            file_writer.write(element)
                file_writer.close()'''

class SintaxicalAnalyzer():
        def __init__(self,tokens_table,errors_table,filename) -> None:
                self.is_EOF = False
                self._tokens_table = tokens_table
                self._length_tokens_table = len(tokens_table)
                self._erros_table = errors_table
                self.filename = filename
                self._header = 0

        def _is_TYPE(self,token):
             return token["token"] in ['int','real','boolean','string']
        def _is_IDE(self,token):
            return  token["type"] == "IDE"
        def _is_INTEGER(self,token):
            return token["token"].isdigit()
        def _is_NRO(self,token):
            return token["type"] == "NRO"
        def _is_BOOL(self,token):
            return (token["token"] == "true") | (token["token"] == "false")
        def _is_CAC(self,token):
            return token["type"] == "CAC"
        def _is_ATTRIBUTION(self,token):
            return (self._is_NRO(token)) | (self._is_BOOL(token)) | (self._is_CAC(token))

        def _error_message(self,line:str,expected:[],founded:str):
            print("Erro na linha " + line + ", no token " + str(self._header) + ", era esperado um dos seguintes tokens:", expected, "mas foi encontrado: " + founded)
        
        def start_analysis(self):
            while not self.is_EOF:
                token = self.next_token()
                if not self.is_EOF:
                    if token["token"] == "const":
                        self._const_block()
                        self._variables_block()
                        self._class_block()    
                    else:
                        self._error_message(line=token["line"],founded=token["token"],expected=["const"])  
        
        def next_token(self) -> object:
            if self._header < self._length_tokens_table:
                  actual_element = self._tokens_table[self._header].split(":",1)
                  actual_type_token =  actual_element[1].split(',',1)
                  token = {"line":actual_element[0],"type": actual_type_token[0][2:], "token":actual_type_token[1][1:-1]}
                  self._header += 1
                  return token
            else:
                 self.is_EOF = True
                 token = {"line":"","type":"EOF", "token":"EOF"}
                 return token

## BLOCO DE CONSTANTES
        def _const_block(self):
            token = self.next_token()
            if token["token"] == "{":
                self._consts()
            else:
                self._error_message(expected=["{"],founded=token["token"], line=token["line"])

        def _consts(self):
            token = self.next_token()
            if self._is_TYPE(token):
                self._const_attribution()
                self._multiple_consts()
                self._consts()
            elif token["token"] == '}':
                print("achou const")
            else:
                self._error_message(expected=["}"],founded=token["token"], line=token["line"])

        def _const_attribution(self):
            token = self.next_token()
            if self._is_IDE(token):
                token = self.next_token()
                if token["token"] == "=":
                      token = self.next_token()
                      if self._is_ATTRIBUTION(token):
                           print("passou Atribuição")
                else:
                    self._error_message(expected=["="],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["IDE"],founded=token["token"], line=token["line"])
        
        def _multiple_consts(self):
            token = self.next_token()
            if token["token"] == ",":
                 self._const_attribution()
                 self._multiple_consts()
            elif token["token"] == ';':
                 print("Achou multiple consts")
            else:
                self._error_message(expected=[",",";"],founded=token["token"], line=token["line"])

#FIM DO BLOCO DE CONSTANTES
#BLOCO DE VARIÁVEIS

        def _variables_block(self):
            token = self.next_token()
            if token["token"] == "variables":
                token = self.next_token()
                if token["token"] == "{":
                    self._variables()
                    print("achou variables block")
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["variables"],founded=token["token"], line=token["line"])
        
        def _variables(self):
            token = self.next_token()
            if self._is_TYPE(token):
                self._dec_var()
                self._multiple_variables_line()
            elif token["token"] == '}':
                print("Achou variables")
            else:
                self._error_message(expected=["}",'int','real','boolean','string'],founded=token["token"], line=token["line"])
        
        def _dec_var(self):
            token = self.next_token()
            if self._is_IDE(token):
                self._dimensions()
            else:
                self._error_message(expected=["IDE"],founded=token["token"], line=token["line"])
        
        def _dimensions(self):
            token = self.next_token()
            if token["token"] == "[":
                self._size_dimensions
                token = self.next_token()
                if token["token"] == "]":
                     self._dimensions()
            else:
                self._header -= 1

        def _size_dimensions(self):
            token = self.next_token()
            if self._is_IDE(token) | self._is_INTEGER(token):
                pass
            else:
                self._error_message(expected=["IDE","INTEGER"],founded=token["token"], line=token["line"])

        def _multiple_variables_line(self):
            token = self.next_token()
            if token["token"] == ";":
                print("Achou multiple_variables_line")
            elif token["token"] == ',':
                self._dec_var()
                self._multiple_variables_line()
            else:
                self._error_message(expected=[",",";"],founded=token["token"], line=token["line"])
#FIM BLOCO DE VARIAVEIS
#BLOCO DE CLASSE

        def _class_block(self):
           token = self.next_token()
           if token["token"] == "class":
               self._ide_class()
           else:
               self._error_message(expected=["class"],founded=token["token"], line=token["line"])
        
        def _ide_class(self):
            token = self.next_token()
            if self._is_IDE(token):
                self._extends()
            else:
                self._header -= 1
                self._main()
        
        def _extends(self):
            token = self.next_token()
            if token["token"] == "extends":
                token = self.next_token()
                if self._is_IDE(token):
                    self._start_class_block()
                else:
                    self._error_message(expected=["IDE"],founded=token["token"], line=token["line"])
            else:
                self._start_class_block()

        def _start_class_block(self):
            token = self.next_token()
            if token["token"] == "{":
                self._init_class()
            else:
                self._error_message(expected=["{"],founded=token["token"], line=token["line"])

        def _init_class(self):
            self._body_blocks()
            self._methods_block()
            self._constructor()
        
        def _constructor(self):
            token = self.next_token()
            if token["token"] == "constructor":
                token = self.next_token()
                if token["token"] == "(":
                    self._dec_parameters_constructor()
                    token = self.next_token()
                    if token["token"] == ")":
                        token = self.next_token()
                        if token["token"] == '{':
                            self._variables_block()
                            self._objects_block()
                            self._commands()
                            if token["token"] == '}':
                                self._end_class()
                            else:
                                self._error_message(expected=["}"],founded=token["token"], line=token["line"])
                        else:
                            self._error_message(expected=["{"],founded=token["token"], line=token["line"])
                    else:
                        self._error_message(expected=[")"],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["("],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["constructor"],founded=token["token"], line=token["line"])
        
        def _end_class(self):
            token = self.next_token()
            if token["token"] == "}":
                self._class_block()
            else:
                self._error_message(expected=["}"],founded=token["token"], line=token["line"])
        
        def _main(self):
            token = self.next_token()
            if token["token"] == "main":
                token = self.next_token()
                if token["token"] == "{":
                    self._init_main()
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["main"],founded=token["token"], line=token["line"])
        
        def _init_main(self):
            self._body_blocks()
            self._main_methods()
            token = self.next_token()
            if token["token"] == "}":
                pass
            else:
                self._error_message(expected=["}"],founded=token["token"], line=token["line"])
        
        def _body_blocks(self):
            self._variables_block()
            self._objects_block()
            
        def _main_methods(self):
            token = self.next_token()
            if token["token"] == "methods":
                token = self.next_token()
                if token["token"] == "{":
                    self._main_methods_body()
                    token = self.next_token()
                    if token["token"] == "}":
                        pass
                    else:
                        self._error_message(expected=["}"],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["methods"],founded=token["token"], line=token["line"])
        
        def _main_methods_body(self):
            token = self.next_token()
            if (self._is_TYPE(token))|(token["token"] == 'void'):
                token = self.next_token()
                if token["token"] == 'main':
                    token = self.next_token()
                    if token["token"] == '(':
                        token = self.next_token()
                        if token["token"] == ')':
                            token = self.next_token()
                            if token["token"] == '{':
                                self._method_body()
                                self._methods()
                            else:
                                self._error_message(expected=["{"],founded=token["token"], line=token["line"])
                        else:
                            self._error_message(expected=[")"],founded=token["token"], line=token["line"])
                    else:
                        self._error_message(expected=["("],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["main"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=['int','real','boolean','string','void'],founded=token["token"], line=token["line"])

#BLOCO DE OBJETOS       
        def _objects_block(self):
            token = self.next_token()
            if token["token"] == 'objects':
                token = self.next_token()
                if token['token'] == '{':
                    self._objects()
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["objects"],founded=token["token"], line=token["line"])

        def _objects(self):
            token = self.next_token()
            if self._is_IDE(token):
                self._dec_var()
                self._multiple_objects()
            elif token["token"] == '}':
                pass
            else:
                self._error_message(expected=["IDE","}"],founded=token["token"], line=token["line"])
        
        def _multiple_objects(self):
            token = self.next_token()
            if token["token"] == ',':
                self._dec_var()
                self._multiple_objects()
            elif token["token"] == ';':
                pass
            else:
                self._error_message(expected=[",",";"],founded=token["token"], line=token["line"])

#Corpo de método
        def _method_body(self):
            self._variables_block()
            self._objects_block()
            self._commands_method_body()
#Comandos
        def _commands_method_body(self):
            token = self.next_token()
            if token["token"] == 'return':
                self._return()
            else:
                self._header -= 1
                self._commands()
                self._commands_method_body
        def _commands(self):
            token = self.next_token()
            self._header -= 1
            if token["token"] == 'print':
                self._print_begin()
            elif token["token"] == 'read':
                self._read_begin()
            elif token["token"] == '->':
                self._object_method_access()
                token = self.next_token()
                if token["token"] == ';':
                    pass
                else:
                    self._error_message(expected=[";"],founded=token["token"], line=token["line"])
            elif self._is_IDE(token):
                print('implementar commands->ASSIGMENT, -> OBJECT ATRIBUTE ACESS, -> DOUBLE EXPRESSION dps')
                self._object_atribute_acess() #PENSAR EM COMO IMPLEMENTAR O BLOCO ASSIGMENT, DOUBLE EXPRESSION NESSE CONTEXTO, PROVAVELMENTE MUDAR A GRAMÁTICA NO OBJECT ATRIBUTE ACESS
                token = self.next_token()
                if token["token"] == ';':
                    pass
                else:
                    self._error_message(expected=[";"],founded=token["token"], line=token["line"])
            elif token['token'] == 'if':
                self._if()
            elif token["token"] == 'for':
                self._for_block()
            else:
                self._header -= 1
        def _return(self):
            token = self.next_token()
            #if token[token] <VALUE>
            #else:
            print('implementar return dps')
            pass
#Bloco de métodos
        def _methods_block(self):
            token = self.next_token()
            if token['token'] == 'methods':
                token = self.next_token()
                if token["token"] == '{':
                    self._methods()
                    token = self.next_token()
                    if token["token"] == '}':
                        pass
                    else:
                        self._error_message(expected=["}"],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["methods"],founded=token["token"], line=token["line"])
        
        def _methods(self):
            token = self.next_token()
            if self._is_TYPE(token) | self._is_IDE(token) | (token["token"] == 'void'):
                self._header -= 1
                self._method()
                self._methods()
            else:
                self._header -= 1
        
        def _method(self):
            token = self.next_token()
            if self._is_TYPE(token) | self._is_IDE(token) | (token["token"] == 'void'):
                token = self.next_token()
                if self._is_IDE(token):
                    token = self.next_token()
                    if token['token'] == '(':
                        self._dec_parameters()
                    else:
                        self._error_message(expected=["("],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["IDE"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["IDE","void","int","real","boolean","string"],founded=token["token"], line=token["line"])
        
#declaração de parameters
        def _dec_parameters(self):
            pass