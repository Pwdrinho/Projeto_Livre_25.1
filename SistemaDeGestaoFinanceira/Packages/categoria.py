class RegistroDeCategorias:
    _categorias = set()

    @classmethod
    def registrar(cls, categoria: str) -> str:
        categoria_padronizada = categoria.strip().lower().upper()
        cls._categorias.add(categoria_padronizada)
        return categoria_padronizada
    
    @classmethod
    def existe(cls, categoria: str) -> bool:
        return categoria.strip().lower().upper() in cls._categorias
    
    @classmethod
    def listar_categorias(cls) -> list[str]:
        return sorted(cls._categorias)

  
class Categoria: # Abstração para manipulação de categorias
    #Classe para manipulação de categorias de transações financeiras.
    @staticmethod
    def todas() -> list[str]:
        #Retorna todas as categorias registradas.
        return RegistroDeCategorias.listar_categorias()
    
    @staticmethod
    def existe(categoria: str) -> bool:
        #Verifica se uma categoria existe.
        return RegistroDeCategorias.existe(categoria)
    
    @staticmethod
    def registrar(categoria: str) -> str:
        #Registra uma nova categoria.
        return RegistroDeCategorias.registrar(categoria)