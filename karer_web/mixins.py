class OwnQuerysetMixin:
    def get_exclude(self, request, obj):
        exclude = super().get_exclude(request, obj) or []
        if request.user.is_superuser:
            return exclude
        if hasattr(self.model, 'karer'):
            return [*exclude, 'karer']
        return exclude
    
    def save_model(self, request, obj, form, change) -> None:
        if request.user.is_superuser:
            return super().save_model(request, obj, form, change)
        if request.user.karer:
            obj.karer = request.user.karer
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs 
        if hasattr(qs.model, 'karer') and request.user.karer:
            return qs.filter(karer=request.user.karer)
        return qs
