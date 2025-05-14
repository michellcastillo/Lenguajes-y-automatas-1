import ply.lex as lex

# Lista de tokens
tokens = (
    'CLASE', 'DEF', 'RETORNAR', 'IDENTIFICADOR', 'NUMERO', 'FLOTANTE',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ', 'LLAVE_DER', 'DOS_PUNTOS', 'COMA',
    'IGUAL', 'PUNTO', 'COMENTARIO', 'TIPO_DATO', 'MAS', 'MENOS', 'MULTIPLICAR', 'DIVIDIR', 
    'PUNTO_Y_COMA', 'PUBLIC', 'PRIVATE', 'STATIC', 'VOID', 'IF', 'ELSE', 'WHILE', 'NEW'
)

# Palabras reservadas
reserved = {
    'class': 'CLASE',
    'def': 'DEF',
    'return': 'RETORNAR',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'static': 'STATIC',
    'void': 'VOID',
    'new': 'NEW',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# Tipos de datos
tipos_datos = {'int', 'float', 'str', 'bool', 'list', 'dict', 'Color'}

# Reglas para tokens simples
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_DOS_PUNTOS = r':'
t_COMA = r','
t_IGUAL = r'='
t_PUNTO = r'\.'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_PUNTO_Y_COMA = r';'

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Check for reserved words
    if t.value in tipos_datos:
        t.type = 'TIPO_DATO'
    return t

def t_COMENTARIO(t):
    r'\/\*[\s\S]*?\*\/|\/\/.*'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
public class Circulo

{

private float radio;

private Color color; //imagina que existe la clase color sonrisa

public void dibujarCirculo()

{

/*

Generar codigo de dibujo del circulo usando el radio y el color de la clase

*/

}

public static void dibujarCirculo(int unRadio, Color unColor)

{

/*

Dibujo el circulo, pero tomo los parametros ya que la clase no esta intanciada

*/

}

}

public void main()

{

Circulo unCirculo = new Circulo(20,Color.BLUE); //Creo una instancia

unCirculo.dibujarCirculo(); //Lo dibuja, un circulo radio 20 y color azul

Circulo.dibujarCirculo(30, Color.RED); //Dibuja un circulo radio 30 y color rojo, sin necesidad de crear una instancia.

}
'''

lexer.input(data)
while tok := lexer.token():
    print(tok)
