from semanticalAnalyzer import SemanticalAnalyzer

class SintaxicalAnalyzer():
        def __init__(self,tokens_table,errors_table,filename) -> None:
                self._inputdir = "./Files/"
                self.is_EOF = False
                self._tokens_table = tokens_table
                self._length_tokens_table = len(tokens_table)
                self._errors_table = errors_table
                self._filename = filename
                self._header = 0
                self.semanticalAnalyzer = SemanticalAnalyzer()
        
        def _save_output(self):
            print(self.semanticalAnalyzer.global_scope_table)
            with open(self._inputdir+self._filename[:-4]+"-saída.txt", 'w') as file_writer:
                for element in self._tokens_table:
                    file_writer.write(element)
                    file_writer.write('\n')
                if(len(self._errors_table)>0):
                        file_writer.write('\n')
                        file_writer.write('-----------------TABELA DE ERROS-----------------\n')
                        for element in self._errors_table:
                            file_writer.write('\n')
                            file_writer.write(element)
                else:
                   file_writer.write("Analise Sintatica feita com sucesso!") 
                file_writer.close()

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
        def _is_ART(self,token):
            return token["type"] == "ART" and token["token"] != '++' and token["token"] != '--'
        def _is_REL(self,token):
            return token["type"] == "REL"
        def _is_LOG(self,token):
            return token["type"] == "LOG"
        def _is_ATTRIBUTION(self,token):
            return (self._is_NRO(token)) | (self._is_BOOL(token)) | (self._is_CAC(token))

        def _error_message(self,line:str,expected:[],founded:str):
            self._errors_table.append("Erro na linha " + line + ", no token " + str(self._header) + ", era esperado um dos seguintes tokens: " + str(expected) + " mas foi encontrado: " + founded)
        
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
            self._save_output() 
        
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
## RULES

        def _dec_object_attribute_access(self):
            token = self.next_token()
            if self._is_IDE(token):
                self._dimensions()
                self._end_object_attribute_access()
            else:
                self._error_message(expected=["<IDE>"],founded=token["token"], line=token["line"])
        



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
                self.semanticalAnalyzer.actual_type = token["token"]
                self._const_attribution()
                self._multiple_consts()
                self._consts()
            elif token["token"] == '}':
                pass
            else:
                self._error_message(expected=["}"],founded=token["token"], line=token["line"])

        def _const_attribution(self):
            token = self.next_token()
            if self._is_IDE(token):
                self.semanticalAnalyzer.actual_name = token["token"]
                token = self.next_token()
                if token["token"] == "=":
                    token = self.next_token()
                    if self._is_ATTRIBUTION(token):
                        if token["type"] == "NRO":
                            match self.semanticalAnalyzer.actual_type:
                                case "int":
                                    if not '.' in token["token"]:
                                        self.semanticalAnalyzer.add_declaration_const()
                                        pass #sucesso
                                    else:
                                        print("Incompatibilidade de tipo") #erro de incompatibilidade de tipo
                                case "real":
                                    if '.' in token["token"]:
                                        self.semanticalAnalyzer.add_declaration_const()
                                        pass #sucesso
                                    else:
                                        print("Incompatibilidade de tipo") #erro de incompatibilidade de tipo
                        elif token["type"] == "CAC":
                            if self.semanticalAnalyzer.actual_type == 'string':
                                self.semanticalAnalyzer.add_declaration_const()
                            else:
                                print("Incompatibilidade de tipo")
                    else:
                       self._error_message(expected=["<NRO>",'<CAC>','<BOOL>'],founded=token["token"], line=token["line"]) 
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
                pass
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
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=["variables"],founded=token["token"], line=token["line"])
        
        def _variables(self):
            token = self.next_token()
            if self._is_TYPE(token):
                self.semanticalAnalyzer.actual_type = token["token"]
                self._dec_var()
                self._multiple_variables_line()
                self._variables()
            elif token["token"] == '}':
                pass
            else:
                self._error_message(expected=["}",'int','real','boolean','string'],founded=token["token"], line=token["line"])
        
        def _dec_var(self):
            token = self.next_token()
            if self._is_IDE(token):
                self.semanticalAnalyzer.actual_name = token["token"]
                self._dimensions()
                if not self.semanticalAnalyzer.is_actual_object:
                    self.semanticalAnalyzer.add_local_declaration_variable()
                else:
                    self.semanticalAnalyzer.add_local_declaration_object()
            else:
                self._error_message(expected=["IDE"],founded=token["token"], line=token["line"])
        
        def _dimensions(self):
            token = self.next_token()
            if token["token"] == "[":
                self._size_dimensions()
                token = self.next_token()
                if token["token"] == "]":
                    self.semanticalAnalyzer.is_actual_vector = True
                    self._dimensions()
                else:
                    self._error_message(expected=["]"],founded=token["token"], line=token["line"])
            else:
                self._header -= 1

        def _size_dimensions(self):
            token = self.next_token()
            if self._is_IDE(token) | self._is_NRO(token):
                pass
            else:
                self._error_message(expected=["IDE","NRO"],founded=token["token"], line=token["line"])

        def _multiple_variables_line(self):
            token = self.next_token()
            if token["token"] == ";":
                pass
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
                self.semanticalAnalyzer.actual_name = token["token"]
                self._extends()
            else:
                self._header -= 1
                self._main()
        
        def _extends(self):
            token = self.next_token()
            if token["token"] == "extends":
                token = self.next_token()
                if self._is_IDE(token):
                    self.semanticalAnalyzer.add_declaration_class(extends=True)
                    self._start_class_block()
                else:
                    self._error_message(expected=["IDE"],founded=token["token"], line=token["line"])
            else:
                self._header -= 1
                self.semanticalAnalyzer.add_declaration_class(extends=False)
                self._start_class_block()

        def _start_class_block(self):
            token = self.next_token()
            if token["token"] == "{":
                self.semanticalAnalyzer.add_scope(self.semanticalAnalyzer.actual_name)
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
                self.semanticalAnalyzer.actual_name = token["token"]
                token = self.next_token()
                if token["token"] == "(":
                    self._dec_parameters_constructor()
                    token = self.next_token()
                    if token["token"] == ")":
                        token = self.next_token()
                        if token["token"] == '{':
                            self.semanticalAnalyzer.add_local_declaration_method()
                            self.semanticalAnalyzer.add_scope(self.semanticalAnalyzer.actual_name)
                            self._variables_block()
                            self._objects_block()
                            self._commands()
                            token = self.next_token()
                            if token["token"] == '}':
                                self.semanticalAnalyzer.remove_scope()
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
                self.semanticalAnalyzer.remove_scope()
                self._class_block()
            else:
                self._error_message(expected=["}"],founded=token["token"], line=token["line"])
        
        def _main(self):
            token = self.next_token()
            if token["token"] == "main":
                self.semanticalAnalyzer.actual_name = token["token"]
                token = self.next_token()
                if token["token"] == "{":
                    self.semanticalAnalyzer.add_declaration_class(extends=False)
                    self.semanticalAnalyzer.add_scope(self.semanticalAnalyzer.actual_name)
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
                self.semanticalAnalyzer.remove_scope()
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
                self.semanticalAnalyzer.actual_type = token["token"]
                token = self.next_token()
                if token["token"] == 'main':
                    self.semanticalAnalyzer.actual_name = token["token"]
                    token = self.next_token()
                    if token["token"] == '(':
                        token = self.next_token()
                        if token["token"] == ')':
                            token = self.next_token()
                            if token["token"] == '{':
                                self.semanticalAnalyzer.add_local_declaration_method()
                                self.semanticalAnalyzer.add_scope(self.semanticalAnalyzer.actual_name)
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
                self.semanticalAnalyzer.actual_type = token["token"]
                self.semanticalAnalyzer.is_actual_object = True
                self._dec_var()
                self._multiple_objects()
                self._objects()
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
            self._commands()
            token = self.next_token()
            if token["token"] == 'return':
                self._return()
                token = self.next_token()
                if token["token"] == ';':
                    self.semanticalAnalyzer.verify_return_type()
                    token = self.next_token()
                    if token["token"] == '}':
                        pass
            else:
                self._error_message(expected=['return'], founded=token['token'], line=token["line"])
        def _commands(self):
            token = self.next_token()
            self._header -= 1
            if (token["token"] in ['print','read','if','for']) | self._is_IDE(token):
                self._command()
                self._commands()
            else:
                pass
        
        def _command(self):
            token = self.next_token()
            self._header -= 1
            if token["token"] == 'print':
                self._print_begin()
            elif token["token"] == 'read':
                self._read_begin()
            elif self._is_IDE(token):
                self._object_access_or_assigment() 
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
                pass
            
        def _return(self):
            token = self.next_token()
            if self._is_CAC(token=token) | self._is_NRO(token=token) | (token["token"] == '[') |self._is_IDE(token)| (token["token"] == '!') | (token["token"] == '(')|self._is_BOOL(token):
                self._header -= 1
                self._value()
            else:
                self._header -= 1

#Bloco de atribuição       
        def _object_access_or_assigment(self):
            self._dec_object_attribute_access()
            self._object_access_or_assigment_end()
        
        def _object_access_or_assigment_end(self):
            token = self.next_token()
            if token["token"] == '->':
                self._header -= 1 
                self._object_method_access_end()
            elif token["token"] == '=':
                self._value()
            elif token["token"] in ['++','--']:
                pass
            else:
                self._error_message(expected=['->','=','++','--'], founded=token["token"], line=token["line"])
        
        def _object_method_access_end(self):
            token = self.next_token()
            if token['token'] == '->':
                self._ide_or_constructor()
                token = self.next_token()
                if token["token"] == '(':
                    self._parameters()
                    token = self.next_token()
                    if token["token"] == ')':
                        pass
                    else:
                        self._error_message(expected=[')'], founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=['('], founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=['->'], founded=token["token"], line=token["line"])
            
            
        
        def _parameters(self):
            token = self.next_token()
            if self._is_IDE(token)|self._is_CAC(token=token) | self._is_NRO(token=token) | (token["token"] in ['[','!','('])|self._is_BOOL(token):
                self._header -= 1
                self._value()
                self._mult_parameters()
            else:
                self._header -= 1
        
        def _mult_parameters(self):
            token = self.next_token()
            if token["token"] == ',':
                self._value()
                self._mult_parameters()
            else:
                self._header -= 1
        
        def _object_method_or_object_access_or_part(self):
            token = self.next_token()
            self._header -= 1
            if self._is_IDE(token):
                self._dec_object_attribute_access()
                self._optional_object_method_access()
            else:
                self._error_message(expected=['<IDE>'], founded=token["token"], line=token["line"])
        

        def _value(self):
            token = self.next_token()
            if self._is_NRO(token):
                self.semanticalAnalyzer.add_type_arithmetic_expression(token)
                self._simple_or_double_arithimetic_expression_optional()
            elif self._is_CAC(token):
                pass
            elif token["token"] == '[':
                self._header -= 1
                self._vector_assign_block()
            elif self._is_IDE(token):
                self._header -= 1
                self._init_expression()
            elif token["token"] == "!":
                self._logical_expression_begin()
                self._logical_expression_end() 
            elif token["token"] == '(':
                self._header -= 1
                self._arithimetic_or_logical_expression_with_parentheses()
            elif self._is_BOOL(token):
                pass

        def _simple_or_double_arithimetic_expression_optional(self):
            token = self.next_token()
            if self._is_ART(token):
                self._header -=  1
                self._simple_or_double_arithimetic_expression()
            else:
                self._header -= 1
                pass
        
        def _init_expression(self):
            self._dec_object_attribute_access()
            self._arithimetic_or_logical_expression()
        
        def _arithimetic_or_logical_expression(self):
            token = self.next_token()
            if (token['token'] == '->')|self._is_REL(token)|self._is_LOG(token):
                self._header -= 1
                self._optional_object_method_access()
                self._log_rel_optional()
                self._logical_expression_end()
            elif (token['token'] == '--' )| (token["token"] == '++')| self._is_ART(token):
                self._header -= 1
                self._simple_or_double_arithimetic_expression()
            else:
                self._header -= 1

        
        def _arithimetic_or_logical_expression_with_parentheses(self):
            self._parentheses_begin()
        
        def _parentheses_begin(self):
            token = self.next_token()
            if token["token"] == '(':
                self._expressions()
                self._parentheses_end()
            else: 
                self._error_message(expected=['('], founded=token["token"],line=token['line'])

        def _expressions(self):
            token = self.next_token()
            self._header -= 1
            if token["token"] == '(':
                self._parentheses_begin()
            elif self._is_NRO(token):
                self._simple_expression_without_parentheses()
            elif self._is_BOOL(token):
                self._logical_expression_without_parentheses()
            elif self._is_IDE(token):
                self._simple_or_logical_ide_begin()
            else:
                self._error_message(expected=['(','<NRO>','Boolean','<IDE>'], founded=token["token"],line=token['line'])
        
        def _simple_or_logical_ide_begin(self):
            self._dec_object_attribute_access()
            self._simple_or_logical_ide_end()
        
        def _simple_or_logical_ide_end(self):
            token = self.next_token()
            self._header -= 1
            if self._is_ART(token):
                self._end_expression()
            elif (token["token"] == '->') | self.is_REL(token)|self._is_LOG(token):
                self._optional_object_method_access()
                self._log_rel_optional()
                self._logical_expression_end()
            else:
                self._error_message(expected=['<ART>','->','<REL>','<LOG>'],founded=token["token"],line=token['line'])
        
        def _parentheses_end(self):
            token = self.next_token()
            if token[token] == ')':
                self._expressions_without_parentheses_end()
            else:
                self._error_message(expected=[')'], founded=token["token"],line=token['line'])

        def _expression_without_parentheses_end(self):
            token = self.next_token()
            if self._is_ART(token):
                self._header -= 1
                self._end_expression()
            elif self._is_LOG(token):
                self._logical_expression_begin()
                self._logical_expression_end()
            else:
                self._header -= 1
                pass
        
        def _simple_expression_without_parentheses(self):
            token = self.next_token()
            if self._is_NRO(token):
                self._end_expression()
            else:
                self._error_message(expected=['<NRO>'],founded=token["token"],line=token['line'])
        
        def _logical_expression_without_parentheses(self):
            token = self.next_token()
            if self._is_BOOL(token):
                self._logical_expression_end()
            elif token["token"] == '!':
                self._logical_expression_begin()
                self._logical_expression_end()
            else:
                self._error_message(expected=["Boolean",'!'], founded=token["token"],line=token['line'])
        
        def _vector_assign_block(self):
            token = self.next_token()
            if token["token"] == '[':
                self._elements_assign()
                token = self.next_token()
                if token["token"] == ']':
                    pass
                else:
                    self._error_message(expected=[']'],founded=token["token"],line=token['line'])
            else:
                self._error_message(expected=['['],founded=token["token"],line=token['line'])

        def _elements_assign(self):
           self._element_assign()
           self._multiple_elements_assign()
        
        def _n_dimensions_assign(self):
            token = self.next_token()
            if token["token"] == '[':
                self._elements_assign()
                token = self.next_token()
                if token["token"] == ']':
                    pass
                else:
                    self._error_message(expected=[']'],founded=token["token"],line=token['line'])
            else:
                self._header -= 1
        
        def _multiple_elements_assign(self):
            token = self.next_token()
            if token['token'] == ',':
                self._element_assign()
                self._multiple_elements_assign()
            else:
                self._header -= 1
        
        def _element_assign(self):
            token = self.next_token()
            if self._is_IDE(token):
                pass
            elif self._is_CAC(token):
                pass
            elif self._is_NRO(token):
                pass
            elif token["token"] == '[':
                self._header -= 1
                self._n_dimensions_assign()
            else:
                self._error_message(expected=['[',"<NRO>","<CAC>","<IDE>"],founded=token["token"],line=token['line'])

#Print e Read
        def _print_begin(self):
            token = self.next_token()
            if token["token"] == 'print':
                token = self.next_token()
                if token["token"] == '(':
                    self._print_end()
                else:
                    self._error_message(expected=['('],founded=token["token"],line=token['line'])
            else:
                    self._error_message(expected=['print'],founded=token["token"],line=token['line'])
        
        def _print_end(self):
            self._print_parameter()
            token = self.next_token()
            if token["token"] == ')':
                token = self.next_token()
                if token["token"] == ';':
                    pass
                else:
                    self._error_message(expected=[';'],founded=token["token"],line=token['line'])
            else:
                self._error_message(expected=[')'],founded=token["token"],line=token['line'])

        def _read_begin(self):
            token = self.next_token()
            if token[token] == 'read':
                if token[token] == '(':
                    self._read_end()
                else:
                    self._error_message(expected=['('],founded=token["token"],line=token['line'])
            else:
                    self._error_message(expected=['read'],founded=token["token"],line=token['line'])
        
        def _read_end(self):
            self._dec_object_attribute_access()
            token = self.next_token()
            if token["token"] == ')':
                token = self.next_token()
                if token["token"] == ';':
                    pass
                else:
                    self._error_message(expected=[';'],founded=token["token"],line=token['line'])
            else:
                self._error_message(expected=[')'],founded=token["token"],line=token['line'])

        def _print_parameter(self):
            token = self.next_token()
            if self._is_IDE(token):
                self._header -= 1
                self._dec_object_attribute_access()
            elif self._is_CAC(token):
                pass
            elif self._is_NRO():
                pass
            else:
                self._error_message(expected=['<IDE>','<CAC>','<NRO>'],founded=token["token"],line=token['line'])

#Bloco acesso a atributos e métodos de objetos
        def _multiple_object_attribute_access(self):
            self._dec_var()
            self._end_object_attribute_access()
        
        def _end_object_attribute_access(self):
            token = self.next_token()
            if token['token'] == '.':
                self._multiple_object_attribute_access()
            else:
                self._header -= 1
        
        def _object_method_or_object_access(self):
            self._object_method_or_object_access_or_part()
        
        def _optional_object_method_access(self):
            token = self.next_token()
            self._header -= 1
            if token["token"] == '->':
                self._object_method_access_end()
            else:
                pass
        
        def _ide_or_constructor(self):
            token = self.next_token()
            if token["token"] == 'constructor':
                pass
            elif self._is_IDE(token):
                pass
            else:
                self._error_message(expected=['constructor','<IDE>'], founded=token["token"],line=token["line"])

#Bloco operadores aritméticos
        def _simple_or_double_arithimetic_expression(self):
            token = self.next_token()
            if self._is_ART(token):
                self._header -= 1
                self._end_expression()
            elif token["token"] in ['++','--']:
                pass
            else:
                self._error_message(expected=['<ART>'], founded=token["token"],line=token["line"])

        def _end_expression_optional(self):
            token = self.next_token()
            self._header -= 1
            if self._is_ART(token):
                self._end_expression()
            else:
                pass
        
        def _simple_expression(self):
            token = self.next_token()
            self.header -= 1
            if self._is_NRO(token) | self.is_IDE(token):
                self._part()
                self._end_expression()
            elif token['token'] == '(':
                self._parenthesis_expression()

        def _parenthesis_expression(self):
            token = self.next_token()
            if token['token'] == '(':
                self._simple_expression()
                token = self.next_token()
                if token['token'] == ')':
                    self._end_expression_optional()
                else:
                    self._error_message(expected=[')'], founded=token["token"],line=token["line"])
            else:
                self._error_message(expected=['('], founded=token["token"],line=token["line"])

        def _end_expression(self):
            token = self.next_token()
            if self._is_ART(token):
                self._part_loop()
            else:
                self._error_message(expected=['<ART>'], founded=token["token"],line=token["line"])

        def _part_loop(self):
            token = self.next_token()
            self._header -= 1
            if self._is_NRO(token) | self._is_IDE(token):
                self._part()
                self._end_expression_optional()
            elif token["token"] == '(':
                self._parenthesis_expression()
            else:
                self._error_message(expected=['(','<NRO>','<IDE>'], founded=token["token"],line=token["line"])

        def _part(self):
            token = self.next_token()
            if self._is_NRO(token):
                self.semanticalAnalyzer.add_type_arithmetic_expression(token)
            elif self._is_IDE(token):
                self._header -= 1
                self._object_method_or_object_access_or_part()
            else:
                self._error_message(expected=['<NRO>','<IDE>'], founded=token["token"],line=token["line"])

#Bloco de métodos
        def _methods_block(self):
            token = self.next_token()
            if token['token'] == 'methods':
                token = self.next_token()
                if token["token"] == '{':
                    self._methods()
                    token = self.next_token()
                    if token["token"] == '}':
                        self.semanticalAnalyzer.remove_scope()
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
                self.semanticalAnalyzer.actual_type = token["token"]
                token = self.next_token()
                if self._is_IDE(token):
                    self.semanticalAnalyzer.actual_name = token["token"]
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
            token = self.next_token()
            self._header -= 1
            if self._is_TYPE(token):
                self._variable_param()
                self._mult_dec_parameters()
            elif self._is_IDE(token):
                self._object_param()
                self._mult_dec_parameters()
            elif token["token"] == ')':
                self._end_dec_parameters()
            else:
                self._error_message(expected=["IDE","void","int","real","boolean","string",')'],founded=token["token"], line=token["line"])
        
        def _mult_dec_parameters(self):
            token = self.next_token()
            if token["token"] == ',':
                token = self.next_token()
                if self._is_TYPE(token)| self._is_IDE(token):
                    self.semanticalAnalyzer.actual_parameter_type = token["token"]
                    token = self.next_token()
                    if self._is_IDE(token):
                        self.semanticalAnalyzer.actual_parameter_name = token["token"]
                        self.semanticalAnalyzer.add_parameters()
                        self._mult_dec_parameters()
                    else:
                        self._error_message(expected=["<IDE>"],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["<IDE>","void","int","real","boolean","string"],founded=token["token"], line=token["line"])
            elif token["token"] == ')':
                self._header -= 1
                self._end_dec_parameters()
            else:
                self._error_message(expected=[",",")"],founded=token["token"], line=token["line"])
        
        def _end_dec_parameters(self):
            token = self.next_token()
            if token["token"] == ')':
                token = self.next_token()
                if token["token"] == '{':
                    self.semanticalAnalyzer.add_scope(self.semanticalAnalyzer.actual_name)
                    self.semanticalAnalyzer.add_local_declaration_method()
                    self._method_body()
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=[")"],founded=token["token"], line=token["line"])
#If-else

        def _if(self):
            token = self.next_token()
            if token['token'] == 'if':
                token = self.next_token()
                if token['token'] == '(':
                    self._condition()
                    token = self.next_token()
                    if token['token'] == ')':
                        token = self.next_token()
                        if token['token'] == 'then':
                            token = self.next_token()
                            if token['token'] == '{':
                                self._commands()
                                token = self.next_token()
                                if token['token'] == '}':
                                    self._if_else()
                                else:
                                    self._error_message(expected=["}"],founded=token["token"], line=token["line"])
                            else:
                                self._error_message(expected=["{"],founded=token["token"], line=token["line"])
                        else:
                            self._error_message(expected=["then"],founded=token["token"], line=token["line"])
                    else:
                        self._error_message(expected=[")"],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=["("],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=[")"],founded=token["token"], line=token["line"])
        
        def _if_else(self):
            token = self.next_token()
            if token['token'] == 'else':
                token = self.next_token()
                if token['token'] == '{':
                    self._commands()
                    token = self.next_token()
                    if token['token'] == '}':
                        pass
                else:
                    self._error_message(expected=["{"],founded=token["token"], line=token["line"])
            else:
                self._header -= 1
        
        def _condition(self):
            self._logical_expression()
# Parametros construtor
        def _dec_parameters_constructor(self):
            token = self.next_token()
            self._header -= 1
            if self._is_TYPE(token)| self._is_IDE(token):
                self._mult_param_constructor()
                self._mult_dec_parameters_constructor()
            else:
                pass

        def _variable_param(self):
            token = self.next_token()
            if self._is_TYPE(token):
                self.semanticalAnalyzer.actual_parameter_type = token["token"]
                token = self.next_token()
                if self._is_IDE(token):
                    self.semanticalAnalyzer.actual_parameter_name = token["token"]
                    self.semanticalAnalyzer.add_parameters()
                else:
                    self._error_message(expected=['<IDE>'],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=['int','real','boolean','string'],founded=token["token"], line=token["line"])

        def _object_param(self):
            token = self.next_token()
            if self._is_IDE(token):
                self.semanticalAnalyzer.actual_parameter_type = token["token"]
                token = self.next_token()
                if self._is_IDE(token):
                    self.semanticalAnalyzer.actual_parameter_name = token["token"]
                    self.semanticalAnalyzer.add_parameters()
                else:
                    self._error_message(expected=['<IDE>'],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=['<IDE>'],founded=token["token"], line=token["line"])
        
        def _mult_dec_parameters_constructor(self):
            token = self.next_token()
            if token["token"] == ',':
                self._mult_param_constructor()
                self._mult_dec_parameters_constructor()
            else:
                self._header -= 1
        
        def _mult_param_constructor(self):
            token = self.next_token()
            self._header -= 1
            if self._is_TYPE(token):
                self._variable_param()
            elif self._is_IDE(token):
                self._object_param()
            else:
                self._error_message(expected=['int','real','boolean','string','<IDE>'],founded=token["token"], line=token["line"])
#Bloco for

        def _for_block(self):
            self._begin_for()
            self._for_increment()
            self._end_for()

        def _assignment(self):
            token = self.next_token()
            if token["token"] == '=':
                self._value()
            elif token["token"] in ['--','++']:
                pass
            else:
                self._error_message(expected=['=', '--', '++'],founded=token["token"], line=token["line"])

        def _for_increment(self):
            self._dec_object_attribute_access()
            self._assignment()
        
        def _begin_for(self):
            token = self.next_token()
            if token["token"] == 'for':
                token = self.next_token()
                if token["token"] == '(':
                    self._object_access_or_assigment()
                    token = self.next_token()
                    if token["token"] == ';':
                        self._conditional_expression()
                        token = self.next_token()
                        if token["token"] == ';':
                            pass
                        else:
                            self._error_message(expected=[';'],founded=token["token"], line=token["line"])
                    else:
                        self._error_message(expected=[';'],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=['('],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=['for'],founded=token["token"], line=token["line"])
    
        def _end_for(self):
            token = self.next_token()
            if token["token"] == ')':
                token = self.next_token()
                if token["token"] == '{': 
                    self._commands()
                    token = self.next_token()
                    if token["token"] == '}':
                       pass
                    else:
                        self._error_message(expected=['}'],founded=token["token"], line=token["line"])
                else:
                    self._error_message(expected=['{'],founded=token["token"], line=token["line"])
            else:
                self._error_message(expected=[')'],founded=token["token"], line=token["line"])
        
        def _conditional_expression(self):
            token = self.next_token()
            if self._is_IDE(token) | self._is_CAC(token) | self._is_NRO(token):
                self._header -= 1
                self._relational_expression()
            elif token['token'] == '(':
                self._relational_expression()
                token = self.next_token()
                if token['token'] == ')':
                    pass
                else:
                   self._error_message(expected=[')'],founded=token["token"], line=token["line"]) 
            else:
                self._error_message(expected=['(',',<IDE>','<NRO>','<CAC>'],founded=token["token"], line=token["line"])
#Operadores Relacionais

        def _relational_expression(self):
            self._relational_expression_value()
            token = self.next_token()
            if self._is_REL(token):
                self._relational_expression_value()
            else:
                self._error_message(expected=['<REL>'],founded=token["token"], line=token["line"])

        def _relational_expression_value(self):
            token = self.next_token()
            if self._is_NRO(token):
                pass
            elif self._is_IDE(token):
                self._header -= 1
                self._object_method_or_object_access()
            elif self._is_CAC(token):
                pass
#Operadores lógicos-relacionais

        def _logical_expression(self):
            self._logical_expression_begin()
            self._logical_expression_end()
        
        def _logical_expression_begin(self):
            token = self.next_token()
            if token["token"] == '!':
                self._logical_expression_begin()
            elif token["token"] == '(':
                self._logical_expression()
                token = self.next_token()
                if token["token"] == ')':
                    pass
                else:
                    self._error_message(expected=[')'],founded=token["token"], line=token["line"])
            elif self._is_BOOL(token) | self._is_IDE(token):
                self._header -= 1
                self._logical_expression_value()
            else:
                self._error_message(expected=['!','(','<IDE>'],founded=token["token"], line=token["line"])
        
        def _logical_expression_end(self):
            token = self.next_token()
            if self._is_LOG(token):
                self._logical_expression_begin()
                self._logical_expression_end()
            else:
                self._header -= 1
                pass
        
        def _log_rel_optional(self):
            token = self.next_token()
            if self._is_REL(token):
                self._relational_expression_value()
            else:
                self._header -= 1
                pass
        
        def _logical_expression_value(self):
            token = self.next_token()
            if self._is_BOOL(token):
                pass
            elif self._is_IDE(token):
                self._header -= 1
                self._object_method_or_object_access()
                self._log_rel_optional()
            else:
                self._error_message(expected=['<BOOL>','<IDE>'],founded=token["token"], line=token["line"])
     