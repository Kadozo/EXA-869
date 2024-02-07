class SemanticalAnalyzer():
    def __init__(self) -> None:
        self.global_scope_table = {"consts":{}, "variables":{},"classes":{}}
            
    def add_declaration_const(self,name, type):
        self.global_scope_table["consts"][name] = {"name":name,
                                            "type":type  
                                            }
            
    def add_declaration_global_variable(self,name, type):
        self.global_scope_table["variables"][name] = {"name":name,
                                            "type":type  
                                            }

    def add_declaration_class(self,name, type, extends = False, superclass_name = ""):
        self.global_scope_table["classes"][name] = {"name":name,
                                            "type":type,
                                            "extends":extends,
                                            "superclass_name":superclass_name,
                                            "variables":{},
                                            "objects":{},
                                            "methods":{"variables":{},
                                                    "objects":{}}  
                                            }
    
    def add_local_declaration_variable(self,name, type,scope_number,scope_name_1,scope_name_2 = ""): # Escopo 0 = Classe, Escopo 1 = Método
        match scope_number:
            case 0:
                self.global_scope_table["classes"][scope_name_1]["variables"] = {"name":name,"type":type}   
            case 1:
                self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["variables"] = {"name":name,"type":type}  
            case _:
                pass
            

    def add_local_declaration_object(self,name, type,scope_number,scope_name_1,scope_name_2 = ""): # Escopo 0 = Classe, Escopo 1 = Método
        match scope_number:
            case 0:
                self.global_scope_table["classes"][scope_name_1]["objects"] = {"name":name,
                            "type":type, 
                            "instantiated":False}
            case 1:
                self.global_scope_table["classes"][scope_name_1]["methods"][scope_name_2]["objects"] = {"name":name,
                            "type":type, 
                            "instantiated":False}
            case _:
                pass
    


a = SemanticalAnalyzer()
