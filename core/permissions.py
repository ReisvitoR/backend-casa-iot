from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada que permite:
    - Leitura para todos
    - Escrita apenas para o dono do objeto
    """
    
    def has_permission(self, request, view):
        # Permite leitura para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        # Escrita requer autenticação
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Leitura para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Verifica se o usuário é dono do objeto
        if hasattr(obj, 'usuario'):
            return obj.usuario == request.user
        elif hasattr(obj, 'casa'):
            return obj.casa.usuario == request.user
        elif hasattr(obj, 'comodo'):
            return obj.comodo.casa.usuario == request.user
        
        return False

class IsAuthententicatedOrPublicRead(permissions.BasePermission):
    """
    Permite leitura pública mas requer autenticação para mudanças
    """
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
