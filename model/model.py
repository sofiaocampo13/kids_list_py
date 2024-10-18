from pydantic import BaseModel

class Kid(BaseModel):
    id: str
    name: str
    age: int
    gender: str

class NodeDE:
    def __init__(self, kid: Kid):
        self.__data = kid
        self.__next = None
        self.__previous = None

    def get_data(self):
        return self.__data

    def set_data(self, data: Kid):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def get_previous(self):
        return self.__previous

    def set_previous(self, node):
        self.__previous = node

class ListDE:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_head(self):
        return self.__head

    def set_head(self, node):
        self.__head = node

    def get_size(self):
        return self.__size

    def set_size(self, size: int):
        self.__size = size

    def add(self, data: Kid):
        if self.__head == None:
            self.__head = NodeDE(data)

    #Método para añadir
    def add(self, data: Kid):
        new_node = NodeDE(data)
        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head
            while temp.get_next() is not None:
                temp = temp.get_next()
            temp.set_next(new_node)
            new_node.set_previous(temp)
        self.__size += 1

    #Método para añadir al inicio
    def add_to_start(self, data: Kid):
        new_node = NodeDE(data)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.set_next(self.__head)
            self.__head.set_previous(new_node)
            self.__head = new_node
        self.__size += 1

    #Método para añadir en posición
    def add_in_position(self, data: Kid, position: int):
        if position == 1 or self.__head is None:
            self.add_to_start(data)
        elif position > self.__size:
            self.add(data)
        else:
            new_node = NodeDE(data)
            temp = self.__head
            pos = 1
            while pos < position - 1:
                temp = temp.get_next()
                pos += 1
            new_node.set_next(temp.get_next())
            if temp.get_next() is not None:
                temp.get_next().set_previous(new_node)
            temp.set_next(new_node)
            new_node.set_previous(temp)
            self.__size += 1

    #Método para invertir
    def invert(self):
        current = self.__head
        previous = None
        while current is not None:
            next_node = current.get_next()
            current.set_next(previous)
            current.set_previous(next_node)
            previous = current
            current = next_node
        self.__head = previous

    #Método para eliminar por ID
    def delete_by_id(self, kid_id: str):
        if self.__head is None:
            print("No se encontró el niño, la lista está vacía")
            return
        current = self.__head
        #Si el nodo a eliminar es la cabeza
        if current.get_data().id == kid_id:
            self.__head = current.get_next()
            if self.__head is not None:
                self.__head.set_previous(None)
            self.__size -= 1
            return
        #Recorrer la lista para encontrar el nodo a eliminar
        while current is not None and current.get_data().id != kid_id:
            current = current.get_next()
        if current is None:
            print("No se encontró el niño")
            return
        # Eliminar el nodo si se encuentra
        previous_node = current.get_previous()
        next_node = current.get_next()
        if previous_node is not None:
            previous_node.set_next(next_node)
        if next_node is not None:
            next_node.set_previous(previous_node)
        self.__size -= 1

    #Método para eliminar por posición
    def delete_by_position(self, position: int):
        if position < 1 or position > self.__size or self.__head is None:
            print("Posición no válida o lista vacía")
            return
        current = self.__head
        if position == 1:
            self.__head = current.get_next()
            if self.__head is not None:
                self.__head.set_previous(None)
            self.__size -= 1
            return
        #Recorrer la lista hasta la posición deseada
        for _ in range(position - 1):
            current = current.get_next()
        previous_node = current.get_previous()
        next_node = current.get_next()
        if previous_node is not None:
            previous_node.set_next(next_node)
        if next_node is not None:
            next_node.set_previous(previous_node)
        self.__size -= 1

    #Método para intercalar por género
    def switch_by_gender(self):
        if self.__head is None:
            print("La lista está vacía")
            return

        boys = []
        girls = []
        current = self.__head
        while current:
            kid_data = current.get_data()
            if kid_data.gender.lower() == 'm':
                boys.append(kid_data)
            elif kid_data.gender.lower() == 'f':
                girls.append(kid_data)
            current = current.get_next()

        merged = []
        boy_count, girl_count = 0, 0
        i, j = 0, 0
        while i < len(boys) and j < len(girls):
            if girl_count <= boy_count:
                merged.append(girls[j])
                j += 1
                girl_count += 1
            else:
                merged.append(boys[i])
                i += 1
                boy_count += 1

        while i < len(boys):
            merged.append(boys[i])
            i += 1

        while j < len(girls):
            merged.append(girls[j])
            j += 1

        current = self.__head
        for kid in merged:
            current.set_data(kid)
            current = current.get_next()

    #Método para intercambiar extremos
    def switch_ends(self):
        if self.__head is None or self.__head.get_next() is None:
            print("La lista está vacía o solo hay un elemento")
            return
        if self.__head.get_next().get_next() is None:
            self.invert()
            return
        #Si hay más de dos nodos
        current = self.__head
        first = self.__head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        current.set_next(first.get_next())
        current.set_previous(None)
        previous.set_next(first)
        first.set_next(None)
        first.set_previous(previous)
        self.__head = current

    #Mostrar los niños en la lista
    def show(self):
        kids_list = []
        temp = self.__head
        while temp is not None:
            kids_list.append(temp.get_data())
            temp = temp.get_next()
        return kids_list
