TIPOS_ELEMENTARES = ["int","real","string","boolean"]
class SemanticalAnalyzer():
    def __init__(self) -> None:
        self.actual_line = 0
        self.global_scope_table = {"consts":{}, "variables":{},"classes":{}}
        self.actual_type = ""
        self.actual_name = ""
        self.actual_method_acess_name = ""
        self.actual_parameter_type = ""
        self.actual_parameter_name = ""
        self.is_actual_vector = False
        self.is_actual_object = False
        self.is_actual_object_atributte_acess = False
        self.is_assigment = False
        self.is_return = False
        self.is_arithmetic_expression = False
        self.is_actual_method_acess = False
        self.actual_type_arithmetic_expression = []
        self.actual_parameter_method_acess_parameters = []
        self.actual_type_assigment = []
        self.actual_path_object_atributte_acess = []
        self.actual_path_method_acess = []
        self.actual_scope = []
        self.actual_type_return = []
        self.actual_parameters = {}
        self.actual_result_object_acess = {}
        self.actual_result_method_acess = {}
        self.errors_table = []
        

    def save_error(self,s):
        self.errors_table.append(s)

    def add_declaration_const(self):
        if not self.exists_global(self.actual_name):
            self.global_scope_table["consts"][self.actual_name] = {"name":self.actual_name,
                                                "type":self.actual_type  
                                                }
        else:
            self.save_error("Erro de duplicidade na linha " + self.actual_line)
            
    def add_declaration_global_variable(self,name):
        self.global_scope_table["variables"][name] = {"name":name,
                                            "type":self.actual_type  
                                            }

    def add_declaration_class(self, extends = False, superclass_name = ""):
        self.global_scope_table["classes"][self.actual_name] = {"name":self.actual_name,
                                            "extends":extends,
                                            "superclass_name":superclass_name,
                                            "variables":{},
                                            "objects":{},
                                            "methods":{}  
                                            }
        if extends:
            superclass_result = self.search_class(name=superclass_name)
            self.global_scope_table["classes"][self.actual_name]["variables"] = superclass_result["variables"]
            self.global_scope_table["classes"][self.actual_name]["objects"] = superclass_result["objects"]
            self.global_scope_table["classes"][self.actual_name]["methods"] = superclass_result["methods"]
            
    
    def add_local_declaration_variable(self): # Escopo 0 = Global, Escopo 1 = Classe, Escopo 2 = Método
        if not self.exists(self.actual_name,len(self.actual_scope)):
            match len(self.actual_scope):
                case 0:
                    self.global_scope_table["variables"][self.actual_name] = {"name":self.actual_name,"type":self.actual_type, "is_vector": self.is_actual_vector}
                case 1:
                    scope_name_1 = self.actual_scope[0]
                    self.global_scope_table["classes"][scope_name_1]["variables"][self.actual_name] = {"name":self.actual_name,"type":self.actual_type, "is_vector": self.is_actual_vector}   
                case 2:
                    scope_name_1 = self.actual_scope[0]
                    scope_name_2 = self.actual_scope[1]
                    self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["variables"][self.actual_name] = {"name":self.actual_name,"type":self.actual_type, "is_vector": self.is_actual_vector}  
                case _:
                    print("x")
        else:
            self.save_error("Erro de duplicidade na linha " + self.actual_line)
        self.is_actual_vector = False
            

    def add_local_declaration_object(self): # Escopo 0 = Global, Escopo 1 = Classe, Escopo 2 = Método
        if not self.exists(self.actual_name,len(self.actual_scope)):
            if self.exists_class(self.actual_type,len(self.actual_scope)):
                match len(self.actual_scope):
                    case 1:
                        scope_name_1 = self.actual_scope[0]
                        self.global_scope_table["classes"][scope_name_1]["objects"][self.actual_name] = {"name":self.actual_name,
                                    "type":self.actual_type}
                    case 2:
                        scope_name_1 = self.actual_scope[0]
                        scope_name_2 = self.actual_scope[1]
                        self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["objects"][self.actual_name] = {"name":self.actual_name,
                                    "type":self.actual_type}
                    case _:
                        pass
            else:
                self.save_error("Tipo não declarado " + self.actual_type + " na linha " + self.actual_line)
        else:
            self.save_error("Erro de duplicidade na linha ", self.actual_line)
        self.is_actual_object = False
    
    def add_local_declaration_method(self): # Escopo 0 = Global, Escopo 1 = Classe, Escopo 2 = Método
            scope_name_1 = self.actual_scope[0]
            self.global_scope_table["classes"][scope_name_1]["methods"][self.actual_name] = {"name":self.actual_name,
                                                                                            "type":self.actual_type,
                                                                                            "parameters":self.actual_parameters,
                                                                                            "variables":{},
                                                                                            "objects":{}}
            self.actual_parameters = {}
    def exists_global(self,name):
        return  (name in self.global_scope_table["consts"]) or (name in self.global_scope_table["variables"]) or (name in self.global_scope_table["classes"])
    
    def exists(self,name,scope_number): # Escopo 0 = Global, Escopo 1 = Classe, Escopo 2 = Método
        match scope_number:
            case 0:
                return self.exists_global(name)
            case 1:
                scope_name_1 = self.actual_scope[0]
                return  (name in self.global_scope_table["classes"][scope_name_1]["variables"] or
                        name in self.global_scope_table["classes"][scope_name_1]["objects"] or
                        name in self.global_scope_table["classes"][scope_name_1]["methods"])  
            case 2:
                scope_name_1 = self.actual_scope[0]
                scope_name_2 = self.actual_scope[1]
                return  (name in self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["parameters"] or
                        name in self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["variables"] or 
                        name in self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["objects"])  
            case _:
                print("x")
    
    def search_actual_scope(self):
        match len(self.actual_scope):
            case 1:
                scope_name_1 = self.actual_scope[0]
                return self.global_scope_table["classes"][scope_name_1]
            case 2:
                scope_name_1 = self.actual_scope[0]
                scope_name_2 = self.actual_scope[1]
                return self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]
    
    def search_variables_or_objects(self, name):
        scope_name_1 = self.actual_scope[0]
        scope_name_2 = self.actual_scope[1]
        if name == 'this':
            self.actual_path_object_atributte_acess.pop(0)
            name = self.actual_path_object_atributte_acess[0]
            if name in self.global_scope_table["classes"][scope_name_1]["variables"]:
                return self.global_scope_table["classes"][scope_name_1]["variables"][name] 
            elif name in self.global_scope_table["classes"][scope_name_1]["objects"]:
                return self.global_scope_table["classes"][scope_name_1]["objects"][name]
        else:
            if name in self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["parameters"]:
                return self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["parameters"][name]
            elif name in self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["variables"]:
                return self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["variables"][name]
            elif name in self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["objects"]:
                return self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["objects"][name]
            elif name in self.global_scope_table["classes"][scope_name_1]["variables"]:
                return self.global_scope_table["classes"][scope_name_1]["variables"][name] 
            elif name in self.global_scope_table["classes"][scope_name_1]["objects"]:
                return self.global_scope_table["classes"][scope_name_1]["objects"][name]
            elif name in self.global_scope_table["variables"]:
                return self.global_scope_table["variables"][name]
            elif name in self.global_scope_table["consts"]:
                return self.global_scope_table["consts"][name]
    
    def search_class(self,name):
        if name in self.global_scope_table["classes"]:
            return self.global_scope_table["classes"][name]
        else:
            self.semanticalAnalyzer.save_error("Classe não existe: " + name + " na linha" + self.actual_line)
    def exists_class(self,name,scope_number): # Escopo 0 = Global, Escopo 1 = Classe, Escopo 2 = Método
        match scope_number:
            case 0:
                return self.exists_global(name)
            case 1:
                return  (name in self.global_scope_table["classes"])  
            case 2:
                return  (name in self.global_scope_table["classes"])  
            case _:
                print("x")
    
    def add_scope(self,scope):
        self.actual_scope.append(scope)
    def remove_scope(self):
        self.actual_scope.pop()
    
    def add_parameters(self):
        if not self.actual_parameter_name in self.actual_parameters:
            if self.actual_parameter_type in TIPOS_ELEMENTARES:
                self.actual_parameters[self.actual_parameter_name] = {"name":self.actual_parameter_name,"type":self.actual_parameter_type}
            elif self.exists_class(self.actual_parameter_type,1):
                self.actual_parameters[self.actual_parameter_name] = {"name":self.actual_parameter_name,"type":self.actual_parameter_type}
            else:
                self.semanticalAnalyzer.save_error("Tipo no parâmetro não existe na linha " + self.actual_line)
        else:
            self.save_error("Erro de duplicidade em parâmetros na linha " + self.actual_line)

    def add_type_arithmetic_expression(self,token):
        if token["type"] == "NRO":
            if "." in token["token"]:
                self.actual_type_arithmetic_expression.append("real")
            else:
                self.actual_type_arithmetic_expression.append("int")
        elif token["type"] == "IDE":
            result = self.search_variables_or_objects(token["token"])
            self.actual_type_arithmetic_expression.append(result["type"])
    
    def verify_arithmetic_expression_type(self):
        result = all(item == self.actual_type_arithmetic_expression[0] for item in self.actual_type_arithmetic_expression)
        type_result = self.actual_type_arithmetic_expression[0]
        self.actual_type_arithmetic_expression = []
        self.is_arithmetic_expression = False
        return result,type_result
    
    def save_actual_return(self,void=False):
        if void == True:
            self.actual_type_return.append("void")
        else:
            result = self.search_variables_or_objects(name=self.actual_name)
            self.actual_type_return.append(result["type"])

    def verify_return_type(self):
        if len(self.actual_type_arithmetic_expression) != 0:
            [result,type_result] = self.verify_arithmetic_expression_type()
            if result:
                self.actual_type_return.append(type_result)
                result = all(item == self.actual_type_return[0] for item in self.actual_type_return)
                if result:
                    if self.actual_type_return[0] == self.search_actual_scope()["type"]:
                        pass #sucesso
                    else:
                        self.save_error("Retorno com tipo incompatível na linha " + self.actual_line)
                else:
                    self.save_error("tipos incompatíveis na linha" + self.actual_line)
            else:
                self.save_error("Expressão com tipos incompatíveis na linha " + self.actual_line)
        else:
            if len(self.actual_type_return) > 0:
                result = all(item == self.actual_type_return[0] for item in self.actual_type_return)
                if result:
                    if self.actual_type_return[0] == self.search_actual_scope()["type"]:
                        pass #sucesso
                    else:
                        self.save_error("retorno com tipo incompatível na linha " + self.actual_line)
            else: #retorno vazio
                pass

        self.is_return = False
    
    def save_actual_assigment(self,is_string = False):
        if not self.is_actual_method_acess:
            if not self.is_actual_object_atributte_acess:
                if is_string:
                    self.actual_type_assigment.append('string')
                else:
                    result = self.search_variables_or_objects(name=self.actual_name)
                    self.actual_type_assigment.append(result["type"])
            else:
                    self.actual_type_assigment.append(self.actual_result_object_acess["type"])
                    self.is_actual_object_atributte_acess = False

    def verify_assigment(self):
        if self.is_actual_method_acess:
            self.is_actual_method_acess = False
            self.actual_type_assigment.append(self.actual_result_method_acess["type"])
        result = all(item == self.actual_type_assigment[0] for item in self.actual_type_assigment)
        if result:
            pass #sucesso
        else:
            self.save_error("Tipos incompatíveis na atribuição na linha " + self.actual_line)
        self.is_assigment = False
        self.actual_type_assigment = []
    
    def verify_object_atributte_acess(self):
        is_this = self.actual_path_object_atributte_acess[0] == 'this'
        result = self.search_variables_or_objects(name=self.actual_path_object_atributte_acess[0])
        if not is_this:
            self.actual_path_object_atributte_acess.pop(0)
        if not result["type"] in TIPOS_ELEMENTARES:
            result = self.search_class(result["type"])
            if self.actual_path_object_atributte_acess[0] in result["variables"]:
                self.actual_result_object_acess = result["variables"][self.actual_path_object_atributte_acess[0]]
                if len(self.actual_path_object_atributte_acess) > 1:
                    self.save_error("Acesso de objeto em tipo incompatível na linha" + self.actual_line)
            elif self.actual_path_object_atributte_acess[0] in result["objects"]:
                if len(self.actual_path_object_atributte_acess) > 1:
                    self.verify_object_atributte_acess()
                else:
                    self.actual_result_object_acess = result["objects"][self.actual_path_object_atributte_acess[0]]
            else:
                self.save_error("Atributo inexistente na classe na linha " + self.actual_line)
        else:
            self.save_error("Acesso de objeto em tipo incompatível na linha " + self.actual_line)
    
    def verify_object_method_acess(self):
        aux = []
        result = self.search_variables_or_objects(name=self.actual_path_method_acess[0])
        aux.append(self.actual_path_method_acess.pop(0))
        if not result["type"] in TIPOS_ELEMENTARES:
            result = self.search_class(result["type"])
            if self.actual_path_method_acess[0] in result["methods"]:
                self.actual_result_method_acess = result["methods"][self.actual_path_method_acess[0]]
                if len(self.actual_path_method_acess) > 1:
                    self.save_error("Acesso de objeto em tipo incompatível na linha " + self.actual_line)
                self.actual_path_method_acess = []
            elif self.actual_path_method_acess[0] in result["objects"]:
                result["objects"][self.actual_path_method_acess[0]]
                self.verify_object_atributte_acess()
            else:
                self.save_error("Atributo inexistente na classe na linha " + self.actual_line)
        else:
            self.save_error("Acesso de método em tipo incompatível na linha " + self.actual_line)
        if not self.is_assigment:
            self.is_actual_method_acess = False
    
    def verify_parameters_method(self):
        count = 0
        if len(self.actual_parameter_method_acess_parameters) == len(self.actual_result_method_acess["parameters"]):
            for i in self.actual_parameter_method_acess_parameters:
                result = self.search_variables_or_objects(name=i)
                if result["type"] !=  list(self.actual_result_method_acess["parameters"].values())[count]["type"]:
                    self.save_error("Parametro ", count+1, "com tipo incompatível no método na linha " + self.actual_line)
                count+=1
        else:
            self.save_error("Quantidade de parametros diferente da declaração do método na linha " + self.actual_line)
        
        self.actual_parameter_method_acess_parameters = []
        