class CreateMixin:
    def create(self, **kwargs):
        return self.post(kwargs)


class ReadMixin:
    def read(self, id):
        return self.get(id)


class UpdateMixin:
    def update(self, id, **kwargs):
        return self.put(id, kwargs)


class DeleteMixin:
    def delete(self, id):
        return self.delete(id)