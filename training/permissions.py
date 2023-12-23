from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    """
        Права доступа для владельца.

        Владелец имеет право видеть и редактировать свои объекты, а также видеть и редактировать уроки и курсы, если он
        модератор.
    """
    message = "НЕ ХОДИ СЮДА снег башка попадет, можно только ВЛАДЕЛЬЦЕМ"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsModerator(BasePermission):
    """
        Права доступа для модератора.

        Модератор может видеть и редактировать уроки и курсы, но не создавать и не удалять.

    """
    message = "ТЫ не помощник царя сюда нельзя, можно только МОДЕРАТОРАМ "

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
