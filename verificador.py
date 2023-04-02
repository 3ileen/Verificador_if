import ast

def sentencia_if(expression):
    try:
        # Analizar la sentencia y crear el AST correspondiente
        ast.parse(expression)
        return True
    except SyntaxError:
        return False
    
# ejemplo : "if x > 0:\n    print('x es positivo')"
sentencia = "if x > 0:"
#sentencia = input("Ingresa una sentencia:")
if sentencia_if(sentencia):
    print("La sentencia si pertenece al lenguaje de Python.")
else:
    print("La sentencia no pertenece al lenguaje de Python o esta sintacticamente mal.")
