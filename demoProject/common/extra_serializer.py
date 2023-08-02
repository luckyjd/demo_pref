def get_extra_fields(model, extra):
    fields = [f.name for f in model._meta.fields]
    if not isinstance(extra, list):
        extra = [extra]
    return fields + extra