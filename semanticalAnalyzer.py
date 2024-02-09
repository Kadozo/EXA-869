TIPOS_ELEMENTARES = ["int","real","string","boolean"]
class SemanticalAnalyzer():
    def __init__(self) -> None:
        self.global_scope_table = {"consts":{}, "variables":{},"classes":{}}
        self.actual_type = ""
        self.actual_name = ""
        self.actual_parameter_type = ""
        self.actual_parameter_name = ""
        self.is_actual_vector = False
        self.is_actual_object = False
        self.actual_type_arithmetic_expression = []
        self.actual_scope = []
        self.actual_parameters = {}
            
    def add_declaration_const(self):
        if not self.exists_global(self.actual_name):
            self.global_scope_table["consts"][self.actual_name] = {"name":self.actual_name,
                                                "type":self.actual_type  
                                                }
        else:
            print("Erro de duplicidade")
            
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
            print("Erro de duplicidade")
        self.is_actual_vector = False
            

    def add_local_declaration_object(self): # Escopo 0 = Global, Escopo 1 = Classe, Escopo 2 = Método
        if not self.exists(self.actual_name,len(self.actual_scope)):
            if self.exists_class(self.actual_type,len(self.actual_scope)):
                match len(self.actual_scope):
                    case 1:
                        scope_name_1 = self.actual_scope[0]
                        self.global_scope_table["classes"][scope_name_1]["objects"] = {"name":self.actual_name,
                                    "type":self.actual_type}
                    case 2:
                        scope_name_1 = self.actual_scope[0]
                        scope_name_2 = self.actual_scope[1]
                        self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["objects"] = {"name":self.actual_name,
                                    "type":self.actual_type}
                    case _:
                        pass
            else:
                print("Tipo não declarado" + self.actual_type)
        else:
            print("Erro de duplicidade")
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
                print("tipo no parâmetro não existe")
        else:
            print("Erro de duplicidade em parâmetros")

    def add_type_arithmetic_expression(self,token):
        if token["type"] == "NRO":
            if "." in token["token"]:
                self.actual_type_arithmetic_expression.append("real")
            else:
                self.actual_type_arithmetic_expression.append("int")
    
    def verify_arithmetic_expression_type(self):
        result = all(item == self.actual_type_arithmetic_expression[0] for item in self.actual_type_arithmetic_expression)
        type_result = self.actual_type_arithmetic_expression[0]
        self.verify_arithmetic_expression_type = []
        return result,type_result
    
    def verify_return_type(self):
        if len(self.actual_type_arithmetic_expression) != 0:
            [result,type_result] = self.verify_arithmetic_expression_type()
            if result:
                if type_result == self.search_actual_scope()["type"]:
                    pass #sucesso
                else:
                    print("retorno com tipo incompatível")
            else:
                print("expressão com tipos incompatíveis")
        else:
            print("Está vazio")
